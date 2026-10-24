# gen_2410240714_000 — engine run 20261024_070526_gen_2410240714_000

Hypothesis: grammar draw seed=2410240714: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 2062. PBO (CSCV) across family: 0.816. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 8de884eba0b2ecb8f0a09ebe7255dec26d8edcd102620fec7eda85ac1436f84c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2059 | hibeta|sma_cross(fast=20,slow=150)+rsi_band(hi=70) | 186.39/1.24/-32.19 | 809.88 | 239 | 0.0247 | 0.62138 (214.73) | 1.0 | 0.927 | 0.5105 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2060 | hibeta|sma_cross(fast=20,slow=200)+rsi_band(hi=70) | 151.25/1.1/-32.7 | 809.88 | 222 | 0.024 | 0.75425 (217.08) | 1.0 | 0.8873 | 0.515 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2061 | hibeta|sma_cross(fast=50,slow=150)+rsi_band(hi=70) | 196.85/1.27/-32.7 | 809.88 | 210 | 0.0247 | 0.55345 (214.05) | 1.0 | 0.9353 | 0.5105 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2062 | hibeta|sma_cross(fast=50,slow=200)+rsi_band(hi=70) | 138.09/1.03/-32.7 | 809.88 | 199 | 0.024 | 0.81918 (219.53) | 1.0 | 0.8655 | 0.5125 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
