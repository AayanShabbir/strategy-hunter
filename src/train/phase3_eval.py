"""SDE Phase 3: portfolio + validity evaluation of one finished run.

    .venv17/bin/python -m src.train.phase3_eval --run-id csi300_s0_20261023 [--cost-bps 5]

Writes runs_sde/<run_id>/phase3.json and appends a `p3_eval` entry (plus the Promote `candidate`/`escore` rows) to the ledger.
Selection never uses the test split: pool members/signs come from the Phase 2 run (TRAIN IC); the combination is walk-forward;
CSCV/PBO and CPCV use train+val only; the DSR/SPA/e-process reads of the test split are pure reporting.
"""
from __future__ import annotations
import argparse, json, time, warnings
from math import comb
from pathlib import Path
import numpy as np
warnings.filterwarnings("ignore")
from src.audit.ledger import Ledger, DEFAULT_PATH
from src.data.loader import load_panel, SPLITS
from src.portfolio.long_short import (zscore_rows, leverage_normalized_weights, tradable_mask, backtest, metrics, sharpe_daily)
from src.portfolio.combine import (member_signals, label_matrix, combine_equal, combine_rolling_ols, factor_matrix, DEFAULTS, HORIZON)
from src.validation.dsr import deflated_sharpe
from src.validation.cscv import cscv_pbo
from src.validation.cpcv import cpcv_splits, cpcv_paths, n_paths
from src.validation.spa import spa_test
from src.validation import eprocess as ep

ROOT = Path(__file__).resolve().parents[2]
COSTS = (0.0, 5.0, 10.0, 20.0)
TARGETS = dict(sharpe=5.5, annual_return=0.18, pbo=0.10, dsr=0.95, spa_p=0.05)   # blueprint targets we have (see docs/sde_phase3.md)
PROGRAM = "sde-promote-v1"; LIB_SLOTS = 8; ALPHA = 0.05


def split_slices(panel, uni):
    out = {}
    for name, (s, e) in SPLITS[uni].items():
        a, b = panel.idx(s, e); out[name] = (a, b)
    return out


def trial_returns(panel, trad, expr, sign, cost_bps):
    sig = sign * zscore_rows(factor_matrix(panel, expr), trad)
    bt = backtest(leverage_normalized_weights(sig), panel.data["$close"], cost_bps)
    return bt["net"]


def ledger_trials(ledger, uni):
    seen, out, n_total, n_uni = set(), [], 0, 0
    for e in ledger.entries():
        if e.get("kind") != "trial": continue
        n_total += 1
        if e.get("universe") != uni: continue
        n_uni += 1
        if e.get("ast_hash") in seen or e.get("ic") is None: continue
        seen.add(e["ast_hash"]); out.append((e["ast"], float(e["ic"]), e["ast_hash"]))
    return out, n_total, n_uni


def split_metrics(bt_net, bt_to, slices, active_start):
    res = {}
    for name, (a, b) in slices.items():
        a2 = max(a, active_start); b2 = min(b, len(bt_net))
        res[name] = metrics(bt_net[a2:b2], bt_to[a2:b2]); res[name]["first_day_index"] = int(a2)
    return res


def run_cpcv(Z, Y, close, trad, a0, a1, cost_bps, n_groups=10, k=2, purge=HORIZON, embargo=5):
    """Static pooled-OLS combination re-fit per CPCV split on purged/embargoed train rows; OOS path Sharpe distribution."""
    K = Z.shape[0]; T = a1 - a0
    splits = cpcv_splits(T, n_groups, k, purge, embargo)
    for s in splits: s["train"][T - HORIZON:] = False                          # labels reaching past val end
    rets = []; Zs = np.nan_to_num(Z[:, a0:a1].astype(np.float64)); Ys = Y[a0:a1]
    for s in splits:
        tr = s["train"]; X = Zs[:, tr]; y = Ys[tr]; ok = np.isfinite(y)
        X = X[:, ok]; y = y[ok]; beta = np.linalg.solve(X @ X.T + 1e-6 * X.shape[1] * np.eye(K), X @ y)
        sig = np.einsum("k,kda->da", beta, Zs); sig[~np.isfinite(Z[:, a0:a1]).any(0)] = np.nan
        bt = backtest(leverage_normalized_weights(sig), close[a0:a1], cost_bps)
        rets.append(bt["net"])                                                  # length T-1
    paths = cpcv_paths(splits, n_groups); gb = np.linspace(0, T, n_groups + 1).astype(int); L = T - 1; out = []
    for p in paths:
        r = np.concatenate([rets[si][gb[g]:min(gb[g + 1], L)] for g, si in p]); out.append(r)
    sr = np.array([np.sqrt(252) * r.mean() / r.std(ddof=1) for r in out])
    return dict(n_splits=len(splits), n_paths=len(out), expected_paths=n_paths(n_groups, k), path_sharpe=[float(x) for x in sr],
                mean_sharpe=float(sr.mean()), median_sharpe=float(np.median(sr)), min_sharpe=float(sr.min()), frac_paths_positive=float(np.mean(sr > 0)),
                purge=purge, embargo=embargo, n_groups=n_groups, k=k)


