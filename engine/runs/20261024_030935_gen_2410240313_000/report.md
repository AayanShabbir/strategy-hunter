# gen_2410240313_000 — engine run 20261024_030935_gen_2410240313_000

Hypothesis: grammar draw seed=2410240313: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 1638. PBO (CSCV) across family: 0.5. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 f8887bc14aee91c95ee5bd7c13b852358c8beb34b3628de6c96a3cd803774170. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1635 | crypto|sma_cross(fast=20,slow=150)+rsi_band(hi=80) | 9.9/0.36/-37.69 | 428.6 | 928 | 0.0972 | 0.78721 (129.44) | 1.0 | 0.2892 | 0.9185 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1636 | crypto|sma_cross(fast=20,slow=200)+rsi_band(hi=80) | 13.9/0.43/-38.8 | 428.6 | 817 | 0.1002 | 0.77922 (150.75) | 1.0 | 0.3175 | 0.9125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1637 | crypto|sma_cross(fast=50,slow=150)+rsi_band(hi=80) | 34.85/0.75/-35.56 | 428.6 | 728 | 0.0996 | 0.63237 (143.97) | 1.0 | 0.462 | 0.893 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1638 | crypto|sma_cross(fast=50,slow=200)+rsi_band(hi=80) | 42.1/0.87/-34.57 | 428.6 | 623 | 0.1001 | 0.61738 (169.75) | 1.0 | 0.5192 | 0.882 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
