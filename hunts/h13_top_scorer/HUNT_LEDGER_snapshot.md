# Strategy Hunt Ledger (offline replays, Alpaca paper desk)

Updated 2026-10-15T20:12 ET. N (all tested incl. 35 prior in REPORT/AFTERNOON/SCOUT) = **146**. Bonferroni bar: twin p <= 0.05/N = 0.00034. Verified also needs OOS>0, >=30 OOS trades, both OOS halves (walk-forward A/B, % of $10k) >0, AND in-sample (untuned, oldest 70%) >0.

Engine: 15m IEX bars, top-50 liquid (bond/leveraged/crypto ETFs excluded), 4 bps/side, next-bar entry, gap stops at open, same-bar stop first, flat 15:45 bar open, 1% risk, cash-only, max 4/day, SPY regime block. IS = oldest 70% days, OOS = newest 30%. Twins: 500, extended to 4000 if real beats all 500. p/pct only computed when OOS>0 and >=30 trades.

| # | Name | Family | Rule/params | IS ret | OOS trades | OOS ret | PF | WF A | WF B | twins | pct | p | z | Verified (at current N) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 36 | orb15_rv1 | ORB-SIP | {'nb': '1', 'rvmin': '1.0'} | 66.24% | 1205 | 12.39% | 1.08 | 3.21% | 9.18% | 500 | 97.4 | 0.02794 | 1.89 | no |
| 37 | rsi2_200 | RSI(2) pullback | {} | 0.16% | 777 | 4.46% | 1.03 | 2.42% | 2.04% | 500 | 69.8 | 0.30339 | 0.49 | no |
| 38 | rsi2_200_stk | RSI(2) pullback | {'uni': 'stk'} | 13.42% | 659 | 5.33% | 1.04 | 1.66% | 3.66% | 500 | 70.2 | 0.2994 | 0.51 | no |
| 39 | rsi2_200_th5 | RSI(2) pullback | {'th': '5'} | -1.92% | 429 | -10.7% | 0.88 | -7.12% | -3.58% | 0 | 0.0 | 1.0 | None | no |
| 40 | intra_mom_L20 | Intraday-momentum-XS | {} | 19.29% | 1459 | -36.59% | 0.86 | 6.28% | -42.88% | 0 | 0.0 | 1.0 | None | no |
| 41 | intra_mom_L60 | Intraday-momentum-XS | {'L': '60'} | 33.9% | 1516 | 1.3% | 1.0 | -3.16% | 4.46% | 500 | 68.8 | 0.31337 | 0.48 | no |
| 42 | prev_loser | ST-reversal | {} | 10.05% | 382 | 10.45% | 1.16 | 3.32% | 7.14% | 500 | 77.8 | 0.22355 | 0.77 | no |
| 43 | gapdown_rev | Gap-down reversal | {} | -11.79% | 128 | -0.55% | 0.98 | -0.2% | -0.35% | 0 | 0.0 | 1.0 | None | no |
| 44 | gapdown_rev_g05 | Gap-down reversal | {'gk': '0.5'} | -13.47% | 413 | -9.08% | 0.89 | -1.8% | -7.28% | 0 | 0.0 | 1.0 | None | no |
| 45 | tom_etf | Turn-of-month | {'uni': 'etf'} | -9.17% | 328 | 11.68% | 1.54 | 3.42% | 8.26% | 500 | 78.2 | 0.21956 | 0.82 | no |
| 46 | orb15_rv1_etf | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'uni': 'etf'} | 5.24% | 626 | -26.41% | 0.65 | -12.61% | -13.79% | 0 | 0.0 | 1.0 | None | no |
| 47 | orb15_rv1_stk | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'uni': 'stk'} | 59.97% | 1019 | 14.49% | 1.09 | 2.23% | 12.26% | 500 | 97.0 | 0.03194 | 1.93 | no |
| 48 | spy_noise | SPY noise-area momentum | {} | 17.95% | 215 | -3.48% | 0.86 | -0.89% | -2.6% | 0 | 0.0 | 1.0 | None | no |
| 49 | spy_noise_m15 | SPY noise-area momentum | {'mult': '1.5'} | 11.94% | 124 | 0.25% | 1.02 | 1.01% | -0.76% | 500 | 76.2 | 0.23952 | 0.68 | no |
| 50 | spy_noise_15min | SPY noise-area momentum | {'every': '15'} | 5.4% | 268 | -6.85% | 0.76 | -4.21% | -2.64% | 0 | 0.0 | 1.0 | None | no |
| 51 | spy_noise_noVWAP | SPY noise-area momentum | {'vwap_exit': 'False'} | 16.4% | 213 | -3.24% | 0.87 | -0.71% | -2.53% | 0 | 0.0 | 1.0 | None | no |
| 52 | nr7_orb15 | NR7/inside-day ORB | {} | 14.33% | 684 | 15.33% | 1.15 | 3.99% | 11.34% | 500 | 98.6 | 0.01597 | 1.95 | no |
| 53 | inside_orb15 | NR7/inside-day ORB | {'inside': 'True'} | 41.42% | 567 | 3.18% | 1.03 | 1.63% | 1.55% | 500 | 91.4 | 0.08782 | 1.27 | no |
| 54 | crabel_stretch | Crabel stretch breakout | {} | 59.56% | 1824 | 30.07% | 1.1 | 19.38% | 10.7% | 500 | 90.4 | 0.0978 | 1.35 | no |
| 55 | hi52_orb15 | 52wk-high ORB | {} | -1.38% | 447 | -16.24% | 0.75 | 4.24% | -20.48% | 0 | 0.0 | 1.0 | None | no |
| 56 | open_drive | Opening drive (first 30m momentum) | {} | 7.58% | 584 | -18.97% | 0.88 | -19.52% | 0.55% | 0 | 0.0 | 1.0 | None | no |
| 57 | orb15_rv1_sa005 | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'sa': '0.05'} | 128.56% | 1204 | 40.06% | 1.42 | 20.06% | 20.0% | 500 | 99.8 | 0.00399 | 3.55 | no |
| 58 | orb15_rv1_sa015 | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'sa': '0.15'} | 30.94% | 1212 | -15.23% | 0.92 | -12.02% | -3.21% | 0 | 0.0 | 1.0 | None | no |
| 59 | prev_loser_m075 | ST-reversal | {'m': '0.75'} | 2.35% | 610 | 6.85% | 1.06 | 6.07% | 0.78% | 500 | 69.6 | 0.30539 | 0.55 | no |
| 60 | prev_loser_m15 | ST-reversal | {'m': '1.5'} | -9.95% | 140 | 5.96% | 1.23 | 2.07% | 3.89% | 500 | 79.4 | 0.20758 | 0.82 | no |
| 61 | prev_loser_sl05 | ST-reversal | {'sl': '0.5'} | 4.41% | 371 | 12.15% | 1.13 | 7.83% | 4.33% | 500 | 80.4 | 0.1976 | 0.87 | no |
| 62 | prev_loser_stk | ST-reversal | {'uni': 'stk'} | 5.31% | 310 | 15.2% | 1.27 | 7.84% | 7.36% | 500 | 92.4 | 0.07784 | 1.39 | no |
| 63 | loser5d | ST-reversal (weekly) | {} | -1.47% | 455 | -0.57% | 0.99 | 7.56% | -8.13% | 0 | 0.0 | 1.0 | None | no |
| 64 | loser_confirm | ST-reversal | {} | -10.49% | 205 | 2.3% | 1.05 | 4.19% | -1.9% | 500 | 68.4 | 0.31737 | 0.44 | no |
| 65 | tom_all | Turn-of-month | {} | 4.72% | 352 | 18.82% | 1.58 | 3.24% | 15.59% | 500 | 91.2 | 0.08982 | 1.31 | no |
| 66 | tom_stk | Turn-of-month | {'uni': 'stk'} | 8.62% | 356 | 31.63% | 1.71 | 9.98% | 21.66% | 500 | 99.4 | 0.00798 | 2.56 | no |
| 67 | tom_etf_sl05 | Turn-of-month | {'uni': 'etf', 'sl': '0.5'} | -0.47% | 283 | 14.81% | 1.63 | 4.42% | 10.4% | 500 | 87.8 | 0.12375 | 1.07 | no |
| 68 | PESS_orb15_rv1_sa005 | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'sa': '0.05'} | -228.02% | 1204 | -147.32% | 0.16 | -67.7% | -79.62% | 0 | 0.0 | 1.0 | None | no |
| 69 | PESS_orb15_rv1 | ORB-SIP | {'nb': '1', 'rvmin': '1.0'} | -201.62% | 1205 | -146.89% | 0.29 | -63.91% | -82.98% | 0 | 0.0 | 1.0 | None | no |
| 70 | PESS_orb15_rv1_stk | ORB-SIP | {'nb': '1', 'rvmin': '1.0', 'uni': 'stk'} | -214.48% | 1019 | -159.85% | 0.27 | -66.95% | -92.91% | 0 | 0.0 | 1.0 | None | no |
| 71 | PESS_crabel_stretch | Crabel stretch breakout | {} | 57.54% | 1824 | 21.8% | 1.07 | 12.49% | 9.31% | 500 | 87.2 | 0.12974 | 1.03 | no |
| 72 | PESS_nr7_orb15 | NR7/inside-day ORB | {} | -123.86% | 684 | -68.4% | 0.46 | -19.47% | -48.93% | 0 | 0.0 | 1.0 | None | no |
| 73 | PESS_prev_loser | ST-reversal | {} | 10.05% | 382 | 10.45% | 1.16 | 3.32% | 7.14% | 500 | 79.0 | 0.21158 | 0.82 | no |
| 74 | PESS_tom_etf | Turn-of-month | {'uni': 'etf'} | -9.17% | 328 | 11.68% | 1.54 | 3.42% | 8.26% | 500 | 79.4 | 0.20758 | 0.83 | no |
| 75 | tomw_stk_1_2 | Turn-of-month | {'uni': 'stk', 'before': '1', 'after': '2'} | -30.78% | 264 | 22.7% | 1.51 | 12.05% | 10.65% | 4000 | 100.0 | 0.00025 | 4.42 | no |
| 76 | tomw_stk_2_4 | Turn-of-month | {'uni': 'stk', 'before': '2', 'after': '4'} | -81.82% | 536 | 22.43% | 1.22 | 0.76% | 21.67% | 4000 | 99.92 | 0.001 | 3.17 | no |
| 77 | tomw_stk_0_3 | Turn-of-month | {'uni': 'stk', 'before': '0', 'after': '3'} | -41.98% | 268 | 42.72% | 2.09 | 20.54% | 22.18% | 4000 | 100.0 | 0.00025 | 7.89 | no |
| 78 | tomw_stk_1_3_sl05 | Turn-of-month | {'uni': 'stk', 'sl': '0.5'} | -65.69% | 356 | 71.6% | 1.76 | 34.74% | 36.86% | 4000 | 100.0 | 0.00025 | 7.64 | no |
| 79 | prev_loser_stk_m075 | ST-reversal | {'uni': 'stk', 'm': '0.75'} | -4.68% | 507 | 6.63% | 1.07 | 8.33% | -1.7% | 500 | 75.0 | 0.2515 | 0.7 | no |
| 80 | prev_loser_stk_m15 | ST-reversal | {'uni': 'stk', 'm': '1.5'} | -6.01% | 106 | 1.76% | 1.08 | 1.42% | 0.34% | 500 | 68.4 | 0.31737 | 0.45 | no |
| 81 | prev_loser_stk_sl05 | ST-reversal | {'uni': 'stk', 'sl': '0.5'} | -4.55% | 302 | 14.25% | 1.17 | 9.68% | 4.58% | 500 | 87.8 | 0.12375 | 1.16 | no |
| 82 | hvol_up | High-volume return premium | {} | -64.54% | 366 | 1.16% | 1.01 | -5.98% | 7.15% | 500 | 61.8 | 0.38323 | 0.29 | no |
| 83 | hvol_up_stk | High-volume return premium | {'uni': 'stk'} | -43.78% | 314 | -4.71% | 0.95 | -6.24% | 1.53% | 0 | 0.0 | 1.0 | None | no |
| 84 | loser_hivol | ST-reversal x vol regime | {} | 0.85% | 179 | 2.88% | 1.1 | 1.16% | 1.72% | 500 | 64.4 | 0.35729 | 0.35 | no |
| 85 | loser_hivol_stk | ST-reversal x vol regime | {'uni': 'stk'} | -0.88% | 150 | 3.33% | 1.12 | 2.65% | 0.68% | 500 | 71.2 | 0.28942 | 0.57 | no |
| 86 | crabel_stretch_k05 | Crabel stretch breakout | {'k': '0.5'} | 83.92% | 1833 | 38.96% | 1.13 | 12.54% | 26.42% | 500 | 95.0 | 0.0519 | 1.6 | no |
| 87 | crabel_stretch_k15 | Crabel stretch breakout | {'k': '1.5'} | 29.97% | 1811 | 30.47% | 1.1 | 26.25% | 4.22% | 500 | 89.0 | 0.11178 | 1.3 | no |
| 88 | crabel_stretch_etf | Crabel stretch breakout | {'uni': 'etf'} | 8.34% | 1607 | -28.52% | 0.86 | -1.97% | -26.56% | 0 | 0.0 | 1.0 | None | no |
| 89 | crabel_stretch_k05_sl025 | Crabel stretch breakout | {'k': '0.5', 'sl': '0.25'} | 49.08% | 1783 | 33.39% | 1.12 | 11.13% | 22.26% | 500 | 95.8 | 0.04391 | 1.66 | no |
| 90 | crabel_stretch_n20 | Crabel stretch breakout | {'n': '20'} | 57.53% | 1839 | 53.98% | 1.16 | 30.58% | 23.4% | 500 | 97.4 | 0.02794 | 2.17 | no |
| 91 | crabel_stretch_200 | Stretch/reversal + 200MA filter | {} | 33.2% | 1782 | 26.39% | 1.09 | 24.49% | 1.9% | 500 | 90.4 | 0.0978 | 1.24 | no |
| 92 | prev_loser_200 | Stretch/reversal + 200MA filter | {} | 19.1% | 287 | 23.2% | 1.52 | 8.36% | 14.84% | 500 | 95.4 | 0.0479 | 1.77 | no |
| 93 | prev_loser_200_stk | Stretch/reversal + 200MA filter | {'uni': 'stk'} | 15.78% | 217 | 22.57% | 1.65 | 9.92% | 12.64% | 500 | 99.8 | 0.00399 | 2.64 | no |
| 94 | nr4_orb15 | NR7/inside-day ORB | {'n': '4'} | 45.36% | 992 | -4.93% | 0.96 | -2.45% | -2.48% | 0 | 0.0 | 1.0 | None | no |
| 95 | oir_on | Overnight-intraday reversal | {} | -50.33% | 773 | -6.18% | 0.95 | -3.76% | -2.43% | 0 | 0.0 | 1.0 | None | no |
| 96 | oir_on_stk | Overnight-intraday reversal | {'uni': 'stk'} | -46.17% | 627 | -9.47% | 0.92 | -0.29% | -9.18% | 0 | 0.0 | 1.0 | None | no |
| 97 | oir_day | Overnight-intraday reversal | {'mode': 'day'} | -37.65% | 1358 | -26.09% | 0.89 | -21.57% | -4.52% | 0 | 0.0 | 1.0 | None | no |
| 98 | oir_day_stk | Overnight-intraday reversal | {'mode': 'day', 'uni': 'stk'} | -35.83% | 1236 | -9.6% | 0.96 | -18.17% | 8.57% | 0 | 0.0 | 1.0 | None | no |
| 99 | crabel_stretch_sl1 | Crabel stretch breakout | {'sl': '1.0'} | 30.15% | 1855 | 21.65% | 1.08 | 13.96% | 7.69% | 500 | 89.6 | 0.10579 | 1.15 | no |
| 100 | crabel_stretch_sl025 | Crabel stretch breakout | {'sl': '0.25'} | 39.8% | 1762 | 36.28% | 1.13 | 16.61% | 19.67% | 500 | 97.0 | 0.03194 | 1.89 | no |
| 101 | crabel_stretch_stk | Crabel stretch breakout | {'uni': 'stk'} | 47.03% | 1822 | 32.87% | 1.1 | 25.37% | 7.5% | 500 | 93.6 | 0.06587 | 1.53 | no |
| 102 | etf_rs30 | Sector-ETF relative strength | {} | -29.72% | 1207 | -29.16% | 0.83 | -12.01% | -17.15% | 0 | 0.0 | 1.0 | None | no |
| 103 | etf_rs60 | Sector-ETF relative strength | {'nb': '4'} | -4.64% | 1204 | -11.62% | 0.92 | 0.72% | -12.34% | 0 | 0.0 | 1.0 | None | no |
| 104 | ibs20 | IBS mean reversion | {} | -3.97% | 1491 | -22.61% | 0.91 | -17.91% | -4.7% | 0 | 0.0 | 1.0 | None | no |
| 105 | ibs20_etf | IBS mean reversion | {'uni': 'etf'} | -10.06% | 762 | 0.75% | 1.01 | 11.89% | -11.14% | 500 | 61.8 | 0.38323 | 0.28 | no |
| 106 | ibs10 | IBS mean reversion | {'th': '0.1'} | -4.84% | 1115 | -32.2% | 0.84 | -22.67% | -9.53% | 0 | 0.0 | 1.0 | None | no |
| 107 | down3_200 | Down-streak above 200MA | {} | -7.57% | 817 | -8.37% | 0.94 | -2.81% | -5.56% | 0 | 0.0 | 1.0 | None | no |
| 108 | down3_200_stk | Down-streak above 200MA | {'uni': 'stk'} | 10.51% | 717 | -16.71% | 0.88 | -9.23% | -7.48% | 0 | 0.0 | 1.0 | None | no |
| 109 | preholiday | Pre-holiday | {} | -0.49% | 68 | -1.48% | 0.84 | -0.82% | -0.66% | 0 | 0.0 | 1.0 | None | no |
| 110 | xsmom_12_1 | XS momentum 12-1 (intraday hold) | {'uni': 'stk'} | -49.35% | 1844 | -4.4% | 0.99 | -3.5% | -0.9% | 0 | 0.0 | 1.0 | None | no |
| 111 | xsmom_6_1 | XS momentum 12-1 (intraday hold) | {'uni': 'stk', 'L': '126'} | -67.36% | 1825 | 22.22% | 1.06 | 10.94% | 11.28% | 500 | 97.0 | 0.03194 | 1.77 | no |
| 112 | ind_mom_etf21 | Industry/sector-ETF momentum (daily) | {'uni': 'etf', 'L': '21', 'skip': '0'} | -31.25% | 1558 | -30.76% | 0.85 | -15.59% | -15.18% | 0 | 0.0 | 1.0 | None | no |
| 113 | ind_mom_etf63 | Industry/sector-ETF momentum (daily) | {'uni': 'etf', 'L': '63', 'skip': '0'} | -76.19% | 1727 | -25.55% | 0.89 | -9.83% | -15.73% | 0 | 0.0 | 1.0 | None | no |
| 114 | mrev21_200 | 1-month reversal above 200MA | {'uni': 'stk'} | -9.18% | 722 | -4.9% | 0.96 | -5.99% | 1.09% | 0 | 0.0 | 1.0 | None | no |
| 115 | mrev21_noma | 1-month reversal above 200MA | {'uni': 'stk', 'ma': '0', 'm': '-0.12'} | -39.28% | 836 | -2.85% | 0.98 | 7.06% | -9.91% | 0 | 0.0 | 1.0 | None | no |
| 116 | vcp_open | Volatility contraction | {'uni': 'stk'} | -2.4% | 19 | -4.29% | 0.17 | -0.59% | -3.7% | 0 | 0.0 | 1.0 | None | no |
| 117 | vcp_bo | Volatility contraction | {'uni': 'stk', 'mode': 'bo'} | -2.49% | 11 | -4.38% | 0.06 | -0.3% | -4.08% | 0 | 0.0 | 1.0 | None | no |
| 118 | vcp_open_r07 | Volatility contraction | {'ratio': '0.7'} | -14.14% | 220 | -10.61% | 0.71 | -2.67% | -7.94% | 0 | 0.0 | 1.0 | None | no |
| 119 | gapgo_1atr | Gap-up continuation (news/earnings proxy) | {'uni': 'stk'} | 0.15% | 108 | -8.19% | 0.75 | -4.58% | -3.6% | 0 | 0.0 | 1.0 | None | no |
| 120 | gapgo_15atr | Gap-up continuation (news/earnings proxy) | {'uni': 'stk', 'gk': '1.5'} | 3.69% | 33 | 5.89% | 2.05 | 1.93% | 3.97% | 500 | 93.4 | 0.06786 | 1.5 | no |
| 121 | gapgo_05atr_all | Gap-up continuation (news/earnings proxy) | {'gk': '0.5'} | 9.42% | 521 | -45.93% | 0.64 | -17.24% | -28.69% | 0 | 0.0 | 1.0 | None | no |
| 122 | pairlag_12 | Stock-vs-sector-ETF lag (intraday pairs, long leg) | {} | 7.61% | 528 | -16.18% | 0.76 | -14.7% | -1.47% | 0 | 0.0 | 1.0 | None | no |
| 123 | pairlag_1030 | Stock-vs-sector-ETF lag (intraday pairs, long leg) | {'at': '10:30:00'} | 7.23% | 468 | -7.01% | 0.91 | -5.16% | -1.85% | 0 | 0.0 | 1.0 | None | no |
| 124 | pairlag_12_k1 | Stock-vs-sector-ETF lag (intraday pairs, long leg) | {'k': '1.0'} | 0.45% | 140 | -5.95% | 0.75 | -8.38% | 2.43% | 0 | 0.0 | 1.0 | None | no |
| 125 | fomc_etf_1400 | Pre-FOMC drift | {'uni': 'etf'} | 1.85% | 60 | -0.92% | 0.82 | -0.35% | -0.57% | 0 | 0.0 | 1.0 | None | no |
| 126 | fomc_stk_1400 | Pre-FOMC drift | {'uni': 'stk'} | 13.98% | 60 | 10.41% | 2.96 | 7.71% | 2.69% | 4000 | 100.0 | 0.00025 | 5.3 | **YES** |
| 127 | fomc_etf_close | Pre-FOMC drift | {'uni': 'etf', 'exit_t': 'None'} | 13.92% | 60 | -6.85% | 0.46 | -3.24% | -3.62% | 0 | 0.0 | 1.0 | None | no |
| 128 | fomc_eve_etf | Pre-FOMC drift | {'uni': 'etf', 'eve': 'True'} | -2.01% | 48 | -0.5% | 0.72 | -0.47% | -0.03% | 0 | 0.0 | 1.0 | None | no |
| 129 | spydn1_etf | Index-level daily reversal | {'uni': 'etf'} | -20.99% | 204 | 28.4% | 2.07 | 21.62% | 6.78% | 500 | 99.8 | 0.00399 | 3.25 | no |
| 130 | spydn1_stk | Index-level daily reversal | {'uni': 'stk'} | -30.2% | 204 | 16.59% | 1.47 | 15.23% | 1.36% | 4000 | 99.98 | 0.0005 | 4.28 | no |
| 131 | spydn15_all | Index-level daily reversal | {'m': '-0.015'} | -14.86% | 112 | 12.0% | 1.65 | 8.87% | 3.13% | 4000 | 100.0 | 0.00025 | 4.21 | no |
| 132 | dow_mon_stk | Day-of-week | {'uni': 'stk', 'wd': '0'} | 4.55% | 352 | 5.23% | 1.08 | 2.08% | 3.15% | 500 | 86.2 | 0.13972 | 1.11 | no |
| 133 | dow_fri_stk | Day-of-week | {'uni': 'stk', 'wd': '4'} | -18.7% | 368 | 6.13% | 1.08 | 8.58% | -2.45% | 500 | 85.2 | 0.1497 | 1.08 | no |
| 134 | fomc_stk_1330 | Pre-FOMC drift | {'uni': 'stk', 'exit_t': '13:30:00'} | 13.62% | 60 | 9.72% | 2.85 | 7.32% | 2.4% | 4000 | 99.92 | 0.001 | 5.27 | no |
| 135 | fomc_stk_1500 | Pre-FOMC drift | {'uni': 'stk', 'exit_t': '15:00:00'} | 30.4% | 60 | 11.07% | 2.66 | 7.04% | 4.03% | 4000 | 99.98 | 0.0005 | 4.84 | no |
| 136 | fomc_stk_1400_sl05 | Pre-FOMC drift | {'uni': 'stk', 'sl': '0.5'} | 16.13% | 60 | 15.58% | 2.45 | 9.8% | 5.78% | 4000 | 99.92 | 0.001 | 4.79 | no |
| 137 | fomc_stk_1400_sl15 | Pre-FOMC drift | {'uni': 'stk', 'sl': '1.5'} | 9.82% | 60 | 7.64% | 3.48 | 5.04% | 2.59% | 4000 | 100.0 | 0.00025 | 5.73 | **YES** |
| 138 | fomc_all_1400 | Pre-FOMC drift | {} | 14.52% | 60 | 10.14% | 2.95 | 7.71% | 2.43% | 500 | 99.8 | 0.00399 | 4.83 | no |
| 139 | fomc_eve_stk | Pre-FOMC drift | {'uni': 'stk', 'eve': 'True'} | -1.87% | 48 | -0.4% | 0.83 | -0.09% | -0.3% | 0 | 0.0 | 1.0 | None | no |
| 140 | day2_gap2_v3 | Post-news-gap day-2 drift | {} | 6.41% | 15 | 5.48% | 2.47 | 2.69% | 2.79% | 0 | 0.0 | 1.0 | None | no |
| 141 | day2_gap1_v2_stk | Post-news-gap day-2 drift | {'uni': 'stk', 'gk': '1.0', 'vk': '2.0'} | 2.46% | 67 | 15.31% | 2.05 | 11.33% | 3.98% | 500 | 99.4 | 0.00798 | 2.64 | no |
| 142 | hi52_open_stk | 52wk-high proximity (open entry) | {'uni': 'stk'} | -39.36% | 979 | -40.26% | 0.79 | -6.77% | -33.48% | 0 | 0.0 | 1.0 | None | no |
| 143 | hi52_open_etf | 52wk-high proximity (open entry) | {'uni': 'etf'} | -39.91% | 871 | -25.53% | 0.76 | -11.68% | -13.85% | 0 | 0.0 | 1.0 | None | no |
| 144 | day2_gap15_v2_stk | Post-news-gap day-2 drift | {'uni': 'stk', 'gk': '1.5', 'vk': '2.0'} | 10.54% | 39 | 8.19% | 1.8 | 5.69% | 2.5% | 500 | 97.6 | 0.02595 | 2.06 | no |
| 145 | day2_gap1_v2_stk_sl05 | Post-news-gap day-2 drift | {'uni': 'stk', 'gk': '1.0', 'vk': '2.0', 'sl': '0.5'} | -4.74% | 66 | 14.69% | 1.5 | 9.74% | 4.95% | 500 | 97.0 | 0.03194 | 1.9 | no |
| 146 | day2_gap1_v15_all | Post-news-gap day-2 drift | {'gk': '1.0', 'vk': '1.5'} | -3.85% | 126 | 16.74% | 1.62 | 14.19% | 2.55% | 500 | 96.8 | 0.03393 | 2.03 | no |

