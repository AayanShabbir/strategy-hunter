# gen_2410240524_000 — engine run 20261024_051259_gen_2410240524_000

Hypothesis: grammar draw seed=2410240524: donchian

**0/4 pass.** Ledger N at evaluation: 1874. PBO (CSCV) across family: 0.243. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 5a9423c89a4c77def53cdd261f91ff12ba06c604b379aae82abdeab4b5876a1c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1871 | crypto|donchian(entry_n=55,exit_n=10) | 38.79/1.02/-15.0 | 56.21 | 28 | 0.0218 | 0.42757 (31.83) | 1.0 | 0.4587 | 0.7445 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1872 | crypto|donchian(entry_n=55,exit_n=20) | 45.08/1.08/-14.84 | 56.21 | 24 | 0.0218 | 0.31169 (27.15) | 1.0 | 0.4873 | 0.7205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1873 | crypto|donchian(entry_n=100,exit_n=10) | 13.94/0.52/-18.64 | 56.21 | 20 | 0.0224 | 0.63037 (25.4) | 1.0 | 0.2379 | 0.8355 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1874 | crypto|donchian(entry_n=100,exit_n=20) | 12.91/0.47/-23.93 | 56.21 | 18 | 0.0224 | 0.63736 (26.34) | 1.0 | 0.2206 | 0.8415 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
