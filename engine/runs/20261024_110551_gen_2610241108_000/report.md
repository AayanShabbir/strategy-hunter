# gen_2610241108_000 — engine run 20261024_110551_gen_2610241108_000

Hypothesis: grammar draw seed=2610241108: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 2430. PBO (CSCV) across family: 0.879. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 5ddfd3fc5eb63561f933712b50d92c39ea72580c3174c6de27c64303d348914a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2427 | index|supertrend(atr_n=7,mult=2)+vol_regime(max_atr_pct=0.04) | 59.03/1.43/-9.07 | 107.42 | 138 | 0.0734 | 0.12587 (41.3) | 1.0 | 0.9805 | 0.959 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2428 | index|supertrend(atr_n=7,mult=4)+vol_regime(max_atr_pct=0.04) | 49.38/1.3/-10.21 | 107.42 | 52 | 0.0757 | 0.33666 (44.59) | 1.0 | 0.9655 | 0.5115 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2429 | index|supertrend(atr_n=14,mult=2)+vol_regime(max_atr_pct=0.04) | 61.85/1.44/-12.23 | 107.42 | 141 | 0.0712 | 0.0969 (41.28) | 1.0 | 0.9814 | 0.969 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2430 | index|supertrend(atr_n=14,mult=4)+vol_regime(max_atr_pct=0.04) | 56.84/1.36/-11.63 | 107.42 | 51 | 0.0647 | 0.16484 (43.27) | 1.0 | 0.9727 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
