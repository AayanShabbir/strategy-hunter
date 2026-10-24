# gen_2310232131_001 — engine run 20261023_210433_gen_2310232131_001

Hypothesis: grammar draw seed=2310232131: sma_cross

**0/4 pass.** Ledger N at evaluation: 962. PBO (CSCV) across family: 0.124. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6eb5ea9eb99cb362c0e06906104c95c56250a07d24da3a0eb4c1a9caa94ec497. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 959 | crypto|sma_cross(fast=5,slow=100) | 22.9/0.57/-43.01 | 428.6 | 1314 | 0.1048 | 0.62837 (65.9) | 1.0 | 0.443 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 960 | crypto|sma_cross(fast=5,slow=150) | -0.17/0.19/-40.03 | 428.6 | 1068 | 0.1035 | 0.84815 (164.51) | 1.0 | 0.2733 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 961 | crypto|sma_cross(fast=10,slow=100) | 25.71/0.61/-43.88 | 428.6 | 1018 | 0.1042 | 0.66234 (185.84) | 1.0 | 0.4629 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 962 | crypto|sma_cross(fast=10,slow=150) | 4.55/0.27/-43.06 | 428.6 | 800 | 0.1023 | 0.84815 (151.06) | 1.0 | 0.309 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
