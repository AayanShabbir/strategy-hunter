# gen_2410240312_000 — engine run 20261024_030926_gen_2410240312_000

Hypothesis: grammar draw seed=2410240312: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1634. PBO (CSCV) across family: 0.174. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 14ef478e19f2271fe80a7dee386174375dbdc010981fb579af5c79d3e967050f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1627 | crypto|rsi_revert(entry=5,exit=70,n=2) | -1.97/0.06/-16.18 | 428.6 | 3220 | 0.0973 | 0.6963 (50.87) | 1.0 | 0.0274 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1628 | crypto|rsi_revert(entry=5,exit=70,n=3) | -33.58/-1.43/-37.94 | 428.6 | 918 | 0.0921 | 0.998 (178.03) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1629 | crypto|rsi_revert(entry=5,exit=80,n=2) | -8.09/-0.07/-25.09 | 428.6 | 2973 | 0.0981 | 0.75225 (51.66) | 1.0 | 0.0184 | 0.9155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1630 | crypto|rsi_revert(entry=5,exit=80,n=3) | -28.75/-0.91/-33.41 | 428.6 | 846 | 0.0923 | 0.996 (156.3) | 1.0 | 0.0004 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1631 | crypto|rsi_revert(entry=10,exit=70,n=2) | -13.03/-0.19/-27.38 | 428.6 | 5399 | 0.1007 | 0.5994 (21.4) | 1.0 | 0.0126 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1632 | crypto|rsi_revert(entry=10,exit=70,n=3) | -17.11/-0.36/-30.56 | 428.6 | 2131 | 0.0978 | 0.91009 (50.9) | 1.0 | 0.0061 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1633 | crypto|rsi_revert(entry=10,exit=80,n=2) | -26.82/-0.47/-40.98 | 428.6 | 4730 | 0.1014 | 0.78422 (14.83) | 1.0 | 0.0044 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1634 | crypto|rsi_revert(entry=10,exit=80,n=3) | -18.34/-0.28/-33.41 | 428.6 | 1826 | 0.099 | 0.94406 (54.95) | 1.0 | 0.0086 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
