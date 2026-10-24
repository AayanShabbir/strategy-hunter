# gen_2310232014_000 — engine run 20261023_201102_gen_2310232014_000

Hypothesis: grammar draw seed=2310232014: rsi_revert

**0/8 pass.** Ledger N at evaluation: 834. PBO (CSCV) across family: 0.216. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 9366729f60984e080ebddb540f6b17649a62cc3f2cf730f979b106f9fcd3f63c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 827 | megacap_h|rsi_revert(entry=5,exit=60,n=3) | 4.3/0.5/-6.2 | 43.45 | 518 | 0.1253 | 0.85115 (15.88) | 1.0 | 0.0141 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 828 | megacap_h|rsi_revert(entry=5,exit=60,n=5) | 4.01/1.24/-1.3 | 43.45 | 46 | 0.1035 | 0.97103 (19.96) | 1.0 | 0.0527 | 0.9605 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 829 | megacap_h|rsi_revert(entry=5,exit=80,n=3) | 15.19/1.2/-7.19 | 43.45 | 470 | 0.127 | 0.5964 (16.29) | 1.0 | 0.0945 | 0.9175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 830 | megacap_h|rsi_revert(entry=5,exit=80,n=5) | 9.44/2.19/-0.74 | 43.45 | 46 | 0.1035 | 0.8951 (20.5) | 1.0 | 0.4897 | 0.9215 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 831 | megacap_h|rsi_revert(entry=20,exit=60,n=3) | 0.12/0.06/-13.54 | 43.45 | 1982 | 0.1283 | 0.47752 (6.84) | 1.0 | 0.0027 | 0.4935 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 832 | megacap_h|rsi_revert(entry=20,exit=60,n=5) | 11.14/0.72/-10.8 | 43.45 | 859 | 0.1277 | 0.60939 (14.58) | 1.0 | 0.0178 | 0.9525 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 833 | megacap_h|rsi_revert(entry=20,exit=80,n=3) | 10.89/0.5/-17.06 | 43.45 | 1417 | 0.1301 | 0.26474 (9.84) | 1.0 | 0.011 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 834 | megacap_h|rsi_revert(entry=20,exit=80,n=5) | 40.71/1.46/-13.41 | 43.45 | 574 | 0.1306 | 0.21678 (16.19) | 1.0 | 0.1389 | 0.614 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
