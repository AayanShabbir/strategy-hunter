# gen_2610241101_000 — engine run 20261024_110529_gen_2610241101_000

Hypothesis: grammar draw seed=2610241101: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2394. PBO (CSCV) across family: 0.517. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4f8102206856edbf1d24dbb91456f575efbb608c99302e4ec00037718507a76c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2387 | megacap|rsi_revert(entry=5,exit=60,n=2) | 25.47/0.84/-6.22 | 118.49 | 113 | 0.0486 | 0.83217 (45.65) | 1.0 | 0.7003 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2388 | megacap|rsi_revert(entry=5,exit=60,n=3) | 12.68/0.73/-3.85 | 118.49 | 28 | 0.0427 | 0.94805 (47.12) | 1.0 | 0.5983 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2389 | megacap|rsi_revert(entry=5,exit=80,n=2) | 34.23/0.96/-7.01 | 118.49 | 102 | 0.0501 | 0.7043 (45.9) | 1.0 | 0.7706 | 0.97 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2390 | megacap|rsi_revert(entry=5,exit=80,n=3) | 25.72/1.21/-3.92 | 118.49 | 28 | 0.0427 | 0.82018 (46.97) | 1.0 | 0.8957 | 0.9785 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2391 | megacap|rsi_revert(entry=10,exit=60,n=2) | 29.82/0.83/-10.27 | 118.49 | 210 | 0.0494 | 0.74725 (43.58) | 1.0 | 0.669 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2392 | megacap|rsi_revert(entry=10,exit=60,n=3) | 21.44/0.72/-6.23 | 118.49 | 71 | 0.0502 | 0.89011 (46.78) | 1.0 | 0.5973 | 0.4945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2393 | megacap|rsi_revert(entry=10,exit=80,n=2) | 36.03/0.86/-9.51 | 118.49 | 178 | 0.0505 | 0.63337 (44.38) | 1.0 | 0.6804 | 0.974 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2394 | megacap|rsi_revert(entry=10,exit=80,n=3) | 42.99/1.12/-6.7 | 118.49 | 68 | 0.0501 | 0.58042 (47.3) | 1.0 | 0.8582 | 0.9245 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
