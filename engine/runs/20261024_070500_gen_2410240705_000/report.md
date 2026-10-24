# gen_2410240705_000 — engine run 20261024_070500_gen_2410240705_000

Hypothesis: grammar draw seed=2410240705: sma_cross

**0/4 pass.** Ledger N at evaluation: 2022. PBO (CSCV) across family: 0.047. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 ace82fb80a25c040e200d2471787eac2ef7cda4a6e8e250855654091fb6da5ec. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | crypto|sma_cross(fast=5,slow=100) | 22.9/0.57/-43.01 | 428.6 | 1314 | 0.1048 | 0.65135 (87.62) | 1.0 | 0.4713 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2020 | crypto|sma_cross(fast=5,slow=150) | -0.17/0.19/-40.03 | 428.6 | 1068 | 0.1035 | 0.84515 (75.5) | 1.0 | 0.2974 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2021 | crypto|sma_cross(fast=20,slow=100) | 23.33/0.57/-42.12 | 428.6 | 793 | 0.1029 | 0.71628 (175.09) | 1.0 | 0.4746 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2022 | crypto|sma_cross(fast=20,slow=150) | 15.42/0.45/-39.27 | 428.6 | 621 | 0.1018 | 0.78222 (111.07) | 1.0 | 0.4175 | 0.9165 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
