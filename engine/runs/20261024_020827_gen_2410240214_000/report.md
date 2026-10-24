# gen_2410240214_000 — engine run 20261024_020827_gen_2410240214_000

Hypothesis: grammar draw seed=2410240214: drop_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1586. PBO (CSCV) across family: 0.457. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 163c13dbc947dbc7fb4dd19a35602ef033b61fd3f8ae6b73800997fdf433b3a5. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1579 | crypto|drop_revert(drop=0.05,hold=3,n=1)+vol_regime(max_atr_pct=0.06) | -2.53/-0.52/-3.98 | 428.6 | 147 | 0.0281 | 0.92108 (77.02) | 1.0 | 0.0001 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1580 | crypto|drop_revert(drop=0.05,hold=3,n=3)+vol_regime(max_atr_pct=0.06) | 5.75/0.65/-3.45 | 428.6 | 507 | 0.0364 | 0.89111 (87.23) | 1.0 | 0.0322 | 0.9035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1581 | crypto|drop_revert(drop=0.05,hold=5,n=1)+vol_regime(max_atr_pct=0.06) | -3.07/-0.47/-4.02 | 428.6 | 154 | 0.0274 | 0.91808 (87.24) | 1.0 | 0.0002 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1582 | crypto|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.06) | 13.89/0.98/-5.04 | 428.6 | 482 | 0.0373 | 0.81518 (75.54) | 1.0 | 0.0696 | 0.896 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1583 | crypto|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.06) | -0.6/-0.82/-0.6 | 428.6 | 6 | 0.0188 | 0.95105 (296.69) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1584 | crypto|drop_revert(drop=0.1,hold=3,n=3)+vol_regime(max_atr_pct=0.06) | 0.46/0.34/-0.71 | 428.6 | 21 | 0.0216 | 0.95704 (59.06) | 1.0 | 0.0066 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1585 | crypto|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.06) | 0.35/0.26/-0.6 | 428.6 | 7 | 0.0181 | 0.95305 (46.47) | 1.0 | 0.0056 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1586 | crypto|drop_revert(drop=0.1,hold=5,n=3)+vol_regime(max_atr_pct=0.06) | 1.51/0.69/-0.6 | 428.6 | 25 | 0.0207 | 0.96204 (74.49) | 1.0 | 0.006 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
