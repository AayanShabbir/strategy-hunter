# gen_2610241008_000 — engine run 20261024_100954_gen_2610241008_000

Hypothesis: grammar draw seed=2610241008: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2322. PBO (CSCV) across family: 0.618. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 2be5c2b648e640fd547941afab515059094635e212712bc46f465631ac0181e8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2315 | sectors|rsi_revert(entry=5,exit=60,n=3) | -0.52/-0.06/-4.16 | 94.31 | 45 | 0.0597 | 1.0 (38.94) | 1.0 | 0.0438 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2316 | sectors|rsi_revert(entry=5,exit=60,n=5) | 0.58/0.47/-0.27 | 94.31 | 6 | 0.0564 | 0.96104 (41.53) | 1.0 | 0.1765 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2317 | sectors|rsi_revert(entry=5,exit=70,n=3) | 1.51/0.22/-4.16 | 94.31 | 45 | 0.0597 | 0.997 (40.49) | 1.0 | 0.1116 | 0.497 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2318 | sectors|rsi_revert(entry=5,exit=70,n=5) | 1.01/0.39/-1.22 | 94.31 | 6 | 0.0564 | 0.96903 (41.72) | 1.0 | 0.1716 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2319 | sectors|rsi_revert(entry=10,exit=60,n=3) | 14.04/0.57/-8.07 | 94.31 | 124 | 0.0629 | 0.98302 (38.72) | 1.0 | 0.2276 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2320 | sectors|rsi_revert(entry=10,exit=60,n=5) | 1.61/0.24/-3.71 | 94.31 | 23 | 0.0554 | 0.98002 (43.76) | 1.0 | 0.1203 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2321 | sectors|rsi_revert(entry=10,exit=70,n=3) | 23.84/0.84/-8.07 | 94.31 | 120 | 0.063 | 0.86613 (38.88) | 1.0 | 0.4229 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2322 | sectors|rsi_revert(entry=10,exit=70,n=5) | 3.05/0.42/-3.71 | 94.31 | 23 | 0.0554 | 0.97303 (38.27) | 1.0 | 0.193 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
