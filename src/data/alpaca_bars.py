"""Alpaca Market Data v2 historical daily bars (READ-ONLY research data; no trading endpoints, no orders, no account calls).

Why: Alpaca's consolidated (SIP) history keeps bars for symbols that have since been delisted/acquired, which Yahoo mostly drops.
Limit: coverage starts 2016-01-04, so names removed before 2016 stay unpriced.
Credentials come from the environment (ALPACA_API_KEY + ALPACA_SECRET_KEY, alias ALPACA_API_SECRET) and are sent only as request
headers to data.alpaca.markets. They are never logged, cached, written to a panel/meta, or included in an exception message.
"""
from __future__ import annotations
import os, time
from pathlib import Path
import numpy as np

BASE = "https://data.alpaca.markets/v2/stocks/bars"
FIELDS = {"c": "Close", "h": "High", "l": "Low", "v": "Volume"}


def have_credentials() -> bool:
    return bool(os.environ.get("ALPACA_API_KEY")) and bool(os.environ.get("ALPACA_SECRET_KEY") or os.environ.get("ALPACA_API_SECRET"))


def _headers() -> dict:
    k = os.environ.get("ALPACA_API_KEY"); s = os.environ.get("ALPACA_SECRET_KEY") or os.environ.get("ALPACA_API_SECRET")
    if not (k and s): raise RuntimeError("Alpaca market-data credentials are not set in the environment")
    return {"APCA-API-KEY-ID": k, "APCA-API-SECRET-KEY": s}


def to_alpaca(t: str) -> str: return t.replace("-", ".")      # BRK-B (yfinance style) -> BRK.B
def from_alpaca(t: str) -> str: return t.replace(".", "-")


def fetch_bars(tickers, start: str, end: str, batch: int = 40, feed: str = "sip", sleep: float = 0.35, session=None) -> dict:
    """{yfinance-style ticker: DataFrame[Close, High, Low, Volume] indexed by trading date}. `end` is inclusive. Adjusted for
    splits AND dividends (adjustment='all'), i.e. comparable to yfinance auto_adjust. Tickers with no bars are absent."""
    import pandas as pd, requests
    ses = session or requests.Session(); hd = _headers(); out: dict = {}
    end_excl = (pd.Timestamp(end) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    syms = [to_alpaca(t) for t in sorted(set(tickers))]
    for i in range(0, len(syms), batch):
        rows: dict = {}; tok = None
        while True:
            q = dict(symbols=",".join(syms[i:i + batch]), timeframe="1Day", start=start, end=end_excl, limit=10000,
                     adjustment="all", feed=feed, sort="asc")
            if tok: q["page_token"] = tok
            for attempt in range(5):
                r = ses.get(BASE, headers=hd, params=q, timeout=60)
                if r.status_code == 429: time.sleep(2 + 3 * attempt); continue
                break
            if r.status_code != 200: raise RuntimeError(f"Alpaca data request failed: HTTP {r.status_code} {r.text[:160]}")
            j = r.json()
            for s, bars in (j.get("bars") or {}).items(): rows.setdefault(s, []).extend(bars)
            tok = j.get("next_page_token")
            time.sleep(sleep)
            if not tok: break
        for s, bars in rows.items():
            df = pd.DataFrame(bars)
            idx = pd.DatetimeIndex(pd.to_datetime(df["t"]).dt.tz_convert("America/New_York").dt.tz_localize(None).dt.normalize())
            f = pd.DataFrame({v: df[k].astype(float).values for k, v in FIELDS.items()}, index=idx)
            out[from_alpaca(s)] = f[~f.index.duplicated(keep="last")].sort_index()
    return out


def fetch_cached(tickers, start: str, end: str, cache_dir: Path, tag: str = "alpaca") -> dict:
    """Same as fetch_bars, cached as one pickle per (tag, start, end, ticker-set hash) under cache_dir."""
    import hashlib, pickle
    from src.data.guard import forbid_sealed
    forbid_sealed(cache_dir, "use as a search-side cache")
    key = hashlib.sha256("|".join(sorted(set(tickers))).encode()).hexdigest()[:12]
    p = Path(cache_dir) / f"{tag}_{start}_{end}_{key}.pkl"
    if p.exists():
        with open(p, "rb") as f: return pickle.load(f)
    d = fetch_bars(tickers, start, end)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "wb") as f: pickle.dump(d, f)
    return d
