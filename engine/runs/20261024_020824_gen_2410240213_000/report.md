# gen_2410240213_000 — engine run 20261024_020824_gen_2410240213_000

Hypothesis: grammar draw seed=2410240213: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1578. PBO (CSCV) across family: 0.439. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 81ae0b2884e4f9e601cc5030d10f07109be303d4641eba34a6e30696ef6c4834. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1571 | defensive|rsi_revert(entry=5,exit=60,n=2) | 26.3/1.79/-2.29 | 104.36 | 251 | 0.0654 | 0.84715 (40.18) | 1.0 | 0.6303 | 0.516 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1572 | defensive|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 104.36 | 3 | 0.0393 | 1.0 (30.69) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1573 | defensive|rsi_revert(entry=5,exit=80,n=2) | 30.49/1.49/-4.81 | 104.36 | 231 | 0.0658 | 0.75025 (41.19) | 1.0 | 0.405 | 0.51 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1574 | defensive|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 104.36 | 3 | 0.0393 | 1.0 (30.69) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1575 | defensive|rsi_revert(entry=20,exit=60,n=2) | 11.41/0.53/-8.81 | 104.36 | 702 | 0.0677 | 0.97203 (36.37) | 1.0 | 0.0291 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1576 | defensive|rsi_revert(entry=20,exit=60,n=5) | 20.91/1.07/-6.91 | 104.36 | 144 | 0.0625 | 0.92408 (41.0) | 1.0 | 0.1578 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1577 | defensive|rsi_revert(entry=20,exit=80,n=2) | 22.68/0.81/-7.38 | 104.36 | 554 | 0.0671 | 0.87612 (38.06) | 1.0 | 0.0808 | 0.51 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1578 | defensive|rsi_revert(entry=20,exit=80,n=5) | 41.58/1.5/-6.97 | 104.36 | 104 | 0.0625 | 0.53646 (43.36) | 1.0 | 0.4133 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
