# gen_2410240001_001 — engine run 20261024_000533_gen_2410240001_001

Hypothesis: grammar draw seed=2410240001: drop_revert+day_of_week

**0/32 pass.** Ledger N at evaluation: 1298. PBO (CSCV) across family: 0.702. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 f88f83f52866bc08b6b656c4a239b5a1ad0234bb57421085d69de48b63a4d31c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1267 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=0) | -5.04/-0.36/-9.61 | 234.6 | 247 | 0.0098 | 0.92008 (80.45) | 1.0 | 0.0008 | 0.9005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1268 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=1) | 26.65/1.16/-8.41 | 234.6 | 300 | 0.0106 | 0.68731 (72.73) | 1.0 | 0.032 | 0.87 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1269 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=2) | -15.72/-0.74/-20.82 | 234.6 | 328 | 0.0111 | 0.97902 (75.64) | 1.0 | 0.0005 | 0.9125 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1270 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=3) | -1.16/0.02/-13.76 | 234.6 | 329 | 0.0111 | 0.91409 (71.62) | 1.0 | 0.0032 | 0.8985 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1271 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | -11.63/-0.59/-18.63 | 234.6 | 447 | 0.0119 | 0.96603 (114.43) | 1.0 | 0.0003 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1272 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 34.89/1.13/-6.89 | 234.6 | 467 | 0.012 | 0.62338 (76.54) | 1.0 | 0.0458 | 0.866 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1273 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -8.12/-0.26/-21.22 | 234.6 | 460 | 0.0121 | 0.93207 (81.39) | 1.0 | 0.0013 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1274 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | 5.04/0.31/-10.77 | 234.6 | 456 | 0.0118 | 0.86513 (90.76) | 1.0 | 0.0082 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1275 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=0) | -4.44/-0.22/-8.24 | 234.6 | 404 | 0.0107 | 0.92807 (104.9) | 1.0 | 0.0013 | 0.902 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1276 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=1) | 9.21/0.45/-11.79 | 234.6 | 414 | 0.0108 | 0.82118 (69.91) | 1.0 | 0.0084 | 0.8865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1277 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=2) | -23.25/-1.08/-28.27 | 234.6 | 405 | 0.0108 | 0.995 (93.92) | 1.0 | 0.0001 | 0.92 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1278 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=3) | -1.6/0.02/-14.62 | 234.6 | 450 | 0.011 | 0.92707 (94.92) | 1.0 | 0.0031 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1279 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -9.84/-0.44/-15.31 | 234.6 | 571 | 0.0122 | 0.95405 (77.71) | 1.0 | 0.0005 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1280 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 40.02/1.19/-10.62 | 234.6 | 580 | 0.0123 | 0.58342 (73.27) | 1.0 | 0.0572 | 0.8595 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1281 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -11.26/-0.35/-21.28 | 234.6 | 568 | 0.0123 | 0.95405 (96.23) | 1.0 | 0.0009 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1282 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 4.04/0.25/-11.31 | 234.6 | 587 | 0.0123 | 0.84416 (92.05) | 1.0 | 0.0067 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1283 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=0) | -3.77/-0.67/-4.92 | 234.6 | 63 | 0.0081 | 0.95105 (67.18) | 1.0 | 0.0 | 0.9005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1284 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=1) | 13.74/0.86/-5.82 | 234.6 | 65 | 0.0089 | 0.8042 (66.86) | 1.0 | 0.0056 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1285 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=2) | 3.32/0.39/-5.12 | 234.6 | 71 | 0.0088 | 0.93606 (125.72) | 1.0 | 0.0056 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1286 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=3) | 2.1/1.29/-0.03 | 234.6 | 58 | 0.0082 | 0.94605 (152.54) | 1.0 | 0.0067 | 0.8965 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1287 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=0) | 1.03/0.12/-11.12 | 234.6 | 240 | 0.01 | 0.88711 (64.3) | 1.0 | 0.0042 | 0.898 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1288 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=1) | 8.92/0.51/-6.22 | 234.6 | 229 | 0.0101 | 0.84416 (78.49) | 1.0 | 0.0092 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1289 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=2) | -7.26/-0.37/-15.12 | 234.6 | 222 | 0.0102 | 0.95005 (82.73) | 1.0 | 0.0015 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1290 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=3) | 11.01/1.01/-4.48 | 234.6 | 215 | 0.0099 | 0.82617 (106.89) | 1.0 | 0.0368 | 0.888 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1291 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=0) | -6.21/-0.96/-7.32 | 234.6 | 103 | 0.0081 | 0.95704 (99.15) | 1.0 | 0.0 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1292 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=1) | 9.78/0.62/-5.82 | 234.6 | 102 | 0.0086 | 0.83017 (109.17) | 1.0 | 0.0057 | 0.889 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1293 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=2) | -3.77/-0.33/-11.62 | 234.6 | 94 | 0.0085 | 0.95005 (107.06) | 1.0 | 0.0013 | 0.9005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1294 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=3) | 1.8/0.3/-3.42 | 234.6 | 97 | 0.0084 | 0.90809 (126.17) | 1.0 | 0.0069 | 0.895 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1295 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | -1.89/-0.08/-12.54 | 234.6 | 314 | 0.0102 | 0.92108 (68.25) | 1.0 | 0.0022 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1296 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 19.19/0.86/-6.22 | 234.6 | 315 | 0.0103 | 0.75624 (125.06) | 1.0 | 0.0244 | 0.877 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1297 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | -13.75/-0.64/-20.7 | 234.6 | 319 | 0.0105 | 0.97602 (98.32) | 1.0 | 0.0006 | 0.9135 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1298 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | 15.98/1.16/-4.14 | 234.6 | 306 | 0.0106 | 0.76923 (71.76) | 1.0 | 0.0633 | 0.884 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
