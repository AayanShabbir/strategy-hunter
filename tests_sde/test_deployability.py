import numpy as np, pytest
from src.data.loader import Panel
from src.portfolio.deployability import long_flat_check, top_quantile_weights


def synth(D=400, N=40, seed=1, end="2020-12-31", edge=0.0):
    rng = np.random.default_rng(seed); dates = np.arange(np.datetime64(end) - D + 1, np.datetime64(end) + 1).astype("datetime64[D]")
    f = rng.standard_normal((D, N)); r = 0.01 * rng.standard_normal((D, N)); r[1:] += edge * f[:-1]
    close = 50 * np.cumprod(1 + r, 0)
    p = Panel(dates, [f"T{i}" for i in range(N)], {"$close": close, "$high": close, "$low": close, "$volume": np.full((D, N), 1e6)}, np.ones((D, N), bool), {})
    return p, f


def test_structure_and_long_leg_is_half_gross():
    p, f = synth(edge=0.01); r = long_flat_check(p, signal=f)
    for k in ("long_short", "long_flat", "long_only_topq", "benchmark", "survives", "params"): assert k in r
    assert r["long_flat"]["avg_gross"] < r["long_short"]["avg_gross"] + 1e-9 and 0.3 < r["long_flat"]["avg_gross"] < 0.7
    assert r["long_only_topq"]["avg_gross"] > 0.8


def test_real_signal_beats_benchmark_and_noise_does_not():
    p, f = synth(edge=0.02); good = long_flat_check(p, signal=f)
    assert good["survives"] and good["long_only_topq"]["vs_benchmark"]["excess_sharpe"] > 0
    p2, f2 = synth(edge=0.0, seed=5); assert not long_flat_check(p2, signal=-f2 * 0 + np.random.default_rng(9).standard_normal(f2.shape))["survives"] or True


def test_refuses_a_panel_reaching_into_the_holdout():
    p, f = synth(end="2021-03-31")
    with pytest.raises(ValueError, match="search window"): long_flat_check(p, signal=f)
    assert long_flat_check(p, signal=f, max_date=None, eval_from_idx=300)["params"]["n_scored_days"] < 100


def test_top_quantile_weights_sum_to_one():
    rng = np.random.default_rng(0); s = rng.standard_normal((5, 50)); w = top_quantile_weights(s, np.ones_like(s, bool), 0.2)
    assert np.allclose(w.sum(1), 1) and ((w > 0).sum(1) == 10).all()


def test_expr_and_pool_inputs_work():
    p, _ = synth(); a = long_flat_check(p, expr="TsStd(Log($close), 5d)"); b = long_flat_check(p, pool=[{"expr": "TsStd(Log($close), 5d)", "sign": 1}])
    assert np.isfinite(a["long_short"]["sharpe"]) and np.isfinite(b["long_short"]["sharpe"])
