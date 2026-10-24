# gen_2610241020_000 — engine run 20261024_101021_gen_2610241020_000

Hypothesis: grammar draw seed=2610241020: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2374. PBO (CSCV) across family: 0.119. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 7f59042b90e3b0fcc813e8c8367fb5d26ad60963002466baffbf02d862ecfaf9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2367 | crypto|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=100) | 1.63/0.49/-1.02 | 434.62 | 20 | 0.0103 | 0.91009 (46.99) | 1.0 | 0.027 | 0.905 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2368 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=100) | 5.13/0.4/-6.87 | 434.62 | 67 | 0.0123 | 0.91608 (224.56) | 1.0 | 0.048 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2369 | crypto|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=100) | -1.94/-0.37/-4.45 | 434.62 | 21 | 0.0112 | 0.97602 (43.39) | 1.0 | 0.005 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2370 | crypto|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=100) | 4.42/0.31/-11.09 | 434.62 | 69 | 0.0133 | 0.88312 (91.9) | 1.0 | 0.0408 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2371 | crypto|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 434.62 | 3 | 0.0044 | 1.0 (41.55) | 1.0 | 0.0 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2372 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=100) | 6.7/1.15/-1.96 | 434.62 | 21 | 0.0112 | 0.89411 (239.02) | 1.0 | 0.1919 | 0.9015 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2373 | crypto|drop_revert(drop=0.15,hold=5,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 434.62 | 3 | 0.0044 | 1.0 (311.64) | 1.0 | 0.0 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2374 | crypto|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=100) | 0.34/0.07/-4.45 | 434.62 | 23 | 0.0103 | 0.94505 (150.78) | 1.0 | 0.022 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
