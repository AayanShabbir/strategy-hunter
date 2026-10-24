"""Phase 3 tests: long-short leverage-normalized portfolio, combination, DSR, CSCV/PBO, CPCV, SPA, Ville e-process on the ledger."""
import json
from math import comb
import numpy as np, pytest
from scipy import stats
from src.audit.ledger import Ledger
from src.portfolio.long_short import (zscore_rows, leverage_normalized_weights, backtest, metrics, forward_returns, tradable_mask, sharpe_daily)
from src.portfolio.combine import combine_equal, combine_rolling_ols, label_matrix, daily_ic_matrix, member_signals
from src.validation.dsr import expected_max_sr, deflated_sharpe, probabilistic_sharpe
from src.validation.cscv import cscv_pbo
from src.validation.cpcv import cpcv_splits, cpcv_paths, n_paths
from src.validation.spa import spa_test, stationary_bootstrap_idx
from src.validation import eprocess as ep
from tests_sde.test_phase2 import toy_panel


# ------------------------------------------------------------------ weights / backtest
def test_weights_dollar_neutral_unit_gross_and_nan_safe():
    rng = np.random.default_rng(0); S = rng.normal(size=(6, 50)); S[1, :10] = np.nan; S[2] = np.nan; S[3] = 1.0   # row 2 all NaN, row 3 constant
    W = leverage_normalized_weights(S, gross=1.0)
    assert np.allclose(W[[0, 1, 4, 5]].sum(1), 0, atol=1e-12) and np.allclose(np.abs(W[[0, 1, 4, 5]]).sum(1), 1.0)
    assert np.all(W[1, :10] == 0) and np.all(W[2] == 0) and np.all(W[3] == 0)
    assert np.allclose(np.abs(leverage_normalized_weights(S, gross=2.0)[0]).sum(), 2.0)
    assert np.allclose(leverage_normalized_weights(5 * S + 3)[0], W[0])          # invariant to affine scaling of the signal


def test_zscore_rows_min_cross_section_and_moments():
    rng = np.random.default_rng(1); F = rng.normal(5, 3, (4, 60)); valid = np.ones_like(F, bool); valid[3, :40] = False
    Z = zscore_rows(F, valid)
    assert np.allclose(np.nanmean(Z[:3], 1), 0, atol=1e-9) and np.allclose(np.nanstd(Z[:3], 1, ddof=1), 1)
    assert np.all(np.isnan(Z[3]))                                               # only 20 valid < 30


def test_backtest_hand_example_and_costs():
    close = np.array([[100., 100.], [110., 90.], [121., 81.], [133.1, 72.9]])
    W = np.array([[.5, -.5]] * 4)
    bt = backtest(W, close, cost_bps=10.0)
    assert np.allclose(bt["gross"], 0.5 * 0.1 + 0.5 * 0.1)                          # 0.10 each day
    pre1 = np.array([.5 * 1.1, -.5 * 0.9]) / 1.1
    assert np.isclose(bt["turnover"][0], 1.0)                                       # initial build = gross
    assert np.isclose(bt["turnover"][1], np.abs(W[0] - pre1).sum())                 # drifted pre-trade weights
    assert np.allclose(bt["net"], bt["gross"] - 10e-4 * bt["turnover"]) and len(bt["net"]) == 3


def test_no_cost_means_gross_and_cost_monotone():
    p = toy_panel(300, 60, 3); trad = tradable_mask(p); rng = np.random.default_rng(2)
    W = leverage_normalized_weights(zscore_rows(rng.normal(size=p.data["$close"].shape), trad))
    a, b, c = (backtest(W, p.data["$close"], x)["net"].sum() for x in (0, 5, 20))
    assert a > b > c and np.allclose(backtest(W, p.data["$close"], 0)["net"], backtest(W, p.data["$close"], 0)["gross"])


