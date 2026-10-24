# gen_2310232009_000 — engine run 20261023_201037_gen_2310232009_000

Hypothesis: grammar draw seed=2310232009: supertrend

**0/4 pass.** Ledger N at evaluation: 790. PBO (CSCV) across family: 0.713. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 ade992db81a8502dc4d64a8779fca38647c58da41c7ef791f62d7a58ed8e0db9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 787 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.83417 (132.6) | 1.0 | 0.323 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 788 | crypto|supertrend(atr_n=10,mult=3) | -9.6/-0.01/-44.27 | 428.6 | 1339 | 0.0981 | 0.91209 (95.61) | 1.0 | 0.3397 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 789 | crypto|supertrend(atr_n=14,mult=2) | -4.81/0.1/-37.43 | 428.6 | 2376 | 0.0958 | 0.76124 (50.17) | 1.0 | 0.3864 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 790 | crypto|supertrend(atr_n=14,mult=3) | 0.35/0.19/-41.76 | 428.6 | 1347 | 0.0966 | 0.82517 (156.31) | 1.0 | 0.4294 | 0.92 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
