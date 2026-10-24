# gen_2410240600_000 — engine run 20261024_060448_gen_2410240600_000

Hypothesis: grammar draw seed=2410240600: donchian

**0/4 pass.** Ledger N at evaluation: 1894. PBO (CSCV) across family: 0.49. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 a3034070e0d1cab05903b73ca483224512786b8f4cbd061dc0f06d040923e37b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1891 | crypto|donchian(entry_n=55,exit_n=10) | 250.98/0.87/-24.68 | 428.6 | 959 | 0.1037 | 0.27972 (121.87) | 1.0 | 0.949 | 0.9495 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1892 | crypto|donchian(entry_n=55,exit_n=20) | 212.99/0.83/-38.82 | 428.6 | 771 | 0.1005 | 0.38561 (76.95) | 1.0 | 0.928 | 0.9705 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1893 | crypto|donchian(entry_n=100,exit_n=10) | 328.47/0.94/-15.33 | 428.6 | 689 | 0.0994 | 0.15185 (73.39) | 1.0 | 0.9763 | 0.8875 | False | beats_buy_hold, cost_stop, holm, spa |
| 1894 | crypto|donchian(entry_n=100,exit_n=20) | 329.19/0.94/-22.39 | 428.6 | 554 | 0.0976 | 0.15485 (132.47) | 1.0 | 0.9757 | 0.8905 | False | beats_buy_hold, cost_stop, holm, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
