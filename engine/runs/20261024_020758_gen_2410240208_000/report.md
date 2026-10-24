# gen_2410240208_000 — engine run 20261024_020758_gen_2410240208_000

Hypothesis: grammar draw seed=2410240208: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1510. PBO (CSCV) across family: 0.561. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 c1e36a313d2dfd35f4f6d52d5f28de41ec731d6acf7b6d81e6f4c87d5565eb1a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1503 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+relvol(min_ratio=1.2) | -18.73/-0.71/-26.21 | 268.18 | 375 | 0.0122 | 0.97303 (114.3) | 1.0 | 0.0012 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1504 | crypto_d|drop_revert(drop=0.05,hold=5,n=3)+relvol(min_ratio=1.2) | -4.66/-0.04/-23.27 | 268.18 | 459 | 0.0133 | 0.89111 (73.44) | 1.0 | 0.0129 | 0.9015 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1505 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.2) | -25.47/-0.79/-29.27 | 268.18 | 486 | 0.0128 | 0.98801 (122.18) | 1.0 | 0.0007 | 0.912 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1506 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.2) | -8.26/-0.12/-31.02 | 268.18 | 601 | 0.0139 | 0.89111 (134.18) | 1.0 | 0.01 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1507 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.2) | 2.21/0.6/-2.07 | 268.18 | 27 | 0.0074 | 0.92807 (48.08) | 1.0 | 0.0504 | 0.8875 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1508 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+relvol(min_ratio=1.2) | -1.65/-0.03/-9.6 | 268.18 | 90 | 0.0095 | 0.89411 (142.71) | 1.0 | 0.0132 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1509 | crypto_d|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.2) | -6.23/-0.79/-8.67 | 268.18 | 38 | 0.0077 | 0.96803 (179.55) | 1.0 | 0.0 | 0.8955 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1510 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.2) | 7.77/0.41/-15.72 | 268.18 | 127 | 0.0095 | 0.7972 (140.14) | 1.0 | 0.056 | 0.8835 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
