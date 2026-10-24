"""Auditor gates on known-null vs known-signal data, and the Trader's correlation / delta-IC logic."""
import json
import os
import sys
import tempfile

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from swarm.auditor import AuditConfig, Auditor, audit_cohort, gate_cpcv, spa_candidate_pvalues  # noqa: E402
from swarm.data import synthetic_panel  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402
from swarm.trader import Trader, panel_signal_fn, pairwise_signal_corr  # noqa: E402
from src.dsl.grammar import parse_expr  # noqa: E402
from swarm.ast_json import node_hash, node_to_json  # noqa: E402

T = 500


def _items(rng, n_null, signal_sr=None, tag=0):
    its = []
    for i in range(n_null):
        r = rng.normal(0, 0.01, T)
        its.append({"id": i, "net": r, "gross": r, "turnover": np.zeros(T), "cost_bps": 0.0, "metrics": {"search_sharpe": 0.0}})
    if signal_sr is not None:
        r = rng.normal(signal_sr * 0.01, 0.01, T)
        its.append({"id": 999, "net": r, "gross": r, "turnover": np.zeros(T), "cost_bps": 0.0, "metrics": {"search_sharpe": 3.0}})
    return its


def test_known_null_cohorts_produce_zero_survivors():
    cfg = AuditConfig(seed=1, spa_B=300)
    for seed in range(4):
        items = _items(np.random.default_rng(seed), 40)
        res = audit_cohort(items, n_trials=5000, var_sr=float("nan"), n_var=0, cfg=cfg)
        assert sum(v["overall_status"] == "APPROVED" for v in res.values()) == 0
        # every rejected record says which gate failed and carries all four gate results
        assert all(set(v["gates"]) == {"cpcv", "pbo", "dsr", "spa"} and v["failed_gates"] for v in res.values())


def test_known_signal_survives_all_four_gates_among_nulls():
    cfg = AuditConfig(seed=1, spa_B=500)
    items = _items(np.random.default_rng(7), 39, signal_sr=0.28)                  # annual Sharpe ~4.4 planted
    res = audit_cohort(items, n_trials=300, var_sr=float("nan"), n_var=0, cfg=cfg)
    sig = res[999]
    assert sig["overall_status"] == "APPROVED", json.dumps(sig["gates"], default=float)[:800]
    assert [i for i, v in res.items() if v["overall_status"] == "APPROVED"] == [999]


def test_dsr_gate_uses_global_trial_count():
    cfg = AuditConfig(seed=1, spa_B=300)
    items = _items(np.random.default_rng(7), 39, signal_sr=0.17)                  # marginal edge
    few = audit_cohort(items, n_trials=10, var_sr=1.0 / T, n_var=50, cfg=cfg, targets={999})[999]["gates"]["dsr"]
    many = audit_cohort(items, n_trials=10_000_000, var_sr=1.0 / T, n_var=50, cfg=cfg, targets={999})[999]["gates"]["dsr"]
    assert many["p_value"] > few["p_value"] and many["n_trials"] == 10_000_000
    assert not many["pass"]                                                         # an enormous search budget deflates it away


