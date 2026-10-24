# gen_2310232101_001 — engine run 20261023_210354_gen_2310232101_001

Hypothesis: grammar draw seed=2310232101: donchian

**0/4 pass.** Ledger N at evaluation: 898. PBO (CSCV) across family: 0.625. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 54f33338cf26d41f252d9a00ab7b04053f19e5f90aea14bd83fc183d1a833862. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 895 | crypto_d|donchian(entry_n=55,exit_n=10) | 10.59/0.39/-29.59 | 234.6 | 61 | 0.0177 | 0.84615 (103.89) | 1.0 | 0.5456 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 896 | crypto_d|donchian(entry_n=55,exit_n=20) | 15.44/0.47/-32.96 | 234.6 | 50 | 0.0177 | 0.81718 (111.65) | 1.0 | 0.5852 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 897 | crypto_d|donchian(entry_n=100,exit_n=10) | 15.9/0.55/-21.16 | 234.6 | 39 | 0.0184 | 0.75924 (120.42) | 1.0 | 0.6242 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 898 | crypto_d|donchian(entry_n=100,exit_n=20) | 19.48/0.59/-23.98 | 234.6 | 32 | 0.0186 | 0.72028 (94.3) | 1.0 | 0.6411 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
