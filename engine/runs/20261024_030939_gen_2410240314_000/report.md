# gen_2410240314_000 — engine run 20261024_030939_gen_2410240314_000

Hypothesis: grammar draw seed=2410240314: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1646. PBO (CSCV) across family: 0.09. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 7d5246bd2ab2a1f437df151207ad056e610501723bed6b4b7120d8b6fd81e164. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1639 | crypto|rsi_revert(entry=10,exit=60,n=2) | -28.7/-0.77/-30.12 | 428.6 | 5809 | 0.1004 | 0.75225 (63.8) | 1.0 | 0.0051 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1640 | crypto|rsi_revert(entry=10,exit=60,n=3) | -12.19/-0.29/-23.96 | 428.6 | 2329 | 0.0961 | 0.86214 (73.53) | 1.0 | 0.026 | 0.9185 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1641 | crypto|rsi_revert(entry=10,exit=80,n=2) | -26.82/-0.47/-40.98 | 428.6 | 4730 | 0.1014 | 0.7952 (16.69) | 1.0 | 0.0154 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1642 | crypto|rsi_revert(entry=10,exit=80,n=3) | -18.34/-0.28/-33.41 | 428.6 | 1826 | 0.099 | 0.92108 (74.12) | 1.0 | 0.0271 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1643 | crypto|rsi_revert(entry=20,exit=60,n=2) | -49.65/-1.35/-51.19 | 428.6 | 9537 | 0.1013 | 0.72527 (2.35) | 1.0 | 0.0004 | 0.926 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1644 | crypto|rsi_revert(entry=20,exit=60,n=3) | -28.41/-0.59/-39.75 | 428.6 | 4920 | 0.1012 | 0.81119 (25.89) | 1.0 | 0.0101 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1645 | crypto|rsi_revert(entry=20,exit=80,n=2) | -37.55/-0.65/-54.44 | 428.6 | 6954 | 0.103 | 0.75624 (6.62) | 1.0 | 0.0084 | 0.926 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1646 | crypto|rsi_revert(entry=20,exit=80,n=3) | -17.84/-0.13/-44.65 | 428.6 | 3211 | 0.1017 | 0.83716 (27.55) | 1.0 | 0.0425 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
