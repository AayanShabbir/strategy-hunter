# gen_2310232201_003 — engine run 20261023_220757_gen_2310232201_003

Hypothesis: grammar draw seed=2310232201: drop_revert

**0/8 pass.** Ledger N at evaluation: 1030. PBO (CSCV) across family: 0.315. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 3ff324181e849e0d7f49315f02c28eba0a3a48b9899f73ba543cc9c0fb58e906. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1023 | crypto_d|drop_revert(drop=0.05,hold=3,n=1) | 1.02/0.18/-26.82 | 234.6 | 492 | 0.0115 | 0.87512 (87.26) | 1.0 | 0.0674 | 0.8875 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1024 | crypto_d|drop_revert(drop=0.05,hold=3,n=3) | 10.38/0.37/-32.2 | 234.6 | 544 | 0.0126 | 0.81019 (86.43) | 1.0 | 0.1008 | 0.8875 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1025 | crypto_d|drop_revert(drop=0.05,hold=5,n=1) | -28.67/-0.4/-41.04 | 234.6 | 375 | 0.0123 | 0.999 (80.59) | 1.0 | 0.0142 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1026 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | -0.07/0.24/-41.85 | 234.6 | 408 | 0.0136 | 0.89111 (81.86) | 1.0 | 0.0764 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1027 | crypto_d|drop_revert(drop=0.1,hold=3,n=1) | 25.7/1.1/-11.52 | 234.6 | 130 | 0.0089 | 0.66933 (62.49) | 1.0 | 0.3101 | 0.875 | False | beats_buy_hold, holm, dsr, spa |
| 1028 | crypto_d|drop_revert(drop=0.1,hold=3,n=3) | 19.15/0.6/-17.49 | 234.6 | 289 | 0.0105 | 0.74825 (72.08) | 1.0 | 0.1499 | 0.8765 | False | beats_buy_hold, holm, dsr, spa |
| 1029 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.83716 (126.33) | 1.0 | 0.1146 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 1030 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.95105 (107.13) | 1.0 | 0.0459 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
