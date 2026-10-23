# c13_dip_in_uptrend_v1 — engine run 20261023_174823_c13_dip_in_uptrend_v1

Hypothesis: Buy 1/3/5-day drops of 8%/12% held 2/5 days only above the 100d SMA (dip in uptrend) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/24 pass.** Ledger N at evaluation: 663. PBO (CSCV) across family: 0.764. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 58efafa3b00735e8bc856103a37752c26c2f1d319f42997e886e0a3895cb3caa. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 640 | ALTS|drop_revert(drop=0.08,hold=2,n=1)+trend_sma(n=100) | -6.95/-0.39/-14.72 | 193.2 | 128 | 0.0143 | 0.93706 (90.51) | 1.0 | 0.0053 | 0.905 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 641 | ALTS|drop_revert(drop=0.08,hold=2,n=3)+trend_sma(n=100) | 7.7/0.35/-12.13 | 193.2 | 221 | 0.0158 | 0.78521 (73.44) | 1.0 | 0.0694 | 0.889 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 642 | ALTS|drop_revert(drop=0.08,hold=2,n=5)+trend_sma(n=100) | -17.45/-0.64/-22.81 | 193.2 | 225 | 0.0158 | 0.97403 (72.67) | 1.0 | 0.0015 | 0.9165 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 643 | ALTS|drop_revert(drop=0.08,hold=5,n=1)+trend_sma(n=100) | -4.92/-0.16/-15.28 | 193.2 | 135 | 0.0149 | 0.93407 (89.69) | 1.0 | 0.0136 | 0.9045 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 644 | ALTS|drop_revert(drop=0.08,hold=5,n=3)+trend_sma(n=100) | 14.35/0.47/-19.73 | 193.2 | 224 | 0.0163 | 0.6973 (73.78) | 1.0 | 0.0938 | 0.8865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 645 | ALTS|drop_revert(drop=0.08,hold=5,n=5)+trend_sma(n=100) | 7.98/0.29/-16.52 | 193.2 | 234 | 0.0165 | 0.77123 (60.13) | 1.0 | 0.058 | 0.891 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 646 | ALTS|drop_revert(drop=0.12,hold=2,n=1)+trend_sma(n=100) | 2.37/0.39/-1.59 | 193.2 | 35 | 0.0115 | 0.96503 (49.57) | 1.0 | 0.0365 | 0.8965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 647 | ALTS|drop_revert(drop=0.12,hold=2,n=3)+trend_sma(n=100) | 5.56/0.44/-8.47 | 193.2 | 107 | 0.014 | 0.84016 (60.16) | 1.0 | 0.0871 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 648 | ALTS|drop_revert(drop=0.12,hold=2,n=5)+trend_sma(n=100) | 1.17/0.11/-10.22 | 193.2 | 124 | 0.0147 | 0.87712 (56.99) | 1.0 | 0.0342 | 0.8965 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 649 | ALTS|drop_revert(drop=0.12,hold=5,n=1)+trend_sma(n=100) | 7.56/0.7/-3.38 | 193.2 | 38 | 0.0111 | 0.88911 (133.08) | 1.0 | 0.099 | 0.89 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 650 | ALTS|drop_revert(drop=0.12,hold=5,n=3)+trend_sma(n=100) | 5.76/0.32/-9.77 | 193.2 | 117 | 0.0142 | 0.83317 (78.49) | 1.0 | 0.0598 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 651 | ALTS|drop_revert(drop=0.12,hold=5,n=5)+trend_sma(n=100) | 10.31/0.43/-14.83 | 193.2 | 140 | 0.0149 | 0.74625 (51.17) | 1.0 | 0.0887 | 0.8905 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 652 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=1)+trend_sma(n=100) | -1.64/-0.35/-2.7 | 56.21 | 16 | 0.0194 | 0.85514 (27.81) | 1.0 | 0.0098 | 0.862 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 653 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=3)+trend_sma(n=100) | 4.69/0.4/-8.57 | 56.21 | 47 | 0.023 | 0.72228 (21.92) | 1.0 | 0.0723 | 0.8495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 654 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=5)+trend_sma(n=100) | 2.39/0.19/-5.54 | 56.21 | 51 | 0.0229 | 0.76424 (23.79) | 1.0 | 0.0426 | 0.854 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 655 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=1)+trend_sma(n=100) | -4.61/-0.73/-4.9 | 56.21 | 19 | 0.0195 | 0.86613 (28.19) | 1.0 | 0.0012 | 0.8745 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 656 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=3)+trend_sma(n=100) | 5.21/0.35/-6.48 | 56.21 | 46 | 0.0232 | 0.71528 (21.73) | 1.0 | 0.0656 | 0.846 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 657 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=5)+trend_sma(n=100) | 12.54/0.57/-12.06 | 56.21 | 54 | 0.0238 | 0.62637 (22.02) | 1.0 | 0.1129 | 0.821 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 658 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 56.21 | 4 | 0.0106 | 1.0 (25.72) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 659 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=3)+trend_sma(n=100) | -0.17/-0.04/-2.11 | 56.21 | 15 | 0.0192 | 0.82218 (26.51) | 1.0 | 0.0191 | 0.8595 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 660 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=5)+trend_sma(n=100) | 2.28/0.41/-2.94 | 56.21 | 20 | 0.0211 | 0.7972 (27.54) | 1.0 | 0.0756 | 0.8485 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 661 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=1)+trend_sma(n=100) | -2.35/-0.69/-3.21 | 56.21 | 7 | 0.0074 | 1.0 (32.81) | 1.0 | 0.0001 | 0.8685 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 662 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=3)+trend_sma(n=100) | -3.17/-0.47/-4.64 | 56.21 | 15 | 0.0192 | 0.88112 (29.59) | 1.0 | 0.003 | 0.869 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 663 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=5)+trend_sma(n=100) | -1.57/-0.18/-3.31 | 56.21 | 23 | 0.0195 | 0.85914 (28.63) | 1.0 | 0.0119 | 0.8685 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
