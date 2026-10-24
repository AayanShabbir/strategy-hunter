# gen_2410240131_000 — engine run 20261024_010813_gen_2410240131_000

Hypothesis: grammar draw seed=2410240131: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1458. PBO (CSCV) across family: 0.359. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 0dec490a410f75347f3ab7b5335ac07f0262ebf7746060c89fe49332721258c4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1451 | sectors|rsi_revert(entry=5,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 1.44/0.25/-2.7 | 50.2 | 138 | 0.0653 | 1.0 (22.28) | 1.0 | 0.063 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1452 | sectors|rsi_revert(entry=5,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 1.87/0.76/-0.84 | 50.2 | 22 | 0.0597 | 1.0 (23.19) | 1.0 | 0.2515 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1453 | sectors|rsi_revert(entry=5,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 6.2/0.85/-2.45 | 50.2 | 136 | 0.0653 | 0.999 (22.87) | 1.0 | 0.3131 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1454 | sectors|rsi_revert(entry=5,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 4.69/1.29/-0.86 | 50.2 | 26 | 0.0513 | 0.997 (23.96) | 1.0 | 0.6183 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1455 | sectors|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 9.6/0.57/-5.27 | 50.2 | 368 | 0.0666 | 0.98002 (21.6) | 1.0 | 0.1163 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1456 | sectors|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0626 | 0.998 (22.78) | 1.0 | 0.191 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1457 | sectors|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 20.84/0.92/-7.58 | 50.2 | 339 | 0.0675 | 0.55744 (21.95) | 1.0 | 0.3407 | 0.955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1458 | sectors|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 11.32/1.19/-2.1 | 50.2 | 85 | 0.0601 | 0.92507 (23.08) | 1.0 | 0.5459 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
