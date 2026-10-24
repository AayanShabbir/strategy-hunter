# gen_2410240525_000 — engine run 20261024_051301_gen_2410240525_000

Hypothesis: grammar draw seed=2410240525: donchian

**0/4 pass.** Ledger N at evaluation: 1878. PBO (CSCV) across family: 0.257. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 e98c14cafff60655adaed0d012a3b147088ec5594d4a8bd6adf39b633e65a741. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1875 | BROAD|donchian(entry_n=20,exit_n=10) | -23.59/-0.82/-26.98 | 5.92 | 201 | 0.0539 | 0.98002 (1.64) | 1.0 | 0.0 | 0.9515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1876 | BROAD|donchian(entry_n=20,exit_n=20) | -20.98/-0.56/-30.95 | 5.92 | 148 | 0.0529 | 0.98102 (2.44) | 1.0 | 0.0 | 0.9535 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1877 | BROAD|donchian(entry_n=100,exit_n=10) | 0.2/0.04/-11.16 | 5.92 | 80 | 0.0602 | 0.58342 (2.68) | 1.0 | 0.0006 | 0.6325 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1878 | BROAD|donchian(entry_n=100,exit_n=20) | 9.41/0.43/-6.67 | 5.92 | 60 | 0.0581 | 0.3996 (3.13) | 1.0 | 0.005 | 0.505 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
