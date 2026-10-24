# gen_2610241213_000 — engine run 20261024_120804_gen_2610241213_000

Hypothesis: grammar draw seed=2610241213: supertrend+trend_sma

**0/4 pass.** Ledger N at evaluation: 2574. PBO (CSCV) across family: 0.903. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 2015707410ea65380c4564cf44b67ab8cfff80da6ab470af999c994390988cb4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2571 | index|supertrend(atr_n=7,mult=2)+trend_sma(n=100) | 38.22/1.13/-7.03 | 107.42 | 137 | 0.0734 | 0.6024 (42.08) | 1.0 | 0.7987 | 0.49 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2572 | index|supertrend(atr_n=7,mult=4)+trend_sma(n=100) | 57.64/1.52/-6.83 | 107.42 | 55 | 0.0781 | 0.15584 (43.94) | 1.0 | 0.934 | 0.966 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2573 | index|supertrend(atr_n=14,mult=2)+trend_sma(n=100) | 42.8/1.22/-8.17 | 107.42 | 144 | 0.0713 | 0.46553 (41.36) | 1.0 | 0.8393 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2574 | index|supertrend(atr_n=14,mult=4)+trend_sma(n=100) | 56.15/1.42/-9.46 | 107.42 | 58 | 0.0643 | 0.20879 (44.07) | 1.0 | 0.9086 | 0.515 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
