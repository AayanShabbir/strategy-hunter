# gen_2610240803_000 — engine run 20261024_080326_gen_2610240803_000

Hypothesis: grammar draw seed=2610240803: donchian+day_of_week

**0/20 pass.** Ledger N at evaluation: 2122. PBO (CSCV) across family: 0.31. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 aea6bf9c0a06f96b731d101cc253515be24905543f3ec2da3d3168999ed42f80. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2103 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=0) | -9.41/-0.87/-10.5 | 5.92 | 804 | 0.054 | 0.72627 (-1.61) | 1.0 | 0.0 | 0.7565 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2104 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=1) | -4.99/-0.36/-8.3 | 5.92 | 899 | 0.0548 | 0.59341 (-2.05) | 1.0 | 0.0002 | 0.7245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2105 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=2) | -16.5/-1.23/-18.42 | 5.92 | 888 | 0.0551 | 0.88112 (-2.4) | 1.0 | 0.0 | 0.851 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2106 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=3) | -8.88/-0.57/-11.91 | 5.92 | 875 | 0.0549 | 0.71029 (-2.32) | 1.0 | 0.0001 | 0.7675 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2107 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=4) | -9.56/-0.75/-10.62 | 5.92 | 871 | 0.055 | 0.72927 (-1.48) | 1.0 | 0.0 | 0.7575 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2108 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=0) | -4.54/-0.29/-6.91 | 5.92 | 1078 | 0.0533 | 0.4955 (-4.1) | 1.0 | 0.0004 | 0.691 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2109 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=1) | -2.99/-0.17/-10.34 | 5.92 | 1202 | 0.054 | 0.45954 (-4.79) | 1.0 | 0.0009 | 0.688 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2110 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=2) | -17.17/-1.02/-18.62 | 5.92 | 1195 | 0.0543 | 0.85115 (-4.6) | 1.0 | 0.0 | 0.8665 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2111 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=3) | -15.98/-0.85/-22.56 | 5.92 | 1187 | 0.0537 | 0.83916 (-4.0) | 1.0 | 0.0 | 0.8655 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2112 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=4) | -17.28/-1.13/-18.35 | 5.92 | 1179 | 0.0537 | 0.85015 (-3.97) | 1.0 | 0.0 | 0.8455 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2113 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=0) | -4.24/-0.48/-7.78 | 5.92 | 510 | 0.0559 | 0.61738 (-0.38) | 1.0 | 0.0001 | 0.6915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2114 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=1) | -0.12/0.0/-4.97 | 5.92 | 576 | 0.0558 | 0.51449 (0.02) | 1.0 | 0.0023 | 0.6565 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2115 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=2) | -4.86/-0.55/-7.35 | 5.92 | 561 | 0.0565 | 0.63137 (-0.44) | 1.0 | 0.0 | 0.714 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2116 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=3) | 4.15/0.35/-4.15 | 5.92 | 557 | 0.0567 | 0.36563 (-0.08) | 1.0 | 0.0103 | 0.5765 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2117 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=4) | -9.87/-0.99/-11.08 | 5.92 | 548 | 0.0561 | 0.80719 (0.45) | 1.0 | 0.0 | 0.7635 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2118 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=0) | -4.58/-0.45/-7.33 | 5.92 | 685 | 0.0563 | 0.60539 (-1.19) | 1.0 | 0.0001 | 0.696 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2119 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=1) | 1.33/0.13/-4.55 | 5.92 | 773 | 0.0559 | 0.3986 (-2.34) | 1.0 | 0.0044 | 0.628 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2120 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=2) | -4.49/-0.36/-9.06 | 5.92 | 766 | 0.0563 | 0.57143 (-2.41) | 1.0 | 0.0002 | 0.714 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2121 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=3) | 3.15/0.24/-9.03 | 5.92 | 756 | 0.0565 | 0.35864 (-1.18) | 1.0 | 0.0068 | 0.5955 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2122 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=4) | -13.83/-1.19/-16.45 | 5.92 | 743 | 0.0555 | 0.86214 (-0.84) | 1.0 | 0.0 | 0.8085 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
