# gen_2410240518_000 — engine run 20261024_051241_gen_2410240518_000

Hypothesis: grammar draw seed=2410240518: drop_revert

**0/8 pass.** Ledger N at evaluation: 1834. PBO (CSCV) across family: 1.0. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 de4f81afb6b271befd800fb2d1cde7efcef3b7cb1a5bcb67a09d45ca2de69301. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1827 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0175 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1828 | BROAD|drop_revert(drop=0.1,hold=5,n=3) | 3.23/0.27/-2.57 | 78.13 | 10 | 0.0287 | 0.996 (33.6) | 1.0 | 0.6384 | 0.503 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1829 | BROAD|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0175 | 1.0 (32.58) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1830 | BROAD|drop_revert(drop=0.1,hold=10,n=3) | 3.99/0.31/-3.42 | 78.13 | 10 | 0.0287 | 0.995 (32.5) | 1.0 | 0.6638 | 0.504 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1831 | BROAD|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 78.13 | 0 | inf | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1832 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1833 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 78.13 | 0 | inf | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1834 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
