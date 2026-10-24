# s07_country_tsmom_breakout_v1 — engine run 20261023_195853_s07_country_tsmom_breakout_v1

Hypothesis: Country-index time-series momentum (Asness, Moskowitz & Pedersen 2013 JF 'Value and Momentum Everywhere'; Moskowitz, Ooi & Pedersen 2012): long a single-country ETF after a close above its prior 6- or 12-month high, flat on a 1- or 3-month low, beats buy-and-hold of the same basket OOS after 5 bps/side. Country ETFs are a new universe (s04 tested this rule on MEGA/SECTORS; s05 tested SMA trend on EEM/EFA). Pre-registered 2026-10-23 before results. 4x ATR stop.

**0/4 pass.** Ledger N at evaluation: 683. PBO (CSCV) across family: 0.684. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b6f151fda3c82cde92218aae0d9abb50ede1c8482761aac125b84c6fa312eebe. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 680 | COUNTRIES|donchian(entry_n=126,exit_n=21) | 3.28/0.21/-6.68 | 64.42 | 102 | 0.0199 | 0.996 (28.36) | 1.0 | 0.4808 | 0.5035 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 681 | COUNTRIES|donchian(entry_n=126,exit_n=63) | 5.16/0.27/-9.18 | 64.42 | 56 | 0.0173 | 1.0 (28.69) | 1.0 | 0.5242 | 0.508 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 682 | COUNTRIES|donchian(entry_n=252,exit_n=21) | 1.11/0.1/-6.57 | 64.42 | 75 | 0.0202 | 0.999 (28.84) | 1.0 | 0.4058 | 0.5035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 683 | COUNTRIES|donchian(entry_n=252,exit_n=63) | 2.09/0.15/-8.46 | 64.42 | 43 | 0.0191 | 0.998 (29.05) | 1.0 | 0.4415 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
