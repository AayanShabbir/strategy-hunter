# gen_2410240605_000 — engine run 20261024_060511_gen_2410240605_000

Hypothesis: grammar draw seed=2410240605: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1938. PBO (CSCV) across family: 0.062. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 144f7b8c3b7dcbd67c558026fd1879aa8601b237a97a256fd0e406e08020be81. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1931 | semis|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.0) | 0.72/0.15/-5.16 | -38.66 | 656 | 0.0753 | 0.10589 (-22.63) | 1.0 | 0.0001 | 0.29 | False | cost_stop, walk_forward, holm, dsr, spa |
| 1932 | semis|rsi_revert(entry=10,exit=60,n=5)+relvol(min_ratio=1.0) | 9.23/2.05/-1.81 | -38.66 | 281 | 0.0678 | 0.05794 (-22.43) | 1.0 | 0.0764 | 0.251 | False | cost_stop, holm, dsr, spa |
| 1933 | semis|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.0) | 0.26/0.06/-5.48 | -38.66 | 822 | 0.075 | 0.08791 (-23.52) | 1.0 | 0.0002 | 0.291 | False | cost_stop, walk_forward, holm, dsr, spa |
| 1934 | semis|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.0) | 10.61/2.01/-2.12 | -38.66 | 391 | 0.0664 | 0.05894 (-23.16) | 1.0 | 0.1087 | 0.2435 | False | cost_stop, holm, dsr, spa |
| 1935 | semis|rsi_revert(entry=20,exit=60,n=3)+relvol(min_ratio=1.0) | -0.28/-0.01/-6.2 | -38.66 | 1156 | 0.0765 | 0.08691 (-24.52) | 1.0 | 0.0003 | 0.2955 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1936 | semis|rsi_revert(entry=20,exit=60,n=5)+relvol(min_ratio=1.0) | 7.23/1.01/-3.64 | -38.66 | 904 | 0.0746 | 0.06394 (-22.89) | 1.0 | 0.0146 | 0.259 | False | cost_stop, holm, dsr, spa |
| 1937 | semis|rsi_revert(entry=20,exit=70,n=3)+relvol(min_ratio=1.0) | -1.92/-0.2/-6.74 | -38.66 | 1388 | 0.0779 | 0.09191 (-25.03) | 1.0 | 0.0002 | 0.3025 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1938 | semis|rsi_revert(entry=20,exit=70,n=5)+relvol(min_ratio=1.0) | 8.59/1.02/-4.47 | -38.66 | 1169 | 0.076 | 0.05395 (-24.92) | 1.0 | 0.0258 | 0.2515 | False | cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
