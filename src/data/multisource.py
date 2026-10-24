"""Multi-source point-in-time S&P 500 loader (Task A: reduce survivorship bias; an ADDITION, `load_sp500` / `load_sp500_pit` are untouched).

Sources merged per ticker, with provenance:
  yfinance            primary (what the old loaders use; auto-adjusted)
  yfinance-alt        Yahoo history of the SAME company under its new ticker (curated ALT_TICKERS, e.g. FB -> META); used only when it
                      agrees with another source on an overlap (so a wrong mapping is rejected, not trusted)
  alpaca              Alpaca SIP daily bars (2016-01-04 onward, includes since-delisted symbols); see alpaca_bars.py
A lower-priority source may fill dates a higher-priority one lacks ONLY if the two overlap on >= MIN_OVERLAP days with a tight
log-price ratio (median |log ratio| <= TOL and MAD <= TOL); it is then rescaled to the higher-priority series by the overlap median so
adjustment-basis differences do not create a jump. Without a valid overlap sources are never mixed (a re-used ticker would otherwise
splice two different companies); instead the best single-source candidate is taken.
Keep rule: a series that is yfinance-only must price >= 95 % of ALL membership days (the old rule, so the old universe is kept);
a series involving Alpaca/alt must price >= 95 % of the membership days INSIDE its own date range (it cannot see before 2016).
Coverage (the honest number) is always measured against ALL point-in-time membership days.
`load_sp500_merged` is the SEARCH-side entry point and refuses any end date after 2020-12-31 (the sealed holdout starts 2021-01-01).
"""
from __future__ import annotations
import numpy as np
from src.data.loader import Panel, _panel_from_frames
from src.data import sp500_pit as P

MIN_COVER = 0.95
MIN_OVERLAP = 20
TOL = 0.01
MIN_CORR = 0.98
SEARCH_END = "2020-12-31"
COLS = ("Close", "High", "Low", "Volume")

# Same company, new Yahoo ticker. Only trusted after an overlap check against another source (Alpaca has the old symbol 2016+).
ALT_TICKERS = {
    "FB": "META", "ANTM": "ELV", "WLTW": "WTW", "JEC": "J", "HCP": "DOC", "SYMC": "GEN", "UTX": "RTX", "ARNC": "HWM", "BHGE": "BKR",
    "ADS": "BFH", "TMK": "GL", "ABC": "COR", "PKI": "RVTY", "HRS": "LHX", "HFC": "DINO", "FBHS": "FBIN", "CTL": "LUMN", "LB": "BBWI",
    "KORS": "CPRI", "GPS": "GAP", "RE": "EG", "MYL": "VTRS", "FLT": "CPAY", "FI": "FISV", "COG": "CTRA", "PEAK": "DOC",
}


def _overlap_ok(a, b):
    """(ok, scale, info): a, b Close series. scale multiplies b onto a's price basis."""
    j = a.index.intersection(b.index)
    j = j[np.isfinite(a.reindex(j).values) & np.isfinite(b.reindex(j).values)]
    if len(j) < MIN_OVERLAP: return False, 1.0, {"overlap_days": int(len(j)), "reason": "overlap<%d" % MIN_OVERLAP}
    r = np.log(a.reindex(j).values / b.reindex(j).values); med = float(np.median(r)); mad = float(np.median(np.abs(r - med)))
    ra, rb = np.diff(np.log(a.reindex(j).values)), np.diff(np.log(b.reindex(j).values))
    corr = float(np.corrcoef(ra, rb)[0, 1]) if len(ra) > 3 and ra.std() > 0 and rb.std() > 0 else 0.0
    ok = mad <= TOL and corr >= MIN_CORR    # a constant offset (spin-off / merger adjustment basis) is fine; a different company is not
    return bool(ok), float(np.exp(med)), {"overlap_days": int(len(j)), "median_log_ratio": round(med, 5), "mad": round(mad, 5), "ret_corr": round(corr, 4)}


