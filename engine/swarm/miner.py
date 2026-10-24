"""Miner Agent: proposes formulas, filters them for structure, and emits task-assignment JSON payloads.

State machine (blueprint): HYPOTHESIS_GEN -> AST_SYNTAX_CHECK -> NOVELTY_FILTER -> [assignment to a worker].
The Miner is isolated from prices and returns: it only reads formula strings and aggregated audit summaries.

Sources of proposals (all go through the same screen, and every one is a counted trial):
  * `SymbolicGenerator` - grammar-driven random generator with persona biases (no LLM needed, always available);
  * an `LLMBackend` (mailbox agent or OpenAI-compatible HTTP) - asynchronous: `request_llm` never blocks and `ingest_llm`
    picks up whatever has arrived, so workers keep busy on generator proposals while LLM requests are pending.
Anti-collapse: normalised d_TED >= 0.35 against the memory vault + frequent-subtree blacklist (support > 15%); after
more than 3 consecutive structural rejections the generator is "reheated" (temperature -> 0.9, wider/deeper trees).
"""
from __future__ import annotations

import json
import time
from typing import Optional

import numpy as np

from src.dsl.grammar import BINARY, FEATURES, MAX_LEN, WINDOWS, DSLSyntaxError, parse_expr

from . import PROTOCOL
from .dialect import SyntaxErrors, dialect_of_node, hash_any as node_hash, parse_any, to_json_any as node_to_json
from .dsl_ext import ExtGenerator
from .signing import task_payload
from .simplify import degenerate_reasons
from .llm import PERSONAS, LLMBackend, build_request, validate_response
from .novelty import NoveltyMemory
from .shared_ledger import SharedLedger, utc_now

# persona -> (feature weights over $close,$high,$low,$volume ; weight of Log, TsStd, binary ; binary weights Add,Sub,Div)
PERSONA_BIAS = {
    "momentum": ([5, 1, 1, 1], (2, 2, 4), (1, 3, 3)),
    "mean_reversion": ([3, 2, 2, 1], (1, 3, 4), (1, 4, 2)),
    "volatility": ([3, 2, 2, 2], (1, 5, 3), (1, 2, 4)),
    "liquidity": ([2, 1, 1, 5], (3, 2, 3), (1, 2, 4)),
    "range_microstructure": ([2, 4, 4, 2], (1, 2, 4), (1, 4, 4)),
    "cross_contrast": ([2, 2, 2, 2], (2, 2, 5), (2, 3, 3)),
}
PERSONA_ORDER = list(PERSONA_BIAS)
MIN_NODES = 4


class SymbolicGenerator:
    """Grammar-directed random formula generator. `temperature` in [0,1]: higher = flatter weights and deeper trees."""

    def __init__(self, seed: int = 0, max_nodes: int = MAX_LEN):
        self.rng = np.random.default_rng(seed)
        self.max_nodes = max_nodes

    def sample(self, persona: str = "cross_contrast", temperature: float = 0.5) -> str:
        fw, ow, bw = PERSONA_BIAS.get(persona, PERSONA_BIAS["cross_contrast"])
        flat = 0.15 + 0.85 * (1 - temperature) if temperature < 1 else 0.15
        norm = lambda w: (np.array(w, float) ** flat) / (np.array(w, float) ** flat).sum()  # noqa: E731
        fw, ow, bw = norm(fw), norm(ow), norm(bw)
        depth = 3 + int(round(2 * temperature))
        rng = self.rng

        def gen(d: int) -> str:
            leaf_p = 0.15 if d == depth else 0.25 + 0.15 * (depth - d)
            if d == 0 or rng.random() < leaf_p:
                return FEATURES[int(rng.choice(4, p=fw))]
            k = int(rng.choice(3, p=ow))
            if k == 0:
                return f"Log({gen(d - 1)})"
            if k == 1:
                return f"TsStd({gen(d - 1)}, {list(WINDOWS)[int(rng.integers(len(WINDOWS)))]})"
            return f"{BINARY[int(rng.choice(3, p=bw))]}({gen(d - 1)}, {gen(d - 1)})"

        for _ in range(200):
            s = gen(depth)
            try:
                n = parse_expr(s).size()
            except DSLSyntaxError:
                continue
            if MIN_NODES <= n <= self.max_nodes:
                return s
        return "Div(Sub($high, $low), TsStd($close, 20d))"


