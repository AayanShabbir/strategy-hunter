# gen_2310232231_000 — engine run 20261023_220824_gen_2310232231_000

Hypothesis: grammar draw seed=2310232231: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 1082. PBO (CSCV) across family: 0.002. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 a54739b993078e1fd31f2aa3936da952dd2cdc6ff752a3c0777c77fd4774d6cd. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1079 | crypto|sma_cross(fast=10,slow=50)+relvol(min_ratio=1.0) | -59.24/-3.32/-61.91 | 428.6 | 9374 | 0.1026 | 0.87013 (-23.64) | 1.0 | 0.0003 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1080 | crypto|sma_cross(fast=10,slow=150)+relvol(min_ratio=1.0) | -62.42/-3.62/-64.2 | 428.6 | 9212 | 0.1029 | 0.94206 (14.87) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1081 | crypto|sma_cross(fast=50,slow=50)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1082 | crypto|sma_cross(fast=50,slow=150)+relvol(min_ratio=1.0) | -60.41/-3.42/-62.17 | 428.6 | 9119 | 0.1019 | 0.90709 (-16.67) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
