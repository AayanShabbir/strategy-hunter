# c08_donchian_grid_v1 — engine run 20261023_174743_c08_donchian_grid_v1

Hypothesis: Donchian channel breakout grid beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/24 pass.** Ledger N at evaluation: 559. PBO (CSCV) across family: 0.821. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 fe617f96081f31b59c5490062e2f17a1a52e8dd0b8b455a6a5b50673b7d74054. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 536 | ALTS|donchian(entry_n=10,exit_n=5) | 85.77/0.63/-41.94 | 193.2 | 228 | 0.0204 | 0.44456 (75.63) | 1.0 | 0.5087 | 0.9355 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 537 | ALTS|donchian(entry_n=10,exit_n=10) | 71.02/0.59/-49.18 | 193.2 | 191 | 0.0205 | 0.46853 (66.74) | 1.0 | 0.4755 | 0.964 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 538 | ALTS|donchian(entry_n=10,exit_n=20) | 90.56/0.66/-53.98 | 193.2 | 135 | 0.0196 | 0.44655 (82.21) | 1.0 | 0.531 | 0.9695 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 539 | ALTS|donchian(entry_n=20,exit_n=5) | 7.97/0.27/-29.0 | 193.2 | 147 | 0.0229 | 0.80519 (67.87) | 1.0 | 0.3075 | 0.889 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 540 | ALTS|donchian(entry_n=20,exit_n=10) | -2.08/0.13/-38.54 | 193.2 | 129 | 0.023 | 0.88511 (75.87) | 1.0 | 0.2403 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 541 | ALTS|donchian(entry_n=20,exit_n=20) | 11.19/0.33/-42.24 | 193.2 | 94 | 0.0225 | 0.78821 (66.43) | 1.0 | 0.3375 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 542 | ALTS|donchian(entry_n=30,exit_n=5) | 7.68/0.27/-27.46 | 193.2 | 123 | 0.0235 | 0.81918 (70.52) | 1.0 | 0.3049 | 0.8915 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 543 | ALTS|donchian(entry_n=30,exit_n=10) | 2.39/0.19/-35.16 | 193.2 | 108 | 0.0235 | 0.85415 (63.3) | 1.0 | 0.2664 | 0.8995 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 544 | ALTS|donchian(entry_n=30,exit_n=20) | 15.82/0.38/-35.78 | 193.2 | 83 | 0.0236 | 0.76124 (78.06) | 1.0 | 0.3634 | 0.888 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 545 | ALTS|donchian(entry_n=55,exit_n=5) | 10.13/0.32/-35.07 | 193.2 | 85 | 0.024 | 0.82118 (88.48) | 1.0 | 0.332 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 546 | ALTS|donchian(entry_n=55,exit_n=10) | 8.73/0.28/-41.93 | 193.2 | 76 | 0.0242 | 0.84116 (85.3) | 1.0 | 0.3155 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 547 | ALTS|donchian(entry_n=55,exit_n=20) | 19.27/0.42/-40.35 | 193.2 | 62 | 0.0243 | 0.68531 (78.49) | 1.0 | 0.3906 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 548 | BTC_ETH|donchian(entry_n=10,exit_n=5) | 21.51/0.48/-25.3 | 56.21 | 87 | 0.0303 | 0.41359 (16.12) | 1.0 | 0.4207 | 0.8435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 549 | BTC_ETH|donchian(entry_n=10,exit_n=10) | 19.21/0.43/-25.24 | 56.21 | 66 | 0.0301 | 0.46953 (18.21) | 1.0 | 0.3904 | 0.873 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 550 | BTC_ETH|donchian(entry_n=10,exit_n=20) | 22.07/0.45/-34.3 | 56.21 | 48 | 0.0273 | 0.46254 (20.52) | 1.0 | 0.4011 | 0.8875 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 551 | BTC_ETH|donchian(entry_n=20,exit_n=5) | 0.67/0.12/-21.31 | 56.21 | 61 | 0.0313 | 0.72328 (17.07) | 1.0 | 0.2342 | 0.9065 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 552 | BTC_ETH|donchian(entry_n=20,exit_n=10) | -0.24/0.12/-24.85 | 56.21 | 48 | 0.0312 | 0.71728 (17.85) | 1.0 | 0.2345 | 0.914 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 553 | BTC_ETH|donchian(entry_n=20,exit_n=20) | 19.32/0.44/-27.22 | 56.21 | 34 | 0.0309 | 0.5015 (21.53) | 1.0 | 0.3962 | 0.857 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 554 | BTC_ETH|donchian(entry_n=30,exit_n=5) | 7.09/0.27/-16.44 | 56.21 | 52 | 0.0316 | 0.67632 (21.54) | 1.0 | 0.3056 | 0.871 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 555 | BTC_ETH|donchian(entry_n=30,exit_n=10) | 11.43/0.34/-19.28 | 56.21 | 41 | 0.0316 | 0.61538 (21.66) | 1.0 | 0.3443 | 0.8725 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 556 | BTC_ETH|donchian(entry_n=30,exit_n=20) | 26.93/0.57/-21.98 | 56.21 | 30 | 0.0316 | 0.40659 (24.44) | 1.0 | 0.4736 | 0.8285 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 557 | BTC_ETH|donchian(entry_n=55,exit_n=5) | 19.35/0.57/-14.87 | 56.21 | 36 | 0.0305 | 0.52148 (20.86) | 1.0 | 0.4693 | 0.825 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 558 | BTC_ETH|donchian(entry_n=55,exit_n=10) | 34.69/0.78/-15.5 | 56.21 | 28 | 0.0305 | 0.38561 (24.24) | 1.0 | 0.5945 | 0.761 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 559 | BTC_ETH|donchian(entry_n=55,exit_n=20) | 41.64/0.84/-15.22 | 56.21 | 24 | 0.0305 | 0.3017 (23.12) | 1.0 | 0.6317 | 0.7325 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
