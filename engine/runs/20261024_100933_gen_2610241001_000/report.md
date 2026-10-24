# gen_2610241001_000 — engine run 20261024_100933_gen_2610241001_000

Hypothesis: grammar draw seed=2610241001: supertrend

**0/4 pass.** Ledger N at evaluation: 2282. PBO (CSCV) across family: 0.837. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 1ed1ac17db85894c9dc66eecab8ceb516b7b1eaf07060ab16711b899c8425001. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2279 | index|supertrend(atr_n=10,mult=2) | 57.8/1.35/-13.15 | 107.42 | 136 | 0.0734 | 0.15085 (41.06) | 1.0 | 0.9808 | 0.4875 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2280 | index|supertrend(atr_n=10,mult=4) | 52.07/1.29/-11.25 | 107.42 | 54 | 0.0728 | 0.27373 (43.94) | 1.0 | 0.9738 | 0.522 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2281 | index|supertrend(atr_n=14,mult=2) | 59.49/1.38/-13.51 | 107.42 | 140 | 0.0712 | 0.11688 (41.71) | 1.0 | 0.9833 | 0.978 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2282 | index|supertrend(atr_n=14,mult=4) | 56.84/1.36/-11.63 | 107.42 | 51 | 0.0647 | 0.1978 (43.55) | 1.0 | 0.9808 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
