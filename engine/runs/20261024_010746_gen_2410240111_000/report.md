# gen_2410240111_000 — engine run 20261024_010746_gen_2410240111_000

Hypothesis: grammar draw seed=2410240111: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1422. PBO (CSCV) across family: 0.288. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 43a2c7f38abbe670649d0a96bfb2c485363bbb0d2ae33f2a5de59beb6d4ed82f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1415 | megacap|drop_revert(drop=0.05,hold=5,n=1)+relvol(min_ratio=1.0) | -1.54/-0.89/-1.96 | 26.77 | 10 | 0.0458 | 0.98202 (12.42) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1416 | megacap|drop_revert(drop=0.05,hold=5,n=5)+relvol(min_ratio=1.0) | 1.06/0.3/-2.83 | 26.77 | 89 | 0.0537 | 0.92607 (12.26) | 1.0 | 0.0029 | 0.8885 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1417 | megacap|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | -0.22/-0.11/-1.99 | 26.77 | 23 | 0.0449 | 0.97902 (13.06) | 1.0 | 0.0004 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1418 | megacap|drop_revert(drop=0.05,hold=10,n=5)+relvol(min_ratio=1.0) | 0.39/0.1/-3.22 | 26.77 | 126 | 0.0505 | 0.92807 (12.56) | 1.0 | 0.0014 | 0.8945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1419 | megacap|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 26.77 | 1 | 0.0045 | 0.93906 (13.1) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1420 | megacap|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 0.59/1.03/-0.0 | 26.77 | 3 | 0.0385 | 0.95504 (12.97) | 1.0 | 0.0 | 0.9015 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1421 | megacap|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 26.77 | 1 | 0.0045 | 0.93806 (13.1) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1422 | megacap|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 1.66/1.16/-0.0 | 26.77 | 7 | 0.0385 | 0.92907 (13.41) | 1.0 | 0.0 | 0.89 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
