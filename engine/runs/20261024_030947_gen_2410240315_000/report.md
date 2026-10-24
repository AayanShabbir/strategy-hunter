# gen_2410240315_000 — engine run 20261024_030947_gen_2410240315_000

Hypothesis: grammar draw seed=2410240315: supertrend+day_of_week

**0/16 pass.** Ledger N at evaluation: 1662. PBO (CSCV) across family: 0.138. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 84811ff60c9f6a105b98b08bd47b3d6db6caffc8255a1c188b9aa9ff654a2e48. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1647 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | -12.8/-0.53/-25.49 | 234.6 | 548 | 0.0158 | 0.95205 (105.21) | 1.0 | 0.003 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1648 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | 6.77/0.37/-13.04 | 234.6 | 531 | 0.0155 | 0.82817 (59.78) | 1.0 | 0.052 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1649 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | -1.68/0.03/-13.1 | 234.6 | 529 | 0.0159 | 0.90809 (100.6) | 1.0 | 0.0202 | 0.901 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1650 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -5.44/-0.14/-27.16 | 234.6 | 523 | 0.0158 | 0.91309 (64.19) | 1.0 | 0.0121 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1651 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | -15.3/-0.66/-23.2 | 234.6 | 596 | 0.0156 | 0.97003 (96.27) | 1.0 | 0.0022 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1652 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | 11.46/0.54/-14.95 | 234.6 | 598 | 0.0153 | 0.8022 (85.03) | 1.0 | 0.0752 | 0.8845 | False | beats_buy_hold, holm, dsr, spa |
| 1653 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | -25.72/-0.93/-25.72 | 234.6 | 600 | 0.0152 | 0.99401 (65.56) | 1.0 | 0.0006 | 0.921 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1654 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 0.41/0.11/-22.3 | 234.6 | 597 | 0.015 | 0.88511 (97.3) | 1.0 | 0.026 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1655 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -10.68/-0.4/-25.51 | 234.6 | 546 | 0.0162 | 0.95105 (90.6) | 1.0 | 0.0053 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1656 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | 5.02/0.31/-13.17 | 234.6 | 530 | 0.0159 | 0.84116 (66.5) | 1.0 | 0.0441 | 0.8895 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1657 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | -3.72/-0.06/-12.46 | 234.6 | 528 | 0.0161 | 0.92408 (113.6) | 1.0 | 0.0164 | 0.9005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1658 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -7.58/-0.24/-27.63 | 234.6 | 518 | 0.0162 | 0.94306 (79.49) | 1.0 | 0.0082 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1659 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -16.8/-0.81/-22.58 | 234.6 | 569 | 0.0156 | 0.98901 (62.8) | 1.0 | 0.0011 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1660 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | 14.35/0.66/-14.65 | 234.6 | 571 | 0.0154 | 0.76823 (92.61) | 1.0 | 0.0981 | 0.8815 | False | beats_buy_hold, holm, dsr, spa |
| 1661 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | -24.57/-0.9/-24.62 | 234.6 | 572 | 0.0156 | 0.99001 (89.57) | 1.0 | 0.0007 | 0.9205 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1662 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 0.59/0.12/-24.72 | 234.6 | 570 | 0.0153 | 0.87313 (73.4) | 1.0 | 0.0278 | 0.902 | False | beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
