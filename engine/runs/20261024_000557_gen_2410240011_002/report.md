# gen_2410240011_002 — engine run 20261024_000557_gen_2410240011_002

Hypothesis: grammar draw seed=2410240011: supertrend

**0/4 pass.** Ledger N at evaluation: 1322. PBO (CSCV) across family: 0.253. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 3dae10c8ef234a3198f04ee8bff0a552248fe4fae02fb77f673569e702b77696. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1319 | crypto|supertrend(atr_n=7,mult=2) | -12.28/-0.06/-39.69 | 428.6 | 2367 | 0.0975 | 0.82018 (50.96) | 1.0 | 0.2523 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1320 | crypto|supertrend(atr_n=7,mult=4) | 3.91/0.25/-42.89 | 428.6 | 886 | 0.0999 | 0.82817 (84.62) | 1.0 | 0.3858 | 0.9215 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1321 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.83417 (51.3) | 1.0 | 0.2598 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1322 | crypto|supertrend(atr_n=10,mult=4) | -3.46/0.11/-43.75 | 428.6 | 871 | 0.0993 | 0.88811 (108.04) | 1.0 | 0.3229 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