def _chain(parts):
    """parts: [(label, df)] by priority. Returns (composite df or None, used labels, qc dict)."""
    import pandas as pd
    comp = None; used = []; qc = {}
    for lab, df in parts:
        if df is None or not len(df): continue
        if comp is None:
            if lab.startswith("yfinance-alt"): qc[lab] = {"accepted": False, "reason": "alt ticker needs a base source to validate against"}; continue
            comp = df.copy(); used.append(lab); continue
        ok, sc, info = _overlap_ok(comp["Close"], df["Close"]); qc[lab] = info
        if not ok: qc[lab]["accepted"] = False; continue
        add = df.loc[~df.index.isin(comp.index)].copy()
        for c in ("Close", "High", "Low"): add[c] = add[c] * sc
        qc[lab]["accepted"] = True; qc[lab]["scale"] = round(sc, 5)
        if len(add): comp = pd.concat([comp, add]).sort_index(); used.append(lab)
    return comp, used, qc


def integrity_flags(df, max_abs_log_ret: float = 1.2) -> dict:
    """Cheap sanity checks for a single-source series: one-day moves that are not credible after adjustment, stale prices, bad bars."""
    c = df["Close"].to_numpy(float); r = np.diff(np.log(c)) if len(c) > 1 else np.zeros(0)
    jumps = int((np.abs(r) > max_abs_log_ret).sum()); stale = float((r == 0).mean()) if len(r) else 0.0
    badbar = int(((df["High"] < df["Low"] * 0.999) | (df["Close"] <= 0)).sum())
    return {"jumps_gt_%.1f" % max_abs_log_ret: jumps, "stale_frac": round(stale, 4), "bad_bars": badbar, "bad": bool(jumps > 0 or stale > 0.5 or badbar > 5)}


def _member_days(win_t, dates, w0, w1):
    import pandas as pd
    m = np.zeros(len(dates), bool); inwin = (dates >= w0) & (dates <= w1)
    for r in win_t.itertuples():
        x = (dates >= r.start_date) & inwin
        if not pd.isna(r.end_date): x &= dates < r.end_date
        m |= x
    return m


def merge_sources(win, yf: dict, al: dict, w0: str, w1: str, start: str, end: str, alt: dict = ALT_TICKERS, min_cover: float = MIN_COVER, fs: dict | None = None):
    """-> (frames {ticker: df} for kept names, provenance {ticker: {...}}, dates). Pure function of its inputs (no network)."""
    import pandas as pd
    pitwin = win[(win.start_date <= w1) & (win.end_date.isna() | (win.end_date >= w0))]
    names = sorted(set(pitwin.yt))
    cut = lambda d: None if d is None else d.loc[(d.index >= start) & (d.index <= end)]
    alld = set()
    fs = fs or {}
    for f in list(yf.values()) + list(al.values()) + list(fs.values()): alld |= set(f.index[(f.index >= start) & (f.index <= end)])
    dates = pd.DatetimeIndex(sorted(alld))
    frames, prov = {}, {}
    for t in names:
        wt = pitwin[pitwin.yt == t]; m = _member_days(wt, dates, w0, w1); nm = int(m.sum())
        y, a_, f_, alt_y = cut(yf.get(t)), cut(al.get(t)), cut(fs.get(t)), (cut(yf.get(alt[t])) if t in alt else None)
        cands = {}; fin_flags = None
        if f_ is not None and len(f_):
            fin_flags = integrity_flags(f_)
            if fin_flags["bad"]: f_ = None
        full, used, qc = _chain([("yfinance", y), ("alpaca", a_), ("finsaber", f_), ("yfinance-alt:" + alt.get(t, ""), alt_y)])
        chain_qc = qc
        if full is not None: cands["merged:" + "+".join(used)] = (full, used, qc)
        if a_ is not None and len(a_): cands["alpaca"] = (a_, ["alpaca"], {})
        if y is not None and len(y): cands["yfinance"] = (y, ["yfinance"], {})
        if f_ is not None and len(f_): cands["finsaber"] = (f_, ["finsaber"], {"integrity": fin_flags})
        best = None
        for name, (df, used, qc) in cands.items():
            px = np.asarray(dates.isin(df.index[np.isfinite(df["Close"])]))
            priced = int((m & px).sum()); lo, hi = df.index[0], df.index[-1]
            rng = m & (dates >= lo) & (dates <= hi); nr = int(rng.sum())
            yf_only = used == ["yfinance"]
            ok = nm > 0 and ((priced >= min_cover * nm) if yf_only else (nr > 0 and priced >= min_cover * nr))
            if ok and (best is None or priced > best[0]): best = (priced, name, df, used, qc, nr)
        rec = {"member_days": nm, "pit_windows": [[str(r.start_date)[:10], "" if pd.isna(r.end_date) else str(r.end_date)[:10]] for r in wt.itertuples()],
               "candidates": sorted(cands), "available": {"yfinance": bool(y is not None and len(y)), "alpaca": bool(a_ is not None and len(a_)),
                                                         "yfinance-alt": bool(alt_y is not None and len(alt_y)),
                                                         "finsaber": bool(f_ is not None and len(f_))}, "chain_qc": chain_qc}
        if fin_flags is not None: rec["finsaber_integrity"] = fin_flags
        if best is None:
            rec.update(status="dropped", reason="no-member-days-in-window" if nm == 0 else ("no price source" if not cands else "coverage<95%"))
        else:
            priced, name, df, used, qc, nr = best
            rec.update(status="kept", source=name, sources_used=used, priced_member_days=priced, coverage_all=round(priced / max(nm, 1), 4),
                       coverage_in_range=round(priced / max(nr, 1), 4), first=str(df.index[0])[:10], last=str(df.index[-1])[:10], qc=qc)
            frames[t] = df[list(COLS)]
        prov[t] = rec
    return frames, prov, dates


