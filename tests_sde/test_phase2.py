"""Phase 2 tests: ledger, vectorized TsStd, GFlowNet policy (masks/TB/entropy), multi-faceted reward, pool, loader, e2e."""
import json, multiprocessing as mp, os, types
import numpy as np, pytest, torch
from src.audit.ledger import Ledger, GENESIS
from src.dsl.grammar import _ts_std, _ts_std_loop, evaluate, parse_expr, parse_ast, MAX_LEN
from src.gflownet.policy import (GFlowNetPolicy, ExprState, N_ACTIONS, TOKENS, SEP_ID, TOK_ID, FEAT_IDS, WIN_IDS, TOKENS as TK)
from src.rewards.multi_faceted import (Cells, FactorPool, MultiFacetedReward, weights, REWARD_FLOOR, IC_MIN, ICIR_MIN, CORR_MAX)
from src.data.loader import Panel, SPLITS, _read_bin, _panel_from_frames


# ------------------------------------------------------------------ synthetic panel
def toy_panel(D=500, N=80, seed=0, start="2010-01-04"):
    rng = np.random.default_rng(seed)
    dates = np.arange(np.datetime64(start), np.datetime64(start) + np.timedelta64(D * 2, "D"))
    dates = dates[np.is_busday(dates)][:D]
    ret = rng.normal(0, 0.02, (D, N))
    close = 50 * np.exp(np.cumsum(ret, 0))
    vol = np.exp(rng.normal(12, 1, (D, N)) + 0.5 * np.sin(np.arange(D))[:, None])
    data = {"$close": close, "$high": close * 1.01, "$low": close * 0.99, "$volume": vol}
    return Panel(dates, [f"S{i}" for i in range(N)], data, np.ones((D, N), bool), {"source": "toy"})


# ------------------------------------------------------------------ ledger
def test_ledger_chain_and_counts(tmp_path):
    L = Ledger(tmp_path / "l.jsonl")
    for i in range(5): L.append({"kind": "trial", "ast_hash": f"h{i % 3}", "ic": float("nan") if i == 0 else 0.1 * i})
    ok, n, msg = L.verify(); assert ok and n == 5 and msg == "ok"
    assert L.count() == 5 and L.distinct() == 3
    es = list(L.entries()); assert es[0]["prev"] == GENESIS and es[1]["prev"] == es[0]["hash"] and es[0]["ic"] is None


def test_ledger_append_only_never_shrinks(tmp_path):
    L = Ledger(tmp_path / "l.jsonl"); sizes = []
    for i in range(10): L.append({"kind": "trial", "ast_hash": str(i)}); sizes.append(os.path.getsize(L.path))
    assert sizes == sorted(sizes) and len(set(sizes)) == 10
    L2 = Ledger(L.path)                       # re-open continues the chain, does not truncate
    e = L2.append({"kind": "trial", "ast_hash": "x"}); assert e["n"] == 11 and L2.verify()[0]


def test_ledger_detects_tamper_delete_reorder(tmp_path):
    p = tmp_path / "l.jsonl"; L = Ledger(p)
    for i in range(6): L.append({"kind": "trial", "ast_hash": str(i), "ic": 0.01 * i})
    lines = p.read_text().splitlines()
    edited = lines.copy(); edited[2] = edited[2].replace('"ic":0.02', '"ic":0.9'); p.write_text("\n".join(edited) + "\n")
    assert not L.verify()[0]
    p.write_text("\n".join(lines[:2] + lines[3:]) + "\n"); assert not L.verify()[0]          # deleted entry
    p.write_text("\n".join(lines[:2] + [lines[3], lines[2]] + lines[4:]) + "\n"); assert not L.verify()[0]   # reordered
    p.write_text("\n".join(lines) + "\n"); assert L.verify()[0]                                # restored


def _worker(args):
    path, k = args
    L = Ledger(path)
    for i in range(25): L.append({"kind": "trial", "ast_hash": f"{k}-{i}"})


