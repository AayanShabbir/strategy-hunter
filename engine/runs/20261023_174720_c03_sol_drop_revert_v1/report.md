# c03_sol_drop_revert_v1 — engine run 20261023_174720_c03_sol_drop_revert_v1

Hypothesis: After a sharp sell-off (3-day return below -15% or -25%) buying SOL/alts and holding a fixed 3 or 7 days beats buy-and-hold OOS net of 35 bps/side (short-term reversal / liquidity provision, Kozlowski et al. 2021; note Zaremba et al. 2021 find the largest coins show daily momentum instead, so this is a genuine test). 5x ATR stop. Strategy Scout crypto submission.

**0/8 pass.** Ledger N at evaluation: 482. PBO (CSCV) across family: 0.638. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6822eb6ee5a39eb65332130805986110099914e53b0220659da762ebdff1aa83. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 475 | SOL|drop_revert(drop=0.15,hold=3,n=3) | 10.9/0.46/-10.19 | 923.45 | 28 | 0.0106 | 0.59241 (54.4) | 1.0 | 0.3798 | 0.881 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 476 | SOL|drop_revert(drop=0.15,hold=7,n=3) | 6.67/0.25/-33.8 | 923.45 | 22 | 0.0123 | 0.65634 (69.99) | 1.0 | 0.2768 | 0.8795 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 477 | SOL|drop_revert(drop=0.25,hold=3,n=3) | 0.0/0.0/0.0 | 923.45 | 6 | 0.0078 | 1.0 (0.0) | 1.0 | 0.0 | 0.8915 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 478 | SOL|drop_revert(drop=0.25,hold=7,n=3) | 0.0/0.0/0.0 | 923.45 | 6 | 0.0078 | 1.0 (919.87) | 1.0 | 0.0 | 0.8915 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 479 | ALTS|drop_revert(drop=0.15,hold=3,n=3) | 14.41/0.5/-11.46 | 193.2 | 170 | 0.0119 | 0.75824 (72.15) | 1.0 | 0.4079 | 0.88 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 480 | ALTS|drop_revert(drop=0.15,hold=7,n=3) | 14.27/0.4/-18.64 | 193.2 | 148 | 0.0126 | 0.74426 (89.61) | 1.0 | 0.357 | 0.8785 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 481 | ALTS|drop_revert(drop=0.25,hold=3,n=3) | 3.12/0.61/-1.65 | 193.2 | 31 | 0.0082 | 0.97902 (40.51) | 1.0 | 0.4712 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 482 | ALTS|drop_revert(drop=0.25,hold=7,n=3) | -0.04/0.01/-5.18 | 193.2 | 29 | 0.0089 | 0.99101 (38.02) | 1.0 | 0.1759 | 0.8995 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
