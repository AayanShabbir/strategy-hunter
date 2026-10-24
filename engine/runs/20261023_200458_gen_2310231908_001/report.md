# gen_2310231908_001 — engine run 20261023_200458_gen_2310231908_001

Hypothesis: grammar draw seed=2310231908: drop_revert

**0/8 pass.** Ledger N at evaluation: 774. PBO (CSCV) across family: 0.526. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 0bb941f05c74b8ee23c0efa1511b8fd39218539213a7f478aed07a3ccb1a7917. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 767 | semis|drop_revert(drop=0.05,hold=3,n=1) | 6.17/0.58/-3.57 | -38.66 | 80 | 0.0343 | 0.12288 (-20.9) | 1.0 | 0.0269 | 0.26 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 768 | semis|drop_revert(drop=0.05,hold=3,n=3) | -8.01/-0.53/-13.02 | -38.66 | 323 | 0.0473 | 0.26474 (-21.93) | 1.0 | 0.0013 | 0.35 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 769 | semis|drop_revert(drop=0.05,hold=10,n=1) | 18.86/1.15/-6.81 | -38.66 | 75 | 0.0354 | 0.03197 (-22.15) | 1.0 | 0.1096 | 0.21 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 770 | semis|drop_revert(drop=0.05,hold=10,n=3) | 6.0/0.33/-14.25 | -38.66 | 276 | 0.0489 | 0.06893 (-21.32) | 1.0 | 0.0306 | 0.228 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 771 | semis|drop_revert(drop=0.1,hold=3,n=1) | 0.05/0.03/-2.7 | -38.66 | 17 | 0.0221 | 0.12488 (-20.4) | 1.0 | 0.0149 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 772 | semis|drop_revert(drop=0.1,hold=3,n=3) | 0.67/0.13/-3.61 | -38.66 | 37 | 0.0263 | 0.12987 (-22.07) | 1.0 | 0.0045 | 0.2935 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 773 | semis|drop_revert(drop=0.1,hold=10,n=1) | 5.53/1.04/-3.18 | -38.66 | 17 | 0.0221 | 0.0999 (-20.22) | 1.0 | 0.1332 | 0.2685 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 774 | semis|drop_revert(drop=0.1,hold=10,n=3) | 3.43/0.41/-6.67 | -38.66 | 34 | 0.0271 | 0.09391 (-20.81) | 1.0 | 0.0187 | 0.278 | False | min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
