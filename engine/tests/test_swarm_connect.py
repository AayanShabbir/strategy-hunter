"""SDE <-> swarm connection: live N baseline, degenerate-formula rejection, GFlowNet policy as a proposal source, LLM-sourced proposals
through the ledger, the one-global-count mirror (no double counting) and the SDE-vs-swarm evaluator cross-check."""
import json
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.audit.ledger import Ledger as SdeLedger  # noqa: E402
from swarm.auditor import AuditConfig, Auditor  # noqa: E402
from swarm.data import synthetic_panel  # noqa: E402
from swarm.llm import MailboxLLM  # noqa: E402
from swarm.miner import Miner  # noqa: E402
from swarm.sde_bridge import PolicySource, global_count, load_pool, mirror_to_sde, resolve_run  # noqa: E402
from swarm.shared_ledger import SharedLedger, compute_baseline  # noqa: E402
from swarm.simplify import degenerate_reasons  # noqa: E402
from swarm.worker import Worker, evaluate_formula  # noqa: E402
from src.dsl.grammar import parse_expr  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _engine_state(tmp_path, n):
    p = tmp_path / "state.json"
    p.write_text(json.dumps({"N": n}))
    return str(p)


def _sde(tmp_path, n_own=5):
    led = SdeLedger(tmp_path / "sde.jsonl")
    for i in range(n_own):
        led.append(dict(kind="trial", run_id="r", universe="sp500", ast=f"Log($close{'' if i == 0 else ''})", ast_hash=f"h{i}", ic=0.01))
    led.append(dict(kind="p3_eval", run_id="r"))                                  # non-trial kinds are never counted
    return led


# ------------------------------------------------------------------------------------------------ live baseline
def test_baseline_is_read_live_and_excludes_swarm_mirrored(tmp_path):
    es, sde = _engine_state(tmp_path, 100), _sde(tmp_path, 5)
    b = compute_baseline(es, str(sde.path))
    assert (b["engine_n"], b["sde_n"], b["swarm_mirrored_in_sde_ledger"], b["live"]) == (100, 5, 0, True)
    sde.append(dict(kind="trial", origin="swarm", universe="swarm:sp500", ast_hash="x"))        # a mirrored swarm row is NOT baseline
    sde.append(dict(kind="trial", run_id="r2", universe="sp500", ast_hash="y"))                  # a new SDE trial IS
    b = compute_baseline(es, str(sde.path))
    assert (b["sde_n"], b["swarm_mirrored_in_sde_ledger"]) == (6, 1)
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(es, str(sde.path))
    assert led.baseline_n() == 106
    sde.append(dict(kind="trial", run_id="r2", universe="sp500", ast_hash="z"))
    assert led.baseline_n() == 106                                                             # stored value is stable between refreshes
    assert led.maybe_refresh_baseline(0.0) and led.baseline_n() == 107                         # ... and re-read live on demand
    hist = led.get_meta("baseline_history")
    assert hist and hist[-1]["sde_n"] == 6                                                     # the previous value is kept for audit


def test_pinned_baseline_is_not_refreshed(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 7, "sde_n": 3, "note": "pinned"})
    assert not led.maybe_refresh_baseline(0.0) and led.baseline_n() == 10


def test_real_baseline_matches_a_fresh_scan_of_the_real_files():
    b = compute_baseline()
    assert b["engine_n"] >= 0 and b["sde_n"] >= 0 and b["live"]
    assert b["sde_n"] != 84_610 or b["engine_n"] != 0                                         # not the frozen historic number by construction


# ------------------------------------------------------------------------------------------------ degenerate formulas
@pytest.mark.parametrize("expr,why", [("Sub($close, $close)", "self_cancel"), ("Div($volume, $volume)", "self_ratio"),
                                      ("Add(Sub(Log($high), Log($high)), Log($low))", "self_cancel"), ("Log(Sub($low, $low))", "self_cancel")])
def test_degenerate_formulas_are_detected(expr, why):
    assert why in degenerate_reasons(parse_expr(expr))


def test_sane_formulas_are_not_degenerate():
    for e in ("Sub($close, $low)", "Div(TsStd($close, 20d), TsStd($volume, 5d))", "Log(Add($high, $low))"):
        assert degenerate_reasons(parse_expr(e)) == []


