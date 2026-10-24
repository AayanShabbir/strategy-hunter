# gen_2410240011_003 — engine run 20261024_000602_gen_2410240011_003

Hypothesis: grammar draw seed=2410240011: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 1326. PBO (CSCV) across family: 0.888. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 655d422f983d563e41032908544b770595f4b92b4e3bb690ddeab8a69eeb85f0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1323 | crypto|sma_cross(fast=10,slow=150)+vol_regime(max_atr_pct=0.04) | 8.08/0.33/-41.15 | 428.6 | 840 | 0.0987 | 0.81219 (102.9) | 1.0 | 0.2055 | 0.917 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1324 | crypto|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.04) | 23.26/0.58/-38.14 | 428.6 | 720 | 0.1 | 0.71429 (94.56) | 1.0 | 0.3005 | 0.9095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1325 | crypto|sma_cross(fast=50,slow=150)+vol_regime(max_atr_pct=0.04) | 44.11/0.87/-35.92 | 428.6 | 511 | 0.0982 | 0.5974 (81.61) | 1.0 | 0.4318 | 0.887 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1326 | crypto|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.04) | 53.55/1.01/-35.04 | 428.6 | 423 | 0.0954 | 0.56044 (92.47) | 1.0 | 0.4993 | 0.863 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
