# gen_2410240031_000 — engine run 20261024_000615_gen_2410240031_000

Hypothesis: grammar draw seed=2410240031: sma_cross

**0/4 pass.** Ledger N at evaluation: 1342. PBO (CSCV) across family: 0.199. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 151b5d59f9eb1def24295df73946d81feabd88f941e8b9f285858cce12f78c6d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1339 | semis|sma_cross(fast=5,slow=50) | -11.82/-0.44/-20.99 | -38.66 | 186 | 0.0788 | 0.31668 (-20.19) | 1.0 | 0.0 | 0.3555 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1340 | semis|sma_cross(fast=5,slow=100) | 3.56/0.78/-2.66 | -38.66 | 40 | 0.0835 | 0.07792 (-20.15) | 1.0 | 0.0114 | 0.275 | False | min_trades, cost_stop, holm, dsr, spa |
| 1341 | semis|sma_cross(fast=10,slow=50) | -14.34/-0.58/-21.45 | -38.66 | 165 | 0.0808 | 0.37962 (-21.11) | 1.0 | 0.0 | 0.3715 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1342 | semis|sma_cross(fast=10,slow=100) | 3.5/0.8/-2.58 | -38.66 | 36 | 0.0835 | 0.08292 (-20.56) | 1.0 | 0.0129 | 0.2745 | False | min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