def test_ledger_concurrent_writers(tmp_path):
    p = tmp_path / "l.jsonl"; Ledger(p)
    with mp.get_context("fork").Pool(4) as pool: pool.map(_worker, [(p, k) for k in range(4)])
    L = Ledger(p); ok, n, msg = L.verify(); assert ok and n == 100 and L.distinct() == 100


# ------------------------------------------------------------------ TsStd
@pytest.mark.parametrize("w", [5, 10, 20, 60])
def test_tsstd_vectorized_matches_loop(w):
    rng = np.random.default_rng(1); x = rng.normal(size=(300, 7)) * 5 + 100
    x[50:60, 2] = np.nan; x[100:100 + w + 3, 4] = 7.0; x[200, 5] = np.inf
    a, b = _ts_std(x, w), _ts_std_loop(x, w)
    assert np.array_equal(np.isnan(a), np.isnan(b)); assert np.nanmax(np.abs(a - b)) < 1e-8
    assert np.isnan(a[:w - 1]).all() and np.all(a[100 + w - 1:100 + w + 3, 4] == 0)


def test_tsstd_causal_and_1d_and_short():
    x = np.random.default_rng(2).normal(size=(120, 3)); y = x.copy(); y[80:] += 10
    assert np.allclose(_ts_std(x, 20)[:80], _ts_std(y, 20)[:80], equal_nan=True)
    assert _ts_std(x[:, 0], 5).shape == (120,) and np.isnan(_ts_std(x[:3], 5)).all()


# ------------------------------------------------------------------ policy
def test_action_space_is_24_with_reserved_masked():
    assert N_ACTIONS == 24 and len(TOKENS) == 24 and sum(t.startswith("<reserved") for t in TOKENS) == 10
    p = GFlowNetPolicy(); assert p.head[-1].out_features == 24
    st = ExprState(); m = st.mask()
    assert not m[[i for i, t in enumerate(TOKENS) if t.startswith("<reserved")]].any() and not m[SEP_ID]


def test_mask_rules():
    st = ExprState(); m = st.mask()
    assert not m[FEAT_IDS].any()                                  # root can't be a bare feature
    st.step(TOK_ID["TsStd"]); m = st.mask(); assert m[FEAT_IDS].all() and not m[WIN_IDS].any()
    st.step(TOK_ID["$close"]); m = st.mask(); assert m[WIN_IDS].all() and m.sum() == 4      # window slot: windows only
    st.step(TOK_ID["20d"]); assert st.complete() and st.mask().sum() == 1 and st.mask()[SEP_ID]
    st.step(SEP_ID); assert st.done and st.mask().sum() == 0 and st.expr() == "TsStd($close, 20d)"


def test_random_valid_rollouts_always_parse_and_respect_maxlen():
    rng = np.random.default_rng(0); reached = 0
    for _ in range(600):
        st = ExprState(); bias = rng.random()
        while not st.done:
            m = st.mask().numpy().copy()
            ids = np.flatnonzero(m)
            w = np.where(np.isin(ids, [TOK_ID[t] for t in ("Add", "Sub", "Div", "TsStd")]), 1 + 8 * bias, 1.0)  # push toward deep trees
            st.step(int(rng.choice(ids, p=w / w.sum())))
            assert st.size + len(st.open) <= MAX_LEN
        n = parse_expr(st.expr()).size(); assert n <= MAX_LEN and n == st.size; reached += n == MAX_LEN
    assert reached > 0                                            # the cap is actually exercised


def test_sampled_graph_matches_parse_ast_typing():
    torch.manual_seed(0); p = GFlowNetPolicy()
    for _ in range(25):
        r = p.sample(); g = r["state"].graph(); h = parse_ast(r["expr"])
        assert sorted(g.node_type) == sorted(h.node_type) and len(g) == len(h)
        assert len(g.edges[1]) == len(h.edges[1]) and len(g.edges[0]) == len(h.edges[0])


