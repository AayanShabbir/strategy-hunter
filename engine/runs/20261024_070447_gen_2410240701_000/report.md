# gen_2410240701_000 — engine run 20261024_070447_gen_2410240701_000

Hypothesis: grammar draw seed=2410240701: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2002. PBO (CSCV) across family: 0.644. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 43b432e663df47bea4af878e2357ef32e746de3f0503eac45b72c6743e4c39d9. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1995 | sectors|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=50) | -0.63/-0.54/-0.63 | 50.2 | 36 | 0.0368 | 1.0 (23.24) | 1.0 | 0.0055 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1996 | sectors|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=50) | -0.59/-0.48/-0.78 | 50.2 | 63 | 0.0423 | 1.0 (23.28) | 1.0 | 0.0123 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1997 | sectors|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=50) | -0.61/-0.49/-0.8 | 50.2 | 54 | 0.0422 | 1.0 (23.58) | 1.0 | 0.0091 | 0.4945 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1998 | sectors|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=50) | -0.16/-0.1/-0.88 | 50.2 | 89 | 0.0438 | 1.0 (22.82) | 1.0 | 0.084 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1999 | sectors|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 1 | 0.0197 | 1.0 (23.8) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2000 | sectors|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.42) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2001 | sectors|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 1 | 0.0197 | 1.0 (22.82) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2002 | sectors|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.61) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
