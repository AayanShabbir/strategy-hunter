# gen_2610240904_000 — engine run 20261024_091148_gen_2610240904_000

Hypothesis: grammar draw seed=2610240904: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 2210. PBO (CSCV) across family: 0.66. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 b971ce2a3371a7e16fac9fac31527c54d4750b3cb22a20edeb51ce88a8306dba. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2207 | crypto|sma_cross(fast=5,slow=100)+rsi_band(hi=80) | 47.54/0.99/-24.09 | 72.28 | 23 | 0.0273 | 0.32468 (29.82) | 1.0 | 0.3664 | 0.806 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2208 | crypto|sma_cross(fast=5,slow=200)+rsi_band(hi=80) | -4.31/0.11/-39.91 | 72.28 | 21 | 0.0266 | 0.88611 (31.47) | 1.0 | 0.0818 | 0.5005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2209 | crypto|sma_cross(fast=20,slow=100)+rsi_band(hi=80) | 21.44/0.57/-35.04 | 72.28 | 20 | 0.0275 | 0.57842 (28.42) | 1.0 | 0.1968 | 0.922 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2210 | crypto|sma_cross(fast=20,slow=200)+rsi_band(hi=80) | 33.85/0.7/-26.05 | 72.28 | 13 | 0.0273 | 0.45654 (30.29) | 1.0 | 0.2423 | 0.9115 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
