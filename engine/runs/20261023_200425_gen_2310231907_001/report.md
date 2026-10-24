# gen_2310231907_001 — engine run 20261023_200425_gen_2310231907_001

Hypothesis: grammar draw seed=2310231907: rsi_revert

**0/8 pass.** Ledger N at evaluation: 750. PBO (CSCV) across family: 0.892. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 d7c7b7acb88452bbe41bcd5b426d03f8e113c8c2096d7434a12f6e4bea94fd43. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 743 | crypto_d|rsi_revert(entry=5,exit=70,n=2) | 49.4/1.2/-13.0 | 268.18 | 177 | 0.0134 | 0.54046 (81.34) | 1.0 | 0.5469 | 0.838 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 744 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 3.23/0.46/-3.83 | 268.18 | 4 | 0.0148 | 0.95804 (165.9) | 1.0 | 0.2042 | 0.8875 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 745 | crypto_d|rsi_revert(entry=5,exit=80,n=2) | 33.77/0.8/-19.99 | 268.18 | 163 | 0.0137 | 0.61239 (98.34) | 1.0 | 0.3535 | 0.8565 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 746 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 3.09/0.32/-8.84 | 268.18 | 4 | 0.0148 | 0.96404 (42.84) | 1.0 | 0.1715 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 747 | crypto_d|rsi_revert(entry=20,exit=70,n=2) | 9.31/0.35/-25.07 | 268.18 | 438 | 0.0151 | 0.77123 (79.1) | 1.0 | 0.1809 | 0.8785 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 748 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 59.81/1.09/-26.28 | 268.18 | 94 | 0.0141 | 0.52248 (80.48) | 1.0 | 0.492 | 0.8385 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 749 | crypto_d|rsi_revert(entry=20,exit=80,n=2) | 27.63/0.6/-25.3 | 268.18 | 368 | 0.0154 | 0.62438 (67.14) | 1.0 | 0.2681 | 0.853 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 750 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 69.35/1.04/-33.78 | 268.18 | 73 | 0.0155 | 0.47253 (55.65) | 1.0 | 0.4673 | 0.811 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
