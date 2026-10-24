# gen_2410240713_000 — engine run 20261024_070524_gen_2410240713_000

Hypothesis: grammar draw seed=2410240713: donchian

**0/4 pass.** Ledger N at evaluation: 2058. PBO (CSCV) across family: 0.053. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 ddd1d7ca306c0fbee9d77e64817f430e465e76034e639c7007b594bc54cb3793. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2055 | BROAD|donchian(entry_n=20,exit_n=10) | 26.5/1.13/-4.46 | 78.13 | 220 | 0.0831 | 0.72328 (31.57) | 1.0 | 0.3952 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2056 | BROAD|donchian(entry_n=20,exit_n=20) | 45.05/1.49/-5.88 | 78.13 | 148 | 0.0798 | 0.07493 (32.59) | 1.0 | 0.638 | 0.9785 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2057 | BROAD|donchian(entry_n=100,exit_n=10) | 8.43/0.58/-5.38 | 78.13 | 137 | 0.0899 | 0.997 (31.94) | 1.0 | 0.1179 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2058 | BROAD|donchian(entry_n=100,exit_n=20) | 20.34/1.04/-5.13 | 78.13 | 92 | 0.0844 | 0.94505 (32.95) | 1.0 | 0.3393 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
