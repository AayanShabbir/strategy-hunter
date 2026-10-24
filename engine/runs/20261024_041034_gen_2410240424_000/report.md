# gen_2410240424_000 — engine run 20261024_041034_gen_2410240424_000

Hypothesis: grammar draw seed=2410240424: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1786. PBO (CSCV) across family: 0.413. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 44f50248c74957805e118fd8c66a4ee6b9ba7db4bc3f53e9f66e5d77c5692bed. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1779 | MEGA|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=50) | 8.51/0.88/-4.26 | 287.89 | 330 | 0.0281 | 1.0 (98.47) | 1.0 | 0.1573 | 0.4835 | False | beats_buy_hold, holm, dsr, spa |
| 1780 | MEGA|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=50) | 2.46/0.26/-7.19 | 287.89 | 378 | 0.0308 | 1.0 (96.66) | 1.0 | 0.0178 | 0.4855 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1781 | MEGA|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=50) | 9.18/0.79/-5.39 | 287.89 | 398 | 0.0287 | 1.0 (98.67) | 1.0 | 0.1188 | 0.4885 | False | beats_buy_hold, holm, dsr, spa |
| 1782 | MEGA|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=50) | -0.78/-0.04/-8.9 | 287.89 | 459 | 0.031 | 1.0 (96.7) | 1.0 | 0.0042 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1783 | MEGA|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=50) | 4.5/1.31/-0.48 | 287.89 | 39 | 0.0195 | 1.0 (103.3) | 1.0 | 0.3357 | 0.4905 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1784 | MEGA|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 2.5/0.66/-1.31 | 287.89 | 56 | 0.0218 | 1.0 (101.39) | 1.0 | 0.0674 | 0.489 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1785 | MEGA|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=50) | 2.78/0.62/-1.79 | 287.89 | 49 | 0.0192 | 1.0 (99.04) | 1.0 | 0.0651 | 0.4905 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1786 | MEGA|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=50) | 0.79/0.16/-3.44 | 287.89 | 74 | 0.0217 | 1.0 (101.85) | 1.0 | 0.0119 | 0.488 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
