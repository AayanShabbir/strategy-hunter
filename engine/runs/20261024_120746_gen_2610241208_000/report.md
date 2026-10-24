# gen_2610241208_000 — engine run 20261024_120746_gen_2610241208_000

Hypothesis: grammar draw seed=2610241208: drop_revert

**0/8 pass.** Ledger N at evaluation: 2526. PBO (CSCV) across family: 0.411. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d45bb6deb83dfc7ae1aadfa6a89a5a8c6bd73b42083bdb8839fc06735f68ce6a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2519 | index|drop_revert(drop=0.05,hold=5,n=1) | 8.5/0.41/-4.32 | 107.42 | 9 | 0.0391 | 0.95804 (45.16) | 1.0 | 0.3853 | 0.4835 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2520 | index|drop_revert(drop=0.05,hold=5,n=5) | 11.3/0.47/-7.15 | 107.42 | 60 | 0.0453 | 0.98501 (44.69) | 1.0 | 0.4435 | 0.4845 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2521 | index|drop_revert(drop=0.05,hold=10,n=1) | 3.12/0.17/-6.69 | 107.42 | 8 | 0.0399 | 0.995 (44.87) | 1.0 | 0.2445 | 0.4895 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2522 | index|drop_revert(drop=0.05,hold=10,n=5) | 13.68/0.52/-8.41 | 107.42 | 43 | 0.0513 | 0.95305 (43.23) | 1.0 | 0.483 | 0.48 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2523 | index|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 107.42 | 0 | inf | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2524 | index|drop_revert(drop=0.15,hold=5,n=5) | 0.0/0.0/0.0 | 107.42 | 2 | 0.0217 | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2525 | index|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 107.42 | 0 | inf | 1.0 (37.07) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2526 | index|drop_revert(drop=0.15,hold=10,n=5) | 0.0/0.0/0.0 | 107.42 | 2 | 0.0217 | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
