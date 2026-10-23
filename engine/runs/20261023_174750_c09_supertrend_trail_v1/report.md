# c09_supertrend_trail_v1 — engine run 20261023_174750_c09_supertrend_trail_v1

Hypothesis: Supertrend as an ATR trailing exit (ATR 7/10/14 x 2/3/4) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/18 pass.** Ledger N at evaluation: 577. PBO (CSCV) across family: 0.477. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 dac9565cc0b8790658d8c3b1523a9003b742e250ef3af411aa68fba75fbc37ae. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 560 | ALTS|supertrend(atr_n=7,mult=2) | -4.89/0.12/-42.35 | 193.2 | 190 | 0.0206 | 0.88711 (64.3) | 1.0 | 0.3841 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 561 | ALTS|supertrend(atr_n=7,mult=3) | -1.43/0.16/-37.09 | 193.2 | 118 | 0.0222 | 0.89211 (70.89) | 1.0 | 0.4039 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 562 | ALTS|supertrend(atr_n=7,mult=4) | -5.06/0.15/-41.76 | 193.2 | 80 | 0.023 | 0.92607 (74.33) | 1.0 | 0.3979 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 563 | ALTS|supertrend(atr_n=10,mult=2) | -2.0/0.16/-41.88 | 193.2 | 189 | 0.0208 | 0.87612 (70.1) | 1.0 | 0.4035 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 564 | ALTS|supertrend(atr_n=10,mult=3) | -8.59/0.06/-39.37 | 193.2 | 119 | 0.0217 | 0.93606 (70.8) | 1.0 | 0.3486 | 0.9085 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 565 | ALTS|supertrend(atr_n=10,mult=4) | -0.69/0.19/-40.57 | 193.2 | 77 | 0.0236 | 0.84915 (59.96) | 1.0 | 0.4191 | 0.906 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 566 | ALTS|supertrend(atr_n=14,mult=2) | 10.4/0.31/-36.19 | 193.2 | 187 | 0.0208 | 0.77223 (70.68) | 1.0 | 0.4908 | 0.8965 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 567 | ALTS|supertrend(atr_n=14,mult=3) | -6.62/0.08/-37.93 | 193.2 | 117 | 0.022 | 0.94106 (77.01) | 1.0 | 0.3586 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 568 | ALTS|supertrend(atr_n=14,mult=4) | 0.2/0.19/-40.8 | 193.2 | 75 | 0.0236 | 0.86114 (67.52) | 1.0 | 0.4214 | 0.904 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 569 | BTC_ETH|supertrend(atr_n=7,mult=2) | 8.04/0.27/-28.88 | 56.21 | 79 | 0.03 | 0.61139 (16.02) | 1.0 | 0.466 | 0.9105 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 570 | BTC_ETH|supertrend(atr_n=7,mult=3) | 4.72/0.22/-30.66 | 56.21 | 43 | 0.0313 | 0.72228 (22.49) | 1.0 | 0.4348 | 0.92 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 571 | BTC_ETH|supertrend(atr_n=7,mult=4) | 7.4/0.26/-27.05 | 56.21 | 31 | 0.0311 | 0.63137 (22.85) | 1.0 | 0.4608 | 0.909 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 572 | BTC_ETH|supertrend(atr_n=10,mult=2) | 8.27/0.27/-31.54 | 56.21 | 77 | 0.03 | 0.61239 (15.81) | 1.0 | 0.4682 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 573 | BTC_ETH|supertrend(atr_n=10,mult=3) | -5.2/0.05/-31.89 | 56.21 | 44 | 0.0312 | 0.80519 (20.96) | 1.0 | 0.3455 | 0.9685 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 574 | BTC_ETH|supertrend(atr_n=10,mult=4) | 5.99/0.24/-26.34 | 56.21 | 30 | 0.0317 | 0.70529 (24.13) | 1.0 | 0.4477 | 0.923 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 575 | BTC_ETH|supertrend(atr_n=14,mult=2) | 17.89/0.42/-28.28 | 56.21 | 76 | 0.03 | 0.49151 (18.3) | 1.0 | 0.553 | 0.858 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 576 | BTC_ETH|supertrend(atr_n=14,mult=3) | 0.16/0.15/-33.06 | 56.21 | 45 | 0.0306 | 0.76923 (22.19) | 1.0 | 0.3959 | 0.954 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 577 | BTC_ETH|supertrend(atr_n=14,mult=4) | 16.88/0.41/-25.78 | 56.21 | 26 | 0.0311 | 0.58541 (24.35) | 1.0 | 0.5491 | 0.8905 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
