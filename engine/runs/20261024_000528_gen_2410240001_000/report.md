# gen_2410240001_000 — engine run 20261024_000528_gen_2410240001_000

Hypothesis: grammar draw seed=2410240001: supertrend+rsi_band

**0/4 pass.** Ledger N at evaluation: 1266. PBO (CSCV) across family: 0.97. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 3c9ad29588f462ca1f42bbf7eae0611932de99738538fc391fdb06dc9f4917fa. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1263 | crypto_d|supertrend(atr_n=10,mult=3)+rsi_band(hi=80) | -4.63/0.11/-34.95 | 234.6 | 146 | 0.0162 | 0.93806 (75.0) | 1.0 | 0.3777 | 0.904 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1264 | crypto_d|supertrend(atr_n=10,mult=4)+rsi_band(hi=80) | 3.99/0.28/-31.71 | 234.6 | 114 | 0.0172 | 0.88012 (82.16) | 1.0 | 0.4534 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1265 | crypto_d|supertrend(atr_n=14,mult=3)+rsi_band(hi=80) | -4.84/0.1/-33.24 | 234.6 | 146 | 0.0163 | 0.95504 (73.17) | 1.0 | 0.3695 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1266 | crypto_d|supertrend(atr_n=14,mult=4)+rsi_band(hi=80) | 6.97/0.32/-30.7 | 234.6 | 109 | 0.017 | 0.87013 (69.92) | 1.0 | 0.4738 | 0.9005 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
