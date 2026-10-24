# gen_2410240606_000 — engine run 20261024_060515_gen_2410240606_000

Hypothesis: grammar draw seed=2410240606: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 1942. PBO (CSCV) across family: 0.911. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b99b8e550a08752d5f7fd7da5195300795db6b8ff20fc041434f027fad8a1e78. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1939 | hibeta|sma_cross(fast=10,slow=150)+relvol(min_ratio=1.0) | 162.25/1.59/-25.81 | 809.88 | 970 | 0.0239 | 0.63037 (189.19) | 1.0 | 0.9855 | 0.5165 | False | beats_buy_hold, holm, spa, pbo |
| 1940 | hibeta|sma_cross(fast=10,slow=200)+relvol(min_ratio=1.0) | 134.57/1.4/-29.16 | 809.88 | 1003 | 0.0239 | 0.78721 (194.0) | 1.0 | 0.9664 | 0.5095 | False | beats_buy_hold, holm, spa, pbo |
| 1941 | hibeta|sma_cross(fast=20,slow=150)+relvol(min_ratio=1.0) | 156.92/1.54/-28.56 | 809.88 | 959 | 0.0238 | 0.69431 (198.03) | 1.0 | 0.9811 | 0.5125 | False | beats_buy_hold, holm, spa, pbo |
| 1942 | hibeta|sma_cross(fast=20,slow=200)+relvol(min_ratio=1.0) | 130.91/1.38/-29.08 | 809.88 | 995 | 0.0238 | 0.83317 (204.16) | 1.0 | 0.9626 | 0.509 | False | beats_buy_hold, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