def test_no_lookahead_future_prices_dont_change_past_weights():
    from src.portfolio.combine import factor_matrix
    p = toy_panel(300, 60, 4); trad = tradable_mask(p); expr = "TsStd(Log($volume), 20d)"
    W1 = leverage_normalized_weights(zscore_rows(factor_matrix(p, expr), trad))
    p2 = toy_panel(300, 60, 4)
    for k in p2.data: p2.data[k] = p2.data[k].copy(); p2.data[k][200:] *= 3.7
    W2 = leverage_normalized_weights(zscore_rows(factor_matrix(p2, expr), tradable_mask(p2)))
    assert np.allclose(W1[:200], W2[:200])


def test_perfect_foresight_signal_earns_and_noise_does_not():
    p = toy_panel(400, 80, 5); c = p.data["$close"]; r = forward_returns(c); trad = tradable_mask(p)
    W = leverage_normalized_weights(zscore_rows(np.where(np.isfinite(r), r, np.nan), trad))
    assert metrics(backtest(W, c, 5)["net"])["sharpe"] > 5
    noise = leverage_normalized_weights(zscore_rows(np.random.default_rng(0).normal(size=c.shape), trad))
    assert abs(metrics(backtest(noise, c, 0)["net"])["sharpe"]) < 1.5


def test_metrics_known_values():
    R = np.array([0.01, -0.02, 0.03, 0.0, 0.01]); m = metrics(R, np.ones(5))
    assert np.isclose(m["sharpe"], np.sqrt(252) * R.mean() / R.std(ddof=1)) and np.isclose(m["annual_return"], 252 * R.mean())
    w = np.cumprod(1 + R); dd = 1 - w / np.maximum.accumulate(np.r_[1, w])[1:]; assert np.isclose(m["max_drawdown"], -dd.max())
    assert np.isclose(m["turnover_annual"], 252.0)
    s = metrics(np.array([0.01]))["sharpe"]; assert s != s


# ------------------------------------------------------------------ combination
def _toy_members_data(seed=0, D=700, A=70):
    p = toy_panel(D, A, seed); c = p.data["$close"]; trad = tradable_mask(p)
    Y = label_matrix(c, trad); rng = np.random.default_rng(seed)
    good = np.where(np.isfinite(Y), Y, 0) + rng.normal(0, 3, Y.shape)                 # informative (noisy) factor ~ future label
    bad = rng.normal(size=Y.shape)
    Z = np.stack([zscore_rows(good, trad), zscore_rows(bad, trad)]).astype(np.float32)
    return p, trad, Y, Z


def test_rolling_ols_filters_and_weights_informative_member():
    p, trad, Y, Z = _toy_members_data()
    sig, info = combine_rolling_ols(Z, Y, first_day=0, return_info=True, lookback=250, refresh=20)
    assert len(info["refresh_idx"]) > 5 and all(0 in k for k in info["kept"])
    betas = [b for b in info["betas"] if len(b) == 2]
    if betas: assert np.mean([b[0] for b in betas]) > 3 * abs(np.mean([b[1] for b in betas]))
    assert np.all(np.isnan(sig[:250 + 20]))                                        # nothing before the first refresh


def test_rolling_ols_is_causal_labels_after_t_minus_h_cannot_matter():
    p, trad, Y, Z = _toy_members_data(1)
    s1 = combine_rolling_ols(Z, Y, lookback=200, refresh=20)
    Y2 = Y.copy(); Y2[400:] = np.random.default_rng(9).normal(size=Y2[400:].shape)       # corrupt labels of days >= 400
    s2 = combine_rolling_ols(Z, Y2, lookback=200, refresh=20)
    first_diff = next(t for t in range(len(s1)) if not np.allclose(np.nan_to_num(s1[t]), np.nan_to_num(s2[t])))
    assert first_diff >= 420          # refresh at t uses labels of days <= t-20 only


