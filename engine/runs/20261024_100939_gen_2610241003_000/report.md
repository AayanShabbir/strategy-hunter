# gen_2610241003_000 — engine run 20261024_100939_gen_2610241003_000

Hypothesis: grammar draw seed=2610241003: sma_cross

**0/4 pass.** Ledger N at evaluation: 2294. PBO (CSCV) across family: 0.855. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 ac1069c7215677c119f8678988d8c94d46e91dd0bfd881346f1c794a516cb844. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2291 | sectors|sma_cross(fast=5,slow=100) | 34.35/0.84/-12.06 | 94.31 | 78 | 0.0566 | 0.5994 (38.7) | 1.0 | 0.7937 | 0.524 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2292 | sectors|sma_cross(fast=5,slow=150) | 38.78/0.91/-12.45 | 94.31 | 49 | 0.0558 | 0.50649 (40.36) | 1.0 | 0.8241 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2293 | sectors|sma_cross(fast=20,slow=100) | 47.23/1.09/-11.15 | 94.31 | 39 | 0.0605 | 0.26474 (40.06) | 1.0 | 0.8903 | 0.5195 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2294 | sectors|sma_cross(fast=20,slow=150) | 40.86/0.93/-13.98 | 94.31 | 32 | 0.0553 | 0.46753 (40.54) | 1.0 | 0.8318 | 0.515 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
