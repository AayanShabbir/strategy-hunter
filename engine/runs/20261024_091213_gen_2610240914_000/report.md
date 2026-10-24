# gen_2610240914_000 — engine run 20261024_091213_gen_2610240914_000

Hypothesis: grammar draw seed=2610240914: drop_revert

**0/8 pass.** Ledger N at evaluation: 2262. PBO (CSCV) across family: 0.386. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 fc05a8b15ee5975fa96737f0bf63fb76a797b426c4a27c43b934acae92951c86. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2255 | index|drop_revert(drop=0.05,hold=3,n=1) | 2.22/0.19/-2.67 | 84.67 | 13 | 0.0375 | 0.99201 (36.7) | 1.0 | 0.0168 | 0.489 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2256 | index|drop_revert(drop=0.05,hold=3,n=3) | 16.45/0.74/-4.28 | 84.67 | 80 | 0.0406 | 0.8981 (36.09) | 1.0 | 0.0938 | 0.973 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2257 | index|drop_revert(drop=0.05,hold=10,n=1) | 2.51/0.15/-5.31 | 84.67 | 11 | 0.0385 | 0.99001 (36.43) | 1.0 | 0.0179 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2258 | index|drop_revert(drop=0.05,hold=10,n=3) | 26.89/1.02/-5.69 | 84.67 | 62 | 0.0438 | 0.73626 (36.21) | 1.0 | 0.269 | 0.927 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2259 | index|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 84.67 | 3 | 0.0175 | 1.0 (34.39) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2260 | index|drop_revert(drop=0.1,hold=3,n=3) | 2.02/0.13/-4.63 | 84.67 | 11 | 0.0277 | 0.997 (37.9) | 1.0 | 0.0174 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2261 | index|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 84.67 | 3 | 0.0175 | 1.0 (40.44) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2262 | index|drop_revert(drop=0.1,hold=10,n=3) | 6.39/0.31/-5.69 | 84.67 | 9 | 0.0281 | 0.98601 (35.92) | 1.0 | 0.0306 | 0.483 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
