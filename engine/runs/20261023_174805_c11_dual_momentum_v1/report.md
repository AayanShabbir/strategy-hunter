# c11_dual_momentum_v1 — engine run 20261023_174805_c11_dual_momentum_v1

Hypothesis: Dual momentum: hold coin while its 7-60d return beats BTC or ETH (relative) and optionally > 0 (absolute) beats buy-and-hold OOS. Long/flat spot, 25+10 bps/side, 5x ATR stop, UTC daily bars. Strategy Scout crypto batch 2 (pre-registered 2026-10-23 before results).

**0/20 pass.** Ledger N at evaluation: 615. PBO (CSCV) across family: 0.829. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 27b3ef6f3db3c9ce0db2e165c17e03af69148dffe63bf5cb155cff49116efce4. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 596 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=7) | -16.28/-0.13/-46.91 | 193.2 | 757 | 0.0189 | 0.83317 (34.46) | 1.0 | 0.0414 | 0.9255 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 597 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=14) | -12.55/-0.07/-32.22 | 193.2 | 524 | 0.0197 | 0.86214 (71.73) | 1.0 | 0.0506 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 598 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=21) | 20.28/0.45/-30.96 | 193.2 | 419 | 0.0193 | 0.62138 (61.44) | 1.0 | 0.1842 | 0.8785 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 599 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=30) | 10.2/0.3/-30.23 | 193.2 | 365 | 0.0205 | 0.6973 (56.64) | 1.0 | 0.1354 | 0.899 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 600 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=60) | 9.5/0.3/-25.89 | 193.2 | 240 | 0.0204 | 0.74625 (52.56) | 1.0 | 0.1344 | 0.8915 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 601 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=7) | -32.21/-0.71/-46.54 | 193.2 | 613 | 0.0183 | 0.97502 (45.12) | 1.0 | 0.0048 | 0.9325 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 602 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=14) | -12.07/-0.15/-30.96 | 193.2 | 430 | 0.0186 | 0.90909 (73.31) | 1.0 | 0.0404 | 0.9055 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 603 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=21) | -2.7/0.06/-28.35 | 193.2 | 356 | 0.0189 | 0.83616 (64.49) | 1.0 | 0.0725 | 0.8965 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 604 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=30) | -7.13/-0.01/-39.19 | 193.2 | 284 | 0.0193 | 0.85814 (57.49) | 1.0 | 0.06 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 605 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=60) | 22.86/0.51/-29.16 | 193.2 | 185 | 0.0191 | 0.61738 (67.32) | 1.0 | 0.2104 | 0.884 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 606 | ALTS|rel_strength(abs_filter=False,bench=BTC/USD,n=7) | -25.33/-0.26/-53.75 | 193.2 | 805 | 0.0186 | 0.9041 (38.64) | 1.0 | 0.027 | 0.937 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 607 | ALTS|rel_strength(abs_filter=False,bench=BTC/USD,n=14) | -9.62/0.01/-32.83 | 193.2 | 545 | 0.0195 | 0.81618 (49.15) | 1.0 | 0.0624 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 608 | ALTS|rel_strength(abs_filter=False,bench=BTC/USD,n=21) | 13.94/0.36/-37.1 | 193.2 | 448 | 0.0194 | 0.69031 (65.02) | 1.0 | 0.1515 | 0.8875 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 609 | ALTS|rel_strength(abs_filter=False,bench=BTC/USD,n=30) | 30.85/0.57/-26.56 | 193.2 | 373 | 0.02 | 0.59241 (62.32) | 1.0 | 0.2351 | 0.8775 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 610 | ALTS|rel_strength(abs_filter=False,bench=BTC/USD,n=60) | 16.05/0.38/-26.57 | 193.2 | 242 | 0.0196 | 0.70929 (73.78) | 1.0 | 0.1636 | 0.8865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 611 | ALTS|rel_strength(abs_filter=False,bench=ETH/USD,n=7) | 6.25/0.25/-31.63 | 193.2 | 691 | 0.0174 | 0.60939 (44.25) | 1.0 | 0.118 | 0.8905 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 612 | ALTS|rel_strength(abs_filter=False,bench=ETH/USD,n=14) | 13.95/0.36/-33.62 | 193.2 | 471 | 0.0176 | 0.64036 (60.24) | 1.0 | 0.1517 | 0.887 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 613 | ALTS|rel_strength(abs_filter=False,bench=ETH/USD,n=21) | 33.09/0.61/-30.48 | 193.2 | 366 | 0.0182 | 0.53147 (52.27) | 1.0 | 0.2514 | 0.8675 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 614 | ALTS|rel_strength(abs_filter=False,bench=ETH/USD,n=30) | 6.12/0.25/-44.29 | 193.2 | 283 | 0.0184 | 0.72927 (53.32) | 1.0 | 0.1189 | 0.898 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 615 | ALTS|rel_strength(abs_filter=False,bench=ETH/USD,n=60) | 42.12/0.67/-39.19 | 193.2 | 210 | 0.018 | 0.55744 (94.86) | 1.0 | 0.2846 | 0.865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
