# gen_2310232101_000 — engine run 20261023_210347_gen_2310232101_000

Hypothesis: grammar draw seed=2310232101: rsi_revert

**0/8 pass.** Ledger N at evaluation: 894. PBO (CSCV) across family: 0.167. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 f7eb3cd8a2108233c422e383ac02adf4de029b3908144f418f2f7759f761cc6c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 887 | crypto_d|rsi_revert(entry=10,exit=60,n=2) | 40.51/0.91/-18.78 | 234.6 | 391 | 0.0134 | 0.62438 (95.86) | 1.0 | 0.3512 | 0.856 | False | beats_buy_hold, holm, dsr, spa |
| 888 | crypto_d|rsi_revert(entry=10,exit=60,n=3) | 54.19/1.31/-13.67 | 234.6 | 160 | 0.013 | 0.58242 (125.49) | 1.0 | 0.5479 | 0.847 | False | beats_buy_hold, holm, dsr, spa |
| 889 | crypto_d|rsi_revert(entry=10,exit=70,n=2) | 31.3/0.72/-24.35 | 234.6 | 355 | 0.0136 | 0.64935 (68.66) | 1.0 | 0.2681 | 0.857 | False | beats_buy_hold, holm, dsr, spa |
| 890 | crypto_d|rsi_revert(entry=10,exit=70,n=3) | 65.16/1.37/-16.26 | 234.6 | 149 | 0.0131 | 0.53047 (97.99) | 1.0 | 0.5816 | 0.8365 | False | beats_buy_hold, holm, dsr, spa |
| 891 | crypto_d|rsi_revert(entry=20,exit=60,n=2) | 9.81/0.36/-25.79 | 234.6 | 640 | 0.0138 | 0.81219 (113.42) | 1.0 | 0.149 | 0.8845 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 892 | crypto_d|rsi_revert(entry=20,exit=60,n=3) | 29.9/0.66/-25.45 | 234.6 | 327 | 0.0134 | 0.66733 (101.27) | 1.0 | 0.2446 | 0.8545 | False | beats_buy_hold, holm, dsr, spa |
| 893 | crypto_d|rsi_revert(entry=20,exit=70,n=2) | 10.84/0.38/-29.74 | 234.6 | 563 | 0.0138 | 0.7992 (111.8) | 1.0 | 0.1544 | 0.884 | False | beats_buy_hold, holm, dsr, spa |
| 894 | crypto_d|rsi_revert(entry=20,exit=70,n=3) | 47.68/0.84/-24.91 | 234.6 | 290 | 0.0135 | 0.59241 (114.03) | 1.0 | 0.3232 | 0.835 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
