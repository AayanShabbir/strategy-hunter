# gen_2410240521_000 — engine run 20261024_051250_gen_2410240521_000

Hypothesis: grammar draw seed=2410240521: donchian

**0/4 pass.** Ledger N at evaluation: 1854. PBO (CSCV) across family: 0.609. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 3cbec9bb290e549c7cce282256ab9a0134dfd78de91a638c3ad485c4836e3383. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1851 | BROAD|donchian(entry_n=55,exit_n=10) | -1.18/-0.11/-4.45 | 23.43 | 145 | 0.2021 | 0.998 (10.26) | 1.0 | 0.0514 | 0.49 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1852 | BROAD|donchian(entry_n=55,exit_n=20) | 3.03/0.29/-5.46 | 23.43 | 102 | 0.187 | 0.97802 (10.37) | 1.0 | 0.17 | 0.9565 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1853 | BROAD|donchian(entry_n=100,exit_n=10) | 1.43/0.24/-3.48 | 23.43 | 117 | 0.2232 | 0.999 (10.62) | 1.0 | 0.1492 | 0.9665 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1854 | BROAD|donchian(entry_n=100,exit_n=20) | 3.6/0.47/-3.55 | 23.43 | 85 | 0.2214 | 0.98901 (10.8) | 1.0 | 0.2645 | 0.9625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
