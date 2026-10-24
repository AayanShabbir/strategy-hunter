# gen_2610241210_000 — engine run 20261024_120753_gen_2610241210_000

Hypothesis: grammar draw seed=2610241210: supertrend+day_of_week

**0/16 pass.** Ledger N at evaluation: 2550. PBO (CSCV) across family: 0.244. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 e8410e628696d0d94529f8677ee742e1bbfc2390df46590dd0ec848e809a9614. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2535 | crypto|supertrend(atr_n=7,mult=3)+day_of_week(days=0) | -5.4/-0.28/-15.72 | 434.62 | 347 | 0.0193 | 0.93506 (96.17) | 1.0 | 0.0014 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2536 | crypto|supertrend(atr_n=7,mult=3)+day_of_week(days=1) | 18.0/0.86/-11.08 | 434.62 | 351 | 0.0192 | 0.77423 (122.14) | 1.0 | 0.0453 | 0.8925 | False | beats_buy_hold, holm, dsr, spa |
| 2537 | crypto|supertrend(atr_n=7,mult=3)+day_of_week(days=2) | -10.22/-0.43/-13.66 | 434.62 | 353 | 0.0191 | 0.95405 (91.88) | 1.0 | 0.0009 | 0.9125 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2538 | crypto|supertrend(atr_n=7,mult=3)+day_of_week(days=3) | -8.06/-0.32/-15.05 | 434.62 | 348 | 0.0189 | 0.96204 (172.24) | 1.0 | 0.0013 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2539 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | -8.94/-0.41/-18.67 | 434.62 | 361 | 0.0191 | 0.95305 (162.42) | 1.0 | 0.0009 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2540 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | 23.47/1.07/-7.51 | 434.62 | 361 | 0.0186 | 0.73526 (93.27) | 1.0 | 0.0742 | 0.888 | False | beats_buy_hold, holm, dsr, spa |
| 2541 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | -18.49/-0.78/-22.07 | 434.62 | 364 | 0.0188 | 0.98601 (182.91) | 1.0 | 0.0002 | 0.917 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2542 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | -1.81/-0.0/-16.06 | 434.62 | 361 | 0.0188 | 0.9001 (180.61) | 1.0 | 0.004 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2543 | crypto|supertrend(atr_n=10,mult=3)+day_of_week(days=0) | -7.41/-0.39/-17.8 | 434.62 | 329 | 0.0197 | 0.94206 (173.78) | 1.0 | 0.0009 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2544 | crypto|supertrend(atr_n=10,mult=3)+day_of_week(days=1) | 15.72/0.77/-11.91 | 434.62 | 331 | 0.0197 | 0.78222 (108.93) | 1.0 | 0.0355 | 0.8935 | False | beats_buy_hold, holm, dsr, spa |
| 2545 | crypto|supertrend(atr_n=10,mult=3)+day_of_week(days=2) | -6.02/-0.15/-15.07 | 434.62 | 334 | 0.0196 | 0.93407 (183.07) | 1.0 | 0.0028 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2546 | crypto|supertrend(atr_n=10,mult=3)+day_of_week(days=3) | -7.07/-0.26/-15.2 | 434.62 | 327 | 0.0193 | 0.94306 (96.51) | 1.0 | 0.0016 | 0.911 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2547 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -10.09/-0.52/-18.18 | 434.62 | 360 | 0.0191 | 0.95504 (89.71) | 1.0 | 0.0004 | 0.911 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2548 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | 20.48/0.97/-8.01 | 434.62 | 361 | 0.0188 | 0.75824 (71.87) | 1.0 | 0.0588 | 0.8915 | False | beats_buy_hold, holm, dsr, spa |
| 2549 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | -21.59/-0.95/-23.07 | 434.62 | 365 | 0.0188 | 0.98801 (150.99) | 1.0 | 0.0001 | 0.918 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2550 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | -0.66/0.05/-16.27 | 434.62 | 361 | 0.0188 | 0.91209 (179.55) | 1.0 | 0.0047 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
