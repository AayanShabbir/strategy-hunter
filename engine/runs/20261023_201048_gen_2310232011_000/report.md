# gen_2310232011_000 — engine run 20261023_201048_gen_2310232011_000

Hypothesis: grammar draw seed=2310232011: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 806. PBO (CSCV) across family: 0.544. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 60bdecd7082b3858532fd6762aed896074c1a7322132061d639f1b2f8e291719. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 799 | megacap|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.0) | 19.29/0.72/-3.4 | 214.9 | 530 | 0.0441 | 0.999 (76.14) | 1.0 | 0.5125 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 800 | megacap|rsi_revert(entry=10,exit=60,n=5)+relvol(min_ratio=1.0) | 6.54/0.92/-1.23 | 214.9 | 62 | 0.0392 | 0.995 (76.65) | 1.0 | 0.6844 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 801 | megacap|rsi_revert(entry=10,exit=80,n=2)+relvol(min_ratio=1.0) | 22.04/0.76/-5.76 | 214.9 | 661 | 0.0427 | 0.996 (71.98) | 1.0 | 0.5476 | 0.4845 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 802 | megacap|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.0) | 6.03/0.38/-4.96 | 214.9 | 168 | 0.0353 | 0.996 (76.17) | 1.0 | 0.2584 | 0.4995 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 803 | megacap|rsi_revert(entry=20,exit=60,n=2)+relvol(min_ratio=1.0) | 34.07/1.03/-4.04 | 214.9 | 809 | 0.0442 | 0.98102 (71.49) | 1.0 | 0.7782 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 804 | megacap|rsi_revert(entry=20,exit=60,n=5)+relvol(min_ratio=1.0) | 28.8/1.03/-2.97 | 214.9 | 346 | 0.0398 | 0.99401 (77.16) | 1.0 | 0.8145 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 805 | megacap|rsi_revert(entry=20,exit=80,n=2)+relvol(min_ratio=1.0) | 35.14/1.0/-6.16 | 214.9 | 933 | 0.0437 | 0.96803 (70.67) | 1.0 | 0.7467 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 806 | megacap|rsi_revert(entry=20,exit=80,n=5)+relvol(min_ratio=1.0) | 31.85/0.97/-8.24 | 214.9 | 672 | 0.0388 | 0.97902 (74.52) | 1.0 | 0.7108 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
