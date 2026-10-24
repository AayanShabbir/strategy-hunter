# gen_2610241015_000 — engine run 20261024_101008_gen_2610241015_000

Hypothesis: grammar draw seed=2610241015: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 2350. PBO (CSCV) across family: 0.16. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 4c791a55227c5797ad0c290f581cb8f75963e203c4eaa4fcadf19f6930dfe988. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2347 | crypto|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.06) | 16.32/0.61/-17.72 | 434.62 | 49 | 0.0182 | 0.8012 (187.34) | 1.0 | 0.3139 | 0.9005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2348 | crypto|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.06) | 18.21/0.6/-16.37 | 434.62 | 55 | 0.0172 | 0.74326 (66.28) | 1.0 | 0.3088 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2349 | crypto|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 5.02/0.29/-15.71 | 434.62 | 30 | 0.02 | 0.84815 (136.93) | 1.0 | 0.1918 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2350 | crypto|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | -2.77/0.0/-19.5 | 434.62 | 38 | 0.0174 | 0.91309 (86.56) | 1.0 | 0.1132 | 0.9125 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
