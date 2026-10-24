# gen_2410240031_003 — engine run 20261024_000622_gen_2410240031_003

Hypothesis: grammar draw seed=2410240031: drop_revert+day_of_week

**0/32 pass.** Ledger N at evaluation: 1382. PBO (CSCV) across family: 0.533. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 5f5e20908c2787480286d70cfde45e2d2eef3508c8c301e6916c9c8b8773074f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1351 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=0) | 10.01/1.0/-2.31 | -38.66 | 19 | 0.0347 | 0.06893 (-21.88) | 1.0 | 0.0003 | 0.251 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1352 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=1) | -1.61/-0.92/-1.67 | -38.66 | 17 | 0.0253 | 0.13287 (-22.3) | 1.0 | 0.0 | 0.307 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1353 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=2) | -0.83/-0.29/-2.38 | -38.66 | 23 | 0.0338 | 0.16983 (-21.29) | 1.0 | 0.0 | 0.299 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1354 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=3) | -0.72/-0.34/-1.23 | -38.66 | 19 | 0.0424 | 0.15684 (-21.88) | 1.0 | 0.0 | 0.301 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1355 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | 4.98/0.45/-4.93 | -38.66 | 88 | 0.0477 | 0.10889 (-22.38) | 1.0 | 0.0009 | 0.2705 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1356 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 2.83/0.39/-3.57 | -38.66 | 107 | 0.0559 | 0.08492 (-22.42) | 1.0 | 0.0014 | 0.28 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1357 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -7.39/-0.91/-9.57 | -38.66 | 106 | 0.05 | 0.25175 (-21.01) | 1.0 | 0.0 | 0.337 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1358 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | -9.15/-0.96/-12.81 | -38.66 | 137 | 0.0488 | 0.2048 (-22.26) | 1.0 | 0.0 | 0.354 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1359 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=0) | 14.58/1.1/-3.76 | -38.66 | 28 | 0.0347 | 0.03197 (-21.09) | 1.0 | 0.0019 | 0.2245 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 1360 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=1) | 2.24/0.46/-4.02 | -38.66 | 35 | 0.0272 | 0.0989 (-21.0) | 1.0 | 0.0012 | 0.2885 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1361 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=2) | 0.73/0.13/-4.92 | -38.66 | 33 | 0.0326 | 0.15085 (-20.94) | 1.0 | 0.0005 | 0.2895 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1362 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=3) | -0.62/-0.1/-3.99 | -38.66 | 35 | 0.0388 | 0.16484 (-20.32) | 1.0 | 0.0001 | 0.3005 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1363 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | 16.5/0.83/-9.67 | -38.66 | 150 | 0.0492 | 0.04995 (-21.45) | 1.0 | 0.0029 | 0.217 | False | cost_stop, holm, dsr, spa, pbo |
| 1364 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 2.75/0.29/-11.47 | -38.66 | 179 | 0.0551 | 0.07992 (-22.72) | 1.0 | 0.0007 | 0.2755 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1365 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | 1.21/0.12/-15.49 | -38.66 | 182 | 0.0529 | 0.14785 (-22.52) | 1.0 | 0.0002 | 0.262 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1366 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | -12.49/-0.92/-18.59 | -38.66 | 202 | 0.0502 | 0.21578 (-22.43) | 1.0 | 0.0 | 0.3745 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1367 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=0) | 0.38/1.16/0.0 | -38.66 | 2 | 0.0013 | 0.07992 (-20.6) | 1.0 | 0.0 | 0.297 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1368 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=1) | -1.32/-1.16/-1.32 | -38.66 | 3 | 0.0038 | 0.19281 (-20.52) | 1.0 | 0.0 | 0.3065 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1369 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=2) | 0.8/0.82/0.0 | -38.66 | 1 | 0.0271 | 0.15784 (-20.55) | 1.0 | 0.0 | 0.2915 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1370 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=3) | 0.18/0.82/0.0 | -38.66 | 1 | 0.0309 | 0.03297 (-21.12) | 1.0 | 0.0 | 0.299 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1371 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=0) | -0.76/-0.77/-1.0 | -38.66 | 4 | 0.0026 | 0.0999 (-20.3) | 1.0 | 0.0 | 0.3025 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1372 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=1) | -1.27/-1.17/-1.27 | -38.66 | 3 | 0.0038 | 0.18282 (-20.27) | 1.0 | 0.0 | 0.306 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1373 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=2) | 1.33/0.36/-2.23 | -38.66 | 10 | 0.0299 | 0.12188 (-21.08) | 1.0 | 0.0018 | 0.287 | False | min_trades, holm, dsr, spa, pbo |
| 1374 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=3) | 2.8/0.84/-1.11 | -38.66 | 4 | 0.0189 | 0.10589 (-21.38) | 1.0 | 0.0007 | 0.2825 | False | min_trades, holm, dsr, spa, pbo |
| 1375 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=0) | 0.06/0.11/-0.33 | -38.66 | 2 | 0.0013 | 0.07093 (-21.0) | 1.0 | 0.0005 | 0.2995 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1376 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=1) | -1.71/-1.5/-1.71 | -38.66 | 5 | 0.0023 | 0.15784 (-20.88) | 1.0 | 0.0 | 0.3085 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1377 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=2) | 2.64/1.02/0.0 | -38.66 | 3 | 0.0107 | 0.13487 (-21.28) | 1.0 | 0.0 | 0.2805 | False | min_trades, holm, dsr, spa, pbo |
| 1378 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=3) | 0.46/0.93/0.0 | -38.66 | 1 | 0.0309 | 0.03896 (-20.26) | 1.0 | 0.0 | 0.295 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1379 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | 0.59/0.51/-0.61 | -38.66 | 5 | 0.0265 | 0.1029 (-20.45) | 1.0 | 0.0007 | 0.2945 | False | min_trades, holm, dsr, spa, pbo |
| 1380 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | -2.07/-1.27/-2.07 | -38.66 | 8 | 0.0064 | 0.16883 (-21.07) | 1.0 | 0.0 | 0.311 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1381 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -0.58/-0.08/-5.2 | -38.66 | 12 | 0.0298 | 0.12987 (-20.87) | 1.0 | 0.0001 | 0.2955 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1382 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 6.63/1.44/-1.41 | -38.66 | 12 | 0.0274 | 0.07293 (-22.24) | 1.0 | 0.0134 | 0.2615 | False | min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
