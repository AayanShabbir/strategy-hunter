# Hunt #12 — original strategies (h12_original), 2026-10-22. RESEARCH ONLY, no orders/bets.
Prereg: prereg.yaml (written before results). Code: run.py. Numbers: results.json. Tearsheet: tearsheet_best_OOS.html (E4 vs SPY, OOS).
Data: Alpaca IEX daily (ALL_1d.pkl, 2020-07..2026-10-14); IS 2020-08-25..2024-12-06, OOS 2024-12-09..2026-10-14. 5 bps/side. NFL: nflverse games.csv, -110.
Ledger N fix: HUNT_LEDGER said 307 but omitted h11_candle_setups (+12, in research_lab/ledger). True prior N = 319; Holm at N = 324.
Method notes: returns computed with an explicit open/close trade engine (not vectorbt); CPCV/PBO/DSR not run (Holm and SPA already fail by a wide margin). Universe survivor-biased.

| Strategy | Thesis | OOS ret% / Sharpe / MaxDD | IS ret% / Sh | p (vs SPY / mean>0) | Holm@324 | SPA p vs SPY / 70-30 | Pass |
|---|---|---|---|---|---|---|---|
| E1 month-end rebalance flow | balanced funds buy the MTD laggard (SPY vs TLT gap >=3%) last 3 days | 3.81 / 0.78 / -2.88 (30 days in) | 10.92 / 0.57 | 0.84 / 0.145 | 1.0 | 0.88 / 0.85 | FAIL |
| E2 LETF close reversal | QQQ ±2% day -> fade next open->close | 2.29 / 0.22 / -7.06 | -3.74 / -0.06 | 0.85 / 0.385 | 1.0 | 0.87 / 0.84 | FAIL |
| E3 credit-calm equity panic | SPY 10d <= -3% while HYG 10d >= -0.5% -> long SPY 5d | 1.84 / 0.23 / -7.12 | 1.97 / 0.14 | 0.87 / 0.378 | 1.0 | 0.92 / 0.91 | FAIL |
| E4 defensive-lead guard | hold SPY unless XLK-XLU 20d < -5% | 17.16 / 0.80 / -13.68 | 42.10 / 0.64 | 0.72 / 0.138 | 1.0 | 0.91 / 0.59 | FAIL |
| SPY | benchmark | 26.76 / 0.87 / -18.98 | 77.24 / 0.89 | | | | |
| 70% SPY + 30% cash | benchmark | 18.66 / 0.87 / -13.60 | 51.15 / 0.89 | | | | |

NFL N1 wind 10–14 mph under (games disjoint from S3 wind>=15; fresh, not a re-use of S3's OOS):
IS 1999–2018: 930 bets, 51.86% win, ROI -0.99%. OOS 2019–2026: 294 bets, 59.93% win, ROI +14.32%, binomial p 0.0056, Holm@324 = 1.0. FAIL (IS negative; Holm). Read: wind-unders look strong only since 2019 in both bands; 20 years before that they did not work in 10–14 mph. Could be a regime change (books/totals) or luck; unverified.

Prediction markets (Kalshi + Polymarket public read APIs work, no keys):
- P1 Polymarket-vs-Kalshi gap: snapshot 2026-10-22 ~15:05 ET, Oct-2026 FOMC: "hold" Kalshi 93/94c vs Polymarket 94/95c; "hike 25" 5/6c on both. Gap <= 1c, below fees. No matched historical book data on the box -> 0 trials, not testable.
- P2 Fed odds -> stocks: needs per-market candle history; short history; 0 trials.
Snapshots: kalshi_events.json, kalshi_feddecision.json, kalshi_26oct.json, poly_markets.json.
Not used: Finnhub/FMP keys exist in env but no strategy needed them this hunt.

Verdict: 0/5 pass. SPY core stays the engine.
Best idea to paper-watch (NOT verified): NFL wind-under family (>=10 mph outdoors) as a zero-stakes paper log for the rest of 2026–27; it is the only signal with a decent OOS p, but IS failure means it is promising at best. Best stock idea: E4 guard (cut DD by ~5 pts vs SPY but trailed SPY and only matched 70/30) — market-ride, not an edge.