## Families / sources

- **ORB-SIP**: Long buy-stop above opening-range high when OR candle green, RVOL>=threshold, top-4 by RVOL; stop entry - sa*ATR14d; hold to 15:45. Source: Zarattini, Barbon & Aziz (2024), 'A Profitable Day Trading Strategy For The U.S. Equity Market', SSRN 4729284
- **RSI(2) pullback**: Daily close > 200d SMA and RSI(2) < 10 -> buy next open, 1 ATR stop, exit 15:45; top 4 by lowest RSI. Source: Connors & Alvarez (2008), 'Short Term Trading Strategies That Work' (TradingMarkets): RSI(2) pullback above 200-day MA
- **Intraday-momentum-XS**: At 9:30 open buy stocks whose past-L-day open->close returns have t-stat >= minz (top 4 by t); stop 1 ATR; exit 15:45. Source: Lou, Polk & Skouras (2019), 'A Tug of War: Overnight Versus Intraday Expected Returns', JFE 134(1)
- **ST-reversal**: Prior day down >= 1 ATR and no gap up -> buy open, stop 1 ATR, exit 15:45; top 4 by drop. Source: Lehmann (1990) QJE 105(1) & Jegadeesh (1990) JF 45(3), short-term reversal
- **Gap-down reversal**: Gap down >= 1 ATR, first 30m closes above open -> buy 10:00, stop 30m low - 0.05ATR, target prior close, else 15:45. Source: Gap-down overreaction / opening reversal; e.g. Grant, Wolf & Yu (2005) J. Futures Markets 25(10) 'Intraday price reversals in the US stock index futures market'
- **Turn-of-month**: Last + first 3 trading days of month: buy ETFs at open, 1 ATR stop, exit 15:45. Source: Ariel (1987) JFE 18(1) 'A monthly effect in stock returns'; Lakonishok & Smidt (1988) RFS 1(4)
- **SPY noise-area momentum**: SPY 1m: sigma_t = 14d mean |close_t/open-1|; UB = max(open, prev close)*(1+mult*sigma_t); at each :00/:30 from 10:00 buy next-minute open if close>UB (<=15:00); exit next open when close < max(UB, VWAP); flat 15:49; 98% cash; 1.5 bps/side. Source: Zarattini, Aziz & Barbon (2024), 'Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)', SSRN 4824172
- **NR7/inside-day ORB**: Prior day is NR7 (or inside day); green 15m OR -> buy-stop OR high+0.01 until 11:00, stop 0.10 ATR, hold to 15:45. Source: Crabel (1990), 'Day Trading with Short Term Price Patterns and Opening Range Breakout' (Traders Press): NR7/inside-day + opening-range stretch breakouts
- **Crabel stretch breakout**: Buy-stop at open + 10d avg 'stretch' (mean of min(H-O, O-L)) before 11:00; stop 0.5 ATR; hold to 15:45; top 4 by smallest stretch. Source: Crabel (1990), 'Day Trading with Short Term Price Patterns and Opening Range Breakout' (Traders Press): NR7/inside-day + opening-range stretch breakouts
- **52wk-high ORB**: Within 3% of 252d high + green 15m OR + RVOL>=1 -> ORB buy-stop, 0.10 ATR stop. Source: George & Hwang (2004), 'The 52-Week High and Momentum Investing', JF 59(5)
- **Opening drive (first 30m momentum)**: Prev close->10:00 >= 0.5 ATR, above VWAP, 30m RVOL>=1.5 -> buy 10:00, stop 0.5 ATR, hold to 15:45. Source: Gao, Han, Li & Zhou (2018), 'Market Intraday Momentum', JFE 129(2) (first-30-min return predicts later intraday returns)
- **ST-reversal (weekly)**: 5-day drop >= 2 ATR, no gap up -> buy open, stop 1 ATR, exit 15:45. Source: Lehmann (1990) QJE 105(1) & Jegadeesh (1990) JF 45(3), short-term reversal
- **High-volume return premium**: Prior day up with volume >= 2x 20d avg -> buy open, 1 ATR stop, exit 15:45. Source: Gervais, Kaniel & Mingelgrin (2001), 'The High-Volume Return Premium', JF 56(3)
- **ST-reversal x vol regime**: prev_loser rule only when SPY 20d realized vol > its 1y median. Source: Nagel (2012), 'Evaporating Liquidity', RFS 25(7): short-term reversal profits are higher when VIX/market volatility is high
- **Stretch/reversal + 200MA filter**: Base rule only when prior close > 200d SMA. Source: Connors & Alvarez (2008), 'Short Term Trading Strategies That Work': only buy pullbacks above the 200-day MA
- **Overnight-intraday reversal**: Yesterday's overnight return (prior close->open) <= -0.5 ATR -> buy today's open, 1 ATR stop, exit 15:45; top 4 by drop. Source: Akbas, Boehmer, Jiang & Koch (2022), 'Overnight Returns, Daytime Reversals, and Future Stock Returns', JFE 145(3)
- **Sector-ETF relative strength**: At 10:00 buy sector/region ETFs whose 9:30-10:00 return beats SPY and are above VWAP (top 4 by RS), stop 0.5 ATR, exit 15:45. Source: Moskowitz & Grinblatt (1999), 'Do Industries Explain Momentum?', JF 54(4) (industry momentum), applied intraday to sector ETFs
- **IBS mean reversion**: Prior-day IBS=(C-L)/(H-L) < 0.2 -> buy open, 1 ATR stop, exit 15:45; top 4 by lowest IBS. Source: Pagonidis (2013), 'The IBS Effect: Mean Reversion in Equity ETFs', NAAIM Wagner Award paper
- **Down-streak above 200MA**: 3 consecutive lower closes while above 200d SMA -> buy open, 1 ATR stop, exit 15:45. Source: Connors & Alvarez (2008), 'Short Term Trading Strategies That Work': consecutive down closes above 200-day MA
- **Pre-holiday**: Trading day before a US market holiday: buy open, 1 ATR stop, exit 15:45. Source: Ariel (1990), 'High Stock Returns before Holidays', JF 45(5)
- **XS momentum 12-1 (intraday hold)**: Stocks with positive 12-1 month return and above 200d SMA: top 4 by 12-1 return, buy open, 1 ATR stop (pessimistic intrabar), exit 15:45. Source: Jegadeesh & Titman (1993), 'Returns to Buying Winners and Selling Losers', JF 48(1)
- **Industry/sector-ETF momentum (daily)**: Sector ETFs: top 4 by trailing 21d return (>0, above 200MA), buy open, 1 ATR stop, exit 15:45. Source: Moskowitz & Grinblatt (1999), 'Do Industries Explain Momentum?', JF 54(4)
- **1-month reversal above 200MA**: 21d return <= -8% while above 200d SMA: top 4 biggest losers, buy open, 1 ATR stop, exit 15:45. Source: Jegadeesh (1990), 'Evidence of Predictable Behavior of Security Returns', JF 45(3) (1-month reversal)
- **Volatility contraction**: ATR5 <= 0.6*ATR20 (daily range) and close within 5% of 50d high: buy open, 1 ATR stop, exit 15:45. Source: Minervini (2013), 'Trade Like a Stock Market Wizard', McGraw-Hill (volatility contraction pattern)
- **Gap-up continuation (news/earnings proxy)**: Gap up >= 1 ATR, 9:45 bar closes above open and VWAP -> buy 10:00, stop below 9:30-10:00 low -0.05ATR, exit 15:45. Source: Chan (2003), 'Stock Price Reaction to News and No-News: Drift and Reversal After Headlines', JFE 70(2)
- **Stock-vs-sector-ETF lag (intraday pairs, long leg)**: At 12:00 if stock's day return lags its sector ETF by >=0.5 ATR and ETF is up: buy 12:15, 0.75 ATR stop, exit 15:45. Source: Gatev, Goetzmann & Rouwenhorst (2006), 'Pairs Trading: Performance of a Relative-Value Arbitrage Rule', RFS 19(3)
- **Pre-FOMC drift**: FOMC announcement day: buy ETFs at open, exit 14:00 bar open (before 2pm statement), 1 ATR stop. Source: Lucca & Moench (2015), 'The Pre-FOMC Announcement Drift', JF 70(1); dates from federalreserve.gov/monetarypolicy/fomccalendars.htm
- **Index-level daily reversal**: Prior day SPY <= -1%: buy ETFs at open (top 4 by ATR%), 1 ATR stop, exit 15:45. Source: Lo & MacKinlay (1990), 'When Are Contrarian Profits Due to Stock Market Overreaction?', RFS 3(2)
- **Day-of-week**: Monday-only (and Friday-only variants): buy open, 1 ATR stop, exit 15:45. Source: Cross (1973), 'The Behavior of Stock Prices on Fridays and Mondays', FAJ 29(6)
- **Post-news-gap day-2 drift**: Yesterday gapped up >=2 ATR on >=3x 20d volume and closed above its open: buy today's open, 1 ATR stop, exit 15:45. Source: Chan (2003), 'Stock Price Reaction to News and No-News: Drift and Reversal After Headlines', JFE 70(2)
- **52wk-high proximity (open entry)**: Prior close within 2% of 252d high: buy open (top 4 closest), 1 ATR stop, exit 15:45. Source: George & Hwang (2004), 'The 52-Week High and Momentum Investing', JF 59(5)