def coverage_numbers(win, frames, prov, w0, w1, dates):
    """Headline numbers on the SAME definition as the baseline (member-days priced / all point-in-time member-days)."""
    import pandas as pd
    pitwin = win[(win.start_date <= w1) & (win.end_date.isna() | (win.end_date >= w0))]
    tot = sum(rec["member_days"] for rec in prov.values())
    got = sum(rec.get("priced_member_days", 0) for rec in prov.values())
    removed = set(win[win.end_date.notna() & (win.end_date >= w0) & (win.end_date <= w1) & (win.start_date <= w1)].yt)
    # a name is "removed" if it left in the window; priced = kept with at least one priced member day
    rem_priced = {t for t in removed if prov.get(t, {}).get("priced_member_days", 0) > 0}
    rem_md = sum(prov[t]["member_days"] for t in removed if t in prov); rem_got = sum(prov[t].get("priced_member_days", 0) for t in removed if t in prov)
    by_src = {}
    for rec in prov.values():
        if rec["status"] == "kept": by_src[rec["source"]] = by_src.get(rec["source"], 0) + 1
    return {"pit_names": len(prov), "pit_names_priced": sum(1 for r in prov.values() if r["status"] == "kept"),
            "member_days_total": int(tot), "member_days_priced": int(got), "member_day_coverage": round(got / max(tot, 1), 4),
            "removed_names": len(removed), "removed_names_priced": len(rem_priced), "removed_name_coverage": round(len(rem_priced) / max(len(removed), 1), 4),
            "removed_member_day_coverage": round(rem_got / max(rem_md, 1), 4), "kept_by_source": by_src}


def panel_from_merge(frames, prov, win, w0, w1, meta_extra: dict) -> Panel:
    import pandas as pd
    pan = _panel_from_frames(frames, {"close": "Close", "high": "High", "low": "Low", "volume": "Volume"}, {})
    dates = pd.DatetimeIndex(pan.dates)
    pit = P.membership_mask(dates, pan.assets, win, w0, w1)
    pan.member = pit & np.isfinite(pan.data["$close"])
    pan.meta = {"source": "yfinance + yfinance-alt + alpaca (SIP) merged per ticker, fja05680/sp500 PIT windows (MIT)", "universe": "sp500_merged",
                "survivorship": "REDUCED, NOT ELIMINATED (see docs/data_quality_sp500.md)", **meta_extra}
    return pan


def _yf_frames(tickers, start, end):
    import yfinance as yf, pandas as pd
    out = {}
    tickers = sorted(set(tickers))
    for i in range(0, len(tickers), 30):
        b = tickers[i:i + 30]
        raw = yf.download(b, start=start, end=str(np.datetime64(end) + 1), auto_adjust=True, progress=False, threads=False)
        if raw is None or raw.empty: continue
        for t in b:
            if t in raw["Close"] and raw["Close"][t].notna().any():
                out[t] = pd.DataFrame({k: raw[k][t] for k in COLS}).dropna(subset=["Close"])
    return out


