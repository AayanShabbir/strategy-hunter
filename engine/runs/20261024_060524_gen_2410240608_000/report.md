# gen_2410240608_000 — engine run 20261024_060524_gen_2410240608_000

Hypothesis: grammar draw seed=2410240608: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1958. PBO (CSCV) across family: 0.461. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 76ced2f1c187bb2801d1ea7dffff803290951f8c22bfdb2af88602f876464c0b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1951 | sectors|rsi_revert(entry=10,exit=60,n=2) | 15.83/0.8/-5.08 | 50.2 | 993 | 0.0698 | 0.71329 (19.45) | 1.0 | 0.719 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1952 | sectors|rsi_revert(entry=10,exit=60,n=5) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0631 | 0.997 (23.0) | 1.0 | 0.5832 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1953 | sectors|rsi_revert(entry=10,exit=70,n=2) | 21.31/0.99/-5.61 | 50.2 | 941 | 0.0701 | 0.34266 (19.15) | 1.0 | 0.8308 | 0.9455 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1954 | sectors|rsi_revert(entry=10,exit=70,n=5) | 6.29/0.96/-1.66 | 50.2 | 79 | 0.0631 | 0.99101 (23.72) | 1.0 | 0.7811 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1955 | sectors|rsi_revert(entry=20,exit=60,n=2) | 16.85/0.73/-8.14 | 50.2 | 1652 | 0.0701 | 0.45854 (16.32) | 1.0 | 0.6469 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1956 | sectors|rsi_revert(entry=20,exit=60,n=5) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0656 | 0.44755 (21.9) | 1.0 | 0.8857 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1957 | sectors|rsi_revert(entry=20,exit=70,n=2) | 22.98/0.91/-9.13 | 50.2 | 1505 | 0.0703 | 0.16484 (17.06) | 1.0 | 0.764 | 0.965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1958 | sectors|rsi_revert(entry=20,exit=70,n=5) | 24.67/1.02/-7.08 | 50.2 | 312 | 0.0674 | 0.32567 (22.48) | 1.0 | 0.8322 | 0.9265 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
