# s04_52wk_high_v1 — engine run 20261023_174700_s04_52wk_high_v1

Hypothesis: 52-week-high proximity (George & Hwang 2004, JF): anchoring makes investors under-react near the 52w high; buying a close above the prior 252-day high (above SMA200) and exiting on an N-day low beats buy-and-hold after costs.

**0/9 pass.** Ledger N at evaluation: 450. PBO (CSCV) across family: 0.039. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 95be418d78064159d37ec80e9bfb633ef17dd280ccf5b8a176f42938ee7105b0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 442 | MEGA|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 39.98/1.27/-9.05 | 287.89 | 180 | 0.0117 | 1.0 (101.45) | 1.0 | 0.5771 | 0.5025 | False | beats_buy_hold, holm, dsr, spa |
| 443 | MEGA|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 60.37/1.46/-12.88 | 287.89 | 108 | 0.0111 | 0.95704 (99.39) | 1.0 | 0.6958 | 0.51 | False | beats_buy_hold, holm, dsr, spa |
| 444 | MEGA|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 69.44/1.4/-16.22 | 287.89 | 212 | 0.0097 | 0.85115 (100.36) | 1.0 | 0.657 | 0.5055 | False | beats_buy_hold, holm, dsr, spa |
| 445 | SECTORS|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 9.4/0.84/-3.23 | 56.34 | 155 | 0.0196 | 0.999 (25.18) | 1.0 | 0.2967 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 446 | SECTORS|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 8.89/0.6/-6.3 | 56.34 | 135 | 0.0177 | 1.0 (25.46) | 1.0 | 0.1724 | 0.5095 | False | beats_buy_hold, holm, dsr, spa |
| 447 | SECTORS|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 12.98/0.71/-7.5 | 56.34 | 163 | 0.015 | 0.98701 (25.23) | 1.0 | 0.2248 | 0.5085 | False | beats_buy_hold, holm, dsr, spa |
| 448 | BROAD|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 5.23/0.51/-4.07 | 64.52 | 390 | 0.0142 | 1.0 (28.58) | 1.0 | 0.1347 | 0.5055 | False | beats_buy_hold, holm, dsr, spa |
| 449 | BROAD|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 8.71/0.62/-6.75 | 64.52 | 297 | 0.0133 | 1.0 (28.5) | 1.0 | 0.1773 | 0.512 | False | beats_buy_hold, holm, dsr, spa |
| 450 | BROAD|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 9.64/0.55/-9.18 | 64.52 | 486 | 0.0123 | 1.0 (27.98) | 1.0 | 0.1524 | 0.5075 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
