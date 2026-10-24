# gen_2410240101_001 — engine run 20261024_010736_gen_2410240101_001

Hypothesis: grammar draw seed=2410240101: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1398. PBO (CSCV) across family: 0.83. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 ba571775ccf9564e7ed7a2a6b61a3dcfbec9af31f86b1362c46e993bfff66caf. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1391 | crypto_d|rsi_revert(entry=5,exit=70,n=2) | 64.66/1.37/-15.7 | 234.6 | 223 | 0.0132 | 0.54346 (102.89) | 1.0 | 0.4977 | 0.8365 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1392 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 2.61/0.46/-3.07 | 234.6 | 4 | 0.0148 | 0.98302 (60.43) | 1.0 | 0.1198 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1393 | crypto_d|rsi_revert(entry=5,exit=80,n=2) | 57.4/1.13/-17.19 | 234.6 | 208 | 0.0132 | 0.53447 (84.85) | 1.0 | 0.3739 | 0.843 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1394 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.98901 (155.65) | 1.0 | 0.1003 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1395 | crypto_d|rsi_revert(entry=20,exit=70,n=2) | 10.84/0.38/-29.74 | 234.6 | 563 | 0.0138 | 0.78721 (67.13) | 1.0 | 0.1125 | 0.884 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1396 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 72.94/1.2/-24.27 | 234.6 | 120 | 0.0132 | 0.52947 (107.75) | 1.0 | 0.4114 | 0.837 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1397 | crypto_d|rsi_revert(entry=20,exit=80,n=2) | 29.46/0.61/-29.15 | 234.6 | 477 | 0.014 | 0.65435 (71.66) | 1.0 | 0.1745 | 0.864 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1398 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 63.41/0.97/-32.5 | 234.6 | 92 | 0.0134 | 0.53447 (94.02) | 1.0 | 0.3102 | 0.8365 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
