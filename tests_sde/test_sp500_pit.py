"""Survivorship-reduced S&P 500 universe: pure-function tests (no network, no market data)."""
import numpy as np, pandas as pd
from src.data.sp500_pit import membership_mask, coverage_keep


def _win(rows):
    d = pd.DataFrame(rows, columns=["yt", "start_date", "end_date"])
    d["start_date"] = pd.to_datetime(d["start_date"]); d["end_date"] = pd.to_datetime(d["end_date"]); return d


def test_membership_windows_end_exclusive_open_end_and_rejoin():
    dates = pd.bdate_range("2010-01-01", "2010-12-31")
    win = _win([("AAA", "2009-01-01", "2010-03-01"),      # leaves 2010-03-01 (exclusive)
                ("BBB", "2010-06-01", None),              # joins mid-year, still a member
                ("CCC", "2008-01-01", "2010-02-01"), ("CCC", "2010-09-01", None)])   # leaves and re-joins
    m = membership_mask(dates, ["AAA", "BBB", "CCC", "ZZZ"], win, "2010-01-01", "2010-12-31")
    d = pd.DatetimeIndex(dates)
    assert m[d == "2010-02-26", 0].all() and not m[d == "2010-03-01", 0].any()
    assert not m[d == "2010-05-31", 1].any() and m[d == "2010-06-01", 1].all() and m[d == "2010-12-31", 1].all()
    assert m[d == "2010-01-15", 2].all() and not m[d == "2010-05-03", 2].any() and m[d == "2010-10-01", 2].all()
    assert not m[:, 3].any()                              # asset without a window is never a member


def test_membership_is_clipped_to_evaluation_window():
    dates = pd.bdate_range("2009-06-01", "2011-06-01")
    m = membership_mask(dates, ["AAA"], _win([("AAA", "2000-01-01", None)]), "2010-01-01", "2010-12-31")
    d = pd.DatetimeIndex(dates)
    assert not m[d < "2010-01-01", 0].any() and not m[d > "2010-12-31", 0].any() and m[d == "2010-06-01", 0].all()


def test_coverage_guard_drops_reused_or_patchy_tickers():
    D = 200; pit = np.zeros((D, 3), bool); pit[:, :] = True
    px = np.ones((D, 3), bool)
    px[:150, 1] = False            # ticker re-used: this company's prices only exist for the last 25 % of the window
    px[::25, 2] = False            # 4 % gaps: still kept (>= 95 % covered)
    keep = coverage_keep(pit, px)
    assert keep.tolist() == [True, False, True]
    assert coverage_keep(np.zeros((D, 1), bool), np.zeros((D, 1), bool)).tolist() == [True]   # never a member: irrelevant
