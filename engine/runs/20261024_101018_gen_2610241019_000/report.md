# gen_2610241019_000 — engine run 20261024_101018_gen_2610241019_000

Hypothesis: grammar draw seed=2610241019: supertrend

**0/4 pass.** Ledger N at evaluation: 2366. PBO (CSCV) across family: 0.32. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 bfacb821fc765e612dd5655353af64592d6e0caa50503ad8dde37c6bb82a7c52. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2363 | BROAD|supertrend(atr_n=10,mult=3) | 30.56/0.82/-14.65 | 83.36 | 140 | 0.0873 | 0.61239 (34.32) | 1.0 | 0.7477 | 0.482 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2364 | BROAD|supertrend(atr_n=10,mult=4) | 36.86/0.96/-12.17 | 83.36 | 87 | 0.0839 | 0.47153 (34.95) | 1.0 | 0.8161 | 0.484 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2365 | BROAD|supertrend(atr_n=14,mult=3) | 29.55/0.8/-13.75 | 83.36 | 143 | 0.0873 | 0.62038 (33.48) | 1.0 | 0.7411 | 0.491 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2366 | BROAD|supertrend(atr_n=14,mult=4) | 41.64/1.06/-11.32 | 83.36 | 88 | 0.0838 | 0.35165 (35.15) | 1.0 | 0.8577 | 0.4915 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
