# gen_2410240710_000 — engine run 20261024_070516_gen_2410240710_000

Hypothesis: grammar draw seed=2410240710: supertrend

**0/4 pass.** Ledger N at evaluation: 2050. PBO (CSCV) across family: 0.161. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 ab53e20ca2bafe29da5f7bc3e477c39cc6b32ea51e187e488fbe3389137c40b9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2047 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.82517 (37.29) | 1.0 | 0.3215 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2048 | crypto|supertrend(atr_n=10,mult=4) | -3.46/0.11/-43.75 | 428.6 | 871 | 0.0993 | 0.88112 (63.16) | 1.0 | 0.3902 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2049 | crypto|supertrend(atr_n=14,mult=2) | -4.81/0.1/-37.43 | 428.6 | 2376 | 0.0958 | 0.75824 (37.06) | 1.0 | 0.3848 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2050 | crypto|supertrend(atr_n=14,mult=4) | -13.24/-0.08/-47.58 | 428.6 | 874 | 0.0969 | 0.94605 (164.26) | 1.0 | 0.3043 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
