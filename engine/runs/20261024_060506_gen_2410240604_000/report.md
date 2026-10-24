# gen_2410240604_000 — engine run 20261024_060506_gen_2410240604_000

Hypothesis: grammar draw seed=2410240604: sma_cross+day_of_week

**0/16 pass.** Ledger N at evaluation: 1930. PBO (CSCV) across family: 0.347. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 630af81a08ea221636fddcc87909c1cc38b507f1fc8170b94a2ce443aacda863. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1915 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=1) | 3.83/0.31/-5.22 | 78.13 | 1619 | 0.0875 | 0.98801 (20.53) | 1.0 | 0.0034 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1916 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=2) | -12.15/-1.02/-14.78 | 78.13 | 1594 | 0.0869 | 1.0 (20.26) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1917 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=3) | -6.32/-0.51/-10.46 | 78.13 | 1562 | 0.087 | 0.999 (20.31) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1918 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=4) | -3.8/-0.33/-10.54 | 78.13 | 1565 | 0.0873 | 0.999 (21.09) | 1.0 | 0.0001 | 0.4885 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1919 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=1) | 1.46/0.13/-7.1 | 78.13 | 1692 | 0.0871 | 0.99401 (19.35) | 1.0 | 0.0014 | 0.5115 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1920 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=2) | -12.53/-1.0/-14.03 | 78.13 | 1671 | 0.0868 | 1.0 (19.67) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1921 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=3) | -11.12/-0.86/-14.36 | 78.13 | 1650 | 0.087 | 1.0 (20.2) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1922 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=4) | -2.03/-0.17/-7.79 | 78.13 | 1651 | 0.0873 | 0.999 (19.15) | 1.0 | 0.0002 | 0.4885 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1923 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=1) | 4.29/0.34/-3.92 | 78.13 | 1618 | 0.0868 | 0.98701 (20.94) | 1.0 | 0.004 | 0.507 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1924 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=2) | -15.77/-1.34/-18.01 | 78.13 | 1595 | 0.0863 | 1.0 (21.39) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1925 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=3) | -9.25/-0.72/-11.93 | 78.13 | 1569 | 0.0865 | 1.0 (21.09) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1926 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=4) | 0.65/0.08/-6.45 | 78.13 | 1563 | 0.0871 | 0.995 (21.47) | 1.0 | 0.0009 | 0.485 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1927 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=1) | 2.65/0.22/-6.11 | 78.13 | 1691 | 0.087 | 0.98302 (19.34) | 1.0 | 0.0023 | 0.507 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1928 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=2) | -12.66/-1.01/-14.06 | 78.13 | 1672 | 0.0865 | 1.0 (19.57) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1929 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=3) | -10.97/-0.83/-14.16 | 78.13 | 1651 | 0.0865 | 1.0 (19.65) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1930 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=4) | -2.65/-0.22/-7.98 | 78.13 | 1658 | 0.0872 | 0.998 (19.99) | 1.0 | 0.0001 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
