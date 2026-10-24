# gen_2610240916_000 — engine run 20261024_091219_gen_2610240916_000

Hypothesis: grammar draw seed=2610240916: donchian

**0/4 pass.** Ledger N at evaluation: 2270. PBO (CSCV) across family: 0.71. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 42d81797515fa6b122cd7a4d85feb5c4622e5d699a093136550f3da332c2a255. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2267 | BROAD|donchian(entry_n=55,exit_n=10) | 0.41/0.05/-8.63 | 33.23 | 66 | 0.101 | 0.97203 (14.55) | 1.0 | 0.0197 | 0.4895 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2268 | BROAD|donchian(entry_n=55,exit_n=20) | 7.36/0.43/-6.86 | 33.23 | 49 | 0.0979 | 0.83616 (14.36) | 1.0 | 0.0807 | 0.483 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2269 | BROAD|donchian(entry_n=100,exit_n=10) | 3.06/0.27/-5.82 | 33.23 | 53 | 0.1036 | 0.97003 (14.81) | 1.0 | 0.0472 | 0.4965 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2270 | BROAD|donchian(entry_n=100,exit_n=20) | 13.34/0.9/-4.34 | 33.23 | 37 | 0.1031 | 0.66134 (15.49) | 1.0 | 0.2756 | 0.9575 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
