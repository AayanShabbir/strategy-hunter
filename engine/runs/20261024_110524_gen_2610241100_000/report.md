# gen_2610241100_000 — engine run 20261024_110524_gen_2610241100_000

Hypothesis: grammar draw seed=2610241100: sma_cross

**0/4 pass.** Ledger N at evaluation: 2386. PBO (CSCV) across family: 0.079. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 7b1beab42092c7f2f756e6a979fb64ef86cb22094b415bc173778f07932c18c1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2383 | crypto|sma_cross(fast=10,slow=50) | 28.53/0.66/-25.53 | 434.62 | 59 | 0.0196 | 0.71828 (139.79) | 1.0 | 0.2377 | 0.9005 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2384 | crypto|sma_cross(fast=10,slow=100) | -7.08/0.04/-32.97 | 434.62 | 39 | 0.0198 | 0.95305 (87.44) | 1.0 | 0.0746 | 0.922 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2385 | crypto|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 434.62 | 0 | inf | 1.0 (311.64) | 1.0 | 0.0 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2386 | crypto|sma_cross(fast=50,slow=100) | 28.38/0.66/-27.28 | 434.62 | 30 | 0.0187 | 0.72727 (92.57) | 1.0 | 0.2408 | 0.895 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
