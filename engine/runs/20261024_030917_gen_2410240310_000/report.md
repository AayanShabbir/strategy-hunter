# gen_2410240310_000 — engine run 20261024_030917_gen_2410240310_000

Hypothesis: grammar draw seed=2410240310: drop_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1622. PBO (CSCV) across family: 0.955. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 0df3516763697867b9e8a9da023948f2a930e9432dc4af8bb496114ecd45887b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1615 | sectors|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.02) | 0.11/0.04/-1.04 | 57.67 | 36 | 0.0578 | 1.0 (26.42) | 1.0 | 0.0137 | 0.4885 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1616 | sectors|drop_revert(drop=0.05,hold=5,n=5)+vol_regime(max_atr_pct=0.02) | -0.03/0.0/-2.26 | 57.67 | 67 | 0.0562 | 1.0 (26.1) | 1.0 | 0.0116 | 0.4885 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1617 | sectors|drop_revert(drop=0.05,hold=10,n=3)+vol_regime(max_atr_pct=0.02) | 2.84/0.77/-1.11 | 57.67 | 50 | 0.0547 | 1.0 (26.55) | 1.0 | 0.1811 | 0.488 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1618 | sectors|drop_revert(drop=0.05,hold=10,n=5)+vol_regime(max_atr_pct=0.02) | 3.67/0.6/-2.58 | 57.67 | 85 | 0.0535 | 0.998 (26.16) | 1.0 | 0.1125 | 0.4855 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1619 | sectors|drop_revert(drop=0.15,hold=5,n=3)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1620 | sectors|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (27.27) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1621 | sectors|drop_revert(drop=0.15,hold=10,n=3)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1622 | sectors|drop_revert(drop=0.15,hold=10,n=5)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 1 | 0.0509 | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
