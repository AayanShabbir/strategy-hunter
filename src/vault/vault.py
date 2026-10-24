"""Single-use vault for the sealed 2021+ holdout (research only; no trading, no broker).

Ideas reused from engine/hunt_engine/vault.py + vault_test.py (read, not modified): the vault gets ONE look per candidate and a
failure is final; the look is recorded under a lock BEFORE results can be used; only gauntlet survivors may open it. Added here:
  * candidates are pre-registered (hash of the canonical spec, the manifest hash they commit to, and the pass rule) in the log first;
  * only candidates whose every AST hash is APPROVED by the swarm auditor (data/ledger/trials.db, audit_status) may open it;
  * a GLOBAL cap on total looks (default 3, src/vault/vault_config.json); cap edits are logged and visible;
  * an append-only, hash-chained audit log (src/audit/ledger.Ledger format) src/vault/vault_log.jsonl, git-tracked so every look is a commit.
A look is consumed when the `open` entry is written, before the sealed panel is read: an evaluator that crashes still used its look.
Refusals are logged and do not consume a look. Nothing here runs unless someone calls Vault.open(); building the data never evaluates it."""
from __future__ import annotations
import contextlib, fcntl, hashlib, json, os, sqlite3
from pathlib import Path
from typing import Callable, Optional
from src.audit.ledger import Ledger
from src.data import guard
from src.vault import sealed_data as SD

ROOT = guard.ROOT
LOG_PATH = ROOT / "src" / "vault" / "vault_log.jsonl"
CONFIG_PATH = ROOT / "src" / "vault" / "vault_config.json"
TRIALS_DB = ROOT / "data" / "ledger" / "trials.db"
RULE_ID = "default_v1"


class VaultRefused(Exception):
    pass


def canonical_spec(spec: dict) -> dict:
    """kind 'formula': {expr, sign}; kind 'pool': {members:[{expr, sign}], combiner:'equal'}. Expressions are canonicalised through the DSL parser."""
    from src.dsl.grammar import ast_hash, parse_expr
    def one(m): return {"expr": parse_expr(m["expr"]).canonical(), "ast_hash": ast_hash(parse_expr(m["expr"])), "sign": int(m.get("sign", 1))}
    if spec.get("kind") == "formula": return {"kind": "formula", **one(spec)}
    if spec.get("kind") == "pool":
        ms = sorted((one(m) for m in spec["members"]), key=lambda x: (x["ast_hash"], x["sign"]))
        return {"kind": "pool", "members": ms, "combiner": spec.get("combiner", "equal")}
    raise ValueError("spec.kind must be 'formula' or 'pool'")


