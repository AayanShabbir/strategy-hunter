# gen_2410240416_000 — engine run 20261024_041010_gen_2410240416_000

Hypothesis: grammar draw seed=2410240416: donchian

**0/4 pass.** Ledger N at evaluation: 1746. PBO (CSCV) across family: 0.605. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 427562a37e3253c2b92baeaba83de8a5308a4249d98242af5988ec98faba0d50. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1743 | crypto|donchian(entry_n=20,exit_n=10) | 217.84/0.83/-35.62 | 428.6 | 1641 | 0.1029 | 0.31469 (130.15) | 1.0 | 0.9623 | 0.5165 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1744 | crypto|donchian(entry_n=20,exit_n=20) | 204.93/0.83/-45.63 | 428.6 | 1263 | 0.1008 | 0.36663 (115.85) | 1.0 | 0.9568 | 0.508 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1745 | crypto|donchian(entry_n=55,exit_n=10) | 250.98/0.87/-24.68 | 428.6 | 959 | 0.1037 | 0.30969 (77.66) | 1.0 | 0.974 | 0.9495 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1746 | crypto|donchian(entry_n=55,exit_n=20) | 212.99/0.83/-38.82 | 428.6 | 771 | 0.1005 | 0.43556 (203.26) | 1.0 | 0.9601 | 0.9705 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
