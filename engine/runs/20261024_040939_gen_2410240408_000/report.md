# gen_2410240408_000 — engine run 20261024_040939_gen_2410240408_000

Hypothesis: grammar draw seed=2410240408: drop_revert

**0/8 pass.** Ledger N at evaluation: 1702. PBO (CSCV) across family: 0.008. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 1e6739aec37e30eac326dbc208dbfc693afa66e59c4740cface810042987d606. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1695 | BROAD|drop_revert(drop=0.05,hold=3,n=1) | 0.09/0.03/-3.97 | 64.52 | 480 | 0.0302 | 1.0 (28.3) | 1.0 | 0.0649 | 0.4905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1696 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 10.7/0.65/-5.87 | 64.52 | 1450 | 0.0377 | 1.0 (27.38) | 1.0 | 0.3097 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1697 | BROAD|drop_revert(drop=0.05,hold=5,n=1) | 1.29/0.12/-4.22 | 64.52 | 448 | 0.0309 | 1.0 (28.65) | 1.0 | 0.0825 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1698 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 14.45/0.81/-6.15 | 64.52 | 1381 | 0.0381 | 0.998 (27.5) | 1.0 | 0.4271 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1699 | BROAD|drop_revert(drop=0.1,hold=3,n=1) | 0.59/0.42/-0.77 | 64.52 | 61 | 0.0187 | 1.0 (28.49) | 1.0 | 0.2079 | 0.497 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1700 | BROAD|drop_revert(drop=0.1,hold=3,n=5) | 3.98/0.35/-2.57 | 64.52 | 287 | 0.0275 | 1.0 (28.27) | 1.0 | 0.1346 | 0.485 | False | beats_buy_hold, holm, dsr, spa |
| 1701 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.32/0.19/-0.94 | 64.52 | 57 | 0.02 | 1.0 (29.15) | 1.0 | 0.1061 | 0.498 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1702 | BROAD|drop_revert(drop=0.1,hold=5,n=5) | 4.9/0.42/-2.63 | 64.52 | 281 | 0.0276 | 1.0 (28.73) | 1.0 | 0.1624 | 0.484 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
