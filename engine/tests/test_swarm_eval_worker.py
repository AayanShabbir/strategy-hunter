"""Tensor evaluator vs the SDE numpy evaluator, worker pipeline, and the search-window isolation guarantee."""
import os
import re
import sys
import tempfile

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.dsl.grammar import evaluate, parse_expr, random_expr  # noqa: E402
from swarm.data import SEARCH_END, build_search_panel, synthetic_panel  # noqa: E402
from swarm.miner import Miner  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402
from swarm.tensor_eval import evaluate_numpy  # noqa: E402
from swarm.worker import Worker, evaluate_formula  # noqa: E402

SWARM_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "swarm")


def test_tensor_evaluator_matches_sde_evaluator():
    import random
    panel = synthetic_panel(300, 20, seed=1)
    rng = np.random.default_rng(5)
    for _ in range(25):
        e = random_expr(rng)
        a, b = evaluate(e, panel.data), evaluate_numpy(parse_expr(e), panel.data)
        both = np.isfinite(a) & np.isfinite(b)
        assert (np.isfinite(a) == np.isfinite(b)).mean() > 0.999, e
        assert np.allclose(a[both], b[both], rtol=1e-6, atol=1e-8), e


def test_tensor_evaluator_is_causal():
    p = synthetic_panel(200, 10, seed=2)
    n = parse_expr("Div(TsStd(Log($close), 20d), TsStd($volume, 5d))")
    full = evaluate_numpy(n, p.data)
    cut = {k: v[:150].copy() for k, v in p.data.items()}
    part = evaluate_numpy(n, cut)
    both = np.isfinite(part)
    assert np.allclose(full[:150][both], part[both], rtol=1e-9)                      # future rows never change the past


def test_worker_logs_return_vectors_and_metrics():
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        panel = synthetic_panel(700, 60, seed=0, drift_signal=0.004)
        mn = Miner(led, seed=0)
        mn.propose_batch(5)
        mn.screen("Log($volume)", "test")
        w = Worker(led, panel, "w0")
        done = 0
        while w.run_once() is not None:
            done += 1
        assert done == 6
        c = led.counts()["by_status"]
        assert c.get("EVALUATED", 0) + c.get("ERROR", 0) == 6
        t = led.evaluated_unaudited()[0]
        r = led.get_returns(t["id"])
        T = panel.n_days - 1 - panel.start_idx
        assert len(r["net"]) == len(r["gross"]) == len(r["turnover"]) == T and np.isfinite(r["net"]).all()
        import json
        m = json.loads(t["metrics_json"])
        for k in ("search_sharpe", "annualized_turnover", "max_drawdown", "sign", "cost_bps", "worker", "device"):
            assert k in m
        # the planted volume edge is found: Log($volume) has positive net Sharpe
        lv = [x for x in led.evaluated_unaudited() if x["canonical"] == "Log($volume)"][0]
        assert lv["sharpe_daily"] > 0.05


def test_sign_is_chosen_on_train_only():
    panel = synthetic_panel(700, 60, seed=0, drift_signal=-0.004)               # inverted edge: sign must flip to -1
    from swarm.ast_json import payload_to_node  # noqa: F401
    r = evaluate_formula(parse_expr("Log($volume)"), panel)
    assert r["sign"] == -1 and r["metrics"]["search_sharpe"] > 0


def test_panel_never_contains_test_years_and_code_never_loads_them():
    for fn in sorted(os.listdir(SWARM_DIR)):
        if fn.endswith(".py"):
            src = open(os.path.join(SWARM_DIR, fn)).read()
            assert "allow_vault" not in src.replace("allow_vault=False", ""), fn
            code = re.sub(r"#.*|\"\"\"[\s\S]*?\"\"\"|'[^']*2018-2020[^']*'|\"[^\"]*2018-2020[^\"]*\"", "", src)
            code = code.replace('load_sp500(end="2020-12-31")', "")    # the only mention: the cached SDE pickle, truncated at once (see data._from_sde)
            assert not re.search(r"2018|2019|2020", code), fn
            assert "vault_test" not in src and "vault.seal" not in src, fn
    if os.path.exists(os.path.join(os.path.dirname(SWARM_DIR), "..", "data", "swarm", "cache", "sp500_search_panel.npz")):
        p = build_search_panel()
        assert str(p.dates[-1]) <= SEARCH_END
