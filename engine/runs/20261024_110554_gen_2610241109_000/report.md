# gen_2610241109_000 — engine run 20261024_110554_gen_2610241109_000

Hypothesis: grammar draw seed=2610241109: supertrend

**0/4 pass.** Ledger N at evaluation: 2434. PBO (CSCV) across family: 0.938. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 977d5ef1eb1e2ca9ecf25e302e138d10a76dde969c7f428166a53a7e1407466a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2431 | BROAD|supertrend(atr_n=7,mult=2) | 22.54/0.64/-14.73 | 83.36 | 231 | 0.0858 | 0.78621 (33.03) | 1.0 | 0.7011 | 0.496 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2432 | BROAD|supertrend(atr_n=7,mult=3) | 30.82/0.82/-14.09 | 83.36 | 140 | 0.0877 | 0.61439 (33.9) | 1.0 | 0.7978 | 0.4795 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2433 | BROAD|supertrend(atr_n=10,mult=2) | 24.23/0.68/-15.38 | 83.36 | 234 | 0.0858 | 0.73327 (31.95) | 1.0 | 0.724 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2434 | BROAD|supertrend(atr_n=10,mult=3) | 30.56/0.82/-14.65 | 83.36 | 140 | 0.0873 | 0.63836 (34.91) | 1.0 | 0.7958 | 0.482 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
