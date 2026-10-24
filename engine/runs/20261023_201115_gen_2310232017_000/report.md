# gen_2310232017_000 — engine run 20261023_201115_gen_2310232017_000

Hypothesis: grammar draw seed=2310232017: drop_revert+day_of_week

**0/32 pass.** Ledger N at evaluation: 878. PBO (CSCV) across family: 0.896. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 83553f7bd162ee48c01a436a0ea82b0552dd5ce54ae372f8c266b35534c61d03. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 847 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=0) | -0.67/-0.02/-8.28 | 214.9 | 349 | 0.0293 | 1.0 (77.45) | 1.0 | 0.0003 | 0.49 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 848 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=1) | 20.28/0.74/-3.77 | 214.9 | 358 | 0.0298 | 1.0 (77.85) | 1.0 | 0.0013 | 0.495 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 849 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=2) | -14.15/-1.21/-19.49 | 214.9 | 352 | 0.0299 | 1.0 (77.92) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 850 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=3) | 12.0/0.96/-4.21 | 214.9 | 355 | 0.0293 | 1.0 (76.2) | 1.0 | 0.0479 | 0.4935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 851 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -3.18/-0.18/-9.93 | 214.9 | 443 | 0.0319 | 1.0 (76.06) | 1.0 | 0.0001 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 852 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 13.45/0.5/-5.64 | 214.9 | 465 | 0.0318 | 0.999 (75.7) | 1.0 | 0.0013 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 853 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -8.41/-0.57/-15.07 | 214.9 | 469 | 0.0322 | 1.0 (76.07) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 854 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 11.54/0.79/-4.14 | 214.9 | 462 | 0.0313 | 1.0 (76.11) | 1.0 | 0.0258 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 855 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -2.05/-0.09/-9.93 | 214.9 | 562 | 0.0313 | 1.0 (73.84) | 1.0 | 0.0002 | 0.49 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 856 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 23.9/0.8/-5.25 | 214.9 | 599 | 0.0308 | 0.998 (75.84) | 1.0 | 0.0035 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 857 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -16.03/-1.04/-23.14 | 214.9 | 591 | 0.031 | 1.0 (74.3) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 858 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 10.75/0.6/-8.07 | 214.9 | 599 | 0.0306 | 1.0 (73.44) | 1.0 | 0.0153 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 859 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -1.68/-0.07/-9.93 | 214.9 | 682 | 0.033 | 1.0 (73.21) | 1.0 | 0.0002 | 0.4935 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 860 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 23.65/0.75/-6.0 | 214.9 | 734 | 0.0331 | 0.99401 (73.11) | 1.0 | 0.0051 | 0.4935 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 861 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -12.45/-0.67/-20.47 | 214.9 | 744 | 0.0331 | 1.0 (72.57) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 862 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 9.46/0.52/-7.49 | 214.9 | 725 | 0.0324 | 1.0 (72.65) | 1.0 | 0.0085 | 0.4875 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 863 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=0) | -4.37/-0.58/-4.88 | 214.9 | 54 | 0.0212 | 1.0 (78.43) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 864 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=1) | 9.25/0.59/-1.96 | 214.9 | 53 | 0.0208 | 1.0 (81.47) | 1.0 | 0.0001 | 0.49 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 865 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=2) | -0.58/-0.15/-2.49 | 214.9 | 50 | 0.0217 | 1.0 (79.69) | 1.0 | 0.0001 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 866 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=3) | 4.56/0.89/-0.54 | 214.9 | 53 | 0.0203 | 1.0 (80.52) | 1.0 | 0.0001 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 867 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | -4.73/-0.56/-7.01 | 214.9 | 94 | 0.023 | 1.0 (78.89) | 1.0 | 0.0 | 0.494 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 868 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 10.08/0.59/-2.47 | 214.9 | 101 | 0.0238 | 1.0 (80.37) | 1.0 | 0.0003 | 0.4925 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 869 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | 0.63/0.14/-3.28 | 214.9 | 90 | 0.023 | 1.0 (79.94) | 1.0 | 0.0008 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 870 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | 4.97/0.72/-1.85 | 214.9 | 101 | 0.0234 | 1.0 (78.21) | 1.0 | 0.0094 | 0.495 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 871 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=0) | -2.22/-0.21/-6.78 | 214.9 | 95 | 0.0212 | 1.0 (78.14) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 872 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=1) | 10.12/0.61/-2.85 | 214.9 | 94 | 0.0212 | 1.0 (80.19) | 1.0 | 0.0002 | 0.4925 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 873 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=2) | -1.82/-0.34/-4.17 | 214.9 | 91 | 0.0218 | 1.0 (80.99) | 1.0 | 0.0001 | 0.4945 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 874 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=3) | 5.22/0.8/-1.55 | 214.9 | 94 | 0.0212 | 1.0 (80.03) | 1.0 | 0.0046 | 0.493 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 875 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=0) | -4.05/-0.39/-8.13 | 214.9 | 152 | 0.0237 | 1.0 (79.3) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 876 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=1) | 12.08/0.66/-3.08 | 214.9 | 166 | 0.0245 | 1.0 (79.16) | 1.0 | 0.0008 | 0.4935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 877 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=2) | -0.41/-0.05/-4.91 | 214.9 | 155 | 0.024 | 1.0 (79.25) | 1.0 | 0.0003 | 0.494 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 878 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=3) | 3.72/0.46/-3.6 | 214.9 | 170 | 0.0239 | 1.0 (74.77) | 1.0 | 0.0033 | 0.4975 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
