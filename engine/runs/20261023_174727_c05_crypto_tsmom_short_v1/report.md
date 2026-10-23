# c05_crypto_tsmom_short_v1 — engine run 20261023_174727_c05_crypto_tsmom_short_v1

Hypothesis: Short-horizon time-series momentum: hold while close > its 7/14/28-day SMA (1-4 week horizon where Liu & Tsyvinski 2021 find TSMOM in BTC/ETH) on SOL, the alt basket, and BTC+ETH beats buy-and-hold OOS net of 35 bps/side. 5x ATR stop. Strategy Scout crypto submission.

**0/9 pass.** Ledger N at evaluation: 499. PBO (CSCV) across family: 0.653. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 eae14d8ec9b646d00ab65ad2b5c20603c63778e01bb4b5753cf10cab2ececf49. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 491 | SOL|sma_cross(fast=1,slow=7) | 3.78/0.25/-51.44 | 923.45 | 138 | 0.0152 | 0.62637 (122.97) | 1.0 | 0.1591 | 0.897 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 492 | SOL|sma_cross(fast=1,slow=14) | 8.0/0.3/-35.02 | 923.45 | 87 | 0.015 | 0.69031 (222.82) | 1.0 | 0.1753 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 493 | SOL|sma_cross(fast=1,slow=28) | 37.74/0.58/-31.95 | 923.45 | 71 | 0.0162 | 0.58342 (124.71) | 1.0 | 0.2942 | 0.8575 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 494 | ALTS|sma_cross(fast=1,slow=7) | -13.95/0.01/-51.71 | 193.2 | 1044 | 0.0183 | 0.6963 (16.26) | 1.0 | 0.088 | 0.924 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 495 | ALTS|sma_cross(fast=1,slow=14) | 2.88/0.23/-49.52 | 193.2 | 672 | 0.0187 | 0.67632 (40.37) | 1.0 | 0.1512 | 0.9105 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 496 | ALTS|sma_cross(fast=1,slow=28) | 22.05/0.44/-36.46 | 193.2 | 464 | 0.0192 | 0.5994 (52.32) | 1.0 | 0.2336 | 0.871 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 497 | BTC_ETH|sma_cross(fast=1,slow=7) | -26.24/-0.36/-46.71 | 56.21 | 390 | 0.0276 | 0.6953 (-17.13) | 1.0 | 0.0311 | 0.503 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 498 | BTC_ETH|sma_cross(fast=1,slow=14) | 5.1/0.23/-40.98 | 56.21 | 246 | 0.0272 | 0.4006 (-1.34) | 1.0 | 0.1476 | 0.951 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 499 | BTC_ETH|sma_cross(fast=1,slow=28) | 39.53/0.69/-28.78 | 56.21 | 145 | 0.0283 | 0.17782 (10.98) | 1.0 | 0.3502 | 0.7815 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
