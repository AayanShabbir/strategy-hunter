# gen_2610241116_000 — engine run 20261024_110613_gen_2610241116_000

Hypothesis: grammar draw seed=2610241116: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2474. PBO (CSCV) across family: 0.264. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 c44e50b2bc3c036ce30b4836f3c681a842309fad2bf434a8bc7ed818b84946fb. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2467 | megacap|rsi_revert(entry=5,exit=60,n=2) | 25.47/0.84/-6.22 | 118.49 | 113 | 0.0486 | 0.82617 (45.95) | 1.0 | 0.8853 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2468 | megacap|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2469 | megacap|rsi_revert(entry=5,exit=70,n=2) | 34.15/1.03/-5.95 | 118.49 | 109 | 0.0494 | 0.7013 (45.05) | 1.0 | 0.9513 | 0.9715 | False | beats_buy_hold, cost_stop, holm, spa |
| 2470 | megacap|rsi_revert(entry=5,exit=70,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2471 | megacap|rsi_revert(entry=20,exit=60,n=2) | 31.65/0.75/-10.83 | 118.49 | 359 | 0.0491 | 0.67133 (41.33) | 1.0 | 0.7932 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2472 | megacap|rsi_revert(entry=20,exit=60,n=5) | 30.41/0.91/-6.44 | 118.49 | 65 | 0.0471 | 0.76823 (47.65) | 1.0 | 0.9037 | 0.9635 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2473 | megacap|rsi_revert(entry=20,exit=70,n=2) | 39.67/0.87/-11.89 | 118.49 | 326 | 0.0498 | 0.53846 (42.26) | 1.0 | 0.8507 | 0.9755 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2474 | megacap|rsi_revert(entry=20,exit=70,n=5) | 34.47/0.9/-11.61 | 118.49 | 60 | 0.0497 | 0.74126 (48.07) | 1.0 | 0.8718 | 0.9705 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
