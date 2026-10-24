# gen_2610241009_000 — engine run 20261024_100957_gen_2610241009_000

Hypothesis: grammar draw seed=2610241009: sma_cross

**0/4 pass.** Ledger N at evaluation: 2326. PBO (CSCV) across family: 0.771. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 00eb88188d6e78c62c47c43262e24ff2b42225c5170c545af06a712e44290d2e. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2323 | BROAD|sma_cross(fast=10,slow=100) | 38.46/0.91/-12.92 | 83.36 | 66 | 0.0816 | 0.42557 (34.74) | 1.0 | 0.7657 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2324 | BROAD|sma_cross(fast=10,slow=150) | 35.27/0.84/-18.5 | 83.36 | 56 | 0.0882 | 0.51748 (35.09) | 1.0 | 0.7292 | 0.5095 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2325 | BROAD|sma_cross(fast=50,slow=100) | 40.46/0.96/-9.92 | 83.36 | 47 | 0.079 | 0.40859 (35.97) | 1.0 | 0.7924 | 0.4845 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2326 | BROAD|sma_cross(fast=50,slow=150) | 54.12/1.16/-11.83 | 83.36 | 30 | 0.0883 | 0.17283 (36.1) | 1.0 | 0.8754 | 0.929 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
