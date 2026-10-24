# gen_2410240101_003 — engine run 20261024_010743_gen_2410240101_003

Hypothesis: grammar draw seed=2410240101: rsi_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1414. PBO (CSCV) across family: 0.163. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 9da2696f0adec043aff5e1ce208759d6b6dda5ee9c7024580790e8d9f94cb72e. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1407 | crypto_d|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=100) | 8.92/0.58/-10.1 | 234.6 | 83 | 0.0143 | 0.85315 (125.08) | 1.0 | 0.0138 | 0.889 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1408 | crypto_d|rsi_revert(entry=5,exit=70,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1409 | crypto_d|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=100) | 8.93/0.54/-10.1 | 234.6 | 95 | 0.0143 | 0.82118 (60.34) | 1.0 | 0.012 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1410 | crypto_d|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1411 | crypto_d|rsi_revert(entry=10,exit=70,n=2)+trend_sma(n=100) | -0.29/0.07/-11.62 | 234.6 | 158 | 0.016 | 0.91808 (74.07) | 1.0 | 0.0024 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1412 | crypto_d|rsi_revert(entry=10,exit=70,n=5)+trend_sma(n=100) | 5.31/2.08/-0.34 | 234.6 | 6 | 0.02 | 0.98002 (153.59) | 1.0 | 0.2273 | 0.8925 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1413 | crypto_d|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=100) | 3.03/0.21/-11.38 | 234.6 | 172 | 0.0161 | 0.88511 (82.82) | 1.0 | 0.0039 | 0.896 | False | beats_buy_hold, holm, dsr, spa |
| 1414 | crypto_d|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=100) | 3.4/0.78/-5.78 | 234.6 | 13 | 0.0187 | 0.97802 (46.98) | 1.0 | 0.0224 | 0.8945 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
