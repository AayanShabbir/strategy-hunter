# gen_2610240903_000 — engine run 20261024_091146_gen_2610240903_000

Hypothesis: grammar draw seed=2610240903: drop_revert

**0/8 pass.** Ledger N at evaluation: 2206. PBO (CSCV) across family: 0.453. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-09-16.
Spec sha256 aca2c32e7956fe18e019cf0843a5cb6bff792e3e1eecfb2c66416819546d6562. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2199 | crypto|drop_revert(drop=0.1,hold=3,n=1) | 25.31/1.18/-6.2 | 41.29 | 31 | 0.008 | 0.41858 (16.58) | 1.0 | 0.0719 | 0.7325 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2200 | crypto|drop_revert(drop=0.1,hold=3,n=5) | -1.92/0.22/-37.63 | 41.29 | 69 | 0.0097 | 0.67133 (17.94) | 1.0 | 0.0174 | 0.8255 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2201 | crypto|drop_revert(drop=0.1,hold=5,n=1) | 15.99/0.69/-11.59 | 41.29 | 28 | 0.0081 | 0.51049 (17.82) | 1.0 | 0.0381 | 0.7595 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2202 | crypto|drop_revert(drop=0.1,hold=5,n=5) | -4.76/0.2/-39.37 | 41.29 | 61 | 0.01 | 0.65335 (16.42) | 1.0 | 0.0163 | 0.8295 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2203 | crypto|drop_revert(drop=0.15,hold=3,n=1) | -2.09/-0.24/-6.2 | 41.29 | 9 | 0.0069 | 0.93207 (18.52) | 1.0 | 0.0027 | 0.8425 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2204 | crypto|drop_revert(drop=0.15,hold=3,n=5) | 74.79/1.61/-15.21 | 41.29 | 41 | 0.0089 | 0.12787 (17.92) | 1.0 | 0.1914 | 0.5365 | False | min_trades, holm, dsr, spa |
| 2205 | crypto|drop_revert(drop=0.15,hold=5,n=1) | -2.47/-0.15/-6.64 | 41.29 | 9 | 0.0069 | 0.84316 (17.65) | 1.0 | 0.0067 | 0.8405 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2206 | crypto|drop_revert(drop=0.15,hold=5,n=5) | 10.91/0.43/-31.25 | 41.29 | 39 | 0.0089 | 0.57043 (17.86) | 1.0 | 0.0286 | 0.761 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