## Progress log

- 2026-10-15 ~18:50 ET (hour 1.3): ran 58 variants (batches 1-7 + SPY noise-area). Found twin-baseline bug: gate.twins_stock never matches trades entered 9:30 and held to 15:45 (needs len>hold+1, slot>=1) so those trades add $0 to every twin -> inflated percentiles for open-entry strategies (TOM, prev-day loser). Also found 15m same-bar stop ambiguity makes tight-stop ORB results unreliable (pessimistic fill: ORB -147% OOS). Archived v1 state to hunt_state_v1_buggy_twins.json; rerunning everything with fixed twins + IS>0 requirement.
- 18:40 ET: resumed hunt. Found state clobbered by a concurrent full rerun (hunt.py twins fix 18:10: full-day holds were contributing $0 to twins, inflating percentiles). Re-ran missing b7/b8 entries; all 74 hunt entries now use fixed twins. Batches b8 (RSI2, IBS, down-streak, pre-holiday), b9 (Crabel variants, 200MA filters, NR4), b10 (overnight-intraday reversal) added. 0 verified at N=109.
- 2026-10-15 ~20:15 ET (overnight hunt): batches b11-b15 (+37 variants, N=146). All b11+ use PESSIMISTIC entry-bar stops. New families: XS momentum 12-1/6-1, sector-ETF daily momentum, 1-month reversal, volatility contraction, gap-up continuation, stock-vs-ETF lag, pre-FOMC drift, index daily reversal, day-of-week, post-gap day-2 drift, 52wk-high open. fomc_stk_1400 meets the formal gate (p=0.00025<=0.05/127) and all 4 fragility variants stay positive IS/OOS/both halves, BUT day-clustered twins p=0.00275 and symbol-matched (timing-only) p=0.022 -> flagged NOT verified (only 15 OOS event days; per-trade twins understate variance when 4 trades share a day). Insight: the per-trade twin baseline is anti-conservative for day-clustered event strategies; spydn* (index-reversal) also looked p<=0.0005 but IS<0 and clustered p 0.003-0.005.

