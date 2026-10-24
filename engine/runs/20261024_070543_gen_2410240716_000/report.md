# gen_2410240716_000 — engine run 20261024_070543_gen_2410240716_000

Hypothesis: grammar draw seed=2410240716: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 2090. PBO (CSCV) across family: 0.491. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 f0c8042613c5e6ad709f8defaf3da14ad2b36059f977c40678ab76f94ae0f0fc. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2083 | sectors|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.0) | 3.03/0.28/-2.54 | 50.2 | 59 | 0.0286 | 1.0 (23.07) | 1.0 | 0.3585 | 0.4975 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2084 | sectors|drop_revert(drop=0.05,hold=3,n=5)+relvol(min_ratio=1.0) | 3.06/0.21/-4.74 | 50.2 | 321 | 0.043 | 1.0 (22.34) | 1.0 | 0.3229 | 0.502 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2085 | sectors|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | 5.04/0.36/-3.02 | 50.2 | 83 | 0.0296 | 0.997 (22.93) | 1.0 | 0.4223 | 0.4985 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2086 | sectors|drop_revert(drop=0.05,hold=10,n=5)+relvol(min_ratio=1.0) | 3.14/0.21/-4.93 | 50.2 | 501 | 0.043 | 1.0 (21.72) | 1.0 | 0.324 | 0.505 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2087 | sectors|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 50.2 | 4 | 0.0213 | 1.0 (23.03) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2088 | sectors|drop_revert(drop=0.15,hold=3,n=5)+relvol(min_ratio=1.0) | 0.07/0.03/-0.73 | 50.2 | 23 | 0.0205 | 1.0 (23.3) | 1.0 | 0.2344 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2089 | sectors|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 50.2 | 9 | 0.0153 | 1.0 (23.93) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2090 | sectors|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 0.07/0.03/-0.73 | 50.2 | 32 | 0.021 | 1.0 (22.94) | 1.0 | 0.2344 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
