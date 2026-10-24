"""Blueprint features added to the swarm: extended operator set, square-root impact, signed bundles, Gram-Schmidt / MVO / ERC trader
weights, Redis coordination, DuckDB analytics, publisher PIT hash. All opt-in; the SDE dialect and its results are untouched."""
import json
import os
import sys
import time

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from swarm import dsl_ext  # noqa: E402
from swarm.auditor import AuditConfig, Auditor  # noqa: E402
from swarm.costs import ImpactModel, adv_sigma, check_turnover, impact_cost, trades  # noqa: E402
from swarm.data import synthetic_panel  # noqa: E402
from swarm.dialect import SyntaxErrors, hash_any, parse_any  # noqa: E402
from swarm.miner import Miner  # noqa: E402
from swarm.novelty import NoveltyMemory  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402
from swarm.signing import KeyStore  # noqa: E402
from swarm.trader import Trader, cap_assets, erc_weights, mgs_orthogonalise, mvo_weights, panel_signal_fn, shrink_cov  # noqa: E402
from swarm.worker import EvalError, Worker, evaluate_formula  # noqa: E402
from src.dsl.grammar import DSLSyntaxError, parse_expr  # noqa: E402


# ------------------------------------------------------------------------------------------------ extended operator set
EXT_EXPRS = ["cs_rank(ts_mean(multiply(ts_delta(close, 1), volume), 20))", "cs_normalize(divide(subtract(high, low), ts_std(returns, 10)))",
             "cs_rank(ts_decay_linear(subtract(tp, close), 7))", "sign(log(abs(ts_delta(volume, 5))))", "cs_rank(add(returns, 0.5))"]


def test_ext_evaluator_matches_independent_reference():
    panel = synthetic_panel(300, 40, seed=2)
    trad = np.ones_like(panel.data["$close"], bool)
    trad[:, :3] = False
    for e in EXT_EXPRS:
        n = dsl_ext.parse_ext(e)
        a, b = dsl_ext.evaluate_numpy(n, panel.data, mask=trad), dsl_ext.evaluate_reference(n, panel.data, mask=trad)
        assert (np.isfinite(a) == np.isfinite(b)).mean() > 0.999, e
        both = np.isfinite(a) & np.isfinite(b)
        assert np.allclose(a[both], b[both], rtol=1e-6, atol=1e-8), e


def test_ext_evaluator_is_causal():
    p = synthetic_panel(220, 15, seed=3)
    n = dsl_ext.parse_ext("cs_rank(ts_decay_linear(ts_delta(close, 3), 10))")
    full = dsl_ext.evaluate_numpy(n, p.data)
    part = dsl_ext.evaluate_numpy(n, {k: v[:150].copy() for k, v in p.data.items()})
    both = np.isfinite(part)
    assert np.allclose(full[:150][both], part[both], rtol=1e-9)


def test_ext_grammar_limits_forbidden_ops_and_schema():
    for bad in ("future_shift(close, 1)", "lookahead_max(close, 5)", "unadjusted_close", "target_return",   # blueprint's forbidden operators
                "ts_mean(close, 300)", "ts_mean(close, 0)", "cs_rank(cs_rank(cs_rank(cs_rank(cs_rank(cs_rank(close))))))",   # window / depth > limits
                "add(add(add(add(add(add(add(add(add(close, high), low), volume), close), high), low), volume), close), high)"):
        with pytest.raises(dsl_ext.ExtSyntaxError):
            dsl_ext.parse_ext(bad)
    n = dsl_ext.parse_ext(EXT_EXPRS[0])
    assert n.size() <= 10 and dsl_ext.parse_ext(n.canonical()).canonical() == n.canonical()
    dsl_ext.validate_schema({"expression_id": "x", "ast_root": dsl_ext.node_to_json(n)})                  # draft-07 schema
    assert dsl_ext.payload_to_node(dsl_ext.node_to_json(n)).canonical() == n.canonical()
    with pytest.raises(Exception):
        dsl_ext.validate_schema({"ast_root": {"node_type": "operator", "operator": "future_shift", "arguments": []}})


