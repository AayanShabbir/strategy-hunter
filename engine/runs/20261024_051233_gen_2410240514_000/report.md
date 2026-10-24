# gen_2410240514_000 — engine run 20261024_051233_gen_2410240514_000

Hypothesis: grammar draw seed=2410240514: donchian

**0/4 pass.** Ledger N at evaluation: 1818. PBO (CSCV) across family: 0.541. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 886b982d37691c6193a44114b8cf2f2e66460b7247b4233f617681c20e8f5393. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1815 | BROAD|donchian(entry_n=55,exit_n=10) | -5.77/-0.24/-11.41 | 62.38 | 167 | 0.0818 | 1.0 (25.92) | 1.0 | 0.1581 | 0.5085 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1816 | BROAD|donchian(entry_n=55,exit_n=20) | -3.66/-0.09/-16.52 | 62.38 | 106 | 0.0768 | 1.0 (27.33) | 1.0 | 0.2305 | 0.521 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1817 | BROAD|donchian(entry_n=100,exit_n=10) | -5.42/-0.28/-10.7 | 62.38 | 137 | 0.086 | 1.0 (26.67) | 1.0 | 0.1431 | 0.4955 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1818 | BROAD|donchian(entry_n=100,exit_n=20) | -7.65/-0.32/-18.22 | 62.38 | 88 | 0.0795 | 1.0 (27.24) | 1.0 | 0.1284 | 0.5095 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
