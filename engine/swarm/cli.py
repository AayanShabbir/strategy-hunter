"""CLI glue for the swarm; registered into `hunt` (engine/hunt_engine/cli.py) via `add_subparsers` / `dispatch`.

  ./engine/hunt swarm-start --workers 4 [--max-trials 200 | --continuous] [--llm none|mailbox|openai] [--db PATH]
  ./engine/hunt swarm-start --sde-policy sp500_s2 --workers 4      # connected mode: GFlowNet proposals + SDE pool + shared N + signing + impact
  ./engine/hunt swarm-status [--db PATH]
  ./engine/hunt swarm-llm-check '<expr>' ['<expr>' ...]
  ./engine/hunt swarm-llm-ping [--timeout 600] [--backend mailbox|openai]
"""
from __future__ import annotations

import json
import sys
import time

from . import DEFAULT_DB


def add_subparsers(sub) -> None:
    s = sub.add_parser("swarm-start", help="launch the strategy-discovery swarm (miner/workers/auditor/trader/publisher); research only")
    s.add_argument("--workers", type=int, default=4)
    s.add_argument("--db", default=DEFAULT_DB, help="shared trial ledger (default data/ledger/trials.db)")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--max-trials", type=int, default=200, help="bounded run: stop after this many NEW formulas were issued, evaluated and audited")
    g.add_argument("--continuous", action="store_true", help="run until Ctrl-C / SIGTERM / `touch data/swarm/STOP`")
    s.add_argument("--max-seconds", type=float, default=None)
    s.add_argument("--llm", choices=["none", "mailbox", "openai"], default="none")
    s.add_argument("--seed", type=int, default=0)
    s.add_argument("--no-publish", action="store_true"); s.add_argument("--no-tearsheet", action="store_true"); s.add_argument("--no-mlflow", action="store_true")
    s.add_argument("--synthetic", action="store_true", help="smoke-test on a synthetic panel instead of the S&P 500 search window")
    s.add_argument("--json", action="store_true", help="print the final report as JSON only")
    s.add_argument("--sde-policy", default=None, help="trained GFlowNet run (id, prefix like sp500_s2, or dir with policy.pt): extra proposal source; "
                   "also turns on the SDE ledger mirror and imports that run's pool.json")
    s.add_argument("--policy-share", type=float, default=0.5, help="share of each generator batch sampled from the policy (default 0.5)")
    s.add_argument("--sde-pool", default=None, help="run whose pool.json members are re-evaluated once (default: the --sde-policy run; 'none' disables)")
    s.add_argument("--sde-ledger", default=None, help="SDE ledger path (default src/audit/ledger.jsonl)")
    s.add_argument("--mirror", action="store_true", help="write swarm trials/verdicts into the SDE ledger (implied by --sde-policy/--sde-pool)")
    s.add_argument("--no-mirror", action="store_true")
    s.add_argument("--dsl", choices=["sde", "ext", "mixed"], default="sde", help="formula dialect: SDE grammar (default), opt-in extended operator set, or both")
    s.add_argument("--no-signing", action="store_true", help="disable Ed25519 signed bundles"); s.add_argument("--key-dir", default=None)
    s.add_argument("--no-impact", action="store_true", help="flat 5 bp cost only (no square-root impact)")
    s.add_argument("--impact-eta", type=float, default=1.0); s.add_argument("--aum", type=float, default=50e6)
    s.add_argument("--allocation", choices=["mvo", "erc", "equal"], default="mvo")
    s.add_argument("--redis", default=None, help="'embedded' (private redis-server, fakeredis fallback) or redis://host:port/db")
    s.add_argument("--duckdb", default=None, help="DuckDB analytics mirror path")
    st = sub.add_parser("swarm-status", help="ledger N, counts, audit verdicts, factor pool"); st.add_argument("--db", default=DEFAULT_DB)
    c = sub.add_parser("swarm-llm-check", help="syntax-check formulas against the swarm DSL (for the Swarm Miner agent)"); c.add_argument("expressions", nargs="+")
    c.add_argument("--dsl", choices=["sde", "ext", "mixed"], default="sde")
    p = sub.add_parser("swarm-llm-ping", help="send one small request through the LLM backend and wait for the answer")
    p.add_argument("--timeout", type=float, default=600.0); p.add_argument("--backend", choices=["mailbox", "openai"], default="mailbox")
    p.add_argument("--root", default=None, help="mailbox directory override")


