# gen_2310232012_000 — engine run 20261023_201054_gen_2310232012_000

Hypothesis: grammar draw seed=2310232012: donchian+day_of_week

**0/16 pass.** Ledger N at evaluation: 822. PBO (CSCV) across family: 0.445. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 96ec04e9f0947f37483d82f00f70db7c4700a155ccd190bea79a5eef186179f6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 807 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=0) | -0.96/-0.12/-3.47 | 63.33 | 1151 | 0.0812 | 1.0 (22.01) | 1.0 | 0.0003 | 0.495 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 808 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=1) | 3.98/0.49/-3.41 | 63.33 | 1275 | 0.0821 | 0.995 (21.97) | 1.0 | 0.0095 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 809 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=2) | -9.05/-1.06/-10.8 | 63.33 | 1275 | 0.0818 | 1.0 (21.47) | 1.0 | 0.0 | 0.4875 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 810 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=3) | -5.34/-0.6/-6.87 | 63.33 | 1263 | 0.0822 | 1.0 (21.3) | 1.0 | 0.0 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 811 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=0) | 1.28/0.15/-3.65 | 63.33 | 1500 | 0.0791 | 0.995 (20.79) | 1.0 | 0.0016 | 0.4975 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 812 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=1) | 3.87/0.41/-3.37 | 63.33 | 1666 | 0.08 | 0.98801 (19.72) | 1.0 | 0.007 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 813 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=2) | -11.55/-1.15/-13.35 | 63.33 | 1651 | 0.08 | 1.0 (20.08) | 1.0 | 0.0 | 0.4945 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 814 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=3) | -3.72/-0.33/-7.63 | 63.33 | 1630 | 0.0801 | 1.0 (20.03) | 1.0 | 0.0001 | 0.496 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 815 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=0) | -1.35/-0.21/-3.84 | 63.33 | 950 | 0.0844 | 1.0 (23.21) | 1.0 | 0.0002 | 0.498 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 816 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=1) | 3.56/0.52/-4.03 | 63.33 | 1063 | 0.0858 | 0.999 (22.57) | 1.0 | 0.0113 | 0.496 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 817 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=2) | -6.9/-0.93/-8.33 | 63.33 | 1070 | 0.0853 | 1.0 (22.97) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 818 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=3) | -4.26/-0.51/-6.22 | 63.33 | 1063 | 0.0857 | 1.0 (22.87) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 819 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=0) | 0.2/0.04/-3.07 | 63.33 | 1256 | 0.0821 | 1.0 (22.21) | 1.0 | 0.0009 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 820 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=1) | 3.44/0.42/-3.08 | 63.33 | 1412 | 0.0829 | 0.99001 (21.08) | 1.0 | 0.0076 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 821 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=2) | -9.72/-1.08/-11.21 | 63.33 | 1402 | 0.0828 | 1.0 (21.21) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 822 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=3) | -2.82/-0.26/-7.06 | 63.33 | 1385 | 0.0833 | 1.0 (21.32) | 1.0 | 0.0001 | 0.4975 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
