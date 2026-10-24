# gen_2410240001_003 — engine run 20261024_000543_gen_2410240001_003

Hypothesis: grammar draw seed=2410240001: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 1306. PBO (CSCV) across family: 0.767. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 ada8a3e97bc132fac0c8790fce20736fad1d993596481dac1d33e2d0a8c0b7d9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1303 | crypto_d|sma_cross(fast=5,slow=50)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 2 | 0.0545 | 0.98002 (106.5) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1304 | crypto_d|sma_cross(fast=5,slow=100)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 1 | 0.0509 | 0.97902 (42.86) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1305 | crypto_d|sma_cross(fast=20,slow=50)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 234.6 | 1 | 0.0512 | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1306 | crypto_d|sma_cross(fast=20,slow=100)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 2 | 0.0512 | 0.97502 (170.14) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
