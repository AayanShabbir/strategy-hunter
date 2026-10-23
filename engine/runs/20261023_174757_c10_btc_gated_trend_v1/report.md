# c10_btc_gated_trend_v1 — engine run 20261023_174757_c10_btc_gated_trend_v1

Hypothesis: Coin trend (close > SMA 10/20/50) only while BTC > its 50/100/200d SMA (BTC leads the crypto market factor, Liu Tsyvinski Wu 2022) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/18 pass.** Ledger N at evaluation: 595. PBO (CSCV) across family: 0.3. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 1b5c39c463148e6c17e1cf5f23ca1e748e60d5c1b49e82317c2f4e4091b8eadd. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 578 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=50) | 32.32/0.57/-41.23 | 193.2 | 583 | 0.0204 | 0.52048 (39.72) | 1.0 | 0.2939 | 0.8595 | False | beats_buy_hold, holm, dsr, spa |
| 579 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=100) | 15.21/0.37/-44.09 | 193.2 | 562 | 0.0207 | 0.55045 (29.46) | 1.0 | 0.2023 | 0.8885 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 580 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=200) | -23.69/-0.18/-60.16 | 193.2 | 561 | 0.0203 | 0.91309 (36.46) | 1.0 | 0.051 | 0.925 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 581 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=50) | 34.33/0.58/-30.76 | 193.2 | 411 | 0.0205 | 0.56444 (62.13) | 1.0 | 0.2985 | 0.8495 | False | beats_buy_hold, holm, dsr, spa |
| 582 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=100) | 17.12/0.39/-37.02 | 193.2 | 372 | 0.021 | 0.66134 (77.0) | 1.0 | 0.2125 | 0.8805 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 583 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=200) | -2.28/0.15/-44.35 | 193.2 | 358 | 0.0205 | 0.78621 (54.57) | 1.0 | 0.1269 | 0.9085 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 584 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=50) | 2.52/0.22/-37.73 | 193.2 | 319 | 0.0205 | 0.78821 (59.72) | 1.0 | 0.1464 | 0.9045 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 585 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=100) | -5.0/0.13/-42.19 | 193.2 | 277 | 0.0213 | 0.82118 (67.49) | 1.0 | 0.1184 | 0.9145 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 586 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=200) | -4.3/0.14/-41.09 | 193.2 | 238 | 0.0206 | 0.83716 (80.01) | 1.0 | 0.1211 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 587 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=50) | 15.97/0.41/-25.85 | 56.21 | 207 | 0.0291 | 0.2977 (0.99) | 1.0 | 0.2136 | 0.8605 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 588 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=100) | 3.74/0.19/-30.62 | 56.21 | 204 | 0.0303 | 0.40759 (-2.89) | 1.0 | 0.136 | 0.9195 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 589 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=200) | -29.31/-0.48/-48.34 | 56.21 | 207 | 0.0302 | 0.87812 (-6.08) | 1.0 | 0.0207 | 0.4905 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 590 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=50) | 21.37/0.47/-25.23 | 56.21 | 148 | 0.0284 | 0.33467 (8.25) | 1.0 | 0.2392 | 0.8425 | False | beats_buy_hold, holm, dsr, spa |
| 591 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=100) | 18.88/0.43/-24.94 | 56.21 | 134 | 0.0291 | 0.37063 (8.96) | 1.0 | 0.2226 | 0.8625 | False | beats_buy_hold, holm, dsr, spa |
| 592 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=200) | 11.58/0.32/-36.18 | 56.21 | 129 | 0.0295 | 0.42458 (6.74) | 1.0 | 0.1798 | 0.9225 | False | beats_buy_hold, holm, dsr, spa |
| 593 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=50) | 36.49/0.67/-24.69 | 56.21 | 103 | 0.0292 | 0.22977 (12.37) | 1.0 | 0.3424 | 0.7865 | False | beats_buy_hold, holm, dsr, spa |
| 594 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=100) | 38.26/0.69/-23.64 | 56.21 | 83 | 0.0302 | 0.22478 (13.48) | 1.0 | 0.3506 | 0.7645 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 595 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=200) | 36.4/0.67/-24.9 | 56.21 | 72 | 0.0312 | 0.28671 (16.99) | 1.0 | 0.341 | 0.778 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
