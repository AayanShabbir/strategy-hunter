# gen_2310232211_002 — engine run 20261023_220805_gen_2310232211_002

Hypothesis: grammar draw seed=2310232211: supertrend

**0/4 pass.** Ledger N at evaluation: 1042. PBO (CSCV) across family: 0.016. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 35217c793d2b8595203129322d1eac03c7f041b48d6b325e0efb2e69b44492e6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1039 | sectors|supertrend(atr_n=10,mult=2) | 18.34/0.78/-9.43 | 50.2 | 601 | 0.0657 | 0.62737 (20.96) | 1.0 | 0.5489 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1040 | sectors|supertrend(atr_n=10,mult=4) | 8.66/0.42/-8.67 | 50.2 | 243 | 0.0666 | 0.98801 (22.38) | 1.0 | 0.3103 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1041 | sectors|supertrend(atr_n=14,mult=2) | 20.22/0.83/-10.15 | 50.2 | 604 | 0.0654 | 0.4985 (20.79) | 1.0 | 0.5808 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1042 | sectors|supertrend(atr_n=14,mult=4) | 9.33/0.44/-9.81 | 50.2 | 244 | 0.0662 | 0.98601 (22.04) | 1.0 | 0.323 | 0.5115 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
