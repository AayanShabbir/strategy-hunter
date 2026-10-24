# gen_2410240111_001 — engine run 20261024_010749_gen_2410240111_001

Hypothesis: grammar draw seed=2410240111: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 1426. PBO (CSCV) across family: 0.155. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 bfb318a84462a212156644cef3d698f29f8885fda7babbf4415b0a818d68b800. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1423 | megacap|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.04) | -11.03/-0.47/-16.44 | 26.77 | 922 | 0.1269 | 0.77123 (9.31) | 1.0 | 0.0 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1424 | megacap|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.04) | -9.2/-0.32/-21.91 | 26.77 | 1986 | 0.1239 | 0.61139 (5.54) | 1.0 | 0.0 | 0.9305 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1425 | megacap|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.04) | 6.05/1.15/-1.62 | 26.77 | 156 | 0.1681 | 0.85415 (11.19) | 1.0 | 0.0369 | 0.8525 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1426 | megacap|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.04) | -7.82/-0.34/-16.55 | 26.77 | 232 | 0.1502 | 0.76623 (10.28) | 1.0 | 0.0 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
