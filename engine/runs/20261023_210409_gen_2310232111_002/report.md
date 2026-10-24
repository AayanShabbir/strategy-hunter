# gen_2310232111_002 — engine run 20261023_210409_gen_2310232111_002

Hypothesis: grammar draw seed=2310232111: drop_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 926. PBO (CSCV) across family: 0.584. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 2e95d3bd585333ed5c106ef9e7a5ca7128c91612d7bd7ace9bf7bed746c3da96. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 919 | sectors|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (22.45) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 920 | sectors|drop_revert(drop=0.1,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 2.81/0.37/-1.55 | 50.2 | 35 | 0.035 | 0.999 (22.85) | 1.0 | 0.2468 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 921 | sectors|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.01) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 922 | sectors|drop_revert(drop=0.1,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 2.76/0.37/-1.55 | 50.2 | 36 | 0.0349 | 0.999 (23.18) | 1.0 | 0.2434 | 0.5005 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 923 | sectors|drop_revert(drop=0.15,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.37) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 924 | sectors|drop_revert(drop=0.15,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | -0.03/-0.01/-0.59 | 50.2 | 4 | 0.0304 | 0.999 (24.29) | 1.0 | 0.108 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 925 | sectors|drop_revert(drop=0.15,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.01) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 926 | sectors|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | -0.03/-0.01/-0.59 | 50.2 | 4 | 0.0304 | 0.999 (23.4) | 1.0 | 0.108 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
