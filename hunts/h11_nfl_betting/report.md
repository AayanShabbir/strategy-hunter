# Hunt #11: NFL betting strategies vs the -110 vig (research only)
Date 2026-10-22. Rules pre-registered in prereg.yaml before results. No bets, no accounts, no paid data.

**Verdict: 0 of 9 beat the vig out-of-sample. None pass.** Cumulative N = 307 (298 + 9).

Data: nflverse/nfldata games.csv (credit nflverse / Lee Sharpe; repo has no LICENSE file, so the license is unverified; private research use). Seasons 1999-2026, completed games. IS 1999-2018, OOS 2019-2026 (2026 partial). Whether spread_line/total_line are true closing lines is unverified. College skipped: no free, keyless closing-line source (CollegeFootballData needs an API key).
Pricing: flat -110 (break-even 52.38%). Pushes refunded. 10k bootstrap CI. Holm at N=307.

| # | Name | IS bets/win%/ROI% | OOS bets (push) | OOS win% | OOS ROI% | OOS 95% CI ROI | binom p vs 52.38% | Holm@307 | pass |
|---|---|---|---|---|---|---|---|---|---|
| 299 | S1_home_dog | 1742/50.03/-4.35 | 809 (18) | 51.33 | -1.97 | (-8.47, 4.56) | 0.735 | 1.00 | False |
| 300 | S2_div_home_dog | 714/48.69/-6.79 | 289 (4) | 51.93 | -0.85 | (-11.76, 10.07) | 0.584 | 1.00 | False |
| 301 | S3_wind_under | 540/57.52/9.66 | 144 (2) | 54.93 | 4.8 | (-10.48, 20.08) | 0.300 | 1.00 | False |
| 302 | S4_cold_under | 296/46.74/-10.6 | 88 (2) | 47.67 | -8.78 | (-28.31, 10.85) | 0.837 | 1.00 | False |
| 303 | S5_rest_edge | 616/51.58/-1.49 | 184 (3) | 46.41 | -11.22 | (-24.75, 2.22) | 0.954 | 1.00 | False |
| 304 | S6_short_week_fade | 0/0.0/nan | 0 (0) | 0.0 | False | (nan, nan) | 1.000 | 1.00 | False |
| 305 | S7_west_early_east | 197/52.36/-0.05 | 100 (1) | 42.42 | -18.82 | (-37.0, -0.64) | 0.981 | 1.00 | False |
| 306 | S8_elo_vs_line | 1528/52.66/0.52 | 723 (17) | 51.27 | -2.06 | (-9.05, 4.75) | 0.734 | 1.00 | False |
| 307 | S9_big_dog | 651/52.91/0.99 | 257 (9) | 50.0 | -4.39 | (-15.88, 7.18) | 0.792 | 1.00 | False |

Notes
- S3 wind unders (wind >= 15 mph, outdoors) was the only IS winner (57.5%, +9.7%, p=0.010), but OOS fell to 54.9% / +4.8% on 144 bets, p=0.30, CI (-10.5, +20.1). It's a known, published angle that the market has likely priced in. Promising at best, not verified.
- S6 short-week fade produced 0 bets as written: Thursday games give both teams short rest, so "opponent rest >= 7" never happens. Counted as a trial and not re-tuned.
- Elo vs line (S8): 52.7% IS -> 51.3% OOS. The closing line beats a simple Elo.
- Untestable with free data: closing-line value (needs our own bet price vs the close), line moves (no open lines), public fade (no free public-betting %). Travel was tested only as the Pacific-team-in-an-early-Eastern-game rule (S7); there were no coordinates for a full distance test.
Files: prereg.yaml, run.py, results.csv, data/games.csv (+ sha256).
