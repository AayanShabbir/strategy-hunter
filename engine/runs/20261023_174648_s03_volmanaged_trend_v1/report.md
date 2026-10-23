# s03_volmanaged_trend_v1 — engine run 20261023_174648_s03_volmanaged_trend_v1

Hypothesis: Volatility-managed exposure (Moreira & Muir 2017, JF) as long/flat: hold the ETF only when price > SMA(slow) AND ATR20/price is below a calm cap; exit in high-vol regimes. Should improve risk-adjusted return and beat buy-and-hold OOS after costs.

**0/27 pass.** Ledger N at evaluation: 441. PBO (CSCV) across family: 0.384. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 59fa3cae9a9a6cb87f93f313abad90f697aa23c4354e0f789e4420f18a0f49c7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 415 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 33.09/1.2/-7.77 | 84.3 | 55 | 0.023 | 0.49451 (33.62) | 1.0 | 0.5823 | 0.518 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 416 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 35.04/1.13/-12.38 | 84.3 | 56 | 0.0205 | 0.45854 (34.28) | 1.0 | 0.532 | 0.529 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 417 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 34.14/0.99/-12.38 | 84.3 | 74 | 0.0193 | 0.45255 (32.78) | 1.0 | 0.4394 | 0.5285 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 418 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 35.83/1.21/-7.47 | 84.3 | 31 | 0.0215 | 0.46853 (35.28) | 1.0 | 0.5853 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 419 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 46.05/1.33/-9.7 | 84.3 | 30 | 0.0191 | 0.25974 (35.19) | 1.0 | 0.6627 | 0.962 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 420 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 54.55/1.35/-9.2 | 84.3 | 41 | 0.015 | 0.17483 (34.69) | 1.0 | 0.6759 | 0.9365 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 421 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 38.06/1.23/-7.58 | 84.3 | 23 | 0.0216 | 0.41958 (34.38) | 1.0 | 0.5999 | 0.5125 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 422 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 42.42/1.18/-9.7 | 84.3 | 19 | 0.0176 | 0.2977 (34.25) | 1.0 | 0.5699 | 0.5205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 423 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 43.51/1.11/-12.05 | 84.3 | 26 | 0.0149 | 0.37962 (35.21) | 1.0 | 0.5191 | 0.505 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 424 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 40 | 0.0215 | 0.91808 (48.46) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 425 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 42.34/1.17/-10.11 | 132.49 | 39 | 0.0179 | 0.62438 (51.97) | 1.0 | 0.5591 | 0.5115 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 426 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 53.33/1.21/-12.4 | 132.49 | 59 | 0.0155 | 0.42857 (49.4) | 1.0 | 0.5897 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 427 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 32 | 0.0215 | 0.91508 (51.86) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 428 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 31.32/0.88/-12.82 | 132.49 | 25 | 0.0171 | 0.78521 (52.12) | 1.0 | 0.3685 | 0.5125 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 429 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 43.2/0.93/-21.52 | 132.49 | 40 | 0.014 | 0.6014 (51.59) | 1.0 | 0.4014 | 0.5235 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 430 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 29 | 0.0215 | 0.93107 (51.21) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 431 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 29.41/0.83/-13.71 | 132.49 | 20 | 0.0172 | 0.7962 (52.32) | 1.0 | 0.3391 | 0.5155 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 432 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 59.04/1.14/-18.88 | 132.49 | 19 | 0.0129 | 0.41059 (50.66) | 1.0 | 0.5441 | 0.5205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 433 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 2.82/0.36/-3.92 | 53.95 | 293 | 0.0222 | 0.998 (23.22) | 1.0 | 0.109 | 0.49 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 434 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 12.12/0.8/-5.15 | 53.95 | 444 | 0.0188 | 0.96703 (22.51) | 1.0 | 0.3156 | 0.501 | False | beats_buy_hold, holm, dsr, spa |
| 435 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 8.9/0.45/-10.9 | 53.95 | 613 | 0.0169 | 0.98302 (21.46) | 1.0 | 0.1427 | 0.507 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 436 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 1.96/0.25/-3.5 | 53.95 | 229 | 0.0219 | 0.999 (23.25) | 1.0 | 0.0769 | 0.4935 | False | beats_buy_hold, holm, dsr, spa |
| 437 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 12.81/0.79/-6.04 | 53.95 | 324 | 0.0181 | 0.92707 (23.48) | 1.0 | 0.3127 | 0.5145 | False | beats_buy_hold, holm, dsr, spa |
| 438 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 7.42/0.36/-13.39 | 53.95 | 427 | 0.016 | 0.98102 (22.64) | 1.0 | 0.1108 | 0.509 | False | beats_buy_hold, holm, dsr, spa |
| 439 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 1.69/0.21/-3.81 | 53.95 | 187 | 0.0217 | 1.0 (23.2) | 1.0 | 0.0693 | 0.492 | False | beats_buy_hold, holm, dsr, spa |
| 440 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 13.51/0.81/-6.21 | 53.95 | 260 | 0.0179 | 0.92308 (23.19) | 1.0 | 0.3256 | 0.5075 | False | beats_buy_hold, holm, dsr, spa |
| 441 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 10.97/0.47/-13.04 | 53.95 | 305 | 0.0157 | 0.94406 (23.01) | 1.0 | 0.1531 | 0.514 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
