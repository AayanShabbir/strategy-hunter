# gen_2410240609_000 — engine run 20261024_060528_gen_2410240609_000

Hypothesis: grammar draw seed=2410240609: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1966. PBO (CSCV) across family: 0.731. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 31729bacc0638b40c1b7104cc79c9be3f4e1969b5178334f0e2b0daad1e2e079. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1959 | crypto_d|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.0) | 34.82/1.13/-13.71 | 234.6 | 394 | 0.014 | 0.64036 (126.72) | 1.0 | 0.7302 | 0.867 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1960 | crypto_d|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.0) | 14.76/0.69/-10.06 | 234.6 | 211 | 0.0133 | 0.78721 (79.64) | 1.0 | 0.5201 | 0.8805 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1961 | crypto_d|rsi_revert(entry=10,exit=80,n=2)+relvol(min_ratio=1.0) | 36.45/1.08/-15.52 | 234.6 | 511 | 0.014 | 0.64236 (108.49) | 1.0 | 0.7055 | 0.8655 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1962 | crypto_d|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.0) | 24.09/0.95/-10.28 | 234.6 | 353 | 0.0132 | 0.68531 (69.3) | 1.0 | 0.6483 | 0.879 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1963 | crypto_d|rsi_revert(entry=20,exit=60,n=2)+relvol(min_ratio=1.0) | 24.33/0.8/-15.06 | 234.6 | 571 | 0.014 | 0.69431 (78.29) | 1.0 | 0.5752 | 0.8745 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1964 | crypto_d|rsi_revert(entry=20,exit=60,n=3)+relvol(min_ratio=1.0) | 37.72/1.14/-14.67 | 234.6 | 459 | 0.0139 | 0.5994 (79.8) | 1.0 | 0.7335 | 0.8615 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1965 | crypto_d|rsi_revert(entry=20,exit=80,n=2)+relvol(min_ratio=1.0) | 36.69/1.03/-15.52 | 234.6 | 692 | 0.0142 | 0.62138 (105.58) | 1.0 | 0.6814 | 0.868 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1966 | crypto_d|rsi_revert(entry=20,exit=80,n=3)+relvol(min_ratio=1.0) | 46.73/1.26/-14.67 | 234.6 | 647 | 0.014 | 0.56044 (71.77) | 1.0 | 0.7783 | 0.8595 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
