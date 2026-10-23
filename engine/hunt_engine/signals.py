"""Base ideas and filters. Each returns a 0/1 desired-position DataFrame decided on bar close (no lookahead;
execution happens next bar open in backtest.py)."""
import numpy as np, pandas as pd
def atr(H, L, C, n):
    pc = C.shift(1); tr = pd.concat([H - L, (H - pc).abs(), (L - pc).abs()]).groupby(level=0).max().reindex(C.index)
    return tr.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
def rsi(C, n):
    d = C.diff(); up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False, min_periods=n).mean(); return 100 - 100 / (1 + up / dn)
def _supertrend_1(h, l, c, n, m):  # same rules as h16
    tr = np.maximum(h - l, np.maximum(abs(h - np.r_[np.nan, c[:-1]]), abs(l - np.r_[np.nan, c[:-1]]))); tr[0] = h[0] - l[0]
    a = pd.Series(tr).ewm(alpha=1 / n, adjust=False, min_periods=n).mean().values
    hl = (h + l) / 2; bu = hl + m * a; bl = hl - m * a; fu = bu.copy(); fl = bl.copy(); d = np.zeros(len(c))
    for i in range(1, len(c)):
        if np.isnan(a[i]): continue
        fu[i] = bu[i] if (np.isnan(fu[i-1]) or bu[i] < fu[i-1] or c[i-1] > fu[i-1]) else fu[i-1]
        fl[i] = bl[i] if (np.isnan(fl[i-1]) or bl[i] > fl[i-1] or c[i-1] < fl[i-1]) else fl[i-1]
        d[i] = (1 if c[i] > fu[i] else -1) if d[i-1] <= 0 else (-1 if c[i] < fl[i] else 1)
    return (d > 0).astype(float)
def supertrend(D, atr_n=10, mult=3):
    out = {}
    for s in D["close"]:
        ok = D["close"][s].dropna().index
        out[s] = pd.Series(_supertrend_1(D["high"][s][ok].values, D["low"][s][ok].values, D["close"][s][ok].values, atr_n, mult), index=ok)
    return pd.DataFrame(out).reindex(D["close"].index).fillna(0)
def sma_cross(D, fast=20, slow=100):
    C = D["close"]; return (C.rolling(fast).mean() > C.rolling(slow).mean()).astype(float)
def donchian(D, entry_n=55, exit_n=20):
    C = D["close"]; up = C > D["high"].rolling(entry_n).max().shift(1); dn = C < D["low"].rolling(exit_n).min().shift(1)
    st = pd.DataFrame(np.nan, index=C.index, columns=C.columns); st[up] = 1.0; st[dn] = 0.0; return st.ffill().fillna(0)
def rsi_revert(D, n=2, entry=10, exit=70):
    r = rsi(D["close"], n); st = pd.DataFrame(np.nan, index=r.index, columns=r.columns)
    st[r < entry] = 1.0; st[r > exit] = 0.0; return st.ffill().fillna(0)
def random_entry(D, p_switch=0.05, seed=0):  # explicit random idea (useful as a sanity spec)
    rng = np.random.default_rng(seed); x = rng.random(D["close"].shape) < p_switch
    return pd.DataFrame(np.cumsum(x, 0) % 2, index=D["close"].index, columns=D["close"].columns).astype(float)
def rel_strength(D, bench="BTC/USD", n=30, abs_filter=True):
    """Long a symbol while its n-bar return beats the benchmark's n-bar return (and, if abs_filter, is > 0).
    Benchmark bars come from data.load (vault-truncated like everything else); decided on bar close."""
    from . import data
    C = D["close"]; tf = "1Day" if (C.index == C.index.normalize()).all() else None
    b = data.load([bench], tf or "1Hour")["close"][bench].reindex(C.index).ffill()
    r = C.pct_change(n); rb = b.pct_change(n)
    m = r.gt(rb, axis=0)
    if abs_filter: m = m & (r > 0)
    return m.astype(float).where(r.notna() & rb.notna().values[:, None], 0.0)
def drop_revert(D, n=3, drop=0.15, hold=5):
    """Long after the n-bar return falls below -drop (sharp sell-off); hold a fixed `hold` bars, then flat."""
    C = D["close"]; trig = (C.pct_change(n) < -drop).astype(float)
    return (trig.rolling(hold, min_periods=1).max() > 0).astype(float)
IDEAS = dict(rel_strength=rel_strength, drop_revert=drop_revert, supertrend=supertrend, sma_cross=sma_cross, donchian=donchian, rsi_revert=rsi_revert, random_entry=random_entry)
# ---- filters: boolean masks, position allowed only where True
def trend_sma(D, n=200): C = D["close"]; return C > C.rolling(n).mean()
def relvol(D, n=20, min_ratio=1.2): V = D["volume"]; return V > min_ratio * V.rolling(n).mean()
def vol_regime(D, n=14, max_atr_pct=0.03): return atr(D["high"], D["low"], D["close"], n) / D["close"] < max_atr_pct
def rsi_band(D, n=14, lo=0, hi=70): r = rsi(D["close"], n); return (r >= lo) & (r <= hi)
def session(D, start="09:30", end="15:45"):
    t = D["close"].index.time; m = (t >= pd.Timestamp(start).time()) & (t <= pd.Timestamp(end).time())
    return pd.DataFrame(np.repeat(m[:, None], D["close"].shape[1], 1), index=D["close"].index, columns=D["close"].columns)
def bench_trend(D, bench="BTC/USD", n=100):
    """Allow positions only while the benchmark coin closes above its n-bar SMA (BTC-trend gate)."""
    from . import data
    C = D["close"]; tf = "1Day" if (C.index == C.index.normalize()).all() else "1Hour"
    b = data.load([bench], tf)["close"][bench].reindex(C.index).ffill(); m = (b > b.rolling(n).mean()).values
    return pd.DataFrame(np.repeat(m[:, None], C.shape[1], 1), index=C.index, columns=C.columns)
def day_of_week(D, days=(0, 1, 2, 3, 4)):
    """Allow positions only on listed weekdays (Mon=0..Sun=6) of the decision bar."""
    days = [days] if isinstance(days, int) else list(days); m = np.isin(D["close"].index.dayofweek, days)
    return pd.DataFrame(np.repeat(m[:, None], D["close"].shape[1], 1), index=D["close"].index, columns=D["close"].columns)
FILTERS = dict(day_of_week=day_of_week, bench_trend=bench_trend, trend_sma=trend_sma, relvol=relvol, vol_regime=vol_regime, rsi_band=rsi_band, session=session)
def position(D, idea, base_params, filters):
    P = IDEAS[idea](D, **base_params)
    for fn, fp in filters: P = P.where(FILTERS[fn](D, **fp).fillna(False), 0.0)
    return P
