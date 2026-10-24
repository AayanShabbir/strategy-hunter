# gen_2410240211_000 — engine run 20261024_020810_gen_2410240211_000

Hypothesis: grammar draw seed=2410240211: drop_revert+day_of_week

**0/40 pass.** Ledger N at evaluation: 1566. PBO (CSCV) across family: 0.81. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 6ccb3148f8f70866194c804dc2db62cf70a763c14c2127710aeeec9d5d18334e. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1527 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=0) | 8.87/0.87/-3.31 | -38.66 | 19 | 0.0347 | 0.08292 (-21.02) | 1.0 | 0.0029 | 0.256 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1528 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=1) | -1.98/-0.74/-1.99 | -38.66 | 17 | 0.0253 | 0.15385 (-20.06) | 1.0 | 0.0001 | 0.3115 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1529 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=2) | -0.48/-0.14/-1.64 | -38.66 | 23 | 0.0338 | 0.16184 (-20.44) | 1.0 | 0.0005 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1530 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=3) | -1.98/-0.96/-1.98 | -38.66 | 19 | 0.0424 | 0.16484 (-20.35) | 1.0 | 0.0 | 0.312 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1531 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=4) | -2.09/-0.87/-2.09 | -38.66 | 12 | 0.0313 | 0.16983 (-21.06) | 1.0 | 0.0 | 0.31 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1532 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | 12.6/0.84/-4.78 | -38.66 | 114 | 0.0479 | 0.07393 (-23.15) | 1.0 | 0.0076 | 0.233 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1533 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 4.57/0.49/-5.78 | -38.66 | 135 | 0.0555 | 0.1029 (-21.63) | 1.0 | 0.0053 | 0.2745 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1534 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -3.55/-0.31/-9.67 | -38.66 | 152 | 0.0514 | 0.21179 (-20.9) | 1.0 | 0.0003 | 0.3045 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1535 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | -11.04/-0.94/-15.75 | -38.66 | 166 | 0.0494 | 0.20679 (-23.09) | 1.0 | 0.0 | 0.375 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1536 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=4) | -13.18/-0.99/-17.9 | -38.66 | 166 | 0.0507 | 0.31868 (-21.83) | 1.0 | 0.0 | 0.3775 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1537 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=0) | 14.58/1.1/-3.76 | -38.66 | 28 | 0.0347 | 0.02398 (-21.55) | 1.0 | 0.0098 | 0.2245 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 1538 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=1) | 2.24/0.46/-4.02 | -38.66 | 35 | 0.0272 | 0.07692 (-21.95) | 1.0 | 0.0047 | 0.2885 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1539 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=2) | 0.73/0.13/-4.92 | -38.66 | 33 | 0.0326 | 0.16184 (-20.82) | 1.0 | 0.0022 | 0.2895 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1540 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=3) | -0.62/-0.1/-3.99 | -38.66 | 35 | 0.0388 | 0.14086 (-21.2) | 1.0 | 0.0007 | 0.3005 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1541 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=4) | 0.48/0.13/-1.71 | -38.66 | 30 | 0.0393 | 0.14885 (-19.12) | 1.0 | 0.0 | 0.2935 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1542 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | 16.5/0.83/-9.67 | -38.66 | 150 | 0.0492 | 0.04396 (-20.88) | 1.0 | 0.0116 | 0.217 | False | cost_stop, holm, dsr, spa, pbo |
| 1543 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 2.75/0.29/-11.47 | -38.66 | 179 | 0.0551 | 0.07293 (-21.97) | 1.0 | 0.0027 | 0.2755 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1544 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | 1.21/0.12/-15.49 | -38.66 | 182 | 0.0529 | 0.14985 (-21.46) | 1.0 | 0.001 | 0.262 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1545 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | -12.49/-0.92/-18.59 | -38.66 | 202 | 0.0502 | 0.21678 (-22.24) | 1.0 | 0.0 | 0.3745 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1546 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=4) | -10.5/-0.61/-17.16 | -38.66 | 214 | 0.0509 | 0.32967 (-22.58) | 1.0 | 0.0 | 0.36 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1547 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=0) | 1.61/0.53/-1.5 | -38.66 | 5 | 0.0204 | 0.13487 (-22.65) | 1.0 | 0.0061 | 0.292 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1548 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=1) | -1.0/-0.88/-1.0 | -38.66 | 5 | 0.0183 | 0.11389 (-20.91) | 1.0 | 0.0 | 0.305 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1549 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=2) | 1.99/0.83/-1.11 | -38.66 | 6 | 0.031 | 0.12587 (-20.65) | 1.0 | 0.0157 | 0.286 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1550 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=3) | -0.63/-0.48/-1.01 | -38.66 | 3 | 0.025 | 0.12987 (-22.42) | 1.0 | 0.0 | 0.302 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1551 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=4) | 0.0/0.0/0.0 | -38.66 | 2 | 0.0227 | 0.1049 (-20.95) | 1.0 | 0.0 | 0.2995 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1552 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | 3.83/0.65/-3.2 | -38.66 | 16 | 0.0269 | 0.13487 (-20.47) | 1.0 | 0.0077 | 0.2805 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1553 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 1.09/0.28/-2.04 | -38.66 | 13 | 0.0209 | 0.07592 (-22.08) | 1.0 | 0.0015 | 0.2925 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1554 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | 0.24/0.06/-6.52 | -38.66 | 17 | 0.0311 | 0.14885 (-19.81) | 1.0 | 0.0014 | 0.29 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1555 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | -1.88/-0.42/-4.44 | -38.66 | 20 | 0.0309 | 0.11289 (-20.96) | 1.0 | 0.0001 | 0.3075 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1556 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=4) | -1.0/-0.28/-2.52 | -38.66 | 16 | 0.0374 | 0.18482 (-20.83) | 1.0 | 0.0 | 0.3025 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1557 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=0) | 1.43/0.44/-2.02 | -38.66 | 6 | 0.0209 | 0.15884 (-20.25) | 1.0 | 0.003 | 0.287 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1558 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=1) | -1.68/-1.23/-1.7 | -38.66 | 11 | 0.0188 | 0.13886 (-20.55) | 1.0 | 0.0 | 0.309 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1559 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=2) | 3.95/1.21/-0.55 | -38.66 | 8 | 0.0289 | 0.11788 (-20.42) | 1.0 | 0.005 | 0.273 | False | min_trades, holm, dsr, spa, pbo |
| 1560 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=3) | 1.32/0.53/-1.41 | -38.66 | 6 | 0.0236 | 0.11389 (-19.88) | 1.0 | 0.0031 | 0.2895 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1561 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=4) | 0.22/0.24/-0.4 | -38.66 | 4 | 0.0231 | 0.1039 (-20.75) | 1.0 | 0.0015 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1562 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=0) | 10.92/1.01/-3.04 | -38.66 | 24 | 0.0269 | 0.07493 (-20.39) | 1.0 | 0.0108 | 0.2405 | False | min_trades, holm, dsr, spa, pbo |
| 1563 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=1) | 1.17/0.25/-4.22 | -38.66 | 24 | 0.0272 | 0.12987 (-20.03) | 1.0 | 0.0022 | 0.294 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1564 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=2) | -0.92/-0.12/-6.19 | -38.66 | 23 | 0.0303 | 0.15884 (-21.53) | 1.0 | 0.0005 | 0.296 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1565 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=3) | 2.77/0.47/-5.5 | -38.66 | 27 | 0.0352 | 0.06394 (-21.74) | 1.0 | 0.0054 | 0.282 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1566 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=4) | -5.32/-0.91/-6.01 | -38.66 | 23 | 0.0409 | 0.19181 (-21.01) | 1.0 | 0.0 | 0.332 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
