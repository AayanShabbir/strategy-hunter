# gen_2410240031_001 — engine run 20261024_000618_gen_2410240031_001

Hypothesis: grammar draw seed=2410240031: donchian+relvol

**0/4 pass.** Ledger N at evaluation: 1346. PBO (CSCV) across family: 0.294. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 219938c447b8d2541ad019fbf70c42a3a223d156c6fe202d87c60c88908fad3a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1343 | semis|donchian(entry_n=55,exit_n=10)+relvol(min_ratio=1.0) | 0.96/0.25/-1.98 | -38.66 | 270 | 0.0868 | 0.08991 (-22.35) | 1.0 | 0.0607 | 0.287 | False | cost_stop, walk_forward, holm, dsr, spa |
| 1344 | semis|donchian(entry_n=55,exit_n=20)+relvol(min_ratio=1.0) | -1.01/-0.21/-3.77 | -38.66 | 393 | 0.085 | 0.09291 (-23.21) | 1.0 | 0.0079 | 0.301 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1345 | semis|donchian(entry_n=100,exit_n=10)+relvol(min_ratio=1.0) | 0.62/0.32/-1.14 | -38.66 | 89 | 0.0846 | 0.0979 (-22.33) | 1.0 | 0.0687 | 0.2925 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1346 | semis|donchian(entry_n=100,exit_n=20)+relvol(min_ratio=1.0) | -1.04/-0.44/-1.83 | -38.66 | 123 | 0.0835 | 0.12687 (-20.81) | 1.0 | 0.009 | 0.3055 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
