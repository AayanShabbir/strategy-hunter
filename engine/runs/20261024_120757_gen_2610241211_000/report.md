# gen_2610241211_000 — engine run 20261024_120757_gen_2610241211_000

Hypothesis: grammar draw seed=2610241211: supertrend+trend_sma

**0/4 pass.** Ledger N at evaluation: 2554. PBO (CSCV) across family: 0.852. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 8af301975a3cd3c544925e7899ee4fd9bdd02bf2c9300b481651a759200ca3e6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2551 | megacap|supertrend(atr_n=7,mult=3)+trend_sma(n=100) | 26.85/0.68/-16.95 | 118.49 | 89 | 0.0496 | 0.7952 (45.83) | 1.0 | 0.7388 | 0.5105 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2552 | megacap|supertrend(atr_n=7,mult=4)+trend_sma(n=100) | 29.13/0.73/-20.48 | 118.49 | 65 | 0.0496 | 0.76723 (47.17) | 1.0 | 0.7641 | 0.505 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2553 | megacap|supertrend(atr_n=10,mult=3)+trend_sma(n=100) | 34.44/0.84/-16.96 | 118.49 | 91 | 0.0478 | 0.67433 (45.68) | 1.0 | 0.8173 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2554 | megacap|supertrend(atr_n=10,mult=4)+trend_sma(n=100) | 36.45/0.87/-19.39 | 118.49 | 66 | 0.0492 | 0.68531 (48.12) | 1.0 | 0.8335 | 0.515 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