def test_policy_uses_128d_rgcn_embedding_and_is_finite():
    p = GFlowNetPolicy(); st = ExprState(); st.step(TOK_ID["Add"])
    assert p.embed(ExprState()).shape == (128,) and p.embed(st).shape == (128,) and torch.isfinite(p.logits(st)).all()


def test_tb_loss_zero_at_balance_and_gradients_reach_everything():
    p = GFlowNetPolicy(seed=1); torch.manual_seed(1)
    r = p.sample(); lr = (p.log_z[0] + r["sum_logp"]).detach()
    fin, tb, ent = p.tb_loss(r["sum_logp"], lr, r["sum_entropy"], beta=0.0)
    assert tb.item() < 1e-10 and abs(fin.item()) < 1e-10
    _, tb2, _ = p.tb_loss(r["sum_logp"], lr - 2.0, r["sum_entropy"]); assert abs(tb2.item() - 4.0) < 1e-4
    r = p.sample(); loss = p.tb_loss(r["sum_logp"], torch.tensor(-1.0), r["sum_entropy"])[0]; loss.backward()
    assert p.log_z.grad is not None and p.head[0].weight.grad.abs().sum() > 0
    assert any(q.grad is not None and q.grad.abs().sum() > 0 for q in p.encoder.parameters())   # TB trains the RGCN too


def test_entropy_term_sign_and_value():
    p = GFlowNetPolicy(); st = ExprState(); m = st.mask(); pr = torch.softmax(p.logits(st).masked_fill(~m, -1e30), -1)
    h = -(pr[m] * pr[m].log()).sum(); r = p.sample()
    assert r["sum_entropy"].item() >= 0 and h.item() <= np.log(m.sum().item()) + 1e-6
    _, _, l_ent = p.tb_loss(r["sum_logp"], torch.tensor(0.0), r["sum_entropy"]); assert l_ent.item() == pytest.approx(-r["sum_entropy"].item())


def test_tb_training_shifts_mass_toward_high_reward():
    """Toy reward: 20 if the formula uses $volume else 1. TB training must raise P(volume formulas)."""
    torch.manual_seed(0); p = GFlowNetPolicy(seed=0)
    opt = torch.optim.Adam([{"params": [q for n, q in p.named_parameters() if n != "log_z"], "lr": 3e-3}, {"params": [p.log_z], "lr": 0.1}])
    frac = lambda: np.mean(["$volume" in p.sample()["expr"] for _ in range(150)])
    before = frac(); batch = []
    for i in range(700):
        r = p.sample(); R = 20.0 if "$volume" in r["expr"] else 1.0
        batch.append(p.tb_loss(r["sum_logp"], torch.log(torch.tensor(R)), r["sum_entropy"])[0])
        if len(batch) == 8: l = torch.stack(batch).mean(); opt.zero_grad(); l.backward(); opt.step(); batch = []
    assert frac() > before + 0.1


# ------------------------------------------------------------------ cells / reward / pool
@pytest.fixture(scope="module")
def world():
    P = toy_panel(); s, e = "2010-06-01", "2011-12-31"
    c = Cells(P, s, e); c.set_label(P.label(e)); return P, c


def test_label_is_purged_at_split_end(world):
    P, c = world; e = np.datetime64("2011-12-31")
    y = P.label("2011-12-31"); last = np.searchsorted(P.dates, e, "right") - 1
    assert np.isnan(y[last - 19:]).all() and np.isfinite(y[last - 20]).all()
    assert np.allclose(y[10], P.data["$close"][30] / P.data["$close"][10] - 1)