def evaluate_run_p3(run_id, cost_bps=5.0, ledger_path=DEFAULT_PATH, n_cands=100, n_var=200, write_ledger=True, seed=0, B=1000, out_name="phase3.json"):
    t0 = time.time(); out = ROOT / "runs_sde" / run_id
    cfg = json.loads((out / "config.json").read_text()); pool = json.loads((out / "pool.json").read_text())
    uni = cfg["universe"]; members = pool["members"]; ledger = Ledger(ledger_path)
    panel = load_panel(uni, upto="test"); close = panel.data["$close"]; trad = tradable_mask(panel)
    sl = split_slices(panel, uni); a_tr = sl["train"][0]; v0, v1 = sl["val"]; t_a, t_b = sl["test"]
    D = close.shape[0]; res = dict(run_id=run_id, universe=uni, cost_bps=cost_bps, pool_size=len(members), data_meta=panel.meta,
                                   splits={k: [str(panel.dates[a]), str(panel.dates[min(b, D) - 1])] for k, (a, b) in sl.items()},
                                   combiner_params=DEFAULTS, targets=TARGETS, n_assets=len(panel.assets))
    trials, n_total, n_uni = ledger_trials(ledger, uni)
    res["N"] = dict(ledger_trials_total=n_total, ledger_trials_universe=n_uni, distinct_universe=len(trials))
    # ---- trial-Sharpe variance (for DSR) and candidate family (CSCV / SPA): ledger formulas, sign from TRAIN IC
    rng = np.random.default_rng(seed)
    pick = rng.choice(len(trials), size=min(n_var, len(trials)), replace=False) if trials else []
    srs = []
    for i in pick:
        ex, ic, _ = trials[i]
        try:
            net = trial_returns(panel, trad, ex, np.sign(ic) or 1.0, cost_bps); srs.append(sharpe_daily(net[a_tr:v0]))
        except Exception: pass
    srs = np.array([s for s in srs if np.isfinite(s)]); var_sr = float(srs.var(ddof=1)) if len(srs) > 2 else float("nan")
    res["trial_sharpe_sample"] = dict(n=int(len(srs)), var_daily_sr=var_sr, mean_annual_sr=float(srs.mean() * np.sqrt(252)) if len(srs) else None)
    order = sorted(range(len(trials)), key=lambda i: -abs(trials[i][1]))
    want = {m["ast_hash"] for m in members}; chosen = order[:n_cands] + [i for i in order[n_cands:] if trials[i][2] in want]
    cand = []; 
    for i in chosen:
        ex, ic, h = trials[i]
        try: cand.append(trial_returns(panel, trad, ex, np.sign(ic) or 1.0, cost_bps))
        except Exception: pass
    C = np.stack(cand, 1) if cand else np.zeros((D - 1, 0))
    res["family"] = dict(size=int(C.shape[1]), selection="top-%d distinct ledger formulas of this universe by |train IC| (+ pool members)" % n_cands)
    # ---- portfolio: pool combination
    port = {}
    if members:
        Z = member_signals(panel, members, trad); Y = label_matrix(close, trad)
        sigs = {"rolling_ols": None, "equal": combine_equal(Z)}
        sigs["rolling_ols"], info = combine_rolling_ols(Z, Y, first_day=a_tr, return_info=True, **DEFAULTS)
        act = {"rolling_ols": a_tr + DEFAULTS["lookback"] + HORIZON, "equal": a_tr}
        for name, sig in sigs.items():
            W = leverage_normalized_weights(sig); port[name] = dict(by_cost={})
            for c in COSTS:
                bt = backtest(W, close, c); port[name]["by_cost"][str(c)] = split_metrics(bt["net"], bt["turnover"], sl, act[name])
                if c == cost_bps: port[name]["bt"] = bt
            lev = port[name]["bt"]["gross_leverage"]; net = port[name]["bt"]["net_exposure"]
            act_days = lev > 0
            port[name]["checks"] = dict(max_gross_leverage=float(lev.max()), min_gross_leverage_when_active=float(lev[act_days].min()) if act_days.any() else 0.0,
                                        max_abs_net_exposure=float(np.abs(net).max()), active_days=int(act_days.sum()))
        res["combiner_info"] = dict(n_refresh=len(info["refresh_idx"]), mean_members_kept=float(np.mean(info["n_kept"])) if info["n_kept"] else 0.0,
                                    frac_refresh_flat=float(np.mean(np.array(info["n_kept"]) == 0)) if info["n_kept"] else None)
        res["portfolio"] = {n: dict(by_cost=p["by_cost"], checks=p["checks"]) for n, p in port.items()}
    else:
        res["portfolio"] = None; res["note"] = "pool is empty: no portfolio to build"
    # ---- validity
    val = {}
    val["cscv"] = cscv_pbo(C[a_tr:v1], 16) if C.shape[1] >= 2 else dict(pbo=float("nan"), reason="family < 2")
    val["spa_test_family"] = spa_test(C[t_a:t_b], B=B, seed=seed) if C.shape[1] >= 1 else dict(p_consistent=float("nan"))
    if members:
        prim = port["rolling_ols"]["bt"]; pa = act["rolling_ols"]
        val["dsr"] = {}
        for name in port:
            bt = port[name]["bt"]; a0 = act[name]
            R_tr = bt["net"][max(a_tr, a0):v0]; R_te = bt["net"][t_a:min(t_b, len(bt["net"]))]
            val["dsr"][name] = dict(
                train_N_ledger_total=deflated_sharpe(R_tr, n_total, var_sr), test_N_ledger_total=deflated_sharpe(R_te, n_total, var_sr),
                train_N_ledger_universe=deflated_sharpe(R_tr, n_uni, var_sr), test_N_ledger_universe=deflated_sharpe(R_te, n_uni, var_sr),
                test_N_1=deflated_sharpe(R_te, 1, var_sr))
        val["cpcv"] = run_cpcv(Z, Y, close, trad, a_tr, v1, cost_bps)
        val["spa_pool_members_test"] = spa_test(np.stack([trial_returns(panel, trad, m["expr"], m["sign"], cost_bps)[t_a:t_b] for m in members], 1), B=B, seed=seed)
        val["spa_combined_test"] = spa_test(prim["net"][t_a:t_b, None], B=B, seed=seed)
        # Ville e-process on the ledger: candidate = rolling-OLS combined portfolio, birth = last val day, scores = test days only
        scale = ep.predictable_scale(prim["net"][max(a_tr, pa):v1]); mass = 1.0 / LIB_SLOTS
        birth = str(panel.dates[v1 - 1]); dver = f"{uni}:{panel.meta.get('source', '')}:{panel.dates[0]}..{panel.dates[-1]}"
        package = dict(run_id=run_id, universe=uni, members=[(m["ast_hash"], m["sign"]) for m in members], combiner="rolling_ols", params=DEFAULTS,
                       weights="leverage_normalized_long_short", cost_bps=cost_bps, scale=scale)
        dates_t = [str(d) for d in panel.dates[t_a + 1:min(t_b, len(prim["net"])) + 1]]   # return set at close t is realised on t+1
        net_t = prim["net"][t_a:min(t_b, len(prim["net"]))]; cost_t = cost_bps * 1e-4 * prim["turnover"][t_a:min(t_b, len(prim["net"]))]
        if write_ledger:
            cand_row = ep.register_candidate(ledger, PROGRAM, package, parent=None, birth=birth, mass=mass, scale=scale, alpha=ALPHA, data_version=dver)
            fp = cand_row["fingerprint"]
        else: fp = ep.candidate_fingerprint(package)
        val["eprocess"] = ep.score_candidate(ledger, PROGRAM, fp, dates_t, net_t, cost_t, scale, mass, ALPHA, dver, write_rows=write_ledger)
        val["eprocess"].update(fingerprint=fp, birth=birth, library_slots=LIB_SLOTS)
    res["validity"] = val
    # ---- targets
    tg = {}
    if members:
        te = res["portfolio"]["rolling_ols"]["by_cost"][str(cost_bps)]["test"]
        tg = dict(sharpe=dict(value=te["sharpe"], target=">= 5.5", met=bool(te["sharpe"] >= 5.5)),
                  annual_return=dict(value=te["annual_return"], target=">= 18%", met=bool(te["annual_return"] >= 0.18)))
        d = val["dsr"]["rolling_ols"]["test_N_ledger_total"]["dsr"]
        tg["dsr_test_N_total"] = dict(value=d, target="> 0.95 (convention)", met=bool(d > 0.95))
        tg["spa_p_combined_test"] = dict(value=val["spa_combined_test"]["p_consistent"], target="< 0.05", met=bool(val["spa_combined_test"]["p_consistent"] < 0.05))
        tg["eprocess"] = dict(value=val["eprocess"]["max_evidence"], target=">= %.0f" % val["eprocess"]["boundary"], met=bool(val["eprocess"]["promoted"]))
        tg["cpcv_mean_path_sharpe"] = dict(value=val["cpcv"]["mean_sharpe"], target="reported (no numeric target)", met=None)
    p = val["cscv"].get("pbo"); tg["pbo"] = dict(value=p, target="<= 10%", met=bool(p <= 0.10) if p == p else None)
    res["targets_check"] = tg; res["elapsed_s"] = round(time.time() - t0, 1)
    (out / out_name).write_text(json.dumps(res, indent=1, default=str))
    if write_ledger:
        ledger.append(dict(kind="p3_eval", run_id=run_id, universe=uni, cost_bps=cost_bps, N_total=n_total, N_universe=n_uni, pool_size=len(members),
                           targets_check=tg, pbo=p))
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--run-id", required=True); ap.add_argument("--cost-bps", type=float, default=5.0)
    ap.add_argument("--ledger", default=str(DEFAULT_PATH)); ap.add_argument("--n-cands", type=int, default=100)
    a = ap.parse_args(); r = evaluate_run_p3(a.run_id, a.cost_bps, a.ledger, a.n_cands)
    print(json.dumps(r["targets_check"], indent=1, default=str)); print("elapsed", r["elapsed_s"])