def test_rolling_ols_drops_negative_ic_members_and_equal_combo_basic():
    p, trad, Y, Z = _toy_members_data(2)
    _, info = combine_rolling_ols(np.stack([-Z[0], Z[1]]), Y, lookback=250, refresh=20, return_info=True)
    assert all(0 not in k for k in info["kept"])                                    # member 0 anti-predictive => filtered out
    e = combine_equal(Z); assert np.allclose(e[300], np.nan_to_num(Z[:, 300]).mean(0), atol=1e-5)
    s0 = combine_rolling_ols(np.zeros((0, 10, 5), np.float32), np.zeros((10, 5))); assert s0.shape == (10, 5) and np.isnan(s0).all()


# ------------------------------------------------------------------ DSR
def test_dsr_n1_equals_psr_and_decreases_with_n():
    rng = np.random.default_rng(0); R = rng.normal(0.001, 0.01, 1000)
    d1 = deflated_sharpe(R, 1, 1e-4); assert np.isclose(d1["dsr"], d1["psr0"]) and d1["sr0"] == 0.0
    ds = [deflated_sharpe(R, n, 1e-4)["dsr"] for n in (1, 10, 1000, 100000)]
    assert all(x >= y for x, y in zip(ds, ds[1:])) and ds[0] > ds[-1]


def test_expected_max_sr_matches_simulation():
    rng = np.random.default_rng(1); N, sd = 500, 0.05
    sim = np.mean([rng.normal(0, sd, N).max() for _ in range(400)])
    assert abs(expected_max_sr(N, sd ** 2) - sim) / sim < 0.08


def test_psr_matches_normal_cdf_closed_form():
    sr, T = 0.1, 400; assert np.isclose(probabilistic_sharpe(sr, T, 0.0, 3.0), stats.norm.cdf(sr * np.sqrt(T - 1) / np.sqrt(1 + sr ** 2 / 2)))
    z = deflated_sharpe(np.zeros(100), 10, 1e-4)["dsr"]; assert z != z                # zero variance -> NaN


# ------------------------------------------------------------------ CSCV / PBO
def test_cscv_noise_pbo_near_half_and_true_edge_near_zero():
    rng = np.random.default_rng(0); noise = rng.normal(0, 0.01, (1600, 30))
    r = cscv_pbo(noise, 16); assert r["n_splits"] == comb(16, 8) and 0.3 < r["pbo"] < 0.7
    edge = noise.copy(); edge[:, 0] += 0.004                                       # one persistently good strategy
    assert cscv_pbo(edge, 16)["pbo"] < 0.05


