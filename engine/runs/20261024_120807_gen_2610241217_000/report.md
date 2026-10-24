# gen_2610241217_000 — engine run 20261024_120807_gen_2610241217_000

Hypothesis: grammar draw seed=2610241217: sma_cross

**0/4 pass.** Ledger N at evaluation: 2578. PBO (CSCV) across family: 0.47. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 a6622413090cf1709be48630652ffae26eeb06366fcf162eeedce3e4c5414b0d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2575 | sectors|sma_cross(fast=20,slow=50) | 31.85/0.85/-11.34 | 94.31 | 74 | 0.0622 | 0.69331 (39.7) | 1.0 | 0.744 | 0.5155 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2576 | sectors|sma_cross(fast=20,slow=200) | 51.87/1.11/-12.75 | 94.31 | 21 | 0.0547 | 0.24875 (40.43) | 1.0 | 0.8599 | 0.9605 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2577 | sectors|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (36.43) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2578 | sectors|sma_cross(fast=50,slow=200) | 50.29/1.05/-17.37 | 94.31 | 19 | 0.0673 | 0.2997 (40.48) | 1.0 | 0.8385 | 0.5155 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
