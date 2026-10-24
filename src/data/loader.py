"""SDE Phase 2 data loader.

CSI300: Qlib public cn_data (chenditc/investment_data release, qlib_bin format) read directly from its binary
files (no pyqlib dependency; pyqlib has no wheel for this Python). Point-in-time CSI300 membership comes from
instruments/csi300.txt, so there is no index-membership look-ahead. Fallback: akshare (current constituent list,
survivorship-biased; flagged in meta). S&P 500: yfinance (current Wikipedia constituents => survivorship-biased,
flagged in meta). Everything is cached under data/sde/ (gitignored) -- never committed.

Splits (blueprint): CSI train 2010-2020 / val 2021 / test 2022-2024; S&P train 2010-2016 / val 2017 / test 2018-2020.
Label y_t = close_{t+20}/close_t - 1 (AlphaGen/AlphaSAGE convention); y is NaN when t+20 falls beyond the split end
(purge, so no label peeks into the next split).
"""
from __future__ import annotations
import json, os
from dataclasses import dataclass, field
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.environ.get("SDE_DATA_DIR", ROOT / "data" / "sde"))
QLIB_DIR = DATA_DIR / "qlib_bin"
QLIB_URL = "https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz"
FIELDS = {"$close": "close", "$high": "high", "$low": "low", "$volume": "volume"}
WARMUP_START = "2009-01-01"       # >=60 trading days of look-back before the first train day
LABEL_HORIZON = 20

SPLITS = {
    "csi300": {"train": ("2010-01-01", "2020-12-31"), "val": ("2021-01-01", "2021-12-31"), "test": ("2022-01-01", "2024-12-31")},
    "csi500": {"train": ("2010-01-01", "2020-12-31"), "val": ("2021-01-01", "2021-12-31"), "test": ("2022-01-01", "2024-12-31")},
    "csi1000": {"train": ("2010-01-01", "2020-12-31"), "val": ("2021-01-01", "2021-12-31"), "test": ("2022-01-01", "2024-12-31")},
    "sp500": {"train": ("2010-01-01", "2016-12-31"), "val": ("2017-01-01", "2017-12-31"), "test": ("2018-01-01", "2020-12-31")},
}


@dataclass
class Panel:
    dates: np.ndarray                 # datetime64[D], length D
    assets: list
    data: dict                        # '$close' etc -> (D, N) float64
    member: np.ndarray                # (D, N) bool, point-in-time universe membership (and has a price)
    meta: dict = field(default_factory=dict)

    def idx(self, start, end):
        a = np.searchsorted(self.dates, np.datetime64(start), "left")
        b = np.searchsorted(self.dates, np.datetime64(end), "right")
        return a, b

    def label(self, split_end, horizon: int = LABEL_HORIZON):
        """Forward return label, NaN where t+horizon is past split_end (purge)."""
        c = self.data["$close"]; y = np.full_like(c, np.nan)
        y[:-horizon] = c[horizon:] / c[:-horizon] - 1.0
        last = np.searchsorted(self.dates, np.datetime64(split_end), "right") - 1   # last day index inside the split
        y[max(last - horizon + 1, 0):] = np.nan
        y[~np.isfinite(y)] = np.nan
        return y

    def split_mask(self, start, end):
        """Boolean (D,N): members on days inside [start, end]."""
        m = np.zeros_like(self.member); a, b = self.idx(start, end); m[a:b] = self.member[a:b]
        return m


# ---------------------------------------------------------------- Qlib cn_data
def ensure_qlib_data(download: bool = True) -> Path:
    if (QLIB_DIR / "calendars" / "day.txt").exists(): return QLIB_DIR
    if not download: raise FileNotFoundError(f"Qlib data not found at {QLIB_DIR}")
    import subprocess
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    tgz = DATA_DIR / "qlib_bin.tar.gz"
    subprocess.run(["curl", "-sL", "-o", str(tgz), QLIB_URL], check=True)
    subprocess.run(["tar", "xzf", str(tgz)], cwd=DATA_DIR, check=True)
    return QLIB_DIR


def _read_bin(path: Path, n_cal: int) -> np.ndarray:
    a = np.fromfile(path, dtype="<f4")
    out = np.full(n_cal, np.nan)
    if len(a) < 2: return out
    s = int(a[0]); v = a[1:].astype(float)
    e = min(s + len(v), n_cal)
    out[s:e] = v[: e - s]
    return out


def _qlib_membership(universe: str, cal: np.ndarray, tickers_wanted=None):
    spans = {}
    for line in (QLIB_DIR / "instruments" / f"{universe}.txt").read_text().splitlines():
        p = line.split()
        if len(p) < 3: continue
        spans.setdefault(p[0].lower(), []).append((np.datetime64(p[1]), np.datetime64(p[2])))
    return spans


