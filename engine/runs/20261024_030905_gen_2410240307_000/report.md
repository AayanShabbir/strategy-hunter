# gen_2410240307_000 — engine run 20261024_030905_gen_2410240307_000

Hypothesis: grammar draw seed=2410240307: sma_cross

**0/4 pass.** Ledger N at evaluation: 1602. PBO (CSCV) across family: 0.736. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 147e15467c1dd35e56c094613d0417fd981bec426f35152d7dd76809f408bcf0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1599 | megacap|sma_cross(fast=5,slow=50) | 99.16/1.47/-12.02 | 214.9 | 191 | 0.0428 | 0.18282 (78.28) | 1.0 | 0.9883 | 0.4985 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 1600 | megacap|sma_cross(fast=5,slow=150) | 91.05/1.36/-16.72 | 214.9 | 92 | 0.0409 | 0.34266 (78.63) | 1.0 | 0.9767 | 0.511 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 1601 | megacap|sma_cross(fast=10,slow=50) | 102.65/1.49/-10.83 | 214.9 | 151 | 0.0446 | 0.14585 (78.64) | 1.0 | 0.9889 | 0.501 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 1602 | megacap|sma_cross(fast=10,slow=150) | 99.98/1.46/-14.43 | 214.9 | 67 | 0.0419 | 0.27273 (79.89) | 1.0 | 0.985 | 0.5145 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
