# gen_2310231908_000 — engine run 20261023_200433_gen_2310231908_000

Hypothesis: grammar draw seed=2310231908: drop_revert

**0/8 pass.** Ledger N at evaluation: 766. PBO (CSCV) across family: 0.7. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 2408c906133fef57aa3063b5420e324ff9bc69f832ee46d04a55dfdd187e6bc2. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 759 | semis|drop_revert(drop=0.1,hold=3,n=1) | 0.05/0.03/-2.7 | -38.66 | 17 | 0.0221 | 0.11688 (-22.2) | 1.0 | 0.0116 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 760 | semis|drop_revert(drop=0.1,hold=3,n=3) | 0.67/0.13/-3.61 | -38.66 | 37 | 0.0263 | 0.12388 (-22.07) | 1.0 | 0.0034 | 0.2935 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 761 | semis|drop_revert(drop=0.1,hold=5,n=1) | 2.02/0.51/-2.76 | -38.66 | 17 | 0.0221 | 0.1049 (-22.28) | 1.0 | 0.046 | 0.289 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 762 | semis|drop_revert(drop=0.1,hold=5,n=3) | -5.92/-0.85/-6.97 | -38.66 | 35 | 0.0271 | 0.20879 (-21.35) | 1.0 | 0.0 | 0.332 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 763 | semis|drop_revert(drop=0.15,hold=3,n=1) | 0.04/0.04/-0.75 | -38.66 | 6 | 0.002 | 0.12787 (-20.42) | 1.0 | 0.0136 | 0.3 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 764 | semis|drop_revert(drop=0.15,hold=3,n=3) | -0.19/-0.03/-2.73 | -38.66 | 16 | 0.0272 | 0.12987 (-20.55) | 1.0 | 0.0039 | 0.2965 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 765 | semis|drop_revert(drop=0.15,hold=5,n=1) | 0.73/0.64/-0.57 | -38.66 | 6 | 0.002 | 0.10589 (-20.9) | 1.0 | 0.063 | 0.292 | False | min_trades, holm, dsr, spa, pbo |
| 766 | semis|drop_revert(drop=0.15,hold=5,n=3) | -1.23/-0.28/-2.92 | -38.66 | 16 | 0.0272 | 0.13786 (-21.61) | 1.0 | 0.0003 | 0.302 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
