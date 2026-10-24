# gen_2410240308_000 — engine run 20261024_030911_gen_2410240308_000

Hypothesis: grammar draw seed=2410240308: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 1606. PBO (CSCV) across family: 0.844. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 dd09fb2aeeb1508e18904adfa4bf21255a5438739c8bbf32c5df20f411de4375. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1603 | megacap|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.0) | 10.85/0.4/-7.77 | 214.9 | 1182 | 0.0507 | 1.0 (66.78) | 1.0 | 0.6208 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1604 | megacap|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | 10.81/0.39/-7.91 | 214.9 | 1144 | 0.0518 | 1.0 (67.56) | 1.0 | 0.6098 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1605 | megacap|supertrend(atr_n=14,mult=3)+relvol(min_ratio=1.0) | 15.48/0.53/-7.83 | 214.9 | 1217 | 0.0506 | 1.0 (65.79) | 1.0 | 0.707 | 0.4845 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1606 | megacap|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.0) | 13.64/0.47/-8.23 | 214.9 | 1180 | 0.0511 | 1.0 (67.01) | 1.0 | 0.6676 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