def test_cpcv_purges_training_rows_and_rejects_sign_flipping_series():
    rng = np.random.default_rng(3)
    drift = np.concatenate([np.full(T // 2, 0.004), np.full(T // 2, -0.004)])        # edge flips sign mid-sample: sign cannot generalise
    g = drift + rng.normal(0, 0.01, T)
    out = gate_cpcv(g, np.zeros(T), 0.0, AuditConfig())
    assert out["n_paths"] == 9 and out["n_splits"] == 45
    assert not out["pass"] or out["frac_paths_positive"] < 1.0
    good = rng.normal(0.004, 0.01, T)
    assert gate_cpcv(good, np.zeros(T), 0.0, AuditConfig())["pass"]


def test_cpcv_split_really_purges_and_embargoes():
    from src.validation.cpcv import cpcv_splits
    for s in cpcv_splits(T, 10, 2, 20, 5):
        te = np.where(s["test"])[0]
        tr = np.where(s["train"])[0]
        assert not (set(te) & set(tr))
        trs = set(tr.tolist())
        for a in te:                                                              # nothing within 20 rows before / 5 rows after a test row trains
            assert not (trs & set(range(max(0, a - 20), min(T, a + 6))))


def test_spa_candidate_p_is_family_wise():
    rng = np.random.default_rng(0)
    D = rng.normal(0, 0.01, (T, 60))
    p = spa_candidate_pvalues(D, B=400, seed=0)
    assert (p["p_candidate"] <= 0.05).sum() <= 6 and p["p_cohort"] > 0.01             # nothing systematically significant under the null
    D[:, 5] += 0.004
    q = spa_candidate_pvalues(D, B=400, seed=0)
    assert q["p_candidate"][5] < 0.05


def test_auditor_reads_ledger_and_writes_verdicts():
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        led.set_baseline({"engine_n": 1498, "sde_n": 0, "note": "t"})
        rng = np.random.default_rng(0)
        for i in range(12):
            tid = led.record_proposal(f"Log($close)#{i}", "t", "m", "PENDING", ast_hash=f"h{i}", canonical=f"c{i}", ast_json={"x": 1}, task_json={})
            t = led.claim_task("w")
            r = rng.normal(0, 0.01, T)
            led.complete_task(t["trial_id"], "w", metrics={"cost_bps": 5.0, "search_sharpe": 0.1}, net=r, gross=r, turnover=np.zeros(T), sharpe_daily=float(r.mean() / r.std()), sign=1)
        out = Auditor(led, AuditConfig(spa_B=200)).audit_pending()
        assert out["audited"] == 12 and out["approved"] == []
        assert led.counts()["by_audit"] == {"REJECTED": 12}
        a = json.loads(led.get_trial(1)["audit_json"])
        assert a["n_trials_at_audit"] == 1498 + 12                                   # global N = baseline offset + swarm rows


# ------------------------------------------------------------------ trader
def _trader(led, panel, **kw):
    return Trader.from_panel(led, panel, **kw)


def _row(led, expr):
    n = parse_expr(expr)
    tid = led.record_proposal(expr, "t", "m", "PENDING", ast_hash=node_hash(n), canonical=n.canonical(), ast_json=node_to_json(n), task_json={})
    return {"id": tid, "ast_hash": node_hash(n), "canonical": n.canonical(), "sign": 1}


def test_trader_enforces_rho_below_030_and_positive_delta_ic():
    panel = synthetic_panel(900, 80, seed=4, drift_signal=0.004)
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        tr = _trader(led, panel)
        a = tr.consider(_row(led, "Log($volume)"))
        assert a["decision"] == "INTEGRATED" and a["delta_ic"] > 0 and a["pool_size_before"] == 0
        # Log(2v) = Log(v) + const  ->  cross-sectional correlation 1  -> rejected by the rho < 0.30 rule
        b = tr.consider(_row(led, "Log(Add($volume, $volume))"))
        assert b["decision"] == "REJECTED_CORRELATED" and b["max_abs_rho"] >= 0.30
        # an independent noise formula is uncorrelated with the pool, but adds no information -> rejected on delta-IC (or integrated if lucky: then it must have delta_ic > 0)
        c = tr.consider(_row(led, "TsStd(Log($close), 20d)"))
        assert c["max_abs_rho"] < 0.30
        assert (c["decision"] == "INTEGRATED") == (c["delta_ic"] > 0)
        assert [m["canonical"] for m in led.pool_members()][0] == "Log($volume)"
        assert led.get_trial(a["trial_id"])["trader_status"] == "INTEGRATED"


def test_pairwise_corr_and_pool_cap():
    panel = synthetic_panel(400, 60, seed=1)
    f = panel_signal_fn(panel)
    z1, z2 = f("Log($volume)", 1), f("Log($volume)", -1)
    assert abs(pairwise_signal_corr(z1, z1) - 1) < 1e-9 and abs(pairwise_signal_corr(z1, z2) + 1) < 1e-9
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        tr = _trader(led, synthetic_panel(900, 80, seed=4, drift_signal=0.004), pool_cap=0)
        assert tr.consider(_row(led, "Log($volume)"))["decision"] == "REJECTED_POOL_FULL"
