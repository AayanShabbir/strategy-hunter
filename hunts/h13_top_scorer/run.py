import sys, os, json, numpy as np, pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
from arch.bootstrap import SPA
sys.path.insert(0, "/workspace/trading-desk"); import desk_common as dc
D = "/workspace/research_lab/data/alpaca/h13_15m"; FEE = 7e-4; PRIOR_N = 324
syms = json.load(open("/workspace/trading-desk/state/liquid500_2026-10-16.json"))["symbols"]
F = {}
for s in syms:
    p = f"{D}/{s}.parquet"
    if not os.path.exists(p): continue
    x = pd.read_parquet(p)
    if x.empty: continue
    x.index = pd.DatetimeIndex(x.index).tz_convert("America/New_York")
    m = x.index.hour*60 + x.index.minute; x = x[(m >= 570) & (m <= 945)].copy()
    x["day"] = x.index.date; x["b"] = (x.index.hour*60 + x.index.minute - 570)//15
    pc = x.close.shift(1)
    tr = np.maximum(x.high - x.low, np.maximum((x.high - pc).abs(), (x.low - pc).abs()))
    x["atr"] = tr.rolling(14).mean()
    ema = x.close.ewm(span=20, adjust=False).mean()
    x["trend"] = (x.close - ema) / x.atr
    rng = x.high - x.low; x["candle"] = np.where(rng > 0, (x.close - x.open) / rng.replace(0, np.nan), 0.0)
    pv = (x.vwap * x.volume).groupby(x.day).cumsum(); vv = x.volume.groupby(x.day).cumsum()
    x["vw"] = (x.close - pv / vv) / x.atr
    piv = x.pivot_table(index="day", columns="b", values="volume")
    mv = piv.shift(1).rolling(20, min_periods=10).mean()
    x["rv"] = x.volume.values / mv.stack().reindex(list(zip(x.day, x.b))).values
    x = x.reset_index().rename(columns={"timestamp": "ts"}); x["sym"] = s
    F[s] = x
SPY = F.pop("SPY")
for s in list(F):
    if dc.symbol_block(s): F.pop(s)
A = pd.concat(F.values(), ignore_index=True)
elig = A[np.isfinite(A[["trend", "candle", "vw", "rv"]]).all(1) & (A.atr > 0) & (A.close >= 5)].copy()
g = elig.groupby("ts")
for k in ["trend", "candle", "vw"]: elig["u_"+k] = 2*g[k].rank(pct=True) - 1
elig["p_rv"] = g["rv"].rank(pct=True)
elig["s0"] = (elig.u_trend + elig.u_candle + elig.u_vw)/3 * elig.p_rv
elig["s2"] = (elig.u_trend + elig.u_vw)/2 * elig.p_rv
days = sorted(A.day.unique()); days = [d for d in days if d >= pd.Timestamp("2024-10-15").date()]
cut = days[int(len(days)*0.7)]; IS_days = set(days[:int(len(days)*0.7)])
elig = elig[elig.day.isin(set(days)) & (elig.b <= 21)]  # bar start <= 14:45
idx = {s: F[s].set_index("ts") for s in F}
arr = {s: (F[s].ts.values, F[s].open.values, F[s].high.values, F[s].low.values, F[s].close.values, F[s].day.values) for s in F}
pos = {s: pd.Index(F[s].ts) for s in F}
res = {}; trades_all = []
for V, col, flip in (("V0_cont", "s0", 1), ("V1_fade", "s0", -1), ("V2_cont_no_candle", "s2", 1)):
    e = elig.assign(a=elig[col].abs()); top = e.loc[e.groupby("ts").a.idxmax()].sort_values("ts")
    thr = float(top[top.day.isin(IS_days)].a.quantile(0.90))
    sig = top[top.a >= thr]; busy_until = pd.Timestamp("1900-01-01", tz="America/New_York"); T = []
    for _, r in sig.iterrows():
        if r.ts < busy_until: continue
        s = r.sym; ts_, O, H, L, C, DY = arr[s]; i = pos[s].get_loc(r.ts); j = i+1
        if j >= len(O) or DY[j] != DY[i]: continue
        side = flip * np.sign(r[col]); ent = O[j]; risk = 1.5*r.atr
        stp = ent - side*risk; tg = ent + side*2*risk; k = j; ex = None
        while k < len(O) and DY[k] == DY[i]:
            if side > 0:
                if L[k] <= stp: ex = L[k]; break
                if H[k] >= tg: ex = tg; break
            else:
                if H[k] >= stp: ex = H[k]; break
                if L[k] <= tg: ex = tg; break
            k += 1
        if ex is None: k -= 1; ex = C[k]
        ret = side*(ex - ent)/ent - 2*FEE
        T.append(dict(var=V, sym=s, side=int(side), t_in=ts_[j], t_out=ts_[k], day=DY[i], ret=ret, is_=DY[i] in IS_days))
        busy_until = pd.Timestamp(ts_[k]).tz_localize("UTC").tz_convert("America/New_York") if pd.Timestamp(ts_[k]).tzinfo is None else pd.Timestamp(ts_[k])
    T = pd.DataFrame(T); T["thr"] = thr; trades_all.append(T)
