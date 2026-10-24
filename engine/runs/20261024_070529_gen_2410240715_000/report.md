# gen_2410240715_000 — engine run 20261024_070529_gen_2410240715_000

Hypothesis: grammar draw seed=2410240715: sma_cross+day_of_week

**0/20 pass.** Ledger N at evaluation: 2082. PBO (CSCV) across family: 0.704. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 1c10ff2f9cfe4eb140587f11047632ffcbc30307b27a1dd1286295dc690259f5. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2063 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=0) | -29.22/-1.21/-36.37 | 428.6 | 506 | 0.1124 | 0.998 (73.8) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2064 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=1) | -10.64/-0.49/-18.55 | 428.6 | 501 | 0.1 | 0.95804 (173.1) | 1.0 | 0.0001 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2065 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=2) | 16.51/0.85/-14.34 | 428.6 | 517 | 0.0981 | 0.78921 (163.72) | 1.0 | 0.012 | 0.8995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2066 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=3) | 0.69/0.11/-16.29 | 428.6 | 505 | 0.0932 | 0.88911 (192.17) | 1.0 | 0.001 | 0.913 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2067 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=4) | -0.64/0.02/-13.4 | 428.6 | 470 | 0.0993 | 0.91409 (91.16) | 1.0 | 0.0008 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2068 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=0) | -36.99/-1.63/-41.64 | 428.6 | 487 | 0.1123 | 1.0 (91.7) | 1.0 | 0.0 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2069 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=1) | -8.99/-0.34/-18.41 | 428.6 | 484 | 0.1014 | 0.96304 (91.42) | 1.0 | 0.0002 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2070 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=2) | 20.66/0.97/-13.21 | 428.6 | 482 | 0.1006 | 0.75125 (160.47) | 1.0 | 0.0176 | 0.8965 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2071 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=3) | -3.52/-0.06/-15.81 | 428.6 | 477 | 0.0933 | 0.93307 (76.19) | 1.0 | 0.0006 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2072 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=4) | 0.21/0.07/-14.86 | 428.6 | 446 | 0.0965 | 0.89311 (90.36) | 1.0 | 0.0009 | 0.9095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2073 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=0) | -29.34/-1.09/-37.73 | 428.6 | 461 | 0.1132 | 0.997 (138.29) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2074 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=1) | -2.5/-0.05/-16.43 | 428.6 | 458 | 0.0993 | 0.92607 (107.64) | 1.0 | 0.0006 | 0.9065 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2075 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=2) | 10.76/0.62/-12.45 | 428.6 | 448 | 0.0977 | 0.83417 (75.51) | 1.0 | 0.0052 | 0.9075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2076 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=3) | 6.56/0.36/-14.3 | 428.6 | 465 | 0.0949 | 0.85315 (112.03) | 1.0 | 0.0026 | 0.909 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2077 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=4) | 9.62/0.57/-11.52 | 428.6 | 452 | 0.0964 | 0.83217 (119.95) | 1.0 | 0.0049 | 0.905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2078 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=0) | -31.93/-1.36/-37.34 | 428.6 | 430 | 0.1123 | 0.998 (174.59) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2079 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=1) | 1.46/0.14/-23.98 | 428.6 | 420 | 0.1002 | 0.91009 (183.11) | 1.0 | 0.0012 | 0.901 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2080 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=2) | 18.74/0.97/-8.05 | 428.6 | 433 | 0.0983 | 0.76024 (197.05) | 1.0 | 0.0153 | 0.8985 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2081 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=3) | -2.8/-0.05/-14.54 | 428.6 | 428 | 0.0956 | 0.93007 (130.43) | 1.0 | 0.0006 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2082 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=4) | 8.6/0.57/-12.09 | 428.6 | 432 | 0.0981 | 0.85714 (189.12) | 1.0 | 0.0053 | 0.906 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
