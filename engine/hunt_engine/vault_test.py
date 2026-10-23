import os, json, numpy as np, pandas as pd, yaml
from . import data, vault, spec as specmod, gauntlet as G
from .backtest import run_variant, to_daily, bh_bar
from .util import paths
def vault_test(run_id, variant, loader=None, n_random=2000):
    rd = os.path.join(paths()["runs"], run_id); res = json.load(open(os.path.join(rd, "results.json")))
    v = res["variants"].get(variant)
    if v is None: raise SystemExit(f"no variant {variant!r} in {run_id}")
    if not v["pass"]: raise SystemExit("refused: only gauntlet survivors may open the vault")
    cand = f"{run_id}::{variant}"
    if vault.already_tested(cand): raise SystemExit(f"refused: vault already used for {cand} (one look only)")
    s = yaml.safe_load(open(os.path.join(rd, "spec.yaml"))); vd = next(x for x in specmod.variants(s) if x["name"] == variant)
    D = (loader or data.load)(s["universe"][vd["basket"]], s["timeframe"], allow_vault=True)  # full history for warm-up
    bt = run_variant(D, s, vd); cut = vault.vault_start_ts(s["timeframe"]); m = bt["bar_ret"].index >= cut
    dr = to_daily(bt["bar_ret"][m], s["timeframe"]); bh = to_daily(bh_bar(D)[m], s["timeframe"])
    fee = (s["costs"].get("fee_bps", 0) + s["costs"].get("slippage_bps", 5)) / 1e4
    R = (D["open"].shift(-1) / D["open"] - 1)[m]; W = bt["W"][m]
    dW = np.abs(np.diff(np.vstack([np.zeros((1, W.shape[1])), W.values]), axis=0))
    real = float(np.prod(1 + (W.values * np.nan_to_num(R.values) - fee * dW).mean(1)) - 1)
    p, rmed = G.random_twin(W, R, fee, real, n=n_random, seed=7)
    ann = G.ann_factor(s['universe'][vd['basket']]); out = dict(VAULT=G.stats(dr, ann), BH=G.stats(bh, ann), p_twin=p, random_median=rmed,
               window=f"{dr.index[0].date()}..{dr.index[-1].date()}" if len(dr) else "empty")
    out["pass"] = bool(out["VAULT"]["ret"] > 0 and out["VAULT"]["ret"] > out["BH"]["ret"] and p < 0.05)
    vault.record(cand, out); print(json.dumps(out, indent=1)); return out
