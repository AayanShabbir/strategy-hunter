# gen_2610241212_000 — engine run 20261024_120800_gen_2610241212_000

Hypothesis: grammar draw seed=2610241212: sma_cross+day_of_week

**0/16 pass.** Ledger N at evaluation: 2570. PBO (CSCV) across family: 0.292. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 6943eb8c5a835bcedf0e229ca3604a03a6a48ed05dee23651f759e509e9d9293. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2555 | sectors|sma_cross(fast=20,slow=50)+day_of_week(days=1) | 0.41/0.05/-7.73 | 94.31 | 1036 | 0.0751 | 0.98901 (27.63) | 1.0 | 0.0002 | 0.5015 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2556 | sectors|sma_cross(fast=20,slow=50)+day_of_week(days=2) | -20.08/-1.21/-22.89 | 94.31 | 1023 | 0.0749 | 1.0 (25.94) | 1.0 | 0.0 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2557 | sectors|sma_cross(fast=20,slow=50)+day_of_week(days=3) | -2.57/-0.12/-5.96 | 94.31 | 1010 | 0.0748 | 0.99001 (26.79) | 1.0 | 0.0001 | 0.493 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2558 | sectors|sma_cross(fast=20,slow=50)+day_of_week(days=4) | 3.48/0.27/-8.39 | 94.31 | 1010 | 0.0751 | 0.97802 (26.66) | 1.0 | 0.0007 | 0.496 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2559 | sectors|sma_cross(fast=20,slow=200)+day_of_week(days=1) | 0.59/0.06/-9.07 | 94.31 | 1103 | 0.0719 | 0.97502 (23.44) | 1.0 | 0.0002 | 0.496 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2560 | sectors|sma_cross(fast=20,slow=200)+day_of_week(days=2) | -22.37/-1.26/-23.68 | 94.31 | 1087 | 0.0719 | 1.0 (24.39) | 1.0 | 0.0 | 0.5025 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2561 | sectors|sma_cross(fast=20,slow=200)+day_of_week(days=3) | -4.83/-0.2/-10.72 | 94.31 | 1071 | 0.0715 | 0.998 (24.64) | 1.0 | 0.0 | 0.503 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2562 | sectors|sma_cross(fast=20,slow=200)+day_of_week(days=4) | 2.42/0.18/-8.94 | 94.31 | 1071 | 0.0723 | 0.95804 (23.27) | 1.0 | 0.0005 | 0.502 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2563 | sectors|sma_cross(fast=50,slow=50)+day_of_week(days=1) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (45.7) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2564 | sectors|sma_cross(fast=50,slow=50)+day_of_week(days=2) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (45.7) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2565 | sectors|sma_cross(fast=50,slow=50)+day_of_week(days=3) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (45.7) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2566 | sectors|sma_cross(fast=50,slow=50)+day_of_week(days=4) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (36.43) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2567 | sectors|sma_cross(fast=50,slow=200)+day_of_week(days=1) | 1.25/0.09/-8.73 | 94.31 | 1093 | 0.0713 | 0.96304 (24.08) | 1.0 | 0.0003 | 0.4985 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2568 | sectors|sma_cross(fast=50,slow=200)+day_of_week(days=2) | -21.23/-1.22/-25.14 | 94.31 | 1077 | 0.0714 | 1.0 (24.87) | 1.0 | 0.0 | 0.511 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2569 | sectors|sma_cross(fast=50,slow=200)+day_of_week(days=3) | -5.21/-0.21/-13.79 | 94.31 | 1067 | 0.0709 | 0.99301 (24.36) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2570 | sectors|sma_cross(fast=50,slow=200)+day_of_week(days=4) | 4.43/0.3/-8.99 | 94.31 | 1066 | 0.0717 | 0.95305 (24.83) | 1.0 | 0.001 | 0.492 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
