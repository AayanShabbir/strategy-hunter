# gen_2410240317_000 — engine run 20261024_030953_gen_2410240317_000

Hypothesis: grammar draw seed=2410240317: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1674. PBO (CSCV) across family: 0.805. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4089134b3efdeb9cada25553cf8b7d2f5e4e0f8958e6529e05d3350e22fc4928. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1667 | semis|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 1.53/0.55/-0.47 | 440.15 | 3 | 0.0179 | 0.998 (142.87) | 1.0 | 0.171 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1668 | semis|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=50) | 0.77/0.17/-2.47 | 440.15 | 27 | 0.0195 | 1.0 (137.67) | 1.0 | 0.0962 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1669 | semis|drop_revert(drop=0.1,hold=10,n=1)+trend_sma(n=50) | 3.12/0.54/-1.23 | 440.15 | 9 | 0.0185 | 1.0 (139.7) | 1.0 | 0.2512 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1670 | semis|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=50) | 10.87/1.12/-2.12 | 440.15 | 56 | 0.019 | 1.0 (141.29) | 1.0 | 0.6447 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1671 | semis|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 1.01/0.59/-0.25 | 440.15 | 1 | 0.0179 | 0.996 (144.66) | 1.0 | 0.1883 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1672 | semis|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=50) | 0.99/0.51/-0.32 | 440.15 | 5 | 0.0195 | 0.99301 (143.83) | 1.0 | 0.1812 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1673 | semis|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=50) | 2.21/0.7/-0.62 | 440.15 | 2 | 0.0141 | 0.99301 (141.49) | 1.0 | 0.3242 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1674 | semis|drop_revert(drop=0.15,hold=10,n=3)+trend_sma(n=50) | 2.53/0.8/-0.62 | 440.15 | 10 | 0.0183 | 0.99201 (137.24) | 1.0 | 0.4008 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
