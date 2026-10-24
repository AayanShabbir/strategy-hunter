"""Search-data panel for the swarm: the SDE's S&P 500 loader, cut to the SEARCH window only.

Search window = SDE train 2010-2016 + validation 2017. Rows after 2017-12-31 (the SDE test years, 2018-2020) are dropped
inside `build_search_panel` before anything is cached or returned, so workers, the auditor, the trader and every LLM prompt
never see them. The engine's sealed vault is a different system and is never read here.
Survivorship: the loader uses today's constituents (same flag as the SDE S&P run), so results are optimistic; this is recorded in
`meta` and printed in reports.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

import numpy as np

from . import DATA_DIR

SEARCH_START = "2010-01-01"
TRAIN_END = "2016-12-31"
SEARCH_END = "2017-12-31"
WARMUP_START = "2009-01-01"


@dataclass
class SearchPanel:
    dates: np.ndarray            # datetime64[D]
    assets: list
    data: dict                   # '$close' etc -> (D, N)
    member: np.ndarray           # (D, N) bool
    start_idx: int               # first row of the search window (SEARCH_START)
    train_end_idx: int           # exclusive end of train inside the panel
    meta: dict

    @property
    def n_days(self) -> int:
        return len(self.dates)

    def calendar(self) -> list[str]:
        """ISO dates of the return vector (rows start_idx .. D-2: the last row has no next-day return)."""
        return [str(d) for d in self.dates[self.start_idx:len(self.dates) - 1]]


def _from_sde(end: str = SEARCH_END):
    from src.data.loader import load_sp500
    p = load_sp500(end="2020-12-31")                 # cached pickle; test years are truncated immediately below
    b = int(np.searchsorted(p.dates, np.datetime64(end), "right"))
    return (p.dates[:b], list(p.assets), {k: v[:b] for k, v in p.data.items()}, p.member[:b], dict(p.meta))


def build_search_panel(cache_path: str | None = None, rebuild: bool = False) -> SearchPanel:
    cache_path = cache_path or os.path.join(DATA_DIR, "cache", "sp500_search_panel.npz")
    if os.path.exists(cache_path) and not rebuild:
        z = np.load(cache_path, allow_pickle=False)
        dates, assets, meta = z["dates"].astype("datetime64[D]"), [str(a) for a in z["assets"]], json.loads(str(z["meta"]))
        data = {k: z[k] for k in ("$close", "$high", "$low", "$volume")}
        member = z["member"]
    else:
        dates, assets, data, member, meta = _from_sde()
        meta.update(window=f"{SEARCH_START}..{SEARCH_END}", note="search data only; SDE test years 2018-2020 excluded")
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        np.savez(cache_path + ".tmp.npz", dates=dates.astype("datetime64[D]"), assets=np.array(assets), member=member,
                 meta=json.dumps(meta), **data)
        os.replace(cache_path + ".tmp.npz", cache_path)
    assert dates[-1] <= np.datetime64(SEARCH_END), "panel leaks beyond the search window"
    s = int(np.searchsorted(dates, np.datetime64(SEARCH_START), "left"))
    te = int(np.searchsorted(dates, np.datetime64(TRAIN_END), "right"))
    return SearchPanel(dates, assets, data, member, s, te, meta)


def synthetic_panel(n_days: int = 700, n_assets: int = 60, seed: int = 0, drift_signal: float = 0.0) -> SearchPanel:
    """Small deterministic panel for tests/smoke. `drift_signal`>0 plants a cross-sectional edge in `$volume` (high volume -> higher return)."""
    rng = np.random.default_rng(seed)
    dates = np.arange(np.datetime64("2012-01-02"), np.datetime64("2012-01-02") + int(n_days * 1.5))
    dates = dates[np.is_busday(dates)][:n_days]
    vol = np.exp(rng.normal(0, 1, (1, n_assets)) + rng.normal(0, 0.05, (n_days, n_assets)))
    r = rng.normal(0.0003, 0.012, (n_days, n_assets)) + drift_signal * (np.log(vol) - np.log(vol).mean(1, keepdims=True))
    close = 100 * np.exp(np.cumsum(r, 0))
    data = {"$close": close, "$high": close * (1 + np.abs(rng.normal(0, 0.005, close.shape))),
            "$low": close * (1 - np.abs(rng.normal(0, 0.005, close.shape))), "$volume": vol * 1e6}
    start = 80
    te = int(n_days * 0.8)
    return SearchPanel(dates, [f"S{i}" for i in range(n_assets)], data, np.ones_like(close, bool), start, te, {"source": "synthetic"})
