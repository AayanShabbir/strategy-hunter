# gen_2410240423_000 — engine run 20261024_041031_gen_2410240423_000

Hypothesis: grammar draw seed=2410240423: sma_cross

**0/4 pass.** Ledger N at evaluation: 1778. PBO (CSCV) across family: 0.5. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b19998ead7fc5e7262a177af9bc22797129c15c3a6d131312fdc598fe4e7f5e6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1775 | BONDS_INTL|sma_cross(fast=5,slow=50) | 14.83/0.64/-9.35 | 40.38 | 207 | 0.0874 | 0.64336 (17.56) | 1.0 | 0.5669 | 0.9745 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1776 | BONDS_INTL|sma_cross(fast=5,slow=200) | 5.07/0.25/-10.73 | 40.38 | 88 | 0.091 | 0.97602 (17.34) | 1.0 | 0.3093 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1777 | BONDS_INTL|sma_cross(fast=20,slow=50) | 9.61/0.43/-9.8 | 40.38 | 125 | 0.0888 | 0.87512 (17.65) | 1.0 | 0.4259 | 0.4865 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1778 | BONDS_INTL|sma_cross(fast=20,slow=200) | 9.97/0.43/-11.19 | 40.38 | 52 | 0.0955 | 0.90809 (18.52) | 1.0 | 0.426 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
