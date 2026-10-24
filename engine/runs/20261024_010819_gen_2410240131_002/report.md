# gen_2410240131_002 — engine run 20261024_010819_gen_2410240131_002

Hypothesis: grammar draw seed=2410240131: drop_revert+day_of_week

**0/32 pass.** Ledger N at evaluation: 1494. PBO (CSCV) across family: 0.608. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 eccb90b0b5f25960358811bd95678b9af8335c4ae63e22def59489bd02401e38. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1463 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=0) | -4.34/-0.56/-5.93 | 50.2 | 260 | 0.0366 | 1.0 (22.52) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1464 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=1) | 4.89/0.33/-2.62 | 50.2 | 269 | 0.0386 | 1.0 (22.93) | 1.0 | 0.0003 | 0.5015 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1465 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=2) | -3.22/-0.77/-4.03 | 50.2 | 268 | 0.0378 | 1.0 (22.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1466 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=3) | 2.54/0.52/-1.89 | 50.2 | 273 | 0.0367 | 0.999 (22.96) | 1.0 | 0.0059 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1467 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -4.65/-0.54/-6.33 | 50.2 | 373 | 0.0406 | 1.0 (22.09) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1468 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 3.28/0.23/-4.25 | 50.2 | 389 | 0.041 | 1.0 (21.78) | 1.0 | 0.0005 | 0.497 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1469 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -2.02/-0.41/-3.83 | 50.2 | 403 | 0.0409 | 1.0 (22.08) | 1.0 | 0.0001 | 0.4995 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1470 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 1.69/0.28/-3.18 | 50.2 | 405 | 0.0408 | 1.0 (21.77) | 1.0 | 0.0038 | 0.494 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1471 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -1.47/-0.15/-5.93 | 50.2 | 431 | 0.0375 | 1.0 (22.55) | 1.0 | 0.0001 | 0.503 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1472 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 3.91/0.27/-3.47 | 50.2 | 469 | 0.0387 | 0.999 (22.29) | 1.0 | 0.0005 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1473 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -2.82/-0.58/-4.1 | 50.2 | 453 | 0.0383 | 1.0 (21.88) | 1.0 | 0.0 | 0.4995 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1474 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 5.33/0.83/-1.87 | 50.2 | 458 | 0.038 | 0.997 (22.51) | 1.0 | 0.0367 | 0.49 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1475 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -2.14/-0.21/-6.32 | 50.2 | 600 | 0.0411 | 1.0 (21.56) | 1.0 | 0.0001 | 0.5 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1476 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 3.67/0.25/-3.71 | 50.2 | 641 | 0.0415 | 0.998 (21.64) | 1.0 | 0.0006 | 0.4965 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1477 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -2.27/-0.37/-4.24 | 50.2 | 650 | 0.0411 | 1.0 (21.36) | 1.0 | 0.0001 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1478 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 3.61/0.47/-3.11 | 50.2 | 654 | 0.0411 | 0.998 (21.3) | 1.0 | 0.0108 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1479 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=0) | -0.81/-0.75/-0.81 | 50.2 | 11 | 0.0153 | 1.0 (23.21) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1480 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=1) | 0.79/0.41/-0.29 | 50.2 | 11 | 0.0155 | 0.998 (22.95) | 1.0 | 0.0002 | 0.5025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1481 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=2) | -0.41/-0.52/-0.45 | 50.2 | 9 | 0.0145 | 1.0 (23.36) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1482 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=3) | 0.47/0.82/0.0 | 50.2 | 9 | 0.0148 | 0.999 (23.54) | 1.0 | 0.0002 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1483 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=0) | -0.76/-0.7/-0.82 | 50.2 | 21 | 0.0151 | 0.999 (23.02) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1484 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=1) | 0.79/0.41/-0.29 | 50.2 | 21 | 0.0155 | 0.997 (23.29) | 1.0 | 0.0002 | 0.5025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1485 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=2) | -0.41/-0.52/-0.45 | 50.2 | 22 | 0.0146 | 1.0 (23.16) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1486 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=3) | 0.47/0.82/0.0 | 50.2 | 25 | 0.0173 | 0.998 (23.15) | 1.0 | 0.0002 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1487 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=0) | -0.54/-0.48/-0.82 | 50.2 | 20 | 0.0155 | 1.0 (23.32) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1488 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=1) | 0.9/0.46/-0.29 | 50.2 | 19 | 0.0154 | 0.998 (23.03) | 1.0 | 0.0002 | 0.5005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1489 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=2) | -0.44/-0.5/-0.45 | 50.2 | 16 | 0.0144 | 1.0 (22.87) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1490 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=3) | 0.49/0.75/-0.12 | 50.2 | 16 | 0.015 | 1.0 (23.84) | 1.0 | 0.0041 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1491 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | -0.54/-0.48/-0.82 | 50.2 | 32 | 0.0155 | 1.0 (23.25) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1492 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | 0.88/0.45/-0.31 | 50.2 | 33 | 0.0155 | 0.99401 (23.36) | 1.0 | 0.0003 | 0.5005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1493 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -0.44/-0.5/-0.45 | 50.2 | 33 | 0.0148 | 0.998 (22.97) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1494 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 0.49/0.75/-0.12 | 50.2 | 37 | 0.0164 | 0.998 (22.6) | 1.0 | 0.0041 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