def load_qlib(universe: str = "csi300", start: str = WARMUP_START, end: str = "2024-12-31") -> Panel:
    ensure_qlib_data()
    cal_all = np.array(open(QLIB_DIR / "calendars" / "day.txt").read().split(), dtype="datetime64[D]")
    lo = int(np.searchsorted(cal_all, np.datetime64(start), "left")); hi = int(np.searchsorted(cal_all, np.datetime64(end), "right"))
    cal = cal_all[lo:hi]
    spans = _qlib_membership(universe, cal)
    keep = [k for k, v in spans.items() if any(b >= cal[0] and a <= cal[-1] for a, b in v)]
    assets, cols, member = [], {f: [] for f in FIELDS}, []
    for k in sorted(keep):
        d = QLIB_DIR / "features" / k
        if not (d / "close.day.bin").exists(): continue
        arrs = {f: _read_bin(d / f"{n}.day.bin", len(cal_all))[lo:hi] for f, n in FIELDS.items()}
        m = np.zeros(len(cal), dtype=bool)
        for a, b in spans[k]: m |= (cal >= a) & (cal <= b)
        m &= np.isfinite(arrs["$close"]) & (arrs["$volume"] > 0)
        if not m.any(): continue
        assets.append(k.upper()); member.append(m)
        for f in FIELDS: cols[f].append(arrs[f])
    data = {f: np.stack(v, axis=1) for f, v in cols.items()}
    data["$volume"] = np.where(data["$volume"] > 0, data["$volume"], np.nan)    # suspended day: no volume
    return Panel(cal, assets, data, np.stack(member, axis=1),
                 meta={"source": "qlib cn_data (chenditc/investment_data)", "universe": universe,
                       "membership": "point-in-time (instruments file)", "survivorship": "delisted names included per Qlib data",
                       "prices": "qlib-adjusted (normalized per stock; ratios valid, absolute level not)"})


# ---------------------------------------------------------------- fallbacks
def load_csi300_akshare(start="2009-01-01", end="2024-12-31", max_assets=None) -> Panel:
    """Fallback if Qlib data is unavailable. Current CSI300 constituents only (survivorship-biased)."""
    import akshare as ak, pandas as pd
    cons = ak.index_stock_cons_csindex(symbol="000300")["成分券代码"].astype(str).tolist()[:max_assets]
    frames = {}
    for c in cons:
        try:
            df = ak.stock_zh_a_hist(symbol=c, period="daily", start_date=start.replace("-", ""), end_date=end.replace("-", ""), adjust="qfq")
            df["日期"] = pd.to_datetime(df["日期"]); frames[c] = df.set_index("日期")
        except Exception:
            continue
    return _panel_from_frames(frames, {"close": "收盘", "high": "最高", "low": "最低", "volume": "成交量"},
                              {"source": "akshare (eastmoney, qfq)", "universe": "csi300",
                               "membership": "CURRENT constituents applied to all dates", "survivorship": "BIASED (current members only)"})


def sp500_tickers() -> list:
    import pandas as pd, io, urllib.request
    req = urllib.request.Request("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode()
    return [t.replace(".", "-") for t in pd.read_html(io.StringIO(html))[0]["Symbol"].tolist()]


def load_sp500(tickers=None, start="2009-01-01", end="2020-12-31", cache=True) -> Panel:
    """S&P 500 via yfinance (auto-adjusted). Current constituents (Wikipedia) => survivorship-biased; flagged in meta."""
    import yfinance as yf, pandas as pd
    tickers = tickers or sp500_tickers()
    cp = DATA_DIR / "cache" / f"sp500_{start}_{end}_{len(tickers)}.pkl"
    if cache and cp.exists(): raw = pd.read_pickle(cp)
    else:
        raw = yf.download(tickers, start=start, end=str(np.datetime64(end) + 1), auto_adjust=True, progress=False, threads=True)
        if cache: cp.parent.mkdir(parents=True, exist_ok=True); raw.to_pickle(cp)
    frames = {t: pd.DataFrame({k: raw[k][t] for k in ("Close", "High", "Low", "Volume")}).dropna(subset=["Close"]) for t in tickers if t in raw["Close"]}
    return _panel_from_frames(frames, {"close": "Close", "high": "High", "low": "Low", "volume": "Volume"},
                              {"source": "yfinance (auto-adjusted)", "universe": "sp500",
                               "membership": "CURRENT constituents applied to all dates", "survivorship": "BIASED (current members only)"})


def _panel_from_frames(frames: dict, cols: dict, meta: dict) -> Panel:
    import pandas as pd
    idx = sorted(set().union(*[set(f.index) for f in frames.values()]))
    assets = sorted(frames)
    data = {k: np.stack([frames[a][cols[n]].reindex(idx).to_numpy(float) for a in assets], axis=1) for k, n in
            {"$close": "close", "$high": "high", "$low": "low", "$volume": "volume"}.items()}
    member = np.isfinite(data["$close"])
    return Panel(np.array(idx, dtype="datetime64[D]"), assets, data, member, meta)


def load_panel(universe: str = "csi300", upto: str = "train", source: str = "auto") -> Panel:
    """Load a universe up to the end of the named split ('train','val','test'). Training runs use upto='train', so the
    process never even holds validation/test prices in memory."""
    sp = SPLITS[universe]; end = sp[upto][1]
    if universe == "sp500": return load_sp500(end=end)
    if source in ("auto", "qlib"):
        try: return load_qlib(universe, end=end)
        except Exception as e:
            if source == "qlib": raise
            print(f"[loader] Qlib unavailable ({e!r}); falling back to akshare")
    return load_csi300_akshare(end=end)
