# c12_rsi_revert_v1 — engine run 20261023_174814_c12_rsi_revert_v1

Hypothesis: Short RSI oversold reversion (RSI 2/3 < 5/10/20, exit > 50/70) beats buy-and-hold OOS (reversal, Kozlowski et al. 2021). Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/24 pass.** Ledger N at evaluation: 639. PBO (CSCV) across family: 0.144. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 afd2a0e65fa804cf1f1f404c13482eaa7eb209f320db8945f951c50f9276f425. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 616 | ALTS|rsi_revert(entry=5,exit=50,n=2) | 33.51/0.78/-17.61 | 193.2 | 287 | 0.0162 | 0.56943 (52.66) | 1.0 | 0.3866 | 0.86 | False | beats_buy_hold, holm, dsr, spa |
| 617 | ALTS|rsi_revert(entry=5,exit=50,n=3) | 9.62/0.46/-10.73 | 193.2 | 72 | 0.0157 | 0.84116 (90.93) | 1.0 | 0.2136 | 0.8855 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 618 | ALTS|rsi_revert(entry=5,exit=70,n=2) | 27.13/0.61/-18.87 | 193.2 | 262 | 0.0164 | 0.64236 (74.0) | 1.0 | 0.2969 | 0.8675 | False | beats_buy_hold, holm, dsr, spa |
| 619 | ALTS|rsi_revert(entry=5,exit=70,n=3) | 18.53/0.71/-11.84 | 193.2 | 70 | 0.0158 | 0.74725 (74.35) | 1.0 | 0.3425 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 620 | ALTS|rsi_revert(entry=10,exit=50,n=2) | 12.73/0.35/-17.57 | 193.2 | 493 | 0.0172 | 0.64535 (64.24) | 1.0 | 0.1823 | 0.8775 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 621 | ALTS|rsi_revert(entry=10,exit=50,n=3) | 27.98/0.7/-14.75 | 193.2 | 200 | 0.0159 | 0.65734 (75.44) | 1.0 | 0.3411 | 0.868 | False | beats_buy_hold, holm, dsr, spa |
| 622 | ALTS|rsi_revert(entry=10,exit=70,n=2) | 17.08/0.4/-24.51 | 193.2 | 428 | 0.0174 | 0.64136 (66.11) | 1.0 | 0.2021 | 0.8735 | False | beats_buy_hold, holm, dsr, spa |
| 623 | ALTS|rsi_revert(entry=10,exit=70,n=3) | 41.89/0.8/-19.81 | 193.2 | 178 | 0.016 | 0.56843 (73.32) | 1.0 | 0.4021 | 0.856 | False | beats_buy_hold, holm, dsr, spa |
| 624 | ALTS|rsi_revert(entry=20,exit=50,n=2) | -25.81/-0.29/-42.38 | 193.2 | 830 | 0.0173 | 0.92108 (48.17) | 1.0 | 0.0358 | 0.9175 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 625 | ALTS|rsi_revert(entry=20,exit=50,n=3) | 27.96/0.56/-18.18 | 193.2 | 440 | 0.0168 | 0.58042 (62.87) | 1.0 | 0.272 | 0.863 | False | beats_buy_hold, holm, dsr, spa |
| 626 | ALTS|rsi_revert(entry=20,exit=70,n=2) | -9.04/0.06/-33.47 | 193.2 | 670 | 0.0176 | 0.77522 (40.17) | 1.0 | 0.0946 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 627 | ALTS|rsi_revert(entry=20,exit=70,n=3) | 18.67/0.41/-28.1 | 193.2 | 339 | 0.0171 | 0.62338 (66.61) | 1.0 | 0.2059 | 0.8675 | False | beats_buy_hold, holm, dsr, spa |
| 628 | BTC_ETH|rsi_revert(entry=5,exit=50,n=2) | 28.24/0.74/-16.45 | 56.21 | 99 | 0.0258 | 0.31668 (13.73) | 1.0 | 0.3589 | 0.7355 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 629 | BTC_ETH|rsi_revert(entry=5,exit=50,n=3) | 25.35/0.91/-9.48 | 56.21 | 27 | 0.0242 | 0.4995 (25.3) | 1.0 | 0.4541 | 0.738 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 630 | BTC_ETH|rsi_revert(entry=5,exit=70,n=2) | 34.77/0.76/-16.08 | 56.21 | 91 | 0.0257 | 0.25674 (14.29) | 1.0 | 0.3701 | 0.703 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 631 | BTC_ETH|rsi_revert(entry=5,exit=70,n=3) | 37.85/1.13/-9.51 | 56.21 | 27 | 0.0242 | 0.35065 (25.79) | 1.0 | 0.6126 | 0.6935 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 632 | BTC_ETH|rsi_revert(entry=10,exit=50,n=2) | 12.4/0.36/-24.05 | 56.21 | 176 | 0.0271 | 0.42657 (7.3) | 1.0 | 0.1838 | 0.7995 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 633 | BTC_ETH|rsi_revert(entry=10,exit=50,n=3) | 27.04/0.7/-16.26 | 56.21 | 69 | 0.0249 | 0.38162 (17.15) | 1.0 | 0.3374 | 0.7225 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 634 | BTC_ETH|rsi_revert(entry=10,exit=70,n=2) | 34.81/0.67/-22.53 | 56.21 | 158 | 0.0269 | 0.20779 (8.12) | 1.0 | 0.3269 | 0.701 | False | beats_buy_hold, holm, dsr, spa |
| 635 | BTC_ETH|rsi_revert(entry=10,exit=70,n=3) | 17.33/0.45/-21.29 | 56.21 | 62 | 0.0249 | 0.5035 (18.79) | 1.0 | 0.2217 | 0.7715 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 636 | BTC_ETH|rsi_revert(entry=20,exit=50,n=2) | -8.06/-0.02/-33.15 | 56.21 | 290 | 0.0273 | 0.57942 (-3.31) | 1.0 | 0.0775 | 0.922 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 637 | BTC_ETH|rsi_revert(entry=20,exit=50,n=3) | 35.53/0.73/-24.1 | 56.21 | 156 | 0.0262 | 0.17982 (8.39) | 1.0 | 0.3593 | 0.6945 | False | beats_buy_hold, holm, dsr, spa |
| 638 | BTC_ETH|rsi_revert(entry=20,exit=70,n=2) | 15.86/0.38/-29.86 | 56.21 | 243 | 0.0271 | 0.29171 (-0.02) | 1.0 | 0.1931 | 0.829 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 639 | BTC_ETH|rsi_revert(entry=20,exit=70,n=3) | 27.74/0.55/-33.24 | 56.21 | 130 | 0.0264 | 0.17882 (10.93) | 1.0 | 0.2689 | 0.722 | False | beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
