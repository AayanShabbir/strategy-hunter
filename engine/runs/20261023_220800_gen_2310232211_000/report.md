# gen_2310232211_000 — engine run 20261023_220800_gen_2310232211_000

Hypothesis: grammar draw seed=2310232211: sma_cross

**0/4 pass.** Ledger N at evaluation: 1034. PBO (CSCV) across family: 0.225. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 38af5e3e37daf21d5e19292c7338500c1cb316998c21b2b270655534b2c33b8b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1031 | sectors|sma_cross(fast=10,slow=150) | 7.96/0.34/-12.02 | 50.2 | 148 | 0.0656 | 0.996 (22.66) | 1.0 | 0.4751 | 0.506 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1032 | sectors|sma_cross(fast=10,slow=200) | 12.77/0.49/-13.04 | 50.2 | 119 | 0.0645 | 0.92308 (23.16) | 1.0 | 0.5767 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1033 | sectors|sma_cross(fast=20,slow=150) | 11.03/0.43/-12.34 | 50.2 | 122 | 0.0696 | 0.95205 (23.11) | 1.0 | 0.5426 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1034 | sectors|sma_cross(fast=20,slow=200) | 16.95/0.61/-11.96 | 50.2 | 90 | 0.0688 | 0.75524 (22.77) | 1.0 | 0.6562 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
