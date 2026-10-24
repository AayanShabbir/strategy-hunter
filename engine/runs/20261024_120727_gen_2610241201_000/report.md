# gen_2610241201_000 — engine run 20261024_120727_gen_2610241201_000

Hypothesis: grammar draw seed=2610241201: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2490. PBO (CSCV) across family: 0.498. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 ef60e3234abd3077b7dd3f283fab152a5c7cef056011e1aa3cbad9b4db2f0c10. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2483 | megacap|rsi_revert(entry=10,exit=70,n=2) | 35.83/0.91/-11.56 | 118.49 | 200 | 0.0497 | 0.67932 (45.28) | 1.0 | 0.8598 | 0.977 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2484 | megacap|rsi_revert(entry=10,exit=70,n=3) | 27.29/0.84/-7.37 | 118.49 | 69 | 0.05 | 0.81618 (46.2) | 1.0 | 0.8404 | 0.973 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2485 | megacap|rsi_revert(entry=10,exit=80,n=2) | 36.03/0.86/-9.51 | 118.49 | 178 | 0.0505 | 0.62438 (44.03) | 1.0 | 0.8221 | 0.974 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2486 | megacap|rsi_revert(entry=10,exit=80,n=3) | 42.99/1.12/-6.7 | 118.49 | 68 | 0.0501 | 0.55544 (46.45) | 1.0 | 0.9424 | 0.9245 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2487 | megacap|rsi_revert(entry=20,exit=70,n=2) | 39.67/0.87/-11.89 | 118.49 | 326 | 0.0498 | 0.52048 (41.61) | 1.0 | 0.8257 | 0.9755 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2488 | megacap|rsi_revert(entry=20,exit=70,n=3) | 37.32/0.82/-15.65 | 118.49 | 154 | 0.0503 | 0.62238 (45.59) | 1.0 | 0.8051 | 0.486 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2489 | megacap|rsi_revert(entry=20,exit=80,n=2) | 35.25/0.75/-13.68 | 118.49 | 270 | 0.0509 | 0.63936 (44.06) | 1.0 | 0.7557 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2490 | megacap|rsi_revert(entry=20,exit=80,n=3) | 41.49/0.83/-13.02 | 118.49 | 138 | 0.0526 | 0.55744 (46.77) | 1.0 | 0.803 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
