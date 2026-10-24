"""Survivorship-REDUCED S&P 500 universe (an addition to, not a replacement of, the blueprint run in loader.load_sp500).

Membership: point-in-time ticker windows from the public MIT-licensed dataset https://github.com/fja05680/sp500
(`sp500_ticker_start_end.csv`, derived from its "S&P 500 Historical Components & Changes" file; downloaded at run time into
the git-ignored data/sde/cache/, never committed). Prices: yfinance (auto-adjusted), the only free source used.

What this does and does NOT fix (all of it is recorded in Panel.meta and printed by `coverage_report`):
  * Fixed: today's constituents are no longer applied to all dates; a stock is a member only inside its real windows
    (so e.g. late joiners are excluded before they joined, and removed stocks are included while they were members).
  * NOT fixed: yfinance has no price history for most delisted/acquired tickers. A ticker is kept only if its prices cover
    >= 95 % of its membership days in the window (this also rejects re-used tickers, whose Yahoo history belongs to a
    different company in the window). Names that fail are dropped entirely, so the universe is still tilted toward
    survivors; the fraction of point-in-time member-days that have prices is stored as `coverage`.
"""
from __future__ import annotations
import io, urllib.request
from pathlib import Path
import numpy as np
from src.data.loader import DATA_DIR, Panel, _panel_from_frames, load_sp500

URL = "https://raw.githubusercontent.com/fja05680/sp500/master/sp500_ticker_start_end.csv"
CACHE = DATA_DIR / "cache"
MIN_COVER = 0.95
START, END = "2009-01-01", "2020-12-31"
W0, W1 = "2010-01-01", "2020-12-31"           # evaluation window (train start .. test end)


def _y(t: str) -> str: return t.replace(".", "-")


def membership_windows(refresh: bool = False):
    import pandas as pd
    p = CACHE / "sp500_pit_ticker_start_end.csv"
    if refresh or not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    d = pd.read_csv(p, parse_dates=["start_date", "end_date"]); d["yt"] = d["ticker"].map(_y)
    return d


def _download(tickers, cache=True):
    import yfinance as yf, pandas as pd
    cp = CACHE / f"sp500_pit_extra_{START}_{END}_{len(tickers)}.pkl"
    if cache and cp.exists(): return pd.read_pickle(cp)
    raw = yf.download(sorted(tickers), start=START, end=str(np.datetime64(END) + 1), auto_adjust=True, progress=False, threads=True)
    if cache: cp.parent.mkdir(parents=True, exist_ok=True); raw.to_pickle(cp)
    return raw


def membership_mask(dates, assets, win, w0=W0, w1=W1) -> np.ndarray:
    """(D, A) bool: asset is a member on day d iff start_date <= d < end_date (end exclusive; open end = still a member)
    inside [w0, w1]. Several windows per ticker are OR-ed (tickers that left and re-joined)."""
    import pandas as pd
    dates = pd.DatetimeIndex(dates); idx = {a: i for i, a in enumerate(assets)}
    pit = np.zeros((len(dates), len(assets)), bool); inwin = (dates >= w0) & (dates <= w1)
    for _, r in win.iterrows():
        i = idx.get(r.yt)
        if i is None: continue
        m = (dates >= r.start_date) & inwin
        if not pd.isna(r.end_date): m &= dates < r.end_date
        pit[m, i] = True
    return pit


def coverage_keep(pit: np.ndarray, px: np.ndarray, min_cover: float = MIN_COVER) -> np.ndarray:
    """Keep a ticker only if prices exist on >= min_cover of its membership days (drops re-used tickers / patchy data)."""
    n = pit.sum(0)
    return (n == 0) | ((pit & px).sum(0) >= min_cover * np.maximum(n, 1))


def load_sp500_pit(cache: bool = True) -> Panel:
    import pandas as pd
    win = membership_windows()
    base = load_sp500(end=END, cache=cache)                       # current constituents (already cached by the blueprint runs)
    have = set(base.assets)
    need = sorted(set(win[(win.start_date <= W1) & (win.end_date.isna() | (win.end_date >= W0))].yt) - have)
    raw = _download(need, cache) if need else None
    frames = {}
    for j, a in enumerate(base.assets):
        frames[a] = pd.DataFrame({k: base.data[k2][:, j] for k, k2 in (("Close", "$close"), ("High", "$high"), ("Low", "$low"), ("Volume", "$volume"))},
                                 index=pd.DatetimeIndex(base.dates)).dropna(subset=["Close"])
    if raw is not None:
        for t in need:
            if t in raw["Close"] and raw["Close"][t].notna().any():
                frames[t] = pd.DataFrame({k: raw[k][t] for k in ("Close", "High", "Low", "Volume")}).dropna(subset=["Close"])
    pan = _panel_from_frames(frames, {"close": "Close", "high": "High", "low": "Low", "volume": "Volume"}, {})
    dates = pd.DatetimeIndex(pan.dates); A = len(pan.assets); idx = {a: i for i, a in enumerate(pan.assets)}
    inwin = (dates >= W0) & (dates <= W1)
    pit = membership_mask(dates, pan.assets, win, W0, W1)
    px = np.isfinite(pan.data["$close"])
    keep = coverage_keep(pit, px)
    member = pit & px & keep[None, :]
    # bookkeeping on the whole PIT universe (members with or without prices)
    all_pit_names = set(win[(win.start_date <= W1) & (win.end_date.isna() | (win.end_date >= W0))].yt)
    covered = {pan.assets[i] for i in range(A) if member[:, i].any()}
    left = set(win[(win.start_date <= W1) & win.end_date.notna() & (win.end_date >= W0) & (win.end_date <= W1)].yt)   # removed during 2010-2020
    # member-day coverage: pit membership windows over trading days vs member-days we can actually use
    tot_pit_days = 0
    for _, r in win.iterrows():
        m = (dates >= r.start_date) & inwin
        if not pd.isna(r.end_date): m &= dates < r.end_date
        tot_pit_days += int(m.sum())
    avg_pit = tot_pit_days / max(int(inwin.sum()), 1)
    pan.member = member
    pan.meta = {"source": "yfinance (auto-adjusted) + fja05680/sp500 point-in-time ticker windows (MIT)", "universe": "sp500_pit",
                "membership": "point-in-time windows 2010-2020 (price-covered names only)",
                "survivorship": "REDUCED, NOT ELIMINATED (delisted names without free price history are missing)",
                "min_cover": MIN_COVER, "pit_names_2010_2020": len(all_pit_names), "pit_names_with_prices": len(covered),
                "removed_2010_2020_names": len(left), "removed_2010_2020_with_prices": len(left & covered),
                "avg_pit_members_per_day": round(avg_pit, 1),
                "avg_usable_members_per_day": round(float(member[inwin].sum(1).mean()), 1),
                "member_day_coverage": round(float(member[inwin].sum(1).mean()) / avg_pit, 4)}
    return pan


def coverage_report(pan: Panel) -> dict:
    import pandas as pd
    d = pd.DatetimeIndex(pan.dates); out = {}
    for y in range(2010, 2021):
        m = pan.member[d.year == y]; out[y] = round(float(m.sum(1).mean()), 1)
    return {"meta": pan.meta, "usable_members_per_day_by_year": out}
