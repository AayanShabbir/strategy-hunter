# gen_2410240522_000 — engine run 20261024_051253_gen_2410240522_000

Hypothesis: grammar draw seed=2410240522: drop_revert

**0/8 pass.** Ledger N at evaluation: 1862. PBO (CSCV) across family: 0.151. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 85a0e9f98ac6a88a7326cebc026049768f387093be34aa61dc831d9227153aff. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1855 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 62.38 | 5 | 0.0228 | 1.0 (28.31) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1856 | BROAD|drop_revert(drop=0.1,hold=5,n=3) | 6.45/0.43/-3.61 | 62.38 | 20 | 0.029 | 0.99301 (28.52) | 1.0 | 0.2823 | 0.494 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1857 | BROAD|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 62.38 | 5 | 0.0228 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1858 | BROAD|drop_revert(drop=0.1,hold=10,n=3) | 12.17/0.74/-3.69 | 62.38 | 19 | 0.0291 | 0.95105 (28.22) | 1.0 | 0.521 | 0.976 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1859 | BROAD|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 62.38 | 2 | 0.0151 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1860 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.81/0.23/-1.14 | 62.38 | 4 | 0.0212 | 0.998 (28.54) | 1.0 | 0.1962 | 0.4945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1861 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 62.38 | 2 | 0.0151 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1862 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 1.61/0.43/-1.14 | 62.38 | 4 | 0.0212 | 0.98901 (28.2) | 1.0 | 0.3034 | 0.494 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
