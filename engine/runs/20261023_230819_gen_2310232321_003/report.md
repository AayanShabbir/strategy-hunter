# gen_2310232321_003 — engine run 20261023_230819_gen_2310232321_003

Hypothesis: grammar draw seed=2310232321: sma_cross+day_of_week

**0/16 pass.** Ledger N at evaluation: 1206. PBO (CSCV) across family: 0.258. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 58e4b0fb9ffadd2f980c9868d4ef432afaa1f8371261d3568e4797eb563c636d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1191 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=0) | 5.47/1.09/-3.98 | 51.37 | 98 | 0.1194 | 0.8961 (21.7) | 1.0 | 0.0012 | 0.9465 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1192 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=1) | -4.59/-0.64/-9.55 | 51.37 | 119 | 0.1176 | 0.99201 (21.42) | 1.0 | 0.0 | 0.5075 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1193 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=2) | 9.93/1.35/-3.16 | 51.37 | 127 | 0.1183 | 0.83816 (22.08) | 1.0 | 0.0037 | 0.94 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1194 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=3) | -8.07/-1.19/-8.28 | 51.37 | 119 | 0.1089 | 0.99301 (21.61) | 1.0 | 0.0 | 0.5155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1195 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=0) | 1.4/0.38/-3.56 | 51.37 | 34 | 0.1087 | 0.93906 (21.49) | 1.0 | 0.0001 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1196 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=1) | -2.73/-0.53/-6.34 | 51.37 | 37 | 0.1052 | 0.98002 (22.13) | 1.0 | 0.0 | 0.51 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1197 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=2) | 11.73/1.97/-2.44 | 51.37 | 39 | 0.1139 | 0.78422 (21.84) | 1.0 | 0.0138 | 0.9325 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1198 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=3) | -0.95/-0.24/-3.1 | 51.37 | 40 | 0.1044 | 0.96703 (23.13) | 1.0 | 0.0 | 0.97 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1199 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=0) | 2.55/0.44/-6.7 | 51.37 | 102 | 0.1151 | 0.92308 (20.91) | 1.0 | 0.0001 | 0.961 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1200 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=1) | -4.5/-0.66/-9.49 | 51.37 | 109 | 0.1188 | 0.97902 (20.39) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1201 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=2) | 11.24/1.5/-4.24 | 51.37 | 117 | 0.1216 | 0.78322 (21.76) | 1.0 | 0.0046 | 0.945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1202 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=3) | -4.84/-0.78/-5.06 | 51.37 | 114 | 0.1135 | 0.98102 (21.76) | 1.0 | 0.0 | 0.5205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1203 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=0) | 2.64/0.7/-3.39 | 51.37 | 34 | 0.1087 | 0.92108 (21.96) | 1.0 | 0.0006 | 0.963 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1204 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=1) | -4.29/-0.78/-7.94 | 51.37 | 37 | 0.1052 | 0.99101 (22.4) | 1.0 | 0.0 | 0.508 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1205 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=2) | 9.95/1.66/-2.93 | 51.37 | 40 | 0.1089 | 0.84316 (22.47) | 1.0 | 0.0049 | 0.9435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1206 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=3) | -0.27/-0.06/-2.69 | 51.37 | 38 | 0.1075 | 0.96204 (23.72) | 1.0 | 0.0 | 0.968 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
