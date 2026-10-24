# gen_2410240526_000 — engine run 20261024_051304_gen_2410240526_000

Hypothesis: grammar draw seed=2410240526: drop_revert

**0/8 pass.** Ledger N at evaluation: 1886. PBO (CSCV) across family: 0.463. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 557905cef14d03562a0e9add4cb9e713b690b77e6d77069ff0767bd7fcdb182a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1879 | BROAD|drop_revert(drop=0.05,hold=3,n=3) | 11.27/0.79/-2.08 | 78.13 | 88 | 0.0408 | 0.96603 (32.86) | 1.0 | 0.7958 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1880 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 7.47/0.52/-4.63 | 78.13 | 125 | 0.0483 | 0.996 (34.29) | 1.0 | 0.5368 | 0.508 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1881 | BROAD|drop_revert(drop=0.05,hold=5,n=3) | 12.27/0.83/-2.08 | 78.13 | 85 | 0.041 | 0.97602 (33.79) | 1.0 | 0.825 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1882 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 9.8/0.65/-4.91 | 78.13 | 122 | 0.0489 | 0.99001 (33.34) | 1.0 | 0.644 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1883 | BROAD|drop_revert(drop=0.15,hold=3,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1884 | BROAD|drop_revert(drop=0.15,hold=3,n=5) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0222 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1885 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1886 | BROAD|drop_revert(drop=0.15,hold=5,n=5) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0222 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
