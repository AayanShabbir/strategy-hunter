# gen_2410240709_000 — engine run 20261024_070513_gen_2410240709_000

Hypothesis: grammar draw seed=2410240709: drop_revert

**0/8 pass.** Ledger N at evaluation: 2046. PBO (CSCV) across family: 0.733. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 c924508fa280299555f1744e03f39ad00aa4a1dc9a17d53decca6de7c4b17efa. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2039 | hibeta|drop_revert(drop=0.05,hold=3,n=1) | 124.02/1.2/-17.41 | 809.88 | 503 | 0.0161 | 0.85315 (212.35) | 1.0 | 0.3551 | 0.5095 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2040 | hibeta|drop_revert(drop=0.05,hold=3,n=5) | 53.09/0.62/-25.79 | 809.88 | 516 | 0.0199 | 0.98901 (212.02) | 1.0 | 0.0869 | 0.5175 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2041 | hibeta|drop_revert(drop=0.05,hold=5,n=1) | 200.16/1.38/-22.26 | 809.88 | 410 | 0.0174 | 0.51349 (211.32) | 1.0 | 0.4934 | 0.5125 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2042 | hibeta|drop_revert(drop=0.05,hold=5,n=5) | 82.08/0.76/-33.74 | 809.88 | 460 | 0.0204 | 0.96004 (212.06) | 1.0 | 0.1329 | 0.515 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2043 | hibeta|drop_revert(drop=0.1,hold=3,n=1) | 55.83/1.62/-4.01 | 809.88 | 87 | 0.0113 | 0.98102 (230.3) | 1.0 | 0.6909 | 0.5065 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2044 | hibeta|drop_revert(drop=0.1,hold=3,n=5) | 47.38/0.68/-17.67 | 809.88 | 293 | 0.0155 | 0.998 (215.67) | 1.0 | 0.0936 | 0.514 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2045 | hibeta|drop_revert(drop=0.1,hold=5,n=1) | 68.15/1.58/-4.95 | 809.88 | 80 | 0.0114 | 0.96703 (219.85) | 1.0 | 0.6545 | 0.499 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2046 | hibeta|drop_revert(drop=0.1,hold=5,n=5) | 87.69/0.95/-18.89 | 809.88 | 276 | 0.0155 | 0.96004 (219.9) | 1.0 | 0.2067 | 0.5015 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
