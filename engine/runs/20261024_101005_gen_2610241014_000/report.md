# gen_2610241014_000 — engine run 20261024_101005_gen_2610241014_000

Hypothesis: grammar draw seed=2610241014: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2346. PBO (CSCV) across family: 0.234. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 a73304071e548e07c9fe2ce1eaa1df7fbf2feb311a4b387ece74158699bfd22b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2339 | BROAD|drop_revert(drop=0.05,hold=3,n=1)+trend_sma(n=200) | -0.71/-0.3/-1.48 | 83.36 | 14 | 0.0312 | 0.99101 (35.66) | 1.0 | 0.0001 | 0.4975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2340 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | 4.4/0.49/-4.32 | 83.36 | 50 | 0.0424 | 0.98402 (33.06) | 1.0 | 0.0251 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2341 | BROAD|drop_revert(drop=0.05,hold=5,n=1)+trend_sma(n=200) | -0.24/-0.07/-1.33 | 83.36 | 14 | 0.0342 | 0.98102 (36.61) | 1.0 | 0.0014 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2342 | BROAD|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 7.0/0.65/-5.43 | 83.36 | 52 | 0.043 | 0.96903 (34.4) | 1.0 | 0.0441 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2343 | BROAD|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=200) | 0.0/0.0/0.0 | 83.36 | 1 | 0.0201 | 1.0 (38.63) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2344 | BROAD|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=200) | 0.33/0.41/-0.12 | 83.36 | 4 | 0.036 | 0.97203 (37.13) | 1.0 | 0.0011 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2345 | BROAD|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=200) | 0.0/0.0/0.0 | 83.36 | 1 | 0.0201 | 1.0 (33.7) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2346 | BROAD|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=200) | 1.18/0.99/0.0 | 83.36 | 4 | 0.036 | 0.96903 (35.23) | 1.0 | 0.0079 | 0.505 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
