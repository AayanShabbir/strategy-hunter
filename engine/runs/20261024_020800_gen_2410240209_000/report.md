# gen_2410240209_000 — engine run 20261024_020800_gen_2410240209_000

Hypothesis: grammar draw seed=2410240209: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1518. PBO (CSCV) across family: 0.004. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 624f6a233fc88ddf4b389503d750b80b113c1ff4f84eb94f5c5cdb5b821d7749. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1511 | megacap|rsi_revert(entry=5,exit=70,n=2) | -9.75/-0.65/-13.23 | 26.77 | 2215 | 0.1195 | 0.82218 (1.35) | 1.0 | 0.0023 | 0.4935 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1512 | megacap|rsi_revert(entry=5,exit=70,n=3) | 2.75/0.28/-7.43 | 26.77 | 639 | 0.1191 | 0.85415 (9.05) | 1.0 | 0.0406 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1513 | megacap|rsi_revert(entry=5,exit=80,n=2) | -0.32/0.03/-11.32 | 26.77 | 1999 | 0.12 | 0.67333 (2.3) | 1.0 | 0.0224 | 0.949 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1514 | megacap|rsi_revert(entry=5,exit=80,n=3) | 8.82/0.67/-9.16 | 26.77 | 605 | 0.1188 | 0.76424 (8.99) | 1.0 | 0.107 | 0.858 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1515 | megacap|rsi_revert(entry=20,exit=70,n=2) | -15.3/-0.68/-25.16 | 26.77 | 4047 | 0.1213 | 0.5025 (-7.54) | 1.0 | 0.0014 | 0.5075 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1516 | megacap|rsi_revert(entry=20,exit=70,n=3) | -0.62/0.04/-16.97 | 26.77 | 2115 | 0.1214 | 0.73127 (1.91) | 1.0 | 0.0209 | 0.9365 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1517 | megacap|rsi_revert(entry=20,exit=80,n=2) | -8.89/-0.31/-23.93 | 26.77 | 3454 | 0.122 | 0.53247 (-4.99) | 1.0 | 0.0064 | 0.96 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1518 | megacap|rsi_revert(entry=20,exit=80,n=3) | 8.42/0.4/-16.14 | 26.77 | 1746 | 0.1211 | 0.6014 (4.08) | 1.0 | 0.0543 | 0.9065 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
