# gen_2410240704_000 — engine run 20261024_070455_gen_2410240704_000

Hypothesis: grammar draw seed=2410240704: donchian

**0/4 pass.** Ledger N at evaluation: 2018. PBO (CSCV) across family: 0.367. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 8afcc958c2fce72e00733380e365ae1a1abbeaf588cb0590ddbe9d7646566c66. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | hibeta|donchian(entry_n=55,exit_n=10) | 159.02/1.43/-19.92 | 809.88 | 117 | 0.0268 | 0.76623 (222.91) | 1.0 | 0.8463 | 0.512 | False | beats_buy_hold, holm, dsr, spa |
| 2016 | hibeta|donchian(entry_n=55,exit_n=20) | 112.02/1.06/-33.06 | 809.88 | 89 | 0.0253 | 0.91109 (223.74) | 1.0 | 0.6389 | 0.5175 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2017 | hibeta|donchian(entry_n=100,exit_n=10) | 145.61/1.59/-11.11 | 809.88 | 86 | 0.029 | 0.7982 (221.45) | 1.0 | 0.908 | 0.51 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2018 | hibeta|donchian(entry_n=100,exit_n=20) | 96.24/1.13/-18.86 | 809.88 | 67 | 0.0278 | 0.95704 (227.74) | 1.0 | 0.6844 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