def llm_check(exprs: list[str], dsl: str = "sde") -> int:
    from .dialect import SyntaxErrors, hash_any, parse_any
    from .simplify import degenerate_reasons
    bad = 0
    for e in exprs:
        try:
            n = parse_any(e, allow_ext=dsl in ("ext", "mixed"))
            deg = degenerate_reasons(n)
            if deg:
                bad += 1
                print(f"DEGENERATE {'+'.join(deg)} (would be rejected free, never evaluated)")
                continue
            print(f"VALID {hash_any(n)} {n.size()}")
        except SyntaxErrors as ex:
            bad += 1
            print(f"INVALID {ex}")
    return 1 if bad else 0


def llm_ping(backend: str = "mailbox", timeout: float = 600.0, root: str | None = None, poll_interval: float = 2.0) -> int:
    from .llm import build_request, make_backend, validate_response
    from src.dsl.grammar import DSLSyntaxError, parse_expr
    be = make_backend(backend, **({"root": root, "abandon_after_s": timeout + 5} if backend == "mailbox" else {}))
    req = build_request("propose", "momentum", 2, avoid_recent=[], n_total_tried=0, blacklisted_subtrees=[], abandon_after_s=timeout + 5)
    be.submit(req)
    print(f"ping submitted: {req['id']} (backend={backend}); waiting up to {timeout:.0f}s ...", flush=True)
    got = be.wait(req["id"], timeout, poll_interval)
    if got is None:
        print("NO RESPONSE before timeout (request left in place; a late answer is still valid)")
        return 2
    _, resp = got
    if isinstance(resp, dict) and "_error" in resp:
        print("ERROR", resp["_error"])
        return 1
    ok, props, err = validate_response(resp, req)
    if not ok:
        print("INVALID RESPONSE:", err)
        return 1
    for p in props:                       # diagnostic only: nothing is backtested or counted as a trial
        try:
            n = parse_expr(p["expression"])
            print(f"OK    {n.canonical()}  ({n.size()} nodes)  // {p.get('hypothesis', '')}")
        except DSLSyntaxError as e:
            print(f"BAD   {p['expression']!r}: {e}")
    print(f"ping complete: {len(props)} proposals from responder={resp.get('responder')!r}")
    return 0


def swarm_start(a) -> int:
    from .cluster import Swarm, SwarmConfig
    connected = bool(a.sde_policy or (a.sde_pool and a.sde_pool != "none"))
    sde_pool = "" if a.sde_pool == "none" else a.sde_pool
    cfg = SwarmConfig(dsl=a.dsl, sde_policy=a.sde_policy, policy_share=a.policy_share, sde_pool=sde_pool, sde_ledger=a.sde_ledger,
                      mirror=(connected or a.mirror) and not a.no_mirror, signing=not a.no_signing, key_dir=a.key_dir, impact=not a.no_impact,
                      impact_eta=a.impact_eta, impact_aum=a.aum, allocation=a.allocation, redis=a.redis, duckdb_path=a.duckdb,
                      workers=a.workers, db=a.db, max_trials=None if a.continuous else a.max_trials, continuous=a.continuous,
                      max_seconds=a.max_seconds, llm=a.llm, seed=a.seed, publish=not a.no_publish, tearsheet=not a.no_tearsheet,
                      mlflow=not a.no_mlflow, panel_spec={"n_days": 700, "n_assets": 60, "seed": a.seed} if a.synthetic else None)
    if not a.json:
        print(f"swarm-start: workers={cfg.workers} db={cfg.db} mode={'continuous' if cfg.continuous else f'bounded({cfg.max_trials})'} llm={cfg.llm}", flush=True)
    rep = Swarm(cfg).run()
    print(json.dumps(rep, indent=None if a.json else 1, default=str))
    return 0


def dispatch(a) -> int:
    if a.cmd == "swarm-start":
        return swarm_start(a)
    if a.cmd == "swarm-status":
        from .cluster import status
        print(json.dumps(status(a.db), indent=1, default=str))
        return 0
    if a.cmd == "swarm-llm-check":
        return llm_check(a.expressions, getattr(a, 'dsl', 'sde'))
    if a.cmd == "swarm-llm-ping":
        return llm_ping(a.backend, a.timeout, a.root)
    raise SystemExit(f"unknown swarm command {a.cmd}")
