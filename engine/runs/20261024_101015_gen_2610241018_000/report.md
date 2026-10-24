# gen_2610241018_000 — engine run 20261024_101015_gen_2610241018_000

Hypothesis: grammar draw seed=2610241018: donchian

**0/4 pass.** Ledger N at evaluation: 2362. PBO (CSCV) across family: 0.866. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 5431a4c3410b1af89932e71e80320dc859146b1c8e5f4e0f1e5b75eef921d26a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2359 | sectors|donchian(entry_n=55,exit_n=10) | 20.42/0.86/-6.2 | 94.31 | 103 | 0.0778 | 0.92408 (39.64) | 1.0 | 0.7842 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2360 | sectors|donchian(entry_n=55,exit_n=20) | 24.42/0.85/-8.69 | 94.31 | 70 | 0.0724 | 0.87413 (40.06) | 1.0 | 0.7781 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2361 | sectors|donchian(entry_n=100,exit_n=10) | 12.94/0.66/-5.27 | 94.31 | 89 | 0.0806 | 0.98002 (38.38) | 1.0 | 0.6738 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2362 | sectors|donchian(entry_n=100,exit_n=20) | 15.8/0.66/-8.29 | 94.31 | 59 | 0.0777 | 0.97203 (39.39) | 1.0 | 0.6738 | 0.514 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
