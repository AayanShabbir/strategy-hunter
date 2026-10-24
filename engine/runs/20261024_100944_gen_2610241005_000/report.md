# gen_2610241005_000 — engine run 20261024_100944_gen_2610241005_000

Hypothesis: grammar draw seed=2610241005: donchian+trend_sma

**0/4 pass.** Ledger N at evaluation: 2302. PBO (CSCV) across family: 0.396. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 3e6e83aaaa03700726c518ab9a5f7daf844ac6a6b9f9e4d169577a48ab31537b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2299 | crypto|donchian(entry_n=20,exit_n=10)+trend_sma(n=50) | 10.05/0.37/-19.61 | 434.62 | 86 | 0.0197 | 0.83816 (89.13) | 1.0 | 0.2415 | 0.9075 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2300 | crypto|donchian(entry_n=20,exit_n=20)+trend_sma(n=50) | 35.15/0.82/-22.99 | 434.62 | 98 | 0.0197 | 0.69331 (94.0) | 1.0 | 0.4349 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2301 | crypto|donchian(entry_n=100,exit_n=10)+trend_sma(n=50) | 2.1/0.17/-18.03 | 434.62 | 33 | 0.0206 | 0.88811 (240.45) | 1.0 | 0.1727 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2302 | crypto|donchian(entry_n=100,exit_n=20)+trend_sma(n=50) | 8.86/0.38/-18.92 | 434.62 | 40 | 0.0217 | 0.82617 (253.34) | 1.0 | 0.2447 | 0.907 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
