# gen_2410240510_000 — engine run 20261024_051216_gen_2410240510_000

Hypothesis: grammar draw seed=2410240510: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1798. PBO (CSCV) across family: 0.35. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4000880e79b07780697c596c286367ed42b385bf823d67a11f5228d6009c6701. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1791 | BROAD|rsi_revert(entry=5,exit=60,n=2) | 14.89/0.93/-3.42 | 78.13 | 293 | 0.0793 | 0.96903 (31.4) | 1.0 | 0.8925 | 0.512 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1792 | BROAD|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 78.13 | 5 | 0.0439 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1793 | BROAD|rsi_revert(entry=5,exit=80,n=2) | 20.18/1.02/-5.65 | 78.13 | 272 | 0.0801 | 0.9011 (31.45) | 1.0 | 0.8981 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1794 | BROAD|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 78.13 | 4 | 0.0491 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1795 | BROAD|rsi_revert(entry=20,exit=60,n=2) | 22.96/0.97/-7.78 | 78.13 | 898 | 0.0798 | 0.63636 (26.07) | 1.0 | 0.8588 | 0.5135 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1796 | BROAD|rsi_revert(entry=20,exit=60,n=5) | 19.95/1.1/-5.46 | 78.13 | 183 | 0.077 | 0.93506 (33.15) | 1.0 | 0.9214 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1797 | BROAD|rsi_revert(entry=20,exit=80,n=2) | 38.14/1.26/-9.33 | 78.13 | 714 | 0.0808 | 0.13387 (28.85) | 1.0 | 0.9404 | 0.5185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1798 | BROAD|rsi_revert(entry=20,exit=80,n=5) | 31.04/1.1/-11.15 | 78.13 | 126 | 0.0803 | 0.56044 (33.0) | 1.0 | 0.8905 | 0.5265 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
