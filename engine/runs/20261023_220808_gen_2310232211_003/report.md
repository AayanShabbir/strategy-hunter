# gen_2310232211_003 — engine run 20261023_220808_gen_2310232211_003

Hypothesis: grammar draw seed=2310232211: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1050. PBO (CSCV) across family: 0.222. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d2975f54503b359117af9b4b6efd0a08e8e6612c2ac7aaa076bf22b3e302075b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1043 | sectors|rsi_revert(entry=10,exit=60,n=2)+vol_regime(max_atr_pct=0.06) | 15.83/0.8/-5.08 | 50.2 | 983 | 0.0699 | 0.7033 (19.09) | 1.0 | 0.6141 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1044 | sectors|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0626 | 0.997 (23.44) | 1.0 | 0.4843 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1045 | sectors|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 24.64/1.02/-5.5 | 50.2 | 836 | 0.071 | 0.1958 (19.71) | 1.0 | 0.7584 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1046 | sectors|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 11.32/1.19/-2.1 | 50.2 | 85 | 0.0601 | 0.92907 (22.98) | 1.0 | 0.8466 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1047 | sectors|rsi_revert(entry=20,exit=60,n=2)+vol_regime(max_atr_pct=0.06) | 16.85/0.73/-8.14 | 50.2 | 1633 | 0.0703 | 0.45954 (16.33) | 1.0 | 0.5457 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1048 | sectors|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0653 | 0.43357 (21.79) | 1.0 | 0.8176 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1049 | sectors|rsi_revert(entry=20,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 28.11/0.99/-10.59 | 50.2 | 1272 | 0.0709 | 0.04795 (17.69) | 1.0 | 0.7222 | 0.95 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1050 | sectors|rsi_revert(entry=20,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 33.87/1.16/-10.14 | 50.2 | 259 | 0.0674 | 0.02897 (22.08) | 1.0 | 0.8112 | 0.8725 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
