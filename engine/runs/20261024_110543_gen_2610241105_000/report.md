# gen_2610241105_000 — engine run 20261024_110543_gen_2610241105_000

Hypothesis: grammar draw seed=2610241105: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2414. PBO (CSCV) across family: 0.466. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 4c22390ea47a2372711197031b00ceb5f3be3ce7599ebf5fb27f535138e178b0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2407 | crypto|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=200) | 8.1/0.63/-5.36 | 434.62 | 37 | 0.0131 | 0.88212 (260.45) | 1.0 | 0.2975 | 0.901 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2408 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=200) | 14.68/0.87/-4.79 | 434.62 | 44 | 0.0157 | 0.77722 (62.97) | 1.0 | 0.4243 | 0.894 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2409 | crypto|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=200) | 5.39/0.38/-9.38 | 434.62 | 36 | 0.0152 | 0.86913 (214.68) | 1.0 | 0.2136 | 0.902 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2410 | crypto|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=200) | 12.95/0.7/-10.32 | 434.62 | 44 | 0.0159 | 0.7952 (260.09) | 1.0 | 0.3462 | 0.8975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2411 | crypto|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=200) | 8.0/0.84/-1.96 | 434.62 | 7 | 0.0105 | 0.91508 (306.5) | 1.0 | 0.3737 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2412 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=200) | 12.17/1.16/-1.96 | 434.62 | 16 | 0.0112 | 0.81918 (64.05) | 1.0 | 0.6179 | 0.896 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2413 | crypto|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=200) | 2.74/0.29/-6.67 | 434.62 | 7 | 0.0105 | 0.92208 (175.66) | 1.0 | 0.1722 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2414 | crypto|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=200) | 4.71/0.45/-6.67 | 434.62 | 16 | 0.0112 | 0.90509 (274.31) | 1.0 | 0.2237 | 0.9025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