def test_ic_matches_bruteforce_pearson(world):
    P, c = world; rw = MultiFacetedReward(P, c, FactorPool(c))
    expr = "Div($close, TsStd($close, 20d))"; z = rw.signal(expr); ic, icir, n = c.ic_stats(z)
    f = evaluate(parse_expr(expr), P.data); y = P.label("2011-12-31"); a, b = P.idx("2010-06-01", "2011-12-31"); v = []
    for d in range(a, b):
        ok = np.isfinite(f[d]) & np.isfinite(y[d])
        if ok.sum() >= 30: v.append(np.corrcoef(f[d][ok], y[d][ok])[0, 1])
    assert ic == pytest.approx(np.mean(v)) and icir == pytest.approx(np.mean(v) / np.std(v, ddof=1)) and n == len(v)


def test_planted_signal_gets_high_ic_and_junk_does_not():
    P = toy_panel(D=700, N=120, seed=3); s, e = "2010-03-01", "2012-06-30"
    c = Cells(P, s, e)
    cl = P.data["$close"]; y_plant = np.full_like(cl, np.nan); y_plant[:-5] = np.log(P.data["$volume"][:-5]) * 0.01 + np.random.default_rng(0).normal(0, 0.01, cl[:-5].shape)
    c.y = c.take(y_plant); rw = MultiFacetedReward(P, c, FactorPool(c))
    assert rw.signal("Log($volume)") is not None
    ic_good, _, _ = c.ic_stats(rw.signal("Log($volume)")); ic_junk, _, _ = c.ic_stats(rw.signal("Div($high, $low)"))
    assert ic_good > 0.3 and abs(ic_junk) < 0.05


def test_signal_is_causal_through_reward_pipeline():
    P = toy_panel(seed=4); Q = toy_panel(seed=4)
    Q.data["$close"][300:] *= 3; Q.data["$volume"][300:] *= 5
    for k in ("$high", "$low"): Q.data[k][300:] *= 3
    s, e = "2010-06-01", "2011-12-31"; c = Cells(P, s, e); c.set_label(P.label(e))
    f1 = evaluate(parse_expr("Sub(TsStd(Log($close), 10d), Div($high, $volume))"), P.data)
    f2 = evaluate(parse_expr("Sub(TsStd(Log($close), 10d), Div($high, $volume))"), Q.data)
    assert np.allclose(f1[:300], f2[:300], equal_nan=True)


def test_weights_schedule():
    assert weights(0, 100) == (1.0, 0.3) and weights(50, 100) == pytest.approx((0.5, 0.15)) and weights(100, 100) == (0.0, 0.0) and weights(150, 100) == (0.0, 0.0)


def test_degenerate_formula_gets_floor_reward(world):
    P, c = world; rw = MultiFacetedReward(P, c, FactorPool(c), encoder=None)
    emb = np.zeros(128)
    r = rw("Sub($close, $close)", 1, 100, emb)          # constant zero -> no cross-sectional variation
    assert r["degenerate"] and r["reward"] == REWARD_FLOOR


def _add(pool, rw, expr, emb=None):
    z = rw.signal(expr); ic, icir, _ = pool.cells.ic_stats(z); g = parse_ast(expr)
    return pool.try_add(g.canonical, g.hash, emb if emb is not None else np.random.default_rng(len(pool.members)).normal(size=128), z, ic, icir), z


def test_pool_thresholds_correlation_duplicates_capacity_and_invariant():
    P = toy_panel(D=800, N=150, seed=5); s, e = "2010-03-01", "2012-12-31"; c = Cells(P, s, e)
    rng = np.random.default_rng(1)
    # label built from two independent planted drivers so that pool-worthy factors exist
    lv = np.log(P.data["$volume"]); lh = _ts_std(np.log(P.data["$high"]), 20)
    y = np.full_like(lv, np.nan)
    y[:-5] = 0.02 * lv[:-5] + 0.05 * np.nan_to_num(lh[:-5]) / (np.nanstd(lh) + 1e-9) + rng.normal(0, 0.05, lv[:-5].shape)
    c.y = c.take(y); rw = MultiFacetedReward(P, c, FactorPool(c, capacity=3))
    pool = rw.pool
    st, _ = _add(pool, rw, "Div($high, $low)"); assert st == "rejected_threshold" and len(pool) == 0
    st, z1 = _add(pool, rw, "Log($volume)"); assert st == "added"
    assert _add(pool, rw, "Log($volume)")[0] == "duplicate"
    st, _ = _add(pool, rw, "Log(Add($volume, $volume))"); assert st == "rejected_corr"            # ~identical behaviour to member 1
    assert pool.novelty(z1) == pytest.approx(0.0, abs=1e-6)                                         # same factor -> zero novelty
    assert pool.corr_with(rw.signal("Add(Log($volume), Log($volume))")).max() > CORR_MAX
    st, _ = _add(pool, rw, "TsStd(Log($high), 20d)"); assert st in ("added", "rejected_threshold", "rejected_corr")
    assert pool.max_pairwise_corr() <= CORR_MAX + 1e-9 and len(pool) <= 3