def test_dialect_gate_keeps_sde_default_unchanged():
    with pytest.raises(DSLSyntaxError):
        parse_any("cs_rank(ts_mean(close, 20))", allow_ext=False)                                          # default miner mode: still a syntax error
    assert parse_any("Log($close)", allow_ext=False).canonical() == parse_expr("Log($close)").canonical()
    assert hash_any(parse_any(EXT_EXPRS[0])) != hash_any(parse_expr("Log($close)"))


def test_ext_flows_through_novelty_miner_worker_and_publisher_source(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    mn = Miner(led, seed=1, dsl="ext")
    tasks = mn.propose_batch(8, max_attempts=300)
    assert len(tasks) == 8 and all(t["dsl"] == "ext" and t["source"] == "generator_ext" for t in tasks)
    nodes = [dsl_ext.parse_ext(t["expression"]) for t in tasks]
    from swarm.novelty import normalized_ted
    assert all(normalized_ted(nodes[i], nodes[j]) >= 0.35 - 1e-12 for i in range(8) for j in range(i))   # same TED rule on the ext trees
    w = Worker(led, synthetic_panel(700, 60, seed=0, drift_signal=0.004), "w")
    while w.run_once() is not None:
        pass
    assert led.counts()["by_status"].get("EVALUATED", 0) >= 6
    # standalone survivor script for an ext formula reproduces the engine signal
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "engine"))
    from vault.publisher import compile_survivor_source
    row = led.evaluated_unaudited()[0]
    src = compile_survivor_source(row)
    ns: dict = {"__name__": "survivor"}
    exec(compile(src, "survivor_alpha.py", "exec"), ns)
    import pandas as pd
    p = synthetic_panel(300, 40, seed=5)
    idx = pd.bdate_range("2015-01-02", periods=300)
    panel = {k: pd.DataFrame(v, index=idx, columns=p.assets) for k, v in p.data.items()}
    sig = ns["compute_signal"](panel).to_numpy()
    node = dsl_ext.parse_ext(row["canonical"])
    ref = panel_signal_fn(p)(row["canonical"], int(row["sign"]))
    both = np.isfinite(sig) & np.isfinite(ref)
    assert both.sum() > 1000 and np.allclose(sig[both], ref[both], rtol=1e-6, atol=1e-8)


