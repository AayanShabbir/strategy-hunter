# gen_2610241013_000 — engine run 20261024_101002_gen_2610241013_000

Hypothesis: grammar draw seed=2610241013: donchian

**0/4 pass.** Ledger N at evaluation: 2338. PBO (CSCV) across family: 0.068. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 535a36828fb22e3f4f143eb894a9af07a0cdb176b57a7840d83163f56633ac39. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2335 | sectors|donchian(entry_n=20,exit_n=10) | 36.82/1.18/-7.3 | 94.31 | 130 | 0.0661 | 0.52947 (38.41) | 1.0 | 0.8233 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2336 | sectors|donchian(entry_n=20,exit_n=20) | 44.61/1.16/-10.27 | 94.31 | 88 | 0.0592 | 0.30569 (38.55) | 1.0 | 0.8188 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2337 | sectors|donchian(entry_n=55,exit_n=10) | 20.42/0.86/-6.2 | 94.31 | 103 | 0.0778 | 0.92108 (39.27) | 1.0 | 0.6512 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2338 | sectors|donchian(entry_n=55,exit_n=20) | 24.42/0.85/-8.69 | 94.31 | 70 | 0.0724 | 0.87912 (39.19) | 1.0 | 0.6421 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
