# gen_2610240906_000 — engine run 20261024_091153_gen_2610240906_000

Hypothesis: grammar draw seed=2610240906: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2222. PBO (CSCV) across family: 0.455. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 6eca925730280fa279bc1834de847ec2b51af6282efc906dbdc01c7f2d601db0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2215 | sectors|rsi_revert(entry=5,exit=70,n=2) | 13.47/0.75/-5.21 | 50.2 | 560 | 0.0683 | 0.90909 (20.63) | 1.0 | 0.663 | 0.9705 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2216 | sectors|rsi_revert(entry=5,exit=70,n=5) | 2.94/0.93/-0.86 | 50.2 | 22 | 0.0635 | 0.998 (22.68) | 1.0 | 0.7449 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2217 | sectors|rsi_revert(entry=5,exit=80,n=2) | 19.68/0.99/-4.72 | 50.2 | 532 | 0.0683 | 0.54246 (20.64) | 1.0 | 0.8223 | 0.937 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2218 | sectors|rsi_revert(entry=5,exit=80,n=5) | 4.69/1.29/-0.86 | 50.2 | 22 | 0.0635 | 0.99401 (23.19) | 1.0 | 0.9136 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2219 | sectors|rsi_revert(entry=10,exit=70,n=2) | 21.31/0.99/-5.61 | 50.2 | 941 | 0.0701 | 0.33267 (18.92) | 1.0 | 0.8105 | 0.9455 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2220 | sectors|rsi_revert(entry=10,exit=70,n=5) | 6.29/0.96/-1.66 | 50.2 | 79 | 0.0631 | 0.98801 (23.88) | 1.0 | 0.7607 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2221 | sectors|rsi_revert(entry=10,exit=80,n=2) | 24.64/1.02/-5.5 | 50.2 | 843 | 0.0711 | 0.2048 (20.01) | 1.0 | 0.8159 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2222 | sectors|rsi_revert(entry=10,exit=80,n=5) | 11.32/1.19/-2.1 | 50.2 | 77 | 0.0633 | 0.92108 (22.95) | 1.0 | 0.8887 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
