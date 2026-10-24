# gen_2610241017_000 — engine run 20261024_101013_gen_2610241017_000

Hypothesis: grammar draw seed=2610241017: donchian+rsi_band

**0/4 pass.** Ledger N at evaluation: 2358. PBO (CSCV) across family: 0.532. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 87cca3dcb796e7495f691a68d95a8b8b9bfe41e385b76645145cecfd99969732. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2355 | megacap|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 54.49/1.24/-15.63 | 118.49 | 105 | 0.0518 | 0.34965 (46.99) | 1.0 | 0.8861 | 0.9665 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2356 | megacap|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 46.85/0.94/-19.22 | 118.49 | 84 | 0.0509 | 0.45554 (46.49) | 1.0 | 0.7527 | 0.512 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2357 | megacap|donchian(entry_n=100,exit_n=10)+rsi_band(hi=80) | 43.3/1.29/-9.05 | 118.49 | 70 | 0.061 | 0.53646 (46.66) | 1.0 | 0.9063 | 0.962 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2358 | megacap|donchian(entry_n=100,exit_n=20)+rsi_band(hi=80) | 38.18/1.08/-10.9 | 118.49 | 58 | 0.0602 | 0.64735 (46.78) | 1.0 | 0.8237 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