class Miner:
    def __init__(self, ledger: SharedLedger, seed: int = 0, agent_id: str = "miner_0", max_nodes: int = MAX_LEN, min_ted: float = 0.35,
                 support_max: float = 0.15, min_history: int = 30, llm: Optional[LLMBackend] = None, llm_max_pending: int = 1,
                 llm_min_interval_s: float = 60.0, llm_n: int = 8, dsl: str = "sde", policy=None, policy_share: float = 0.5,
                 sde_seen: Optional[set] = None, keystore=None, coordinator=None):
        """`dsl`: generator dialect - 'sde' (default, unchanged behaviour), 'ext' (blueprint operators) or 'mixed'.
        `policy`: optional `sde_bridge.PolicySource` (trained GFlowNet) used for `policy_share` of every generator batch.
        `sde_seen`: ast hashes already tried by the SDE; a proposal hitting one is a counted duplicate (not re-evaluated)."""
        self.ledger, self.agent_id, self.max_nodes = ledger, agent_id, max_nodes
        self.gen = SymbolicGenerator(seed, max_nodes)
        self.dsl = dsl
        self.ext_gen = ExtGenerator(seed + 7919) if dsl in ("ext", "mixed") else None
        self.policy, self.policy_share = policy, float(policy_share)
        self.sde_seen = sde_seen if sde_seen is not None else set()
        self.keystore, self.coord = keystore, coordinator
        self.memory = NoveltyMemory(min_ted=min_ted, support_max=support_max, min_history=min_history)
        self.last_id = 0
        self.temperature = 0.5
        self.fail_streak = 0
        self.persona_i = 0
        self.llm, self.llm_max_pending, self.llm_min_interval, self.llm_n = llm, llm_max_pending, llm_min_interval_s, llm_n
        self._last_llm = 0.0
        self.stats = {"generated": 0, "sampled": 0, "accepted": 0, "rejected": {}, "llm_requests": 0, "llm_responses": 0, "llm_proposals": 0, "reheats": 0,
                      "degenerate": {}, "by_source": {}}
        self.refresh_memory()

    # ------------------------------------------------------------------ memory vault
    def refresh_memory(self) -> int:
        """Pull formulas that entered evaluation since the last call (from any miner process) into the in-process vault."""
        n = 0
        for tid, h, canon in self.ledger.history_since(self.last_id):
            self.last_id = max(self.last_id, tid)
            if canon and self.memory.add(parse_any(canon, 64), h):
                n += 1
        return n

    # ------------------------------------------------------------------ screening (syntax -> novelty -> register)
    def screen(self, expression: str, source: str, persona: str = "", hypothesis: str = "", parent_hash: str = "", allow_seen: bool = False) -> dict:
        """Run one proposal through the state machine and register it in the shared ledger.

        Counted as a trial in every case EXCEPT `REJECTED_DEGENERATE`: a formula that algebra already proves self-cancelling or
        constant (`Sub(x, x)`, `Div(x, x)`, ...) is rejected before it costs a trial - it is equivalent to a trivial formula, carries
        no information, and is reported (miner stats + a `degenerate_rejected` event) instead. Syntax errors stay counted."""
        self.refresh_memory()
        kw = dict(persona=persona, hypothesis=hypothesis, parent_hash=parent_hash)
        try:
            node = parse_any(expression, self.max_nodes, allow_ext=self.dsl != "sde")        # AST_SYNTAX_CHECK (SDE: MaxLen 32 nodes; extended: 10 nodes / depth 4)
        except SyntaxErrors as e:
            tid = self.ledger.record_proposal(expression, source, self.agent_id, "REJECTED_SYNTAX", reject_reason="syntax", reject_detail={"error": str(e)}, **kw)
            return self._tally({"trial_id": tid, "status": "REJECTED_SYNTAX", "reason": "syntax", "detail": str(e), "assignment": None}, source)
        reasons = degenerate_reasons(node)                      # DEGENERACY: algebraic, data-free, free of charge
        if reasons:
            key = "+".join(reasons)
            self.stats["degenerate"][key] = self.stats["degenerate"].get(key, 0) + 1
            self.ledger.log_event(self.agent_id, "degenerate_rejected", {"expression": expression[:300], "source": source, "reasons": reasons})
            return self._tally({"trial_id": None, "status": "REJECTED_DEGENERATE", "reason": "degenerate", "detail": reasons, "assignment": None}, source)
        h = node_hash(node)
        if h in self.sde_seen and not allow_seen:               # already a counted SDE trial: a counted swarm duplicate, not re-evaluated
            tid = self.ledger.record_proposal(expression, source, self.agent_id, "REJECTED_NOVELTY", ast_hash=h, canonical=node.canonical(),
                                              reject_reason="sde_seen", reject_detail={"note": "identical AST already in the SDE ledger"}, **kw)
            return self._tally({"trial_id": tid, "status": "REJECTED_NOVELTY", "reason": "sde_seen", "detail": {}, "assignment": None}, source)
        ok, reason, detail = self.memory.check(node, h)         # NOVELTY_FILTER
        if not ok:
            tid = self.ledger.record_proposal(expression, source, self.agent_id, "REJECTED_NOVELTY", ast_hash=h, canonical=node.canonical(),
                                              reject_reason=reason, reject_detail=detail, **kw)
            return self._tally({"trial_id": tid, "status": "REJECTED_NOVELTY", "reason": reason, "detail": detail, "assignment": None}, source)
        task = {"protocol": PROTOCOL, "expression": node.canonical(), "ast_hash": h, "ast": node_to_json(node), "source": source,
                "dsl": dialect_of_node(node), "persona": persona, "agent_id": self.agent_id, "created_utc": utc_now(), "max_nodes": self.max_nodes}
        if self.keystore is not None:                           # signed task bundle (verified by the Worker)
            task["signature"] = self.keystore.sign("miner", task_payload(task))
        tid = self.ledger.record_proposal(expression, source, self.agent_id, "PENDING", ast_hash=h, canonical=node.canonical(),
                                          ast_json=task["ast"], task_json=task, **kw)
        self.memory.add(node, h)
        self.last_id = max(self.last_id, tid)
        if self.coord is not None:
            self.coord.push_task(tid)
            self.coord.incr_n()
        task = dict(task, trial_id=tid, task_id=f"task_{tid}")
        return self._tally({"trial_id": tid, "status": "PENDING", "reason": "ok", "detail": detail, "assignment": task}, source)

    def _tally(self, r: dict, source: str = "") -> dict:
        base = source.split(":")[0] or "?"
        bs = self.stats["by_source"].setdefault(base, {"proposed": 0, "accepted": 0})
        bs["proposed"] += 1
        bs["accepted"] += int(r["status"] == "PENDING")
        if r["status"] == "PENDING":
            self.stats["accepted"] += 1
        else:
            self.stats["rejected"][r["reason"]] = self.stats["rejected"].get(r["reason"], 0) + 1
        return r

    # ------------------------------------------------------------------ generator path
    def _sample_generator(self, persona: str) -> tuple[str, str]:
        """(expression, source) from the symbolic generator(s); 'mixed' alternates the two dialects."""
        use_ext = self.dsl == "ext" or (self.dsl == "mixed" and self.stats["sampled"] % 2 == 1)
        if use_ext:
            return self.ext_gen.sample(persona, self.temperature), "generator_ext"
        return self.gen.sample(persona, self.temperature), "generator"

    def propose_batch(self, n: int, persona: Optional[str] = None, max_attempts: Optional[int] = None) -> list[dict]:
        """Generate until `n` assignments pass the filters or `max_attempts` proposals were made (all but degenerate ones counted).
        With a GFlowNet `policy` attached, `policy_share` of the batch is sampled from it (source 'sde_policy'), the rest from the
        symbolic generator; every sample goes through the identical `screen`."""
        out, attempts, cap = [], 0, max_attempts or n * 20
        n_pol = int(round(n * self.policy_share)) if self.policy is not None else 0
        while len(out) < n and attempts < cap:
            p = persona or PERSONA_ORDER[self.persona_i % len(PERSONA_ORDER)]
            self.persona_i += 1
            if len(out) < n_pol and self.policy is not None:
                expr, src, p = self.policy.sample(), "sde_policy", "sde_policy"
            else:
                expr, src = self._sample_generator(p)
            r = self.screen(expr, source=src, persona=p)
            attempts += 1
            self.stats["sampled"] += 1
            self.stats["generated"] += int(r["trial_id"] is not None)      # `generated` = proposals that cost a trial (degenerate ones are free)
            if r["assignment"]:
                out.append(r["assignment"])
                self.fail_streak = 0
                self.temperature = max(0.5, self.temperature - 0.1)
            elif r["reason"] in ("ted", "duplicate", "frequent_subtree") and src != "sde_policy":
                self.fail_streak += 1
                if self.fail_streak > 3 and self.temperature < 0.9:       # path-collapse recovery (blueprint Table 4)
                    self.temperature = 0.9
                    self.stats["reheats"] += 1
                    self.ledger.log_event(self.agent_id, "path_collapse_reheat", {"fail_streak": self.fail_streak})
        return out

    def import_sde_pool(self, members: list[dict], limit: Optional[int] = None) -> list[dict]:
        """Propose the SDE factor-pool formulas once (source 'sde_pool'). Members already present in this ledger are skipped silently
        (nothing was proposed, so nothing is counted); degenerate members (e.g. `Sub($close, $close)`) are rejected free and reported."""
        out = []
        have = {r[0] for r in self.ledger.conn.execute("SELECT ast_hash FROM trials WHERE ast_hash IS NOT NULL")}
        for m in members[: limit or len(members)]:
            if m.get("ast_hash") in have:
                continue
            r = self.screen(m["expr"], "sde_pool", "sde_pool", hypothesis=f"SDE pool member (train IC {m.get('train_ic')})", allow_seen=True)
            if r["assignment"]:
                out.append(r["assignment"])
        return out

    # ------------------------------------------------------------------ LLM path (non-blocking)
    def feedback_summaries(self, limit: int = 6) -> list[dict]:
        """Search-window summaries of audited-and-rejected formulas (best search Sharpe first) for `refine` requests."""
        rows = self.ledger.conn.execute("SELECT ast_hash, canonical, audit_json, metrics_json FROM trials WHERE audit_status='REJECTED' "
                                        "ORDER BY id DESC LIMIT 200").fetchall()
        items = []
        for r in rows:
            a, m = json.loads(r["audit_json"] or "{}"), json.loads(r["metrics_json"] or "{}")
            g = a.get("gates", {})
            items.append({"hash": r["ast_hash"], "expression": r["canonical"], "failed_gates": a.get("failed_gates", []),
                          "summary": {"search_sharpe_annual": m.get("search_sharpe"), "search_ic": None, "turnover_annual": m.get("annualized_turnover"),
                                      "pbo": g.get("pbo", {}).get("pbo"), "dsr": g.get("dsr", {}).get("dsr"), "spa_p": g.get("spa", {}).get("p_candidate"),
                                      "delta_ic": None, "max_abs_corr_with_pool": None}})
        items.sort(key=lambda x: -(x["summary"]["search_sharpe_annual"] or -9))
        return items[:limit]

    def request_llm(self, kind: Optional[str] = None, persona: Optional[str] = None) -> Optional[str]:
        """Write at most `llm_max_pending` outstanding requests, at least `llm_min_interval` apart. Never waits."""
        if self.llm is None or self.llm.n_pending() >= self.llm_max_pending or time.time() - self._last_llm < self.llm_min_interval:
            return None
        fb = self.feedback_summaries() if kind in (None, "refine") else []
        kind = kind or ("refine" if len(fb) >= 3 and self.stats["llm_requests"] % 2 == 1 else "propose")
        persona = persona or PERSONA_ORDER[self.stats["llm_requests"] % len(PERSONA_ORDER)]
        self.refresh_memory()
        req = build_request(kind, persona, self.llm_n, avoid_recent=self.ledger.recent_formulas(200), n_total_tried=self.ledger.n_swarm_trials(),
                            blacklisted_subtrees=self.memory.blacklist(), feedback=fb if kind == "refine" else [], max_nodes=self.max_nodes,
                            min_ted=self.memory.min_ted, support_max=self.memory.support_max,
                            dialect="ext" if self.dsl == "ext" else "sde")
        self.llm.submit(req)
        self._last_llm = time.time()
        self.stats["llm_requests"] += 1
        self.ledger.upsert_llm_request(req["id"], "pending", kind, persona, self.llm_n)
        return req["id"]

    def ingest_llm(self) -> list[dict]:
        """Collect finished LLM requests and screen every proposal (strict). Returns the new assignments."""
        out = []
        if self.llm is None:
            return out
        for req, resp in self.llm.poll():
            if isinstance(resp, dict) and "_error" in resp:
                self.ledger.upsert_llm_request(req["id"], "failed", detail=resp["_error"])
                self.ledger.log_event(self.agent_id, "llm_failed", {"id": req["id"], "error": resp["_error"]})
                continue
            ok, props, err = validate_response(resp, req)
            if not ok:
                self.ledger.upsert_llm_request(req["id"], "invalid", detail=err)
                self.ledger.log_event(self.agent_id, "llm_invalid_response", {"id": req["id"], "error": err})
                continue
            self.stats["llm_responses"] += 1
            res = []
            for i, p in enumerate(props):
                src = f"llm:{req['id']}"
                if i >= req["n"]:                                # more than requested: counted, never evaluated
                    tid = self.ledger.record_proposal(p["expression"], src, self.agent_id, "REJECTED_EXCESS", persona=req["persona"],
                                                      reject_reason="excess", hypothesis=p["hypothesis"], parent_hash=p["parent_hash"])
                    res.append({"trial_id": tid, "status": "REJECTED_EXCESS", "reason": "excess", "assignment": None})
                    continue
                r = self.screen(p["expression"], src, req["persona"], p["hypothesis"], p["parent_hash"])
                self.stats["llm_proposals"] += 1
                res.append(r)
                if r["assignment"]:
                    out.append(r["assignment"])
            self.ledger.upsert_llm_request(req["id"], "ingested", detail={"proposals": len(props), "accepted": sum(1 for r in res if r["assignment"]),
                                                                           "reasons": [r["reason"] for r in res]})
        return out
