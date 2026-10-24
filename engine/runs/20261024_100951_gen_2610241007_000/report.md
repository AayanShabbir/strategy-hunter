# gen_2610241007_000 — engine run 20261024_100951_gen_2610241007_000

Hypothesis: grammar draw seed=2610241007: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 2314. PBO (CSCV) across family: 0.434. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4b940179d69eb64361612d02d71088c8b209aa9852b7b19d17568e552653112c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2307 | megacap|rsi_revert(entry=5,exit=60,n=2)+rsi_band(hi=60) | 25.49/0.84/-6.22 | 118.49 | 113 | 0.0492 | 0.84515 (44.99) | 1.0 | 0.5578 | 0.4865 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2308 | megacap|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2309 | megacap|rsi_revert(entry=5,exit=80,n=2)+rsi_band(hi=60) | 32.99/0.93/-7.01 | 118.49 | 105 | 0.0501 | 0.72428 (47.12) | 1.0 | 0.6281 | 0.971 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2310 | megacap|rsi_revert(entry=5,exit=80,n=5)+rsi_band(hi=60) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2311 | megacap|rsi_revert(entry=20,exit=60,n=2)+rsi_band(hi=60) | 28.14/0.69/-12.21 | 118.49 | 337 | 0.0486 | 0.6983 (39.7) | 1.0 | 0.4335 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2312 | megacap|rsi_revert(entry=20,exit=60,n=5)+rsi_band(hi=60) | 30.41/0.91/-6.44 | 118.49 | 64 | 0.0471 | 0.78921 (47.74) | 1.0 | 0.6191 | 0.9635 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2313 | megacap|rsi_revert(entry=20,exit=80,n=2)+rsi_band(hi=60) | 31.82/0.7/-12.66 | 118.49 | 266 | 0.0501 | 0.7003 (44.08) | 1.0 | 0.4465 | 0.511 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2314 | megacap|rsi_revert(entry=20,exit=80,n=5)+rsi_band(hi=60) | 67.51/1.3/-11.58 | 118.49 | 64 | 0.049 | 0.17383 (47.13) | 1.0 | 0.8454 | 0.8545 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
