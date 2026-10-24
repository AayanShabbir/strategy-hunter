# gen_2410240121_000 — engine run 20261024_010754_gen_2410240121_000

Hypothesis: grammar draw seed=2410240121: donchian+rsi_band

**0/4 pass.** Ledger N at evaluation: 1434. PBO (CSCV) across family: 0.889. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 c7a386e4747a0ccf0b1f786f89d9a69b460fd190b8c9485b3b33b9bdfdac9147. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1431 | crypto|donchian(entry_n=55,exit_n=10)+rsi_band(hi=70) | 191.15/0.79/-28.31 | 428.6 | 2083 | 0.0967 | 0.36663 (141.98) | 1.0 | 0.9212 | 0.97 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1432 | crypto|donchian(entry_n=55,exit_n=20)+rsi_band(hi=70) | 157.95/0.75/-42.7 | 428.6 | 2024 | 0.0973 | 0.43756 (121.61) | 1.0 | 0.8952 | 0.5095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1433 | crypto|donchian(entry_n=100,exit_n=10)+rsi_band(hi=70) | 245.17/0.86/-17.53 | 428.6 | 1478 | 0.0944 | 0.24875 (102.81) | 1.0 | 0.9523 | 0.9355 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1434 | crypto|donchian(entry_n=100,exit_n=20)+rsi_band(hi=70) | 244.41/0.86/-27.45 | 428.6 | 1453 | 0.0953 | 0.27772 (132.1) | 1.0 | 0.9514 | 0.942 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
