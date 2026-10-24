# gen_2410240021_003 — engine run 20261024_000613_gen_2410240021_003

Hypothesis: grammar draw seed=2410240021: donchian+rsi_band

**0/4 pass.** Ledger N at evaluation: 1338. PBO (CSCV) across family: 0.083. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 9c36bcb6aa9d8fbe35bf7803225cf9de2cfa66852005f547cd1269f8655306fd. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1335 | sectors|donchian(entry_n=20,exit_n=10)+rsi_band(hi=60) | 6.36/0.65/-3.77 | 50.2 | 1105 | 0.0748 | 0.99201 (18.91) | 1.0 | 0.2573 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1336 | sectors|donchian(entry_n=20,exit_n=20)+rsi_band(hi=60) | 7.02/0.49/-5.16 | 50.2 | 1212 | 0.0752 | 0.97403 (18.16) | 1.0 | 0.1771 | 0.5035 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1337 | sectors|donchian(entry_n=100,exit_n=10)+rsi_band(hi=60) | 0.25/0.06/-2.41 | 50.2 | 557 | 0.0836 | 1.0 (20.95) | 1.0 | 0.0478 | 0.4975 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1338 | sectors|donchian(entry_n=100,exit_n=20)+rsi_band(hi=60) | 0.17/0.03/-3.45 | 50.2 | 663 | 0.084 | 1.0 (20.5) | 1.0 | 0.0442 | 0.507 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
