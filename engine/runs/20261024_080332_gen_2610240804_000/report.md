# gen_2610240804_000 — engine run 20261024_080332_gen_2610240804_000

Hypothesis: grammar draw seed=2610240804: supertrend+day_of_week

**0/20 pass.** Ledger N at evaluation: 2142. PBO (CSCV) across family: 0.5. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 701035cf6902db58c1e92aa3bbe2830be8e4314597412849d78f967c08e3e781. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2123 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | -26.56/-1.26/-31.06 | 428.6 | 696 | 0.1057 | 0.98801 (72.42) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2124 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | -13.62/-0.57/-21.88 | 428.6 | 659 | 0.0945 | 0.96404 (88.6) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2125 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | 22.77/1.09/-11.1 | 428.6 | 681 | 0.0938 | 0.71728 (128.41) | 1.0 | 0.0189 | 0.8915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2126 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -0.93/0.04/-20.07 | 428.6 | 634 | 0.0925 | 0.91608 (164.25) | 1.0 | 0.0008 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2127 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=4) | -12.18/-0.59/-13.7 | 428.6 | 622 | 0.0918 | 0.94905 (155.53) | 1.0 | 0.0001 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2128 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | -29.11/-1.44/-33.83 | 428.6 | 498 | 0.1132 | 0.996 (70.6) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2129 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | -9.62/-0.41/-22.16 | 428.6 | 464 | 0.0987 | 0.95205 (201.39) | 1.0 | 0.0002 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2130 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | 12.72/0.71/-10.78 | 428.6 | 500 | 0.0963 | 0.81219 (110.32) | 1.0 | 0.0079 | 0.8995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2131 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 5.42/0.3/-13.41 | 428.6 | 460 | 0.0942 | 0.87612 (114.66) | 1.0 | 0.002 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2132 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | -4.88/-0.25/-12.38 | 428.6 | 443 | 0.098 | 0.93207 (76.6) | 1.0 | 0.0003 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2133 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -22.42/-0.99/-27.47 | 428.6 | 710 | 0.1058 | 0.98501 (110.4) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2134 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | -13.95/-0.6/-23.15 | 428.6 | 660 | 0.0932 | 0.96404 (161.65) | 1.0 | 0.0001 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2135 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 27.59/1.24/-10.54 | 428.6 | 686 | 0.0932 | 0.67832 (97.57) | 1.0 | 0.0288 | 0.884 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2136 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -5.34/-0.16/-22.24 | 428.6 | 639 | 0.0922 | 0.92507 (161.21) | 1.0 | 0.0005 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2137 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | -7.04/-0.3/-13.48 | 428.6 | 616 | 0.0922 | 0.93407 (190.06) | 1.0 | 0.0002 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2138 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -28.3/-1.39/-33.08 | 428.6 | 495 | 0.1136 | 0.996 (91.27) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2139 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -13.21/-0.61/-23.36 | 428.6 | 463 | 0.0992 | 0.96404 (83.0) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2140 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 10.88/0.62/-11.57 | 428.6 | 500 | 0.0971 | 0.81419 (72.4) | 1.0 | 0.0061 | 0.901 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2141 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 4.35/0.26/-15.89 | 428.6 | 462 | 0.0939 | 0.88212 (187.67) | 1.0 | 0.0017 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2142 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -7.63/-0.42/-13.2 | 428.6 | 448 | 0.0987 | 0.94505 (182.04) | 1.0 | 0.0001 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