TR = pd.concat(trades_all)
sp = SPY.groupby("day").close.last(); sp = sp[sp.index.isin(set(days))]; spr = sp.pct_change().fillna(0)
dd = pd.Index(sp.index)
def daily(T):
    r = (0.10*T.ret).groupby(T.day).apply(lambda v: np.prod(1+v)-1)
    return r.reindex(dd).fillna(0)
def stat(r):
    eq = (1+r).cumprod(); return dict(ret=round((eq.iloc[-1]-1)*100, 2), sharpe=round(r.mean()/r.std()*np.sqrt(252), 3) if r.std() > 0 else 0, mdd=round(((eq/eq.cummax())-1).min()*100, 2))
oos = dd >= cut; b7030 = 0.7*spr
R = {V: daily(TR[TR["var"] == V]) for V in TR["var"].unique()}
out = {"split": {"is": f"{days[0]}..{max(IS_days)}", "oos": f"{cut}..{days[-1]}"}, "n_symbols": len(F),
       "bench_oos": {"SPY": stat(spr[oos]), "70/30": stat(b7030[oos])}, "variants": {}}
pvals = []
for V, r in R.items():
    T = TR[TR["var"] == V]; To = T[~T.is_]; w = To[To.ret > 0]; l = To[To.ret <= 0]
    p = float(stats.ttest_1samp(To.ret, 0, alternative="greater").pvalue) if len(To) > 2 else 1.0; pvals.append(p)
    ro = r[oos]; sr = ro.mean()/ro.std() if ro.std() > 0 else 0; n = len(ro)
    # DSR: expected max SR under N trials
    N = PRIOR_N + 3; em = np.euler_gamma; var_sr = (1 - stats.skew(ro)*sr + (stats.kurtosis(ro, fisher=False)-1)/4*sr**2)/(n-1)
    sr0 = np.sqrt(1/(n-1)) * ((1-em)*stats.norm.ppf(1-1/N) + em*stats.norm.ppf(1-1/(N*np.e)))
    dsr = float(stats.norm.cdf((sr - sr0)/np.sqrt(max(var_sr, 1e-12))))
    spa = {}  # arch SPA takes LOSSES -> pass negative returns
    for bn, b in (("SPY", spr[oos]), ("70/30", b7030[oos])):
        s_ = SPA(-b.values, -ro.values.reshape(-1, 1), reps=10000, seed=13); s_.compute(); spa[bn] = round(float(s_.pvalues["consistent"]), 4)
    out["variants"][V] = dict(threshold=round(float(T.thr.iloc[0]), 4), trades_is=int(T.is_.sum()), trades_oos=len(To),
        win_pct=round(len(w)/max(len(To), 1)*100, 2), avg_win_bps=round(w.ret.mean()*1e4, 1), avg_loss_bps=round(l.ret.mean()*1e4, 1),
        avg_net_bps=round(To.ret.mean()*1e4, 2), is_stats=stat(r[~oos]), oos_stats=stat(ro), p=round(p, 5), dsr=round(dsr, 4), spa_p=spa)
hp = multipletests(np.concatenate([pvals, np.ones(PRIOR_N)]), method="holm")[1][:3]
for V, h in zip(R, hp): out["variants"][V]["holm_p"] = round(float(h), 4)
# PBO via CSCV, 16 blocks
M = pd.DataFrame(R).values; S = 16; blocks = np.array_split(np.arange(len(M)), S); from itertools import combinations
lam = []
for c in combinations(range(S), S//2):
    i1 = np.concatenate([blocks[k] for k in c]); i2 = np.concatenate([blocks[k] for k in range(S) if k not in c])
    sh = lambda X: X.mean(0)/(X.std(0)+1e-12); b = np.argmax(sh(M[i1])); rk = stats.rankdata(sh(M[i2]))[b]/(M.shape[1]+1)
    lam.append(np.log(rk/(1-rk)))
out["pbo"] = round(float(np.mean(np.array(lam) <= 0)), 4)
sb = out["bench_oos"]["SPY"]["sharpe"]
for V, v in out["variants"].items():
    v["pass"] = bool(v["oos_stats"]["ret"] > 0 and v["oos_stats"]["sharpe"] > sb and v["holm_p"] < 0.05 and v["dsr"] > 0.95 and out["pbo"] < 0.5 and max(v["spa_p"].values()) < 0.05)
json.dump(out, open("results.json", "w"), indent=1, default=str); TR.to_parquet("trades.parquet")
best = max(R, key=lambda V: out["variants"][V]["oos_stats"]["sharpe"])
try:
    import quantstats as qs
    ix = pd.DatetimeIndex(pd.to_datetime(dd[oos]))
    qs.reports.html(pd.Series(R[best][oos].values, ix), benchmark=pd.Series(spr[oos].values, ix), output="tearsheet.html", title=f"h13 {best} OOS")
    out["tearsheet"] = best
except Exception as e: out["tearsheet_err"] = str(e)
json.dump(out, open("results.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
