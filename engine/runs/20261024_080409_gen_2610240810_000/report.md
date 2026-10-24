# gen_2610240810_000 — engine run 20261024_080409_gen_2610240810_000

Hypothesis: grammar draw seed=2610240810: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 2178. PBO (CSCV) across family: 0.032. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 209f7a916cc1b876abd886894b8cd5092ed74f7c11edff9ac66d2bd84a769716. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2175 | sectors|sma_cross(fast=5,slow=50)+trend_sma(n=50) | 8.03/0.38/-9.03 | 50.2 | 584 | 0.0662 | 0.97502 (20.39) | 1.0 | 0.2612 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2176 | sectors|sma_cross(fast=5,slow=150)+trend_sma(n=50) | 3.66/0.21/-8.71 | 50.2 | 643 | 0.0679 | 0.997 (19.85) | 1.0 | 0.1732 | 0.4905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2177 | sectors|sma_cross(fast=50,slow=50)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.52) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2178 | sectors|sma_cross(fast=50,slow=150)+trend_sma(n=50) | -1.42/-0.05/-7.64 | 50.2 | 610 | 0.0692 | 1.0 (20.39) | 1.0 | 0.0826 | 0.511 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
