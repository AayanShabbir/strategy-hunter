# c04_sol_rel_strength_v1 — engine run 20261023_174723_c04_sol_rel_strength_v1

Hypothesis: Holding SOL (or each alt) only while its 14- or 30-day return beats BTC's or ETH's over the same window AND is positive beats buy-and-hold OOS net of 35 bps/side (cross-sectional crypto momentum at 1-4 week horizons, Liu, Tsyvinski & Wu 2022 JF). 5x ATR stop. Strategy Scout crypto submission.

**0/8 pass.** Ledger N at evaluation: 490. PBO (CSCV) across family: 0.159. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 9bbe700d915562e6e2d5c5a7eec4d937a2c5ec5c3ebc106239f71d5b0f48eb30. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 483 | SOL|rel_strength(abs_filter=True,bench=BTC/USD,n=14) | -27.12/-0.3/-41.62 | 923.45 | 68 | 0.0165 | 0.85614 (106.2) | 1.0 | 0.0344 | 0.9135 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 484 | SOL|rel_strength(abs_filter=True,bench=BTC/USD,n=30) | 19.64/0.41/-26.52 | 923.45 | 47 | 0.0174 | 0.63337 (179.46) | 1.0 | 0.2096 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 485 | SOL|rel_strength(abs_filter=True,bench=ETH/USD,n=14) | -30.9/-0.39/-38.78 | 923.45 | 67 | 0.0159 | 0.90509 (167.45) | 1.0 | 0.028 | 0.916 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 486 | SOL|rel_strength(abs_filter=True,bench=ETH/USD,n=30) | 19.58/0.42/-33.83 | 923.45 | 40 | 0.0161 | 0.62537 (75.69) | 1.0 | 0.2108 | 0.885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 487 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=14) | -12.55/-0.07/-32.22 | 193.2 | 524 | 0.0197 | 0.86613 (47.01) | 1.0 | 0.0688 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 488 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=30) | 10.2/0.3/-30.23 | 193.2 | 365 | 0.0205 | 0.72228 (60.74) | 1.0 | 0.1719 | 0.899 | False | beats_buy_hold, holm, dsr, spa |
| 489 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=14) | -12.07/-0.15/-30.96 | 193.2 | 430 | 0.0186 | 0.88711 (45.61) | 1.0 | 0.0557 | 0.9055 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 490 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=30) | -7.13/-0.01/-39.19 | 193.2 | 284 | 0.0193 | 0.84715 (54.66) | 1.0 | 0.0807 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
