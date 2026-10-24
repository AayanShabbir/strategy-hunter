# gen_2410240131_001 — engine run 20261024_010817_gen_2410240131_001

Hypothesis: grammar draw seed=2410240131: donchian

**0/4 pass.** Ledger N at evaluation: 1462. PBO (CSCV) across family: 0.155. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 9e306d5bea8e89eeb9928969de13bebdf755ef8b39fcddc277f12338a77f5714. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1459 | sectors|donchian(entry_n=20,exit_n=10) | 14.67/0.77/-5.33 | 50.2 | 386 | 0.0703 | 0.85514 (21.6) | 1.0 | 0.7849 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1460 | sectors|donchian(entry_n=20,exit_n=20) | 15.73/0.68/-7.57 | 50.2 | 276 | 0.0645 | 0.84316 (22.69) | 1.0 | 0.7372 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1461 | sectors|donchian(entry_n=55,exit_n=10) | 8.71/0.64/-5.6 | 50.2 | 284 | 0.0777 | 0.997 (22.29) | 1.0 | 0.7093 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1462 | sectors|donchian(entry_n=55,exit_n=20) | 8.86/0.55/-6.55 | 50.2 | 209 | 0.0752 | 0.99201 (22.42) | 1.0 | 0.6567 | 0.513 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
