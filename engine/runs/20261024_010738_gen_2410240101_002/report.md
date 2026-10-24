# gen_2410240101_002 — engine run 20261024_010738_gen_2410240101_002

Hypothesis: grammar draw seed=2410240101: drop_revert

**0/8 pass.** Ledger N at evaluation: 1406. PBO (CSCV) across family: 0.818. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 60ebbd7891732f07806bf3a865636e109301b1db041f6369ceea55e96c2d6c3d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1399 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.83017 (126.08) | 1.0 | 0.2278 | 0.8865 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1400 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.94306 (93.43) | 1.0 | 0.1039 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1401 | crypto_d|drop_revert(drop=0.1,hold=10,n=1) | -0.44/0.12/-24.88 | 234.6 | 97 | 0.0098 | 0.93107 (82.77) | 1.0 | 0.1263 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1402 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 11.7/0.39/-33.6 | 234.6 | 187 | 0.0118 | 0.8002 (62.44) | 1.0 | 0.2044 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1403 | crypto_d|drop_revert(drop=0.15,hold=5,n=1) | 2.44/0.29/-5.48 | 234.6 | 33 | 0.0074 | 0.94605 (132.25) | 1.0 | 0.1668 | 0.895 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1404 | crypto_d|drop_revert(drop=0.15,hold=5,n=3) | 7.63/0.36/-12.4 | 234.6 | 109 | 0.0089 | 0.83916 (120.43) | 1.0 | 0.188 | 0.8895 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1405 | crypto_d|drop_revert(drop=0.15,hold=10,n=1) | -9.04/-0.5/-14.91 | 234.6 | 31 | 0.0075 | 0.999 (136.44) | 1.0 | 0.0275 | 0.906 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1406 | crypto_d|drop_revert(drop=0.15,hold=10,n=3) | 9.36/0.38/-15.09 | 234.6 | 91 | 0.0094 | 0.83017 (131.29) | 1.0 | 0.2005 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
