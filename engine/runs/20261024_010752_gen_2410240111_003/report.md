# gen_2410240111_003 — engine run 20261024_010752_gen_2410240111_003

Hypothesis: grammar draw seed=2410240111: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 1430. PBO (CSCV) across family: 0.245. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 0d74e5fef3c45cbab6f237c90b0ddfceb5292f9088b52c69efe826b40c6a75b3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1427 | megacap|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.06) | -10.41/-0.44/-15.86 | 26.77 | 921 | 0.1269 | 0.75624 (9.12) | 1.0 | 0.0001 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1428 | megacap|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.06) | -7.31/-0.24/-20.28 | 26.77 | 1984 | 0.124 | 0.45455 (5.06) | 1.0 | 0.001 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1429 | megacap|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 1.95/0.82/-0.9 | 26.77 | 15 | 0.1217 | 0.93207 (13.31) | 1.0 | 0.0432 | 0.8975 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1430 | megacap|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | 1.31/0.5/-1.43 | 26.77 | 20 | 0.1268 | 0.94406 (12.93) | 1.0 | 0.0263 | 0.9025 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
