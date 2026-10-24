# gen_2610241209_000 — engine run 20261024_120749_gen_2610241209_000

Hypothesis: grammar draw seed=2610241209: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 2534. PBO (CSCV) across family: 0.282. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 38c87a5e0eacb56b2518000547eebb9442ac3d4ee411c5a77a6fe5abbb0d09d8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2527 | BROAD|rsi_revert(entry=5,exit=60,n=2)+relvol(min_ratio=1.2) | 3.49/0.66/-2.26 | 83.36 | 178 | 0.077 | 0.99101 (34.44) | 1.0 | 0.2703 | 0.4995 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2528 | BROAD|rsi_revert(entry=5,exit=60,n=3)+relvol(min_ratio=1.2) | 2.43/0.76/-0.75 | 83.36 | 67 | 0.0668 | 0.98002 (36.02) | 1.0 | 0.3132 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2529 | BROAD|rsi_revert(entry=5,exit=80,n=2)+relvol(min_ratio=1.2) | 3.54/0.57/-2.37 | 83.36 | 221 | 0.076 | 0.996 (33.27) | 1.0 | 0.2222 | 0.505 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2530 | BROAD|rsi_revert(entry=5,exit=80,n=3)+relvol(min_ratio=1.2) | 2.49/0.54/-1.99 | 83.36 | 134 | 0.0691 | 0.97003 (34.35) | 1.0 | 0.2083 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2531 | BROAD|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.2) | 0.07/0.02/-4.9 | 83.36 | 288 | 0.0788 | 0.999 (33.47) | 1.0 | 0.0465 | 0.5025 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2532 | BROAD|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.2) | 2.18/0.38/-2.01 | 83.36 | 162 | 0.0759 | 1.0 (35.03) | 1.0 | 0.1404 | 0.5025 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2533 | BROAD|rsi_revert(entry=10,exit=80,n=2)+relvol(min_ratio=1.2) | -0.16/-0.01/-5.35 | 83.36 | 361 | 0.0788 | 0.998 (32.5) | 1.0 | 0.042 | 0.5075 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2534 | BROAD|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.2) | 1.93/0.25/-4.06 | 83.36 | 285 | 0.0758 | 0.996 (32.61) | 1.0 | 0.0973 | 0.5005 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
