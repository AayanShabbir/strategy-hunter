# gen_2410240121_002 — engine run 20261024_010802_gen_2410240121_002

Hypothesis: grammar draw seed=2410240121: drop_revert

**0/8 pass.** Ledger N at evaluation: 1446. PBO (CSCV) across family: 0.843. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 fd2b3fc267e4b7c139f9564d77ff60ee863b4a847cebc92290c2b5f41cf2f7c1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1439 | crypto|drop_revert(drop=0.05,hold=5,n=3) | 14.64/1.01/-5.04 | 428.6 | 482 | 0.0373 | 0.82218 (185.26) | 1.0 | 0.1733 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1440 | crypto|drop_revert(drop=0.05,hold=5,n=5) | -2.22/-0.04/-14.4 | 428.6 | 675 | 0.0434 | 0.92707 (149.25) | 1.0 | 0.0132 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1441 | crypto|drop_revert(drop=0.05,hold=10,n=3) | -4.05/-0.18/-10.63 | 428.6 | 412 | 0.0403 | 0.95305 (155.61) | 1.0 | 0.008 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1442 | crypto|drop_revert(drop=0.05,hold=10,n=5) | -6.89/-0.2/-17.22 | 428.6 | 577 | 0.0473 | 0.95205 (137.0) | 1.0 | 0.0074 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1443 | crypto|drop_revert(drop=0.1,hold=5,n=3) | 1.51/0.69/-0.6 | 428.6 | 44 | 0.0155 | 0.94406 (56.48) | 1.0 | 0.0351 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1444 | crypto|drop_revert(drop=0.1,hold=5,n=5) | 3.97/0.75/-2.84 | 428.6 | 89 | 0.0219 | 0.86513 (65.12) | 1.0 | 0.1121 | 0.9065 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1445 | crypto|drop_revert(drop=0.1,hold=10,n=3) | -1.13/-0.36/-1.92 | 428.6 | 39 | 0.0163 | 0.95904 (69.95) | 1.0 | 0.0055 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1446 | crypto|drop_revert(drop=0.1,hold=10,n=5) | 4.28/0.67/-3.04 | 428.6 | 76 | 0.0239 | 0.88811 (219.54) | 1.0 | 0.0761 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
