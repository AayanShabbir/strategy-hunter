# gen_2410240121_001 — engine run 20261024_010758_gen_2410240121_001

Hypothesis: grammar draw seed=2410240121: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 1438. PBO (CSCV) across family: 0.693. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 adba4a9c1d232f252eb50167453f092639955b2f93f24c311dd1fc78e430c778. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1435 | crypto|sma_cross(fast=10,slow=50)+vol_regime(max_atr_pct=0.06) | 35.06/0.74/-43.8 | 428.6 | 1635 | 0.1034 | 0.57542 (73.68) | 1.0 | 0.4845 | 0.902 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1436 | crypto|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.06) | 19.26/0.52/-40.09 | 428.6 | 701 | 0.1024 | 0.74126 (177.96) | 1.0 | 0.3783 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1437 | crypto|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.06) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1438 | crypto|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.06) | 51.37/0.98/-35.78 | 428.6 | 391 | 0.1035 | 0.54246 (66.01) | 1.0 | 0.5966 | 0.866 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
