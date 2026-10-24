# gen_2310232018_000 — engine run 20261023_201123_gen_2310232018_000

Hypothesis: grammar draw seed=2310232018: drop_revert

**0/8 pass.** Ledger N at evaluation: 886. PBO (CSCV) across family: 0.051. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b1ff3521dc9a458f454a3452e609c01078b8cbe2db92409f10836995c21b3465. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 879 | sector_etf|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 63.33 | 8 | 0.0161 | 1.0 (28.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 880 | sector_etf|drop_revert(drop=0.1,hold=3,n=3) | 5.2/0.34/-3.57 | 63.33 | 26 | 0.0275 | 0.999 (28.56) | 1.0 | 0.3779 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 881 | sector_etf|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 63.33 | 7 | 0.017 | 1.0 (29.67) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 882 | sector_etf|drop_revert(drop=0.1,hold=5,n=3) | 7.44/0.46/-3.57 | 63.33 | 24 | 0.0279 | 0.996 (28.09) | 1.0 | 0.4747 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 883 | sector_etf|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 63.33 | 3 | 0.0153 | 1.0 (29.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 884 | sector_etf|drop_revert(drop=0.15,hold=3,n=3) | 0.27/0.11/-0.93 | 63.33 | 7 | 0.0197 | 0.99001 (28.64) | 1.0 | 0.2531 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 885 | sector_etf|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 63.33 | 3 | 0.0153 | 1.0 (29.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 886 | sector_etf|drop_revert(drop=0.15,hold=5,n=3) | 0.59/0.22/-0.93 | 63.33 | 7 | 0.0197 | 0.99201 (27.92) | 1.0 | 0.321 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
