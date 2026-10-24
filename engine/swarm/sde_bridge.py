"""Bridge between the SDE (`src/`) and the swarm (`engine/swarm/`).

 (a) PolicySource  - samples formulas from a trained GFlowNet policy (`runs_sde/<run>/policy.pt`); the Miner feeds them through the
                     same screen (syntax/size, degenerate, duplicate, novelty/TED, frequent-subtree) as every other source.
 (b) load_pool     - reads `pool.json` of an SDE run so its members can be re-evaluated by the swarm's Worker/Auditor (which reuse the SDE's
                     own `src.portfolio` backtest and `src.dsl` evaluator - there is one implementation of that math, see `worker.py`).
 (c) mirror_to_sde - writes every swarm trial into the SDE hash-chained ledger as `kind:"trial", origin:"swarm"` and every audit verdict
                     as `kind:"swarm_audit"`, so SDE tooling sees the same N. NO DOUBLE COUNTING: the swarm's live baseline counts only
                     SDE `trial` lines WITHOUT `origin:"swarm"`, plus its own rows; mirrored lines are therefore counted exactly once
                     on each side, and `global_count()` reports both views and whether they agree. The mirror carries no `ic` field
                     and a distinct `universe`, so `train_gfn` duplicate bookkeeping and `phase3_eval.ledger_trials` ignore it while
                     N_total (what the SDE's DSR uses) includes it.
The mirror is idempotent and resumes from the SDE ledger itself (highest mirrored swarm trial id for this swarm database), under an
flock, so a crash between append and bookkeeping cannot duplicate or lose entries.
"""
from __future__ import annotations

import fcntl
import json
import os
from pathlib import Path
from typing import Optional

from . import REPO_ROOT
from .shared_ledger import SharedLedger, compute_baseline, scan_sde_ledger

RUNS_DIR = Path(REPO_ROOT) / "runs_sde"
SDE_LEDGER = Path(REPO_ROOT) / "src" / "audit" / "ledger.jsonl"


def resolve_run(spec: str, runs_dir: Path = RUNS_DIR) -> Path:
    """`spec` may be a directory, an exact run id (`sp500_s2_20261024`) or a prefix (`sp500_s2`; the newest match wins)."""
    p = Path(spec)
    if p.is_dir() and (p / "policy.pt").exists():
        return p
    cands = sorted(d for d in runs_dir.glob(spec + "*") if d.is_dir() and (d / "policy.pt").exists())
    if not cands:
        raise FileNotFoundError(f"no SDE run with policy.pt matches {spec!r} under {runs_dir}")
    exact = [d for d in cands if d.name == spec]
    return exact[0] if exact else max(cands, key=lambda d: (d / "policy.pt").stat().st_mtime)


def load_pool(run: str | Path, runs_dir: Path = RUNS_DIR) -> list[dict]:
    d = resolve_run(str(run), runs_dir) if not (Path(run) / "pool.json").exists() else Path(run)
    return json.loads((d / "pool.json").read_text())["members"]


class PolicySource:
    """Trained GFlowNet as a proposal source: `sample()` returns one SDE-dialect expression string. Own RNG, CPU, single thread."""

    def __init__(self, run: str | Path, seed: Optional[int] = None, runs_dir: Path = RUNS_DIR):
        import torch
        from src.gflownet.policy import GFlowNetPolicy
        self.run_dir = resolve_run(str(run), runs_dir)
        cfg = json.loads((self.run_dir / "config.json").read_text()) if (self.run_dir / "config.json").exists() else {}
        torch.set_num_threads(1)
        self._torch = torch
        self.policy = GFlowNetPolicy(seed=int(cfg.get("seed", 0)))
        self.policy.load_state_dict(torch.load(self.run_dir / "policy.pt", map_location="cpu"))
        self.policy.eval()
        self.run_id = self.run_dir.name
        self.universe = cfg.get("universe")
        self.gen = torch.Generator().manual_seed(int(seed if seed is not None else cfg.get("seed", 0)) + 9973)
        self.n_sampled = 0

    def sample(self) -> str:
        with self._torch.no_grad():
            expr = self.policy.sample(generator=self.gen)["expr"]
        self.n_sampled += 1
        return expr


