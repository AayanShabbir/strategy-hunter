# gen_2410240426_000 — engine run 20261024_041038_gen_2410240426_000

Hypothesis: grammar draw seed=2410240426: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 1790. PBO (CSCV) across family: 1.0. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-09-16.
Spec sha256 2091393362f28838de8a0020aaca747619ae03e333c2fb1cb7fb5ff1d0820b98. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1787 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1788 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1789 | SOL|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1790 | SOL|supertrend(atr_n=14,mult=4)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (41.22) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
