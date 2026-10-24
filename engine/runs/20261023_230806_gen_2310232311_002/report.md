# gen_2310232311_002 — engine run 20261023_230806_gen_2310232311_002

Hypothesis: grammar draw seed=2310232311: sma_cross

**0/4 pass.** Ledger N at evaluation: 1170. PBO (CSCV) across family: 0.254. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 914dafca32d1d2325f1309d411d3cddc91ffba21c3c4f90ffe9c332065837bc1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1167 | sectors|sma_cross(fast=10,slow=50) | 11.55/0.4/-16.09 | 64.05 | 96 | 0.0573 | 0.87013 (26.24) | 1.0 | 0.1676 | 0.5065 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1168 | sectors|sma_cross(fast=10,slow=100) | -2.03/-0.0/-21.21 | 64.05 | 61 | 0.0522 | 0.995 (28.05) | 1.0 | 0.0488 | 0.5205 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1169 | sectors|sma_cross(fast=20,slow=50) | 9.39/0.33/-14.08 | 64.05 | 82 | 0.0565 | 0.92907 (27.21) | 1.0 | 0.1392 | 0.5145 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1170 | sectors|sma_cross(fast=20,slow=100) | 24.62/0.71/-11.42 | 64.05 | 43 | 0.055 | 0.57043 (28.09) | 1.0 | 0.3327 | 0.513 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
