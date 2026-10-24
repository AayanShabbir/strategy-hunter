# gen_2610240902_000 — engine run 20261024_091142_gen_2610240902_000

Hypothesis: grammar draw seed=2610240902: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 2198. PBO (CSCV) across family: 0.856. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 fce0f1616153d48fb2131e7ca7f7ca7f048c28aa4e4634a7d9653b93b920d15f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2195 | crypto|sma_cross(fast=10,slow=150)+rsi_band(hi=60) | 20.47/0.51/-39.25 | 31.3 | 52 | 0.0199 | 0.44456 (12.32) | 1.0 | 0.3196 | 0.6915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2196 | crypto|sma_cross(fast=10,slow=200)+rsi_band(hi=60) | -3.78/0.14/-44.58 | 31.3 | 49 | 0.0202 | 0.61738 (14.51) | 1.0 | 0.1825 | 0.807 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2197 | crypto|sma_cross(fast=50,slow=150)+rsi_band(hi=60) | 7.52/0.33/-45.78 | 31.3 | 46 | 0.02 | 0.53047 (13.61) | 1.0 | 0.2466 | 0.7265 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2198 | crypto|sma_cross(fast=50,slow=200)+rsi_band(hi=60) | -19.76/-0.09/-56.3 | 31.3 | 45 | 0.0195 | 0.73127 (13.09) | 1.0 | 0.1197 | 0.872 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
