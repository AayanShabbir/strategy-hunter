# gen_2610240801_000 — engine run 20261024_080319_gen_2610240801_000

Hypothesis: grammar draw seed=2610240801: sma_cross

**0/4 pass.** Ledger N at evaluation: 2098. PBO (CSCV) across family: 0.496. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 92e1b5764e89fed67e24b0434bd97c45ddb8f29316a62cf53a681663d9a4ca95. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2095 | crypto|sma_cross(fast=5,slow=100) | 44.16/0.89/-22.2 | 56.21 | 31 | 0.0223 | 0.32268 (28.17) | 1.0 | 0.6655 | 0.7085 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2096 | crypto|sma_cross(fast=5,slow=150) | 21.78/0.54/-29.95 | 56.21 | 20 | 0.0236 | 0.56943 (27.55) | 1.0 | 0.5051 | 0.8575 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2097 | crypto|sma_cross(fast=20,slow=100) | 28.54/0.66/-29.52 | 56.21 | 22 | 0.0258 | 0.45455 (25.69) | 1.0 | 0.5607 | 0.792 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2098 | crypto|sma_cross(fast=20,slow=150) | 24.18/0.58/-31.93 | 56.21 | 14 | 0.0233 | 0.52348 (28.72) | 1.0 | 0.522 | 0.85 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