## Hunt v2 (2026-10-15/16 overnight): daily SIP bars 2017-2026, liquid-500 + 63 ETFs

Cumulative N = **169** (146 prior + 23 v2). Bar per test: max(p_sameday, p_samesym) <= 0.05/N_at_test, IS>0, OOS>0, both OOS halves >0, >=30 OOS trades; VERIFIED additionally needs all fragility neighbours OOS>0 and IS>0.
Engine: buy at open, stop open-k*ATR14 (exact for open entries), else exit at close (proxy for 15:50 flatten; daily bars cannot see 15:50-16:00), 4 bps/side, max 4 x 25% sleeves, cash-only, $20M ADV filter. IS = oldest 70% of days from 2017, OOS = newest 30%. Returns compounded % of equity. Twins 4000 each: same-day random symbols of same type, and same-symbols-on-random-OOS-day. Caveat: universe = today's liquid-500 (survivorship); walk-forward strategies count once.

| # | Name | Family | k | IS% | OOS% | A% | B% | OOS trades | p same-day | p same-sym | core pass | verified |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 147 | v2_regime_rev_mom | Regime switch (vol/trend) | 1.0 | -68.2 | -41.9 | -31.38 | -15.33 | 2672 | 1.0 | 1.0 | False |  |
| 148 | v2_ensemble_vote2 | Ensemble vote of near-misses | 1.0 | -34.21 | -13.94 | -15.0 | 1.25 | 1627 | 1.0 | 1.0 | False |  |
| 149 | v2_prevloser_voltgt | Vol-targeted ST reversal | 1.0 | -76.7 | -41.75 | -38.09 | -5.91 | 2542 | 1.0 | 1.0 | False |  |
| 150 | v2_rs_leaders_spydown | Relative-strength leaders on SPY-down opens | 1.0 | -27.52 | -14.68 | -28.7 | 19.67 | 544 | 1.0 | 1.0 | False |  |
| 151 | v2_etf_rot_5d | Sector/factor ETF rotation | 1.0 | -93.0 | -55.87 | -34.86 | -32.25 | 2942 | 1.0 | 1.0 | False |  |
| 152 | v2_etf_rot_rev5d | Sector/factor ETF rotation | 1.0 | -80.53 | -40.52 | -37.69 | -4.53 | 2950 | 1.0 | 1.0 | False |  |
| 153 | v2_rvol_shock | RVOL / liquidity shock | 1.0 | -29.02 | 52.1 | 15.94 | 31.2 | 680 | 0.00025 | 0.00375 | False |  |
| 154 | v2_gapdn_200 | Gap-down reversal above 200MA | 1.0 | -67.55 | -37.89 | -32.54 | -7.92 | 1036 | 1.0 | 1.0 | False |  |
| 155 | v2_prev_loser_daily | ST reversal (daily, wide universe) | 1.0 | -68.37 | -44.45 | -41.5 | -5.04 | 2542 | 1.0 | 1.0 | False |  |
| 156 | v2_tom_etf | Turn-of-month (ETFs, 10y) | 1.0 | -39.95 | -20.44 | -7.72 | -13.78 | 564 | 1.0 | 1.0 | False |  |
| 157 | v2_wf_expanding_t2 | Walk-forward selected (adaptive) (WF) | 1.0 | 0.85 | 0.0 | 0.0 | 0.0 | 0 | 1.0 | 1.0 | False |  |
| 158 | v2_wf_rolling252_t2 | Walk-forward selected (adaptive) (WF) | 1.0 | -5.59 | -0.61 | 0.0 | -0.61 | 52 | 1.0 | 1.0 | False |  |
| 159 | v2_wf_rolling126_t15 | Walk-forward selected (adaptive) (WF) | 1.0 | -38.55 | 3.07 | -10.65 | 15.36 | 371 | 0.25219 | 0.29843 | False |  |
| 160 | v2_wf_regime_vol_t2 | Walk-forward selected (adaptive) (WF) | 1.0 | -4.04 | -8.27 | 0.0 | -8.27 | 69 | 1.0 | 1.0 | False |  |
| 161 | v2_wf_regime_trend_vol | Walk-forward selected (adaptive) (WF) | 1.0 | -1.31 | 0.0 | 0.0 | 0.0 | 0 | 1.0 | 1.0 | False |  |
| 162 | v2_gapup2_lowvol | IS-regime-conditioned | 1.0 | 29.57 | 3.82 | 14.65 | -9.45 | 508 | 0.09023 | 0.23494 | False |  |
| 163 | v2_tomstk_highvol | IS-regime-conditioned | 1.0 | 30.81 | 52.29 | 29.32 | 17.76 | 284 | 0.00025 | 0.04899 | False |  |
| 164 | v2_rvs4 | RVOL / liquidity shock | 1.0 | 3.78 | -21.21 | -26.07 | 6.57 | 509 | 1.0 | 1.0 | False |  |
| 165 | v2_mom15_lowvol | IS-regime-conditioned | 1.0 | 10.53 | 13.01 | 1.28 | 11.58 | 1146 | 0.0035 | 0.17021 | False |  |
| 166 | v2_tomstk_hv_k05 | IS-regime-conditioned | 0.5 | 32.87 | 50.06 | 27.65 | 17.55 | 284 | 0.00025 | 0.04299 | False |  |
| 167 | v2_tomstk_hv_nostop | IS-regime-conditioned | 99 | 12.34 | 52.52 | 27.33 | 19.78 | 284 | 0.00025 | 0.04324 | False |  |
| 168 | v2_tomstk_hv_top2 | IS-regime-conditioned | 1.0 | 10.34 | 24.27 | 16.21 | 6.94 | 142 | 0.00375 | 0.08623 | False |  |
| 169 | v2_tomstk_hv65 | IS-regime-conditioned | 1.0 | 32.97 | 57.4 | 50.52 | 4.57 | 220 | 0.00025 | 0.02149 | False |  |

### v2 families / sources

- **Regime switch (vol/trend)**: SPY RV20 > 1y median -> prev-day loser (<=-1 ATR, >200MA); else if SPY>200MA -> top-4 nearest 52wk high; else cash. Buy open, 1 ATR stop, exit close. Source: Nagel (2012), 'Evaporating Liquidity', RFS 25(7) (reversal profits rise with volatility); Moskowitz, Ooi & Pedersen (2012) JFE 104(2) time-series momentum for trend regime
- **Ensemble vote of near-misses**: Score = # of signals firing (prev_loser, 52wk-high, day2-gap, RVOL-shock, gap-down>200MA, turn-of-month); buy top-4 with >=2 votes at open, 1 ATR stop, exit close. Source: Near-miss families from HUNT_LEDGER (Lehmann/Jegadeesh, Ariel 1987, Chan 2003, George & Hwang 2004)
- **Vol-targeted ST reversal**: prev_loser signal, weight = 1%/ATR% per name (capped 50%, total <=100%). Source: Lehmann (1990) QJE 105(1); Jegadeesh (1990) JF 45(3); Connors & Alvarez (2008) 200MA filter; Moreira & Muir (2017) JF 72(4) volatility-managed portfolios
- **Relative-strength leaders on SPY-down opens**: SPY opens <=-0.3%: among names whose open gap beats SPY's, buy top-4 by 20d return vs SPY at open, 1 ATR stop, exit close. Source: Jegadeesh & Titman (1993) JF 48(1); Moskowitz & Grinblatt (1999) JF 54(4)
- **Sector/factor ETF rotation**: ETFs above 50d SMA, top-4 by 5d return, buy open, 1 ATR stop, exit close, daily. Source: Moskowitz & Grinblatt (1999) JF 54(4); Faber (2010) 'Relative Strength Strategies for Investing' SSRN 1585517
- **RVOL / liquidity shock**: Prior-day volume >=3x 20d avg, prior IBS >=0.75, above 50d SMA: buy open top-4 by volume ratio, 1 ATR stop, exit close. Source: Gervais, Kaniel & Mingelgrin (2001) JF 56(3)
- **Gap-down reversal above 200MA**: Open gap <= -1.5 ATR while prior close > 200d SMA: buy open, 1 ATR stop, exit close. Source: Akbas et al. (2022) JFE 145(3); Connors & Alvarez (2008)
- **ST reversal (daily, wide universe)**: Prior day down >=1 ATR, above 200d SMA, gap <0.5 ATR: buy open top-4 by drop, 1 ATR stop, exit close. Source: Lehmann (1990) QJE 105(1); Jegadeesh (1990) JF 45(3); Connors & Alvarez (2008) 200MA filter
- **Turn-of-month (ETFs, 10y)**: Last + first 3 trading days of month: top-4 ETFs by ATR%, buy open, 1 ATR stop, exit close. Source: Ariel (1987) JFE 18(1); Lakonishok & Smidt (1988) RFS 1(4)
- **Walk-forward selected (adaptive)**: Monthly re-selection {}. Pool of 30 signals (ST reversal, momentum, 52wk-high, RVOL-shock, gap up/down, IBS, ETF rotation, XS momentum/reversal, ATR, RS on SPY-down, turn-of-month); see pool.py. Source: Walk-forward model selection: Pardo (2008) 'The Evaluation and Optimization of Trading Strategies' (Wiley); regime conditioning per Nagel (2012) RFS 25(7)
- **IS-regime-conditioned**: SPY RV20 <= 1y median AND stock opens >=2 ATR above prior close: buy open top-4 by gap, 1 ATR stop, exit close. Source: Rule picked from v2 in-sample (2017-2023) regime table only (OOS untouched); bases: Chan (2003) JFE 70(2), Gervais et al. (2001) JF 56(3), Ariel (1987) JFE 18(1), Nagel (2012) RFS 25(7)

### v2 log

- 2026-10-15 ~22:45 ET: v2 batches b1-b4 (23 tests, cumulative N=169), 0 verified. Fetched SIP daily bars 2016-2026 for liquid-500 + 63 ETFs (12 requests, shared limiter). Structural finding: universe-average open->close drift = 2.6 bps/day vs 8 bps round-trip cost (overnight drift 5.4 bps); SPY/QQQ/IWM close->next-open after 8 bps is NEGATIVE 2017-2026 (SPY IS -57%, OOS -15%), so the earlier +5% overnight-SPY result does not survive a long sample. Walk-forward model selection over a 32-signal pool (5 variants, each 1 test) found no persistent winner. Best near-miss: turn-of-month high-ATR stocks only when SPY RV20 > 1y median (rule chosen from IS table): IS +30.8%, OOS +52.3%, halves +29.3/+17.8, all 4 fragility variants positive, same-day p=0.00025 but same-symbol p=0.02-0.09 -> edge is mostly selecting high-beta names into a rising 2023-26 tape, not timing; NOT verified.

## Hunt v3 (2026-10-16): multi-day holds + shorts allowed (daily SIP 2017-2026, liquid-500 + 63 ETFs)

Cumulative N = **208** (169 prior + 39 v3). Bar: IS>0, OOS>0, both OOS halves>0, >=30 active OOS days, max(p_sameday,p_samesym) <= 0.05/N_at_test; VERIFIED also needs fragility neighbours positive.
Engine: weights from data through prior close, held open->next open (gaps included); 4 bps/side on turnover; borrow 0.5%/yr on shorts; shorts only ADV>$50M & price>$10 (HTB proxy); gross<=100% equity; drift ignored. IS = oldest 70% of days since 2017, OOS = newest 30%. Twins 4000: same-day random same-type names; same-weights on random OOS days. Survivorship caveat: universe = today's liquid-500 (biases longs up, shorts down).

