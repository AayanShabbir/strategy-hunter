# gen_2410240417_000 — engine run 20261024_041015_gen_2410240417_000

Hypothesis: grammar draw seed=2410240417: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 1754. PBO (CSCV) across family: 0.645. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 6d3cddbb3cdebf73d5e51d79b6f888c1500e70455ef3633f95380d83553db290. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1747 | REAL|rsi_revert(entry=5,exit=60,n=3)+rsi_band(hi=60) | 12.35/1.06/-1.4 | 86.94 | 96 | 0.0463 | 0.96404 (36.94) | 1.0 | 0.5452 | 0.5175 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1748 | REAL|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 1.19/0.57/-0.92 | 86.94 | 9 | 0.041 | 0.98002 (38.75) | 1.0 | 0.2179 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1749 | REAL|rsi_revert(entry=5,exit=80,n=3)+rsi_band(hi=60) | 18.42/1.26/-2.68 | 86.94 | 91 | 0.0459 | 0.90509 (36.62) | 1.0 | 0.7114 | 0.513 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1750 | REAL|rsi_revert(entry=5,exit=80,n=5)+rsi_band(hi=60) | 4.04/0.69/-2.75 | 86.94 | 12 | 0.0455 | 0.96304 (39.02) | 1.0 | 0.2766 | 0.4995 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1751 | REAL|rsi_revert(entry=10,exit=60,n=3)+rsi_band(hi=60) | 23.16/1.34/-4.1 | 86.94 | 217 | 0.0493 | 0.84416 (35.8) | 1.0 | 0.7533 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1752 | REAL|rsi_revert(entry=10,exit=60,n=5)+rsi_band(hi=60) | 7.31/1.21/-1.39 | 86.94 | 52 | 0.0446 | 0.97802 (37.13) | 1.0 | 0.6484 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1753 | REAL|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=60) | 30.98/1.36/-4.48 | 86.94 | 184 | 0.049 | 0.64635 (35.97) | 1.0 | 0.743 | 0.949 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1754 | REAL|rsi_revert(entry=10,exit=80,n=5)+rsi_band(hi=60) | 9.32/0.9/-2.75 | 86.94 | 55 | 0.0472 | 0.98202 (37.76) | 1.0 | 0.4137 | 0.5015 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
