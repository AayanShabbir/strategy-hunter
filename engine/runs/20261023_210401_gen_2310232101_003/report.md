# gen_2310232101_003 — engine run 20261023_210401_gen_2310232101_003

Hypothesis: grammar draw seed=2310232101: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 910. PBO (CSCV) across family: 0.351. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 4154cd85e362fd966f3e8b7929c8b2c600eba88d3d72fee0616d09205cb26eb7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 907 | crypto_d|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.0) | 12.82/0.48/-18.2 | 234.6 | 667 | 0.0165 | 0.80919 (98.12) | 1.0 | 0.5171 | 0.8915 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 908 | crypto_d|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | 7.1/0.32/-13.84 | 234.6 | 723 | 0.0165 | 0.81618 (108.73) | 1.0 | 0.4399 | 0.894 | False | beats_buy_hold, holm, dsr, spa |
| 909 | crypto_d|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.0) | 15.11/0.55/-16.45 | 234.6 | 671 | 0.0169 | 0.75524 (95.29) | 1.0 | 0.5497 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 910 | crypto_d|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.0) | 18.52/0.66/-13.84 | 234.6 | 680 | 0.0166 | 0.73626 (60.66) | 1.0 | 0.5995 | 0.8875 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
