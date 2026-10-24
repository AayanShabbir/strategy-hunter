# gen_2310231906_002 — engine run 20261023_200419_gen_2310231906_002

Hypothesis: grammar draw seed=2310231906: rsi_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 734. PBO (CSCV) across family: 0.222. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 bc493fe5ff5e124fb739627d10a61da2b0b4f648b5d9d0faf6bfc30580481723. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 727 | hibeta|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=100) | 7.73/0.34/-8.45 | 809.88 | 126 | 0.0227 | 1.0 (226.05) | 1.0 | 0.053 | 0.5095 | False | beats_buy_hold, holm, dsr, spa |
| 728 | hibeta|rsi_revert(entry=5,exit=70,n=3)+trend_sma(n=100) | 8.79/0.68/-3.64 | 809.88 | 28 | 0.0178 | 0.999 (220.95) | 1.0 | 0.1097 | 0.5095 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 729 | hibeta|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=100) | 11.22/0.43/-9.03 | 809.88 | 136 | 0.022 | 1.0 (219.32) | 1.0 | 0.0722 | 0.5085 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 730 | hibeta|rsi_revert(entry=5,exit=80,n=3)+trend_sma(n=100) | 14.62/0.83/-4.34 | 809.88 | 29 | 0.0175 | 0.999 (223.63) | 1.0 | 0.1754 | 0.508 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 731 | hibeta|rsi_revert(entry=20,exit=70,n=2)+trend_sma(n=100) | 89.71/1.36/-17.51 | 809.88 | 480 | 0.0229 | 0.97502 (212.08) | 1.0 | 0.5592 | 0.5085 | False | beats_buy_hold, holm, dsr, spa |
| 732 | hibeta|rsi_revert(entry=20,exit=70,n=3)+trend_sma(n=100) | 1.67/0.11/-24.07 | 809.88 | 269 | 0.023 | 1.0 (218.98) | 1.0 | 0.0238 | 0.5105 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 733 | hibeta|rsi_revert(entry=20,exit=80,n=2)+trend_sma(n=100) | 65.79/0.98/-21.82 | 809.88 | 457 | 0.0231 | 0.98801 (209.0) | 1.0 | 0.3095 | 0.504 | False | beats_buy_hold, holm, dsr, spa |
| 734 | hibeta|rsi_revert(entry=20,exit=80,n=3)+trend_sma(n=100) | 19.35/0.42/-16.24 | 809.88 | 283 | 0.0234 | 1.0 (213.07) | 1.0 | 0.0731 | 0.507 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