| # | Name | Family | IS% | OOS% | A% | B% | OOS Sharpe | OOS MaxDD% | SPY OOS ret/Sh/DD | gross | net expo | p same-day | p same-sym | core | verified |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 170 | xsmom12_1_LS_M | XS momentum L/S | 56.49 | 75.05 | 28.78 | 35.93 | 0.95 | -23.91 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 0.00025 | 0.76981 | False |  |
| 171 | xsmom12_1_LO_M | XS momentum long-only | 383.12 | 378.89 | 91.26 | 150.39 | 1.4 | -38.47 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.00025 | 0.63284 | False |  |
| 172 | xsmom6_1_LS_M | XS momentum L/S | 55.26 | 25.19 | 8.47 | 15.42 | 0.47 | -23.04 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 0.00025 | 0.89228 | False |  |
| 173 | xsmom12_1_LS_W | XS momentum L/S | 41.98 | 94.46 | 30.88 | 48.58 | 1.1 | -22.96 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 0.00025 | 0.67458 | False |  |
| 174 | str_week_LS_W | Short-term reversal L/S | 72.6 | -26.9 | -1.73 | -25.61 | -0.49 | -30.34 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 1.0 | 1.0 | False |  |
| 175 | lowvol_LO_M | Low-volatility anomaly | 70.55 | 38.42 | 23.3 | 12.27 | 1.47 | -7.67 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 1.0 | 0.64384 | False |  |
| 176 | lowvol_LS_M | Low-volatility anomaly | -33.62 | -50.71 | -18.58 | -39.47 | -1.27 | -54.73 | 83.45/1.42/-19.77 | 1.0 | -0.0 | 1.0 | 1.0 | False |  |
| 177 | spy_sma200_M | ETF trend timing | 43.9 | 49.6 | 24.65 | 20.02 | 1.22 | -9.82 | 83.45/1.42/-19.77 | 0.89 | 0.89 | 0.54311 | 0.72182 | False |  |
| 178 | spy_sma200_D | ETF trend timing | 58.72 | 68.19 | 29.33 | 30.05 | 1.58 | -11.11 | 83.45/1.42/-19.77 | 0.93 | 0.93 | 0.47163 | 0.57161 | False |  |
| 179 | dualmom_M | Dual momentum | 37.21 | 79.74 | 29.28 | 39.04 | 1.16 | -18.92 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.49813 | 0.46888 | False |  |
| 180 | sector_rot3_M | Sector rotation | 73.15 | 60.94 | 28.06 | 25.68 | 1.16 | -16.15 | 83.45/1.42/-19.77 | 0.97 | 0.97 | 0.64709 | 0.60585 | False |  |
| 181 | sector_LS3_M | Sector rotation | 1.69 | -1.95 | 0.61 | -2.54 | -0.06 | -11.9 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 1.0 | 1.0 | False |  |
| 182 | tsmom_etf_LS_M | Time-series momentum | -9.04 | 40.67 | 12.98 | 24.51 | 1.26 | -7.03 | 83.45/1.42/-19.77 | 0.94 | 0.71 | 0.75106 | 0.67708 | False |  |
| 183 | tsmom_etf_LO_M | Time-series momentum | 26.27 | 55.04 | 17.85 | 31.55 | 1.38 | -11.63 | 83.45/1.42/-19.77 | 0.83 | 0.83 | 0.7973 | 0.58435 | False |  |
| 184 | rsi2_stk_10 | RSI(2) swing | 122.57 | 77.01 | 66.91 | 6.05 | 0.97 | -19.81 | 83.45/1.42/-19.77 | 0.93 | 0.93 | 0.52662 | 0.54536 | False |  |
| 185 | rsi2_etf_10 | RSI(2) swing | 13.74 | 58.91 | 14.44 | 38.87 | 1.3 | -10.95 | 83.45/1.42/-19.77 | 0.45 | 0.45 | 0.00725 | 0.09423 | False |  |
| 186 | donch55_20_etf | Donchian breakout swing | 31.68 | 35.29 | 2.74 | 31.68 | 0.71 | -18.77 | 83.45/1.42/-19.77 | 0.91 | 0.91 | 0.7878 | 0.83479 | False |  |
| 187 | donch55_20_stk | Donchian breakout swing | 151.12 | 134.0 | 23.03 | 90.2 | 1.03 | -28.96 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.1967 | 0.86278 | False |  |
| 188 | sector_spy_pairs_z2 | Pairs / stat-arb | 0.32 | -3.54 | 1.42 | -4.89 | -0.24 | -9.11 | 83.45/1.42/-19.77 | 0.65 | -0.0 | 1.0 | 1.0 | False |  |
| 189 | short_overext_5d | Short overextended | -57.23 | -74.45 | -40.9 | -56.77 | -1.18 | -77.45 | 83.45/1.42/-19.77 | 0.93 | -0.93 | 1.0 | 1.0 | False |  |
| 190 | short_bearpop_3d | Short overextended | -43.74 | -52.65 | -20.15 | -40.71 | -0.78 | -55.3 | 83.45/1.42/-19.77 | 0.58 | -0.58 | 1.0 | 1.0 | False |  |
| 191 | hi52_LO_M | 52-week-high momentum | 78.29 | 78.46 | 34.2 | 32.98 | 1.42 | -12.82 | 83.45/1.42/-19.77 | 0.97 | 0.97 | 0.95851 | 0.73357 | False |  |
| 192 | hi52_LS_M | 52-week-high momentum | -21.25 | -18.32 | -1.07 | -17.44 | -0.41 | -28.89 | 83.45/1.42/-19.77 | 0.99 | -0.01 | 1.0 | 1.0 | False |  |
| 193 | hi52_LO_M_q20 | 52-week-high momentum | 103.67 | 99.34 | 42.72 | 39.67 | 1.83 | -10.16 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.93702 | 0.54686 | False |  |
| 194 | resmom_LO_M | Residual momentum | 168.63 | 173.76 | 61.42 | 69.6 | 1.69 | -15.94 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.00925 | 0.55186 | False |  |
| 195 | resmom_LS_M | Residual momentum | 39.07 | 19.66 | 13.17 | 5.74 | 0.52 | -17.25 | 83.45/1.42/-19.77 | 1.0 | 0.0 | 0.0025 | 0.67083 | False |  |
| 196 | volman_mom_LS_M | Vol-managed momentum | 50.43 | 50.31 | 24.31 | 20.91 | 1.07 | -11.67 | 83.45/1.42/-19.77 | 0.67 | 0.0 | 0.00025 | 0.71707 | False |  |
| 197 | volman_mom_LO_M | Vol-managed momentum | 124.52 | 95.36 | 45.54 | 34.24 | 1.39 | -15.12 | 83.45/1.42/-19.77 | 0.39 | 0.39 | 0.00025 | 0.6081 | False |  |
| 198 | lowbeta_mom_LO_M | Low-beta + momentum | 134.43 | 92.03 | 37.24 | 39.92 | 1.84 | -9.64 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.94101 | 0.53187 | False |  |
| 199 | lowbeta_LO_M | Low-beta + momentum | 40.99 | 20.67 | 15.9 | 4.11 | 0.74 | -10.96 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 1.0 | 0.54361 | False |  |
| 200 | halloween_SPY | Seasonality | 45.07 | 21.5 | 13.15 | 7.39 | 0.57 | -19.77 | 83.45/1.42/-19.77 | 0.5 | 0.5 | 0.5926 | 0.69683 | False |  |
| 201 | halloween_or_trend_SPY | Seasonality | 102.87 | 76.06 | 29.85 | 35.59 | 1.34 | -19.77 | 83.45/1.42/-19.77 | 0.99 | 0.99 | 0.49213 | 0.54886 | False |  |
| 202 | prefomc_eve_SPY | Pre-FOMC drift (daily) | -0.37 | -0.94 | 1.08 | -2.0 | -0.19 | -2.46 | 83.45/1.42/-19.77 | 0.03 | 0.03 | 1.0 | 1.0 | False |  |
| 203 | prefomc_2d_SPY | Pre-FOMC drift (daily) | -2.2 | 2.89 | 4.85 | -1.86 | 0.34 | -4.36 | 83.45/1.42/-19.77 | 0.06 | 0.06 | 0.46688 | 0.45489 | False |  |
| 204 | tsmom_etf_vt_LO_M | TS momentum vol-target | 77.07 | 75.32 | 25.32 | 39.9 | 1.41 | -16.57 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.82329 | 0.52437 | False |  |
| 205 | pairs_stocks_z2 | Pairs (correlated stocks) | -0.22 | -5.87 | -3.64 | -2.32 | -0.82 | -7.67 | 83.45/1.42/-19.77 | 0.46 | -0.0 | 1.0 | 1.0 | False |  |
| 206 | resmom_LO_M_q20 | Residual momentum | 137.81 | 146.37 | 54.76 | 59.2 | 1.68 | -16.42 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.05749 | 0.66933 | False |  |
| 207 | resmom6_LO_M | Residual momentum | 228.11 | 117.78 | 20.32 | 81.0 | 1.25 | -26.25 | 83.45/1.42/-19.77 | 1.0 | 1.0 | 0.4034 | 0.73582 | False |  |
| 208 | resmom_LO_M_trend | Residual momentum | 45.73 | 107.53 | 48.81 | 39.46 | 1.36 | -14.9 | 83.45/1.42/-19.77 | 0.89 | 0.89 | 0.03899 | 0.76131 | False |  |

### v3 families / sources

- **XS momentum L/S**: 12-1m return, long top decile / short bottom decile (shortable names), 50/50, monthly Source: Jegadeesh & Titman (1993) JF 48(1) 65-91; Asness, Moskowitz & Pedersen (2013) JF 68(3)
- **XS momentum long-only**: 12-1m return top decile equal weight 100% long, monthly Source: Jegadeesh & Titman (1993) JF 48(1) 65-91; Asness, Moskowitz & Pedersen (2013) JF 68(3)
- **Short-term reversal L/S**: long prior-week losers decile / short winners decile, weekly Source: Lehmann (1990) QJE 105(1); Jegadeesh (1990) JF 45(3)
- **Low-volatility anomaly**: lowest-quintile 63d vol, equal weight long-only, monthly Source: Ang, Hodrick, Xing & Zhang (2006) JF 61(1); Baker, Bradley & Wurgler (2011) FAJ 67(1); Frazzini & Pedersen (2014) JFE 111(1)
- **ETF trend timing**: hold SPY when prior month-end close > 200d SMA else cash, monthly Source: Faber (2007) 'A Quantitative Approach to Tactical Asset Allocation', J. Wealth Mgmt 9(4)
- **Dual momentum**: best 12m of SPY/EFA/EEM if >0 else cash (no bonds: excluded), monthly Source: Antonacci (2014) 'Dual Momentum Investing' (McGraw-Hill); Antonacci (2012) SSRN 2042750
- **Sector rotation**: top-3 of 11 SPDR sectors by 12-1m, each 1/3 only if >200d SMA else cash, monthly Source: Faber (2010) SSRN 1585517; Moskowitz & Grinblatt (1999) JF 54(4)
- **Time-series momentum**: all 63 ETFs, sign(12m ret) x inverse 63d vol, gross 100%, monthly Source: Moskowitz, Ooi & Pedersen (2012) JFE 104(2); Hurst, Ooi & Pedersen (2017) JPM 44(1)
- **RSI(2) swing**: stock close>200SMA & RSI2<10 -> buy next open (max 10 x 10%, lowest RSI first); exit next open after close>5SMA Source: Connors & Alvarez (2008) 'Short Term Trading Strategies That Work' (TradingMarkets)
- **Donchian breakout swing**: ETF close > prior 55d high -> buy next open; exit after close < prior 20d low; max 10 x 10% Source: Donchian; Faith (2007) 'Way of the Turtle' (McGraw-Hill)
- **Pairs / stat-arb**: each SPDR sector vs SPY: z of log ratio (60d) >2 short sector/long SPY, < -2 reverse, exit |z|<0.5; 9% per leg Source: Gatev, Goetzmann & Rouwenhorst (2006) RFS 19(3)
- **Short overextended**: short names with RSI2>95 and +10% in 5d (ADV>$50M,>$10), 10% each up to 100%, cover after 5 sessions Source: Connors & Alvarez (2008) (RSI(2) extremes); De Bondt & Thaler (1985) JF 40(3)
- **52-week-high momentum**: stocks: top decile of close/252d high, equal weight long-only, monthly Source: George & Hwang (2004) 'The 52-Week High and Momentum Investing', JF 59(5)
- **Residual momentum**: stocks: top decile of 12-1m SPY-residual return / residual vol, long-only, monthly Source: Blitz, Huij & Martens (2011) 'Residual Momentum', J. Empirical Finance 18(3); Gutierrez & Pirinsky (2007)
- **Vol-managed momentum**: 12-1 L/S decile momentum scaled by 12%/126d realized strategy vol (cap 1x), monthly Source: Barroso & Santa-Clara (2015) 'Momentum Has Its Moments', JFE 116(1); Moreira & Muir (2017) JF 72(4)
- **Low-beta + momentum**: stocks: top decile of rank(-beta252)+rank(12-1m mom), long-only, monthly (no fundamental quality data on box) Source: Frazzini & Pedersen (2014) 'Betting Against Beta', JFE 111(1); Asness, Moskowitz & Pedersen (2013) JF 68(3)
- **Seasonality**: hold SPY Nov-Apr, cash May-Oct Source: Bouman & Jacobsen (2002) 'The Halloween Indicator', AER 92(5)
- **Pre-FOMC drift (daily)**: hold SPY open of day before FOMC announcement -> open of announcement day Source: Lucca & Moench (2015) 'The Pre-FOMC Announcement Drift', JF 70(1)
- **TS momentum vol-target**: ETFs with 12m ret>0, each weight ~10%/annual vol scaled, gross capped 100%, monthly Source: Moskowitz, Ooi & Pedersen (2012) JFE 104(2); Hurst, Ooi & Pedersen (2017) JPM 44(1)
- **Pairs (correlated stocks)**: 10 same-industry pairs, 60d z of log ratio >2 short rich/long cheap, exit |z|<0.5 Source: Gatev, Goetzmann & Rouwenhorst (2006) 'Pairs Trading', RFS 19(3)