def spec_hash(spec: dict) -> str:
    return hashlib.sha256(json.dumps(canonical_spec(spec), sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ast_hashes(spec: dict) -> list:
    c = canonical_spec(spec)
    return [c["ast_hash"]] if c["kind"] == "formula" else [m["ast_hash"] for m in c["members"]]


def swarm_approved(hashes: list, db_path=TRIALS_DB) -> tuple:
    """(ok, detail): every AST hash has at least one trial with audit_status='APPROVED' in the swarm's shared trial DB (opened read-only)."""
    if not Path(db_path).exists(): return False, f"swarm trial DB not found: {db_path}"
    c = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        missing = [h for h in hashes if not c.execute("SELECT 1 FROM trials WHERE ast_hash=? AND audit_status='APPROVED' LIMIT 1", (h,)).fetchone()]
    finally: c.close()
    return (not missing, "ok" if not missing else f"not APPROVED by the swarm auditor: {[m[:12] for m in missing]}")


class Vault:
    def __init__(self, log_path=LOG_PATH, config_path=CONFIG_PATH, sealed_dir=None, manifest_path=SD.MANIFEST,
                 auditor_check: Optional[Callable[[list], tuple]] = None):
        self.log = Ledger(log_path); self.config_path = Path(config_path); self.sealed_dir = sealed_dir; self.manifest_path = Path(manifest_path)
        self.auditor_check = auditor_check or (lambda hs: swarm_approved(hs))
        self.lock_path = str(log_path) + ".lock"

    # ---- log helpers
    def entries(self) -> list: return list(self.log.entries())
    def verify_log(self): return self.log.verify()

    @contextlib.contextmanager
    def _lock(self):
        fd = os.open(self.lock_path, os.O_CREAT | os.O_RDWR)
        try: fcntl.flock(fd, fcntl.LOCK_EX); yield
        finally: fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)

    def manifest_sha(self) -> str: return SD.sha256_file(self.manifest_path)

    def _config(self) -> dict:
        raw = self.config_path.read_bytes(); cfg = json.loads(raw); cfg["_sha"] = hashlib.sha256(raw).hexdigest()
        if not isinstance(cfg.get("max_looks"), int) or cfg["max_looks"] < 0: raise VaultRefused("vault_config.json: max_looks must be a non-negative integer")
        return cfg

    def cap(self) -> int:
        """Effective cap. If the committed config file changed since the last logged value, log the change first (never silent)."""
        cfg = self._config(); last = [e for e in self.entries() if e.get("kind") == "config"]
        if not last or last[-1]["config_sha"] != cfg["_sha"]:
            self.log.append({"kind": "config", "max_looks": cfg["max_looks"], "config_sha": cfg["_sha"],
                             "previous_max_looks": last[-1]["max_looks"] if last else None})
        return cfg["max_looks"]

    def looks_used(self) -> int: return sum(1 for e in self.entries() if e.get("kind") == "open")

    def status(self) -> dict:
        ok, n, msg = self.verify_log(); return {"log_ok": ok, "entries": n, "msg": msg, "looks_used": self.looks_used(), "cap": self.cap(),
                                                "preregistered": len({e["spec_hash"] for e in self.entries() if e.get("kind") == "preregister"})}

    # ---- pre-registration
    def preregister(self, spec: dict, note: str = "", rule_id: str = RULE_ID) -> dict:
        """Log the candidate (and the manifest it commits to) BEFORE any look. Idempotent per spec hash."""
        h = spec_hash(spec)
        with self._lock():
            for e in self.entries():
                if e.get("kind") == "preregister" and e["spec_hash"] == h: return e
            return self.log.append({"kind": "preregister", "spec_hash": h, "spec": canonical_spec(spec), "ast_hashes": ast_hashes(spec),
                                    "manifest_sha256": self.manifest_sha(), "rule_id": rule_id, "note": note})

    # ---- the single look
    def _refuse(self, h: str, reason: str):
        self.log.append({"kind": "refused", "spec_hash": h, "reason": reason}); raise VaultRefused(reason)

    def open(self, spec: dict, evaluator: Optional[Callable] = None) -> dict:
        """Evaluate `spec` on the sealed panel exactly once. `evaluator(panel, spec) -> dict` (default: default_evaluator)."""
        h = spec_hash(spec)
        with self._lock():
            ok, n, msg = self.verify_log()
            if not ok: raise VaultRefused(f"vault log failed verification: {msg}")
            cap = self.cap(); es = self.entries()
            pre = next((e for e in es if e.get("kind") == "preregister" and e["spec_hash"] == h), None)
            if pre is None: self._refuse(h, "not pre-registered")
            if pre["manifest_sha256"] != self.manifest_sha(): self._refuse(h, "pre-registration commits to a different sealed manifest")
            if any(e.get("kind") == "open" and e["spec_hash"] == h for e in es): self._refuse(h, "already opened: one look per candidate, a failure is final")
            used = sum(1 for e in es if e.get("kind") == "open")
            if used >= cap: self._refuse(h, f"global cap reached: {used} of {cap} looks used")
            good, detail = self.auditor_check(pre["ast_hashes"])
            if not good: self._refuse(h, detail)
            mok, mmsg = SD.verify_manifest(self.sealed_dir, self.manifest_path)
            if not mok: self._refuse(h, f"sealed data does not match its manifest: {mmsg}")
            self.log.append({"kind": "open", "spec_hash": h, "look_no": used + 1, "cap": cap, "manifest_sha256": pre["manifest_sha256"], "rule_id": pre["rule_id"]})
        try:
            panel = SD.load_sealed_panel(self.sealed_dir)
            res = (evaluator or default_evaluator)(panel, canonical_spec(spec))
        except BaseException as e:                       # the look stays consumed
            self.log.append({"kind": "error", "spec_hash": h, "error": f"{type(e).__name__}: {e}"[:500]}); raise
        self.log.append({"kind": "result", "spec_hash": h, "result": res})
        return res


def default_evaluator(panel, spec: dict, cost_bps: float = 5.0) -> dict:
    """Rule `default_v1`: PASS iff the long-short book's net Sharpe > 0 AND the long-only/flat versions beat the equal-weight benchmark
    (excess Sharpe > 0 for both). Scored on rows >= 2021-01-01 only; the earlier rows are warm-up."""
    from src.portfolio.deployability import long_flat_check
    kw = {"expr": spec["expr"], "sign": spec["sign"]} if spec["kind"] == "formula" else {"pool": spec["members"]}
    r = long_flat_check(panel, max_date=None, cost_bps=cost_bps, eval_from_idx=panel.eval_start_idx, **kw)
    r["rule_id"] = RULE_ID; r["PASS"] = bool(r["long_short"]["sharpe"] > 0 and r["survives"])
    return r
