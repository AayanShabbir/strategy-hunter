# gen_2410240708_000 — engine run 20261024_070510_gen_2410240708_000

Hypothesis: grammar draw seed=2410240708: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2038. PBO (CSCV) across family: 0.716. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4edbf656f7330cb2f13906a9dc4698899feea930c963342b69499194fd90ca64. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2031 | BROAD|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=100) | 1.85/1.0/-0.26 | 78.13 | 26 | 0.0474 | 0.99301 (34.36) | 1.0 | 0.8917 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2032 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=100) | 2.97/1.03/-0.67 | 78.13 | 43 | 0.0514 | 0.999 (34.15) | 1.0 | 0.8186 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2033 | BROAD|drop_revert(drop=0.05,hold=10,n=3)+trend_sma(n=100) | 4.52/1.13/-0.74 | 78.13 | 47 | 0.0475 | 0.998 (34.32) | 1.0 | 0.9075 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2034 | BROAD|drop_revert(drop=0.05,hold=10,n=5)+trend_sma(n=100) | 7.47/1.36/-1.01 | 78.13 | 65 | 0.0515 | 0.998 (33.41) | 1.0 | 0.9417 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2035 | BROAD|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 2 | 0.0315 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2036 | BROAD|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 2 | 0.0384 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2037 | BROAD|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0351 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2038 | BROAD|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 4 | 0.0363 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
