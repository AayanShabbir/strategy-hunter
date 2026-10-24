# gen_2410240011_001 — engine run 20261024_000550_gen_2410240011_001

Hypothesis: grammar draw seed=2410240011: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1318. PBO (CSCV) across family: 0.003. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 cf356faa2175545dc694d652f3e71337736d9fd704411235058f59918ab4de50. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1311 | crypto|rsi_revert(entry=5,exit=60,n=2)+relvol(min_ratio=1.2) | -23.44/-1.55/-23.6 | 428.6 | 3293 | 0.0918 | 0.89211 (40.63) | 1.0 | 0.0001 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1312 | crypto|rsi_revert(entry=5,exit=60,n=3)+relvol(min_ratio=1.2) | -12.01/-1.05/-15.77 | 428.6 | 1449 | 0.0866 | 0.91508 (50.97) | 1.0 | 0.0006 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1313 | crypto|rsi_revert(entry=5,exit=70,n=2)+relvol(min_ratio=1.2) | -17.84/-0.95/-18.06 | 428.6 | 3686 | 0.0927 | 0.80519 (36.43) | 1.0 | 0.0035 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1314 | crypto|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.2) | -19.64/-1.58/-23.87 | 428.6 | 1890 | 0.0862 | 0.94505 (79.77) | 1.0 | 0.0 | 0.917 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1315 | crypto|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.2) | -36.14/-2.22/-36.09 | 428.6 | 5041 | 0.0945 | 0.8981 (18.45) | 1.0 | 0.0 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1316 | crypto|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.2) | -21.66/-1.39/-21.49 | 428.6 | 3275 | 0.0912 | 0.84915 (34.99) | 1.0 | 0.0002 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1317 | crypto|rsi_revert(entry=10,exit=70,n=2)+relvol(min_ratio=1.2) | -33.68/-1.82/-33.47 | 428.6 | 5564 | 0.0952 | 0.82817 (48.52) | 1.0 | 0.0001 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1318 | crypto|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.2) | -31.77/-1.88/-31.8 | 428.6 | 4034 | 0.0921 | 0.91109 (76.87) | 1.0 | 0.0 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
