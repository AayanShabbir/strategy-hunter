# c07_ma_cross_grid_v1 — engine run 20261023_174736_c07_ma_cross_grid_v1

Hypothesis: MA crossover grid (trend; Hudson & Urquhart 2021 MA family) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/24 pass.** Ledger N at evaluation: 535. PBO (CSCV) across family: 0.687. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 b004aa9de9ebe350d28e9162da7adeef2a14775a434b57a893200dbaae8dc372. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 512 | ALTS|sma_cross(fast=5,slow=50) | 6.66/0.28/-40.5 | 193.2 | 157 | 0.0209 | 0.8022 (73.91) | 1.0 | 0.3826 | 0.897 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 513 | ALTS|sma_cross(fast=5,slow=100) | -2.07/0.18/-47.59 | 193.2 | 116 | 0.0218 | 0.86813 (76.56) | 1.0 | 0.3342 | 0.899 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 514 | ALTS|sma_cross(fast=5,slow=150) | 24.69/0.47/-36.4 | 193.2 | 75 | 0.0226 | 0.66434 (69.77) | 1.0 | 0.4911 | 0.872 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 515 | ALTS|sma_cross(fast=5,slow=200) | 0.5/0.2/-39.58 | 193.2 | 54 | 0.0208 | 0.87213 (63.59) | 1.0 | 0.3442 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 516 | ALTS|sma_cross(fast=10,slow=50) | 30.79/0.52/-33.03 | 193.2 | 128 | 0.0214 | 0.66833 (89.85) | 1.0 | 0.5226 | 0.866 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 517 | ALTS|sma_cross(fast=10,slow=100) | 13.73/0.36/-44.98 | 193.2 | 89 | 0.0219 | 0.77922 (74.22) | 1.0 | 0.43 | 0.887 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 518 | ALTS|sma_cross(fast=10,slow=150) | 7.61/0.29/-38.27 | 193.2 | 54 | 0.0226 | 0.81219 (70.51) | 1.0 | 0.3917 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 519 | ALTS|sma_cross(fast=10,slow=200) | -5.76/0.13/-43.58 | 193.2 | 47 | 0.0206 | 0.90909 (68.81) | 1.0 | 0.3038 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 520 | ALTS|sma_cross(fast=20,slow=50) | 19.28/0.41/-39.76 | 193.2 | 106 | 0.0212 | 0.71229 (72.47) | 1.0 | 0.4587 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 521 | ALTS|sma_cross(fast=20,slow=100) | 7.3/0.29/-46.27 | 193.2 | 69 | 0.0214 | 0.81419 (79.16) | 1.0 | 0.3935 | 0.8965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 522 | ALTS|sma_cross(fast=20,slow=150) | -0.4/0.2/-43.38 | 193.2 | 49 | 0.0216 | 0.86513 (78.68) | 1.0 | 0.342 | 0.908 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 523 | ALTS|sma_cross(fast=20,slow=200) | -12.71/0.03/-42.85 | 193.2 | 38 | 0.0198 | 0.92408 (76.84) | 1.0 | 0.2559 | 0.918 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 524 | BTC_ETH|sma_cross(fast=5,slow=50) | 13.17/0.35/-32.47 | 56.21 | 55 | 0.031 | 0.52448 (19.83) | 1.0 | 0.4214 | 0.888 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 525 | BTC_ETH|sma_cross(fast=5,slow=100) | 39.49/0.68/-22.66 | 56.21 | 31 | 0.0313 | 0.32967 (23.44) | 1.0 | 0.6152 | 0.7275 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 526 | BTC_ETH|sma_cross(fast=5,slow=150) | 18.73/0.41/-30.36 | 56.21 | 20 | 0.0331 | 0.54645 (22.69) | 1.0 | 0.4603 | 0.866 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 527 | BTC_ETH|sma_cross(fast=5,slow=200) | 2.44/0.2/-35.77 | 56.21 | 19 | 0.0327 | 0.71628 (23.18) | 1.0 | 0.3388 | 0.9325 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 528 | BTC_ETH|sma_cross(fast=10,slow=50) | 15.01/0.37/-28.88 | 56.21 | 46 | 0.031 | 0.50849 (21.4) | 1.0 | 0.4364 | 0.866 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 529 | BTC_ETH|sma_cross(fast=10,slow=100) | 19.08/0.43/-28.67 | 56.21 | 26 | 0.0331 | 0.50949 (25.4) | 1.0 | 0.4682 | 0.841 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 530 | BTC_ETH|sma_cross(fast=10,slow=150) | 25.14/0.49/-27.97 | 56.21 | 17 | 0.0366 | 0.48452 (23.95) | 1.0 | 0.5053 | 0.833 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 531 | BTC_ETH|sma_cross(fast=10,slow=200) | 5.32/0.24/-35.36 | 56.21 | 15 | 0.0366 | 0.68631 (22.24) | 1.0 | 0.3602 | 0.9275 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 532 | BTC_ETH|sma_cross(fast=20,slow=50) | 31.39/0.6/-31.31 | 56.21 | 39 | 0.0314 | 0.34565 (23.69) | 1.0 | 0.5702 | 0.805 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 533 | BTC_ETH|sma_cross(fast=20,slow=100) | 25.69/0.51/-30.04 | 56.21 | 22 | 0.0361 | 0.47053 (24.4) | 1.0 | 0.5175 | 0.807 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 534 | BTC_ETH|sma_cross(fast=20,slow=150) | 21.96/0.45/-32.33 | 56.21 | 14 | 0.0327 | 0.51349 (26.15) | 1.0 | 0.4834 | 0.8585 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 535 | BTC_ETH|sma_cross(fast=20,slow=200) | 9.4/0.29/-30.9 | 56.21 | 12 | 0.0301 | 0.61838 (26.67) | 1.0 | 0.3921 | 0.9095 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
