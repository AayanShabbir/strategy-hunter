# gen_2410240512_000 — engine run 20261024_051227_gen_2410240512_000

Hypothesis: grammar draw seed=2410240512: sma_cross

**0/4 pass.** Ledger N at evaluation: 1806. PBO (CSCV) across family: 0.24. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 bed159dd800b79792057c163401245a09e1f1c4704e230f0770028d62a4af9ed. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1803 | BROAD|sma_cross(fast=5,slow=100) | 200.12/1.84/-19.07 | 386.25 | 114 | 0.0349 | 0.05894 (127.56) | 1.0 | 0.9977 | 0.5205 | False | beats_buy_hold, cost_stop, holm, spa |
| 1804 | BROAD|sma_cross(fast=5,slow=150) | 192.42/1.77/-16.32 | 386.25 | 90 | 0.0321 | 0.11988 (121.74) | 1.0 | 0.9961 | 0.5235 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |
| 1805 | BROAD|sma_cross(fast=10,slow=100) | 217.23/1.92/-16.37 | 386.25 | 81 | 0.0348 | 0.02198 (124.64) | 1.0 | 0.9984 | 0.531 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |
| 1806 | BROAD|sma_cross(fast=10,slow=150) | 188.06/1.76/-16.93 | 386.25 | 68 | 0.0325 | 0.18082 (125.06) | 1.0 | 0.9957 | 0.533 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
