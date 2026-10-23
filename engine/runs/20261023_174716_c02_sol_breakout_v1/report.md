# c02_sol_breakout_v1 — engine run 20261023_174716_c02_sol_breakout_v1

Hypothesis: Long/flat Donchian breakout (buy close above prior N-day high, exit below prior M-day low) on SOL and an alt basket beats buy-and-hold OOS net of 35 bps/side, since breakout/channel rules are among the trend families that survived data-snooping controls in crypto (Hudson & Urquhart 2021). 5x ATR stop. Strategy Scout crypto submission.

**0/8 pass.** Ledger N at evaluation: 474. PBO (CSCV) across family: 0.805. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 d7576baa60a52713713045156d47adc7ad5f1ba47f6b304623d731f4acc5fe3e. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 467 | SOL|donchian(entry_n=20,exit_n=10) | -10.12/0.03/-42.44 | 923.45 | 18 | 0.0192 | 0.85115 (158.46) | 1.0 | 0.0527 | 0.903 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 468 | SOL|donchian(entry_n=20,exit_n=20) | 11.9/0.33/-53.02 | 923.45 | 12 | 0.0187 | 0.71029 (103.17) | 1.0 | 0.1178 | 0.8945 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 469 | SOL|donchian(entry_n=55,exit_n=10) | -38.03/-0.67/-56.72 | 923.45 | 11 | 0.0217 | 0.96404 (385.31) | 1.0 | 0.0043 | 0.9175 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 470 | SOL|donchian(entry_n=55,exit_n=20) | -31.81/-0.32/-63.28 | 923.45 | 8 | 0.0212 | 0.93107 (113.78) | 1.0 | 0.0173 | 0.9155 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 471 | ALTS|donchian(entry_n=20,exit_n=10) | -2.08/0.13/-38.54 | 193.2 | 129 | 0.023 | 0.87213 (73.74) | 1.0 | 0.0702 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 472 | ALTS|donchian(entry_n=20,exit_n=20) | 11.19/0.33/-42.24 | 193.2 | 94 | 0.0225 | 0.80719 (84.95) | 1.0 | 0.1177 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 473 | ALTS|donchian(entry_n=55,exit_n=10) | 8.73/0.28/-41.93 | 193.2 | 76 | 0.0242 | 0.81419 (78.92) | 1.0 | 0.1062 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 474 | ALTS|donchian(entry_n=55,exit_n=20) | 19.27/0.42/-40.35 | 193.2 | 62 | 0.0243 | 0.71029 (91.93) | 1.0 | 0.1489 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