def test_pool_capacity_replaces_weakest_only_with_stronger():
    P = toy_panel(D=400, N=60, seed=6); c = Cells(P, "2010-03-01", "2011-06-30"); c.set_label(P.label("2011-06-30"))
    pool = FactorPool(c, capacity=2, ic_min=0.0, icir_min=0.0, corr_max=0.99)
    rng = np.random.default_rng(0); N = len(c.flat)
    def mk(ic): return dict(expr=f"e{ic}", ast_hash=f"h{ic}", emb=rng.normal(size=128), z=rng.normal(size=N), ic=ic, icir=1.0)
    for ic in (0.05, 0.04): assert pool.try_add(**mk(ic)) == "added"
    assert pool.try_add(**mk(0.03)) == "rejected_full"
    assert pool.try_add(**mk(0.06)) == "replaced" and sorted(m.ic for m in pool.members) == [0.05, 0.06]


def test_sa_reward_range_and_behaviour_alignment():
    P = toy_panel(D=400, N=60, seed=7); c = Cells(P, "2010-03-01", "2011-06-30"); c.set_label(P.label("2011-06-30"))
    pool = FactorPool(c, ic_min=0.0, icir_min=0.0, corr_max=0.99); rw = MultiFacetedReward(P, c, pool)
    assert pool.sa(np.zeros(128), rw.signal("Log($volume)")) == 0.0 and pool.novelty(rw.signal("Log($volume)")) == 1.0   # empty pool
    emb = np.random.default_rng(0).normal(size=128); _add(pool, rw, "Log($volume)", emb)
    same = pool.sa(emb, rw.signal("Log($volume)")); other = pool.sa(emb, rw.signal("Div($high, $close)"))
    assert same == pytest.approx(1.0, abs=1e-6) and 0 < other < same <= 1.0


def test_reward_combines_components(world):
    P, c = world; pool = FactorPool(c, ic_min=0.0, icir_min=0.0, corr_max=0.99); rw = MultiFacetedReward(P, c, pool)
    emb = np.random.default_rng(0).normal(size=128); _add(pool, rw, "Log($volume)", emb)
    r = rw("Div($high, $close)", 100, 1000, emb + 0.1)
    assert r["reward"] == pytest.approx(r["r_ic"] + r["lam"] * r["r_sa"] + r["eta"] * r["r_nov"]) and r["lam"] == pytest.approx(0.9) and r["eta"] == pytest.approx(0.27)


# ------------------------------------------------------------------ loader
def test_split_constants_match_blueprint():
    for u in ("csi300", "csi500", "csi1000"):
        assert SPLITS[u] == {"train": ("2010-01-01", "2020-12-31"), "val": ("2021-01-01", "2021-12-31"), "test": ("2022-01-01", "2024-12-31")}
    assert SPLITS["sp500"] == {"train": ("2010-01-01", "2016-12-31"), "val": ("2017-01-01", "2017-12-31"), "test": ("2018-01-01", "2020-12-31")}


