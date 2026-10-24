# gen_2610241104_000 — engine run 20261024_110540_gen_2610241104_000

Hypothesis: grammar draw seed=2610241104: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 2406. PBO (CSCV) across family: 0.166. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 f83e7dab32d18c19127bcc096a934084c7ab29fa03b6283b84f663e7ebd59eae. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2403 | BROAD|sma_cross(fast=10,slow=50)+rsi_band(hi=70) | 29.81/0.87/-15.84 | 83.36 | 220 | 0.0844 | 0.6014 (32.32) | 1.0 | 0.7972 | 0.5035 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2404 | BROAD|sma_cross(fast=10,slow=200)+rsi_band(hi=70) | 24.84/0.7/-14.25 | 83.36 | 146 | 0.0844 | 0.75025 (33.03) | 1.0 | 0.7068 | 0.514 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2405 | BROAD|sma_cross(fast=20,slow=50)+rsi_band(hi=70) | 32.11/0.94/-14.25 | 83.36 | 193 | 0.0817 | 0.57143 (33.19) | 1.0 | 0.8281 | 0.5055 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2406 | BROAD|sma_cross(fast=20,slow=200)+rsi_band(hi=70) | 36.14/0.93/-12.27 | 83.36 | 126 | 0.0853 | 0.45255 (33.42) | 1.0 | 0.8254 | 0.522 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
