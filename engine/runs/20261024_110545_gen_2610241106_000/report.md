# gen_2610241106_000 — engine run 20261024_110545_gen_2610241106_000

Hypothesis: grammar draw seed=2610241106: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 2422. PBO (CSCV) across family: 0.677. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 b15a83de574ecc75f794dee63e13acf797dc6ea0e38bf42340505d4ec298be87. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2415 | megacap|rsi_revert(entry=5,exit=60,n=2)+rsi_band(hi=70) | 25.47/0.84/-6.22 | 118.49 | 112 | 0.0486 | 0.84515 (45.06) | 1.0 | 0.8165 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2416 | megacap|rsi_revert(entry=5,exit=60,n=3)+rsi_band(hi=70) | 12.68/0.73/-3.85 | 118.49 | 27 | 0.0427 | 0.95305 (46.82) | 1.0 | 0.7235 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2417 | megacap|rsi_revert(entry=5,exit=70,n=2)+rsi_band(hi=70) | 34.15/1.03/-5.95 | 118.49 | 108 | 0.0494 | 0.70929 (46.59) | 1.0 | 0.9127 | 0.9715 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2418 | megacap|rsi_revert(entry=5,exit=70,n=3)+rsi_band(hi=70) | 21.55/1.08/-3.86 | 118.49 | 27 | 0.0427 | 0.85814 (48.11) | 1.0 | 0.9117 | 0.4935 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2419 | megacap|rsi_revert(entry=10,exit=60,n=2)+rsi_band(hi=70) | 29.82/0.83/-10.27 | 118.49 | 208 | 0.0494 | 0.74126 (44.27) | 1.0 | 0.7786 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2420 | megacap|rsi_revert(entry=10,exit=60,n=3)+rsi_band(hi=70) | 21.44/0.72/-6.23 | 118.49 | 70 | 0.0502 | 0.9001 (46.29) | 1.0 | 0.7271 | 0.4945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2421 | megacap|rsi_revert(entry=10,exit=70,n=2)+rsi_band(hi=70) | 35.83/0.91/-11.56 | 118.49 | 198 | 0.0497 | 0.65435 (44.7) | 1.0 | 0.8236 | 0.977 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2422 | megacap|rsi_revert(entry=10,exit=70,n=3)+rsi_band(hi=70) | 27.29/0.84/-7.37 | 118.49 | 68 | 0.05 | 0.81818 (45.85) | 1.0 | 0.7978 | 0.973 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
