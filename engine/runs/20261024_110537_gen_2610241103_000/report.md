# gen_2610241103_000 — engine run 20261024_110537_gen_2610241103_000

Hypothesis: grammar draw seed=2610241103: supertrend

**0/4 pass.** Ledger N at evaluation: 2402. PBO (CSCV) across family: 0.796. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d86245e1f9e893d655721419036693df3cfa57efcd4218f55a79c87487da1691. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2399 | index|supertrend(atr_n=10,mult=3) | 58.64/1.38/-10.15 | 107.42 | 81 | 0.066 | 0.16783 (43.2) | 1.0 | 0.9724 | 0.973 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2400 | index|supertrend(atr_n=10,mult=4) | 52.07/1.29/-11.25 | 107.42 | 54 | 0.0728 | 0.28472 (43.57) | 1.0 | 0.9598 | 0.522 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2401 | index|supertrend(atr_n=14,mult=3) | 65.0/1.46/-9.93 | 107.42 | 81 | 0.0628 | 0.08092 (42.99) | 1.0 | 0.9806 | 0.9575 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2402 | index|supertrend(atr_n=14,mult=4) | 56.84/1.36/-11.63 | 107.42 | 51 | 0.0647 | 0.1968 (44.28) | 1.0 | 0.9698 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
