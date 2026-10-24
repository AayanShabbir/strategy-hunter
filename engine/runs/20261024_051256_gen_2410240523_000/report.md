# gen_2410240523_000 — engine run 20261024_051256_gen_2410240523_000

Hypothesis: grammar draw seed=2410240523: drop_revert

**0/8 pass.** Ledger N at evaluation: 1870. PBO (CSCV) across family: 0.017. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 72cdedd8cf39b37d2c0646face4f8557e5f11933dea733388986f02d15c15e29. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1863 | BROAD|drop_revert(drop=0.05,hold=5,n=3) | 6.13/0.32/-5.05 | 57.67 | 146 | 0.0403 | 0.98701 (26.24) | 1.0 | 0.0942 | 0.491 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1864 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 8.31/0.4/-7.79 | 57.67 | 187 | 0.042 | 0.96204 (25.29) | 1.0 | 0.1216 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1865 | BROAD|drop_revert(drop=0.05,hold=10,n=3) | 20.92/0.86/-5.39 | 57.67 | 116 | 0.042 | 0.65335 (25.08) | 1.0 | 0.3734 | 0.9275 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1866 | BROAD|drop_revert(drop=0.05,hold=10,n=5) | 18.09/0.71/-6.08 | 57.67 | 143 | 0.0446 | 0.77622 (25.64) | 1.0 | 0.2783 | 0.9655 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1867 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.82/0.22/-1.31 | 57.67 | 6 | 0.0211 | 0.96304 (27.2) | 1.0 | 0.0815 | 0.4895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1868 | BROAD|drop_revert(drop=0.15,hold=5,n=5) | -0.19/-0.04/-1.31 | 57.67 | 9 | 0.0228 | 0.98202 (27.36) | 1.0 | 0.0348 | 0.491 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1869 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 1.59/0.39/-1.31 | 57.67 | 5 | 0.0228 | 0.96204 (26.98) | 1.0 | 0.1355 | 0.488 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1870 | BROAD|drop_revert(drop=0.15,hold=10,n=5) | 0.44/0.11/-1.31 | 57.67 | 7 | 0.0232 | 0.98102 (26.96) | 1.0 | 0.059 | 0.4895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
