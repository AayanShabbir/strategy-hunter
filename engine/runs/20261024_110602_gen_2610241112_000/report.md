# gen_2610241112_000 — engine run 20261024_110602_gen_2610241112_000

Hypothesis: grammar draw seed=2610241112: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 2450. PBO (CSCV) across family: 0.824. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 18fe8d1a165c42423af26cb54e6f5dd3ac4701b8ed6b1c756e6581afca282e32. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2447 | sectors|sma_cross(fast=10,slow=100)+relvol(min_ratio=1.2) | -5.7/-0.3/-12.25 | 94.31 | 724 | 0.0754 | 1.0 (30.83) | 1.0 | 0.0499 | 0.502 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2448 | sectors|sma_cross(fast=10,slow=150)+relvol(min_ratio=1.2) | -8.73/-0.47/-12.71 | 94.31 | 716 | 0.0751 | 1.0 (29.98) | 1.0 | 0.0252 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2449 | sectors|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.2) | -1.57/-0.05/-8.74 | 94.31 | 703 | 0.0748 | 0.998 (31.61) | 1.0 | 0.116 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2450 | sectors|sma_cross(fast=50,slow=150)+relvol(min_ratio=1.2) | -3.28/-0.14/-9.81 | 94.31 | 686 | 0.0752 | 1.0 (30.9) | 1.0 | 0.0872 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
