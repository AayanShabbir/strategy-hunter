"""Multi-source loader: merge rules, provenance, coverage arithmetic, no-network, key hygiene, old loaders untouched."""
import re
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from src.data import multisource as M
from src.data import alpaca_bars as AB

ROOT = Path(__file__).resolve().parents[1]
DAYS = pd.bdate_range("2010-01-04", "2012-12-31")


def frame(idx, scale=1.0, seed=0, vol=1e6):
    r = np.random.default_rng(seed).normal(0, 0.01, len(idx)); c = 50 * np.exp(np.cumsum(r)) * scale
    return pd.DataFrame({"Close": c, "High": c * 1.01, "Low": c * 0.99, "Volume": vol}, index=idx)


def win(rows):
    return pd.DataFrame([{"ticker": t, "yt": t, "start_date": pd.Timestamp(a), "end_date": pd.Timestamp(b) if b else pd.NaT} for t, a, b in rows])


def run(w, yf=None, al=None, fs=None, alt=None):
    return M.merge_sources(w, yf or {}, al or {}, "2010-01-01", "2012-12-31", "2010-01-01", "2012-12-31", alt=alt or {}, fs=fs or {})


def test_yfinance_only_needs_95pct_of_all_member_days_and_is_labelled():
    w = win([("AAA", "2000-01-01", None), ("BBB", "2000-01-01", None)])
    frames, prov, _ = run(w, yf={"AAA": frame(DAYS), "BBB": frame(DAYS[300:], seed=1)})
    assert "AAA" in frames and prov["AAA"]["sources_used"] == ["yfinance"] and prov["AAA"]["coverage_all"] == 1.0
    assert "BBB" not in frames and prov["BBB"]["status"] == "dropped"          # late-starting yfinance history = re-used ticker


def test_gap_filled_from_second_source_only_with_valid_overlap_and_rescaled():
    w = win([("AAA", "2000-01-01", None)])
    base = frame(DAYS, seed=2); tail = base.copy() * 1.0; tail[["Close", "High", "Low"]] *= 0.8      # other source on a 0.8x adjustment basis
    frames, prov, _ = run(w, yf={"AAA": base.iloc[300:]}, fs={"AAA": tail.iloc[:500]})
    assert prov["AAA"]["status"] == "kept" and prov["AAA"]["sources_used"] == ["yfinance", "finsaber"]
    f = frames["AAA"]; assert len(f) == len(DAYS) and np.allclose(f["Close"].values, base["Close"].values, rtol=1e-6)     # rescaled onto primary basis
    assert prov["AAA"]["qc"]["finsaber"]["accepted"] and prov["AAA"]["coverage_all"] == 1.0


def test_sources_that_disagree_are_never_spliced():
    w = win([("AAA", "2000-01-01", None)])
    late = frame(DAYS[300:], seed=3); other = frame(DAYS[:500], seed=99)          # same symbol, different company on the overlap
    frames, prov, _ = run(w, yf={"AAA": late}, fs={"AAA": other})
    q = prov["AAA"]["chain_qc"]["finsaber"]; assert q["accepted"] is False
    assert prov["AAA"]["sources_used"] in (["finsaber"], ["yfinance"]) and prov["AAA"]["status"] in ("kept", "dropped")
    if prov["AAA"]["status"] == "kept": assert len(frames["AAA"]) in (len(late), len(other))      # one source, never a mixture


def test_alt_ticker_used_only_when_validated_against_a_base_source():
    w = win([("OLD", "2000-01-01", None)]); new = frame(DAYS, seed=4)
    f1, p1, _ = run(w, yf={"NEW": new}, alt={"OLD": "NEW"})                         # nothing to validate against
    assert "OLD" not in f1 and p1["OLD"]["status"] == "dropped"
    a = new.iloc[500:] * 1.0; a[["Close", "High", "Low"]] *= 3.0                    # alpaca has OLD for the tail, on a different basis
    f2, p2, _ = run(w, yf={"NEW": new}, al={"OLD": a}, alt={"OLD": "NEW"})
    assert p2["OLD"]["status"] == "kept" and p2["OLD"]["sources_used"] == ["alpaca", "yfinance-alt:NEW"] and len(f2["OLD"]) == len(DAYS)


def test_range_coverage_rule_for_non_yfinance_series_and_headline_uses_all_member_days():
    w = win([("AAA", "2010-01-01", None), ("GONE", "2010-01-01", "2011-06-30")])
    frames, prov, dates = run(w, al={"AAA": frame(DAYS[200:], seed=5)}, fs={"GONE": frame(DAYS, seed=6)})
    assert prov["AAA"]["status"] == "kept" and prov["AAA"]["coverage_in_range"] == 1.0 and prov["AAA"]["coverage_all"] < 0.8   # honest vs all days
    cov = M.coverage_numbers(w, frames, prov, "2010-01-01", "2012-12-31", dates)
    assert cov["removed_names"] == 1 and cov["removed_names_priced"] == 1 and cov["member_days_priced"] == sum(p["priced_member_days"] for p in prov.values())
    assert 0 < cov["member_day_coverage"] < 1


def test_integrity_flags_reject_bad_single_source_series():
    w = win([("BAD", "2000-01-01", None)]); d = frame(DAYS, seed=7); d.iloc[100, 0] = d.iloc[99, 0] * 20       # a x20 one-day print
    frames, prov, _ = run(w, fs={"BAD": d})
    assert "BAD" not in frames and prov["BAD"]["finsaber_integrity"]["bad"]


def test_search_loader_refuses_the_sealed_years():
    M.assert_search_end("2020-12-31")
    with pytest.raises(ValueError): M.assert_search_end("2021-01-01")


def test_alpaca_fetch_uses_headers_only_and_never_leaks_keys(monkeypatch):
    monkeypatch.setenv("ALPACA_API_KEY", "KEY-SENTINEL-123"); monkeypatch.setenv("ALPACA_SECRET_KEY", "SECRET-SENTINEL-456")
    seen = {}

    class R:
        def __init__(s, code, j): s.status_code, s._j, s.text = code, j, "boom"
        def json(s): return s._j

    class S:
        def get(s, url, headers=None, params=None, timeout=None):
            seen.update(url=url, headers=headers, params=params)
            if params["symbols"].startswith("ZZ"): return R(403, {})
            return R(200, {"bars": {"BRK.B": [{"t": "2016-01-04T05:00:00Z", "o": 1, "h": 3, "l": 1, "c": 2, "v": 10}]}, "next_page_token": None})

    out = AB.fetch_bars(["BRK-B"], "2016-01-01", "2016-01-31", session=S(), sleep=0)
    assert list(out) == ["BRK-B"] and float(out["BRK-B"]["Close"].iloc[0]) == 2.0 and str(out["BRK-B"].index[0].date()) == "2016-01-04"
    assert seen["url"].startswith("https://data.alpaca.markets/") and "KEY-SENTINEL-123" not in repr(seen["params"])
    with pytest.raises(RuntimeError) as e: AB.fetch_bars(["ZZZ"], "2016-01-01", "2016-01-31", session=S(), sleep=0)
    assert "SENTINEL" not in str(e.value)
    src = (ROOT / "src/data/alpaca_bars.py").read_text()
    assert "/v2/orders" not in src and "paper-api" not in src and "positions" not in src                 # data endpoint only


def test_old_loaders_do_not_depend_on_the_new_modules():
    for f in ("loader.py", "sp500_pit.py"):
        t = (ROOT / "src/data" / f).read_text()
        assert "multisource" not in t and "alpaca_bars" not in t and "external" not in t
