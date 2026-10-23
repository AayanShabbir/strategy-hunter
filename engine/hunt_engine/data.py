"""Bars loader: local parquet cache (data_cache/<tf>/<SYM>.parquet), Alpaca IEX fetch for misses.
Keys come from env ALPACA_API_KEY / ALPACA_SECRET_KEY and are never printed. Market-data only; no trading client.
Hunt runs ALWAYS get data truncated before the vault start (see vault.py)."""
import os, datetime as dt, pandas as pd
from .util import paths
from . import vault
COLS = ["open", "high", "low", "close", "volume"]
def is_crypto(sym): return "/" in sym          # e.g. SOL/USD (Alpaca crypto spot pair)
def _cache_file(tf, sym): return os.path.join(paths()["cache"], tf, f"{sym.replace('/', '_')}.parquet")
def fetch_alpaca_crypto(sym, tf, start="2020-01-01"):
    """Alpaca crypto bars (US venue, 24/7; 1Day bars are UTC-midnight days). Market data only."""
    from alpaca.data.historical import CryptoHistoricalDataClient
    from alpaca.data.requests import CryptoBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    tfo = {"1Day": TimeFrame.Day, "1Hour": TimeFrame.Hour, "15Min": TimeFrame(15, TimeFrameUnit.Minute)}[tf]
    k, s = os.environ.get("ALPACA_API_KEY"), os.environ.get("ALPACA_SECRET_KEY")
    c = CryptoHistoricalDataClient(k, s) if (k and s) else CryptoHistoricalDataClient()
    df = c.get_crypto_bars(CryptoBarsRequest(symbol_or_symbols=sym, timeframe=tfo, start=pd.Timestamp(start, tz="UTC"))).df
    if df.empty: return df
    df = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
    return df[COLS]
def fetch_alpaca(sym, tf, start="2016-01-01"):
    if is_crypto(sym): return fetch_alpaca_crypto(sym, tf)
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    from alpaca.data.enums import DataFeed
    tfo = {"1Day": TimeFrame.Day, "1Hour": TimeFrame.Hour, "15Min": TimeFrame(15, TimeFrameUnit.Minute)}[tf]
    k, s = os.environ.get("ALPACA_API_KEY"), os.environ.get("ALPACA_SECRET_KEY")
    if not (k and s): raise RuntimeError("Alpaca market-data keys not in env (ALPACA_API_KEY/ALPACA_SECRET_KEY)")
    c = StockHistoricalDataClient(k, s)
    df = c.get_stock_bars(StockBarsRequest(symbol_or_symbols=sym, timeframe=tfo, start=pd.Timestamp(start), feed=DataFeed.IEX)).df
    if df.empty: return df
    df = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
    return df[COLS]
def get(sym, tf, refresh=False):
    f = _cache_file(tf, sym)
    if os.path.exists(f) and not refresh: return pd.read_parquet(f)
    df = fetch_alpaca(sym, tf)
    os.makedirs(os.path.dirname(f), exist_ok=True); df.to_parquet(f + ".tmp"); os.replace(f + ".tmp", f)
    return df
def _norm_index(df, tf, sym=""):
    idx = pd.to_datetime(df.index)
    if idx.tz is None: idx = idx.tz_localize("UTC")
    if tf == "1Day" and is_crypto(sym):          # crypto day = UTC calendar day (24/7), label by UTC date
        out = df.copy(); out.index = idx.tz_convert("UTC").tz_localize(None).normalize(); return out[~out.index.duplicated()].sort_index()
    idx = idx.tz_convert("America/New_York")
    if tf == "1Day": idx = idx.tz_localize(None).normalize()
    out = df.copy(); out.index = idx; return out[~out.index.duplicated()].sort_index()
def load(symbols, tf, allow_vault=False, refresh=False):
    """Returns dict field -> DataFrame(time x symbol). allow_vault only for vault.vault_test."""
    frames = {s: _norm_index(get(s, tf, refresh), tf, s) for s in symbols}
    D = {c: pd.DataFrame({s: f[c] for s, f in frames.items()}) for c in COLS}
    if not allow_vault:
        cut = vault.vault_start_ts(tf)
        D = {c: x[x.index < cut] for c, x in D.items()}
    return D
def seed_cache():
    """One-time: copy existing research data (read-only) into the engine cache."""
    n = 0
    src = "/workspace/trading-desk/validation/hunt2/d1_500.pkl"   # read-only use
    if os.path.exists(src):
        d = pd.read_pickle(src)
        for sym, g in d.groupby(level=0):
            f = _cache_file("1Day", sym); os.makedirs(os.path.dirname(f), exist_ok=True)
            g.droplevel(0)[COLS].to_parquet(f); n += 1
    d15 = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "data", "alpaca", "h13_15m"))
    if os.path.isdir(d15):
        for fn in os.listdir(d15):
            f = _cache_file("15Min", fn[:-8]); os.makedirs(os.path.dirname(f), exist_ok=True)
            pd.read_parquet(os.path.join(d15, fn))[COLS].to_parquet(f); n += 1
    return n
