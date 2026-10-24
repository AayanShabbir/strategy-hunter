# gen_2410240319_000 — engine run 20261024_031001_gen_2410240319_000

Hypothesis: grammar draw seed=2410240319: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 1694. PBO (CSCV) across family: 0.045. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 8877a526da32d07ba801543201aae5e2a5542577f6d1084faf34bf0fc8b079f8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1691 | crypto|sma_cross(fast=5,slow=100)+trend_sma(n=200) | 14.11/0.44/-37.52 | 428.6 | 1585 | 0.106 | 0.70629 (122.21) | 1.0 | 0.5015 | 0.915 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1692 | crypto|sma_cross(fast=5,slow=150)+trend_sma(n=200) | 0.56/0.19/-38.36 | 428.6 | 1478 | 0.1041 | 0.81219 (54.02) | 1.0 | 0.3821 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1693 | crypto|sma_cross(fast=20,slow=100)+trend_sma(n=200) | 7.34/0.31/-35.27 | 428.6 | 1320 | 0.1041 | 0.77023 (134.72) | 1.0 | 0.4404 | 0.9165 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1694 | crypto|sma_cross(fast=20,slow=150)+trend_sma(n=200) | 15.74/0.47/-34.13 | 428.6 | 1240 | 0.1026 | 0.70629 (73.99) | 1.0 | 0.5143 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
