# gen_2610241022_000 — engine run 20261024_101023_gen_2610241022_000

Hypothesis: grammar draw seed=2610241022: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2382. PBO (CSCV) across family: 0.341. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 598f62542555501666af85433ab391502e46edb0e526aa76185edce072819b47. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2375 | megacap|rsi_revert(entry=5,exit=60,n=2) | 25.47/0.84/-6.22 | 118.49 | 113 | 0.0486 | 0.84316 (46.21) | 1.0 | 0.5678 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2376 | megacap|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2377 | megacap|rsi_revert(entry=5,exit=80,n=2) | 34.23/0.96/-7.01 | 118.49 | 102 | 0.0501 | 0.71229 (46.37) | 1.0 | 0.6609 | 0.97 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2378 | megacap|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2379 | megacap|rsi_revert(entry=20,exit=60,n=2) | 31.65/0.75/-10.83 | 118.49 | 359 | 0.0491 | 0.67832 (39.95) | 1.0 | 0.4901 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2380 | megacap|rsi_revert(entry=20,exit=60,n=5) | 30.41/0.91/-6.44 | 118.49 | 65 | 0.0471 | 0.75624 (47.33) | 1.0 | 0.6296 | 0.9635 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2381 | megacap|rsi_revert(entry=20,exit=80,n=2) | 35.25/0.75/-13.68 | 118.49 | 270 | 0.0509 | 0.61439 (43.05) | 1.0 | 0.4907 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2382 | megacap|rsi_revert(entry=20,exit=80,n=5) | 72.05/1.34/-11.58 | 118.49 | 50 | 0.0502 | 0.14186 (49.27) | 1.0 | 0.8654 | 0.848 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