def test_miner_rejects_degenerate_free_and_reports(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    mn = Miner(led, seed=0)
    n0 = led.n_trials()
    r = mn.screen("Sub($close, $close)", "sde_pool")
    assert r["status"] == "REJECTED_DEGENERATE" and r["trial_id"] is None and r["assignment"] is None
    assert led.n_trials() == n0                                                                # cost no trial
    assert mn.stats["degenerate"] and any(e["kind"] == "degenerate_rejected" for e in led.events("degenerate_rejected"))
    ok = mn.screen("Sub($close, $low)", "sde_pool")
    assert ok["assignment"] and led.n_trials() == n0 + 1
    # SDE pool import: degenerate members are skipped for free, the rest are proposed once, re-import is a no-op
    members = [{"expr": "Sub($high, $high)", "ast_hash": "a"}, {"expr": "Log($volume)", "ast_hash": "b"}]
    got = mn.import_sde_pool(members)
    assert len(got) == 1 and led.n_trials() == n0 + 2 and mn.import_sde_pool(members) == []


def test_worker_refuses_a_degenerate_task_even_if_it_slipped_through():
    from swarm.worker import EvalError
    with pytest.raises(EvalError, match="degenerate"):
        evaluate_formula(parse_expr("Sub($close, $close)"), synthetic_panel(300, 40, seed=0))


# ------------------------------------------------------------------------------------------------ LLM-sourced proposals through the ledger
def test_llm_sourced_proposals_flow_through_ledger_worker_auditor(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 10, "sde_n": 20})
    root = str(tmp_path / "mb")
    mn = Miner(led, seed=0, llm=MailboxLLM(root), llm_min_interval_s=0.0, llm_n=3)
    rid = mn.request_llm("propose", "momentum")
    exprs = ["Div(TsStd($close, 20d), $volume)", "Log($volume)", "Sub($close, $close)", "Foo($close)"]
    body = {"protocol": 1, "id": rid, "responder": "agent", "created_utc": "2026-10-24T00:00:00Z", "status": "ok", "notes": "",
            "proposals": [{"expression": e, "hypothesis": "h"} for e in exprs]}
    json.dump(body, open(os.path.join(root, "responses", rid + ".tmp"), "w"))
    os.replace(os.path.join(root, "responses", rid + ".tmp"), os.path.join(root, "responses", rid + ".json"))
    n0 = led.n_swarm_trials()
    tasks = mn.ingest_llm()
    src = f"llm:{rid}"
    assert len(tasks) == 2 and all(t["source"] == src for t in tasks)
    rows = led.conn.execute("SELECT source, status FROM trials WHERE source=?", (src,)).fetchall()
    assert len(rows) == 3                                                                      # 2 accepted + the excess 4th proposal (llm_n=3, counted, never evaluated); the degenerate one is free
    assert led.n_swarm_trials() - n0 == 3 and led.n_trials() == 30 + led.n_swarm_trials()     # global N includes LLM proposals
    assert mn.stats["by_source"]["llm"]["proposed"] == 3 and mn.stats["by_source"]["llm"]["accepted"] == 2
    panel = synthetic_panel(700, 60, seed=0, drift_signal=0.004)
    w = Worker(led, panel, "w0")
    while w.run_once() is not None:
        pass
    ev = led.conn.execute("SELECT COUNT(*) FROM trials WHERE source=? AND status='EVALUATED'", (src,)).fetchone()[0]
    assert ev == 2
    res = Auditor(led, AuditConfig(seed=1, spa_B=100)).audit_pending()
    assert res["audited"] == 2
    audited = led.conn.execute("SELECT source, audit_status FROM trials WHERE audit_status IS NOT NULL").fetchall()
    assert {r["source"] for r in audited} == {src} and all(r["audit_status"] in ("APPROVED", "REJECTED") for r in audited)
    assert json.loads(led.conn.execute("SELECT audit_json FROM trials WHERE audit_status IS NOT NULL").fetchone()[0])["n_trials_at_audit"] >= 33


