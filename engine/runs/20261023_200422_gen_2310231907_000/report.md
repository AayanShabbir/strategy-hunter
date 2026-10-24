# gen_2310231907_000 — engine run 20261023_200422_gen_2310231907_000

Hypothesis: grammar draw seed=2310231907: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 742. PBO (CSCV) across family: 0.8. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 307586a17b34e51fa31f7d0c64fb71915aad4bdaede32b0a077f080c0febe8b8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 735 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.2) | -5.18/-0.16/-17.72 | 268.18 | 301 | 0.0119 | 0.90909 (78.08) | 1.0 | 0.0198 | 0.8935 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 736 | crypto_d|drop_revert(drop=0.05,hold=3,n=3)+relvol(min_ratio=1.2) | -9.19/-0.3/-19.22 | 268.18 | 369 | 0.0131 | 0.93806 (117.85) | 1.0 | 0.0133 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 737 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.2) | -25.47/-0.79/-29.27 | 268.18 | 486 | 0.0128 | 0.97902 (106.97) | 1.0 | 0.0018 | 0.912 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 738 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.2) | -8.26/-0.12/-31.02 | 268.18 | 601 | 0.0139 | 0.8961 (109.22) | 1.0 | 0.0212 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 739 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+relvol(min_ratio=1.2) | 10.81/0.84/-5.71 | 268.18 | 81 | 0.0098 | 0.79121 (71.57) | 1.0 | 0.1327 | 0.878 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 740 | crypto_d|drop_revert(drop=0.1,hold=3,n=3)+relvol(min_ratio=1.2) | 7.42/0.42/-9.91 | 268.18 | 165 | 0.0114 | 0.8002 (69.87) | 1.0 | 0.0775 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 741 | crypto_d|drop_revert(drop=0.1,hold=10,n=1)+relvol(min_ratio=1.2) | -6.92/-0.25/-15.72 | 268.18 | 138 | 0.01 | 0.93606 (132.4) | 1.0 | 0.012 | 0.8955 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 742 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+relvol(min_ratio=1.2) | -0.16/0.1/-16.63 | 268.18 | 319 | 0.0116 | 0.88811 (140.73) | 1.0 | 0.0399 | 0.8915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
