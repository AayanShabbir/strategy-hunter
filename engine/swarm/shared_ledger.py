"""Shared trial ledger for the swarm: one SQLite database in WAL mode that every process (miner, workers, auditor,
trader, publisher) opens independently. SQLite's write lock (BEGIN IMMEDIATE) makes every counter update atomic across
processes, so N_trials is exact no matter how many workers run. (Redis / DuckDB are optional in the blueprint; they are not
needed on one box and are not used - see docs/swarm.md.)

N_trials  =  baseline_engine_N + baseline_sde_N  +  number of rows in `trials`.
  * every proposal gets a row BEFORE it is evaluated, whatever its fate (syntax error, near-duplicate, rejected by the
    novelty filter, evaluated), so the count can only be conservative;
  * the baseline offset (existing engine ledger N and the SDE ledger trial count, read read-only at creation) makes
    the swarm's deflated-Sharpe hurdle at least as strict as everything searched before it.

Lifecycle of a row (`status`): PENDING -> RUNNING -> EVALUATED | ERROR, or terminal REJECTED_* at proposal time.
`audit_status`: NULL -> APPROVED | REJECTED. Approved formulas may enter the `pool` (Trader).
Nothing here deletes trial rows.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
import zlib
from typing import Any, Iterable, Optional

import numpy as np

from . import DEFAULT_DB, REPO_ROOT

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE IF NOT EXISTS trials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ast_hash TEXT, expression TEXT, canonical TEXT, ast_json TEXT,
  source TEXT, agent_id TEXT, persona TEXT, parent_hash TEXT, hypothesis TEXT,
  created_utc TEXT, status TEXT NOT NULL, reject_reason TEXT, reject_detail TEXT,
  lease_owner TEXT, lease_until REAL, attempts INTEGER DEFAULT 0, task_json TEXT,
  metrics_json TEXT, sharpe_daily REAL, n_obs INTEGER, sign INTEGER, evaluated_utc TEXT, error TEXT,
  audit_status TEXT, audit_json TEXT, audited_utc TEXT, trader_status TEXT
);
CREATE INDEX IF NOT EXISTS ix_trials_status ON trials(status);
CREATE INDEX IF NOT EXISTS ix_trials_hash ON trials(ast_hash);
CREATE TABLE IF NOT EXISTS returns (trial_id INTEGER PRIMARY KEY, n INTEGER, net BLOB, gross BLOB, turnover BLOB);
CREATE TABLE IF NOT EXISTS pool (ast_hash TEXT PRIMARY KEY, trial_id INTEGER, added_utc TEXT, delta_ic REAL, max_abs_corr REAL, meta_json TEXT);
CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, agent TEXT, kind TEXT, detail TEXT);
CREATE TABLE IF NOT EXISTS llm_requests (id TEXT PRIMARY KEY, created_utc TEXT, kind TEXT, persona TEXT, n INTEGER, status TEXT, detail TEXT);
"""
REJECTED = ("REJECTED_SYNTAX", "REJECTED_NODES", "REJECTED_NOVELTY", "REJECTED_EXCESS")


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _pack(a: np.ndarray) -> bytes:
    return zlib.compress(np.ascontiguousarray(a, dtype="<f8").tobytes(), 3)


def _unpack(b: Optional[bytes]) -> Optional[np.ndarray]:
    return None if b is None else np.frombuffer(zlib.decompress(b), dtype="<f8").copy()


def compute_baseline(engine_state: Optional[str] = None, sde_ledger: Optional[str] = None) -> dict:
    """Read-only counts of the two earlier ledgers (engine N from state.json, SDE `trial` entries). Never writes them."""
    engine_state = engine_state or os.path.join(REPO_ROOT, "engine", "ledger", "state.json")
    sde_ledger = sde_ledger or os.path.join(REPO_ROOT, "src", "audit", "ledger.jsonl")
    n_engine = n_sde = 0
    if os.path.exists(engine_state):
        n_engine = int(json.load(open(engine_state)).get("N", 0))
    if os.path.exists(sde_ledger):
        with open(sde_ledger, "rb") as f:
            for line in f:
                if b'"kind":"trial"' in line:
                    n_sde += 1
    return {"engine_n": n_engine, "sde_n": n_sde, "read_utc": utc_now(),
            "note": "baseline offset added to N_trials so the swarm's DSR bar is no looser than earlier searches"}


