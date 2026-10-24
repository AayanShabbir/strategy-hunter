# gen_2310232321_000 — engine run 20261023_230811_gen_2310232321_000

Hypothesis: grammar draw seed=2310232321: sma_cross+rsi_band

**0/4 pass.** Ledger N at evaluation: 1178. PBO (CSCV) across family: 0.123. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 9a02e314cbd5e0825329a56d54c354cc34aaa193bc218b1cf066d59d0d9e8204. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1175 | megacap|sma_cross(fast=5,slow=100)+rsi_band(hi=80) | 11.3/0.96/-4.73 | 51.37 | 59 | 0.1033 | 0.7952 (21.99) | 1.0 | 0.7729 | 0.945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1176 | megacap|sma_cross(fast=5,slow=150)+rsi_band(hi=80) | 11.03/1.11/-7.02 | 51.37 | 37 | 0.0982 | 0.7962 (22.76) | 1.0 | 0.8264 | 0.9385 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1177 | megacap|sma_cross(fast=10,slow=100)+rsi_band(hi=80) | 14.68/1.22/-4.4 | 51.37 | 54 | 0.1097 | 0.67133 (21.44) | 1.0 | 0.8567 | 0.932 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1178 | megacap|sma_cross(fast=10,slow=150)+rsi_band(hi=80) | 10.48/1.06/-7.33 | 51.37 | 35 | 0.1065 | 0.79021 (23.05) | 1.0 | 0.808 | 0.9405 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
