"""Third-party free price file used to fill pre-2016 history of removed S&P 500 names: FINSABER-reproduce (Hugging Face, Apache-2.0),
`data/price/all_sp500_prices_2000_2024_delisted_include.csv` (daily OHLCV + adjusted close, 2000-01-03..2024-12-31, 1,017 symbols
incl. delisted S&P 500 members). Downloaded into the git-ignored data/sde/cache/external/ (never committed), pinned by SHA-256.
Provenance of the underlying quotes is not stated by the publisher, so it is only ever used (a) where it AGREES with a second source
on an overlap, or (b) alone, with explicit integrity checks and a per-ticker flag in the provenance report."""
from __future__ import annotations
import hashlib, urllib.request
from pathlib import Path

URL = "https://huggingface.co/datasets/finsaber-team/FINSABER-reproduce/resolve/main/data/price/all_sp500_prices_2000_2024_delisted_include.csv"
SHA256 = "f67e3972dceefbbdf6c17b84b30957a7b83518401955fff8ae0bc4ae206fa83f"
FNAME = "finsaber_sp500_2000_2024_delisted.csv"


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""): h.update(b)
    return h.hexdigest()


def finsaber_path(cache_dir: Path, download: bool = True) -> Path:
    p = Path(cache_dir) / "external" / FNAME
    if not p.exists():
        if not download: raise FileNotFoundError(p)
        p.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=600) as r, open(p, "wb") as o:
            while True:
                b = r.read(1 << 22)
                if not b: break
                o.write(b)
    if _sha(p) != SHA256: raise RuntimeError(f"{p} does not match the pinned SHA-256 (file changed upstream or is corrupt)")
    return p


SEARCH_END = "2020-12-31"
SEARCH_FNAME = "finsaber_sp500_le2020.csv"      # 2000..2020 rows only: what search-side code may read


def _frames(d, start=None, end=None) -> dict:
    import pandas as pd
    if start: d = d[d.date >= start]
    if end: d = d[d.date <= end]
    f = (d["adjusted_close"] / d["close"]).where(d["close"] > 0)
    d = d.assign(High=d["high"] * f, Low=d["low"] * f, Close=d["adjusted_close"], Volume=d["volume"].astype(float))
    out = {}
    for s, g in d.groupby("symbol"):
        g = g.drop_duplicates("date", keep="last").set_index("date").sort_index()[["Close", "High", "Low", "Volume"]]
        g = g[g["Close"] > 0].dropna(subset=["Close"])
        if len(g): out[str(s).replace(".", "-")] = g
    return out


def search_path(cache_dir: Path) -> Path:
    """The search-safe copy (rows <= 2020-12-31). Created from the pinned original if missing; the original is the only file holding 2021+ rows."""
    import pandas as pd
    p = Path(cache_dir) / "external" / SEARCH_FNAME
    if not p.exists():
        d = pd.read_csv(finsaber_path(cache_dir), parse_dates=["date"])
        d[d.date <= SEARCH_END].to_csv(p, index=False)
    return p


def load_finsaber(cache_dir: Path, end: str = SEARCH_END) -> dict:
    """{yfinance-style ticker: DataFrame[Close, High, Low, Volume]} for the SEARCH window only (reads the <=2020 copy; `end` > 2020-12-31 is refused).
    Close = adjusted_close; High/Low are scaled by adjusted/raw close so the whole bar is on the adjusted basis. Volume as published."""
    import pandas as pd
    if str(end) > SEARCH_END: raise ValueError("search-side FINSABER loader is capped at 2020-12-31 (2021+ is sealed)")
    return _frames(pd.read_csv(search_path(cache_dir), parse_dates=["date"]), end=end)


def load_finsaber_full(cache_dir: Path, start: str, end: str = "2024-12-31") -> dict:
    """Sealed-holdout builder only (guard test forbids this name outside src/vault)."""
    import pandas as pd
    return _frames(pd.read_csv(finsaber_path(cache_dir), parse_dates=["date"]), start=start, end=end)
