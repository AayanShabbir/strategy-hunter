# gen_2610240908_000 — engine run 20261024_091159_gen_2610240908_000

Hypothesis: grammar draw seed=2610240908: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 2238. PBO (CSCV) across family: 0.531. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 da98888f883362a5aa671744fa6ff90e5f697552ef7cd9c34743ed83b2664f20. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2231 | index|rsi_revert(entry=5,exit=60,n=3)+vol_regime(max_atr_pct=0.02) | -0.41/-0.12/-1.83 | 75.73 | 42 | 0.0798 | 1.0 (33.69) | 1.0 | 0.003 | 0.494 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2232 | index|rsi_revert(entry=5,exit=60,n=5)+vol_regime(max_atr_pct=0.02) | 0.32/0.22/-0.81 | 75.73 | 5 | 0.0877 | 0.98801 (33.84) | 1.0 | 0.0149 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2233 | index|rsi_revert(entry=5,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 1.53/0.42/-1.83 | 75.73 | 43 | 0.0718 | 1.0 (32.78) | 1.0 | 0.0342 | 0.494 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2234 | index|rsi_revert(entry=5,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 0.58/0.39/-0.81 | 75.73 | 5 | 0.0877 | 0.98501 (34.8) | 1.0 | 0.0286 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2235 | index|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.02) | 13.16/0.8/-6.52 | 75.73 | 307 | 0.0836 | 0.97802 (30.15) | 1.0 | 0.1222 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2236 | index|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.02) | 12.63/1.01/-6.17 | 75.73 | 126 | 0.0736 | 0.98501 (32.48) | 1.0 | 0.214 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2237 | index|rsi_revert(entry=20,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 18.58/0.92/-8.09 | 75.73 | 286 | 0.0843 | 0.9041 (30.33) | 1.0 | 0.1637 | 0.509 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2238 | index|rsi_revert(entry=20,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 17.61/1.07/-6.4 | 75.73 | 132 | 0.0705 | 0.94306 (31.81) | 1.0 | 0.2415 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
