# gen_2310232201_002 — engine run 20261023_220753_gen_2310232201_002

Hypothesis: grammar draw seed=2310232201: supertrend+day_of_week

**0/16 pass.** Ledger N at evaluation: 1022. PBO (CSCV) across family: 0.587. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 0db728858630feb3c7163afc615d82061dbc4ac62059f0bd1a7e1c193850e0f4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1007 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=1) | 7.38/0.39/-15.92 | 234.6 | 558 | 0.0159 | 0.83217 (74.11) | 1.0 | 0.0852 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1008 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=2) | -12.27/-0.4/-16.2 | 234.6 | 562 | 0.0161 | 0.97103 (106.57) | 1.0 | 0.0115 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1009 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=3) | 2.51/0.19/-17.65 | 234.6 | 558 | 0.0158 | 0.88811 (74.86) | 1.0 | 0.0535 | 0.901 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1010 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=4) | 4.32/0.35/-7.86 | 234.6 | 550 | 0.0158 | 0.84216 (65.12) | 1.0 | 0.0722 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1011 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | 11.46/0.54/-14.95 | 234.6 | 598 | 0.0153 | 0.8002 (104.0) | 1.0 | 0.1192 | 0.8845 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1012 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | -25.72/-0.93/-25.72 | 234.6 | 600 | 0.0152 | 0.997 (67.33) | 1.0 | 0.0015 | 0.921 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1013 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 0.41/0.11/-22.3 | 234.6 | 597 | 0.015 | 0.88511 (72.96) | 1.0 | 0.0459 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1014 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | 4.18/0.33/-7.53 | 234.6 | 594 | 0.0152 | 0.86314 (92.04) | 1.0 | 0.0751 | 0.895 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1015 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=1) | 5.85/0.32/-16.7 | 234.6 | 533 | 0.0161 | 0.85415 (99.73) | 1.0 | 0.0743 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1016 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=2) | -10.19/-0.27/-16.23 | 234.6 | 539 | 0.0163 | 0.95604 (89.32) | 1.0 | 0.0184 | 0.9045 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1017 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=3) | 3.18/0.21/-17.95 | 234.6 | 530 | 0.0161 | 0.88012 (123.68) | 1.0 | 0.057 | 0.8995 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1018 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=4) | 1.6/0.16/-9.97 | 234.6 | 518 | 0.0161 | 0.87013 (52.6) | 1.0 | 0.0486 | 0.895 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1019 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | 14.35/0.66/-14.65 | 234.6 | 571 | 0.0154 | 0.77822 (85.59) | 1.0 | 0.1505 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1020 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | -24.57/-0.9/-24.62 | 234.6 | 572 | 0.0156 | 0.995 (99.11) | 1.0 | 0.0017 | 0.9205 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1021 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 0.59/0.12/-24.72 | 234.6 | 570 | 0.0153 | 0.86414 (89.31) | 1.0 | 0.0485 | 0.902 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1022 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | 2.66/0.23/-7.54 | 234.6 | 562 | 0.0153 | 0.85814 (79.52) | 1.0 | 0.0604 | 0.8955 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
