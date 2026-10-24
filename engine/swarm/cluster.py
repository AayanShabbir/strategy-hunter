"""Swarm coordinator: launches the worker processes and runs the Miner / Auditor / Trader / Publisher loop hands-free.

    Swarm(SwarmConfig(workers=4, max_trials=300)).run()        # bounded: stops after 300 NEW evaluated+audited formulas
    Swarm(SwarmConfig(workers=4, continuous=True)).run()       # continuous: until SIGINT/SIGTERM or the STOP file appears

Shutdown is always clean: the stop event is set, workers finish the formula in hand (or release it), are joined with a timeout and
terminated only if they ignore it; workers also exit by themselves if this process dies (parent-pid watch), so there are no orphans.
Workers are `spawn`ed (no forked SQLite connections). The coordinator never blocks on the LLM.
"""
from __future__ import annotations

import json
import multiprocessing as mp
import os
import signal
import time
from dataclasses import dataclass, field
from typing import Optional

from . import DATA_DIR, DEFAULT_DB
from .auditor import AuditConfig, Auditor
from .costs import ImpactModel
from .data import build_search_panel, synthetic_panel
from .llm import make_backend
from .miner import Miner
from .shared_ledger import SharedLedger, scan_sde_ledger
from .signing import DEFAULT_KEY_DIR, KeyStore
from .trader import Trader
from .worker import worker_main


@dataclass
class SwarmConfig:
    workers: int = 4
    db: str = DEFAULT_DB
    max_trials: Optional[int] = 200          # bounded run: stop after this many NEW tasks were evaluated (None => continuous)
    max_seconds: Optional[float] = None
    continuous: bool = False
    llm: str = "none"                        # none | mailbox | openai
    seed: int = 0
    batch: int = 50                          # tasks generated per refill
    low_water: int = 40                      # refill when fewer than this many are pending
    audit_min_batch: int = 20                # audit when this many evaluated formulas are waiting (and at the end)
    audit_cfg: AuditConfig = field(default_factory=AuditConfig)
    publish: bool = True
    tearsheet: bool = True
    mlflow: bool = True
    panel_spec: Optional[dict] = None        # synthetic panel (tests); None => real S&P 500 search window
    tick_s: float = 0.5
    join_timeout_s: float = 20.0
    llm_timeout_s: float = 600.0
    baseline: Optional[dict] = None          # pin the baseline (tests); None => read LIVE at every run start and before every audit
    stop_file: Optional[str] = None
    # ---- SDE connection (all off by default; `hunt swarm-start --sde-policy` turns them on)
    dsl: str = "sde"                         # sde | ext | mixed   (ext = the opt-in blueprint operator set, see dsl_ext.py)
    sde_policy: Optional[str] = None         # run id / prefix / dir of a trained GFlowNet (runs_sde/<run>/policy.pt)
    policy_share: float = 0.5                # share of each generator batch drawn from the policy
    sde_pool: Optional[str] = None           # run whose pool.json members are proposed once (source 'sde_pool')
    sde_ledger: Optional[str] = None         # SDE hash-chained ledger (None => src/audit/ledger.jsonl)
    mirror: bool = False                     # write swarm trials/verdicts into the SDE ledger (shared N, no double count)
    # ---- blueprint features (opt-in so the default stays the audited original behaviour)
    signing: bool = False                    # Ed25519-signed task/result/verdict bundles
    key_dir: Optional[str] = None
    impact: bool = False                     # square-root market-impact cost on top of the flat 5 bp
    impact_eta: float = 1.0
    impact_aum: float = 50e6
    allocation: str = "mvo"                  # trader weights: mvo | erc | equal
    redis: Optional[str] = None              # None | "embedded" (private redis-server, fakeredis fallback) | redis://host:port/db
    duckdb_path: Optional[str] = None        # DuckDB analytics mirror


