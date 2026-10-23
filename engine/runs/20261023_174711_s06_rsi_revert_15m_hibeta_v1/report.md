# s06_rsi_revert_15m_hibeta_v1 — engine run 20261023_174711_s06_rsi_revert_15m_hibeta_v1

Hypothesis: Intraday liquidity-provision reversal (Nagel 2012, RFS; Heston, Korajczyk & Sadka 2010): on high-beta liquid names, buying a 15m RSI(3) washout inside a 15m uptrend (SMA200) between 10:00 and 15:30 ET and exiting on rebound, flat by close, beats buy-and-hold after 5 bps/side. Distinct from s02 (1h megacap) and from intraday trend ideas that died on costs (h11, h16 15m). Stop 8x ATR so cost <= 3% of stop.

**0/4 pass.** Ledger N at evaluation: 458. PBO (CSCV) across family: 1.0. Window 2024-09-03..2025-10-22 (pre-vault), OOS from 2025-06-23.
Spec sha256 a709691b7cf1e97eb6513929d2ac154959e2aa4d6250604bad1c6838796332c8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 455 | HIBETA|rsi_revert(entry=10,exit=50,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.25375 (-2.51) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 456 | HIBETA|rsi_revert(entry=10,exit=70,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.26274 (-2.34) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 457 | HIBETA|rsi_revert(entry=20,exit=50,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.28871 (-2.15) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 458 | HIBETA|rsi_revert(entry=20,exit=70,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.29171 (-2.17) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