def test_mixed_mode_alternates_dialects(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    mn = Miner(led, seed=2, dsl="mixed")
    tasks = mn.propose_batch(10, max_attempts=400)
    assert {t["dsl"] for t in tasks} == {"sde", "ext"}


# ------------------------------------------------------------------------------------------------ square-root impact
def test_impact_trades_sum_to_backtest_turnover_and_follow_sqrt_law():
    from src.portfolio.long_short import backtest, leverage_normalized_weights, tradable_mask, zscore_rows
    p = synthetic_panel(400, 50, seed=1)
    close, vol = p.data["$close"], p.data["$volume"]
    trad = tradable_mask(p)
    W = leverage_normalized_weights(zscore_rows(np.log(vol) + 0.0 * close, trad))
    bt = backtest(W, close, 5.0)
    m = ImpactModel(eta=1.0, aum=50e6)
    cost, dw = impact_cost(W, close, vol, m)
    check_turnover(dw, bt["turnover"])                                                                        # per-asset trades add up to the SDE turnover
    assert np.allclose(dw.sum(1), bt["turnover"], atol=1e-12)
    assert (cost >= 0).all() and cost[10:].mean() > 0
    # sqrt law: 4x the AUM -> exactly 2x the per-unit slippage -> cost scales by 4 * 2 = 8 (dw is AUM-independent)
    c4, _ = impact_cost(W, close, vol, ImpactModel(eta=1.0, aum=200e6))
    assert np.allclose(c4, 2.0 * cost, rtol=1e-9)
    assert np.allclose(impact_cost(W, close, vol, ImpactModel(eta=3.0, aum=50e6))[0], 3.0 * cost)             # linear in eta
    # sign symmetry: |dw| is the same for the flipped book
    assert np.allclose(impact_cost(-W, close, vol, m)[0], cost, rtol=0.1, atol=1e-5)    # drifted pre-trade weights differ only at second order
    # ADV/sigma are causal: changing the last day's volume does not change any earlier cost
    vol2 = vol.copy(); vol2[-1] *= 100
    assert np.allclose(impact_cost(W, close, vol2, m)[0][:-2], cost[:-2])


def test_worker_charges_impact_on_top_of_flat_cost_and_stores_cost_vector():
    p = synthetic_panel(600, 50, seed=0, drift_signal=0.004)
    n = parse_expr("Log($volume)")
    flat = evaluate_formula(n, p)
    imp = evaluate_formula(n, p, impact=ImpactModel(eta=1.0, aum=50e6))
    assert imp["metrics"]["cost_model"] == "flat+sqrt_impact" and imp["metrics"]["impact"]["alpha"] == 0.5
    assert (imp["cost"] >= flat["cost"] - 1e-15).all() and imp["cost"].sum() > flat["cost"].sum()
    assert np.allclose(imp["net"], imp["sign"] * imp["gross"] - imp["cost"]) or imp["sign"] == -1             # +1 books reconcile exactly
    assert imp["metrics"]["search_sharpe"] < flat["metrics"]["search_sharpe"]


def test_auditor_uses_the_stored_cost_vector(tmp_path):
    from swarm.auditor import gate_cpcv
    rng = np.random.default_rng(0)
    g = rng.normal(0.002, 0.01, 500)
    t = np.full(500, 0.5)
    cfg = AuditConfig(seed=1)
    base = gate_cpcv(g, t, 5.0, cfg)
    heavy = gate_cpcv(g, t, 5.0, cfg, cost=np.full(500, 0.004))
    assert heavy["median_path_sharpe"] < base["median_path_sharpe"]


# ------------------------------------------------------------------------------------------------ signed bundles
def test_signatures_verify_and_detect_tampering_and_role_confusion(tmp_path):
    ks = KeyStore(str(tmp_path / "keys"))
    payload = {"a": 1, "b": [1, 2]}
    sig = ks.sign("miner", payload)
    assert ks.verify(payload, sig, "miner") == (True, "ok")
    assert not ks.verify({"a": 2, "b": [1, 2]}, sig, "miner")[0]                                              # payload edited
    assert not ks.verify(payload, sig, "worker")[0]                                                           # signed by the wrong role
    assert not ks.verify(payload, dict(sig, sig=sig["sig"][:-4] + "AAAA"), "miner")[0]                       # signature edited
    assert not ks.verify(payload, None, "miner")[0]
    assert oct(os.stat(tmp_path / "keys" / "miner.key").st_mode & 0o777) == "0o600"
    ks2 = KeyStore(str(tmp_path / "keys"))
    assert ks2.verify(payload, sig, "miner")[0]                                                               # keys persist across processes
    other = KeyStore(str(tmp_path / "other"))
    assert not other.verify(payload, sig, "miner")[0]                                                         # a different key set cannot validate


def _pipeline(tmp_path, ks, n=6):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    mn = Miner(led, seed=0, keystore=ks)
    mn.propose_batch(n, max_attempts=200)
    return led


def test_end_to_end_signing_and_tamper_rejection(tmp_path):
    ks = KeyStore(str(tmp_path / "keys"))
    led = _pipeline(tmp_path, ks)
    panel = synthetic_panel(600, 50, seed=0, drift_signal=0.004)
    # tamper with one task before any worker claims it: the Worker must refuse it
    tid = led.conn.execute("SELECT id FROM trials WHERE status='PENDING' ORDER BY id LIMIT 1").fetchone()[0]
    task = json.loads(led.conn.execute("SELECT task_json FROM trials WHERE id=?", (tid,)).fetchone()[0])
    task["expression"] = "Log($volume)"
    with led._tx() as c:
        c.execute("UPDATE trials SET task_json=? WHERE id=?", (json.dumps(task), tid))
    w = Worker(led, panel, "w", keystore=ks)
    while w.run_once() is not None:
        pass
    bad = led.get_trial(tid)
    assert bad["status"] == "ERROR" and "task bundle rejected" in (bad["error"] if "error" in bad else json.dumps(bad))
    ev = led.conn.execute("SELECT COUNT(*) FROM trials WHERE status='EVALUATED'").fetchone()[0]
    assert ev >= 3
    # edit an evaluated return vector after the fact: the Auditor must reject that row on its signature
    victim = led.conn.execute("SELECT id FROM trials WHERE status='EVALUATED' ORDER BY id LIMIT 1").fetchone()[0]
    r = led.get_returns(victim)
    from swarm.shared_ledger import _pack
    with led._tx() as c:
        c.execute("UPDATE returns SET net=? WHERE trial_id=?", (_pack(r["net"] * 1.5), victim))
    Auditor(led, AuditConfig(seed=1, spa_B=100), keystore=ks).audit_pending()
    a = json.loads(led.get_trial(victim)["audit_json"])
    assert led.get_trial(victim)["audit_status"] == "REJECTED" and a["failed_gates"] == ["signature"]
    others = [json.loads(led.get_trial(i[0])["audit_json"]) for i in led.conn.execute("SELECT id FROM trials WHERE audit_status IS NOT NULL AND id<>?", (victim,))]
    assert others and all("signature" in x and ks.verify(__import__("swarm.signing", fromlist=["x"]).audit_payload(
        x_id, x["ast_hash"], x), x["signature"], "auditor")[0] for x_id, x in zip([i[0] for i in led.conn.execute(
            "SELECT id FROM trials WHERE audit_status IS NOT NULL AND id<>? ORDER BY id", (victim,))], others))


def test_trader_rejects_a_verdict_whose_signature_is_invalid(tmp_path):
    ks = KeyStore(str(tmp_path / "keys"))
    led = _pipeline(tmp_path, ks, 4)
    panel = synthetic_panel(600, 50, seed=0, drift_signal=0.004)
    w = Worker(led, panel, "w", keystore=ks)
    while w.run_once() is not None:
        pass
    Auditor(led, AuditConfig(seed=1, spa_B=100), keystore=ks).audit_pending()
    rid = led.conn.execute("SELECT id FROM trials WHERE audit_status IS NOT NULL ORDER BY id LIMIT 1").fetchone()[0]
    a = json.loads(led.get_trial(rid)["audit_json"])
    a["overall_status"] = "APPROVED"                                                                          # forge an approval
    with led._tx() as c:
        c.execute("UPDATE trials SET audit_status='APPROVED', audit_json=? WHERE id=?", (json.dumps(a), rid))
    tr = Trader.from_panel(led, panel, keystore=ks)
    dec = tr.consider(led.get_trial(rid))
    assert dec["decision"] == "REJECTED_BAD_SIGNATURE"


# ------------------------------------------------------------------------------------------------ Gram-Schmidt / MVO / ERC
def test_modified_gram_schmidt_orthogonalises_and_reconstructs():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(60, 30))
    Z = [base, 0.8 * base + 0.2 * rng.normal(size=(60, 30)), rng.normal(size=(60, 30))]
    Q, R = mgs_orthogonalise(Z)
    V = [np.nan_to_num(q).ravel() for q in Q]
    for i in range(3):
        for j in range(i):
            assert abs(V[i] @ V[j]) < 1e-8 * np.linalg.norm(V[i]) * np.linalg.norm(V[j]) + 1e-8
    for k in range(3):                                                                                        # Z_k = sum_j R[j,k] Q_j
        assert np.allclose(np.nan_to_num(Z[k]).ravel(), sum(R[j, k] * V[j] for j in range(k + 1)), atol=1e-8)
    assert np.linalg.norm(V[1]) < 0.5 * np.linalg.norm(np.nan_to_num(Z[1]))                                   # the near-copy has little new content


