# gen_2610241117_000 — engine run 20261024_110617_gen_2610241117_000

Hypothesis: grammar draw seed=2610241117: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 2478. PBO (CSCV) across family: 0.084. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 390f13c616667a5cc71b2799504df63b48f01345cf618e4c1f2edea464fea0ba. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2475 | sectors|sma_cross(fast=20,slow=50)+trend_sma(n=50) | 30.55/0.9/-9.78 | 94.31 | 184 | 0.0629 | 0.68731 (37.95) | 1.0 | 0.7758 | 0.515 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2476 | sectors|sma_cross(fast=20,slow=200)+trend_sma(n=50) | 36.12/1.05/-9.78 | 94.31 | 196 | 0.0634 | 0.5025 (36.9) | 1.0 | 0.8431 | 0.5195 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2477 | sectors|sma_cross(fast=50,slow=50)+trend_sma(n=50) | 0.0/0.0/0.0 | 94.31 | 0 | inf | 1.0 (36.43) | 1.0 | 0.0 | 0.4935 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2478 | sectors|sma_cross(fast=50,slow=200)+trend_sma(n=50) | 37.82/1.15/-9.78 | 94.31 | 200 | 0.0634 | 0.48152 (37.9) | 1.0 | 0.8812 | 0.5115 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
