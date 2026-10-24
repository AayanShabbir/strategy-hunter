"""Optional DuckDB analytics mirror of the swarm ledger (blueprint: columnar store for subtree/novelty analytics).

SQLite stays the system of record (transactional, multi-process). This module incrementally copies trials into a DuckDB file and
materialises the rooted-subtree table, so the frequent-subtree ("blacklist") query and funnel reports are plain SQL over columnar
data. One writer (the coordinator) owns the file; readers should open it read-only. `subtree_blacklist()` is cross-checked against
`NoveltyMemory.blacklist()` by the tests - both implement the same definition (support = share of distinct novelty-memory formulas
containing the subtree, threshold `support_max`, silent below `min_history` formulas).
"""
from __future__ import annotations

import json
from typing import Optional

from .dialect import parse_any
from .novelty import subtree_set
from .shared_ledger import SharedLedger

IN_MEMORY_STATUSES = ("PENDING", "RUNNING", "EVALUATED", "ERROR")     # statuses whose formulas enter the novelty memory


class Analytics:
    def __init__(self, path: str = ":memory:", read_only: bool = False):
        import duckdb
        self.path = path
        self.db = duckdb.connect(path, read_only=read_only)
        if not read_only:
            self.db.execute("""CREATE TABLE IF NOT EXISTS trials(id BIGINT PRIMARY KEY, ast_hash VARCHAR, canonical VARCHAR, source VARCHAR,
                status VARCHAR, reject_reason VARCHAR, audit_status VARCHAR, trader_status VARCHAR, sharpe_daily DOUBLE, search_sharpe DOUBLE,
                failed_gates VARCHAR)""")
            self.db.execute("CREATE TABLE IF NOT EXISTS subtrees(ast_hash VARCHAR, subtree VARCHAR)")
            self.db.execute("CREATE TABLE IF NOT EXISTS seen_hash(ast_hash VARCHAR PRIMARY KEY)")

    def sync(self, ledger: SharedLedger, subtree_depth: int = 3, subtree_min_size: int = 3) -> dict:
        """Copy new trials (by id) and refresh the mutable columns (status/audit) of existing ones. Returns counts."""
        last = self.db.execute("SELECT COALESCE(max(id),0) FROM trials").fetchone()[0]
        new = ledger.conn.execute("SELECT id, ast_hash, canonical, source, status, reject_reason, audit_status, trader_status, sharpe_daily, "
                                  "metrics_json, audit_json FROM trials WHERE id>? ORDER BY id", (last,)).fetchall()
        n_sub = 0
        for r in new:
            m = json.loads(r["metrics_json"] or "{}")
            a = json.loads(r["audit_json"] or "{}")
            self.db.execute("INSERT INTO trials VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                            [r["id"], r["ast_hash"], r["canonical"], r["source"], r["status"], r["reject_reason"], r["audit_status"], r["trader_status"],
                             r["sharpe_daily"], m.get("search_sharpe"), ",".join(a.get("failed_gates", []) or [])])
            if r["status"] in IN_MEMORY_STATUSES and r["ast_hash"] and r["canonical"]:
                if self.db.execute("SELECT 1 FROM seen_hash WHERE ast_hash=?", [r["ast_hash"]]).fetchone() is None:
                    try:
                        subs = subtree_set(parse_any(r["canonical"]), subtree_depth, subtree_min_size)
                    except Exception:
                        subs = set()
                    self.db.execute("INSERT INTO seen_hash VALUES (?)", [r["ast_hash"]])
                    if subs:
                        self.db.executemany("INSERT INTO subtrees VALUES (?,?)", [[r["ast_hash"], s] for s in subs])
                        n_sub += len(subs)
        for r in ledger.conn.execute("SELECT id, status, audit_status, trader_status, sharpe_daily, metrics_json, audit_json FROM trials "
                                     "WHERE id<=? AND (audit_status IS NOT NULL OR status IN ('EVALUATED','ERROR','RUNNING'))", (last,)):
            m = json.loads(r["metrics_json"] or "{}")
            a = json.loads(r["audit_json"] or "{}")
            self.db.execute("UPDATE trials SET status=?, audit_status=?, trader_status=?, sharpe_daily=?, search_sharpe=?, failed_gates=? WHERE id=?",
                            [r["status"], r["audit_status"], r["trader_status"], r["sharpe_daily"], m.get("search_sharpe"),
                             ",".join(a.get("failed_gates", []) or []), r["id"]])
        return {"new_trials": len(new), "new_subtree_rows": n_sub}

    def n_memory(self) -> int:
        return self.db.execute("SELECT count(*) FROM seen_hash").fetchone()[0]

    def subtree_support(self, subtree: str) -> float:
        n = self.n_memory()
        c = self.db.execute("SELECT count(DISTINCT ast_hash) FROM subtrees WHERE subtree=?", [subtree]).fetchone()[0]
        return c / n if n else 0.0

    def subtree_blacklist(self, support_max: float = 0.15, min_history: int = 30) -> list[str]:
        n = self.n_memory()
        if n < min_history:
            return []
        rows = self.db.execute("SELECT subtree FROM subtrees GROUP BY subtree HAVING count(DISTINCT ast_hash) * 1.0 / ? > ? ORDER BY subtree",
                               [n, support_max]).fetchall()
        return [r[0] for r in rows]

    def funnel(self) -> list[dict]:
        """Per proposal source: proposed / evaluated / audited-approved / in pool."""
        cur = self.db.execute("""SELECT source, count(*) AS proposed, count(*) FILTER (WHERE status='EVALUATED') AS evaluated,
            count(*) FILTER (WHERE audit_status='APPROVED') AS approved, count(*) FILTER (WHERE trader_status='INTEGRATED') AS integrated
            FROM trials GROUP BY source ORDER BY proposed DESC""")
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]

    def gate_failures(self) -> list[tuple]:
        return self.db.execute("""SELECT g AS gate, count(*) AS n FROM (SELECT unnest(string_split(failed_gates, ',')) AS g FROM trials
            WHERE failed_gates <> '') GROUP BY g ORDER BY n DESC""").fetchall()

    def close(self) -> None:
        self.db.close()
