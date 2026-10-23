# s02_reversal_1h_megacap_v1 — engine run 20261023_174443_s02_reversal_1h_megacap_v1

Hypothesis: Short-horizon reversal in liquid large caps (Lehmann 1990; Jegadeesh 1990; intraday liquidity-provision reversal, Nagel 2012): buying 1h oversold RSI(3/5) dips within an uptrend (1h SMA200) and exiting on rebound, flat by close, beats buy-and-hold after costs. Not RSI(2)-daily; 1h bars, session 10:30-15:00 ET.

**0/8 pass.** Ledger N at evaluation: 414. PBO (CSCV) across family: 1.0. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 00a201c3f45f69c49ce04c2cdb91cfae83dda0c73253faf9ad2ce8bcc0cd86b8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 407 | MEGA|rsi_revert(entry=15,exit=50,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97203 (13.23) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 408 | MEGA|rsi_revert(entry=15,exit=50,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98102 (13.2) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 409 | MEGA|rsi_revert(entry=15,exit=70,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97103 (13.42) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 410 | MEGA|rsi_revert(entry=15,exit=70,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.99101 (13.13) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 411 | MEGA|rsi_revert(entry=25,exit=50,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98202 (13.44) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 412 | MEGA|rsi_revert(entry=25,exit=50,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97902 (13.02) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 413 | MEGA|rsi_revert(entry=25,exit=70,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97502 (13.09) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 414 | MEGA|rsi_revert(entry=25,exit=70,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98801 (13.13) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