### v3 log

- 2026-10-16 ~10:30 ET: v3 batches b1-b3 (21 tests, cumulative N=190), 0 verified, 0 core pass. Every long/trend strategy made money OOS (SPY open->open B&H OOS +83.5%, Sharpe 1.42, MaxDD -19.8%) but none beat both random baselines: their return is market beta. XS momentum 12-1 L/S beat same-day random names (p=0.00025) but not same-weights-on-random-days (p=0.67-0.77), consistent with survivorship (universe = today's liquid-500). Shorts-only rules lost 52-74% OOS. Short-term weekly reversal, sector L/S, sector/SPY pairs negative OOS. PEAD not tested: no earnings-surprise data on box. Best near-miss: RSI(2) on ETFs (OOS +58.9%, Sharpe 1.30, DD -11.0%, p 0.007/0.094).
- 2026-10-16 ~11:35 ET: batches b4-b5 (18 tests, cumulative N=208), 0 verified, 0 core pass. New families: 52wk-high (George & Hwang 2004), residual momentum (Blitz et al. 2011), vol-managed momentum (Barroso & Santa-Clara 2015), low-beta+momentum, Halloween (Bouman & Jacobsen 2002), daily pre-FOMC on SPY (Lucca & Moench 2015), vol-targeted TSMOM, 10 same-industry stock pairs. Best: residual momentum long-only OOS +173.8% (Sharpe 1.69, DD -15.9%) beat SPY and same-day random names (p=0.009) but not same-weights-random-days (p=0.55); passes neither Bonferroni bar (0.05/N). Survivorship (today's liquid-500) likely inflates all stock-momentum longs. Earnings effects not testable (no earnings data on box).

## Hunt #2 (2026-10-16, strategy_hunt_2/): always-on candidates, cumulative N = **222** (208 + 14)

Engine strategy_hunt_2/eng4.py (eng3 conventions + close->open leg), 10k twins x2, bar 0.05/N_at_test. 0 verified, 0 core pass. Details: strategy_hunt_2/report.md

| # | Name | Family | IS% | OOS% | OOS A/B% | OOS Sharpe | OOS MaxDD% | day win% | OOS rebal days | OOS cost% | p same-day/same-sym | Bonf bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 209 | overnight_SPY | Overnight drift | -57.02 | -15.19 | -11.78/-3.86 | -0.54 | -22.36 | 50.7 | 738 | 59.04 | 1.0/1.0 | 0.000239 |
| 210 | overnight_SPY_QQQ_IWM | Overnight drift | -47.99 | -8.65 | -7.42/-1.33 | -0.2 | -22.76 | 52.2 | 738 | 59.04 | 1.0/1.0 | 0.000238 |
| 211 | onmom_LS_CO | Overnight momentum XS | -58.35 | -24.15 | -20.59/-4.48 | -0.7 | -24.44 | 49.3 | 738 | 59.77 | 1.0/1.0 | 0.000237 |
| 212 | onmom_LS_M | Overnight momentum XS | -14.51 | 5.76 | -1.8/7.7 | 0.2 | -20.66 | 53.8 | 35 | 2.99 | 0.0348/0.85591 | 0.000236 |
| 213 | pca_statarb_AL | PCA residual stat-arb | 1.71 | -0.46 | 1.95/-2.36 | 0.02 | -9.42 | 47.6 | 147 | 4.64 | 0.33027/0.27477 | 0.000235 |
| 214 | pca_statarb_AL_k2 | PCA residual stat-arb | -3.91 | -1.34 | 1.76/-3.05 | -0.03 | -9.41 | 51.2 | 151 | 3.19 | 1.0/1.0 | 0.000234 |
| 215 | pca_statarb_AL_LO | PCA residual stat-arb | 152.91 | 173.88 | 49.65/83.02 | 1.9 | -18.25 | 55.3 | 147 | 3.55 | 0.05489/0.20578 | 0.000233 |
| 216 | etf_mr_hivol | ETF mean reversion x high-vol regime | 5.67 | 43.06 | 19.37/19.85 | 1.02 | -11.67 | 49.0 | 209 | 3.94 | 0.21398/0.05489 | 0.000231 |
| 217 | resrev_wk_LS | Residual weekly reversal | 9.49 | -10.32 | -3.22/-7.33 | -0.29 | -18.51 | 47.0 | 154 | 11.55 | 1.0/1.0 | 0.00023 |
| 218 | resrev_wk_LS_q20 | Residual weekly reversal | 10.75 | -12.73 | -5.96/-7.2 | -0.43 | -19.36 | 47.4 | 154 | 10.4 | 1.0/1.0 | 0.000229 |
| 219 | etf_mr_hivol_z2 | ETF mean reversion x high-vol regime | -2.68 | 10.29 | 11.61/-1.18 | 0.34 | -11.83 | 45.2 | 122 | 2.21 | 0.83482/0.36306 | 0.000228 |
| 220 | etf_mr_hivol_z1 | ETF mean reversion x high-vol regime | 88.31 | 40.64 | 27.49/10.31 | 0.87 | -15.72 | 49.5 | 255 | 5.62 | 0.47895/0.15128 | 0.000227 |
| 221 | etf_mr_allvol | ETF mean reversion x high-vol regime | 28.26 | 63.29 | 12.09/45.68 | 1.14 | -18.49 | 50.2 | 394 | 7.14 | 0.08739/0.09939 | 0.000226 |
| 222 | etf_mr_hivol_hedged | ETF mean reversion x high-vol regime | -2.65 | 0.41 | -1.23/1.65 | 0.05 | -5.78 | 45.7 | 209 | 3.67 | 0.32547/0.25257 | 0.000225 |

## Hunt #3 (2026-10-16, strategy_hunt_3/): regime meta, walk-forward ML, cross-asset, vol-target/risk parity. Cumulative N = **238** (222 + 16). 0 verified, 0 core pass. Details: strategy_hunt_3/report.md

| # | Name | Family | IS% | OOS% | OOS A/B% | OOS Sharpe | OOS MaxDD% | OOS beta | alpha %/yr (t) | day win% | OOS rebal days | p same-day/same-sym | Bonf bar | core |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
16
| 223 | spy_voltgt15 | Vol targeting | 92.2 | 65.31 | 23.87/33.45 | 1.41 | -15.82 | 0.78 | 0.82 (t 0.36) | 57.3 | 170 | 0.50415/0.61974 | 0.000224 | False |
| 224 | spy_voltgt15_W | Vol targeting | 76.33 | 64.71 | 24.21/32.61 | 1.39 | -16.49 | 0.79 | 0.5 (t 0.22) | 57.3 | 39 | 0.50695/0.62964 | 0.000223 | False |
| 225 | riskparity4_M | Risk parity (no leverage) | 54.44 | 58.06 | 31.93/19.81 | 1.6 | -7.71 | 0.47 | 5.76 (t 1.42) | 56.6 | 35 | 0.80892/0.49285 | 0.000222 | False |
| 226 | eqw4_M | Risk parity (no leverage) | 54.51 | 62.11 | 31.45/23.32 | 1.55 | -9.3 | 0.5 | 6.09 (t 1.33) | 58.0 | 0 | 0.80252/0.50325 | 0.000221 | False |
| 227 | credit_timing_SPY | Cross-asset timing | 7.24 | 53.68 | 13.26/35.69 | 1.36 | -11.87 | 0.47 | 5.0 (t 1.0) | 56.8 | 22 | 0.70263/0.47105 | 0.00022 | False |
| 228 | credit_timing_cash | Cross-asset timing | -10.19 | 45.54 | 7.54/35.34 | 1.26 | -11.09 | 0.47 | 3.14 (t 0.69) | 56.1 | 22 | 0.49605/0.54385 | 0.000219 | False |
| 229 | spy_vs_tlt_mom | Cross-asset timing | 59.92 | 41.5 | 22.46/15.55 | 0.99 | -11.95 | 0.55 | 0.6 (t 0.11) | 56.2 | 8 | 0.75342/0.71743 | 0.000218 | False |
| 230 | gold_riskoff | Cross-asset timing | 44.56 | 150.01 | 47.1/69.95 | 1.76 | -14.82 | 0.72 | 17.23 (t 1.96) | 58.5 | 31 | 0.16948/0.14589 | 0.000217 | False |
| 231 | spy_bh | Benchmark | 115.12 | 83.45 | 29.85/41.28 | 1.42 | -19.77 | 1.0 | -0.03 (t -2.43) | 57.3 | 0 | 0.50745/0.49405 | 0.000216 | False |
| 232 | meta_perf_63 | Regime meta (trailing perf) | 28.42 | 44.76 | 12.1/29.13 | 0.93 | -15.86 | 0.57 | 1.19 (t 0.17) | 51.5 | 262 | 0.54065/0.30107 | 0.000216 | False |
| 233 | meta_perf_126 | Regime meta (trailing perf) | 42.35 | 58.44 | 15.32/37.4 | 1.2 | -10.34 | 0.41 | 7.78 (t 1.07) | 51.9 | 317 | 0.12679/0.17128 | 0.000215 | False |
| 234 | meta_regime_vt | Regime meta (vol/trend) | 8.92 | 45.61 | 18.07/23.33 | 0.91 | -13.67 | 0.64 | -0.08 (t -0.01) | 53.3 | 224 | 0.52905/0.48125 | 0.000214 | False |
| 235 | meta_regime_vt_cashdown | Regime meta (vol/trend) | 30.15 | 46.5 | 20.64/21.43 | 1.08 | -9.57 | 0.37 | 5.85 (t 0.87) | 54.1 | 206 | 0.36606/0.46935 | 0.000213 | False |
| 236 | ml_gbm_LO_M | Walk-forward ML ranking | 39.66 | 199.6 | 46.52/104.48 | 1.37 | -31.06 | 1.62 | 6.72 (t 0.64) | 58.3 | 35 | 0.0001/0.57424 | 0.000212 | False |
| 237 | ml_gbm_LS_M | Walk-forward ML ranking | -9.36 | 18.81 | 0.63/18.06 | 0.52 | -12.76 | 0.39 | -1.92 (t -0.29) | 55.1 | 35 | 0.0006/0.54355 | 0.000211 | False |
| 238 | ml_gbm_LO_hedged | Walk-forward ML ranking | -4.66 | 31.66 | 7.23/22.78 | 0.97 | -9.45 | 0.31 | 3.12 (t 0.59) | 55.3 | 35 | 0.12149/0.61954 | 0.00021 | False |

## Hunt #4 (2026-10-16, strategy_hunt_4/): Holly selection, Danelfin-style ML L/S, grid bot. Cumulative N = **251** (238 + 13). 0 verified, 0 core pass. Details: strategy_hunt_4/report.md

| # | Name | Method | IS% | OOS% | OOS A/B% | OOS Sharpe | MaxDD% | win% | OOS trades/days | beta / alpha%/yr (t) | p (twins) | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 239 | holly_L60_top3 | Holly selection | -25.62 | -12.27 | -5.37/-6.90 | -1.04 | -14.64 | 33.9 (days) | 451 days | n/a (intraday, flat) | 0.074 vs 3 random rules | rejected |
| 240 | holly_L20_top3 | Holly | -30.99 | -21.18 | -4.14/-17.04 | -1.78 | -22.91 | 36.9 | 463 | n/a | 0.31 | rejected |
| 241 | holly_L120_top3 | Holly | -18.74 | -13.92 | -2.12/-11.80 | -1.02 | -15.52 | 30.7 | 433 | n/a | 0.18 | rejected |
| 242 | holly_L60_top1 | Holly | 2.56 | -12.09 | 1.89/-13.98 | -0.69 | -19.72 | 25.3 | 451 | n/a | 0.20 | rejected |
| 243 | ml_LS_stk_dollar_q10 | Danelfin-style ML L/S | -7.01 | 21.37 | 0.95/20.24 | 0.56 | -13.78 | – | monthly | 0.41 / -1.56 (-0.23) | 0.0012 / 0.55 | rejected (market-ride residue) |
| 244 | ml_LS_stk_beta_q10 | ML L/S beta-neutral | -8.25 | -3.86 | -1.62/-2.28 | -0.11 | -14.78 | – | monthly | 0.26 / -6.58 (-1.44) | 1.0 / 1.0 | rejected |
| 245 | ml_LS_stk_dollar_q20 | ML L/S | -6.22 | 12.16 | 0.30/11.83 | 0.44 | -10.60 | – | monthly | 0.33 / -2.81 (-0.55) | 0.002 / 0.62 | rejected |
| 246 | ml_LS_stk_beta_q20 | ML L/S beta-neutral | -14.91 | -7.35 | -1.09/-6.33 | -0.37 | -12.99 | – | monthly | 0.16 / -5.88 (-1.69) | 1.0 / 1.0 | rejected |
| 247 | grid_FRI | Grid bot, flat Fridays | -1.03 | 30.41 | 19.74/10.67 | 1.28* | – | 81.5 | 1549 lots | exposure 21%; matched B&H +5.95% | 0.0001 (same-exit twins) | **promising-at-best** |
| 248 | grid_DAY | Grid, flat daily | -15.54 | 9.52 | 9.75/-0.22 | 0.45* | – | 64.2 | 2042 | expo 0.3% | 0.0001 | rejected |
| 249 | grid_STOP3 | Grid, -3% stop, no time exit | 0.62 | 26.65 | 15.97/10.68 | 1.51* | – | 89.0 | 1665 | expo 33%; matched B&H +9.19% | 0.0001 | promising-at-best |
| 250 | grid_FRI_PESS | Grid FRI, pessimistic fills | -24.50 | 20.46 | 14.87/5.60 | – | – | 78.9 | 1372 | – | 0.0001 | rejected (IS<0) |
| 251 | grid_STOP3_PESS | Grid STOP3, pessimistic | -24.78 | 15.47 | 10.64/4.83 | – | – | 87.4 | 1466 | – | 0.0001 | rejected (IS<0) |

## Hunt #5 (2026-10-21, strategy_hunt_5/): SEC Form 4 insider purchases (DERA 2006-2026Q1, prices 2016+ survivor-biased liquid-500). Cumulative N = **279** (251 + 28). 0 verified, 0 core pass; capS H63/H126 promising only. Details: strategy_hunt_5/report.md

| # | Name | IS/OOS events | IS mean net % / excess % | IS p sd/ss | OOS mean net % / excess % | OOS win% | OOS p sd/ss | cal Sharpe IS/OOS | OOS MaxDD% | OOS beta / alpha (t) | Bonf | core |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 252 | ins_all_H21 | 1626/180 | 1.282 / 0.093 | 0.44536/0.55084 | 3.821 / 1.815 | 59.4 | 0.19458/0.06799 | 0.61 / 1.57 | -11.45 | 1.0 / 8.61 (t 0.95) | 0.000198 | False |
| 253 | ins_cluster3_H21 | 95/14 | 1.717 / 0.001 | 0.53225/0.39036 | 4.128 / 1.825 | 64.3 | –/– | 0.28 / 1.07 | -2.98 | 0.15 / 1.72 (t 0.52) | 0.000198 | False |
| 254 | ins_ceocfo_H21 | 332/42 | 1.445 / 0.207 | 0.34307/0.26697 | 3.128 / 1.606 | 61.9 | 0.36136/0.33517 | 0.43 / 1.18 | -6.3 | 0.31 / 2.54 (t 0.49) | 0.000197 | False |
| 255 | ins_big10pct_100k_H21 | 927/110 | 1.436 / 0.307 | 0.21988/0.39106 | 4.424 / 2.216 | 60.9 | 0.17928/0.0216 | 0.61 / 1.28 | -14.55 | 1.02 / 3.02 (t 0.31) | 0.000196 | False |
| 256 | ins_capS_H21 | 328/33 | 1.806 / 0.826 | 0.10669/0.26277 | 3.436 / 1.854 | 69.7 | 0.35146/0.40566 | 0.49 / 0.69 | -7.59 | 0.37 / -2.51 (t -0.49) | 0.000195 | False |
| 257 | ins_capM_H21 | 601/76 | 2.073 / 0.319 | 0.23028/0.0438 | 3.273 / 1.467 | 53.9 | 0.32657/0.14499 | 0.6 / 1.17 | -9.08 | 0.5 / 3.0 (t 0.4) | 0.000195 | False |
| 258 | ins_capL_H21 | 720/76 | 0.435 / -0.373 | 0.88111/0.9861 | 4.41 / 2.108 | 60.5 | 0.23018/0.12479 | 0.44 / 0.93 | -13.77 | 1.02 / -4.54 (t -0.48) | 0.000194 | False |
| 259 | ins_all_H63 | 1626/180 | 5.761 / 1.763 | 0.008/0.0023 | 8.999 / 2.094 | 65.0 | 0.75742/0.11009 | 0.96 / 1.35 | -11.08 | 1.03 / 2.79 (t 0.36) | 0.000193 | False |
| 260 | ins_cluster3_H63 | 95/14 | 5.787 / 0.699 | 0.53565/0.30377 | 4.384 / -1.558 | 57.1 | –/– | 0.56 / 0.67 | -7.97 | 0.33 / -0.93 (t -0.13) | 0.000192 | False |
| 261 | ins_ceocfo_H63 | 332/42 | 5.592 / 1.351 | 0.21668/0.06009 | 10.633 / 4.228 | 69.0 | 0.40826/0.28587 | 0.71 / 1.39 | -12.07 | 0.97 / 6.93 (t 0.64) | 0.000192 | False |
| 262 | ins_big10pct_100k_H63 | 927/110 | 6.456 / 2.3 | 0.0036/0.0017 | 7.717 / 0.469 | 64.5 | 0.87521/0.09029 | 0.97 / 1.01 | -16.01 | 1.1 / -3.38 (t -0.36) | 0.000191 | False |
| 263 | ins_capS_H63 | 328/33 | 10.752 / 6.243 | 0.0001/0.0002 | 11.061 / 5.374 | 78.8 | 0.35076/0.45575 | 1.07 / 1.79 | -11.02 | 0.82 / 14.16 (t 1.42) | 0.00019 | False |
| 264 | ins_capM_H63 | 601/76 | 6.817 / 2.106 | 0.0353/0.0011 | 9.412 / 2.038 | 63.2 | 0.65693/0.0434 | 0.96 / 1.32 | -12.22 | 0.87 / 4.15 (t 0.46) | 0.000189 | False |
| 265 | ins_capL_H63 | 720/76 | 2.839 / -0.423 | 0.9574/0.9723 | 7.743 / 0.648 | 61.8 | 0.80932/0.29307 | 0.68 / 0.95 | -17.14 | 1.2 / -4.5 (t -0.4) | 0.000189 | False |
| 266 | ins_all_H126 | 1626/180 | 11.317 / 3.109 | 0.0074/0.001 | 12.772 / 0.3 | 68.9 | 0.9811/0.46385 | 0.97 / 1.33 | -11.25 | 1.07 / 1.88 (t 0.26) | 0.000188 | False |
| 267 | ins_cluster3_H126 | 95/14 | 10.541 / 0.821 | 0.58704/0.39946 | 3.445 / -6.891 | 57.1 | –/– | 0.65 / 0.14 | -17.43 | 0.55 / -10.58 (t -0.91) | 0.000187 | False |
| 268 | ins_ceocfo_H126 | 332/42 | 9.833 / 1.323 | 0.52455/0.18468 | 16.273 / 5.057 | 69.0 | 0.61684/0.56704 | 0.74 / 1.33 | -12.62 | 1.16 / 4.7 (t 0.43) | 0.000187 | False |
| 269 | ins_big10pct_100k_H126 | 927/110 | 11.908 / 3.55 | 0.0116/0.0018 | 9.994 / -2.675 | 64.5 | 0.9912/0.19918 | 0.98 / 1.06 | -15.86 | 1.12 / -2.95 (t -0.33) | 0.000186 | False |
| 270 | ins_capS_H126 | 328/33 | 18.059 / 9.106 | 0.0001/0.0001 | 18.985 / 7.456 | 78.8 | 0.50115/0.76112 | 1.15 / 2.13 | -10.66 | 0.92 / 22.42 (t 2.09) | 0.000185 | False |
| 271 | ins_capM_H126 | 601/76 | 11.897 / 3.128 | 0.10639/0.0026 | 9.367 / -3.375 | 68.4 | 0.9774/0.37286 | 0.97 / 0.8 | -12.65 | 0.9 / -6.11 (t -0.7) | 0.000185 | False |
| 272 | ins_capL_H126 | 720/76 | 7.786 / 0.318 | 0.87981/0.82402 | 14.404 / 1.911 | 67.1 | 0.84092/0.18168 | 0.76 / 1.2 | -18.85 | 1.27 / 0.57 (t 0.05) | 0.000184 | False |
| 273 | ins_all_H252 | 1626/75 | 23.926 / 7.2 | 0.0184/0.003 | 52.6 / 27.442 | 73.3 | 0.50495/0.08029 | 0.95 / 1.88 | -11.6 | 1.11 / 14.25 (t 1.81) | 0.000183 | False |
| 274 | ins_cluster3_H252 | 95/7 | 16.649 / -0.661 | 0.86451/0.82222 | 106.875 / 85.905 | 57.1 | –/– | 0.62 / 0.72 | -24.48 | 0.72 / 1.08 (t 0.06) | 0.000182 | False |
| 275 | ins_ceocfo_H252 | 332/18 | 21.309 / 4.261 | 0.54215/0.33557 | 121.021 / 98.42 | 83.3 | –/– | 0.68 / 1.82 | -15.76 | 1.36 / 20.47 (t 1.5) | 0.000182 | False |
| 276 | ins_big10pct_100k_H252 | 927/46 | 26.492 / 9.433 | 0.0037/0.0002 | 42.217 / 16.777 | 73.9 | 0.67433/0.09369 | 0.99 / 1.72 | -11.62 | 1.16 / 13.62 (t 1.31) | 0.000181 | False |
| 277 | ins_capS_H252 | 328/14 | 37.82 / 21.131 | 0.0001/0.0006 | 151.063 / 126.727 | 92.9 | –/– | 1.14 / 2.56 | -12.29 | 1.16 / 37.17 (t 2.99) | 0.000181 | False |
| 278 | ins_capM_H252 | 601/31 | 25.619 / 7.599 | 0.11009/0.0003 | 26.97 / 2.088 | 80.6 | 0.86951/0.009 | 0.96 / 1.91 | -11.74 | 0.88 / 16.94 (t 1.65) | 0.00018 | False |
| 279 | ins_capL_H252 | 720/32 | 16.686 / 0.804 | 0.9899/0.91861 | 35.131 / 9.625 | 59.4 | 0.75292/0.0287 | 0.77 / 1.02 | -15.48 | 1.25 / -4.65 (t -0.51) | 0.000179 | False |

## Hunt #6 (2026-10-21, strategy_hunt_6/): StockTwits social sentiment (NYU public dataset, labeled bull/bear posts 2015-2022). Cumulative N = **288** (279 + 9). 0 verified, 0 core pass, all rejected. Details: strategy_hunt_6/report.md

| # | Name | IS% | OOS% | OOS A/B% | OOS Sharpe | OOS MaxDD% | day win% | OOS cost% | beta / alpha (t) | p sd/ss | Bonf | core |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
['2020-12-11', '2022-12-30'] [8.94, 0.31, -26.29]
| 280 | st_spike_long_1d | -97.19 | -25.87 | -46.56/38.71 | -0.03 | -65.59 | 49.6 | 30.74 | 1.41 / -10.04 (t -0.33) | 1.0/1.0 | 0.000179 | False |
| 281 | st_spike_short_5d | -38.61 | -43.52 | -27.22/-22.4 | -0.73 | -50.14 | 44.5 | 10.49 | -1.27 / -15.35 (t -1.1) | 1.0/1.0 | 0.000178 | False |
| 282 | st_spike_long_5d | -12.55 | -1.29 | 7.34/-8.04 | 0.14 | -34.33 | 52.8 | 9.41 | 1.32 / -3.45 (t -0.25) | 0.38576/0.41966 | 0.000177 | False |
| 283 | st_bull_LS_1d | -52.9 | -38.25 | -16.46/-26.08 | -1.62 | -42.18 | 47.2 | 28.57 | -0.07 / -22.12 (t -2.29) | 1.0/1.0 | 0.000177 | False |
| 284 | st_bull_LS_W | 14.49 | -16.61 | -8.5/-8.86 | -0.64 | -25.84 | 50.5 | 6.82 | -0.07 / -7.67 (t -0.88) | 1.0/1.0 | 0.000176 | False |
| 285 | st_bullshift_LS_1d | -62.54 | -40.98 | -31.73/-13.55 | -1.82 | -47.11 | 44.3 | 29.87 | -0.03 / -24.59 (t -2.59) | 1.0/1.0 | 0.000175 | False |
| 286 | st_bull_contra_W | -0.7 | -13.1 | 0.62/-13.64 | -0.5 | -20.53 | 48.4 | 6.91 | 0.13 / -6.84 (t -0.81) | 1.0/1.0 | 0.000175 | False |
| 287 | st_spy_bullz_long | -8.43 | -9.38 | -4.77/-4.84 | -0.73 | -10.48 | 30.9 | 4.88 | 0.11 / -5.26 (t -1.27) | 1.0/1.0 | 0.000174 | False |
| 288 | st_spy_contra | -19.52 | -5.99 | 3.5/-9.17 | -0.21 | -16.8 | 30.1 | 10.39 | 0.14 / -3.2 (t -0.41) | 1.0/1.0 | 0.000174 | False |

## Hunt #7 (2026-10-21, strategy_hunt_7/): intraday/overnight ETF strategies on IEX 15m bars. Cumulative N = **296** (288 + 8). 0 verified, 0 core pass, none found. Details: strategy_hunt_7/report.md

| # | Name | IS/OOS trades | IS% | OOS% | OOS A/B% | OOS Sharpe | OOS DD% | win% | gross bps/trade | beta / alpha (t) | p date/flip | blend ret/Sh/DD | Bonf | core |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 289 | pairs_z2 | 2331/972 | -91.41 | -60.35 | -40.5/-51.16 | -5.43 | -61.19 | 35.7 | 0.57 | 0.07 / -50.27 (t -7.61) | 1.0/1.0 | 0.95 / 0.1 / -17.03 | 0.000173 | False |
| 290 | pairs_z3 | 1025/457 | -66.58 | -37.96 | -20.28/-27.09 | -4.2 | -38.6 | 35.7 | -0.36 | 0.03 / -25.9 (t -5.84) | 1.0/1.0 | 7.92 / 0.4 / -16.47 | 0.000172 | False |
| 291 | bigdrop_rev_k3 | 512/230 | -13.86 | -10.81 | -3.25/-8.1 | -2.0 | -10.85 | 33.0 | -4.8 | 0.02 / -6.4 (t -2.88) | 1.0/1.0 | 13.93 / 0.65 / -15.91 | 0.000172 | False |
| 292 | bigdrop_rev_k3_hv | 164/89 | 0.92 | -1.36 | -0.26/-1.07 | -0.37 | -2.97 | 46.1 | 5.49 | 0.0 / -0.73 (t -0.51) | 1.0/1.0 | 15.66 / 0.72 / -15.87 | 0.000171 | False |
| 293 | bigdrop_rev_k4_close | 183/92 | -10.25 | -6.44 | -4.98/-1.58 | -1.18 | -7.44 | 46.7 | -11.42 | 0.05 / -4.18 (t -2.0) | 1.0/1.0 | 14.73 / 0.68 / -16.2 | 0.000171 | False |
| 294 | overnight_after_down1 | 473/147 | -12.87 | 3.06 | -3.67/6.94 | 0.34 | -8.72 | 55.8 | 16.67 | 0.08 / 0.78 (t 0.21) | 0.05439/0.0431 | 16.41 / 0.74 / -16.78 | 0.00017 | False |
| 295 | overnight_after_down2 | 124/36 | -10.13 | 2.21 | 0.28/1.95 | 0.55 | -3.06 | 63.9 | 28.61 | 0.01 / 1.06 (t 0.66) | 0.05419/0.08779 | 16.28 / 0.74 / -15.98 | 0.000169 | False |
| 296 | etf_xs_mom_1030 | 1086/462 | -53.47 | -41.52 | -19.08/-33.94 | -3.58 | -41.48 | 39.4 | -1.48 | 0.07 / -29.43 (t -5.09) | 1.0/1.0 | 6.98 / 0.36 / -17.08 | 0.000169 | False |

## Hunt #8 (2026-10-22) — Instagram reels
Both reels UNRECOVERABLE (no testable rules). 0 trials. Cumulative N = 296 (unchanged).

## Hunt #9 (2026-10-22, research_lab/hunts/h9_chronos_spy_guard/): Chronos-Bolt-small (zero-shot, CPU) 5-day SPY forecast as an SPY on/off guard. IEX daily SPY, signal at close, fill next open, 5 bps/side. IS 2021-08-02..2025-03-21, OOS 2025-03-24..2026-10-14. Cumulative N = **298** (296 + 2). 0 pass.

| # | Name | IS% / Sh | OOS% / Sh / DD | SPY OOS% / Sh / DD | 70/30 OOS% / Sh / DD | p vs SPY | Holm@298 | CPCV med Sh (SPY 1.00) | PBO | DSR | SPA p vs SPY / 70-30 | pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 297 | chronos_median_trend | 30.92 / 0.61 | 1.88 / 0.15 / -19.51 | 38.58 / 1.29 / -14.99 | 26.27 / 1.29 / -10.67 | 0.999 | 1.0 | 0.27 | 0.943 | 0.365 | 0.885 / 0.653 (set) | False |
| 298 | chronos_q10_guard | 28.57 / 0.54 | 22.31 / 0.98 / -18.14 | 38.58 / 1.29 / -14.99 | 26.27 / 1.29 / -10.67 | 0.855 | 1.0 | 0.94 | 0.943 | 0.746 | 0.885 / 0.653 (set) | False |

## Hunt #10 (2026-10-22) — Instagram carousel @arwazaz_ DeL4K4hk6k9 ("Algo trading with JEV")
Architecture diagram only, no thresholds/rules; needs Jev API (waitlist). NOT TESTABLE. 0 trials. Cumulative N = 298 (unchanged).

## Hunt #11 (2026-10-22, research_lab/hunts/h11_nfl_betting/): NFL ATS/totals at -110, nflverse lines, IS 1999-2018 / OOS 2019-2026. Cumulative N = **307** (298 + 9). 0 pass.

| # | Name | IS bets/win%/ROI% | OOS bets (push) | OOS win% | OOS ROI% | OOS 95% CI ROI | binom p vs 52.38% | Holm@307 | pass |
|---|---|---|---|---|---|---|---|---|---|
| 299 | S1_home_dog | 1742/50.03/-4.35 | 809 (18) | 51.33 | -1.97 | (-8.47, 4.56) | 0.735 | 1.00 | False |
| 300 | S2_div_home_dog | 714/48.69/-6.79 | 289 (4) | 51.93 | -0.85 | (-11.76, 10.07) | 0.584 | 1.00 | False |
| 301 | S3_wind_under | 540/57.52/9.66 | 144 (2) | 54.93 | 4.8 | (-10.48, 20.08) | 0.300 | 1.00 | False |
| 302 | S4_cold_under | 296/46.74/-10.6 | 88 (2) | 47.67 | -8.78 | (-28.31, 10.85) | 0.837 | 1.00 | False |
| 303 | S5_rest_edge | 616/51.58/-1.49 | 184 (3) | 46.41 | -11.22 | (-24.75, 2.22) | 0.954 | 1.00 | False |
| 304 | S6_short_week_fade | 0/0.0/nan | 0 (0) | 0.0 | nan | (nan, nan) | 1.000 | 1.00 | False |
| 305 | S7_west_early_east | 197/52.36/-0.05 | 100 (1) | 42.42 | -18.82 | (-37.0, -0.64) | 0.981 | 1.00 | False |
| 306 | S8_elo_vs_line | 1528/52.66/0.52 | 723 (17) | 51.27 | -2.06 | (-9.05, 4.75) | 0.734 | 1.00 | False |
| 307 | S9_big_dog | 651/52.91/0.99 | 257 (9) | 50.0 | -4.39 | (-15.88, 7.18) | 0.792 | 1.00 | False |

## Ledger correction (2026-10-22): Hunt #11 candle setups (research_lab/hunts/h11_candle_setups, +12 trials, FAIL) were logged only in research_lab/ledger. True cumulative after Hunt #11 = 298 + 12 + 9 = **319** (rows 308–319 = h11_candle_setups, see that folder).

## Hunt #12 (2026-10-22, research_lab/hunts/h12_original/): original strategies. Stocks IEX daily, IS 2020-08-25..2024-12-06, OOS 2024-12-09..2026-10-14, 5 bps/side; NFL -110. Cumulative N = **324** (319 + 5). 0 pass.

| # | Name | OOS ret%/Sh/DD | SPY OOS 26.76/0.87/-18.98; 70/30 18.66/0.87/-13.60 | p | Holm@324 | SPA vs SPY/70-30 | pass |
|---|---|---|---|---|---|---|---|
| 320 | E1_month_end_rebal_flow | 3.81/0.78/-2.88 | IS 10.92 | 0.145 | 1.0 | 0.88/0.85 | False |
| 321 | E2_letf_close_reversal | 2.29/0.22/-7.06 | IS -3.74 | 0.385 | 1.0 | 0.87/0.84 | False |
| 322 | E3_credit_calm_equity_panic | 1.84/0.23/-7.12 | IS 1.97 | 0.378 | 1.0 | 0.92/0.91 | False |
| 323 | E4_defensive_lead_guard | 17.16/0.80/-13.68 | IS 42.10 | 0.72 | 1.0 | 0.91/0.59 | False |
| 324 | N1_nfl_wind_10_14_under | OOS 294 bets 59.93% ROI +14.32 | IS 930 bets 51.86% ROI -0.99 | 0.0056 | 1.0 | n/a | False |

## Hunt #13 (2026-10-22, research_lab/hunts/h13_top_scorer/): 15m top-scorer (trend+candle+relvol+VWAP rank score), single top name per bar, 90th-pct IS threshold, 1.5xATR stop (filled at bar extreme), 2R, flat by close, 10% size, 7 bps/side (5 fee + 2 slip). 474 names IEX 15m. IS 2024-10-15..2026-03-16, OOS 2026-03-17..2026-10-21. Cumulative N = **327** (324 + 3). 0 pass. PBO 0.708.

| # | Name | OOS trades/win%/avg net bps | OOS ret%/Sh/DD (SPY 15.57/1.90/-5.77; 70/30 10.78/1.90/-4.06) | p | Holm@327 | DSR | SPA vs SPY/70-30 | pass |
|---|---|---|---|---|---|---|---|---|
| 325 | V0_cont | 222/31.53/-44.69 | -9.48/-4.94/-9.28 | 0.9999 | 1.0 | 0.00 | 0.52/0.52 | False |
| 326 | V1_fade | 211/45.50/-5.86 | -1.27/-0.58/-3.16 | 0.662 | 1.0 | 0.00 | 0.93/0.92 | False |
| 327 | V2_cont_no_candle | 180/40.56/-27.55 | -4.89/-2.35/-6.41 | 0.943 | 1.0 | 0.00 | 0.51/0.51 | False |
