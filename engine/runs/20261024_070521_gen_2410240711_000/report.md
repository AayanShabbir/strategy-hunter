# gen_2410240711_000 — engine run 20261024_070521_gen_2410240711_000

Hypothesis: grammar draw seed=2410240711: sma_cross

**0/4 pass.** Ledger N at evaluation: 2054. PBO (CSCV) across family: 0.754. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d8e606d6bfae93b1cd57d56e3a5f8a5b1abba9cb26a9033450557bbcc4e3971e. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2051 | sectors|sma_cross(fast=20,slow=50) | 11.89/0.51/-8.59 | 50.2 | 243 | 0.0704 | 0.96603 (22.32) | 1.0 | 0.7172 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2052 | sectors|sma_cross(fast=20,slow=100) | 15.48/0.61/-10.18 | 50.2 | 150 | 0.0692 | 0.86613 (22.34) | 1.0 | 0.7711 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2053 | sectors|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.63) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2054 | sectors|sma_cross(fast=50,slow=100) | 13.98/0.57/-11.04 | 50.2 | 116 | 0.075 | 0.92807 (22.92) | 1.0 | 0.7469 | 0.5215 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
