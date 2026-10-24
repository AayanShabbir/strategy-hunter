# gen_2410240515_000 — engine run 20261024_051235_gen_2410240515_000

Hypothesis: grammar draw seed=2410240515: sma_cross+relvol

**0/4 pass.** Ledger N at evaluation: 1822. PBO (CSCV) across family: 0.381. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 30ead876d2f67c12f6142d160f99753bb2641de92b64215684c57bde7a7f0aa9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1819 | BROAD|sma_cross(fast=20,slow=100)+relvol(min_ratio=1.2) | -7.84/-0.55/-10.8 | 57.67 | 1091 | 0.0751 | 0.999 (18.12) | 1.0 | 0.0198 | 0.505 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1820 | BROAD|sma_cross(fast=20,slow=200)+relvol(min_ratio=1.2) | -5.78/-0.35/-10.71 | 57.67 | 1060 | 0.0743 | 0.999 (17.75) | 1.0 | 0.045 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1821 | BROAD|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.2) | -4.35/-0.28/-8.41 | 57.67 | 1067 | 0.0745 | 0.999 (18.67) | 1.0 | 0.0573 | 0.4975 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1822 | BROAD|sma_cross(fast=50,slow=200)+relvol(min_ratio=1.2) | -2.45/-0.11/-9.34 | 57.67 | 1039 | 0.0734 | 0.99201 (18.68) | 1.0 | 0.1035 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
