# gen_2610241010_000 — engine run 20261024_101000_gen_2610241010_000

Hypothesis: grammar draw seed=2610241010: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 2334. PBO (CSCV) across family: 0.161. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 008d209a34f6d8b7826377dc4a70377ea0db48e871c03506297aa659f72ddee9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2327 | crypto|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 15.69/0.94/-7.05 | 434.62 | 49 | 0.0202 | 0.79121 (67.27) | 1.0 | 0.5452 | 0.898 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2328 | crypto|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 13.26/1.4/-3.82 | 434.62 | 14 | 0.0188 | 0.82218 (68.45) | 1.0 | 0.7909 | 0.899 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2329 | crypto|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 32.59/1.36/-12.39 | 434.62 | 65 | 0.0175 | 0.67632 (168.28) | 1.0 | 0.7333 | 0.8885 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2330 | crypto|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 19.77/1.07/-12.98 | 434.62 | 22 | 0.0171 | 0.81319 (157.65) | 1.0 | 0.6086 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2331 | crypto|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 18.7/0.73/-16.22 | 434.62 | 117 | 0.0211 | 0.75125 (75.9) | 1.0 | 0.4449 | 0.8945 | False | beats_buy_hold, holm, dsr, spa |
| 2332 | crypto|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 15.49/0.83/-13.47 | 434.62 | 57 | 0.0181 | 0.78022 (237.16) | 1.0 | 0.4976 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2333 | crypto|rsi_revert(entry=20,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 34.19/0.97/-18.4 | 434.62 | 124 | 0.0181 | 0.63636 (190.65) | 1.0 | 0.5658 | 0.8905 | False | beats_buy_hold, holm, dsr, spa |
| 2334 | crypto|rsi_revert(entry=20,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 40.0/1.17/-14.26 | 434.62 | 76 | 0.0172 | 0.60839 (74.1) | 1.0 | 0.6571 | 0.8775 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
