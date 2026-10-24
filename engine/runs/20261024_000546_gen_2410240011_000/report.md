# gen_2410240011_000 — engine run 20261024_000546_gen_2410240011_000

Hypothesis: grammar draw seed=2410240011: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 1310. PBO (CSCV) across family: 0.524. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 73204d549a0b1537d8280c58e1e6fdc93e626314fcfd9b655412359c353b16bd. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1307 | crypto|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.04) | -3.36/0.07/-36.1 | 428.6 | 1659 | 0.1026 | 0.83317 (149.02) | 1.0 | 0.3671 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1308 | crypto|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.04) | -3.14/0.12/-44.22 | 428.6 | 1305 | 0.0987 | 0.87013 (158.84) | 1.0 | 0.3906 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1309 | crypto|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.04) | 6.87/0.31/-25.03 | 428.6 | 972 | 0.1028 | 0.8002 (65.86) | 1.0 | 0.4802 | 0.9125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1310 | crypto|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.04) | -0.48/0.13/-37.23 | 428.6 | 801 | 0.0979 | 0.88611 (65.36) | 1.0 | 0.3971 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
