# gen_2410240318_000 — engine run 20261024_030956_gen_2410240318_000

Hypothesis: grammar draw seed=2410240318: sma_cross+day_of_week

**0/16 pass.** Ledger N at evaluation: 1690. PBO (CSCV) across family: 0.004. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 e015e0abdf1a02cd4b24f08c701ac2e5c5b9bf547f591e7e379387d2aabf14c4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1675 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=1) | 26.01/0.56/-25.23 | 872.11 | 1255 | 0.0242 | 1.0 (195.55) | 1.0 | 0.0015 | 0.502 | False | beats_buy_hold, holm, dsr, spa |
| 1676 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=2) | -29.52/-0.67/-35.62 | 872.11 | 1240 | 0.024 | 1.0 (198.59) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1677 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=3) | 30.31/0.63/-15.68 | 872.11 | 1222 | 0.0241 | 1.0 (199.1) | 1.0 | 0.0025 | 0.495 | False | beats_buy_hold, holm, dsr, spa |
| 1678 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=4) | 55.27/1.12/-14.7 | 872.11 | 1232 | 0.0241 | 0.996 (199.19) | 1.0 | 0.0236 | 0.502 | False | beats_buy_hold, holm, dsr, spa |
| 1679 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=1) | 36.57/0.73/-21.31 | 872.11 | 1237 | 0.024 | 0.999 (198.82) | 1.0 | 0.0036 | 0.499 | False | beats_buy_hold, holm, dsr, spa |
| 1680 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=2) | -27.47/-0.61/-36.15 | 872.11 | 1219 | 0.0239 | 1.0 (200.48) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1681 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=3) | 28.57/0.58/-14.56 | 872.11 | 1201 | 0.0239 | 1.0 (196.14) | 1.0 | 0.0022 | 0.493 | False | beats_buy_hold, holm, dsr, spa |
| 1682 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=4) | 46.62/0.97/-13.95 | 872.11 | 1208 | 0.024 | 0.997 (193.16) | 1.0 | 0.0112 | 0.504 | False | beats_buy_hold, holm, dsr, spa |
| 1683 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=1) | 19.28/0.45/-27.07 | 872.11 | 1258 | 0.0241 | 0.999 (196.48) | 1.0 | 0.0008 | 0.4985 | False | beats_buy_hold, holm, dsr, spa |
| 1684 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=2) | -29.02/-0.66/-36.34 | 872.11 | 1245 | 0.0239 | 1.0 (195.6) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1685 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=3) | 25.97/0.55/-16.13 | 872.11 | 1228 | 0.024 | 0.999 (194.99) | 1.0 | 0.002 | 0.5005 | False | beats_buy_hold, holm, dsr, spa |
| 1686 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=4) | 71.43/1.34/-14.42 | 872.11 | 1234 | 0.024 | 0.98302 (202.41) | 1.0 | 0.0462 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 1687 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=1) | 35.24/0.7/-21.59 | 872.11 | 1240 | 0.0238 | 0.997 (195.5) | 1.0 | 0.0033 | 0.5 | False | beats_buy_hold, holm, dsr, spa |
| 1688 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=2) | -27.43/-0.61/-37.07 | 872.11 | 1227 | 0.0238 | 1.0 (203.77) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1689 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=3) | 29.81/0.59/-16.43 | 872.11 | 1212 | 0.0239 | 1.0 (203.59) | 1.0 | 0.0024 | 0.489 | False | beats_buy_hold, holm, dsr, spa |
| 1690 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=4) | 45.49/0.93/-14.13 | 872.11 | 1210 | 0.0239 | 0.996 (199.35) | 1.0 | 0.0094 | 0.5025 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
