# gen_2610240910_000 — engine run 20261024_091206_gen_2610240910_000

Hypothesis: grammar draw seed=2610240910: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 2246. PBO (CSCV) across family: 0.135. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 01e672489b32d0f0780fa1173a503deb661585e818eb29f99dfd61233e1d83e8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2243 | index|sma_cross(fast=10,slow=50)+trend_sma(n=200) | 41.23/1.07/-10.59 | 107.42 | 58 | 0.0679 | 0.53447 (43.88) | 1.0 | 0.7775 | 0.5205 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2244 | index|sma_cross(fast=10,slow=200)+trend_sma(n=200) | 67.91/1.4/-10.87 | 107.42 | 27 | 0.0561 | 0.16384 (45.59) | 1.0 | 0.9034 | 0.9305 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2245 | index|sma_cross(fast=50,slow=50)+trend_sma(n=200) | 0.0/0.0/0.0 | 107.42 | 0 | inf | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2246 | index|sma_cross(fast=50,slow=200)+trend_sma(n=200) | 63.29/1.37/-10.89 | 107.42 | 34 | 0.0563 | 0.26474 (46.7) | 1.0 | 0.8967 | 0.945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
