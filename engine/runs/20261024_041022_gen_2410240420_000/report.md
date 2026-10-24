# gen_2410240420_000 — engine run 20261024_041022_gen_2410240420_000

Hypothesis: grammar draw seed=2410240420: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 1766. PBO (CSCV) across family: 0.846. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 879d40f8a307722e5ad3e14ec620340daf36c7bd295f6faeeaf5a0cb80d1ef37. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1763 | sector_etf|sma_cross(fast=5,slow=50)+vol_regime(max_atr_pct=0.04) | 20.82/0.71/-10.65 | 63.33 | 292 | 0.0609 | 0.73027 (27.18) | 1.0 | 0.7252 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1764 | sector_etf|sma_cross(fast=5,slow=100)+vol_regime(max_atr_pct=0.04) | 15.45/0.53/-11.84 | 63.33 | 195 | 0.0587 | 0.91808 (27.62) | 1.0 | 0.6125 | 0.5145 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1765 | sector_etf|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 63.33 | 0 | inf | 1.0 (29.82) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1766 | sector_etf|sma_cross(fast=50,slow=100)+vol_regime(max_atr_pct=0.04) | 22.22/0.71/-9.58 | 63.33 | 90 | 0.0712 | 0.75425 (28.29) | 1.0 | 0.7252 | 0.519 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
