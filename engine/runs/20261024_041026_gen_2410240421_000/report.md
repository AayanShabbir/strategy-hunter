# gen_2410240421_000 — engine run 20261024_041026_gen_2410240421_000

Hypothesis: grammar draw seed=2410240421: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 1770. PBO (CSCV) across family: 0.819. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 501cfdf952deb25128f84e11127cfcbc06e4f05d070f4446e2cedd4b5a483d4f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1767 | defensive|sma_cross(fast=10,slow=50)+trend_sma(n=100) | 51.13/1.68/-6.25 | 104.36 | 178 | 0.0692 | 0.26274 (40.16) | 1.0 | 0.9284 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1768 | defensive|sma_cross(fast=10,slow=200)+trend_sma(n=100) | 56.23/1.71/-7.99 | 104.36 | 180 | 0.0692 | 0.23177 (40.87) | 1.0 | 0.9372 | 0.494 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1769 | defensive|sma_cross(fast=20,slow=50)+trend_sma(n=100) | 36.14/1.28/-7.99 | 104.36 | 165 | 0.0671 | 0.68332 (41.19) | 1.0 | 0.7829 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1770 | defensive|sma_cross(fast=20,slow=200)+trend_sma(n=100) | 59.89/1.83/-7.99 | 104.36 | 174 | 0.068 | 0.18581 (42.15) | 1.0 | 0.9583 | 0.9725 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
