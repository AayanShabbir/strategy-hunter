# gen_2310232331_000 — engine run 20261023_230824_gen_2310232331_000

Hypothesis: grammar draw seed=2310232331: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 1210. PBO (CSCV) across family: 0.749. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 b3b63b1c2030f6e06aa2eb36ef355ef61ba695d9643e5aa71d9c2533d4cb8c53. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1207 | crypto|sma_cross(fast=5,slow=50)+trend_sma(n=50) | 7.71/0.32/-43.26 | 428.6 | 3073 | 0.1048 | 0.61439 (46.99) | 1.0 | 0.2932 | 0.916 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1208 | crypto|sma_cross(fast=5,slow=200)+trend_sma(n=50) | -3.75/0.07/-35.87 | 428.6 | 2603 | 0.1078 | 0.76424 (131.64) | 1.0 | 0.1984 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1209 | crypto|sma_cross(fast=10,slow=50)+trend_sma(n=50) | 13.0/0.41/-41.74 | 428.6 | 2884 | 0.1049 | 0.60839 (59.58) | 1.0 | 0.3326 | 0.9155 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1210 | crypto|sma_cross(fast=10,slow=200)+trend_sma(n=50) | -10.15/-0.09/-38.91 | 428.6 | 2499 | 0.1076 | 0.82018 (126.75) | 1.0 | 0.1501 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
