# gen_2610241004_000 — engine run 20261024_100941_gen_2610241004_000

Hypothesis: grammar draw seed=2610241004: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 2298. PBO (CSCV) across family: 0.409. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 3304fae26b5b213a0041fe4ef4f31a359c3fc3144d9427f3a4010ee21eb583c1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2295 | BROAD|sma_cross(fast=5,slow=50)+relvol(min_ratio=1.0) | 1.59/0.11/-16.71 | 83.36 | 753 | 0.087 | 0.98202 (24.85) | 1.0 | 0.3211 | 0.501 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2296 | BROAD|sma_cross(fast=5,slow=100)+relvol(min_ratio=1.0) | 0.85/0.08/-15.26 | 83.36 | 770 | 0.0875 | 0.99101 (23.17) | 1.0 | 0.3025 | 0.4985 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2297 | BROAD|sma_cross(fast=50,slow=50)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 83.36 | 0 | inf | 1.0 (38.63) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2298 | BROAD|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.0) | 5.83/0.28/-12.75 | 83.36 | 724 | 0.0876 | 0.96004 (24.9) | 1.0 | 0.4317 | 0.4955 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
