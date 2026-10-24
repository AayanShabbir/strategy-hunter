# gen_2310232331_003 — engine run 20261023_230901_gen_2310232331_003

Hypothesis: grammar draw seed=2310232331: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 1262. PBO (CSCV) across family: 0.489. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 352d085d4b232cd43b981179ce569f42f6910bc0e13edd15049b382a034aa446. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1255 | crypto|rsi_revert(entry=10,exit=70,n=2)+rsi_band(hi=60) | -9.95/-0.11/-25.26 | 428.6 | 5375 | 0.1008 | 0.59441 (24.69) | 1.0 | 0.1936 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1256 | crypto|rsi_revert(entry=10,exit=70,n=3)+rsi_band(hi=60) | -16.7/-0.34/-30.56 | 428.6 | 2133 | 0.0977 | 0.91508 (131.27) | 1.0 | 0.1194 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1257 | crypto|rsi_revert(entry=10,exit=80,n=2)+rsi_band(hi=60) | -21.16/-0.32/-37.99 | 428.6 | 4786 | 0.1015 | 0.75824 (38.05) | 1.0 | 0.1282 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1258 | crypto|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=60) | -18.56/-0.28/-33.19 | 428.6 | 1849 | 0.0991 | 0.92408 (64.25) | 1.0 | 0.1369 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1259 | crypto|rsi_revert(entry=20,exit=70,n=2)+rsi_band(hi=60) | -32.9/-0.63/-44.6 | 428.6 | 8290 | 0.1023 | 0.55245 (-22.11) | 1.0 | 0.0651 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1260 | crypto|rsi_revert(entry=20,exit=70,n=3)+rsi_band(hi=60) | -26.85/-0.45/-44.01 | 428.6 | 4242 | 0.1018 | 0.84216 (91.76) | 1.0 | 0.098 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1261 | crypto|rsi_revert(entry=20,exit=80,n=2)+rsi_band(hi=60) | -32.94/-0.53/-50.85 | 428.6 | 7042 | 0.1032 | 0.66733 (-10.65) | 1.0 | 0.0822 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1262 | crypto|rsi_revert(entry=20,exit=80,n=3)+rsi_band(hi=60) | -16.76/-0.12/-41.98 | 428.6 | 3426 | 0.1017 | 0.7952 (27.3) | 1.0 | 0.1901 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
