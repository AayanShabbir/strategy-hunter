# gen_2310232331_001 — engine run 20261023_230829_gen_2310232331_001

Hypothesis: grammar draw seed=2310232331: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 1214. PBO (CSCV) across family: 0.787. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 e216f09c887b6e662abac97654a82fa8f75a0f9c779f993c225f344bd19b574d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1211 | crypto|sma_cross(fast=10,slow=100)+rsi_band(hi=60) | -23.86/-0.62/-41.52 | 428.6 | 4134 | 0.1022 | 0.8002 (98.52) | 1.0 | 0.0852 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1212 | crypto|sma_cross(fast=10,slow=150)+rsi_band(hi=60) | -33.83/-0.94/-47.04 | 428.6 | 3783 | 0.1018 | 0.91808 (25.06) | 1.0 | 0.0378 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1213 | crypto|sma_cross(fast=20,slow=100)+rsi_band(hi=60) | -24.82/-0.61/-41.68 | 428.6 | 3687 | 0.1021 | 0.86014 (78.91) | 1.0 | 0.0852 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1214 | crypto|sma_cross(fast=20,slow=150)+rsi_band(hi=60) | -28.0/-0.7/-41.45 | 428.6 | 3416 | 0.1018 | 0.91409 (110.64) | 1.0 | 0.0695 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
