# gen_2410240700_000 — engine run 20261024_070438_gen_2410240700_000

Hypothesis: grammar draw seed=2410240700: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1994. PBO (CSCV) across family: 0.679. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 72e98423df033fa1e7a95adc98fd2c92eaf3f6c6fae847259077bbb0896c3183. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1987 | crypto|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0165 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1988 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 21 | 0.0165 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1989 | crypto|drop_revert(drop=0.1,hold=10,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 5 | 0.017 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1990 | crypto|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=50) | 0.37/0.83/0.0 | 428.6 | 37 | 0.0179 | 0.92607 (42.33) | 1.0 | nan | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1991 | crypto|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 1 | 0.016 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1992 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 3 | 0.0143 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1993 | crypto|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 1 | 0.016 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1994 | crypto|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 3 | 0.0143 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