def test_mgs_keeps_missing_cells_missing():
    rng = np.random.default_rng(1)
    Z = [rng.normal(size=(20, 8)), rng.normal(size=(20, 8))]
    Z[1][3, 4] = np.nan
    Q, _ = mgs_orthogonalise(Z)
    assert np.isnan(Q[1][3, 4]) and np.isfinite(Q[1]).sum() == Z[1].size - 1 and np.isfinite(Q[0]).all()


def test_erc_equalises_risk_contributions_and_mvo_prefers_the_better_factor():
    rng = np.random.default_rng(1)
    A = rng.normal(size=(400, 4)) * np.array([0.5, 1.0, 2.0, 1.5]) + 0.0
    cov = np.cov(A, rowvar=False)
    w = erc_weights(cov)
    rc = w * (cov @ w)
    assert abs(w.sum() - 1) < 1e-9 and (w > 0).all() and rc.std() / rc.mean() < 1e-3                          # equal risk contributions
    mu = np.array([0.0, 0.0, 0.02, 0.0])
    wm = mvo_weights(mu, cov)
    assert abs(wm.sum() - 1) < 1e-9 and (wm >= -1e-12).all() and wm.argmax() == 2
    assert np.allclose(mvo_weights(np.array([-1.0, -2.0]), np.eye(2)), erc_weights(np.eye(2)))                # no positive mean -> ERC fallback
    assert shrink_cov(A).shape == (4, 4) and np.all(np.linalg.eigvalsh(shrink_cov(A)) > 0)
    cw, n = cap_assets(np.array([0.5, 0.3, -0.4, 0.1, 0.05, -0.02]), cap=0.2)
    assert np.abs(cw).max() <= 0.2 + 1e-12 and n >= 2


