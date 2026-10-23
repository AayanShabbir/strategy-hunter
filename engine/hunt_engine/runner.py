"""`hunt run`: pre-register (spec hash + N reserved under lock) -> load pre-vault data -> backtest every variant ->
gauntlet at the CURRENT ledger N -> results.json + report.md + ledger rows (atomic, locked)."""
import os, json, shutil, numpy as np, pandas as pd
from . import spec as specmod, ledger, data, gauntlet as G
from .backtest import run_variant, to_daily, bh_bar
from .util import paths, atomic_json, atomic_write, now_et, sha256_bytes
def _split(idx, is_frac): return idx[int(len(idx) * is_frac)]
def run(spec_path, allow_rerun=False, loader=None, n_random=None, quiet=False):
    s, raw = specmod.load(spec_path); h = sha256_bytes(raw)
    vs = specmod.variants(s); names = [v["name"] for v in vs]
    run_id = f"{now_et():%Y%m%d_%H%M%S}_{s['id']}"
    rd = os.path.join(paths()["runs"], run_id); os.makedirs(rd, exist_ok=True)
    shutil.copy(spec_path, os.path.join(rd, "spec.yaml"))
    rows, N_after = ledger.reserve(run_id, s["id"], h, names, allow_rerun)   # N reserved BEFORE any result
    atomic_json(os.path.join(rd, "prereg.json"), dict(run_id=run_id, spec_hash=h, rows=rows, N_after_reserve=N_after,
                written_before_any_results=True, ts=now_et().isoformat()))
    try:
        res = _evaluate(s, vs, rows, loader or data.load, n_random or int(s.get("n_random", 1000)))
    except Exception as e:
        atomic_json(os.path.join(rd, "results.json"), dict(run_id=run_id, error=repr(e), rows=rows))
        ledger.write_results(run_id, [], f"\n## Engine run {run_id}: CRASHED ({e!r}); rows stay counted in N.\n"); raise
    res.update(run_id=run_id, spec_id=s["id"], spec_hash=h)
    atomic_json(os.path.join(rd, "results.json"), res)
    md = _report(s, res); atomic_write(os.path.join(rd, "report.md"), md)
    out_rows = [dict(row=v["row"], variant=k, p=v["p_twin"], holm=v["holm"], passed=v["pass"]) for k, v in res["variants"].items()]
    ledger.write_results(run_id, out_rows, _ledger_block(s, res))
    if not quiet: print(f"{run_id}: {res['n_pass']}/{len(vs)} pass | N={res['N']} | PBO={res['PBO']} | {rd}/report.md")
    return res, rd
