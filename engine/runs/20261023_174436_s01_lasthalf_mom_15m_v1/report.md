# s01_lasthalf_mom_15m_v1 — engine run 20261023_174436_s01_lasthalf_mom_15m_v1

Hypothesis: Intraday momentum (Gao, Han, Li & Zhou 2018, JFE): when the day's trend is up into 15:30, holding long for the final 30 min (15:30-16:00) on high-beta liquid names beats buy-and-hold after 5 bps/side. Held only in last 30 min via session filter (signal bars 15:15-15:30 ET, filled next open, flat at close). SPY/QQQ excluded: 15m ATR too small to pass cost<=3% of stop.

**0/8 pass.** Ledger N at evaluation: 406. PBO (CSCV) across family: 0.254. Window 2024-09-03..2025-10-22 (pre-vault), OOS from 2025-06-23.
Spec sha256 96549da34ec95124e5f856f9a1edd65b5022c5966604acd44b8399f330f42d6d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 399 | HIBETA|sma_cross(fast=2,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | -4.54/-3.54/-5.15 | -2.96 | 756 | 0.0214 | 0.37562 (-6.05) | 1.0 | 0.0 | 0.6115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 400 | HIBETA|sma_cross(fast=2,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -2.16/-2.82/-2.78 | -2.96 | 371 | 0.021 | 0.32867 (-4.11) | 1.0 | 0.0 | 0.5225 | False | oos_positive, walk_forward, holm, dsr, spa |
| 401 | HIBETA|sma_cross(fast=2,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | 1.09/1.63/-0.47 | -2.96 | 223 | 0.0224 | 0.17083 (-3.29) | 1.0 | 0.0015 | 0.3975 | False | holm, dsr, spa |
| 402 | HIBETA|sma_cross(fast=2,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -0.43/-2.1/-0.53 | -2.96 | 93 | 0.02 | 0.27972 (-2.56) | 1.0 | 0.0 | 0.458 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa |
| 403 | HIBETA|sma_cross(fast=4,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | -3.42/-3.09/-4.38 | -2.96 | 758 | 0.0214 | 0.28472 (-5.81) | 1.0 | 0.0 | 0.5625 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 404 | HIBETA|sma_cross(fast=4,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -1.98/-2.62/-2.81 | -2.96 | 377 | 0.021 | 0.28871 (-4.01) | 1.0 | 0.0 | 0.516 | False | oos_positive, walk_forward, holm, dsr, spa |
| 405 | HIBETA|sma_cross(fast=4,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | 0.69/1.06/-0.49 | -2.96 | 219 | 0.0223 | 0.17682 (-3.42) | 1.0 | 0.0008 | 0.4125 | False | walk_forward, holm, dsr, spa |
| 406 | HIBETA|sma_cross(fast=4,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -0.5/-2.18/-0.63 | -2.96 | 94 | 0.0219 | 0.25774 (-3.12) | 1.0 | 0.0 | 0.4595 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