def test_read_qlib_bin_format(tmp_path):
    a = np.array([3.0, 1.5, 2.5, 3.5], dtype="<f4"); a.tofile(tmp_path / "close.day.bin")
    out = _read_bin(tmp_path / "close.day.bin", 8); assert np.isnan(out[:3]).all() and list(out[3:6]) == [1.5, 2.5, 3.5] and np.isnan(out[6:]).all()


def test_qlib_point_in_time_membership(tmp_path, monkeypatch):
    import src.data.loader as L
    root = tmp_path / "q"; (root / "calendars").mkdir(parents=True); (root / "instruments").mkdir()
    cal = [str(d) for d in np.arange(np.datetime64("2010-01-04"), np.datetime64("2010-02-01")) if np.is_busday(d)]
    (root / "calendars" / "day.txt").write_text("\n".join(cal))
    (root / "instruments" / "csi300.txt").write_text(f"SH600001\t{cal[0]}\t{cal[9]}\nSH600002\t{cal[5]}\t{cal[-1]}\n")
    for t in ("sh600001", "sh600002"):
        d = root / "features" / t; d.mkdir(parents=True)
        for f, v in dict(close=10.0, high=11.0, low=9.0, volume=1000.0).items():
            np.concatenate([[0.0], np.full(len(cal), v)]).astype("<f4").tofile(d / f"{f}.day.bin")
    monkeypatch.setattr(L, "QLIB_DIR", root)
    P = L.load_qlib("csi300", start="2010-01-01", end="2010-01-31")
    assert P.assets == ["SH600001", "SH600002"] and P.member[0].tolist() == [True, False] and P.member[7].tolist() == [True, True] and P.member[12].tolist() == [False, True]


def test_panel_from_frames_and_cache_free(tmp_path):
    import pandas as pd
    idx = pd.bdate_range("2010-01-04", periods=10)
    fr = {t: pd.DataFrame({"Close": np.arange(10.0) + i, "High": 1.0, "Low": 1.0, "Volume": 5.0}, index=idx) for i, t in enumerate(["AAA", "BBB"])}
    P = _panel_from_frames(fr, {"close": "Close", "high": "High", "low": "Low", "volume": "Volume"}, {"survivorship": "BIASED"})
    assert P.data["$close"].shape == (10, 2) and P.member.all() and P.meta["survivorship"] == "BIASED"


def test_data_cache_is_gitignored():
    ig = open(os.path.join(os.path.dirname(__file__), "..", ".gitignore")).read()
    assert "data/" in ig.split() and "*.parquet" in ig and "*.pt" in ig


# ------------------------------------------------------------------ end-to-end (synthetic panel)
def test_training_loop_end_to_end_counts_every_trial(tmp_path, monkeypatch):
    import src.train.train_gfn as T
    P = toy_panel(D=450, N=70, seed=9, start="2010-01-04")
    monkeypatch.setitem(SPLITS, "toy", {"train": ("2010-03-01", "2011-06-30")})
    monkeypatch.setattr(T, "load_panel", lambda u, upto="train": P); monkeypatch.setattr(T, "ROOT", tmp_path)
    args = types.SimpleNamespace(universe="toy", episodes=48, seed=0, run_id="t", lr=1e-4, lr_logz=0.1, entropy=0.01, update_every=16,
                                 log_every=24, ckpt_every=48, ledger=str(tmp_path / "led.jsonl"))
    out = T.run(args); L = Ledger(args.ledger)
    ok, n, _ = L.verify(); trials = [e for e in L.entries() if e["kind"] == "trial"]
    assert ok and len(trials) == 48 and L.count() == 48 and n == 49                 # every episode is one trial; +1 run_end
    assert all(e["split"] == "train" and e["ast_hash"] and 1 <= e["n_nodes"] <= MAX_LEN for e in trials)
    pj = json.loads((out / "pool.json").read_text()); assert pj["max_pairwise_corr"] <= CORR_MAX + 1e-9
    assert (out / "policy.pt").exists() and (out / "curve.csv").exists()
