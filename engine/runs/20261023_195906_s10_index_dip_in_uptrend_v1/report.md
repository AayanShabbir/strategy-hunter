# s10_index_dip_in_uptrend_v1 — engine run 20261023_195906_s10_index_dip_in_uptrend_v1

Hypothesis: Short-horizon index reversal (Lo & MacKinlay 1990 contrarian profits; Nagel 2012 liquidity provision): buying a broad US index ETF after a 3- or 5-day drop of 3% or 5% while above its 200-day SMA, held 5 days, beats buy-and-hold of the same basket OOS after 5 bps/side. Daily index ETFs only (s02/s06 were intraday single stocks; c03/c13 crypto). 5x ATR stop so cost <= 3% of stop.

**0/4 pass.** Ledger N at evaluation: 694. PBO (CSCV) across family: 0.382. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 e16b8f7f9f2baea3722418f5ddc32c05ea3ef69a29d2af0326abf2d790cd6639. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 691 | US_INDEX|drop_revert(drop=0.03,hold=5,n=3)+trend_sma(n=200) | 5.51/0.5/-3.8 | 68.31 | 185 | 0.0119 | 1.0 (29.55) | 1.0 | 0.2636 | 0.4995 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 692 | US_INDEX|drop_revert(drop=0.03,hold=5,n=5)+trend_sma(n=200) | 9.1/0.81/-3.88 | 68.31 | 205 | 0.0126 | 0.99301 (28.51) | 1.0 | 0.4612 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 693 | US_INDEX|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | 3.68/0.72/-0.84 | 68.31 | 50 | 0.011 | 0.999 (30.75) | 1.0 | 0.3664 | 0.4965 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 694 | US_INDEX|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 8.15/1.16/-1.35 | 68.31 | 78 | 0.0111 | 0.999 (30.37) | 1.0 | 0.751 | 0.497 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
