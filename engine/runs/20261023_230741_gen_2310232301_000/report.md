# gen_2310232301_000 — engine run 20261023_230741_gen_2310232301_000

Hypothesis: grammar draw seed=2310232301: donchian

**0/4 pass.** Ledger N at evaluation: 1106. PBO (CSCV) across family: 0.585. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 98043440950310671d49ff55adb79a3598b8ff6fa5f49503517c7d2333972d67. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1103 | crypto_d|donchian(entry_n=55,exit_n=10) | 8.89/0.36/-22.01 | 434.62 | 39 | 0.0203 | 0.87612 (190.04) | 1.0 | 0.5272 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1104 | crypto_d|donchian(entry_n=55,exit_n=20) | 15.81/0.49/-26.31 | 434.62 | 32 | 0.0201 | 0.85015 (128.4) | 1.0 | 0.5885 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1105 | crypto_d|donchian(entry_n=100,exit_n=10) | 4.47/0.26/-16.13 | 434.62 | 25 | 0.0211 | 0.88711 (259.81) | 1.0 | 0.4804 | 0.9085 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1106 | crypto_d|donchian(entry_n=100,exit_n=20) | 9.05/0.38/-18.97 | 434.62 | 21 | 0.0211 | 0.82018 (259.52) | 1.0 | 0.5376 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
