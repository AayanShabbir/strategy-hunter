# gen_2610241107_000 — engine run 20261024_110549_gen_2610241107_000

Hypothesis: grammar draw seed=2610241107: donchian

**0/4 pass.** Ledger N at evaluation: 2426. PBO (CSCV) across family: 0.084. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 bed28be09c3d28fd61f1f690e93a88df4b8df979cb3d8833dd6e1808961b0a4c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2423 | sectors|donchian(entry_n=20,exit_n=10) | 36.82/1.18/-7.3 | 94.31 | 130 | 0.0661 | 0.50849 (37.79) | 1.0 | 0.6016 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2424 | sectors|donchian(entry_n=20,exit_n=20) | 44.61/1.16/-10.27 | 94.31 | 88 | 0.0592 | 0.33966 (39.44) | 1.0 | 0.5921 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2425 | sectors|donchian(entry_n=100,exit_n=10) | 12.94/0.66/-5.27 | 94.31 | 89 | 0.0806 | 0.97403 (39.18) | 1.0 | 0.272 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2426 | sectors|donchian(entry_n=100,exit_n=20) | 15.8/0.66/-8.29 | 94.31 | 59 | 0.0777 | 0.96104 (39.74) | 1.0 | 0.2696 | 0.514 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
