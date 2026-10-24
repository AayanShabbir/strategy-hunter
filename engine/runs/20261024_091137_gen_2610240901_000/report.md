# gen_2610240901_000 — engine run 20261024_091137_gen_2610240901_000

Hypothesis: grammar draw seed=2610240901: sma_cross

**0/4 pass.** Ledger N at evaluation: 2194. PBO (CSCV) across family: 0.798. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 277b14e348f6fe158156d003c73c64641fde514b21120fb5e37a1fbcb348395d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2191 | crypto|sma_cross(fast=5,slow=50) | 23.53/0.59/-26.67 | 434.62 | 71 | 0.019 | 0.77323 (155.02) | 1.0 | 0.4452 | 0.9025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2192 | crypto|sma_cross(fast=5,slow=200) | 7.15/0.31/-24.64 | 434.62 | 23 | 0.0205 | 0.85315 (227.64) | 1.0 | 0.3189 | 0.9085 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2193 | crypto|sma_cross(fast=20,slow=50) | 29.11/0.67/-23.71 | 434.62 | 50 | 0.0202 | 0.77822 (201.97) | 1.0 | 0.486 | 0.903 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2194 | crypto|sma_cross(fast=20,slow=200) | 4.8/0.26/-21.46 | 434.62 | 15 | 0.0209 | 0.82218 (92.36) | 1.0 | 0.2997 | 0.9135 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