def test_cscv_overfit_selection_has_high_pbo_and_validates_shapes():
    rng = np.random.default_rng(3); T = 1600; M = rng.normal(0, 0.01, (T, 40))
    M[:T // 2, :10] += 0.01; M[T // 2:, :10] -= 0.01                                # strategies good in first half, bad in second
    assert cscv_pbo(M, 16)["pbo"] > 0.4
    assert np.isnan(cscv_pbo(M[:, :1], 16)["pbo"]) and np.isnan(cscv_pbo(M[:10], 16)["pbo"])


# ------------------------------------------------------------------ CPCV
def test_cpcv_counts_paths_purge_and_coverage():
    T = 1000; sp = cpcv_splits(T, 10, 2, purge=20, embargo=5)
    assert len(sp) == 45 == comb(10, 2) and n_paths(10, 2) == 9
    for s in sp:
        assert not np.any(s["train"] & s["test"]) and s["test"].sum() == 200
        ti = np.flatnonzero(s["test"]); first = ti[0]
        assert not s["train"][max(0, first - 20):first].any()                       # purged before the test block
        gaps = np.flatnonzero(np.diff(ti) > 1)
        end = ti[gaps[0]] if len(gaps) else ti[-1]
        assert not s["train"][end + 1:end + 6].any()                                # embargo after a block
    paths = cpcv_paths(sp, 10); assert len(paths) == 9
    for p in paths:
        assert sorted(g for g, _ in p) == list(range(10)) and all(g in sp[si]["test_groups"] for g, si in p)
    used = [(g, si) for p in paths for g, si in p]; assert len(used) == len(set(used)) == 90


# ------------------------------------------------------------------ SPA
def test_spa_noise_large_p_and_edge_small_p_and_ordering():
    rng = np.random.default_rng(0); noise = rng.normal(0, 0.01, (750, 50))
    r = spa_test(noise, B=400, seed=1); assert r["p_consistent"] > 0.1 and r["p_lower"] <= r["p_consistent"] <= r["p_upper"] + 1e-12
    edge = noise.copy(); edge[:, 7] += 0.002
    r2 = spa_test(edge, B=400, seed=1); assert r2["p_consistent"] < 0.05 and r2["best_candidate"] == 7


def test_spa_all_losers_p_near_one_and_bootstrap_indices_valid():
    rng = np.random.default_rng(1); r = spa_test(rng.normal(-0.003, 0.01, (500, 10)), B=300, seed=0)
    assert r["p_consistent"] > 0.5
    idx = stationary_bootstrap_idx(100, 20, 10.0, np.random.default_rng(0)); assert idx.min() >= 0 and idx.max() < 100 and idx.shape == (20, 100)


# ------------------------------------------------------------------ Ville e-process (Promote)
def test_eprocess_boundary_scale_and_clipping():
    assert np.isclose(ep.boundary(0.05, 1 / 24), 480.0) and np.isclose(ep.boundary(0.05, 1 / 8), 160.0)
    assert ep.predictable_scale(np.zeros(100)) == 0.005 and ep.predictable_scale(np.r_[np.zeros(980), 0.2 * np.ones(20)]) > 0.005
    assert np.allclose(ep.scores(np.array([-1.0, 0.0, 0.0025, 1.0]), 0.005), [-1, 0, 0.5, 1])


def test_eprocess_nonnegative_and_matches_manual_product():
    s = np.array([0.5, -1.0, 1.0, 0.2]); path = ep.mixture_path(s)
    manual = np.mean([np.cumprod(1 + lam * s) for lam in ep.LAMBDAS], 0)
    assert np.allclose(path, manual) and np.all(path > 0)


def test_eprocess_null_false_promotion_rate_below_alpha():
    rng = np.random.default_rng(0); sims, T, alpha = 2000, 750, 0.05; b = ep.boundary(alpha, 1.0); hits = 0
    for _ in range(sims):
        s = rng.choice([-1.0, 1.0], T); hits += ep.first_crossing(ep.mixture_path(s), b) is not None
    assert hits / sims <= alpha                                                     # Ville: <= alpha (usually far below)


def test_eprocess_detects_real_edge_and_delayed_execution(tmp_path):
    rng = np.random.default_rng(1); L = Ledger(tmp_path / "l.jsonl"); n = 750
    net = rng.normal(0.004, 0.01, n); dates = [str(np.datetime64("2022-01-03") + np.timedelta64(i, "D")) for i in range(n)]
    fp = ep.register_candidate(L, "t", dict(rule="demo"), None, "2021-12-31", 1 / 8, 0.01, 0.05, "v1")["fingerprint"]
    r = ep.score_candidate(L, "t", fp, dates, net, 0.0005 * np.ones(n), 0.01, 1 / 8, 0.05, "v1")
    assert r["promoted"] and r["max_evidence"] >= r["boundary"] == 160.0 and r["crossing_index"] < n - 2
    assert r["first_executable_session"] == dates[r["crossing_index"] + 2]
    rows = [e for e in L.entries() if e["kind"] == "escore"]; assert len(rows) == n and rows[0]["evidence"] > 0
    assert sum(e["decision"] == "promote" for e in rows) == 1 and L.verify()[0]


def test_eprocess_budget_debit_and_idempotence(tmp_path):
    L = Ledger(tmp_path / "l.jsonl")
    for i in range(8): ep.register_candidate(L, "p", dict(i=i), None, "2021-12-31", 1 / 8, 0.01, 0.05, "v")
    with pytest.raises(ValueError): ep.register_candidate(L, "p", dict(i=99), None, "2021-12-31", 1 / 8, 0.01, 0.05, "v")
    n_before = sum(1 for _ in L.entries()); ep.register_candidate(L, "p", dict(i=3), None, "2021-12-31", 1 / 8, 0.01, 0.05, "v")
    assert sum(1 for _ in L.entries()) == n_before                                  # same identity: no second debit
    assert np.isclose(ep.cumulative_debit(L, "p"), 1.0)
    fp = ep.candidate_fingerprint(dict(i=3)); d = [str(np.datetime64("2022-01-03") + np.timedelta64(i, "D")) for i in range(5)]
    ep.score_candidate(L, "p", fp, d, np.zeros(5), np.zeros(5), 0.01, 1 / 8, 0.05, "v"); k = sum(1 for _ in L.entries())
    ep.score_candidate(L, "p", fp, d, np.zeros(5), np.zeros(5), 0.01, 1 / 8, 0.05, "v"); assert sum(1 for _ in L.entries()) == k
    assert L.verify()[0] and L.count("trial") == 0


def test_naive_repeated_test_crosses_on_null_far_more_often_than_eprocess():
    rng = np.random.default_rng(0); naive = sum(ep.naive_repeated_test(rng.normal(0, 0.01, 750))["crossed"] for _ in range(100))
    assert naive > 12                                                               # the paper's point: repeated nominal testing inflates FWER


# ------------------------------------------------------------------ pipeline smoke on a toy panel with a patched loader
def test_phase3_pipeline_smoke(tmp_path, monkeypatch):
    import src.train.phase3_eval as P
    D = 6200; p = toy_panel(D, 40, 7)
    p.dates = (np.datetime64("2009-01-01") + np.arange(D)).astype("datetime64[D]")     # calendar days so the real split dates fall in range
    monkeypatch.setattr(P, "load_panel", lambda uni, upto="test": p)
    monkeypatch.setattr(P, "ROOT", tmp_path)
    run = tmp_path / "runs_sde" / "toy"; run.mkdir(parents=True)
    members = [dict(expr="TsStd(Log($volume), 20d)", ast_hash="h1", sign=1), dict(expr="Sub($close, $high)", ast_hash="h2", sign=-1)]
    (run / "config.json").write_text(json.dumps(dict(universe="csi300"))); (run / "pool.json").write_text(json.dumps(dict(members=members, size=2)))
    L = Ledger(tmp_path / "led.jsonl"); rng = np.random.default_rng(0)
    for i in range(300):
        L.append(dict(kind="trial", universe="csi300", ast="TsStd(Log($volume), %dd)" % [5, 10, 20, 60][i % 4] if i % 7 else "Log($high)",
                      ast_hash=f"x{i}", ic=float(rng.normal(0, 0.03))))
    res = P.evaluate_run_p3("toy", 5.0, tmp_path / "led.jsonl", n_cands=10, n_var=20, B=100)
    assert (run / "phase3.json").exists() and res["portfolio"]["rolling_ols"]["by_cost"]["5.0"]["test"]["n_days"] > 100
    assert set(res["portfolio"]) == {"rolling_ols", "equal"} and res["N"]["ledger_trials_universe"] == 300
    assert abs(res["portfolio"]["equal"]["checks"]["max_gross_leverage"] - 1.0) < 1e-9 and res["portfolio"]["equal"]["checks"]["max_abs_net_exposure"] < 1e-9
    assert res["validity"]["cscv"]["n_splits"] == comb(16, 8) and res["validity"]["cpcv"]["n_paths"] == 9
    ok, n, msg = L.verify(); assert ok and any(e["kind"] == "candidate" for e in L.entries()) and any(e["kind"] == "p3_eval" for e in L.entries())
    assert L.count("trial") == 300                                                  # evaluation never adds trials
    (run / "pool.json").write_text(json.dumps(dict(members=[], size=0)))
    r0 = P.evaluate_run_p3("toy", 5.0, tmp_path / "led.jsonl", n_cands=10, n_var=20, B=100, out_name="p3b.json"); assert r0["portfolio"] is None
