# gen_2310232321_002 — engine run 20261023_230817_gen_2310232321_002

Hypothesis: grammar draw seed=2310232321: sma_cross

**0/4 pass.** Ledger N at evaluation: 1190. PBO (CSCV) across family: 0.238. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 0ce23607530fef61e348fb09479f58af1100b78c385526b8ad424b1f9c821b96. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1187 | megacap|sma_cross(fast=10,slow=50) | -2.64/-0.13/-13.2 | 51.37 | 134 | 0.1158 | 0.96404 (21.51) | 1.0 | 0.0008 | 0.5055 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1188 | megacap|sma_cross(fast=10,slow=100) | 14.16/1.18/-4.4 | 51.37 | 41 | 0.1117 | 0.71229 (22.29) | 1.0 | 0.0849 | 0.934 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1189 | megacap|sma_cross(fast=20,slow=50) | 1.13/0.12/-16.11 | 51.37 | 120 | 0.1196 | 0.93806 (20.95) | 1.0 | 0.0026 | 0.9715 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1190 | megacap|sma_cross(fast=20,slow=100) | 11.59/0.95/-5.7 | 51.37 | 38 | 0.1086 | 0.77522 (22.54) | 1.0 | 0.0498 | 0.941 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
