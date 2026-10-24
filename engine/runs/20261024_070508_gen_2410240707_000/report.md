# gen_2410240707_000 — engine run 20261024_070508_gen_2410240707_000

Hypothesis: grammar draw seed=2410240707: sma_cross

**0/4 pass.** Ledger N at evaluation: 2030. PBO (CSCV) across family: 0.785. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 46909b500375b21c77b36c9770bcb3d177d3b8a6a69965d35b9629cc7b8cecb9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027 | crypto_d|sma_cross(fast=20,slow=50) | 15.82/0.45/-31.97 | 234.6 | 89 | 0.0168 | 0.79321 (86.88) | 1.0 | 0.3143 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2028 | crypto_d|sma_cross(fast=20,slow=200) | -8.3/0.06/-33.75 | 234.6 | 29 | 0.0157 | 0.90609 (114.05) | 1.0 | 0.169 | 0.9155 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2029 | crypto_d|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (31.54) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2030 | crypto_d|sma_cross(fast=50,slow=200) | -11.26/-0.0/-38.28 | 234.6 | 24 | 0.0165 | 0.94406 (72.9) | 1.0 | 0.1518 | 0.9165 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
