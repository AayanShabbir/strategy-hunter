# gen_2610240806_000 — engine run 20261024_080355_gen_2610240806_000

Hypothesis: grammar draw seed=2610240806: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2158. PBO (CSCV) across family: 0.147. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 96177cf1128a2e04083f72d1d62c5d24da80df41e28fca13e90f871da9b83253. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2151 | sectors|rsi_revert(entry=10,exit=60,n=2) | 15.83/0.8/-5.08 | 50.2 | 993 | 0.0698 | 0.71429 (19.51) | 1.0 | 0.5813 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2152 | sectors|rsi_revert(entry=10,exit=60,n=5) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0631 | 0.99401 (23.24) | 1.0 | 0.4552 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2153 | sectors|rsi_revert(entry=10,exit=80,n=2) | 24.64/1.02/-5.5 | 50.2 | 843 | 0.0711 | 0.18981 (19.78) | 1.0 | 0.7328 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2154 | sectors|rsi_revert(entry=10,exit=80,n=5) | 11.32/1.19/-2.1 | 50.2 | 77 | 0.0633 | 0.92707 (23.07) | 1.0 | 0.8271 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2155 | sectors|rsi_revert(entry=20,exit=60,n=2) | 16.85/0.73/-8.14 | 50.2 | 1652 | 0.0701 | 0.46953 (16.52) | 1.0 | 0.5152 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2156 | sectors|rsi_revert(entry=20,exit=60,n=5) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0656 | 0.44056 (21.84) | 1.0 | 0.7936 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2157 | sectors|rsi_revert(entry=20,exit=80,n=2) | 28.11/0.99/-10.59 | 50.2 | 1283 | 0.0709 | 0.04795 (18.03) | 1.0 | 0.6968 | 0.95 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2158 | sectors|rsi_revert(entry=20,exit=80,n=5) | 33.87/1.16/-10.14 | 50.2 | 251 | 0.0684 | 0.03497 (21.96) | 1.0 | 0.791 | 0.8725 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
