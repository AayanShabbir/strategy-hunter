# gen_2310232131_003 — engine run 20261023_210444_gen_2310232131_003

Hypothesis: grammar draw seed=2310232131: supertrend+day_of_week

**0/20 pass.** Ledger N at evaluation: 990. PBO (CSCV) across family: 0.778. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 2d9c6dd75f68c2af6d1ec55fbd0a1a47f3caccb5e03c5b0f3f81ab4bc2870922. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 971 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -22.42/-0.99/-27.47 | 428.6 | 710 | 0.1058 | 0.99101 (64.15) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 972 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | -13.95/-0.6/-23.15 | 428.6 | 660 | 0.0932 | 0.96404 (147.7) | 1.0 | 0.0002 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 973 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 27.59/1.24/-10.54 | 428.6 | 686 | 0.0932 | 0.7043 (190.35) | 1.0 | 0.0466 | 0.884 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 974 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -5.34/-0.16/-22.24 | 428.6 | 639 | 0.0922 | 0.93207 (83.88) | 1.0 | 0.0009 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 975 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | -7.04/-0.3/-13.48 | 428.6 | 616 | 0.0922 | 0.94106 (86.78) | 1.0 | 0.0004 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 976 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -28.3/-1.39/-33.08 | 428.6 | 495 | 0.1136 | 0.999 (90.75) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 977 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -13.21/-0.61/-23.36 | 428.6 | 463 | 0.0992 | 0.96104 (101.82) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 978 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 10.88/0.62/-11.57 | 428.6 | 500 | 0.0971 | 0.83816 (157.61) | 1.0 | 0.0105 | 0.901 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 979 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 4.35/0.26/-15.89 | 428.6 | 462 | 0.0939 | 0.88811 (73.98) | 1.0 | 0.0032 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 980 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -7.63/-0.42/-13.2 | 428.6 | 448 | 0.0987 | 0.94705 (176.6) | 1.0 | 0.0002 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 981 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=0) | -18.39/-0.78/-23.81 | 428.6 | 721 | 0.1047 | 0.96903 (74.99) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 982 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=1) | -18.23/-0.84/-26.93 | 428.6 | 670 | 0.0923 | 0.97802 (135.9) | 1.0 | 0.0001 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 983 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=2) | 33.3/1.41/-10.83 | 428.6 | 686 | 0.0936 | 0.65534 (168.42) | 1.0 | 0.0691 | 0.8795 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 984 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=3) | -7.75/-0.26/-24.61 | 428.6 | 643 | 0.092 | 0.94006 (115.61) | 1.0 | 0.0006 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 985 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=4) | -6.46/-0.26/-12.99 | 428.6 | 627 | 0.0909 | 0.93407 (190.71) | 1.0 | 0.0005 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 986 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=0) | -29.62/-1.42/-35.46 | 428.6 | 515 | 0.1102 | 0.996 (68.52) | 1.0 | 0.0 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 987 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=1) | -16.15/-0.72/-26.68 | 428.6 | 475 | 0.0977 | 0.97403 (191.72) | 1.0 | 0.0001 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 988 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=2) | 10.29/0.61/-12.15 | 428.6 | 505 | 0.0976 | 0.82118 (74.98) | 1.0 | 0.0101 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 989 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=3) | -1.1/0.04/-19.38 | 428.6 | 470 | 0.0939 | 0.93706 (101.54) | 1.0 | 0.0016 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 990 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=4) | -6.16/-0.31/-12.03 | 428.6 | 446 | 0.0973 | 0.93207 (77.43) | 1.0 | 0.0004 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