def _evaluate(s, vs, rows, loader, n_random):
    tf = s["timeframe"]; syms = sorted({x for b in s["universe"].values() for x in b})
    Dall = loader(syms, tf, allow_vault=False)
    cfg = s.get("split", {}); is_frac = cfg.get("is_frac", 0.7); k_wf = cfg.get("wf_folds", 2)
    fee_side = (s["costs"].get("fee_bps", 0) + s["costs"].get("slippage_bps", 5)) / 1e4
    min_trades = int(s.get("min_trades", 100)); out = {}; daily = {}; ann = G.ann_factor(syms, tf)
    for v in vs:
        D = {c: x[s["universe"][v["basket"]]] for c, x in Dall.items()}
        bt = run_variant(D, s, v); idx = bt["bar_ret"].index; cut = _split(idx, is_frac); oos = idx >= cut
        R = (D["open"].shift(-1) / D["open"] - 1)
        dr = to_daily(bt["bar_ret"], tf); dcut = to_daily(pd.Series(0.0, index=idx[oos]), tf).index[0]
        bh = to_daily(bh_bar(D), tf)
        Wo, Ro = bt["W"][oos], R[oos]
        dW = np.abs(np.diff(np.vstack([np.zeros((1, Wo.shape[1])), Wo.values]), axis=0))
        real = float(np.prod(1 + (Wo.values * np.nan_to_num(Ro.values) - fee_side * dW).mean(1)) - 1)
        p, rmed = G.random_twin(Wo, Ro, fee_side, real, n=n_random, seed=rows[v["name"]])
        o = dr[dr.index >= dcut]; folds = [o.iloc[ix] for ix in np.array_split(np.arange(len(o)), k_wf)]
        out[v["name"]] = dict(row=rows[v["name"]], IS=G.stats(dr[dr.index < dcut], ann), OOS=G.stats(o, ann), BH_OOS=G.stats(bh[bh.index >= dcut], ann), CPCV=G.cpcv(dr, ann=ann),
            trades=bt["trades"], time_in_mkt=round(bt["time_in_mkt"], 3), cost_stop=round(float(bt["cost_stop"]), 4),
            WF=[G.stats(f)["ret"] for f in folds], p_twin=round(p, 5), random_median_oos=rmed, real_twin_basis=round(real * 100, 2),
            SPA=round(G.spa_p(bh.reindex(o.index).fillna(0).values, o.values), 4))
        daily[v["name"]] = dr
    N = ledger.current_N()                                   # current ledger N, includes this run's reservation
    allp = ledger.all_pvalues(); allp.update({x["row"]: x["p_twin"] for x in out.values()})
    hadj = G.holm_adjusted(allp, [x["row"] for x in out.values()])
    M = pd.DataFrame(daily).dropna()
    pbo = G.pbo_cscv(M.values) if M.shape[1] >= 2 and len(M) >= 64 else 1.0
    oosM = M[M.index >= M.index[int(len(M) * is_frac)]]
    srv = max(float((oosM.mean() / oosM.std()).var()), 1e-8) if M.shape[1] > 1 else 1e-8
    npass = 0
    for k, x in out.items():
        x["holm"] = round(hadj[x["row"]], 5); x["DSR"] = round(G.dsr(oosM[k], srv, N), 4)
        x["pass"], x["checks"] = G.verdict(x, min_trades, pbo); npass += x["pass"]
        x["dd_improvement_vs_bh"] = round(x["OOS"]["maxdd"] - x["BH_OOS"]["maxdd"], 2)   # diagnostic (+ = shallower DD); not a gate
    return dict(variants=out, N=N, PBO=round(pbo, 3), n_pass=int(npass), min_trades=min_trades,
                window=dict(start=str(M.index[0].date()), end=str(M.index[-1].date()), oos_start=str(oosM.index[0].date())),
                ann_factor=ann, bar=G.BAR, ts=now_et().isoformat())
def _row(k, x):
    f = [c for c, ok in x["checks"].items() if not ok]
    return (f"| {x['row']} | {k} | {x['OOS']['ret']}/{x['OOS']['sharpe']}/{x['OOS']['maxdd']} | {x['BH_OOS']['ret']} | {x['trades']} | "
            f"{x['cost_stop']} | {x['p_twin']} ({x['random_median_oos']}) | {x['holm']} | {x['DSR']} | {x['SPA']} | {x['pass']} | {', '.join(f) or '-'} |")
HDR = "| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
def _report(s, r):
    w = r["window"]
    return (f"# {s['id']} — engine run {r['run_id']}\n\nHypothesis: {s['hypothesis']}\n\n**{r['n_pass']}/{len(r['variants'])} pass.** "
            f"Ledger N at evaluation: {r['N']}. PBO (CSCV) across family: {r['PBO']}. Window {w['start']}..{w['end']} (pre-vault), OOS from {w['oos_start']}.\n"
            f"Spec sha256 {r['spec_hash']}. Costs {s['costs']}. min_trades {r['min_trades']}.\n\n" + HDR +
            "\n".join(_row(k, x) for k, x in r["variants"].items()) + "\n\nBar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, "
            "ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.\n")
def _ledger_block(s, r):
    rows = [x["row"] for x in r["variants"].values()]
    return (f"\n## Engine run {r['run_id']} ({s['id']}): rows #{min(rows)}-{max(rows)}. {r['n_pass']}/{len(rows)} pass. PBO {r['PBO']}. Bar applied at N={r['N']}. "
            f"Report: engine/runs/{r['run_id']}/report.md\n\n" + HDR + "\n".join(_row(k, x) for k, x in r["variants"].items()) + f"\n\nN_cumulative: {ledger.current_N()}\n")
