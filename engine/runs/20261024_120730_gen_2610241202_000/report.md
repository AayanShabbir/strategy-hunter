# gen_2610241202_000 — engine run 20261024_120730_gen_2610241202_000

Hypothesis: grammar draw seed=2610241202: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 2498. PBO (CSCV) across family: 0.352. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 eed6e9b5d58f63c3c01bfda9050e536cfcf4f33d0497ed410e75d6f48e2d0a75. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2491 | sectors|rsi_revert(entry=5,exit=60,n=3)+relvol(min_ratio=1.0) | -2.15/-0.36/-4.16 | 94.31 | 66 | 0.0513 | 0.997 (40.05) | 1.0 | 0.0004 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2492 | sectors|rsi_revert(entry=5,exit=60,n=5)+relvol(min_ratio=1.0) | 0.52/0.43/-0.27 | 94.31 | 18 | 0.0474 | 0.98601 (42.51) | 1.0 | 0.0122 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2493 | sectors|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.0) | -2.56/-0.42/-4.16 | 94.31 | 82 | 0.0513 | 1.0 (41.45) | 1.0 | 0.0002 | 0.4995 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2494 | sectors|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.0) | 0.63/0.4/-0.57 | 94.31 | 22 | 0.0499 | 0.95305 (42.85) | 1.0 | 0.0166 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2495 | sectors|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.0) | 11.91/0.53/-6.68 | 94.31 | 177 | 0.0609 | 0.98901 (37.03) | 1.0 | 0.014 | 0.506 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2496 | sectors|rsi_revert(entry=10,exit=60,n=5)+relvol(min_ratio=1.0) | -2.15/-0.38/-3.71 | 94.31 | 61 | 0.0452 | 0.997 (39.64) | 1.0 | 0.0003 | 0.4955 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2497 | sectors|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.0) | 11.58/0.5/-6.68 | 94.31 | 217 | 0.0603 | 0.97902 (37.21) | 1.0 | 0.0154 | 0.5045 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2498 | sectors|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.0) | -1.55/-0.26/-3.71 | 94.31 | 90 | 0.0477 | 0.99201 (40.49) | 1.0 | 0.0008 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
