# gen_2610241016_000 — engine run 20261024_101010_gen_2610241016_000

Hypothesis: grammar draw seed=2610241016: donchian

**0/4 pass.** Ledger N at evaluation: 2354. PBO (CSCV) across family: 0.13. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 acb344f6b1a1683b699d85391b649324d0d40a2714460d64b7ad55608ebf37e1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2351 | index|donchian(entry_n=20,exit_n=10) | 51.31/1.36/-6.81 | 107.42 | 87 | 0.0757 | 0.28771 (42.67) | 1.0 | 0.7663 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2352 | index|donchian(entry_n=20,exit_n=20) | 76.06/1.58/-8.36 | 107.42 | 53 | 0.0657 | 0.02398 (43.71) | 1.0 | 0.8691 | 0.923 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2353 | index|donchian(entry_n=100,exit_n=10) | 24.69/0.97/-5.84 | 107.42 | 66 | 0.0901 | 0.92308 (43.91) | 1.0 | 0.5247 | 0.5005 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2354 | index|donchian(entry_n=100,exit_n=20) | 36.13/1.11/-7.92 | 107.42 | 41 | 0.0835 | 0.66234 (43.3) | 1.0 | 0.6187 | 0.517 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