def gather_search_sources(cache: bool = True):
    """(win, yf, al, fs) for the SEARCH window (2009-01-01 .. 2020-12-31): raw per-source frames, before any merging."""
    import pickle, pandas as pd
    from src.data.loader import load_sp500
    from src.data.alpaca_bars import fetch_cached
    from src.data.external import load_finsaber
    win = P.membership_windows(); start, end, w0, w1 = P.START, SEARCH_END, P.W0, P.W1
    pitwin = win[(win.start_date <= w1) & (win.end_date.isna() | (win.end_date >= w0))]
    names = sorted(set(pitwin.yt)); alts = sorted({v for k, v in ALT_TICKERS.items() if k in names})
    # old yfinance material first (bit-identical to what load_sp500_pit used), then fill what it lacks
    base = load_sp500(end=end, cache=cache); yf = {}
    for j, a in enumerate(base.assets):
        yf[a] = pd.DataFrame({k: base.data[k2][:, j] for k, k2 in zip(COLS, ("$close", "$high", "$low", "$volume"))},
                             index=pd.DatetimeIndex(base.dates)).dropna(subset=["Close"])
    need = sorted(set(names) - set(yf))
    if need:
        raw = P._download(need, cache)
        for t in need:
            if t in raw["Close"] and raw["Close"][t].notna().any():
                yf[t] = pd.DataFrame({k: raw[k][t] for k in COLS}).dropna(subset=["Close"])
    more = sorted(set(alts) - set(yf))
    if more:
        cp = P.CACHE / f"merged_yf_alt_{start}_{end}_{len(more)}.pkl"
        if cache and cp.exists(): yf.update(pickle.load(open(cp, "rb")))
        else:
            d = _yf_frames(more, start, end); yf.update(d)
            if cache: cp.parent.mkdir(parents=True, exist_ok=True); pickle.dump(d, open(cp, "wb"))
    al = fetch_cached(names, "2016-01-01", end, P.CACHE, tag="merged_alpaca")
    return win, yf, al, load_finsaber(P.CACHE, end=end)


def assert_search_end(end: str) -> None:
    if str(end) > SEARCH_END: raise ValueError(f"search-side loaders cannot reach past {SEARCH_END} (the 2021+ holdout is sealed): got {end}")


def load_sp500_merged(cache: bool = True):
    """SEARCH-window merged panel (2009-01-01 .. 2020-12-31). -> (Panel, provenance, coverage). Never reads or fetches 2021+ data."""
    assert_search_end(SEARCH_END)
    win, yf, al, fs = gather_search_sources(cache)
    w0, w1 = P.W0, P.W1
    frames, prov, dates = merge_sources(win, yf, al, w0, w1, P.START, SEARCH_END, fs=fs)
    cov = coverage_numbers(win, frames, prov, w0, w1, dates)
    return panel_from_merge(frames, prov, win, w0, w1, {"coverage": cov}), prov, cov


def pair_agreement(a: dict, b: dict, lo: str, hi: str, min_days: int = MIN_OVERLAP) -> list[dict]:
    """Per-ticker agreement of two sources on their overlap in [lo, hi]: constant-offset (median log ratio), dispersion (MAD of the log
    ratio), daily-return correlation and median volume ratio. Used for the data-quality report and as the evidence for / against trusting
    a source (e.g. a single-source series is only as good as the source's agreement where it can be checked)."""
    rows = []
    for t in sorted(set(a) & set(b)):
        x, y = a[t], b[t]
        j = x.index.intersection(y.index); j = j[(j >= lo) & (j <= hi)]
        if len(j) < min_days: continue
        xc, yc = x["Close"].reindex(j).to_numpy(float), y["Close"].reindex(j).to_numpy(float)
        ok = np.isfinite(xc) & np.isfinite(yc) & (xc > 0) & (yc > 0)
        if ok.sum() < min_days: continue
        lr = np.log(xc[ok] / yc[ok]); med = float(np.median(lr)); mad = float(np.median(np.abs(lr - med)))
        rx, ry = np.diff(np.log(xc[ok])), np.diff(np.log(yc[ok]))
        corr = float(np.corrcoef(rx, ry)[0, 1]) if len(rx) > 3 and rx.std() > 0 and ry.std() > 0 else float("nan")
        vx, vy = x["Volume"].reindex(j).to_numpy(float)[ok], y["Volume"].reindex(j).to_numpy(float)[ok]
        vv = (vx > 0) & (vy > 0)
        rows.append({"ticker": t, "n": int(ok.sum()), "median_log_ratio": med, "mad": mad, "ret_corr": corr,
                     "vol_log_ratio": float(np.median(np.log(vx[vv] / vy[vv]))) if vv.any() else float("nan")})
    return rows