class Swarm:
    def __init__(self, cfg: SwarmConfig):
        self.cfg = cfg
        self.ledger = SharedLedger(cfg.db)
        self.stop_file = cfg.stop_file or os.path.join(DATA_DIR, "STOP")
        self.procs: list[mp.Process] = []
        self.ctx = mp.get_context("spawn")
        self.stop_event = self.ctx.Event()
        self._signalled = False
        self.report: dict = {}

    # ------------------------------------------------------------------ lifecycle
    def _done_count(self) -> int:
        b = self.ledger.counts()["by_status"]
        return b.get("EVALUATED", 0) + b.get("ERROR", 0)

    def _panel(self):
        return synthetic_panel(**self.cfg.panel_spec) if self.cfg.panel_spec else build_search_panel()

    def _impact(self) -> ImpactModel:
        return ImpactModel(eta=self.cfg.impact_eta, aum=self.cfg.impact_aum)

    _redis_url: Optional[str] = None

    def _spawn_workers(self) -> None:
        for i in range(self.cfg.workers):
            p = self.ctx.Process(target=worker_main, name=f"swarm-worker-{i}", daemon=True,
                                 args=(self.cfg.db, f"worker_{os.getpid()}_{i}", self.stop_event, os.getpid(), None, None, self.cfg.panel_spec,
                                       self._impact().asdict() if self.cfg.impact else None, (self.cfg.key_dir or DEFAULT_KEY_DIR) if self.cfg.signing else None,
                                       self._redis_url, "swarm"))
            p.start()
            self.procs.append(p)

    def _install_signals(self):
        def h(signum, _frm):
            self._signalled = True
        self._old = {s: signal.signal(s, h) for s in (signal.SIGINT, signal.SIGTERM)}

    def _restore_signals(self):
        for s, hnd in getattr(self, "_old", {}).items():
            signal.signal(s, hnd)

    def shutdown(self) -> dict:
        """Stop workers and return their exit info. Idempotent."""
        self.stop_event.set()
        t_end = time.time() + self.cfg.join_timeout_s
        for p in self.procs:
            p.join(max(0.0, t_end - time.time()))
        killed = 0
        for p in self.procs:
            if p.is_alive():
                p.terminate()
                p.join(5)
                if p.is_alive():
                    p.kill()
                    p.join(5)
                killed += 1
        # hand back anything still leased to a dead worker (the lease expiry would do it too, this is just faster)
        self.ledger.conn.execute("PRAGMA busy_timeout=60000")
        with self.ledger._tx() as c:
            c.execute("UPDATE trials SET status='PENDING', lease_owner=NULL, lease_until=NULL WHERE status='RUNNING' AND lease_owner LIKE ?",
                      (f"worker_{os.getpid()}_%",))
        alive = [p.pid for p in self.procs if p.is_alive()]
        return {"workers": len(self.procs), "force_terminated": killed, "still_alive": alive}

    # ------------------------------------------------------------------ main loop
    def run(self) -> dict:
        cfg, led = self.cfg, self.ledger
        t0 = time.time()
        # N baseline = engine N + SDE ledger trials, read LIVE now (never a frozen number); refreshed again before every audit
        baseline = led.refresh_baseline(sde_ledger=cfg.sde_ledger, baseline=cfg.baseline)
        keystore = KeyStore(cfg.key_dir) if cfg.signing else None
        redis_srv, coord = None, None
        if cfg.redis:
            from .redis_coord import Coordinator, EmbeddedRedis
            if cfg.redis in ("embedded", "auto"):
                redis_srv = EmbeddedRedis()
                self._redis_url = redis_srv.url
            else:
                self._redis_url = cfg.redis
            coord = Coordinator(self._redis_url, node="coordinator")
        analytics = None
        if cfg.duckdb_path:
            from .analytics import Analytics
            analytics = Analytics(cfg.duckdb_path)
        panel = self._panel()
        led.set_meta("calendar", panel.calendar())
        n_start = led.n_trials()
        eval0 = self._done_count()
        policy = None
        if cfg.sde_policy:
            from .sde_bridge import PolicySource
            policy = PolicySource(cfg.sde_policy, seed=cfg.seed)
        sde_seen = scan_sde_ledger(baseline["sde_ledger"], want_hashes=True)["hashes"] if baseline.get("sde_ledger") and (policy or cfg.sde_pool) else None
        miner = Miner(led, seed=cfg.seed, llm=make_backend(cfg.llm, **({"timeout_s": cfg.llm_timeout_s} if cfg.llm == "mailbox" else {})),
                      dsl=cfg.dsl, policy=policy, policy_share=cfg.policy_share, sde_seen=sde_seen, keystore=keystore, coordinator=coord)
        auditor = Auditor(led, cfg.audit_cfg, keystore=keystore, coordinator=coord)
        trader = Trader.from_panel(led, panel, allocation=cfg.allocation, keystore=keystore)
        mirror_stats = {"mirrored_trials": 0, "mirrored_audits": 0}
        last_sync = 0.0

        def housekeeping(force: bool = False) -> None:
            nonlocal last_sync
            if not force and time.time() - last_sync < 5.0:
                return
            last_sync = time.time()
            if coord is not None:
                coord.heartbeat("coordinator", f"n={led.n_trials()}")
                drift = coord.reconcile_n(led.n_swarm_trials())
                if drift:
                    led.log_event("cluster", "redis_n_drift", {"drift": drift})
                coord.resync([r[0] for r in led.conn.execute("SELECT id FROM trials WHERE status='PENDING' ORDER BY id")])
            if cfg.mirror:
                from .sde_bridge import mirror_to_sde
                s = mirror_to_sde(led, cfg.sde_ledger)
                mirror_stats["mirrored_trials"] += s["mirrored_trials"]
                mirror_stats["mirrored_audits"] += s["mirrored_audits"]
            if analytics is not None:
                analytics.sync(led)
        target = None if (cfg.continuous or cfg.max_trials is None) else cfg.max_trials
        issued = 0                                  # NEW tasks issued by this run
        published: list = []
        led.log_event("cluster", "start", {"workers": cfg.workers, "target": target, "llm": cfg.llm, "n_trials_at_start": n_start})
        self._install_signals()
        if os.path.exists(self.stop_file):                  # a STOP file left by an earlier run must not abort this one
            os.remove(self.stop_file)
        reason = "completed"
        try:
            self._spawn_workers()
            if cfg.sde_pool or (policy is not None and cfg.sde_pool is None):
                from .sde_bridge import load_pool
                imp = miner.import_sde_pool(load_pool(cfg.sde_pool or cfg.sde_policy), limit=target)
                issued += len(imp)
            while True:
                housekeeping()
                if self._signalled:
                    reason = "signal"
                    break
                if os.path.exists(self.stop_file):
                    reason = "stop_file"
                    break
                if cfg.max_seconds and time.time() - t0 > cfg.max_seconds:
                    reason = "max_seconds"
                    break
                if not any(p.is_alive() for p in self.procs):
                    reason = "all_workers_died"
                    break
                # --- Miner: keep the queue filled; LLM answers are folded in whenever they arrive
                if miner.llm is not None:
                    new = miner.ingest_llm()
                    issued += len(new)
                    miner.request_llm()
                    for rid in getattr(miner.llm, "overdue", lambda: [])():
                        led.log_event("miner", "llm_overdue", {"id": rid})
                if led.pending_count() < cfg.low_water and (target is None or issued < target):
                    n = cfg.batch if target is None else min(cfg.batch, target - issued)
                    issued += len(miner.propose_batch(n, max_attempts=max(n * 40, 400)))
                # --- Auditor -> Trader -> Publisher
                waiting = len(led.evaluated_unaudited(cfg.audit_min_batch))
                drained = led.pending_count() == 0 and led.counts()["by_status"].get("RUNNING", 0) == 0
                if waiting >= cfg.audit_min_batch or (waiting > 0 and drained):
                    auditor.audit_pending()
                    trader.run_once()
                    if cfg.publish:
                        published += self._publish()
                if target is not None and issued >= target and drained and not led.evaluated_unaudited(1):
                    break
                time.sleep(cfg.tick_s)
        finally:
            info = self.shutdown()
            self._restore_signals()
        led.maybe_refresh_baseline(0.0)
        # final pass (also after a signal: whatever finished gets audited)
        if led.evaluated_unaudited(1):
            auditor.audit_pending()
            trader.run_once()
            if cfg.publish:
                published += self._publish()
        housekeeping(force=True)
        glob = None
        if cfg.mirror:
            from .sde_bridge import global_count
            glob = global_count(led, cfg.sde_ledger, baseline.get("engine_state"))
        if redis_srv is not None:
            redis_srv.stop()
        if analytics is not None:
            analytics.close()
        c = led.counts()
        self.report = {
            "baseline": {k: baseline.get(k) for k in ("engine_n", "sde_n", "swarm_mirrored_in_sde_ledger", "read_utc", "live")},
            "baseline_at_end": {k: (led.get_meta("baseline") or {}).get(k) for k in ("engine_n", "sde_n", "read_utc")},
            "global_count": glob, "mirror": mirror_stats if cfg.mirror else None, "allocation": led.get_meta("allocation"),
            "redis": None if not cfg.redis else {"kind": redis_srv.kind if redis_srv else "external", "ok": coord.ok if coord else None},
            "sources": miner.stats.get("by_source"), "degenerate_rejected": miner.stats.get("degenerate", 0),
            "stop_reason": reason, "elapsed_s": round(time.time() - t0, 1), "new_tasks_issued": issued,
            "n_trials_start": n_start, "n_trials_end": led.n_trials(), "baseline_n": led.baseline_n(), "ledger_counts": c,
            "new_evaluated_or_error": self._done_count() - eval0,
            "audit": led.conn.execute("SELECT audit_status, COUNT(*) FROM trials WHERE audit_status IS NOT NULL GROUP BY audit_status").fetchall(),
            "survivors_in_pool": len(led.pool_members()), "published": [m["ast_hash"] for m in published],
            "miner": miner.stats, "workers": info,
        }
        self.report["audit"] = {r[0]: r[1] for r in self.report["audit"]}
        led.log_event("cluster", "stop", {k: v for k, v in self.report.items() if k != "miner"})
        return self.report

    def _publish(self) -> list[dict]:
        import sys
        eng = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if eng not in sys.path:
            sys.path.insert(0, eng)
        from vault.publisher import publish_pool
        return publish_pool(self.ledger, tearsheet=self.cfg.tearsheet, mlflow_uri=None if self.cfg.mlflow else "disabled")


def status(db: Optional[str] = None) -> dict:
    led = SharedLedger(db or DEFAULT_DB)
    return {"db": led.path if hasattr(led, "path") else (db or DEFAULT_DB), "n_trials": led.n_trials(), "baseline_n": led.baseline_n(),
            "swarm_trials": led.n_swarm_trials(), "counts": led.counts(),
            "audit": {r[0]: r[1] for r in led.conn.execute("SELECT audit_status, COUNT(*) FROM trials WHERE audit_status IS NOT NULL GROUP BY audit_status")},
            "pool": [{"hash": m["ast_hash"], "expression": m["canonical"], "delta_ic": m["delta_ic"]} for m in led.pool_members()],
            "recent_events": [{"ts": e["ts"], "agent": e["agent"], "kind": e["kind"]} for e in led.events(limit=8)]}
