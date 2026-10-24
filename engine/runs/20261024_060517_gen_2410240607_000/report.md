# gen_2410240607_000 — engine run 20261024_060517_gen_2410240607_000

Hypothesis: grammar draw seed=2410240607: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 1950. PBO (CSCV) across family: 0.52. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 d98b48e04a01068a3d47a7d35897dbc853921b1f9a867e02f1b29338293e815a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1943 | crypto|rsi_revert(entry=10,exit=70,n=3)+rsi_band(hi=70) | -17.11/-0.36/-30.56 | 428.6 | 2130 | 0.0978 | 0.9001 (59.7) | 1.0 | 0.03 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1944 | crypto|rsi_revert(entry=10,exit=70,n=5)+rsi_band(hi=70) | -23.84/-0.81/-30.67 | 428.6 | 535 | 0.0927 | 0.995 (99.34) | 1.0 | 0.0055 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1945 | crypto|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=70) | -18.34/-0.28/-33.41 | 428.6 | 1825 | 0.099 | 0.92108 (89.13) | 1.0 | 0.0388 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1946 | crypto|rsi_revert(entry=10,exit=80,n=5)+rsi_band(hi=70) | -9.13/-0.11/-31.65 | 428.6 | 478 | 0.0931 | 0.95305 (185.96) | 1.0 | 0.0625 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1947 | crypto|rsi_revert(entry=20,exit=70,n=3)+rsi_band(hi=70) | -28.83/-0.49/-45.79 | 428.6 | 4170 | 0.1017 | 0.86414 (86.09) | 1.0 | 0.0212 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1948 | crypto|rsi_revert(entry=20,exit=70,n=5)+rsi_band(hi=70) | -14.67/-0.17/-26.48 | 428.6 | 1621 | 0.0995 | 0.92408 (162.47) | 1.0 | 0.0528 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1949 | crypto|rsi_revert(entry=20,exit=80,n=3)+rsi_band(hi=70) | -17.84/-0.13/-44.65 | 428.6 | 3212 | 0.1017 | 0.84815 (62.7) | 1.0 | 0.0589 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1950 | crypto|rsi_revert(entry=20,exit=80,n=5)+rsi_band(hi=70) | 9.82/0.37/-28.5 | 428.6 | 1186 | 0.1002 | 0.78422 (171.8) | 1.0 | 0.1716 | 0.899 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
