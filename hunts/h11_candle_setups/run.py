import sys, json, numpy as np, pandas as pd
from scipy import stats
sys.path.insert(0, "/workspace/trading-desk"); import candle_setups as CS, desk_common as dc
from statsmodels.stats.multitest import multipletests
COST = 5e-4; START, END = "2024-10-14", "2026-10-15"
A = pd.read_pickle("/workspace/trading-desk/validation/data/ALL_15m.pkl")
A = A[(A.index.get_level_values(1) >= START) & (A.index.get_level_values(1) < END)]
syms = [s for s in A.index.get_level_values(0).unique() if not dc.symbol_block(s) and s not in ("BITO", "IBIT")]
trades = []
for s in syms:
    g = A.xs(s, level=0).sort_index(); t = g.index.tz_convert("America/New_York")
    g = g[(t.time >= pd.Timestamp("09:30").time()) & (t.time < pd.Timestamp("16:00").time()) & (g["volume"] > 0)]
    for tf, bm in (("15m", 15), ("1h", 60)):
        if tf == "1h":
            x = g.copy(); x.index = x.index.tz_convert("America/New_York")
            x = x.resample("60min", offset="30min").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
            x.index = x.index.tz_convert("UTC")
        else: x = g
        if len(x) < 100: continue
        d = CS.features(x); S = CS.signals(d, bm)
        O, H, L, C, AT, DAY = (d[k].values for k in ("open", "high", "low", "close", "atr", "day"))
        n = len(d)
        for setup in CS.SETUPS:
            sh = setup.startswith("S_")
            for i in np.flatnonzero(S[setup].values):
                j = i + 1
                if j >= n or DAY[j] != DAY[i]: continue
                e = O[j]; risk = CS.ATR_MULT * AT[i]; stp = e + risk if sh else e - risk; tg = e - 2 * risk if sh else e + 2 * risk
                k = j; ex = None
                while k < n and DAY[k] == DAY[i]:
                    if sh:
                        if H[k] >= stp: ex = stp; break
                        if L[k] <= tg: ex = tg; break
                    else:
                        if L[k] <= stp: ex = stp; break
                        if H[k] >= tg: ex = tg; break
                    k += 1
                if ex is None: k -= 1; ex = C[k]
                r = ((e - ex) / e if sh else (ex - e) / e) - 2 * COST
                trades.append({"sym": s, "tf": tf, "setup": setup, "t_in": d.index[j], "t_out": d.index[k], "day": DAY[i], "ret": r, "R": r * e / risk})
T = pd.DataFrame(trades).sort_values("t_in")
rows = []
for (tf, st), g in T.groupby(["tf", "setup"]):
    tt = stats.ttest_1samp(g["ret"], 0, alternative="greater")
    rows.append({"test": f"{tf}:{st}", "trades": len(g), "win%": round((g.ret > 0).mean() * 100, 1), "avg_bps": round(g.ret.mean() * 1e4, 2),
                 "avg_R": round(g.R.mean(), 3), "p": float(tt.pvalue)})
R = pd.DataFrame(rows)
p_all = np.concatenate([R.p.values, np.ones(298)]); R["holm_p"] = multipletests(p_all, method="holm")[1][:len(R)].round(4)
# portfolio: 10% per trade, max 5 concurrent
open_, take = [], []
for r in T.itertuples():
    open_ = [x for x in open_ if x > r.t_in]
    if len(open_) < 5: open_.append(r.t_out); take.append(r)
P = pd.DataFrame(take); daily = P.groupby("day")["ret"].sum() * 0.10
spy = A.xs("SPY", level=0)["close"]; spy.index = spy.index.tz_convert("America/New_York"); sd = spy.groupby(spy.index.date).last().pct_change().dropna()
idx = sd.index; port = daily.reindex(idx).fillna(0.0)
def st(x):
    eq = (1 + x).cumprod(); yrs = len(x) / 252
    return {"total_%": round((eq.iloc[-1] - 1) * 100, 2), "cagr_%": round((eq.iloc[-1] ** (1 / yrs) - 1) * 100, 2),
            "sharpe": round(x.mean() / x.std() * np.sqrt(252), 2) if x.std() > 0 else 0, "maxdd_%": round((eq / eq.cummax() - 1).min() * 100, 2)}
out = {"universe": len(syms), "period": [START, END], "all_signals_trades": len(T), "portfolio_trades": len(P),
       "portfolio_trades_per_day": round(len(P) / len(idx), 2), "portfolio": st(port), "SPY": st(sd), "SPY70_cash30": st(sd * 0.7),
       "portfolio_win%": round((P.ret > 0).mean() * 100, 1), "portfolio_avg_bps": round(P.ret.mean() * 1e4, 2),
       "long_only_avg_bps": round(T[T.setup.str.startswith("L_")].ret.mean() * 1e4, 2), "short_only_avg_bps": round(T[T.setup.str.startswith("S_")].ret.mean() * 1e4, 2),
       "gross_avg_bps_before_costs": round((T.ret.mean() + 2 * COST) * 1e4, 2), "tests": R.to_dict("records")}
out["pass"] = bool(out["portfolio"]["sharpe"] > out["SPY"]["sharpe"] and out["portfolio"]["total_%"] > 0 and (R.holm_p < 0.05).any())
json.dump(out, open("results.json", "w"), indent=1, default=str); T.to_parquet("trades.parquet")
print(json.dumps({k: v for k, v in out.items() if k != "tests"}, indent=1)); print(R.to_string(index=False))