class SharedLedger:
    """Process-safe trial manager. Create one instance per process (connections are re-opened after fork)."""

    def __init__(self, path: Optional[str] = None, timeout: float = 60.0):
        self.path = str(path or DEFAULT_DB)
        self.timeout = timeout
        self._conn: Optional[sqlite3.Connection] = None
        self._pid = -1
        os.makedirs(os.path.dirname(os.path.abspath(self.path)), exist_ok=True)
        with self._tx() as c:
            for stmt in SCHEMA.strip().split(";"):
                if stmt.strip():
                    c.execute(stmt)

    # ------------------------------------------------------------------ connection / transactions
    @property
    def conn(self) -> sqlite3.Connection:
        if self._conn is None or self._pid != os.getpid():
            self._conn = sqlite3.connect(self.path, timeout=self.timeout, isolation_level=None)
            self._conn.row_factory = sqlite3.Row
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute("PRAGMA synchronous=NORMAL")
            self._conn.execute(f"PRAGMA busy_timeout={int(self.timeout * 1000)}")
            self._pid = os.getpid()
        return self._conn

    def _tx(self):
        led = self

        class _T:
            def __enter__(s):
                led.conn.execute("BEGIN IMMEDIATE")
                return led.conn

            def __exit__(s, et, ev, tb):
                led.conn.execute("ROLLBACK" if et else "COMMIT")
                return False

        return _T()

    def close(self) -> None:
        if self._conn is not None and self._pid == os.getpid():
            self._conn.close()
        self._conn = None

    # ------------------------------------------------------------------ meta / baseline
    def get_meta(self, k: str, default: Any = None) -> Any:
        r = self.conn.execute("SELECT v FROM meta WHERE k=?", (k,)).fetchone()
        return json.loads(r["v"]) if r else default

    def set_meta(self, k: str, v: Any) -> None:
        with self._tx() as c:
            c.execute("INSERT INTO meta(k,v) VALUES(?,?) ON CONFLICT(k) DO UPDATE SET v=excluded.v", (k, json.dumps(v)))

    def set_baseline(self, baseline: dict, overwrite: bool = False) -> dict:
        """Store the baseline offset once (first writer wins unless overwrite)."""
        with self._tx() as c:
            r = c.execute("SELECT v FROM meta WHERE k='baseline'").fetchone()
            if r is None or overwrite:
                c.execute("INSERT INTO meta(k,v) VALUES('baseline',?) ON CONFLICT(k) DO UPDATE SET v=excluded.v", (json.dumps(baseline),))
                return baseline
            return json.loads(r["v"])

    def baseline_n(self) -> int:
        b = self.get_meta("baseline") or {}
        return int(b.get("engine_n", 0)) + int(b.get("sde_n", 0))

    # ------------------------------------------------------------------ counting
    def n_swarm_trials(self) -> int:
        return int(self.conn.execute("SELECT COUNT(*) FROM trials").fetchone()[0])

    def n_trials(self) -> int:
        """Global N_trials used by the deflated Sharpe ratio (baseline offset + every swarm proposal)."""
        return self.baseline_n() + self.n_swarm_trials()

    def counts(self) -> dict:
        rows = self.conn.execute("SELECT status, COUNT(*) n FROM trials GROUP BY status").fetchall()
        aud = self.conn.execute("SELECT audit_status, COUNT(*) n FROM trials WHERE audit_status IS NOT NULL GROUP BY audit_status").fetchall()
        return {"n_trials_global": self.n_trials(), "baseline_n": self.baseline_n(), "swarm_trials": self.n_swarm_trials(),
                "by_status": {r["status"]: r["n"] for r in rows}, "by_audit": {r["audit_status"]: r["n"] for r in aud},
                "pool_size": int(self.conn.execute("SELECT COUNT(*) FROM pool").fetchone()[0])}

    # ------------------------------------------------------------------ proposals
    def record_proposal(self, expression: str, source: str, agent_id: str, status: str, *, persona: str = "", parent_hash: str = "",
                        hypothesis: str = "", ast_hash: str = "", canonical: str = "", ast_json: Optional[dict] = None,
                        reject_reason: str = "", reject_detail: Optional[dict] = None, task_json: Optional[dict] = None) -> int:
        """Insert one counted trial and return its id. `task_json` may reference the id via the placeholder '__TRIAL_ID__'."""
        with self._tx() as c:
            cur = c.execute(
                "INSERT INTO trials(ast_hash,expression,canonical,ast_json,source,agent_id,persona,parent_hash,hypothesis,created_utc,status,"
                "reject_reason,reject_detail) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (ast_hash, expression[:2000], canonical, json.dumps(ast_json) if ast_json else None, source, agent_id, persona, parent_hash,
                 hypothesis[:1000], utc_now(), status, reject_reason, json.dumps(reject_detail) if reject_detail else None))
            tid = int(cur.lastrowid)
            if task_json is not None:
                task_json = dict(task_json, trial_id=tid, task_id=f"task_{tid}")
                c.execute("UPDATE trials SET task_json=? WHERE id=?", (json.dumps(task_json), tid))
            return tid

    def history_since(self, last_id: int = 0) -> list[tuple[int, str, str]]:
        """(id, ast_hash, canonical) of formulas that entered evaluation (the novelty 'memory vault')."""
        q = "SELECT id, ast_hash, canonical FROM trials WHERE id>? AND status IN ('PENDING','RUNNING','EVALUATED','ERROR') ORDER BY id"
        return [(r["id"], r["ast_hash"], r["canonical"]) for r in self.conn.execute(q, (last_id,))]

    def recent_formulas(self, limit: int = 200) -> list[dict]:
        q = ("SELECT ast_hash hash, canonical expression FROM trials WHERE status IN ('PENDING','RUNNING','EVALUATED','ERROR') "
             "ORDER BY id DESC LIMIT ?")
        return [dict(r) for r in self.conn.execute(q, (limit,))]

    def pending_count(self) -> int:
        return int(self.conn.execute("SELECT COUNT(*) FROM trials WHERE status IN ('PENDING','RUNNING')").fetchone()[0])

    # ------------------------------------------------------------------ worker queue
    def claim_task(self, worker_id: str, lease_s: float = 300.0) -> Optional[dict]:
        """Atomically lease the oldest PENDING task (expired leases are re-queued first; 3 attempts max)."""
        now = time.time()
        with self._tx() as c:
            c.execute("UPDATE trials SET status='PENDING', lease_owner=NULL WHERE status='RUNNING' AND lease_until<? AND attempts<3", (now,))
            c.execute("UPDATE trials SET status='ERROR', error='lease expired 3 times' WHERE status='RUNNING' AND lease_until<? AND attempts>=3", (now,))
            r = c.execute("SELECT id, task_json FROM trials WHERE status='PENDING' ORDER BY id LIMIT 1").fetchone()
            if r is None:
                return None
            c.execute("UPDATE trials SET status='RUNNING', lease_owner=?, lease_until=?, attempts=attempts+1 WHERE id=?",
                      (worker_id, now + lease_s, r["id"]))
            return json.loads(r["task_json"])

    def release_task(self, trial_id: int, worker_id: str) -> None:
        """Hand an unfinished leased task back (used on clean shutdown)."""
        with self._tx() as c:
            c.execute("UPDATE trials SET status='PENDING', lease_owner=NULL, attempts=MAX(attempts-1,0) WHERE id=? AND status='RUNNING' AND lease_owner=?",
                      (trial_id, worker_id))

    def complete_task(self, trial_id: int, worker_id: str, *, metrics: dict, net: np.ndarray, gross: np.ndarray, turnover: np.ndarray,
                      sharpe_daily: float, sign: int) -> None:
        with self._tx() as c:
            r = c.execute("SELECT status, lease_owner FROM trials WHERE id=?", (trial_id,)).fetchone()
            if r is None or r["status"] != "RUNNING" or r["lease_owner"] != worker_id:
                raise RuntimeError(f"trial {trial_id} is not leased to {worker_id}")
            c.execute("UPDATE trials SET status='EVALUATED', metrics_json=?, sharpe_daily=?, n_obs=?, sign=?, evaluated_utc=?, lease_owner=NULL WHERE id=?",
                      (json.dumps(metrics), float(sharpe_daily), int(len(net)), int(sign), utc_now(), trial_id))
            c.execute("INSERT OR REPLACE INTO returns(trial_id,n,net,gross,turnover) VALUES(?,?,?,?,?)",
                      (trial_id, int(len(net)), _pack(net), _pack(gross), _pack(turnover)))

    def fail_task(self, trial_id: int, worker_id: str, error: str) -> None:
        with self._tx() as c:
            c.execute("UPDATE trials SET status='ERROR', error=?, lease_owner=NULL WHERE id=? AND lease_owner=?", (error[:500], trial_id, worker_id))

    # ------------------------------------------------------------------ reads for audit / trader / publisher
    def get_trial(self, trial_id: int) -> Optional[dict]:
        r = self.conn.execute("SELECT * FROM trials WHERE id=?", (trial_id,)).fetchone()
        return dict(r) if r else None

    def get_returns(self, trial_id: int) -> Optional[dict]:
        r = self.conn.execute("SELECT * FROM returns WHERE trial_id=?", (trial_id,)).fetchone()
        return None if r is None else {"net": _unpack(r["net"]), "gross": _unpack(r["gross"]), "turnover": _unpack(r["turnover"])}

    def evaluated_unaudited(self, limit: int = 500) -> list[dict]:
        return [dict(r) for r in self.conn.execute(
            "SELECT * FROM trials WHERE status='EVALUATED' AND audit_status IS NULL ORDER BY id LIMIT ?", (limit,))]

    def recent_evaluated(self, limit: int = 100, exclude: Iterable[int] = ()) -> list[dict]:
        ex = set(exclude)
        rows = self.conn.execute("SELECT * FROM trials WHERE status='EVALUATED' ORDER BY id DESC LIMIT ?", (limit + len(ex),)).fetchall()
        return [dict(r) for r in rows if r["id"] not in ex][:limit]

    def sharpe_variance(self) -> tuple[float, int]:
        """(variance of per-period Sharpe ratios across all evaluated swarm trials, how many)."""
        v = [r[0] for r in self.conn.execute("SELECT sharpe_daily FROM trials WHERE status='EVALUATED' AND sharpe_daily IS NOT NULL")]
        v = np.array([x for x in v if x is not None and np.isfinite(x)])
        return (float(v.var(ddof=1)) if len(v) > 2 else float("nan")), int(len(v))

    def set_audit(self, trial_id: int, status: str, audit: dict) -> None:
        with self._tx() as c:
            c.execute("UPDATE trials SET audit_status=?, audit_json=?, audited_utc=? WHERE id=?", (status, json.dumps(audit, default=float), utc_now(), trial_id))

    def approved_untraded(self) -> list[dict]:
        return [dict(r) for r in self.conn.execute(
            "SELECT * FROM trials WHERE audit_status='APPROVED' AND trader_status IS NULL ORDER BY id")]

    def set_trader_status(self, trial_id: int, status: str) -> None:
        with self._tx() as c:
            c.execute("UPDATE trials SET trader_status=? WHERE id=?", (status, trial_id))

    # ------------------------------------------------------------------ pool
    def pool_members(self) -> list[dict]:
        return [dict(r) for r in self.conn.execute(
            "SELECT p.*, t.expression, t.canonical, t.ast_json, t.sign, t.metrics_json, t.audit_json FROM pool p JOIN trials t ON t.id=p.trial_id ORDER BY p.rowid")]

    def add_to_pool(self, trial_id: int, ast_hash: str, delta_ic: float, max_abs_corr: float, meta: Optional[dict] = None) -> None:
        with self._tx() as c:
            c.execute("INSERT OR IGNORE INTO pool(ast_hash,trial_id,added_utc,delta_ic,max_abs_corr,meta_json) VALUES(?,?,?,?,?,?)",
                      (ast_hash, trial_id, utc_now(), float(delta_ic), float(max_abs_corr), json.dumps(meta or {}, default=float)))

    # ------------------------------------------------------------------ misc
    def log_event(self, agent: str, kind: str, detail: Any = None) -> None:
        with self._tx() as c:
            c.execute("INSERT INTO events(ts,agent,kind,detail) VALUES(?,?,?,?)", (utc_now(), agent, kind, json.dumps(detail, default=str)))

    def events(self, kind: Optional[str] = None, limit: int = 100) -> list[dict]:
        q, a = ("SELECT * FROM events WHERE kind=? ORDER BY id DESC LIMIT ?", (kind, limit)) if kind else ("SELECT * FROM events ORDER BY id DESC LIMIT ?", (limit,))
        return [dict(r) for r in self.conn.execute(q, a)]

    def upsert_llm_request(self, rid: str, status: str, kind: str = "", persona: str = "", n: int = 0, detail: Any = None) -> None:
        with self._tx() as c:
            c.execute("INSERT INTO llm_requests(id,created_utc,kind,persona,n,status,detail) VALUES(?,?,?,?,?,?,?) "
                      "ON CONFLICT(id) DO UPDATE SET status=excluded.status, detail=excluded.detail",
                      (rid, utc_now(), kind, persona, n, status, json.dumps(detail, default=str)))
