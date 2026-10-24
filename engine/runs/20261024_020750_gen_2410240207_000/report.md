# gen_2410240207_000 — engine run 20261024_020750_gen_2410240207_000

Hypothesis: grammar draw seed=2410240207: sma_cross

**0/4 pass.** Ledger N at evaluation: 1502. PBO (CSCV) across family: 0.635. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 e1c0ef1c5144a8c2b2d656a2107e9b165b9a6f65af456c1434d8ff899d5e4ef4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1499 | crypto|sma_cross(fast=10,slow=100) | 25.71/0.61/-43.88 | 428.6 | 1018 | 0.1042 | 0.63437 (63.18) | 1.0 | 0.7166 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1500 | crypto|sma_cross(fast=10,slow=200) | 19.26/0.52/-40.09 | 428.6 | 682 | 0.1043 | 0.75524 (128.44) | 1.0 | 0.6772 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1501 | crypto|sma_cross(fast=20,slow=100) | 23.33/0.57/-42.12 | 428.6 | 793 | 0.1029 | 0.69331 (90.33) | 1.0 | 0.7008 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1502 | crypto|sma_cross(fast=20,slow=200) | 21.23/0.55/-39.12 | 428.6 | 529 | 0.1034 | 0.76124 (185.6) | 1.0 | 0.6893 | 0.906 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
