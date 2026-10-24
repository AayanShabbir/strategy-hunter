# gen_2410240610_000 — engine run 20261024_060530_gen_2410240610_000

Hypothesis: grammar draw seed=2410240610: supertrend+day_of_week

**0/20 pass.** Ledger N at evaluation: 1986. PBO (CSCV) across family: 0.18. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 2c454768826366e13da2b9a61f7e7d4914fed657aa9ea23aca79aea43b7450aa. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1967 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | 7.21/0.97/-3.59 | 26.77 | 963 | 0.1248 | 0.81518 (7.83) | 1.0 | 0.0036 | 0.8365 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1968 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | 0.76/0.1/-9.01 | 26.77 | 1127 | 0.1258 | 0.90809 (6.67) | 1.0 | 0.0002 | 0.904 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1969 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | 6.99/0.63/-6.08 | 26.77 | 1109 | 0.1247 | 0.69231 (7.4) | 1.0 | 0.0016 | 0.8295 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1970 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -11.18/-1.13/-14.65 | 26.77 | 1064 | 0.1213 | 0.99401 (8.01) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1971 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=4) | 0.78/0.11/-5.69 | 26.77 | 977 | 0.1276 | 0.96503 (7.83) | 1.0 | 0.0001 | 0.918 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1972 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | 10.03/1.45/-3.83 | 26.77 | 830 | 0.1299 | 0.58042 (8.2) | 1.0 | 0.0328 | 0.7915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1973 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | -5.89/-0.64/-7.61 | 26.77 | 954 | 0.1293 | 0.98601 (8.01) | 1.0 | 0.0 | 0.9515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1974 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | 6.65/0.58/-7.26 | 26.77 | 979 | 0.1289 | 0.77223 (7.71) | 1.0 | 0.0007 | 0.8365 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1975 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | -11.69/-1.18/-14.32 | 26.77 | 959 | 0.1265 | 0.997 (8.2) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1976 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | -18.39/-0.91/-23.11 | 26.77 | 920 | 0.1291 | 0.97303 (8.34) | 1.0 | 0.0 | 0.9545 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1977 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | 4.27/0.57/-3.66 | 26.77 | 970 | 0.1248 | 0.86314 (7.92) | 1.0 | 0.0008 | 0.878 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1978 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | 0.15/0.05/-9.27 | 26.77 | 1117 | 0.1259 | 0.92607 (7.17) | 1.0 | 0.0001 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1979 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 7.72/0.69/-6.09 | 26.77 | 1113 | 0.1256 | 0.70729 (7.91) | 1.0 | 0.002 | 0.8175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1980 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -9.78/-0.89/-15.24 | 26.77 | 1083 | 0.1212 | 0.99401 (7.7) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1981 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | 0.8/0.11/-4.75 | 26.77 | 995 | 0.1273 | 0.95405 (7.92) | 1.0 | 0.0001 | 0.9235 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1982 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | 9.49/1.37/-3.76 | 26.77 | 828 | 0.1292 | 0.58841 (8.22) | 1.0 | 0.0264 | 0.7955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1983 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -4.73/-0.52/-7.22 | 26.77 | 954 | 0.1281 | 0.97403 (7.51) | 1.0 | 0.0 | 0.945 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1984 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 5.56/0.48/-8.74 | 26.77 | 988 | 0.1283 | 0.78821 (8.6) | 1.0 | 0.0006 | 0.8475 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1985 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | -10.68/-1.06/-13.34 | 26.77 | 959 | 0.1274 | 0.995 (8.56) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1986 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -18.5/-0.91/-23.44 | 26.77 | 927 | 0.1289 | 0.97403 (8.22) | 1.0 | 0.0 | 0.9545 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