# ---------------------------------------------------------------------------------------------------- mirror to the SDE ledger
def _mirror_state(sde_path: str, db_id: str) -> tuple[int, dict]:
    """(highest mirrored swarm trial id for this swarm db, {trial id: latest mirrored (verdict, failed gates)}) read from the SDE ledger.
    The ledger is append-only: a re-audit that changes a verdict is appended as a new `swarm_audit` line that supersedes the older one."""
    last, audited = 0, {}
    if not os.path.exists(sde_path):
        return last, audited
    with open(sde_path, "rb") as f:
        for line in f:
            if b'"origin":"swarm"' not in line:
                continue
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if e.get("swarm_db_id") != db_id:
                continue
            if e.get("kind") == "trial":
                last = max(last, int(e["swarm_trial_id"]))
            elif e.get("kind") == "swarm_audit":
                audited[int(e["swarm_trial_id"])] = (e.get("verdict"), tuple(e.get("failed_gates") or ()))
    return last, audited


def mirror_to_sde(ledger: SharedLedger, sde_path: Optional[str | Path] = None, universe: str = "swarm:sp500") -> dict:
    """Append not-yet-mirrored swarm trials (every row counts, rejects included) and audit verdicts to the SDE ledger. Idempotent."""
    from src.audit.ledger import Ledger
    sde_path = str(sde_path or SDE_LEDGER)
    db_id = ledger.db_id()
    lock = open(sde_path + ".swarm_mirror.lock", "a")
    fcntl.flock(lock, fcntl.LOCK_EX)
    try:
        last, audited = _mirror_state(sde_path, db_id)
        sde = Ledger(sde_path)
        n_new = n_aud = 0
        rows = ledger.conn.execute("SELECT id, ast_hash, canonical, expression, source, status, reject_reason, audit_status, created_utc FROM trials "
                                   "WHERE id>? ORDER BY id", (last,)).fetchall()
        for r in rows:
            sde.append(dict(kind="trial", origin="swarm", universe=universe, run_id=f"swarm:{db_id}", split="search", swarm_db_id=db_id,
                            swarm_trial_id=int(r["id"]), ast=r["canonical"] or r["expression"], ast_hash=r["ast_hash"] or None,
                            source=r["source"], status=r["status"], reject_reason=r["reject_reason"] or None))
            n_new += 1
        for r in ledger.conn.execute("SELECT id, ast_hash, audit_status, audit_json FROM trials WHERE audit_status IS NOT NULL ORDER BY id"):
            a = json.loads(r["audit_json"] or "{}")
            if audited.get(int(r["id"])) == (r["audit_status"], tuple(a.get("failed_gates") or ())):
                continue
            sde.append(dict(kind="swarm_audit", origin="swarm", swarm_db_id=db_id, swarm_trial_id=int(r["id"]), ast_hash=r["ast_hash"],
                            verdict=r["audit_status"], failed_gates=a.get("failed_gates"), n_trials_at_audit=a.get("n_trials_at_audit")))
            n_aud += 1
        return {"mirrored_trials": n_new, "mirrored_audits": n_aud, "sde_ledger": sde_path}
    finally:
        fcntl.flock(lock, fcntl.LOCK_UN)
        lock.close()


def global_count(ledger: SharedLedger, sde_path: Optional[str | Path] = None, engine_state: Optional[str] = None) -> dict:
    """The one global N_trials from both sides. `in_sync` is True when the swarm view (engine + SDE-own + swarm rows) equals the SDE view
    (engine + every SDE `trial` line incl. mirrored ones) - i.e. every swarm row is mirrored exactly once."""
    sde_path = str(sde_path or SDE_LEDGER)
    b = compute_baseline(engine_state, sde_path)
    sc = scan_sde_ledger(sde_path)
    swarm_rows = ledger.n_swarm_trials()
    swarm_view = b["engine_n"] + b["sde_n"] + swarm_rows
    sde_view = b["engine_n"] + sc["sde_n"] + sc["swarm_mirrored_n"]
    return {"engine_n": b["engine_n"], "sde_own_n": sc["sde_n"], "swarm_rows": swarm_rows, "swarm_mirrored_in_sde": sc["swarm_mirrored_n"],
            "n_global_swarm_view": swarm_view, "n_global_sde_view": sde_view, "ledger_n_trials": ledger.n_trials(),
            "in_sync": swarm_view == sde_view, "unmirrored": swarm_rows - sc["swarm_mirrored_n"]}