# ------------------------------------------------------------------------------------------------ GFlowNet policy as a proposal source
@pytest.fixture
def fake_run(tmp_path):
    import torch
    from src.gflownet.policy import GFlowNetPolicy
    d = tmp_path / "runs" / "sp500_s0_20260101"
    d.mkdir(parents=True)
    torch.save(GFlowNetPolicy(seed=0).state_dict(), d / "policy.pt")
    (d / "config.json").write_text(json.dumps({"seed": 0, "universe": "sp500"}))
    (d / "pool.json").write_text(json.dumps({"members": [{"expr": "Log($volume)", "ast_hash": "q", "train_ic": 0.02}]}))
    return tmp_path / "runs"


def test_policy_source_resolves_runs_and_samples_valid_sde_formulas(fake_run):
    assert resolve_run("sp500_s0", fake_run).name == "sp500_s0_20260101"
    assert resolve_run(str(fake_run / "sp500_s0_20260101")).name == "sp500_s0_20260101"
    with pytest.raises(FileNotFoundError):
        resolve_run("nope", fake_run)
    p = PolicySource("sp500_s0", seed=1, runs_dir=fake_run)
    xs = [p.sample() for _ in range(5)]
    assert all(parse_expr(x).size() <= 32 for x in xs)
    p2 = PolicySource("sp500_s0", seed=1, runs_dir=fake_run)
    assert [p2.sample() for _ in range(5)] == xs                                              # seeded => reproducible
    assert load_pool("sp500_s0", fake_run)[0]["expr"] == "Log($volume)"


