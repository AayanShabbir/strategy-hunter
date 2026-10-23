# c14_volgated_mom_v1 — engine run 20261023_174831_c14_volgated_mom_v1

Hypothesis: Trend (close > 20/50d SMA) gated by low volatility (ATR% < 4%/6%) and RSI14 regime 50-80/100 (volatility-managed momentum proxy, Barroso & Santa-Clara 2015) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/16 pass.** Ledger N at evaluation: 679. PBO (CSCV) across family: 0.91. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 265cfe48c0ee3763100e7a8725f1eb91fc698f197e3368de7c5dfa0f5b905ed3. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 664 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -5.2/-1.06/-5.55 | 193.2 | 43 | 0.0366 | 0.98701 (45.4) | 1.0 | 0.0 | 0.9035 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 665 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -5.2/-1.06/-5.55 | 193.2 | 40 | 0.0362 | 0.99201 (44.4) | 1.0 | 0.0 | 0.9035 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 666 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 15.29/0.5/-15.5 | 193.2 | 248 | 0.0259 | 0.64236 (59.04) | 1.0 | 0.0011 | 0.8845 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 667 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 13.31/0.44/-15.5 | 193.2 | 238 | 0.0257 | 0.66334 (51.12) | 1.0 | 0.0008 | 0.8845 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 668 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -8.4/-1.55/-8.73 | 193.2 | 47 | 0.0366 | 0.995 (46.2) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 669 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -8.4/-1.55/-8.73 | 193.2 | 44 | 0.0361 | 0.997 (50.14) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 670 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 15.76/0.51/-18.41 | 193.2 | 224 | 0.0253 | 0.65235 (55.95) | 1.0 | 0.0012 | 0.8855 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 671 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 13.77/0.45/-18.41 | 193.2 | 214 | 0.0251 | 0.68631 (77.8) | 1.0 | 0.0009 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 672 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | 2.29/0.15/-14.44 | 56.21 | 84 | 0.0381 | 0.66933 (12.79) | 1.0 | 0.0002 | 0.8835 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 673 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | 1.43/0.12/-14.44 | 56.21 | 77 | 0.0371 | 0.69131 (13.4) | 1.0 | 0.0002 | 0.8845 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 674 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 36.11/0.67/-25.66 | 56.21 | 171 | 0.0299 | 0.16883 (7.08) | 1.0 | 0.0019 | 0.775 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 675 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 43.75/0.76/-25.66 | 56.21 | 154 | 0.0292 | 0.13986 (6.94) | 1.0 | 0.0028 | 0.7295 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 676 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -6.04/-0.14/-18.92 | 56.21 | 81 | 0.0376 | 0.79121 (12.95) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 677 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -6.83/-0.17/-18.92 | 56.21 | 74 | 0.0366 | 0.7952 (12.78) | 1.0 | 0.0 | 0.9205 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 678 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 35.55/0.68/-25.24 | 56.21 | 149 | 0.0309 | 0.18182 (7.54) | 1.0 | 0.0023 | 0.78 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 679 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 43.16/0.77/-25.24 | 56.21 | 132 | 0.03 | 0.16683 (9.71) | 1.0 | 0.0033 | 0.74 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
