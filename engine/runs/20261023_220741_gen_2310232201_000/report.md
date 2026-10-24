# gen_2310232201_000 — engine run 20261023_220741_gen_2310232201_000

Hypothesis: grammar draw seed=2310232201: rsi_revert

**0/8 pass.** Ledger N at evaluation: 998. PBO (CSCV) across family: 0.395. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6db8a141afc8b71a8f064c2c6415b60caf288146bb16de8843a5eec6d860aa17. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 991 | crypto_d|rsi_revert(entry=5,exit=70,n=3) | 22.9/1.06/-9.99 | 234.6 | 56 | 0.0127 | 0.76024 (121.35) | 1.0 | 0.4693 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 992 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 2.61/0.46/-3.07 | 234.6 | 4 | 0.0148 | 0.98002 (156.36) | 1.0 | 0.2009 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 993 | crypto_d|rsi_revert(entry=5,exit=80,n=3) | 32.13/1.28/-10.04 | 234.6 | 52 | 0.0139 | 0.64535 (128.22) | 1.0 | 0.5851 | 0.873 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 994 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.98601 (152.1) | 1.0 | 0.1688 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 995 | crypto_d|rsi_revert(entry=20,exit=70,n=3) | 47.68/0.84/-24.91 | 234.6 | 290 | 0.0135 | 0.56044 (78.05) | 1.0 | 0.3703 | 0.835 | False | beats_buy_hold, holm, dsr, spa |
| 996 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 72.94/1.2/-24.27 | 234.6 | 120 | 0.0132 | 0.5025 (79.7) | 1.0 | 0.5423 | 0.837 | False | beats_buy_hold, holm, dsr, spa |
| 997 | crypto_d|rsi_revert(entry=20,exit=80,n=3) | 36.62/0.69/-32.11 | 234.6 | 224 | 0.014 | 0.61738 (99.43) | 1.0 | 0.3046 | 0.8595 | False | beats_buy_hold, holm, dsr, spa |
| 998 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 63.41/0.97/-32.5 | 234.6 | 92 | 0.0134 | 0.53447 (108.57) | 1.0 | 0.4307 | 0.8365 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