def test_trader_records_orthogonal_residual_and_stores_an_allocation(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    panel = synthetic_panel(700, 60, seed=0, drift_signal=0.004)
    mn = Miner(led, seed=0)
    for e in ("Log($volume)", "Sub(Log($high), Log($low))", "Div(TsStd($close, 20d), TsStd($volume, 5d))", "Add(TsStd(Log($close), 10d), Log($volume))"):
        mn.screen(e, "t")
    w = Worker(led, panel, "w")
    while w.run_once() is not None:
        pass
    ids = [r[0] for r in led.conn.execute("SELECT id FROM trials WHERE status='EVALUATED'")]
    for i in ids:                                                                                             # force-approve: this tests the Trader only
        led.set_audit(i, "APPROVED", {"overall_status": "APPROVED", "failed_gates": [], "gates": {}, "n_trials_at_audit": 1})
    tr = Trader.from_panel(led, panel, rho_max=0.99, allocation="erc")
    decs = tr.run_once()
    integ = [d for d in decs if d["decision"] == "INTEGRATED"]
    assert integ
    later = [d for d in decs if "orth_residual_frac" in d]
    assert later and all(0.0 <= d["orth_residual_frac"] <= 1.0 + 1e-9 for d in later)
    alloc = led.get_meta("allocation")
    assert alloc["method"] == "erc" and abs(sum(alloc["weights"].values()) - 1) < 1e-9 and alloc["n_factors"] == len(led.pool_members())
    assert alloc["max_abs_asset_weight"] <= 0.05 + 1e-9
    assert set(alloc["weights"]) == {m["ast_hash"] for m in led.pool_members()}
    mvo = tr.allocate("mvo")
    assert abs(sum(mvo["weights"].values()) - 1) < 1e-9 and tr.allocate("equal")["method"] == "equal"


# ------------------------------------------------------------------------------------------------ Redis
def _redis_variants():
    import shutil
    v = ["fakeredis"]
    if shutil.which("redis-server"):
        v.insert(0, "redis-server")
    return v


@pytest.mark.parametrize("kind", _redis_variants())
def test_redis_queue_lock_heartbeat_counter_and_degradation(kind, tmp_path):
    from swarm.redis_coord import Coordinator, EmbeddedRedis
    with EmbeddedRedis(prefer=kind) as srv:
        assert srv.kind == kind
        c = Coordinator(srv.url, "t", node="n1")
        c2 = Coordinator(srv.url, "t", node="n2")
        for i in (3, 1, 2):
            c.push_task(i)
        assert c.queue_len() == 3 and [c2.pop_task() for _ in range(4)] == [3, 1, 2, None]
        c.resync([7, 8]); assert c.queue_len() == 2
        with c.lock("audit", ttl_ms=5000) as got1:                                                            # mutual exclusion across clients
            assert got1
            with c2.lock("audit", ttl_ms=5000, wait_s=0.2) as got2:
                assert not got2
        with c2.lock("audit", ttl_ms=5000) as got3:
            assert got3                                                                                       # released properly
        with c.lock("short", ttl_ms=100) as g:
            time.sleep(0.25)
            with c2.lock("short", ttl_ms=5000) as g2:
                assert g and g2                                                                               # TTL expiry frees a crashed holder's lock
        c.heartbeat("worker", "x"); c2.heartbeat("auditor", "y")
        assert len(c.live_nodes()) == 2
        c.incr_n(5); c.incr_n(2)
        assert c.n_counter() == 7 and c.reconcile_n(10) == -3 and c.n_counter() == 10                          # drift reported, SQLite value wins
    assert srv._proc is None or srv._proc.poll() is not None                                                   # server stopped
    c.push_task(1)                                                                                             # server is gone: degrade, do not raise
    assert c.pop_task() is None and c.ok is False
    with c.lock("x") as g:
        assert g is True                                                                                       # no Redis -> SQLite BEGIN IMMEDIATE still serialises


def test_claim_with_redis_hint_is_still_decided_by_sqlite(tmp_path):
    from swarm.redis_coord import Coordinator, EmbeddedRedis
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    with EmbeddedRedis() as srv:
        coord = Coordinator(srv.url, "q")
        mn = Miner(led, seed=0, coordinator=coord)
        tasks = mn.propose_batch(5, max_attempts=100)
        assert coord.queue_len() == 5 and coord.n_counter() >= 5
        ids = [t["trial_id"] for t in tasks]
        got = [led.claim_task("a", hint_id=ids[2]), led.claim_task("b", hint_id=ids[2])]                      # same hint twice: only one worker gets it
        assert got[0]["trial_id"] == ids[2] and got[1]["trial_id"] != ids[2]
        assert led.claim_task("c", hint_id=999999) is not None                                                 # stale/bogus hint falls back to the SQLite queue
        coord.resync([])                                                                                      # lost queue -> workers still find work in SQLite
        assert led.claim_task("d", hint_id=coord.pop_task()) is not None


# ------------------------------------------------------------------------------------------------ DuckDB
def test_duckdb_blacklist_matches_novelty_memory_and_funnel_reports(tmp_path):
    from swarm.analytics import Analytics
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    mn = Miner(led, seed=0, dsl="mixed")
    mn.propose_batch(60, max_attempts=2500)
    mem = NoveltyMemory(min_ted=mn.memory.min_ted)
    for _id, h, canon in led.history_since(0):
        mem.add(parse_any(canon), h)
    an = Analytics(str(tmp_path / "a.duckdb"))
    s = an.sync(led)
    assert s["new_trials"] == led.n_swarm_trials() and an.n_memory() == len(mem)
    assert an.subtree_blacklist(mem.support_max, mem.min_history) == mem.blacklist()                          # SQL == in-process definition
    some = next(iter(mem.support))
    assert abs(an.subtree_support(some) - mem.support[some] / len(mem)) < 1e-12
    assert an.sync(led)["new_trials"] == 0                                                                    # incremental
    f = an.funnel()
    assert sum(r["proposed"] for r in f) == led.n_swarm_trials()
    an.close()
    an2 = Analytics(str(tmp_path / "a.duckdb"), read_only=True)                                               # persisted, readable read-only
    assert an2.n_memory() == len(mem)


# ------------------------------------------------------------------------------------------------ publisher PIT hash
def test_publisher_pit_hash_is_reproducible():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "engine"))
    from vault.publisher import pit_hash
    r = np.random.default_rng(0).normal(size=50)
    h = pit_hash("Log($volume)", r, "2026-10-24T00:00:00Z")
    assert h == pit_hash("Log($volume)", r.copy(), "2026-10-24T00:00:00Z") and len(h) == 64
    assert h != pit_hash("Log($volume)", r * 1.0000001, "2026-10-24T00:00:00Z") and h != pit_hash("Log($low)", r, "2026-10-24T00:00:00Z")
    assert h != pit_hash("Log($volume)", r, "2026-10-24T00:00:01Z")
