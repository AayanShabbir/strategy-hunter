# gen_2310232101_002 — engine run 20261023_210356_gen_2310232101_002

Hypothesis: grammar draw seed=2310232101: drop_revert

**0/8 pass.** Ledger N at evaluation: 906. PBO (CSCV) across family: 0.818. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 3c32bc2808274182d39345d44ede5aa171b884698c2e0db917e55347241e5579. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 899 | crypto_d|drop_revert(drop=0.05,hold=5,n=1) | -28.67/-0.4/-41.04 | 234.6 | 375 | 0.0123 | 0.995 (88.84) | 1.0 | 0.0327 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 900 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | -0.07/0.24/-41.85 | 234.6 | 408 | 0.0136 | 0.87812 (96.97) | 1.0 | 0.1401 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 901 | crypto_d|drop_revert(drop=0.05,hold=10,n=1) | -38.74/-0.43/-49.88 | 234.6 | 208 | 0.0141 | 1.0 (79.32) | 1.0 | 0.0304 | 0.9275 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 902 | crypto_d|drop_revert(drop=0.05,hold=10,n=3) | 8.47/0.38/-52.22 | 234.6 | 217 | 0.0148 | 0.82218 (85.9) | 1.0 | 0.182 | 0.911 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 903 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.82018 (122.73) | 1.0 | 0.2038 | 0.8865 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 904 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.93506 (93.25) | 1.0 | 0.0908 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 905 | crypto_d|drop_revert(drop=0.1,hold=10,n=1) | -0.44/0.12/-24.88 | 234.6 | 97 | 0.0098 | 0.92507 (60.92) | 1.0 | 0.111 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 906 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 11.7/0.39/-33.6 | 234.6 | 187 | 0.0118 | 0.79421 (96.94) | 1.0 | 0.1832 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
