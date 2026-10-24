# gen_2410240121_003 — engine run 20261024_010809_gen_2410240121_003

Hypothesis: grammar draw seed=2410240121: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 1450. PBO (CSCV) across family: 0.191. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 63106dd357884bbfeee7d1e8cd45ccf4ed5fb554676ddce099dbfae5c3cd2d56. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1447 | crypto|sma_cross(fast=5,slow=100)+relvol(min_ratio=1.0) | -59.26/-3.25/-61.3 | 428.6 | 9289 | 0.1026 | 0.87612 (-30.06) | 1.0 | 0.0001 | 0.931 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1448 | crypto|sma_cross(fast=5,slow=150)+relvol(min_ratio=1.0) | -62.92/-3.64/-64.77 | 428.6 | 9277 | 0.1025 | 0.94406 (19.58) | 1.0 | 0.0 | 0.933 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1449 | crypto|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.0) | -56.49/-2.9/-58.35 | 428.6 | 9172 | 0.1021 | 0.83317 (-27.04) | 1.0 | 0.0 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1450 | crypto|sma_cross(fast=50,slow=150)+relvol(min_ratio=1.0) | -60.41/-3.42/-62.17 | 428.6 | 9119 | 0.1019 | 0.91309 (2.43) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
