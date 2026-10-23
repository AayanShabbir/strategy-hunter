"""vectorbt backtest of one variant: signal on bar close, fill next bar open, fees+slippage per side,
optional ATR stop. Equal-weight basket of independent per-symbol sleeves (as in h16)."""
import numpy as np, pandas as pd, vectorbt as vbt
from .signals import position, atr
def run_variant(D, spec, v):
    P = position(D, spec["base"]["idea"], v["base"], v["filters"])
    if spec.get("flat_eod") and spec["timeframe"] != "1Day":
        day = pd.Series(D["close"].index.normalize(), index=D["close"].index)
        last = day != day.shift(-1); P[last.values] = 0.0
    P = P.fillna(0.0)
    tgt = P.shift(1).fillna(0.0)                      # desired holding at open t (decided at close t-1)
    entries, exits = (tgt > 0) & (tgt.shift(1).fillna(0) <= 0), (tgt <= 0) & (tgt.shift(1).fillna(0) > 0)
    c = spec["costs"]; fee = c.get("fee_bps", 0) / 1e4; slip = c.get("slippage_bps", 5) / 1e4
    A = atr(D["high"], D["low"], D["close"], 14)
    stop_mult = (spec.get("stop") or {}).get("atr_mult")
    kw = {}
    risk = (A / D["close"]).shift(1)                  # 1x ATR as fraction, known at decision time
    if stop_mult: kw["sl_stop"] = (stop_mult * risk).fillna(np.inf)
    O = D["open"].ffill(); C = D["close"].ffill()
    pf = vbt.Portfolio.from_signals(C, entries, exits, price=O, fees=fee, slippage=slip, init_cash=1.0, freq="1D" if spec["timeframe"]=="1Day" else None, **kw)
    W = (pf.assets() > 0).astype(float)               # actual holdings (after stops)
    bar_ret = pf.returns().fillna(0).mean(axis=1)     # equal-weight sleeves
    ntr = int(pf.trades.count().sum())
    ent_mask = entries & D["close"].notna()
    stop_frac = float(((stop_mult or 1.0) * risk)[ent_mask].stack().median()) if ent_mask.values.any() else np.nan
    cost_stop = (2 * (fee + slip)) / stop_frac if stop_frac and stop_frac > 0 else np.inf
    return dict(bar_ret=bar_ret, W=W, trades=ntr, cost_stop=cost_stop, time_in_mkt=float(W.values.mean()),
                trades_by_bar=pf.trades.records_readable["Entry Timestamp"] if ntr else pd.Series(dtype="datetime64[ns]"))
def to_daily(r, tf):
    if tf == "1Day": return r
    return (1 + r).groupby(r.index.tz_localize(None).normalize()).prod() - 1
def bh_bar(D):
    O = D["open"]; return (O.shift(-1) / O - 1).fillna(0).mean(axis=1)
