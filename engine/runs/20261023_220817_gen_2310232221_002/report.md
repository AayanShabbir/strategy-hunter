# gen_2310232221_002 — engine run 20261023_220817_gen_2310232221_002

Hypothesis: grammar draw seed=2310232221: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1070. PBO (CSCV) across family: 0.422. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 ce5e066d74b923c9986f16fb405e3fcda515b95fd2e3a05ea3b256a8484f0704. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1063 | megacap|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.0) | 3.1/0.94/-1.27 | 26.77 | 264 | 0.1095 | 0.86114 (11.78) | 1.0 | 0.5602 | 0.879 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1064 | megacap|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.0) | 1.26/0.62/-0.88 | 26.77 | 50 | 0.0602 | 0.92607 (12.77) | 1.0 | 0.401 | 0.8915 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1065 | megacap|rsi_revert(entry=5,exit=80,n=3)+relvol(min_ratio=1.0) | 3.41/0.85/-1.77 | 26.77 | 368 | 0.1037 | 0.82517 (11.7) | 1.0 | 0.4917 | 0.879 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1066 | megacap|rsi_revert(entry=5,exit=80,n=5)+relvol(min_ratio=1.0) | 1.58/0.7/-0.88 | 26.77 | 102 | 0.0637 | 0.91508 (13.07) | 1.0 | 0.4429 | 0.8895 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1067 | megacap|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.0) | 2.19/0.55/-3.55 | 26.77 | 577 | 0.1157 | 0.82118 (10.89) | 1.0 | 0.429 | 0.8905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1068 | megacap|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.0) | 2.67/0.73/-1.66 | 26.77 | 293 | 0.0995 | 0.85814 (11.78) | 1.0 | 0.4347 | 0.889 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1069 | megacap|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.0) | 2.26/0.48/-2.1 | 26.77 | 756 | 0.113 | 0.76424 (9.64) | 1.0 | 0.3686 | 0.8915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1070 | megacap|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.0) | 0.57/0.14/-2.6 | 26.77 | 493 | 0.1007 | 0.88711 (10.32) | 1.0 | 0.189 | 0.9 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
