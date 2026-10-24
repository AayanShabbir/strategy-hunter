# gen_2410240101_000 — engine run 20261024_010730_gen_2410240101_000

Hypothesis: grammar draw seed=2410240101: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1390. PBO (CSCV) across family: 0.163. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 8ce82b86db84a219ff021499c0fc0a1ab5ed9e2477c127bbe711366169a64f98. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1383 | crypto_d|rsi_revert(entry=5,exit=60,n=3) | 16.16/0.84/-10.46 | 234.6 | 56 | 0.0127 | 0.7982 (76.05) | 1.0 | 0.1883 | 0.882 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1384 | crypto_d|rsi_revert(entry=5,exit=60,n=5) | 2.03/0.38/-3.07 | 234.6 | 4 | 0.0148 | 0.98801 (65.83) | 1.0 | 0.0784 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1385 | crypto_d|rsi_revert(entry=5,exit=80,n=3) | 32.13/1.28/-10.04 | 234.6 | 52 | 0.0139 | 0.64735 (143.0) | 1.0 | 0.3876 | 0.873 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1386 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.97502 (48.87) | 1.0 | 0.078 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1387 | crypto_d|rsi_revert(entry=10,exit=60,n=3) | 54.19/1.31/-13.67 | 234.6 | 160 | 0.013 | 0.56244 (112.96) | 1.0 | 0.4005 | 0.847 | False | beats_buy_hold, holm, dsr, spa |
| 1388 | crypto_d|rsi_revert(entry=10,exit=60,n=5) | 22.05/1.11/-5.61 | 234.6 | 31 | 0.0124 | 0.74925 (111.5) | 1.0 | 0.289 | 0.8795 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1389 | crypto_d|rsi_revert(entry=10,exit=80,n=3) | 73.05/1.31/-18.43 | 234.6 | 131 | 0.0134 | 0.51349 (100.7) | 1.0 | 0.4091 | 0.8355 | False | beats_buy_hold, holm, dsr, spa |
| 1390 | crypto_d|rsi_revert(entry=10,exit=80,n=5) | 41.28/1.49/-10.29 | 234.6 | 31 | 0.0124 | 0.6004 (134.34) | 1.0 | 0.4976 | 0.8635 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
