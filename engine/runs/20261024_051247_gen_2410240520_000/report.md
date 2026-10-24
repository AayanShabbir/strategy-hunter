# gen_2410240520_000 — engine run 20261024_051247_gen_2410240520_000

Hypothesis: grammar draw seed=2410240520: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1850. PBO (CSCV) across family: 0.093. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b90d1137610b175f2de76f1a37e852da2e5b7799afef1553d361621815819d63. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1843 | BROAD|rsi_revert(entry=5,exit=60,n=2) | 33.37/0.87/-10.83 | 386.25 | 286 | 0.0319 | 1.0 (121.49) | 1.0 | 0.6827 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1844 | BROAD|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 386.25 | 2 | 0.0349 | 1.0 (143.13) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1845 | BROAD|rsi_revert(entry=5,exit=70,n=2) | 37.09/0.91/-11.36 | 386.25 | 276 | 0.0324 | 0.997 (121.51) | 1.0 | 0.7048 | 0.504 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1846 | BROAD|rsi_revert(entry=5,exit=70,n=5) | 0.0/0.0/0.0 | 386.25 | 2 | 0.0349 | 1.0 (113.02) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1847 | BROAD|rsi_revert(entry=10,exit=60,n=2) | 67.27/1.25/-16.9 | 386.25 | 551 | 0.0323 | 0.95005 (117.93) | 1.0 | 0.8876 | 0.5165 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1848 | BROAD|rsi_revert(entry=10,exit=60,n=5) | 13.98/0.83/-2.96 | 386.25 | 28 | 0.0341 | 0.98801 (130.04) | 1.0 | 0.6456 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1849 | BROAD|rsi_revert(entry=10,exit=70,n=2) | 70.89/1.22/-18.16 | 386.25 | 522 | 0.0326 | 0.93906 (120.91) | 1.0 | 0.8634 | 0.513 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1850 | BROAD|rsi_revert(entry=10,exit=70,n=5) | 14.95/0.82/-5.51 | 386.25 | 27 | 0.0341 | 0.98801 (127.27) | 1.0 | 0.619 | 0.505 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
