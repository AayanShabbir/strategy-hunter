# gen_2610241006_000 — engine run 20261024_100948_gen_2610241006_000

Hypothesis: grammar draw seed=2610241006: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 2306. PBO (CSCV) across family: 0.643. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 89a64a4e54c138ca0e0673340784269fc13490f274ebf4a00a83e6fe7595f880. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2303 | index|sma_cross(fast=5,slow=150)+vol_regime(max_atr_pct=0.06) | 65.5/1.34/-10.67 | 107.42 | 25 | 0.0561 | 0.08791 (43.42) | 1.0 | 0.9744 | 0.9555 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2304 | index|sma_cross(fast=5,slow=200)+vol_regime(max_atr_pct=0.06) | 69.69/1.39/-11.79 | 107.42 | 17 | 0.0595 | 0.17682 (45.87) | 1.0 | 0.9784 | 0.934 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2305 | index|sma_cross(fast=10,slow=150)+vol_regime(max_atr_pct=0.06) | 64.42/1.31/-11.61 | 107.42 | 19 | 0.0591 | 0.14086 (42.86) | 1.0 | 0.9706 | 0.9525 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2306 | index|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.06) | 72.12/1.43/-11.61 | 107.42 | 13 | 0.0596 | 0.12687 (45.19) | 1.0 | 0.9818 | 0.9185 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
