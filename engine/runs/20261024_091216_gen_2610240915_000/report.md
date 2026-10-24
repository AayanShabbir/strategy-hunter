# gen_2610240915_000 — engine run 20261024_091216_gen_2610240915_000

Hypothesis: grammar draw seed=2610240915: supertrend

**0/4 pass.** Ledger N at evaluation: 2266. PBO (CSCV) across family: 0.879. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 9b85522a2c854130e7978ece78c08294b7a65a0a8ab54ea4fc1178c5b9c5a083. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2263 | megacap|supertrend(atr_n=7,mult=2) | 138.59/1.72/-20.27 | 273.72 | 260 | 0.0404 | 0.06693 (92.1) | 1.0 | 0.9597 | 0.4915 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2264 | megacap|supertrend(atr_n=7,mult=4) | 91.79/1.31/-16.01 | 273.72 | 98 | 0.0419 | 0.51748 (96.34) | 1.0 | 0.8511 | 0.511 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2265 | megacap|supertrend(atr_n=10,mult=2) | 146.25/1.75/-21.28 | 273.72 | 263 | 0.0403 | 0.04196 (90.14) | 1.0 | 0.9645 | 0.4805 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2266 | megacap|supertrend(atr_n=10,mult=4) | 108.34/1.5/-16.14 | 273.72 | 98 | 0.0414 | 0.33167 (95.45) | 1.0 | 0.9135 | 0.5115 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
