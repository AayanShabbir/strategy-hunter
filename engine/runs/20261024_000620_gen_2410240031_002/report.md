# gen_2410240031_002 — engine run 20261024_000620_gen_2410240031_002

Hypothesis: grammar draw seed=2410240031: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 1350. PBO (CSCV) across family: 0.2. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 907f12889d771029a39ad282e60ac71100a5dcc393271e20806c08698f08f0ec. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1347 | semis|sma_cross(fast=20,slow=50)+trend_sma(n=200) | -0.2/-0.09/-0.89 | -38.66 | 6 | 0.0873 | 0.1049 (-20.98) | 1.0 | 0.2986 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1348 | semis|sma_cross(fast=20,slow=150)+trend_sma(n=200) | 0.19/0.1/-0.89 | -38.66 | 3 | 0.0904 | 0.12088 (-20.75) | 1.0 | 0.3819 | 0.297 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1349 | semis|sma_cross(fast=50,slow=50)+trend_sma(n=200) | 0.0/0.0/0.0 | -38.66 | 0 | inf | 0.1029 (-20.95) | 1.0 | 0.0 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1350 | semis|sma_cross(fast=50,slow=150)+trend_sma(n=200) | 0.11/0.06/-0.89 | -38.66 | 3 | 0.0904 | 0.11788 (-20.49) | 1.0 | 0.3658 | 0.2975 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
