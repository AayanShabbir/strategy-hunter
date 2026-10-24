# gen_2610241113_000 — engine run 20261024_110605_gen_2610241113_000

Hypothesis: grammar draw seed=2610241113: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2458. PBO (CSCV) across family: 0.443. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 1dfe82ea1f353e8120560ade6aebc691edfc718501bdab5f491e0d0ce751cf2f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2451 | index|rsi_revert(entry=5,exit=60,n=2) | 17.75/0.72/-3.68 | 107.42 | 110 | 0.0727 | 0.97303 (43.72) | 1.0 | 0.3409 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2452 | index|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 107.42 | 3 | 0.0558 | 1.0 (37.07) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2453 | index|rsi_revert(entry=5,exit=80,n=2) | 25.62/0.82/-9.68 | 107.42 | 103 | 0.0729 | 0.88511 (42.51) | 1.0 | 0.441 | 0.4855 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2454 | index|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 107.42 | 2 | 0.0723 | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2455 | index|rsi_revert(entry=20,exit=60,n=2) | 52.86/1.29/-11.7 | 107.42 | 361 | 0.0737 | 0.14585 (35.79) | 1.0 | 0.7857 | 0.9295 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2456 | index|rsi_revert(entry=20,exit=60,n=5) | 35.77/1.13/-7.7 | 107.42 | 74 | 0.0695 | 0.68132 (43.54) | 1.0 | 0.7011 | 0.9715 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2457 | index|rsi_revert(entry=20,exit=80,n=2) | 65.08/1.33/-14.87 | 107.42 | 289 | 0.0788 | 0.03696 (38.33) | 1.0 | 0.7856 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2458 | index|rsi_revert(entry=20,exit=80,n=5) | 38.9/0.88/-17.18 | 107.42 | 54 | 0.078 | 0.62438 (43.97) | 1.0 | 0.4908 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
