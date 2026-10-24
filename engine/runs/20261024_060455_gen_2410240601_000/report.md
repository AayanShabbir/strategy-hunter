# gen_2410240601_000 — engine run 20261024_060455_gen_2410240601_000

Hypothesis: grammar draw seed=2410240601: sma_cross

**0/4 pass.** Ledger N at evaluation: 1898. PBO (CSCV) across family: 0.109. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 0109fea4e70f42534ef6e3b4d7db890151e47cb65c9e5c97b250b9cb13e76030. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1895 | sectors|sma_cross(fast=5,slow=100) | 9.94/0.41/-11.71 | 50.2 | 256 | 0.0635 | 0.96803 (22.19) | 1.0 | 0.6449 | 0.519 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1896 | sectors|sma_cross(fast=5,slow=200) | 11.83/0.47/-11.94 | 50.2 | 168 | 0.0605 | 0.95105 (22.23) | 1.0 | 0.6778 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1897 | sectors|sma_cross(fast=10,slow=100) | 8.43/0.36/-12.66 | 50.2 | 193 | 0.0644 | 0.98901 (22.35) | 1.0 | 0.6097 | 0.5095 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1898 | sectors|sma_cross(fast=10,slow=200) | 12.77/0.49/-13.04 | 50.2 | 119 | 0.0645 | 0.93606 (22.94) | 1.0 | 0.6886 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
