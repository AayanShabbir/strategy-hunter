# gen_2610241002_000 — engine run 20261024_100935_gen_2610241002_000

Hypothesis: grammar draw seed=2610241002: drop_revert

**0/8 pass.** Ledger N at evaluation: 2290. PBO (CSCV) across family: 0.171. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 ed090ef4ed383d36017847e596a18301e1e6a1cede4ad514c342d121d9852fa3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2283 | megacap|drop_revert(drop=0.05,hold=3,n=1) | -1.43/-0.07/-6.46 | 118.49 | 32 | 0.0288 | 0.998 (48.17) | 1.0 | 0.0115 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2284 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 26.06/0.87/-6.6 | 118.49 | 93 | 0.0334 | 0.7982 (47.77) | 1.0 | 0.1474 | 0.974 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2285 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 6.46/0.41/-6.02 | 118.49 | 29 | 0.0329 | 0.97502 (49.04) | 1.0 | 0.032 | 0.5015 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2286 | megacap|drop_revert(drop=0.05,hold=5,n=3) | 34.21/0.97/-7.24 | 118.49 | 89 | 0.034 | 0.6963 (47.69) | 1.0 | 0.2081 | 0.957 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2287 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0135 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2288 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 9.6/0.6/-2.49 | 118.49 | 11 | 0.0244 | 0.92108 (58.62) | 1.0 | 0.048 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2289 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0135 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2290 | megacap|drop_revert(drop=0.1,hold=5,n=3) | 6.12/0.42/-2.49 | 118.49 | 9 | 0.025 | 0.95405 (57.16) | 1.0 | 0.0265 | 0.5 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
