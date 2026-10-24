# gen_2410240216_000 — engine run 20261024_020835_gen_2410240216_000

Hypothesis: grammar draw seed=2410240216: drop_revert

**0/8 pass.** Ledger N at evaluation: 1598. PBO (CSCV) across family: 0.606. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 9a7ba414493b345e88519de14f26387864bb4c9154b50455b1d3ea4a956f4d2d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1591 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.8991 (12.54) | 1.0 | 0.5372 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1592 | megacap|drop_revert(drop=0.05,hold=3,n=5) | 3.92/0.71/-2.86 | 26.77 | 203 | 0.0576 | 0.75125 (12.25) | 1.0 | 0.5905 | 0.863 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1593 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.92308 (12.92) | 1.0 | 0.4099 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1594 | megacap|drop_revert(drop=0.05,hold=5,n=5) | 3.66/0.52/-6.0 | 26.77 | 193 | 0.0582 | 0.63137 (12.72) | 1.0 | 0.5007 | 0.8535 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1595 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.87/0.42/-0.92 | 26.77 | 9 | 0.0287 | 0.96004 (13.24) | 1.0 | 0.4409 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1596 | megacap|drop_revert(drop=0.1,hold=3,n=5) | 1.39/0.58/-1.11 | 26.77 | 16 | 0.029 | 0.94306 (13.69) | 1.0 | 0.5244 | 0.8915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1597 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.93/0.37/-1.25 | 26.77 | 9 | 0.0287 | 0.93407 (12.56) | 1.0 | 0.4195 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1598 | megacap|drop_revert(drop=0.1,hold=5,n=5) | 1.57/0.82/-0.9 | 26.77 | 16 | 0.029 | 0.92507 (13.01) | 1.0 | 0.643 | 0.894 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
