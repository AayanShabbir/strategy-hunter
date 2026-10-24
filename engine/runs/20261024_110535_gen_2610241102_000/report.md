# gen_2610241102_000 — engine run 20261024_110535_gen_2610241102_000

Hypothesis: grammar draw seed=2610241102: donchian

**0/4 pass.** Ledger N at evaluation: 2398. PBO (CSCV) across family: 0.068. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 a96bf34544afd3b2a79a265c89be3d85f4038308d68f5e0cf894e88963242466. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2395 | sectors|donchian(entry_n=20,exit_n=10) | 36.82/1.18/-7.3 | 94.31 | 130 | 0.0661 | 0.51149 (37.97) | 1.0 | 0.8227 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2396 | sectors|donchian(entry_n=20,exit_n=20) | 44.61/1.16/-10.27 | 94.31 | 88 | 0.0592 | 0.32068 (39.13) | 1.0 | 0.8183 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2397 | sectors|donchian(entry_n=55,exit_n=10) | 20.42/0.86/-6.2 | 94.31 | 103 | 0.0778 | 0.91409 (39.25) | 1.0 | 0.6504 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2398 | sectors|donchian(entry_n=55,exit_n=20) | 24.42/0.85/-8.69 | 94.31 | 70 | 0.0724 | 0.86114 (39.15) | 1.0 | 0.6413 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
