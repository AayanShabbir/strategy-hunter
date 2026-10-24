# gen_2410240602_000 — engine run 20261024_060500_gen_2410240602_000

Hypothesis: grammar draw seed=2410240602: drop_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1906. PBO (CSCV) across family: 0.556. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 88e74d32d4950e859e05e666ad593ae7f4aafff2c537d096016e8a138213e78c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1899 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | -3.32/-1.19/-3.88 | 234.6 | 10 | 0.0264 | 0.98901 (170.62) | 1.0 | 0.001 | 0.9 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1900 | crypto_d|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.04) | -1.74/-0.43/-2.46 | 234.6 | 23 | 0.0258 | 0.97602 (151.75) | 1.0 | 0.018 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1901 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+vol_regime(max_atr_pct=0.04) | -0.4/-0.1/-3.42 | 234.6 | 17 | 0.0256 | 0.98501 (159.16) | 1.0 | 0.0487 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1902 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+vol_regime(max_atr_pct=0.04) | -1.8/-0.3/-3.87 | 234.6 | 33 | 0.0255 | 0.97502 (151.07) | 1.0 | 0.028 | 0.899 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1903 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (173.95) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1904 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+vol_regime(max_atr_pct=0.04) | -0.47/-0.37/-1.25 | 234.6 | 3 | 0.0258 | 0.99001 (175.27) | 1.0 | 0.0292 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1905 | crypto_d|drop_revert(drop=0.1,hold=10,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1906 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+vol_regime(max_atr_pct=0.04) | -0.6/-0.4/-1.57 | 234.6 | 6 | 0.0257 | 0.98701 (173.46) | 1.0 | 0.0248 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
