# gen_2610240909_000 — engine run 20261024_091203_gen_2610240909_000

Hypothesis: grammar draw seed=2610240909: supertrend

**0/4 pass.** Ledger N at evaluation: 2242. PBO (CSCV) across family: 0.863. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 3fdb7bafe2930976587f2ae1e7b5b45d18fd15bde2fc0a25d0fbbe7f1fe5cee6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2239 | megacap|supertrend(atr_n=7,mult=2) | 157.58/1.9/-15.61 | 311.91 | 395 | 0.041 | 0.02498 (103.38) | 1.0 | 0.993 | 0.475 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2240 | megacap|supertrend(atr_n=7,mult=4) | 123.46/1.61/-11.54 | 311.91 | 141 | 0.0405 | 0.24875 (106.6) | 1.0 | 0.9715 | 0.505 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2241 | megacap|supertrend(atr_n=10,mult=2) | 164.25/1.93/-16.52 | 311.91 | 394 | 0.0404 | 0.01499 (103.27) | 1.0 | 0.994 | 0.469 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2242 | megacap|supertrend(atr_n=10,mult=4) | 136.31/1.73/-11.04 | 311.91 | 143 | 0.0405 | 0.13087 (105.63) | 1.0 | 0.9829 | 0.503 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
