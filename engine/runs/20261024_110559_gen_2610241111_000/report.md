# gen_2610241111_000 — engine run 20261024_110559_gen_2610241111_000

Hypothesis: grammar draw seed=2610241111: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 2446. PBO (CSCV) across family: 0.947. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 eab7d1e8b9290b742ce575405700f5fca5fdf83a3bc8d102af6442e2ecf0c0aa. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2443 | megacap|sma_cross(fast=10,slow=100)+rsi_band(hi=80) | 50.92/1.04/-19.43 | 118.49 | 58 | 0.0516 | 0.39261 (46.24) | 1.0 | 0.9087 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2444 | megacap|sma_cross(fast=10,slow=150)+rsi_band(hi=80) | 46.15/0.95/-18.8 | 118.49 | 50 | 0.0538 | 0.5045 (47.97) | 1.0 | 0.8799 | 0.51 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2445 | megacap|sma_cross(fast=50,slow=100)+rsi_band(hi=80) | 40.49/0.88/-15.16 | 118.49 | 44 | 0.0562 | 0.6044 (48.32) | 1.0 | 0.8537 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2446 | megacap|sma_cross(fast=50,slow=150)+rsi_band(hi=80) | 40.79/0.89/-14.85 | 118.49 | 35 | 0.0633 | 0.58841 (47.23) | 1.0 | 0.8574 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