def test_policy_samples_pass_the_same_gates_and_are_counted_with_their_source(fake_run, tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    pol = PolicySource("sp500_s0", seed=3, runs_dir=fake_run)
    mn = Miner(led, seed=0, policy=pol, policy_share=1.0)
    tasks = mn.propose_batch(6, max_attempts=300)
    assert len(tasks) == 6 and all(t["source"] == "sde_policy" for t in tasks)
    assert pol.n_sampled >= 6
    # same constraints as every other source: pairwise TED >= 0.35 and no duplicates of earlier accepted formulas
    from swarm.novelty import normalized_ted
    nodes = [parse_expr(t["expression"]) for t in tasks]
    assert all(normalized_ted(nodes[i], nodes[j]) >= 0.35 - 1e-12 for i in range(len(nodes)) for j in range(i))
    assert led.n_swarm_trials() == mn.stats["generated"]                                       # every costed sample is a ledger row
    assert mn.stats["by_source"]["sde_policy"]["accepted"] == 6
    # an SDE-ledger duplicate is rejected unless it is an explicit pool re-evaluation (allow_seen)
    from swarm.dialect import hash_any
    led2 = SharedLedger(str(tmp_path / "t2.db"))
    led2.refresh_baseline(baseline={"engine_n": 0, "sde_n": 0})
    h = hash_any(parse_expr("Log($volume)"))
    m2 = Miner(led2, seed=0, sde_seen={h})
    r = m2.screen("Log($volume)", "sde_policy")
    assert r["assignment"] is None and r["reason"] == "sde_seen"
    assert m2.screen("Log($volume)", "sde_pool", allow_seen=True)["assignment"]


@pytest.mark.skipif(not os.path.exists(os.path.join(REPO, "runs_sde", "sp500_s2_20261024", "policy.pt")), reason="trained policy not on this checkout")
def test_real_trained_policy_loads_and_samples():
    p = PolicySource("sp500_s2")
    for _ in range(3):
        parse_expr(p.sample())


# ------------------------------------------------------------------------------------------------ one global count, no double counting
def test_mirror_gives_one_global_count_and_is_idempotent(tmp_path):
    es, sde = _engine_state(tmp_path, 40), _sde(tmp_path, 5)
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(es, str(sde.path))
    mn = Miner(led, seed=0)
    mn.propose_batch(8, max_attempts=200)
    mn.screen("Foo(", "test")                                                                  # a counted reject
    n_before = led.n_trials()
    assert n_before == 40 + 5 + led.n_swarm_trials()
    g0 = global_count(led, str(sde.path), es)
    assert not g0["in_sync"] and g0["unmirrored"] == led.n_swarm_trials()
    out = mirror_to_sde(led, str(sde.path))
    assert out["mirrored_trials"] == led.n_swarm_trials()
    led.maybe_refresh_baseline(0.0)
    assert led.n_trials() == n_before                                                          # N identical before/after mirroring (no double count)
    g = global_count(led, str(sde.path), es)
    assert g["in_sync"] and g["n_global_swarm_view"] == g["n_global_sde_view"] == n_before and g["unmirrored"] == 0
    assert mirror_to_sde(led, str(sde.path))["mirrored_trials"] == 0                          # idempotent
    mn.screen("Log($volume)", "test")
    assert mirror_to_sde(led, str(sde.path))["mirrored_trials"] == 1                          # resumes from the SDE ledger itself
    assert SdeLedger(sde.path).verify()[0]                                                     # hash chain intact
    assert SdeLedger(sde.path).count("trial") == 5 + led.n_swarm_trials()                      # the SDE's own N now includes the swarm
    # SDE tooling ignores mirrored rows where it must: no `ic`, distinct universe
    from src.train.phase3_eval import ledger_trials
    trials, n_total, n_uni = ledger_trials(SdeLedger(sde.path), "sp500")
    assert n_total == 5 + led.n_swarm_trials() and n_uni == 5 and len(trials) == 5


def test_mirror_writes_audit_verdicts_as_non_trial_kind(tmp_path):
    es, sde = _engine_state(tmp_path, 0), _sde(tmp_path, 0)
    led = SharedLedger(str(tmp_path / "t.db"))
    led.refresh_baseline(es, str(sde.path))
    mn = Miner(led, seed=0)
    mn.propose_batch(4, max_attempts=100)
    w = Worker(led, synthetic_panel(500, 50, seed=0), "w")
    while w.run_once() is not None:
        pass
    Auditor(led, AuditConfig(seed=1, spa_B=100)).audit_pending()
    out = mirror_to_sde(led, str(sde.path))
    assert out["mirrored_audits"] == 4
    kinds = [e["kind"] for e in SdeLedger(sde.path).entries() if e.get("origin") == "swarm"]
    assert kinds.count("swarm_audit") == 4 and kinds.count("trial") == led.n_swarm_trials()
    assert mirror_to_sde(led, str(sde.path)) == {"mirrored_trials": 0, "mirrored_audits": 0, "sde_ledger": str(sde.path)}


# ------------------------------------------------------------------------------------------------ evaluator cross-check
def test_swarm_and_sde_evaluators_agree_on_returns():
    """The Worker reuses src.portfolio (zscore/weights/backtest); only the formula evaluator differs (torch vs numpy).
    For several formulas the swarm net-return vector must equal the SDE's `trial_returns` on the same panel."""
    from src.train.phase3_eval import trial_returns
    from src.portfolio.long_short import tradable_mask
    panel = synthetic_panel(500, 50, seed=4, drift_signal=0.003)
    trad = tradable_mask(panel)
    a0 = panel.start_idx
    for e in ("Log($volume)", "Div(TsStd($close, 20d), TsStd($volume, 5d))", "Sub(Log($high), Log($low))", "Add(TsStd(Log($close), 10d), Log($volume))"):
        r = evaluate_formula(parse_expr(e), panel)
        sde_net = trial_returns(panel, trad, e, r["sign"], 5.0)[a0:]
        assert len(sde_net) == len(r["net"]) and np.allclose(sde_net, r["net"], rtol=1e-6, atol=1e-10), e


def test_swarm_and_sde_ast_hashes_agree():
    from src.dsl.grammar import ast_hash
    from swarm.dialect import hash_any
    for e in ("Log($volume)", "Div(TsStd($close, 20d), TsStd($volume, 5d))"):
        assert hash_any(parse_expr(e)) == ast_hash(parse_expr(e))


def test_sde_pool_members_reevaluate_through_the_swarm_worker(fake_run):
    members = load_pool("sp500_s0", fake_run)
    r = evaluate_formula(parse_expr(members[0]["expr"]), synthetic_panel(400, 40, seed=0))
    assert np.isfinite(r["net"]).all() and r["sign"] in (-1, 1)
