# gen_2410240413_000 — engine run 20261024_041000_gen_2410240413_000

Hypothesis: grammar draw seed=2410240413: donchian+relvol

**0/4 pass.** Ledger N at evaluation: 1730. PBO (CSCV) across family: 0.619. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 85374cd3455226ac9c0f7658fc9561d6a9fe3463b17c43ec9af541e293a51a43. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1727 | CREDIT|donchian(entry_n=20,exit_n=10)+relvol(min_ratio=1.0) | -7.0/-1.09/-8.42 | 32.7 | 914 | 0.2288 | 1.0 (6.47) | 1.0 | 0.0004 | 0.5095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1728 | CREDIT|donchian(entry_n=20,exit_n=20)+relvol(min_ratio=1.0) | -7.22/-0.92/-9.12 | 32.7 | 1117 | 0.2261 | 1.0 (4.47) | 1.0 | 0.001 | 0.5145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1729 | CREDIT|donchian(entry_n=100,exit_n=10)+relvol(min_ratio=1.0) | -3.46/-0.69/-5.29 | 32.7 | 584 | 0.2689 | 1.0 (9.28) | 1.0 | 0.0046 | 0.512 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1730 | CREDIT|donchian(entry_n=100,exit_n=20)+relvol(min_ratio=1.0) | -3.14/-0.51/-5.48 | 32.7 | 731 | 0.2598 | 0.998 (7.48) | 1.0 | 0.0093 | 0.5155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
