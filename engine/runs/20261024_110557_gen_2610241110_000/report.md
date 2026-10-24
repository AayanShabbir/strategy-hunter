# gen_2610241110_000 — engine run 20261024_110557_gen_2610241110_000

Hypothesis: grammar draw seed=2610241110: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 2442. PBO (CSCV) across family: 0.745. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 c077ab544f2012bdc31fc94b1e0cc4727430401acd75594622a106757a3fc62a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2435 | crypto|rsi_revert(entry=5,exit=60,n=2)+relvol(min_ratio=1.2) | 29.39/1.28/-6.98 | 434.62 | 124 | 0.0158 | 0.72328 (103.01) | 1.0 | 0.7834 | 0.882 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2436 | crypto|rsi_revert(entry=5,exit=60,n=5)+relvol(min_ratio=1.2) | 4.61/0.68/-1.59 | 434.62 | 7 | 0.0207 | 0.87013 (272.65) | 1.0 | 0.4637 | 0.906 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2437 | crypto|rsi_revert(entry=5,exit=70,n=2)+relvol(min_ratio=1.2) | 21.83/0.96/-7.45 | 434.62 | 138 | 0.0161 | 0.77323 (196.98) | 1.0 | 0.616 | 0.89 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2438 | crypto|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.2) | 7.55/1.01/-1.59 | 434.62 | 9 | 0.0185 | 0.93207 (231.56) | 1.0 | 0.685 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2439 | crypto|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.2) | 23.39/0.9/-8.9 | 434.62 | 206 | 0.0169 | 0.73227 (81.25) | 1.0 | 0.5828 | 0.8905 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2440 | crypto|rsi_revert(entry=10,exit=60,n=5)+relvol(min_ratio=1.2) | 6.97/0.66/-3.97 | 434.62 | 38 | 0.0162 | 0.93307 (81.9) | 1.0 | 0.4591 | 0.9025 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2441 | crypto|rsi_revert(entry=10,exit=70,n=2)+relvol(min_ratio=1.2) | 17.43/0.68/-9.71 | 434.62 | 229 | 0.017 | 0.80819 (184.98) | 1.0 | 0.4733 | 0.895 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2442 | crypto|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.2) | 10.67/0.88/-4.16 | 434.62 | 52 | 0.0165 | 0.86014 (232.35) | 1.0 | 0.5703 | 0.9015 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
