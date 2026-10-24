# gen_2610240907_000 — engine run 20261024_091156_gen_2610240907_000

Hypothesis: grammar draw seed=2610240907: rsi_revert

**0/8 pass.** Ledger N at evaluation: 2230. PBO (CSCV) across family: 0.047. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 7b2d4f4c76fc3962aa9fed19631e70f6dbdc1093fcefc182607d72ce0e90c460. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2223 | BROAD|rsi_revert(entry=5,exit=60,n=2) | 18.48/0.93/-5.6 | 5.92 | 299 | 0.0453 | 0.11089 (1.26) | 1.0 | 0.4061 | 0.391 | False | cost_stop, holm, dsr, spa |
| 2224 | BROAD|rsi_revert(entry=5,exit=60,n=3) | 6.85/0.48/-8.7 | 5.92 | 90 | 0.0437 | 0.38661 (2.1) | 1.0 | 0.155 | 0.553 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2225 | BROAD|rsi_revert(entry=5,exit=80,n=2) | 24.65/0.96/-8.7 | 5.92 | 272 | 0.0463 | 0.05095 (0.88) | 1.0 | 0.4316 | 0.3125 | False | cost_stop, holm, dsr, spa |
| 2226 | BROAD|rsi_revert(entry=5,exit=80,n=3) | 19.61/0.98/-11.45 | 5.92 | 85 | 0.0431 | 0.11888 (3.25) | 1.0 | 0.4448 | 0.3855 | False | min_trades, cost_stop, holm, dsr, spa |
| 2227 | BROAD|rsi_revert(entry=10,exit=60,n=2) | 13.35/0.52/-10.53 | 5.92 | 527 | 0.0469 | 0.15085 (-0.53) | 1.0 | 0.1741 | 0.4495 | False | cost_stop, holm, dsr, spa |
| 2228 | BROAD|rsi_revert(entry=10,exit=60,n=3) | 16.67/0.81/-10.11 | 5.92 | 203 | 0.046 | 0.13686 (1.02) | 1.0 | 0.3291 | 0.408 | False | cost_stop, holm, dsr, spa |
| 2229 | BROAD|rsi_revert(entry=10,exit=80,n=2) | 15.5/0.5/-14.4 | 5.92 | 443 | 0.0481 | 0.13786 (0.01) | 1.0 | 0.1675 | 0.41 | False | cost_stop, walk_forward, holm, dsr, spa |
| 2230 | BROAD|rsi_revert(entry=10,exit=80,n=3) | 41.08/1.36/-11.39 | 5.92 | 173 | 0.0458 | 0.002 (1.28) | 1.0 | 0.6986 | 0.1445 | False | cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
