N_cumulative: 348  # current; Hunt #15 run 2026-10-22 19:40 ET: 16/16 fail (report hunts/h15_lit4/report.md); (327 + 16 Hunt #15 reserved + 5 Hunt #14)
# history: N was 327  # 310 + h11_nfl_betting 9 + h12_original 5 + h13_top_scorer 3 (0 pass)

## Hunt #16 (h16_supertrend, Herald): rows #349-377 RESERVED (29 pre-registered trials, run crashed: no `arch` in venv; no results yet). Counted in N.

## Hunt #17 (2026-10-22, research_lab/hunts/h17_supertrend_scout/): Supertrend 10/3 variants not in h16 (long/short, +SMA200, +relvol, 1h, top-50, BTC/ETH). 7 bps/side stocks, 20 bps crypto, next-open fills, OOS newest 30%. Cumulative N = **392** (348 + 29 h16 reserved + 15). 0 pass. PBO 0.82.

| # | trial | OOS ret/Sharpe/maxDD | trades | win% | bench same window | twin p | Holm@392 | DSR | SPA bench / 70-30 | pass |
|---|---|---|---|---|---|---|---|---|---|---|
| 378 | H17 T1_SPY_LS | 14.0/0.34/-16.72 | 27 | 25.9 | 75.24 | 0.5389 | 1.0 | 0.0 | 0.938/0.846 | False |
| 379 | H17 T2_QQQ_LS | -9.01/-0.04/-24.15 | 29 | 31.0 | 75.24 | 0.7566 | 1.0 | 0.0 | 0.966/0.919 | False |
| 380 | H17 T3_SPY_SMA200 | 36.16/1.21/-7.57 | 14 | 42.9 | 75.24 | 0.6872 | 1.0 | 0.0 | 0.972/0.796 | False |
| 381 | H17 T4_QQQ_SMA200 | 27.06/0.67/-13.09 | 15 | 46.7 | 75.24 | 0.8326 | 1.0 | 0.0 | 0.971/0.818 | False |
| 382 | H17 T5_BASKET_SMA200 | 45.13/1.0/-10.45 | 142 | 42.3 | 75.24 | 0.975 | 1.0 | 0.0 | 0.867/0.544 | False |
| 383 | H17 T6_SPY_RV | -0.43/-0.07/-2.76 | 1 | 0.0 | 75.24 | 0.6713 | 1.0 | 0.0 | 0.483/0.483 | False |
| 384 | H17 T7_QQQ_RV | 0.0/0/0.0 | 0 | 0 | 75.24 | 1.0 | 1.0 | nan | 0.477/0.477 | False |
| 385 | H17 T8_BASKET_RV | 19.73/1.05/-5.05 | 31 | 48.4 | 75.24 | 0.2944 | 1.0 | 0.0 | 0.491/0.964 | False |
| 386 | H17 T9_SPY_1h | -35.25/-3.74/-35.27 | 302 | 40.4 | 32.47 | 1.0 | 1.0 | 0.0 | 0.493/0.493 | False |
| 387 | H17 T10_QQQ_1h | -32.66/-2.64/-32.59 | 296 | 41.2 | 32.47 | 0.9999 | 1.0 | 0.0 | 0.496/0.499 | False |
| 388 | H17 T11_TOP50_LF | 39.57/1.29/-9.2 | 692 | 43.8 | 75.24 | 0.9624 | 1.0 | 0.0 | 0.52/0.815 | False |
| 389 | H17 T12_BTC_LF | -18.38/-0.34/-37.56 | 8 | 50.0 | -21.74 | 0.5902 | 1.0 | 0.0 | 0.544/None | False |
| 390 | H17 T13_ETH_LF | 60.38/0.82/-49.84 | 6 | 50.0 | -28.62 | 0.1342 | 1.0 | 0.0 | 0.195/None | False |
| 391 | H17 T14_BTC_LS | -31.06/-0.28/-53.71 | 15 | 46.7 | -21.74 | 0.6204 | 1.0 | 0.0 | 0.544/None | False |
| 392 | H17 T15_ETH_LS | 124.06/1.01/-50.74 | 13 | 61.5 | -28.62 | 0.1397 | 1.0 | 0.0 | 0.195/None | False |

N_cumulative: 392  # h16_supertrend #349-377 now logged (0/29 pass); h17 #378-392

## Hunt #16 h16_supertrend (2026-10-23, research_lab/hunts/h16_supertrend/): Supertrend long/flat grid, 5 bps/side, IS 2016-01-04..2023-07-18, OOS 2023-07-19..2026-10-14 (15m OOS 2024-11-27..). #349-377. 0/29 pass. PBO 0.381. Bar applied at N=392.

| # | Name | IS ret/Sh/DD | OOS ret/Sh/DD (SPY 75.24/1.22/-19.77) | twin p | Holm@392 | DSR | SPA vs SPY | pass |
|---|---|---|---|---|---|---|---|---|
| 349 | H16 SPY_7_2 | 79.56/0.73/-16.85 | 28.68/0.87/-11.68 | 0.5172 | 1 | 0.0 | 0.979 | False |
| 350 | H16 SPY_7_3 | 66.61/0.74/-14.23 | 35.6/1.19/-7.52 | 0.3784 | 1 | 0.002 | 0.975 | False |
| 351 | H16 SPY_7_4 | 63.73/0.73/-20.71 | 35.03/1.07/-9.57 | 0.4111 | 1 | 0.001 | 0.491 | False |
| 352 | H16 SPY_10_2 | 103.95/0.86/-17.74 | 29.73/0.87/-13.14 | 0.4745 | 1 | 0.0 | 0.504 | False |
| 353 | H16 SPY_10_3 | 53.83/0.59/-16.06 | 45.83/1.43/-7.52 | 0.1901 | 1 | 0.006 | 0.934 | False |
| 354 | H16 SPY_10_4 | 44.69/0.54/-24.41 | 37.6/1.13/-8.37 | 0.3578 | 1 | 0.001 | 0.972 | False |
| 355 | H16 SPY_14_2 | 91.61/0.79/-21.59 | 32.47/0.93/-13.86 | 0.4286 | 1 | 0.0 | 0.502 | False |
| 356 | H16 SPY_14_3 | 49.64/0.54/-16.91 | 57.96/1.52/-8.27 | 0.064 | 1 | 0.008 | 0.839 | False |
| 357 | H16 SPY_14_4 | 60.61/0.65/-23.9 | 45.99/1.29/-8.53 | 0.2034 | 1 | 0.003 | 0.952 | False |
| 358 | H16 QQQ_7_2 | 124.25/0.82/-26.18 | 46.7/0.96/-12.5 | 0.3025 | 1 | 0.0 | 0.811 | False |
| 359 | H16 QQQ_7_3 | 136.88/0.92/-19.79 | 33.46/0.79/-13.0 | 0.5307 | 1 | 0.0 | 0.945 | False |
| 360 | H16 QQQ_7_4 | 75.31/0.65/-25.54 | 52.35/1.24/-7.98 | 0.271 | 1 | 0.002 | 0.798 | False |
| 361 | H16 QQQ_10_2 | 127.52/0.82/-28.81 | 46.14/0.95/-11.62 | 0.3153 | 1 | 0.0 | 0.831 | False |
| 362 | H16 QQQ_10_3 | 123.68/0.86/-19.79 | 37.53/0.85/-13.0 | 0.4598 | 1 | 0.0 | 0.921 | False |
| 363 | H16 QQQ_10_4 | 91.52/0.73/-25.43 | 60.74/1.28/-12.08 | 0.1754 | 1 | 0.003 | 0.734 | False |
| 364 | H16 QQQ_14_2 | 121.37/0.78/-27.72 | 41.8/0.88/-14.25 | 0.3665 | 1 | 0.0 | 0.853 | False |
| 365 | H16 QQQ_14_3 | 97.12/0.72/-22.64 | 43.55/0.93/-13.0 | 0.3769 | 1 | 0.0 | 0.88 | False |
| 366 | H16 QQQ_14_4 | 104.57/0.76/-28.91 | 61.89/1.3/-12.27 | 0.1716 | 1 | 0.003 | 0.719 | False |
| 367 | H16 BASKET_7_2 | 284.34/1.34/-23.78 | 67.26/1.22/-14.19 | 0.4168 | 1 | 0.002 | 0.632 | False |
| 368 | H16 BASKET_7_3 | 325.66/1.44/-23.11 | 54.29/1.1/-10.4 | 0.7408 | 1 | 0.001 | 0.778 | False |
| 369 | H16 BASKET_7_4 | 315.61/1.44/-22.53 | 54.16/1.07/-14.1 | 0.7665 | 1 | 0.001 | 0.771 | False |
| 370 | H16 BASKET_10_2 | 324.79/1.42/-24.06 | 61.5/1.13/-14.2 | 0.554 | 1 | 0.001 | 0.709 | False |
| 371 | H16 BASKET_10_3 | 321.03/1.42/-22.48 | 58.4/1.16/-11.09 | 0.6587 | 1 | 0.001 | 0.736 | False |
| 372 | H16 BASKET_10_4 | 306.66/1.41/-24.15 | 55.23/1.1/-12.75 | 0.7329 | 1 | 0.001 | 0.757 | False |
| 373 | H16 BASKET_14_2 | 293.24/1.31/-25.32 | 53.33/1.04/-15.17 | 0.7295 | 1 | 0.001 | 0.84 | False |
| 374 | H16 BASKET_14_3 | 339.53/1.45/-22.46 | 59.71/1.16/-13.23 | 0.6225 | 1 | 0.001 | 0.736 | False |
| 375 | H16 BASKET_14_4 | 345.75/1.48/-25.52 | 60.77/1.17/-12.04 | 0.6219 | 1 | 0.001 | 0.7 | False |
| 376 | H16 SPY_15m_10_3 | -44.5/-1.52/-45.03 | -36.8/-3.02/-36.98 | 1.0 | 1 | 0.0 | 0.505 | False |
| 377 | H16 QQQ_15m_10_3 | -43.84/-1.1/-44.92 | -30.58/-1.99/-32.14 | 0.9958 | 1 | 0.0 | 0.502 | False |
  # 327 + 16 reserved for Hunt #15 (h14_lit4 -> h15_lit4, pre-registered, run later) + h14_evidence 5 (0 pass)

## Hunt #14 evidence batch (2026-10-22, research_lab/hunts/h14_evidence/): academic anomalies on daily data (d1_500 survivor-biased, EDGAR XBRL, SEC Form 4), 5 bps/side. IS 2016-01-04..2023-07-18, OOS 2023-07-19..2026-10-14. #328-343 = Hunt #15 (h14_lit4, now folder h15_lit4): reserved, run later (16 pre-registered trials, counted in N). Cumulative N = **348** (327 + 16 reserved + 5). 0 pass. PBO 0.028 (across these 5).

| # | Name | OOS ret%/Sh/DD (SPY 75.24/1.22/-19.77; 70/30 49.27/1.22/-14.19) | random-twin median OOS% | p | Holm@348 | DSR | SPA vs SPY/70-30 | pass |
|---|---|---|---|---|---|---|---|---|
| 328 | H15 C1_stmom_hiturn | IS -41.41% (2646 tr) / OOS -15.97% (1663 tr), WF A -10.96 B -5.01 | - | 0.6068 | 1.0 | - | - | False |
| 329 | H15 C1f_stmom_tv50 | IS -38.63% (2947 tr) / OOS 15.73% (1759 tr), WF A 4.97 B 10.77 | - | 0.1317 | 1.0 | - | - | False |
| 330 | H15 C1f_stmom_sl15 | IS -23.26% (2655 tr) / OOS -9.22% (1639 tr), WF A -7.33 B -1.89 | - | 0.5289 | 1.0 | - | - | False |
| 331 | H15 C1f_stmom_skip5 | IS -56.95% (2608 tr) / OOS 1.08% (1637 tr), WF A 7.56 B -6.48 | - | 0.3333 | 1.0 | - | - | False |
| 332 | H15 C2_vwap_trend_etf | IS -56.54% (4193 tr) / OOS -30.79% (1801 tr), WF A -14.15 B -16.63 | - | 0.5509 | 1.0 | - | - | False |
| 333 | H15 C2f_vwap_buf01 | IS -64.52% (4099 tr) / OOS -40.73% (1755 tr), WF A -19.7 B -21.03 | - | 0.7485 | 1.0 | - | - | False |
| 334 | H15 C2f_vwap_sl05 | IS -68.67% (3957 tr) / OOS -37.92% (1673 tr), WF A -16.8 B -21.12 | - | 0.6487 | 1.0 | - | - | False |
| 335 | H15 C2f_vwap_qqq | IS -35.55% (1008 tr) / OOS -24.88% (439 tr), WF A -13.76 B -11.12 | - | 0.6866 | 1.0 | - | - | False |
| 336 | H15 C3_nfl_high_total_under | IS ROI -1.98% / OOS ROI -0.45% (262 bets), WF A 0.69 B -1.6 | - | 0.3613 | 1.0 | - | - | False |
| 337 | H15 C3f_total_p4 | IS ROI -2.49% / OOS ROI -4.74% (372 bets), WF A -5.48 B -4.01 | - | 0.6747 | 1.0 | - | - | False |
| 338 | H15 C3f_total_p6 | IS ROI 0.87% / OOS ROI 0.31% (178 bets), WF A 1.94 B -1.33 | - | 0.3573 | 1.0 | - | - | False |
| 339 | H15 C3f_total_p7 | IS ROI -1.82% / OOS ROI 3.82% (126 bets), WF A 13.15 B -6.11 | - | 0.2355 | 1.0 | - | - | False |
| 340 | H15 C4_kalshi_fav_80_95 | IS -0.2% / OOS -0.56% (447 bets), WF A -1.62 B 0.42 | - | 0.1657 | 1.0 | - | - | False |
| 341 | H15 C4f_band_70_95 | IS -2.37% / OOS -0.11% (642 bets), WF A -1.92 B 1.55 | - | 0.0479 | 1.0 | - | - | False |
| 342 | H15 C4f_band_85_97 | IS -0.64% / OOS -0.52% (478 bets), WF A -0.73 B -0.31 | - | 0.1657 | 1.0 | - | - | False |
| 343 | H15 C4f_snap_12 | IS -0.31% / OOS 0.5% (398 bets), WF A 1.38 B -0.28 | - | 0.0519 | 1.0 | - | - | False |
| 344 | P1_pead_sue (SUE>=2, hold 60d) | 157.49/1.49/-19.08 | 160.83 | 0.535 | 1.0 | 0.32 | 0.011/0.002 | False |
| 345 | P2_gross_profitability (top quintile GP/A, monthly) | 46.30/0.80/-21.09 | 142.17 | 1.0 | 1.0 | 0.04 | 0.95/0.48 | False |
| 346 | P3_insider_cluster (3+ insiders/30d, hold 21d) | 69.98/0.75/-25.78 (30 OOS events, data ends 2026-03-31) | 34.03 | 0.353 | 1.0 | 0.03 | 0.44/0.21 | False |
| 347 | P4_halloween (SPY Nov-Apr) | 25.42/0.62/-19.77 | 33.74 | 0.752 | 1.0 | 0.02 | 0.50/0.90 | False |
| 348 | P5_october_short (short SPY in Oct) | -2.17/-0.18/-6.52 | -5.70 | 0.297 | 1.0 | 0.00 | 0.49/0.48 | False |

## Engine prereg 20261023_174436_s01_lasthalf_mom_15m_v1 (s01_lasthalf_mom_15m_v1, sha256 96549da34ec9): rows #399-406 RESERVED (8 variants). Counted in N.
N_cumulative: 406

## Engine run 20261023_174436_s01_lasthalf_mom_15m_v1 (s01_lasthalf_mom_15m_v1): rows #399-406. 0/8 pass. PBO 0.254. Bar applied at N=406. Report: engine/runs/20261023_174436_s01_lasthalf_mom_15m_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 399 | HIBETA|sma_cross(fast=2,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | -4.54/-3.54/-5.15 | -2.96 | 756 | 0.0214 | 0.37562 (-6.05) | 1.0 | 0.0 | 0.6115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 400 | HIBETA|sma_cross(fast=2,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -2.16/-2.82/-2.78 | -2.96 | 371 | 0.021 | 0.32867 (-4.11) | 1.0 | 0.0 | 0.5225 | False | oos_positive, walk_forward, holm, dsr, spa |
| 401 | HIBETA|sma_cross(fast=2,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | 1.09/1.63/-0.47 | -2.96 | 223 | 0.0224 | 0.17083 (-3.29) | 1.0 | 0.0015 | 0.3975 | False | holm, dsr, spa |
| 402 | HIBETA|sma_cross(fast=2,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -0.43/-2.1/-0.53 | -2.96 | 93 | 0.02 | 0.27972 (-2.56) | 1.0 | 0.0 | 0.458 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa |
| 403 | HIBETA|sma_cross(fast=4,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | -3.42/-3.09/-4.38 | -2.96 | 758 | 0.0214 | 0.28472 (-5.81) | 1.0 | 0.0 | 0.5625 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 404 | HIBETA|sma_cross(fast=4,slow=13)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -1.98/-2.62/-2.81 | -2.96 | 377 | 0.021 | 0.28871 (-4.01) | 1.0 | 0.0 | 0.516 | False | oos_positive, walk_forward, holm, dsr, spa |
| 405 | HIBETA|sma_cross(fast=4,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.0,n=20) | 0.69/1.06/-0.49 | -2.96 | 219 | 0.0223 | 0.17682 (-3.42) | 1.0 | 0.0008 | 0.4125 | False | walk_forward, holm, dsr, spa |
| 406 | HIBETA|sma_cross(fast=4,slow=26)+session(end=15:30,start=15:15)+relvol(min_ratio=1.5,n=20) | -0.5/-2.18/-0.63 | -2.96 | 94 | 0.0219 | 0.25774 (-3.12) | 1.0 | 0.0 | 0.4595 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 406

## Engine prereg 20261023_174443_s02_reversal_1h_megacap_v1 (s02_reversal_1h_megacap_v1, sha256 00a201c3f45f): rows #407-414 RESERVED (8 variants). Counted in N.
N_cumulative: 414

## Engine run 20261023_174443_s02_reversal_1h_megacap_v1 (s02_reversal_1h_megacap_v1): rows #407-414. 0/8 pass. PBO 1.0. Bar applied at N=414. Report: engine/runs/20261023_174443_s02_reversal_1h_megacap_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 407 | MEGA|rsi_revert(entry=15,exit=50,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97203 (13.23) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 408 | MEGA|rsi_revert(entry=15,exit=50,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98102 (13.2) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 409 | MEGA|rsi_revert(entry=15,exit=70,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97103 (13.42) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 410 | MEGA|rsi_revert(entry=15,exit=70,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.99101 (13.13) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 411 | MEGA|rsi_revert(entry=25,exit=50,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98202 (13.44) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 412 | MEGA|rsi_revert(entry=25,exit=50,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97902 (13.02) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 413 | MEGA|rsi_revert(entry=25,exit=70,n=3)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.97502 (13.09) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 414 | MEGA|rsi_revert(entry=25,exit=70,n=5)+session(end=15:00,start=10:30)+trend_sma(n=200) | 0.0/0.0/0.0 | 26.86 | 0 | inf | 0.98801 (13.13) | 1.0 | 0.0 | 0.888 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 414

## Engine prereg 20261023_174648_s03_volmanaged_trend_v1 (s03_volmanaged_trend_v1, sha256 59fa3cae9a9a): rows #415-441 RESERVED (27 variants). Counted in N.
N_cumulative: 441

## Engine run 20261023_174648_s03_volmanaged_trend_v1 (s03_volmanaged_trend_v1): rows #415-441. 0/27 pass. PBO 0.384. Bar applied at N=441. Report: engine/runs/20261023_174648_s03_volmanaged_trend_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 415 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 33.09/1.2/-7.77 | 84.3 | 55 | 0.023 | 0.49451 (33.62) | 1.0 | 0.5823 | 0.518 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 416 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 35.04/1.13/-12.38 | 84.3 | 56 | 0.0205 | 0.45854 (34.28) | 1.0 | 0.532 | 0.529 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 417 | SPY|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 34.14/0.99/-12.38 | 84.3 | 74 | 0.0193 | 0.45255 (32.78) | 1.0 | 0.4394 | 0.5285 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 418 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 35.83/1.21/-7.47 | 84.3 | 31 | 0.0215 | 0.46853 (35.28) | 1.0 | 0.5853 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 419 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 46.05/1.33/-9.7 | 84.3 | 30 | 0.0191 | 0.25974 (35.19) | 1.0 | 0.6627 | 0.962 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 420 | SPY|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 54.55/1.35/-9.2 | 84.3 | 41 | 0.015 | 0.17483 (34.69) | 1.0 | 0.6759 | 0.9365 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 421 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 38.06/1.23/-7.58 | 84.3 | 23 | 0.0216 | 0.41958 (34.38) | 1.0 | 0.5999 | 0.5125 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 422 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 42.42/1.18/-9.7 | 84.3 | 19 | 0.0176 | 0.2977 (34.25) | 1.0 | 0.5699 | 0.5205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 423 | SPY|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 43.51/1.11/-12.05 | 84.3 | 26 | 0.0149 | 0.37962 (35.21) | 1.0 | 0.5191 | 0.505 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 424 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 40 | 0.0215 | 0.91808 (48.46) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 425 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 42.34/1.17/-10.11 | 132.49 | 39 | 0.0179 | 0.62438 (51.97) | 1.0 | 0.5591 | 0.5115 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 426 | QQQ|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 53.33/1.21/-12.4 | 132.49 | 59 | 0.0155 | 0.42857 (49.4) | 1.0 | 0.5897 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 427 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 32 | 0.0215 | 0.91508 (51.86) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 428 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 31.32/0.88/-12.82 | 132.49 | 25 | 0.0171 | 0.78521 (52.12) | 1.0 | 0.3685 | 0.5125 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 429 | QQQ|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 43.2/0.93/-21.52 | 132.49 | 40 | 0.014 | 0.6014 (51.59) | 1.0 | 0.4014 | 0.5235 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 430 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 10.53/0.54/-6.61 | 132.49 | 29 | 0.0215 | 0.93107 (51.21) | 1.0 | 0.1842 | 0.496 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 431 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 29.41/0.83/-13.71 | 132.49 | 20 | 0.0172 | 0.7962 (52.32) | 1.0 | 0.3391 | 0.5155 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 432 | QQQ|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 59.04/1.14/-18.88 | 132.49 | 19 | 0.0129 | 0.41059 (50.66) | 1.0 | 0.5441 | 0.5205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 433 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.012,n=20) | 2.82/0.36/-3.92 | 53.95 | 293 | 0.0222 | 0.998 (23.22) | 1.0 | 0.109 | 0.49 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 434 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.015,n=20) | 12.12/0.8/-5.15 | 53.95 | 444 | 0.0188 | 0.96703 (22.51) | 1.0 | 0.3156 | 0.501 | False | beats_buy_hold, holm, dsr, spa |
| 435 | SECTORS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.02,n=20) | 8.9/0.45/-10.9 | 53.95 | 613 | 0.0169 | 0.98302 (21.46) | 1.0 | 0.1427 | 0.507 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 436 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.012,n=20) | 1.96/0.25/-3.5 | 53.95 | 229 | 0.0219 | 0.999 (23.25) | 1.0 | 0.0769 | 0.4935 | False | beats_buy_hold, holm, dsr, spa |
| 437 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.015,n=20) | 12.81/0.79/-6.04 | 53.95 | 324 | 0.0181 | 0.92707 (23.48) | 1.0 | 0.3127 | 0.5145 | False | beats_buy_hold, holm, dsr, spa |
| 438 | SECTORS|sma_cross(fast=1,slow=100)+vol_regime(max_atr_pct=0.02,n=20) | 7.42/0.36/-13.39 | 53.95 | 427 | 0.016 | 0.98102 (22.64) | 1.0 | 0.1108 | 0.509 | False | beats_buy_hold, holm, dsr, spa |
| 439 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.012,n=20) | 1.69/0.21/-3.81 | 53.95 | 187 | 0.0217 | 1.0 (23.2) | 1.0 | 0.0693 | 0.492 | False | beats_buy_hold, holm, dsr, spa |
| 440 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.015,n=20) | 13.51/0.81/-6.21 | 53.95 | 260 | 0.0179 | 0.92308 (23.19) | 1.0 | 0.3256 | 0.5075 | False | beats_buy_hold, holm, dsr, spa |
| 441 | SECTORS|sma_cross(fast=1,slow=200)+vol_regime(max_atr_pct=0.02,n=20) | 10.97/0.47/-13.04 | 53.95 | 305 | 0.0157 | 0.94406 (23.01) | 1.0 | 0.1531 | 0.514 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 441

## Engine prereg 20261023_174700_s04_52wk_high_v1 (s04_52wk_high_v1, sha256 95be418d7806): rows #442-450 RESERVED (9 variants). Counted in N.
N_cumulative: 450

## Engine run 20261023_174700_s04_52wk_high_v1 (s04_52wk_high_v1): rows #442-450. 0/9 pass. PBO 0.039. Bar applied at N=450. Report: engine/runs/20261023_174700_s04_52wk_high_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 442 | MEGA|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 39.98/1.27/-9.05 | 287.89 | 180 | 0.0117 | 1.0 (101.45) | 1.0 | 0.5771 | 0.5025 | False | beats_buy_hold, holm, dsr, spa |
| 443 | MEGA|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 60.37/1.46/-12.88 | 287.89 | 108 | 0.0111 | 0.95704 (99.39) | 1.0 | 0.6958 | 0.51 | False | beats_buy_hold, holm, dsr, spa |
| 444 | MEGA|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 69.44/1.4/-16.22 | 287.89 | 212 | 0.0097 | 0.85115 (100.36) | 1.0 | 0.657 | 0.5055 | False | beats_buy_hold, holm, dsr, spa |
| 445 | SECTORS|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 9.4/0.84/-3.23 | 56.34 | 155 | 0.0196 | 0.999 (25.18) | 1.0 | 0.2967 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 446 | SECTORS|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 8.89/0.6/-6.3 | 56.34 | 135 | 0.0177 | 1.0 (25.46) | 1.0 | 0.1724 | 0.5095 | False | beats_buy_hold, holm, dsr, spa |
| 447 | SECTORS|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 12.98/0.71/-7.5 | 56.34 | 163 | 0.015 | 0.98701 (25.23) | 1.0 | 0.2248 | 0.5085 | False | beats_buy_hold, holm, dsr, spa |
| 448 | BROAD|donchian(entry_n=252,exit_n=20)+trend_sma(n=200) | 5.23/0.51/-4.07 | 64.52 | 390 | 0.0142 | 1.0 (28.58) | 1.0 | 0.1347 | 0.5055 | False | beats_buy_hold, holm, dsr, spa |
| 449 | BROAD|donchian(entry_n=252,exit_n=50)+trend_sma(n=200) | 8.71/0.62/-6.75 | 64.52 | 297 | 0.0133 | 1.0 (28.5) | 1.0 | 0.1773 | 0.512 | False | beats_buy_hold, holm, dsr, spa |
| 450 | BROAD|donchian(entry_n=252,exit_n=100)+trend_sma(n=200) | 9.64/0.55/-9.18 | 64.52 | 486 | 0.0123 | 1.0 (27.98) | 1.0 | 0.1524 | 0.5075 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 450

## Engine prereg 20261023_174707_s05_tsmom_crossasset_v1 (s05_tsmom_crossasset_v1, sha256 9c24c49f796a): rows #451-454 RESERVED (4 variants). Counted in N.
N_cumulative: 454

## Engine run 20261023_174707_s05_tsmom_crossasset_v1 (s05_tsmom_crossasset_v1): rows #451-454. 0/4 pass. PBO 0.523. Bar applied at N=454. Report: engine/runs/20261023_174707_s05_tsmom_crossasset_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 451 | REAL|sma_cross(fast=1,slow=126) | 19.78/0.5/-19.44 | 86.94 | 293 | 0.0129 | 0.86314 (34.8) | 1.0 | 0.3687 | 0.49 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 452 | REAL|sma_cross(fast=1,slow=252) | 25.04/0.6/-14.36 | 86.94 | 216 | 0.0132 | 0.78821 (36.17) | 1.0 | 0.4283 | 0.496 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 453 | BONDS_INTL|sma_cross(fast=1,slow=126) | 2.39/0.14/-12.12 | 40.38 | 250 | 0.0215 | 0.98302 (16.56) | 1.0 | 0.1684 | 0.497 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 454 | BONDS_INTL|sma_cross(fast=1,slow=252) | 2.9/0.17/-11.54 | 40.38 | 195 | 0.0218 | 0.99101 (16.95) | 1.0 | 0.1796 | 0.5045 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 454

## Engine prereg 20261023_174711_s06_rsi_revert_15m_hibeta_v1 (s06_rsi_revert_15m_hibeta_v1, sha256 a709691b7cf1): rows #455-458 RESERVED (4 variants). Counted in N.
N_cumulative: 458

## Engine run 20261023_174711_s06_rsi_revert_15m_hibeta_v1 (s06_rsi_revert_15m_hibeta_v1): rows #455-458. 0/4 pass. PBO 1.0. Bar applied at N=458. Report: engine/runs/20261023_174711_s06_rsi_revert_15m_hibeta_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 455 | HIBETA|rsi_revert(entry=10,exit=50,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.25375 (-2.51) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 456 | HIBETA|rsi_revert(entry=10,exit=70,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.26274 (-2.34) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 457 | HIBETA|rsi_revert(entry=20,exit=50,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.28871 (-2.15) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 458 | HIBETA|rsi_revert(entry=20,exit=70,n=3)+session(end=15:30,start=10:00)+trend_sma(n=200) | 0.0/0.0/0.0 | -2.96 | 0 | inf | 0.29171 (-2.17) | 1.0 | 0.0 | 0.442 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 458

## Engine prereg 20261023_174713_c01_sol_trend_ma_v1 (c01_sol_trend_ma_v1, sha256 c206eaae0dfd): rows #459-466 RESERVED (8 variants). Counted in N.
N_cumulative: 466

## Engine run 20261023_174713_c01_sol_trend_ma_v1 (c01_sol_trend_ma_v1): rows #459-466. 0/8 pass. PBO 0.271. Bar applied at N=466. Report: engine/runs/20261023_174713_c01_sol_trend_ma_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 459 | SOL|sma_cross(fast=1,slow=50) | 26.19/0.47/-34.46 | 923.45 | 34 | 0.0164 | 0.63636 (123.59) | 1.0 | 0.0689 | 0.8805 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 460 | SOL|sma_cross(fast=1,slow=100) | -47.8/-0.59/-54.45 | 923.45 | 35 | 0.0171 | 0.98601 (98.82) | 1.0 | 0.0016 | 0.9235 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 461 | SOL|sma_cross(fast=10,slow=50) | 29.55/0.5/-41.34 | 923.45 | 13 | 0.0199 | 0.69231 (248.32) | 1.0 | 0.0773 | 0.8685 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 462 | SOL|sma_cross(fast=10,slow=100) | -51.41/-0.68/-62.14 | 923.45 | 13 | 0.019 | 0.98901 (266.75) | 1.0 | 0.0009 | 0.9205 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 463 | ALTS|sma_cross(fast=1,slow=50) | 2.71/0.23/-39.86 | 193.2 | 320 | 0.0199 | 0.78222 (59.97) | 1.0 | 0.0352 | 0.9085 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 464 | ALTS|sma_cross(fast=1,slow=100) | 9.48/0.31/-39.82 | 193.2 | 241 | 0.0208 | 0.73826 (54.83) | 1.0 | 0.0471 | 0.891 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 465 | ALTS|sma_cross(fast=10,slow=50) | 30.79/0.52/-33.03 | 193.2 | 128 | 0.0214 | 0.66733 (74.29) | 1.0 | 0.0837 | 0.866 | False | beats_buy_hold, holm, dsr, spa |
| 466 | ALTS|sma_cross(fast=10,slow=100) | 13.73/0.36/-44.98 | 193.2 | 89 | 0.0219 | 0.77822 (90.12) | 1.0 | 0.0541 | 0.887 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 466

## Engine prereg 20261023_174716_c02_sol_breakout_v1 (c02_sol_breakout_v1, sha256 d7576baa60a5): rows #467-474 RESERVED (8 variants). Counted in N.
N_cumulative: 474

## Engine run 20261023_174716_c02_sol_breakout_v1 (c02_sol_breakout_v1): rows #467-474. 0/8 pass. PBO 0.805. Bar applied at N=474. Report: engine/runs/20261023_174716_c02_sol_breakout_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 467 | SOL|donchian(entry_n=20,exit_n=10) | -10.12/0.03/-42.44 | 923.45 | 18 | 0.0192 | 0.85115 (158.46) | 1.0 | 0.0527 | 0.903 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 468 | SOL|donchian(entry_n=20,exit_n=20) | 11.9/0.33/-53.02 | 923.45 | 12 | 0.0187 | 0.71029 (103.17) | 1.0 | 0.1178 | 0.8945 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 469 | SOL|donchian(entry_n=55,exit_n=10) | -38.03/-0.67/-56.72 | 923.45 | 11 | 0.0217 | 0.96404 (385.31) | 1.0 | 0.0043 | 0.9175 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 470 | SOL|donchian(entry_n=55,exit_n=20) | -31.81/-0.32/-63.28 | 923.45 | 8 | 0.0212 | 0.93107 (113.78) | 1.0 | 0.0173 | 0.9155 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 471 | ALTS|donchian(entry_n=20,exit_n=10) | -2.08/0.13/-38.54 | 193.2 | 129 | 0.023 | 0.87213 (73.74) | 1.0 | 0.0702 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 472 | ALTS|donchian(entry_n=20,exit_n=20) | 11.19/0.33/-42.24 | 193.2 | 94 | 0.0225 | 0.80719 (84.95) | 1.0 | 0.1177 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 473 | ALTS|donchian(entry_n=55,exit_n=10) | 8.73/0.28/-41.93 | 193.2 | 76 | 0.0242 | 0.81419 (78.92) | 1.0 | 0.1062 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 474 | ALTS|donchian(entry_n=55,exit_n=20) | 19.27/0.42/-40.35 | 193.2 | 62 | 0.0243 | 0.71029 (91.93) | 1.0 | 0.1489 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 474

## Engine prereg 20261023_174720_c03_sol_drop_revert_v1 (c03_sol_drop_revert_v1, sha256 6822eb6ee5a3): rows #475-482 RESERVED (8 variants). Counted in N.
N_cumulative: 482

## Engine run 20261023_174720_c03_sol_drop_revert_v1 (c03_sol_drop_revert_v1): rows #475-482. 0/8 pass. PBO 0.638. Bar applied at N=482. Report: engine/runs/20261023_174720_c03_sol_drop_revert_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 475 | SOL|drop_revert(drop=0.15,hold=3,n=3) | 10.9/0.46/-10.19 | 923.45 | 28 | 0.0106 | 0.59241 (54.4) | 1.0 | 0.3798 | 0.881 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 476 | SOL|drop_revert(drop=0.15,hold=7,n=3) | 6.67/0.25/-33.8 | 923.45 | 22 | 0.0123 | 0.65634 (69.99) | 1.0 | 0.2768 | 0.8795 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 477 | SOL|drop_revert(drop=0.25,hold=3,n=3) | 0.0/0.0/0.0 | 923.45 | 6 | 0.0078 | 1.0 (0.0) | 1.0 | 0.0 | 0.8915 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 478 | SOL|drop_revert(drop=0.25,hold=7,n=3) | 0.0/0.0/0.0 | 923.45 | 6 | 0.0078 | 1.0 (919.87) | 1.0 | 0.0 | 0.8915 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 479 | ALTS|drop_revert(drop=0.15,hold=3,n=3) | 14.41/0.5/-11.46 | 193.2 | 170 | 0.0119 | 0.75824 (72.15) | 1.0 | 0.4079 | 0.88 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 480 | ALTS|drop_revert(drop=0.15,hold=7,n=3) | 14.27/0.4/-18.64 | 193.2 | 148 | 0.0126 | 0.74426 (89.61) | 1.0 | 0.357 | 0.8785 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 481 | ALTS|drop_revert(drop=0.25,hold=3,n=3) | 3.12/0.61/-1.65 | 193.2 | 31 | 0.0082 | 0.97902 (40.51) | 1.0 | 0.4712 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 482 | ALTS|drop_revert(drop=0.25,hold=7,n=3) | -0.04/0.01/-5.18 | 193.2 | 29 | 0.0089 | 0.99101 (38.02) | 1.0 | 0.1759 | 0.8995 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 482

## Engine prereg 20261023_174723_c04_sol_rel_strength_v1 (c04_sol_rel_strength_v1, sha256 9bbe700d9155): rows #483-490 RESERVED (8 variants). Counted in N.
N_cumulative: 490

## Engine run 20261023_174723_c04_sol_rel_strength_v1 (c04_sol_rel_strength_v1): rows #483-490. 0/8 pass. PBO 0.159. Bar applied at N=490. Report: engine/runs/20261023_174723_c04_sol_rel_strength_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 483 | SOL|rel_strength(abs_filter=True,bench=BTC/USD,n=14) | -27.12/-0.3/-41.62 | 923.45 | 68 | 0.0165 | 0.85614 (106.2) | 1.0 | 0.0344 | 0.9135 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 484 | SOL|rel_strength(abs_filter=True,bench=BTC/USD,n=30) | 19.64/0.41/-26.52 | 923.45 | 47 | 0.0174 | 0.63337 (179.46) | 1.0 | 0.2096 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 485 | SOL|rel_strength(abs_filter=True,bench=ETH/USD,n=14) | -30.9/-0.39/-38.78 | 923.45 | 67 | 0.0159 | 0.90509 (167.45) | 1.0 | 0.028 | 0.916 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 486 | SOL|rel_strength(abs_filter=True,bench=ETH/USD,n=30) | 19.58/0.42/-33.83 | 923.45 | 40 | 0.0161 | 0.62537 (75.69) | 1.0 | 0.2108 | 0.885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 487 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=14) | -12.55/-0.07/-32.22 | 193.2 | 524 | 0.0197 | 0.86613 (47.01) | 1.0 | 0.0688 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 488 | ALTS|rel_strength(abs_filter=True,bench=BTC/USD,n=30) | 10.2/0.3/-30.23 | 193.2 | 365 | 0.0205 | 0.72228 (60.74) | 1.0 | 0.1719 | 0.899 | False | beats_buy_hold, holm, dsr, spa |
| 489 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=14) | -12.07/-0.15/-30.96 | 193.2 | 430 | 0.0186 | 0.88711 (45.61) | 1.0 | 0.0557 | 0.9055 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 490 | ALTS|rel_strength(abs_filter=True,bench=ETH/USD,n=30) | -7.13/-0.01/-39.19 | 193.2 | 284 | 0.0193 | 0.84715 (54.66) | 1.0 | 0.0807 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

N_cumulative: 490

## Engine prereg 20261023_174727_c05_crypto_tsmom_short_v1 (c05_crypto_tsmom_short_v1, sha256 eae14d8ec9b6): rows #491-499 RESERVED (9 variants). Counted in N.
N_cumulative: 499

## Engine run 20261023_174727_c05_crypto_tsmom_short_v1 (c05_crypto_tsmom_short_v1): rows #491-499. 0/9 pass. PBO 0.653. Bar applied at N=499. Report: engine/runs/20261023_174727_c05_crypto_tsmom_short_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 491 | SOL|sma_cross(fast=1,slow=7) | 3.78/0.25/-51.44 | 923.45 | 138 | 0.0152 | 0.62637 (122.97) | 1.0 | 0.1591 | 0.897 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 492 | SOL|sma_cross(fast=1,slow=14) | 8.0/0.3/-35.02 | 923.45 | 87 | 0.015 | 0.69031 (222.82) | 1.0 | 0.1753 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 493 | SOL|sma_cross(fast=1,slow=28) | 37.74/0.58/-31.95 | 923.45 | 71 | 0.0162 | 0.58342 (124.71) | 1.0 | 0.2942 | 0.8575 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 494 | ALTS|sma_cross(fast=1,slow=7) | -13.95/0.01/-51.71 | 193.2 | 1044 | 0.0183 | 0.6963 (16.26) | 1.0 | 0.088 | 0.924 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 495 | ALTS|sma_cross(fast=1,slow=14) | 2.88/0.23/-49.52 | 193.2 | 672 | 0.0187 | 0.67632 (40.37) | 1.0 | 0.1512 | 0.9105 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 496 | ALTS|sma_cross(fast=1,slow=28) | 22.05/0.44/-36.46 | 193.2 | 464 | 0.0192 | 0.5994 (52.32) | 1.0 | 0.2336 | 0.871 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 497 | BTC_ETH|sma_cross(fast=1,slow=7) | -26.24/-0.36/-46.71 | 56.21 | 390 | 0.0276 | 0.6953 (-17.13) | 1.0 | 0.0311 | 0.503 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 498 | BTC_ETH|sma_cross(fast=1,slow=14) | 5.1/0.23/-40.98 | 56.21 | 246 | 0.0272 | 0.4006 (-1.34) | 1.0 | 0.1476 | 0.951 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 499 | BTC_ETH|sma_cross(fast=1,slow=28) | 39.53/0.69/-28.78 | 56.21 | 145 | 0.0283 | 0.17782 (10.98) | 1.0 | 0.3502 | 0.7815 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 499

## Engine prereg 20261023_174731_c06_crypto_trend_volregime_v1 (c06_crypto_trend_volregime_v1, sha256 6a9680145e3e): rows #500-511 RESERVED (12 variants). Counted in N.
N_cumulative: 511

## Engine run 20261023_174731_c06_crypto_trend_volregime_v1 (c06_crypto_trend_volregime_v1): rows #500-511. 0/12 pass. PBO 0.762. Bar applied at N=511. Report: engine/runs/20261023_174731_c06_crypto_trend_volregime_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 500 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | 33.29/0.98/-11.19 | 923.45 | 3 | 0.0284 | 0.56643 (50.48) | 1.0 | 0.2324 | 0.869 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 501 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | 78.15/1.01/-29.54 | 923.45 | 22 | 0.0182 | 0.58042 (301.2) | 1.0 | 0.2542 | 0.8275 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 502 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | 23.52/0.77/-11.19 | 923.45 | 3 | 0.0286 | 0.61838 (56.47) | 1.0 | 0.1459 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 503 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 67.61/0.84/-42.1 | 923.45 | 24 | 0.0181 | 0.58641 (298.0) | 1.0 | 0.1789 | 0.8275 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 504 | ALTS|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | -5.27/-0.25/-12.37 | 193.2 | 70 | 0.0289 | 0.98501 (66.15) | 1.0 | 0.007 | 0.9015 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 505 | ALTS|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | 15.74/0.38/-29.19 | 193.2 | 182 | 0.0186 | 0.73127 (85.39) | 1.0 | 0.0598 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 506 | ALTS|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | -2.39/-0.11/-10.41 | 193.2 | 67 | 0.0286 | 0.97303 (110.85) | 1.0 | 0.0117 | 0.9045 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 507 | ALTS|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 8.43/0.28/-32.23 | 193.2 | 179 | 0.0182 | 0.79121 (80.11) | 1.0 | 0.0466 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 508 | BTC_ETH|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | -16.54/-0.23/-31.68 | 56.21 | 71 | 0.0288 | 0.8991 (16.7) | 1.0 | 0.0083 | 0.4895 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 509 | BTC_ETH|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | -5.2/0.05/-31.89 | 56.21 | 49 | 0.0305 | 0.8042 (21.73) | 1.0 | 0.022 | 0.9685 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 510 | BTC_ETH|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | -9.87/-0.12/-26.77 | 56.21 | 68 | 0.0287 | 0.85714 (21.92) | 1.0 | 0.012 | 0.957 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 511 | BTC_ETH|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 5.99/0.24/-26.34 | 56.21 | 42 | 0.0276 | 0.66234 (24.41) | 1.0 | 0.0403 | 0.923 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 511

## Engine prereg 20261023_174736_c07_ma_cross_grid_v1 (c07_ma_cross_grid_v1, sha256 b004aa9de9eb): rows #512-535 RESERVED (24 variants). Counted in N.
N_cumulative: 535

## Engine run 20261023_174736_c07_ma_cross_grid_v1 (c07_ma_cross_grid_v1): rows #512-535. 0/24 pass. PBO 0.687. Bar applied at N=535. Report: engine/runs/20261023_174736_c07_ma_cross_grid_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 512 | ALTS|sma_cross(fast=5,slow=50) | 6.66/0.28/-40.5 | 193.2 | 157 | 0.0209 | 0.8022 (73.91) | 1.0 | 0.3826 | 0.897 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 513 | ALTS|sma_cross(fast=5,slow=100) | -2.07/0.18/-47.59 | 193.2 | 116 | 0.0218 | 0.86813 (76.56) | 1.0 | 0.3342 | 0.899 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 514 | ALTS|sma_cross(fast=5,slow=150) | 24.69/0.47/-36.4 | 193.2 | 75 | 0.0226 | 0.66434 (69.77) | 1.0 | 0.4911 | 0.872 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 515 | ALTS|sma_cross(fast=5,slow=200) | 0.5/0.2/-39.58 | 193.2 | 54 | 0.0208 | 0.87213 (63.59) | 1.0 | 0.3442 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 516 | ALTS|sma_cross(fast=10,slow=50) | 30.79/0.52/-33.03 | 193.2 | 128 | 0.0214 | 0.66833 (89.85) | 1.0 | 0.5226 | 0.866 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 517 | ALTS|sma_cross(fast=10,slow=100) | 13.73/0.36/-44.98 | 193.2 | 89 | 0.0219 | 0.77922 (74.22) | 1.0 | 0.43 | 0.887 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 518 | ALTS|sma_cross(fast=10,slow=150) | 7.61/0.29/-38.27 | 193.2 | 54 | 0.0226 | 0.81219 (70.51) | 1.0 | 0.3917 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 519 | ALTS|sma_cross(fast=10,slow=200) | -5.76/0.13/-43.58 | 193.2 | 47 | 0.0206 | 0.90909 (68.81) | 1.0 | 0.3038 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 520 | ALTS|sma_cross(fast=20,slow=50) | 19.28/0.41/-39.76 | 193.2 | 106 | 0.0212 | 0.71229 (72.47) | 1.0 | 0.4587 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 521 | ALTS|sma_cross(fast=20,slow=100) | 7.3/0.29/-46.27 | 193.2 | 69 | 0.0214 | 0.81419 (79.16) | 1.0 | 0.3935 | 0.8965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 522 | ALTS|sma_cross(fast=20,slow=150) | -0.4/0.2/-43.38 | 193.2 | 49 | 0.0216 | 0.86513 (78.68) | 1.0 | 0.342 | 0.908 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 523 | ALTS|sma_cross(fast=20,slow=200) | -12.71/0.03/-42.85 | 193.2 | 38 | 0.0198 | 0.92408 (76.84) | 1.0 | 0.2559 | 0.918 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 524 | BTC_ETH|sma_cross(fast=5,slow=50) | 13.17/0.35/-32.47 | 56.21 | 55 | 0.031 | 0.52448 (19.83) | 1.0 | 0.4214 | 0.888 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 525 | BTC_ETH|sma_cross(fast=5,slow=100) | 39.49/0.68/-22.66 | 56.21 | 31 | 0.0313 | 0.32967 (23.44) | 1.0 | 0.6152 | 0.7275 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 526 | BTC_ETH|sma_cross(fast=5,slow=150) | 18.73/0.41/-30.36 | 56.21 | 20 | 0.0331 | 0.54645 (22.69) | 1.0 | 0.4603 | 0.866 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 527 | BTC_ETH|sma_cross(fast=5,slow=200) | 2.44/0.2/-35.77 | 56.21 | 19 | 0.0327 | 0.71628 (23.18) | 1.0 | 0.3388 | 0.9325 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 528 | BTC_ETH|sma_cross(fast=10,slow=50) | 15.01/0.37/-28.88 | 56.21 | 46 | 0.031 | 0.50849 (21.4) | 1.0 | 0.4364 | 0.866 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 529 | BTC_ETH|sma_cross(fast=10,slow=100) | 19.08/0.43/-28.67 | 56.21 | 26 | 0.0331 | 0.50949 (25.4) | 1.0 | 0.4682 | 0.841 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 530 | BTC_ETH|sma_cross(fast=10,slow=150) | 25.14/0.49/-27.97 | 56.21 | 17 | 0.0366 | 0.48452 (23.95) | 1.0 | 0.5053 | 0.833 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 531 | BTC_ETH|sma_cross(fast=10,slow=200) | 5.32/0.24/-35.36 | 56.21 | 15 | 0.0366 | 0.68631 (22.24) | 1.0 | 0.3602 | 0.9275 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 532 | BTC_ETH|sma_cross(fast=20,slow=50) | 31.39/0.6/-31.31 | 56.21 | 39 | 0.0314 | 0.34565 (23.69) | 1.0 | 0.5702 | 0.805 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 533 | BTC_ETH|sma_cross(fast=20,slow=100) | 25.69/0.51/-30.04 | 56.21 | 22 | 0.0361 | 0.47053 (24.4) | 1.0 | 0.5175 | 0.807 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 534 | BTC_ETH|sma_cross(fast=20,slow=150) | 21.96/0.45/-32.33 | 56.21 | 14 | 0.0327 | 0.51349 (26.15) | 1.0 | 0.4834 | 0.8585 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 535 | BTC_ETH|sma_cross(fast=20,slow=200) | 9.4/0.29/-30.9 | 56.21 | 12 | 0.0301 | 0.61838 (26.67) | 1.0 | 0.3921 | 0.9095 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 535

## Engine prereg 20261023_174743_c08_donchian_grid_v1 (c08_donchian_grid_v1, sha256 fe617f96081f): rows #536-559 RESERVED (24 variants). Counted in N.
N_cumulative: 559

## Engine run 20261023_174743_c08_donchian_grid_v1 (c08_donchian_grid_v1): rows #536-559. 0/24 pass. PBO 0.821. Bar applied at N=559. Report: engine/runs/20261023_174743_c08_donchian_grid_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 536 | ALTS|donchian(entry_n=10,exit_n=5) | 85.77/0.63/-41.94 | 193.2 | 228 | 0.0204 | 0.44456 (75.63) | 1.0 | 0.5087 | 0.9355 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 537 | ALTS|donchian(entry_n=10,exit_n=10) | 71.02/0.59/-49.18 | 193.2 | 191 | 0.0205 | 0.46853 (66.74) | 1.0 | 0.4755 | 0.964 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 538 | ALTS|donchian(entry_n=10,exit_n=20) | 90.56/0.66/-53.98 | 193.2 | 135 | 0.0196 | 0.44655 (82.21) | 1.0 | 0.531 | 0.9695 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 539 | ALTS|donchian(entry_n=20,exit_n=5) | 7.97/0.27/-29.0 | 193.2 | 147 | 0.0229 | 0.80519 (67.87) | 1.0 | 0.3075 | 0.889 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 540 | ALTS|donchian(entry_n=20,exit_n=10) | -2.08/0.13/-38.54 | 193.2 | 129 | 0.023 | 0.88511 (75.87) | 1.0 | 0.2403 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 541 | ALTS|donchian(entry_n=20,exit_n=20) | 11.19/0.33/-42.24 | 193.2 | 94 | 0.0225 | 0.78821 (66.43) | 1.0 | 0.3375 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 542 | ALTS|donchian(entry_n=30,exit_n=5) | 7.68/0.27/-27.46 | 193.2 | 123 | 0.0235 | 0.81918 (70.52) | 1.0 | 0.3049 | 0.8915 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 543 | ALTS|donchian(entry_n=30,exit_n=10) | 2.39/0.19/-35.16 | 193.2 | 108 | 0.0235 | 0.85415 (63.3) | 1.0 | 0.2664 | 0.8995 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 544 | ALTS|donchian(entry_n=30,exit_n=20) | 15.82/0.38/-35.78 | 193.2 | 83 | 0.0236 | 0.76124 (78.06) | 1.0 | 0.3634 | 0.888 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 545 | ALTS|donchian(entry_n=55,exit_n=5) | 10.13/0.32/-35.07 | 193.2 | 85 | 0.024 | 0.82118 (88.48) | 1.0 | 0.332 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 546 | ALTS|donchian(entry_n=55,exit_n=10) | 8.73/0.28/-41.93 | 193.2 | 76 | 0.0242 | 0.84116 (85.3) | 1.0 | 0.3155 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 547 | ALTS|donchian(entry_n=55,exit_n=20) | 19.27/0.42/-40.35 | 193.2 | 62 | 0.0243 | 0.68531 (78.49) | 1.0 | 0.3906 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 548 | BTC_ETH|donchian(entry_n=10,exit_n=5) | 21.51/0.48/-25.3 | 56.21 | 87 | 0.0303 | 0.41359 (16.12) | 1.0 | 0.4207 | 0.8435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 549 | BTC_ETH|donchian(entry_n=10,exit_n=10) | 19.21/0.43/-25.24 | 56.21 | 66 | 0.0301 | 0.46953 (18.21) | 1.0 | 0.3904 | 0.873 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 550 | BTC_ETH|donchian(entry_n=10,exit_n=20) | 22.07/0.45/-34.3 | 56.21 | 48 | 0.0273 | 0.46254 (20.52) | 1.0 | 0.4011 | 0.8875 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 551 | BTC_ETH|donchian(entry_n=20,exit_n=5) | 0.67/0.12/-21.31 | 56.21 | 61 | 0.0313 | 0.72328 (17.07) | 1.0 | 0.2342 | 0.9065 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 552 | BTC_ETH|donchian(entry_n=20,exit_n=10) | -0.24/0.12/-24.85 | 56.21 | 48 | 0.0312 | 0.71728 (17.85) | 1.0 | 0.2345 | 0.914 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 553 | BTC_ETH|donchian(entry_n=20,exit_n=20) | 19.32/0.44/-27.22 | 56.21 | 34 | 0.0309 | 0.5015 (21.53) | 1.0 | 0.3962 | 0.857 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 554 | BTC_ETH|donchian(entry_n=30,exit_n=5) | 7.09/0.27/-16.44 | 56.21 | 52 | 0.0316 | 0.67632 (21.54) | 1.0 | 0.3056 | 0.871 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 555 | BTC_ETH|donchian(entry_n=30,exit_n=10) | 11.43/0.34/-19.28 | 56.21 | 41 | 0.0316 | 0.61538 (21.66) | 1.0 | 0.3443 | 0.8725 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 556 | BTC_ETH|donchian(entry_n=30,exit_n=20) | 26.93/0.57/-21.98 | 56.21 | 30 | 0.0316 | 0.40659 (24.44) | 1.0 | 0.4736 | 0.8285 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 557 | BTC_ETH|donchian(entry_n=55,exit_n=5) | 19.35/0.57/-14.87 | 56.21 | 36 | 0.0305 | 0.52148 (20.86) | 1.0 | 0.4693 | 0.825 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 558 | BTC_ETH|donchian(entry_n=55,exit_n=10) | 34.69/0.78/-15.5 | 56.21 | 28 | 0.0305 | 0.38561 (24.24) | 1.0 | 0.5945 | 0.761 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 559 | BTC_ETH|donchian(entry_n=55,exit_n=20) | 41.64/0.84/-15.22 | 56.21 | 24 | 0.0305 | 0.3017 (23.12) | 1.0 | 0.6317 | 0.7325 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 559

## Engine prereg 20261023_174750_c09_supertrend_trail_v1 (c09_supertrend_trail_v1, sha256 dac9565cc0b8): rows #560-577 RESERVED (18 variants). Counted in N.
N_cumulative: 577

## Engine run 20261023_174750_c09_supertrend_trail_v1 (c09_supertrend_trail_v1): rows #560-577. 0/18 pass. PBO 0.477. Bar applied at N=577. Report: engine/runs/20261023_174750_c09_supertrend_trail_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 560 | ALTS|supertrend(atr_n=7,mult=2) | -4.89/0.12/-42.35 | 193.2 | 190 | 0.0206 | 0.88711 (64.3) | 1.0 | 0.3841 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 561 | ALTS|supertrend(atr_n=7,mult=3) | -1.43/0.16/-37.09 | 193.2 | 118 | 0.0222 | 0.89211 (70.89) | 1.0 | 0.4039 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 562 | ALTS|supertrend(atr_n=7,mult=4) | -5.06/0.15/-41.76 | 193.2 | 80 | 0.023 | 0.92607 (74.33) | 1.0 | 0.3979 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 563 | ALTS|supertrend(atr_n=10,mult=2) | -2.0/0.16/-41.88 | 193.2 | 189 | 0.0208 | 0.87612 (70.1) | 1.0 | 0.4035 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 564 | ALTS|supertrend(atr_n=10,mult=3) | -8.59/0.06/-39.37 | 193.2 | 119 | 0.0217 | 0.93606 (70.8) | 1.0 | 0.3486 | 0.9085 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 565 | ALTS|supertrend(atr_n=10,mult=4) | -0.69/0.19/-40.57 | 193.2 | 77 | 0.0236 | 0.84915 (59.96) | 1.0 | 0.4191 | 0.906 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 566 | ALTS|supertrend(atr_n=14,mult=2) | 10.4/0.31/-36.19 | 193.2 | 187 | 0.0208 | 0.77223 (70.68) | 1.0 | 0.4908 | 0.8965 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 567 | ALTS|supertrend(atr_n=14,mult=3) | -6.62/0.08/-37.93 | 193.2 | 117 | 0.022 | 0.94106 (77.01) | 1.0 | 0.3586 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 568 | ALTS|supertrend(atr_n=14,mult=4) | 0.2/0.19/-40.8 | 193.2 | 75 | 0.0236 | 0.86114 (67.52) | 1.0 | 0.4214 | 0.904 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 569 | BTC_ETH|supertrend(atr_n=7,mult=2) | 8.04/0.27/-28.88 | 56.21 | 79 | 0.03 | 0.61139 (16.02) | 1.0 | 0.466 | 0.9105 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 570 | BTC_ETH|supertrend(atr_n=7,mult=3) | 4.72/0.22/-30.66 | 56.21 | 43 | 0.0313 | 0.72228 (22.49) | 1.0 | 0.4348 | 0.92 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 571 | BTC_ETH|supertrend(atr_n=7,mult=4) | 7.4/0.26/-27.05 | 56.21 | 31 | 0.0311 | 0.63137 (22.85) | 1.0 | 0.4608 | 0.909 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 572 | BTC_ETH|supertrend(atr_n=10,mult=2) | 8.27/0.27/-31.54 | 56.21 | 77 | 0.03 | 0.61239 (15.81) | 1.0 | 0.4682 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 573 | BTC_ETH|supertrend(atr_n=10,mult=3) | -5.2/0.05/-31.89 | 56.21 | 44 | 0.0312 | 0.80519 (20.96) | 1.0 | 0.3455 | 0.9685 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 574 | BTC_ETH|supertrend(atr_n=10,mult=4) | 5.99/0.24/-26.34 | 56.21 | 30 | 0.0317 | 0.70529 (24.13) | 1.0 | 0.4477 | 0.923 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 575 | BTC_ETH|supertrend(atr_n=14,mult=2) | 17.89/0.42/-28.28 | 56.21 | 76 | 0.03 | 0.49151 (18.3) | 1.0 | 0.553 | 0.858 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 576 | BTC_ETH|supertrend(atr_n=14,mult=3) | 0.16/0.15/-33.06 | 56.21 | 45 | 0.0306 | 0.76923 (22.19) | 1.0 | 0.3959 | 0.954 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 577 | BTC_ETH|supertrend(atr_n=14,mult=4) | 16.88/0.41/-25.78 | 56.21 | 26 | 0.0311 | 0.58541 (24.35) | 1.0 | 0.5491 | 0.8905 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 577

## Engine prereg 20261023_174757_c10_btc_gated_trend_v1 (c10_btc_gated_trend_v1, sha256 1b5c39c46314): rows #578-595 RESERVED (18 variants). Counted in N.
N_cumulative: 595

## Engine run 20261023_174757_c10_btc_gated_trend_v1 (c10_btc_gated_trend_v1): rows #578-595. 0/18 pass. PBO 0.3. Bar applied at N=595. Report: engine/runs/20261023_174757_c10_btc_gated_trend_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 578 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=50) | 32.32/0.57/-41.23 | 193.2 | 583 | 0.0204 | 0.52048 (39.72) | 1.0 | 0.2939 | 0.8595 | False | beats_buy_hold, holm, dsr, spa |
| 579 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=100) | 15.21/0.37/-44.09 | 193.2 | 562 | 0.0207 | 0.55045 (29.46) | 1.0 | 0.2023 | 0.8885 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 580 | ALTS|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=200) | -23.69/-0.18/-60.16 | 193.2 | 561 | 0.0203 | 0.91309 (36.46) | 1.0 | 0.051 | 0.925 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 581 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=50) | 34.33/0.58/-30.76 | 193.2 | 411 | 0.0205 | 0.56444 (62.13) | 1.0 | 0.2985 | 0.8495 | False | beats_buy_hold, holm, dsr, spa |
| 582 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=100) | 17.12/0.39/-37.02 | 193.2 | 372 | 0.021 | 0.66134 (77.0) | 1.0 | 0.2125 | 0.8805 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 583 | ALTS|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=200) | -2.28/0.15/-44.35 | 193.2 | 358 | 0.0205 | 0.78621 (54.57) | 1.0 | 0.1269 | 0.9085 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 584 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=50) | 2.52/0.22/-37.73 | 193.2 | 319 | 0.0205 | 0.78821 (59.72) | 1.0 | 0.1464 | 0.9045 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 585 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=100) | -5.0/0.13/-42.19 | 193.2 | 277 | 0.0213 | 0.82118 (67.49) | 1.0 | 0.1184 | 0.9145 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 586 | ALTS|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=200) | -4.3/0.14/-41.09 | 193.2 | 238 | 0.0206 | 0.83716 (80.01) | 1.0 | 0.1211 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 587 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=50) | 15.97/0.41/-25.85 | 56.21 | 207 | 0.0291 | 0.2977 (0.99) | 1.0 | 0.2136 | 0.8605 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 588 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=100) | 3.74/0.19/-30.62 | 56.21 | 204 | 0.0303 | 0.40759 (-2.89) | 1.0 | 0.136 | 0.9195 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 589 | BTC_ETH|sma_cross(fast=1,slow=10)+bench_trend(bench=BTC/USD,n=200) | -29.31/-0.48/-48.34 | 56.21 | 207 | 0.0302 | 0.87812 (-6.08) | 1.0 | 0.0207 | 0.4905 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 590 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=50) | 21.37/0.47/-25.23 | 56.21 | 148 | 0.0284 | 0.33467 (8.25) | 1.0 | 0.2392 | 0.8425 | False | beats_buy_hold, holm, dsr, spa |
| 591 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=100) | 18.88/0.43/-24.94 | 56.21 | 134 | 0.0291 | 0.37063 (8.96) | 1.0 | 0.2226 | 0.8625 | False | beats_buy_hold, holm, dsr, spa |
| 592 | BTC_ETH|sma_cross(fast=1,slow=20)+bench_trend(bench=BTC/USD,n=200) | 11.58/0.32/-36.18 | 56.21 | 129 | 0.0295 | 0.42458 (6.74) | 1.0 | 0.1798 | 0.9225 | False | beats_buy_hold, holm, dsr, spa |
| 593 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=50) | 36.49/0.67/-24.69 | 56.21 | 103 | 0.0292 | 0.22977 (12.37) | 1.0 | 0.3424 | 0.7865 | False | beats_buy_hold, holm, dsr, spa |
| 594 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=100) | 38.26/0.69/-23.64 | 56.21 | 83 | 0.0302 | 0.22478 (13.48) | 1.0 | 0.3506 | 0.7645 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 595 | BTC_ETH|sma_cross(fast=1,slow=50)+bench_trend(bench=BTC/USD,n=200) | 36.4/0.67/-24.9 | 56.21 | 72 | 0.0312 | 0.28671 (16.99) | 1.0 | 0.341 | 0.778 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 595

## Engine prereg 20261023_174805_c11_dual_momentum_v1 (c11_dual_momentum_v1, sha256 27b3ef6f3db3): rows #596-615 RESERVED (20 variants). Counted in N.
N_cumulative: 615

## Engine run 20261023_174805_c11_dual_momentum_v1 (c11_dual_momentum_v1): rows #596-615. 0/20 pass. PBO 0.829. Bar applied at N=615. Report: engine/runs/20261023_174805_c11_dual_momentum_v1/report.md

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

N_cumulative: 615

## Engine prereg 20261023_174814_c12_rsi_revert_v1 (c12_rsi_revert_v1, sha256 afd2a0e65fa8): rows #616-639 RESERVED (24 variants). Counted in N.
N_cumulative: 639

## Engine run 20261023_174814_c12_rsi_revert_v1 (c12_rsi_revert_v1): rows #616-639. 0/24 pass. PBO 0.144. Bar applied at N=639. Report: engine/runs/20261023_174814_c12_rsi_revert_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 616 | ALTS|rsi_revert(entry=5,exit=50,n=2) | 33.51/0.78/-17.61 | 193.2 | 287 | 0.0162 | 0.56943 (52.66) | 1.0 | 0.3866 | 0.86 | False | beats_buy_hold, holm, dsr, spa |
| 617 | ALTS|rsi_revert(entry=5,exit=50,n=3) | 9.62/0.46/-10.73 | 193.2 | 72 | 0.0157 | 0.84116 (90.93) | 1.0 | 0.2136 | 0.8855 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 618 | ALTS|rsi_revert(entry=5,exit=70,n=2) | 27.13/0.61/-18.87 | 193.2 | 262 | 0.0164 | 0.64236 (74.0) | 1.0 | 0.2969 | 0.8675 | False | beats_buy_hold, holm, dsr, spa |
| 619 | ALTS|rsi_revert(entry=5,exit=70,n=3) | 18.53/0.71/-11.84 | 193.2 | 70 | 0.0158 | 0.74725 (74.35) | 1.0 | 0.3425 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 620 | ALTS|rsi_revert(entry=10,exit=50,n=2) | 12.73/0.35/-17.57 | 193.2 | 493 | 0.0172 | 0.64535 (64.24) | 1.0 | 0.1823 | 0.8775 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 621 | ALTS|rsi_revert(entry=10,exit=50,n=3) | 27.98/0.7/-14.75 | 193.2 | 200 | 0.0159 | 0.65734 (75.44) | 1.0 | 0.3411 | 0.868 | False | beats_buy_hold, holm, dsr, spa |
| 622 | ALTS|rsi_revert(entry=10,exit=70,n=2) | 17.08/0.4/-24.51 | 193.2 | 428 | 0.0174 | 0.64136 (66.11) | 1.0 | 0.2021 | 0.8735 | False | beats_buy_hold, holm, dsr, spa |
| 623 | ALTS|rsi_revert(entry=10,exit=70,n=3) | 41.89/0.8/-19.81 | 193.2 | 178 | 0.016 | 0.56843 (73.32) | 1.0 | 0.4021 | 0.856 | False | beats_buy_hold, holm, dsr, spa |
| 624 | ALTS|rsi_revert(entry=20,exit=50,n=2) | -25.81/-0.29/-42.38 | 193.2 | 830 | 0.0173 | 0.92108 (48.17) | 1.0 | 0.0358 | 0.9175 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 625 | ALTS|rsi_revert(entry=20,exit=50,n=3) | 27.96/0.56/-18.18 | 193.2 | 440 | 0.0168 | 0.58042 (62.87) | 1.0 | 0.272 | 0.863 | False | beats_buy_hold, holm, dsr, spa |
| 626 | ALTS|rsi_revert(entry=20,exit=70,n=2) | -9.04/0.06/-33.47 | 193.2 | 670 | 0.0176 | 0.77522 (40.17) | 1.0 | 0.0946 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 627 | ALTS|rsi_revert(entry=20,exit=70,n=3) | 18.67/0.41/-28.1 | 193.2 | 339 | 0.0171 | 0.62338 (66.61) | 1.0 | 0.2059 | 0.8675 | False | beats_buy_hold, holm, dsr, spa |
| 628 | BTC_ETH|rsi_revert(entry=5,exit=50,n=2) | 28.24/0.74/-16.45 | 56.21 | 99 | 0.0258 | 0.31668 (13.73) | 1.0 | 0.3589 | 0.7355 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 629 | BTC_ETH|rsi_revert(entry=5,exit=50,n=3) | 25.35/0.91/-9.48 | 56.21 | 27 | 0.0242 | 0.4995 (25.3) | 1.0 | 0.4541 | 0.738 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 630 | BTC_ETH|rsi_revert(entry=5,exit=70,n=2) | 34.77/0.76/-16.08 | 56.21 | 91 | 0.0257 | 0.25674 (14.29) | 1.0 | 0.3701 | 0.703 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 631 | BTC_ETH|rsi_revert(entry=5,exit=70,n=3) | 37.85/1.13/-9.51 | 56.21 | 27 | 0.0242 | 0.35065 (25.79) | 1.0 | 0.6126 | 0.6935 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 632 | BTC_ETH|rsi_revert(entry=10,exit=50,n=2) | 12.4/0.36/-24.05 | 56.21 | 176 | 0.0271 | 0.42657 (7.3) | 1.0 | 0.1838 | 0.7995 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 633 | BTC_ETH|rsi_revert(entry=10,exit=50,n=3) | 27.04/0.7/-16.26 | 56.21 | 69 | 0.0249 | 0.38162 (17.15) | 1.0 | 0.3374 | 0.7225 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 634 | BTC_ETH|rsi_revert(entry=10,exit=70,n=2) | 34.81/0.67/-22.53 | 56.21 | 158 | 0.0269 | 0.20779 (8.12) | 1.0 | 0.3269 | 0.701 | False | beats_buy_hold, holm, dsr, spa |
| 635 | BTC_ETH|rsi_revert(entry=10,exit=70,n=3) | 17.33/0.45/-21.29 | 56.21 | 62 | 0.0249 | 0.5035 (18.79) | 1.0 | 0.2217 | 0.7715 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 636 | BTC_ETH|rsi_revert(entry=20,exit=50,n=2) | -8.06/-0.02/-33.15 | 56.21 | 290 | 0.0273 | 0.57942 (-3.31) | 1.0 | 0.0775 | 0.922 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 637 | BTC_ETH|rsi_revert(entry=20,exit=50,n=3) | 35.53/0.73/-24.1 | 56.21 | 156 | 0.0262 | 0.17982 (8.39) | 1.0 | 0.3593 | 0.6945 | False | beats_buy_hold, holm, dsr, spa |
| 638 | BTC_ETH|rsi_revert(entry=20,exit=70,n=2) | 15.86/0.38/-29.86 | 56.21 | 243 | 0.0271 | 0.29171 (-0.02) | 1.0 | 0.1931 | 0.829 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 639 | BTC_ETH|rsi_revert(entry=20,exit=70,n=3) | 27.74/0.55/-33.24 | 56.21 | 130 | 0.0264 | 0.17882 (10.93) | 1.0 | 0.2689 | 0.722 | False | beats_buy_hold, walk_forward, holm, dsr, spa |

N_cumulative: 639

## Engine prereg 20261023_174823_c13_dip_in_uptrend_v1 (c13_dip_in_uptrend_v1, sha256 58efafa3b007): rows #640-663 RESERVED (24 variants). Counted in N.
N_cumulative: 663

## Engine run 20261023_174823_c13_dip_in_uptrend_v1 (c13_dip_in_uptrend_v1): rows #640-663. 0/24 pass. PBO 0.764. Bar applied at N=663. Report: engine/runs/20261023_174823_c13_dip_in_uptrend_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 640 | ALTS|drop_revert(drop=0.08,hold=2,n=1)+trend_sma(n=100) | -6.95/-0.39/-14.72 | 193.2 | 128 | 0.0143 | 0.93706 (90.51) | 1.0 | 0.0053 | 0.905 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 641 | ALTS|drop_revert(drop=0.08,hold=2,n=3)+trend_sma(n=100) | 7.7/0.35/-12.13 | 193.2 | 221 | 0.0158 | 0.78521 (73.44) | 1.0 | 0.0694 | 0.889 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 642 | ALTS|drop_revert(drop=0.08,hold=2,n=5)+trend_sma(n=100) | -17.45/-0.64/-22.81 | 193.2 | 225 | 0.0158 | 0.97403 (72.67) | 1.0 | 0.0015 | 0.9165 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 643 | ALTS|drop_revert(drop=0.08,hold=5,n=1)+trend_sma(n=100) | -4.92/-0.16/-15.28 | 193.2 | 135 | 0.0149 | 0.93407 (89.69) | 1.0 | 0.0136 | 0.9045 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 644 | ALTS|drop_revert(drop=0.08,hold=5,n=3)+trend_sma(n=100) | 14.35/0.47/-19.73 | 193.2 | 224 | 0.0163 | 0.6973 (73.78) | 1.0 | 0.0938 | 0.8865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 645 | ALTS|drop_revert(drop=0.08,hold=5,n=5)+trend_sma(n=100) | 7.98/0.29/-16.52 | 193.2 | 234 | 0.0165 | 0.77123 (60.13) | 1.0 | 0.058 | 0.891 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 646 | ALTS|drop_revert(drop=0.12,hold=2,n=1)+trend_sma(n=100) | 2.37/0.39/-1.59 | 193.2 | 35 | 0.0115 | 0.96503 (49.57) | 1.0 | 0.0365 | 0.8965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 647 | ALTS|drop_revert(drop=0.12,hold=2,n=3)+trend_sma(n=100) | 5.56/0.44/-8.47 | 193.2 | 107 | 0.014 | 0.84016 (60.16) | 1.0 | 0.0871 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 648 | ALTS|drop_revert(drop=0.12,hold=2,n=5)+trend_sma(n=100) | 1.17/0.11/-10.22 | 193.2 | 124 | 0.0147 | 0.87712 (56.99) | 1.0 | 0.0342 | 0.8965 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 649 | ALTS|drop_revert(drop=0.12,hold=5,n=1)+trend_sma(n=100) | 7.56/0.7/-3.38 | 193.2 | 38 | 0.0111 | 0.88911 (133.08) | 1.0 | 0.099 | 0.89 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 650 | ALTS|drop_revert(drop=0.12,hold=5,n=3)+trend_sma(n=100) | 5.76/0.32/-9.77 | 193.2 | 117 | 0.0142 | 0.83317 (78.49) | 1.0 | 0.0598 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 651 | ALTS|drop_revert(drop=0.12,hold=5,n=5)+trend_sma(n=100) | 10.31/0.43/-14.83 | 193.2 | 140 | 0.0149 | 0.74625 (51.17) | 1.0 | 0.0887 | 0.8905 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 652 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=1)+trend_sma(n=100) | -1.64/-0.35/-2.7 | 56.21 | 16 | 0.0194 | 0.85514 (27.81) | 1.0 | 0.0098 | 0.862 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 653 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=3)+trend_sma(n=100) | 4.69/0.4/-8.57 | 56.21 | 47 | 0.023 | 0.72228 (21.92) | 1.0 | 0.0723 | 0.8495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 654 | BTC_ETH|drop_revert(drop=0.08,hold=2,n=5)+trend_sma(n=100) | 2.39/0.19/-5.54 | 56.21 | 51 | 0.0229 | 0.76424 (23.79) | 1.0 | 0.0426 | 0.854 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 655 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=1)+trend_sma(n=100) | -4.61/-0.73/-4.9 | 56.21 | 19 | 0.0195 | 0.86613 (28.19) | 1.0 | 0.0012 | 0.8745 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 656 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=3)+trend_sma(n=100) | 5.21/0.35/-6.48 | 56.21 | 46 | 0.0232 | 0.71528 (21.73) | 1.0 | 0.0656 | 0.846 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 657 | BTC_ETH|drop_revert(drop=0.08,hold=5,n=5)+trend_sma(n=100) | 12.54/0.57/-12.06 | 56.21 | 54 | 0.0238 | 0.62637 (22.02) | 1.0 | 0.1129 | 0.821 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 658 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 56.21 | 4 | 0.0106 | 1.0 (25.72) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 659 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=3)+trend_sma(n=100) | -0.17/-0.04/-2.11 | 56.21 | 15 | 0.0192 | 0.82218 (26.51) | 1.0 | 0.0191 | 0.8595 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 660 | BTC_ETH|drop_revert(drop=0.12,hold=2,n=5)+trend_sma(n=100) | 2.28/0.41/-2.94 | 56.21 | 20 | 0.0211 | 0.7972 (27.54) | 1.0 | 0.0756 | 0.8485 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 661 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=1)+trend_sma(n=100) | -2.35/-0.69/-3.21 | 56.21 | 7 | 0.0074 | 1.0 (32.81) | 1.0 | 0.0001 | 0.8685 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 662 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=3)+trend_sma(n=100) | -3.17/-0.47/-4.64 | 56.21 | 15 | 0.0192 | 0.88112 (29.59) | 1.0 | 0.003 | 0.869 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 663 | BTC_ETH|drop_revert(drop=0.12,hold=5,n=5)+trend_sma(n=100) | -1.57/-0.18/-3.31 | 56.21 | 23 | 0.0195 | 0.85914 (28.63) | 1.0 | 0.0119 | 0.8685 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 663

## Engine prereg 20261023_174831_c14_volgated_mom_v1 (c14_volgated_mom_v1, sha256 265cfe48c0ee): rows #664-679 RESERVED (16 variants). Counted in N.
N_cumulative: 679

## Engine run 20261023_174831_c14_volgated_mom_v1 (c14_volgated_mom_v1): rows #664-679. 0/16 pass. PBO 0.91. Bar applied at N=679. Report: engine/runs/20261023_174831_c14_volgated_mom_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 664 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -5.2/-1.06/-5.55 | 193.2 | 43 | 0.0366 | 0.98701 (45.4) | 1.0 | 0.0 | 0.9035 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 665 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -5.2/-1.06/-5.55 | 193.2 | 40 | 0.0362 | 0.99201 (44.4) | 1.0 | 0.0 | 0.9035 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 666 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 15.29/0.5/-15.5 | 193.2 | 248 | 0.0259 | 0.64236 (59.04) | 1.0 | 0.0011 | 0.8845 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 667 | ALTS|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 13.31/0.44/-15.5 | 193.2 | 238 | 0.0257 | 0.66334 (51.12) | 1.0 | 0.0008 | 0.8845 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 668 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -8.4/-1.55/-8.73 | 193.2 | 47 | 0.0366 | 0.995 (46.2) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 669 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -8.4/-1.55/-8.73 | 193.2 | 44 | 0.0361 | 0.997 (50.14) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 670 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 15.76/0.51/-18.41 | 193.2 | 224 | 0.0253 | 0.65235 (55.95) | 1.0 | 0.0012 | 0.8855 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 671 | ALTS|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 13.77/0.45/-18.41 | 193.2 | 214 | 0.0251 | 0.68631 (77.8) | 1.0 | 0.0009 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 672 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | 2.29/0.15/-14.44 | 56.21 | 84 | 0.0381 | 0.66933 (12.79) | 1.0 | 0.0002 | 0.8835 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 673 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | 1.43/0.12/-14.44 | 56.21 | 77 | 0.0371 | 0.69131 (13.4) | 1.0 | 0.0002 | 0.8845 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 674 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 36.11/0.67/-25.66 | 56.21 | 171 | 0.0299 | 0.16883 (7.08) | 1.0 | 0.0019 | 0.775 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 675 | BTC_ETH|sma_cross(fast=1,slow=20)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 43.75/0.76/-25.66 | 56.21 | 154 | 0.0292 | 0.13986 (6.94) | 1.0 | 0.0028 | 0.7295 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 676 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=80,lo=50,n=14) | -6.04/-0.14/-18.92 | 56.21 | 81 | 0.0376 | 0.79121 (12.95) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 677 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.04,n=14)+rsi_band(hi=100,lo=50,n=14) | -6.83/-0.17/-18.92 | 56.21 | 74 | 0.0366 | 0.7952 (12.78) | 1.0 | 0.0 | 0.9205 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 678 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=80,lo=50,n=14) | 35.55/0.68/-25.24 | 56.21 | 149 | 0.0309 | 0.18182 (7.54) | 1.0 | 0.0023 | 0.78 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 679 | BTC_ETH|sma_cross(fast=1,slow=50)+vol_regime(max_atr_pct=0.06,n=14)+rsi_band(hi=100,lo=50,n=14) | 43.16/0.77/-25.24 | 56.21 | 132 | 0.03 | 0.16683 (9.71) | 1.0 | 0.0033 | 0.74 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 679

## Engine prereg 20261023_195853_s07_country_tsmom_breakout_v1 (s07_country_tsmom_breakout_v1, sha256 b6f151fda3c8): rows #680-683 RESERVED (4 variants). Counted in N.
N_cumulative: 683

## Engine run 20261023_195853_s07_country_tsmom_breakout_v1 (s07_country_tsmom_breakout_v1): rows #680-683. 0/4 pass. PBO 0.684. Bar applied at N=683. Report: engine/runs/20261023_195853_s07_country_tsmom_breakout_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 680 | COUNTRIES|donchian(entry_n=126,exit_n=21) | 3.28/0.21/-6.68 | 64.42 | 102 | 0.0199 | 0.996 (28.36) | 1.0 | 0.4808 | 0.5035 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 681 | COUNTRIES|donchian(entry_n=126,exit_n=63) | 5.16/0.27/-9.18 | 64.42 | 56 | 0.0173 | 1.0 (28.69) | 1.0 | 0.5242 | 0.508 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 682 | COUNTRIES|donchian(entry_n=252,exit_n=21) | 1.11/0.1/-6.57 | 64.42 | 75 | 0.0202 | 0.999 (28.84) | 1.0 | 0.4058 | 0.5035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 683 | COUNTRIES|donchian(entry_n=252,exit_n=63) | 2.09/0.15/-8.46 | 64.42 | 43 | 0.0191 | 0.998 (29.05) | 1.0 | 0.4415 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 683

## Engine prereg 20261023_195859_s08_orb_15m_hibeta_v1 (s08_orb_15m_hibeta_v1, sha256 89e4b879bd63): rows #684-687 RESERVED (4 variants). Counted in N.
N_cumulative: 687

## Engine run 20261023_195859_s08_orb_15m_hibeta_v1 (s08_orb_15m_hibeta_v1): rows #684-687. 0/4 pass. PBO 0.695. Bar applied at N=687. Report: engine/runs/20261023_195859_s08_orb_15m_hibeta_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 684 | HIBETA|donchian(entry_n=2,exit_n=8)+session(end=10:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.88/3.05/-0.14 | -2.96 | 90 | 0.0194 | 0.2028 (-2.33) | 1.0 | 0.9946 | 0.4125 | False | min_trades, holm, spa, pbo |
| 685 | HIBETA|donchian(entry_n=2,exit_n=8)+session(end=11:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.93/3.01/-0.14 | -2.96 | 110 | 0.0194 | 0.17283 (-2.63) | 1.0 | 0.9924 | 0.413 | False | holm, spa, pbo |
| 686 | HIBETA|donchian(entry_n=4,exit_n=8)+session(end=10:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.88/3.05/-0.14 | -2.96 | 83 | 0.0195 | 0.1978 (-2.71) | 1.0 | 0.9946 | 0.4125 | False | min_trades, holm, spa, pbo |
| 687 | HIBETA|donchian(entry_n=4,exit_n=8)+session(end=11:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.93/3.01/-0.14 | -2.96 | 100 | 0.0198 | 0.1998 (-2.86) | 1.0 | 0.9924 | 0.413 | False | holm, spa, pbo |

N_cumulative: 687

## Engine prereg 20261023_195900_s09_credit_trend_v1 (s09_credit_trend_v1, sha256 682d1e33d67a): rows #688-690 RESERVED (3 variants). Counted in N.
N_cumulative: 690

## Engine run 20261023_195900_s09_credit_trend_v1 (s09_credit_trend_v1): rows #688-690. 0/3 pass. PBO 0.861. Bar applied at N=690. Report: engine/runs/20261023_195900_s09_credit_trend_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 688 | CREDIT|sma_cross(fast=1,slow=50) | 11.75/0.74/-8.37 | 32.7 | 289 | 0.0199 | 0.52348 (12.25) | 1.0 | 0.7435 | 0.4815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 689 | CREDIT|sma_cross(fast=1,slow=100) | 9.95/0.61/-8.42 | 32.7 | 177 | 0.0183 | 0.81618 (13.58) | 1.0 | 0.6627 | 0.4975 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 690 | CREDIT|sma_cross(fast=1,slow=200) | 14.39/0.84/-5.42 | 32.7 | 115 | 0.0154 | 0.43057 (13.78) | 1.0 | 0.7923 | 0.5195 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 690

## Engine prereg 20261023_195906_s10_index_dip_in_uptrend_v1 (s10_index_dip_in_uptrend_v1, sha256 e16b8f7f9f2b): rows #691-694 RESERVED (4 variants). Counted in N.
N_cumulative: 694

## Engine run 20261023_195906_s10_index_dip_in_uptrend_v1 (s10_index_dip_in_uptrend_v1): rows #691-694. 0/4 pass. PBO 0.382. Bar applied at N=694. Report: engine/runs/20261023_195906_s10_index_dip_in_uptrend_v1/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 691 | US_INDEX|drop_revert(drop=0.03,hold=5,n=3)+trend_sma(n=200) | 5.51/0.5/-3.8 | 68.31 | 185 | 0.0119 | 1.0 (29.55) | 1.0 | 0.2636 | 0.4995 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 692 | US_INDEX|drop_revert(drop=0.03,hold=5,n=5)+trend_sma(n=200) | 9.1/0.81/-3.88 | 68.31 | 205 | 0.0126 | 0.99301 (28.51) | 1.0 | 0.4612 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 693 | US_INDEX|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | 3.68/0.72/-0.84 | 68.31 | 50 | 0.011 | 0.999 (30.75) | 1.0 | 0.3664 | 0.4965 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 694 | US_INDEX|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 8.15/1.16/-1.35 | 68.31 | 78 | 0.0111 | 0.999 (30.37) | 1.0 | 0.751 | 0.497 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 694

## Engine prereg 20261023_195909_gen_2310231905_000 (gen_2310231905_000, sha256 09264db6e4cd): rows #695-702 RESERVED (8 variants). Counted in N.
N_cumulative: 702

## Engine run 20261023_195909_gen_2310231905_000 (gen_2310231905_000): rows #695-702. 0/8 pass. PBO 0.188. Bar applied at N=702. Report: engine/runs/20261023_195909_gen_2310231905_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 695 | crypto|drop_revert(drop=0.05,hold=3,n=3) | 6.45/0.7/-3.45 | 428.6 | 527 | 0.0357 | 0.88412 (141.06) | 1.0 | 0.1025 | 0.903 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 696 | crypto|drop_revert(drop=0.05,hold=3,n=5) | 0.61/0.09/-10.68 | 428.6 | 707 | 0.0427 | 0.91209 (182.05) | 1.0 | 0.0212 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 697 | crypto|drop_revert(drop=0.05,hold=5,n=3) | 14.64/1.01/-5.04 | 428.6 | 482 | 0.0373 | 0.82418 (212.45) | 1.0 | 0.1782 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 698 | crypto|drop_revert(drop=0.05,hold=5,n=5) | -2.22/-0.04/-14.4 | 428.6 | 675 | 0.0434 | 0.91608 (101.4) | 1.0 | 0.0139 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 699 | crypto|drop_revert(drop=0.15,hold=3,n=3) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 700 | crypto|drop_revert(drop=0.15,hold=3,n=5) | -0.37/-0.45/-0.6 | 428.6 | 21 | 0.0132 | 0.93806 (253.93) | 1.0 | 0.0009 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 701 | crypto|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 702 | crypto|drop_revert(drop=0.15,hold=5,n=5) | -0.42/-0.26/-1.37 | 428.6 | 21 | 0.0132 | 0.94106 (259.66) | 1.0 | 0.0084 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 702

## Engine prereg 20261023_200357_gen_2310231905_001 (gen_2310231905_001, sha256 7bb35aba6d16): rows #703-706 RESERVED (4 variants). Counted in N.
N_cumulative: 706

## Engine run 20261023_200357_gen_2310231905_001 (gen_2310231905_001): rows #703-706. 0/4 pass. PBO 0.441. Bar applied at N=706. Report: engine/runs/20261023_200357_gen_2310231905_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 703 | crypto|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.06) | -2.64/0.09/-35.62 | 428.6 | 1653 | 0.1027 | 0.8002 (53.47) | 1.0 | 0.0385 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 704 | crypto|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.06) | -5.08/0.08/-45.63 | 428.6 | 1285 | 0.0997 | 0.86613 (60.75) | 1.0 | 0.0385 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 705 | crypto|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 31.24/0.97/-15.33 | 428.6 | 695 | 0.0988 | 0.66334 (92.96) | 1.0 | 0.2293 | 0.8925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 706 | crypto|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | 33.55/0.91/-22.39 | 428.6 | 566 | 0.0965 | 0.65335 (177.37) | 1.0 | 0.2114 | 0.891 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 706

## Engine prereg 20261023_200404_gen_2310231905_002 (gen_2310231905_002, sha256 99695249a4ec): rows #707-714 RESERVED (8 variants). Counted in N.
N_cumulative: 714

## Engine run 20261023_200404_gen_2310231905_002 (gen_2310231905_002): rows #707-714. 0/8 pass. PBO 0.018. Bar applied at N=714. Report: engine/runs/20261023_200404_gen_2310231905_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 707 | crypto|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=60) | -0.6/-0.82/-0.6 | 428.6 | 15 | 0.0143 | 0.95604 (47.85) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 708 | crypto|drop_revert(drop=0.1,hold=3,n=3)+rsi_band(hi=60) | 0.46/0.34/-0.71 | 428.6 | 47 | 0.0154 | 0.95904 (232.39) | 1.0 | 0.0122 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 709 | crypto|drop_revert(drop=0.1,hold=5,n=1)+rsi_band(hi=60) | 0.35/0.26/-0.6 | 428.6 | 16 | 0.0146 | 0.96004 (46.47) | 1.0 | 0.0103 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 710 | crypto|drop_revert(drop=0.1,hold=5,n=3)+rsi_band(hi=60) | 1.51/0.69/-0.6 | 428.6 | 46 | 0.0155 | 0.95005 (68.79) | 1.0 | 0.0127 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 711 | crypto|drop_revert(drop=0.15,hold=3,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 712 | crypto|drop_revert(drop=0.15,hold=3,n=3)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 713 | crypto|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 714 | crypto|drop_revert(drop=0.15,hold=5,n=3)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 714

## Engine prereg 20261023_200412_gen_2310231906_000 (gen_2310231906_000, sha256 d70cbd3f3d7a): rows #715-718 RESERVED (4 variants). Counted in N.
N_cumulative: 718

## Engine run 20261023_200412_gen_2310231906_000 (gen_2310231906_000): rows #715-718. 0/4 pass. PBO 0.488. Bar applied at N=718. Report: engine/runs/20261023_200412_gen_2310231906_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 715 | hibeta|donchian(entry_n=20,exit_n=10) | 265.0/1.59/-20.74 | 809.88 | 179 | 0.0255 | 0.26873 (216.09) | 1.0 | 0.9478 | 0.511 | False | beats_buy_hold, holm, dsr, spa |
| 716 | hibeta|donchian(entry_n=20,exit_n=20) | 260.77/1.44/-31.36 | 809.88 | 129 | 0.0228 | 0.27273 (219.03) | 1.0 | 0.9075 | 0.5205 | False | beats_buy_hold, holm, dsr, spa |
| 717 | hibeta|donchian(entry_n=100,exit_n=10) | 145.61/1.59/-11.11 | 809.88 | 86 | 0.029 | 0.80819 (223.92) | 1.0 | 0.9492 | 0.51 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 718 | hibeta|donchian(entry_n=100,exit_n=20) | 96.24/1.13/-18.86 | 809.88 | 67 | 0.0278 | 0.95604 (223.61) | 1.0 | 0.7819 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 718

## Engine prereg 20261023_200415_gen_2310231906_001 (gen_2310231906_001, sha256 cb254a9cebf3): rows #719-726 RESERVED (8 variants). Counted in N.
N_cumulative: 726

## Engine run 20261023_200415_gen_2310231906_001 (gen_2310231906_001): rows #719-726. 0/8 pass. PBO 0.502. Bar applied at N=726. Report: engine/runs/20261023_200415_gen_2310231906_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 719 | hibeta|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=70) | 114.41/1.16/-18.15 | 809.88 | 494 | 0.0161 | 0.88112 (213.66) | 1.0 | 0.8417 | 0.5115 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 720 | hibeta|drop_revert(drop=0.05,hold=3,n=3)+rsi_band(hi=70) | 178.3/1.3/-27.73 | 809.88 | 630 | 0.0185 | 0.62338 (212.23) | 1.0 | 0.8887 | 0.5145 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 721 | hibeta|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=70) | 247.98/1.36/-25.49 | 809.88 | 297 | 0.019 | 0.28971 (212.9) | 1.0 | 0.9013 | 0.507 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 722 | hibeta|drop_revert(drop=0.05,hold=10,n=3)+rsi_band(hi=70) | 235.41/1.22/-34.49 | 809.88 | 311 | 0.0218 | 0.34565 (216.08) | 1.0 | 0.8468 | 0.499 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 723 | hibeta|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=70) | 50.9/1.53/-4.01 | 809.88 | 87 | 0.0113 | 0.98801 (217.51) | 1.0 | 0.971 | 0.506 | False | beats_buy_hold, min_trades, holm, spa, pbo |
| 724 | hibeta|drop_revert(drop=0.1,hold=3,n=3)+rsi_band(hi=70) | 84.48/1.07/-11.76 | 809.88 | 273 | 0.0143 | 0.94505 (219.64) | 1.0 | 0.8103 | 0.505 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 725 | hibeta|drop_revert(drop=0.1,hold=10,n=1)+rsi_band(hi=70) | 70.79/1.35/-8.91 | 809.88 | 69 | 0.0124 | 0.97403 (225.34) | 1.0 | 0.9115 | 0.493 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 726 | hibeta|drop_revert(drop=0.1,hold=10,n=3)+rsi_band(hi=70) | 86.54/0.87/-21.86 | 809.88 | 181 | 0.0157 | 0.94805 (223.11) | 1.0 | 0.6601 | 0.508 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 726

## Engine prereg 20261023_200419_gen_2310231906_002 (gen_2310231906_002, sha256 bc493fe5ff5e): rows #727-734 RESERVED (8 variants). Counted in N.
N_cumulative: 734

## Engine run 20261023_200419_gen_2310231906_002 (gen_2310231906_002): rows #727-734. 0/8 pass. PBO 0.222. Bar applied at N=734. Report: engine/runs/20261023_200419_gen_2310231906_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 727 | hibeta|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=100) | 7.73/0.34/-8.45 | 809.88 | 126 | 0.0227 | 1.0 (226.05) | 1.0 | 0.053 | 0.5095 | False | beats_buy_hold, holm, dsr, spa |
| 728 | hibeta|rsi_revert(entry=5,exit=70,n=3)+trend_sma(n=100) | 8.79/0.68/-3.64 | 809.88 | 28 | 0.0178 | 0.999 (220.95) | 1.0 | 0.1097 | 0.5095 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 729 | hibeta|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=100) | 11.22/0.43/-9.03 | 809.88 | 136 | 0.022 | 1.0 (219.32) | 1.0 | 0.0722 | 0.5085 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 730 | hibeta|rsi_revert(entry=5,exit=80,n=3)+trend_sma(n=100) | 14.62/0.83/-4.34 | 809.88 | 29 | 0.0175 | 0.999 (223.63) | 1.0 | 0.1754 | 0.508 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 731 | hibeta|rsi_revert(entry=20,exit=70,n=2)+trend_sma(n=100) | 89.71/1.36/-17.51 | 809.88 | 480 | 0.0229 | 0.97502 (212.08) | 1.0 | 0.5592 | 0.5085 | False | beats_buy_hold, holm, dsr, spa |
| 732 | hibeta|rsi_revert(entry=20,exit=70,n=3)+trend_sma(n=100) | 1.67/0.11/-24.07 | 809.88 | 269 | 0.023 | 1.0 (218.98) | 1.0 | 0.0238 | 0.5105 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 733 | hibeta|rsi_revert(entry=20,exit=80,n=2)+trend_sma(n=100) | 65.79/0.98/-21.82 | 809.88 | 457 | 0.0231 | 0.98801 (209.0) | 1.0 | 0.3095 | 0.504 | False | beats_buy_hold, holm, dsr, spa |
| 734 | hibeta|rsi_revert(entry=20,exit=80,n=3)+trend_sma(n=100) | 19.35/0.42/-16.24 | 809.88 | 283 | 0.0234 | 1.0 (213.07) | 1.0 | 0.0731 | 0.507 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 734

## Engine prereg 20261023_200422_gen_2310231907_000 (gen_2310231907_000, sha256 307586a17b34): rows #735-742 RESERVED (8 variants). Counted in N.
N_cumulative: 742

## Engine run 20261023_200422_gen_2310231907_000 (gen_2310231907_000): rows #735-742. 0/8 pass. PBO 0.8. Bar applied at N=742. Report: engine/runs/20261023_200422_gen_2310231907_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 735 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.2) | -5.18/-0.16/-17.72 | 268.18 | 301 | 0.0119 | 0.90909 (78.08) | 1.0 | 0.0198 | 0.8935 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 736 | crypto_d|drop_revert(drop=0.05,hold=3,n=3)+relvol(min_ratio=1.2) | -9.19/-0.3/-19.22 | 268.18 | 369 | 0.0131 | 0.93806 (117.85) | 1.0 | 0.0133 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 737 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.2) | -25.47/-0.79/-29.27 | 268.18 | 486 | 0.0128 | 0.97902 (106.97) | 1.0 | 0.0018 | 0.912 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 738 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.2) | -8.26/-0.12/-31.02 | 268.18 | 601 | 0.0139 | 0.8961 (109.22) | 1.0 | 0.0212 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 739 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+relvol(min_ratio=1.2) | 10.81/0.84/-5.71 | 268.18 | 81 | 0.0098 | 0.79121 (71.57) | 1.0 | 0.1327 | 0.878 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 740 | crypto_d|drop_revert(drop=0.1,hold=3,n=3)+relvol(min_ratio=1.2) | 7.42/0.42/-9.91 | 268.18 | 165 | 0.0114 | 0.8002 (69.87) | 1.0 | 0.0775 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 741 | crypto_d|drop_revert(drop=0.1,hold=10,n=1)+relvol(min_ratio=1.2) | -6.92/-0.25/-15.72 | 268.18 | 138 | 0.01 | 0.93606 (132.4) | 1.0 | 0.012 | 0.8955 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 742 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+relvol(min_ratio=1.2) | -0.16/0.1/-16.63 | 268.18 | 319 | 0.0116 | 0.88811 (140.73) | 1.0 | 0.0399 | 0.8915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 742

## Engine prereg 20261023_200425_gen_2310231907_001 (gen_2310231907_001, sha256 d7c7b7acb884): rows #743-750 RESERVED (8 variants). Counted in N.
N_cumulative: 750

## Engine run 20261023_200425_gen_2310231907_001 (gen_2310231907_001): rows #743-750. 0/8 pass. PBO 0.892. Bar applied at N=750. Report: engine/runs/20261023_200425_gen_2310231907_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 743 | crypto_d|rsi_revert(entry=5,exit=70,n=2) | 49.4/1.2/-13.0 | 268.18 | 177 | 0.0134 | 0.54046 (81.34) | 1.0 | 0.5469 | 0.838 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 744 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 3.23/0.46/-3.83 | 268.18 | 4 | 0.0148 | 0.95804 (165.9) | 1.0 | 0.2042 | 0.8875 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 745 | crypto_d|rsi_revert(entry=5,exit=80,n=2) | 33.77/0.8/-19.99 | 268.18 | 163 | 0.0137 | 0.61239 (98.34) | 1.0 | 0.3535 | 0.8565 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 746 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 3.09/0.32/-8.84 | 268.18 | 4 | 0.0148 | 0.96404 (42.84) | 1.0 | 0.1715 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 747 | crypto_d|rsi_revert(entry=20,exit=70,n=2) | 9.31/0.35/-25.07 | 268.18 | 438 | 0.0151 | 0.77123 (79.1) | 1.0 | 0.1809 | 0.8785 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 748 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 59.81/1.09/-26.28 | 268.18 | 94 | 0.0141 | 0.52248 (80.48) | 1.0 | 0.492 | 0.8385 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 749 | crypto_d|rsi_revert(entry=20,exit=80,n=2) | 27.63/0.6/-25.3 | 268.18 | 368 | 0.0154 | 0.62438 (67.14) | 1.0 | 0.2681 | 0.853 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 750 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 69.35/1.04/-33.78 | 268.18 | 73 | 0.0155 | 0.47253 (55.65) | 1.0 | 0.4673 | 0.811 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 750

## Engine prereg 20261023_200428_gen_2310231907_002 (gen_2310231907_002, sha256 f42f907f664b): rows #751-754 RESERVED (4 variants). Counted in N.
N_cumulative: 754

## Engine run 20261023_200428_gen_2310231907_002 (gen_2310231907_002): rows #751-754. 0/4 pass. PBO 0.428. Bar applied at N=754. Report: engine/runs/20261023_200428_gen_2310231907_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 751 | crypto_d|supertrend(atr_n=7,mult=2) | -9.09/0.01/-37.93 | 268.18 | 133 | 0.0173 | 0.93307 (83.88) | 1.0 | 0.2559 | 0.913 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 752 | crypto_d|supertrend(atr_n=7,mult=3) | 5.54/0.28/-29.93 | 268.18 | 75 | 0.0184 | 0.85714 (140.33) | 1.0 | 0.3715 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 753 | crypto_d|supertrend(atr_n=14,mult=2) | 9.38/0.35/-27.1 | 268.18 | 128 | 0.0174 | 0.83916 (136.95) | 1.0 | 0.4024 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 754 | crypto_d|supertrend(atr_n=14,mult=3) | -7.44/0.03/-30.33 | 268.18 | 75 | 0.0183 | 0.93506 (128.89) | 1.0 | 0.2627 | 0.904 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 754

## Engine prereg 20261023_200431_gen_2310231907_003 (gen_2310231907_003, sha256 025a665124a9): rows #755-758 RESERVED (4 variants). Counted in N.
N_cumulative: 758

## Engine run 20261023_200431_gen_2310231907_003 (gen_2310231907_003): rows #755-758. 0/4 pass. PBO 0.53. Bar applied at N=758. Report: engine/runs/20261023_200431_gen_2310231907_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 755 | crypto_d|donchian(entry_n=20,exit_n=10) | -8.35/-0.04/-26.1 | 268.18 | 82 | 0.0193 | 0.93806 (81.7) | 1.0 | 0.2206 | 0.905 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 756 | crypto_d|donchian(entry_n=20,exit_n=20) | 0.12/0.2/-33.03 | 268.18 | 59 | 0.0195 | 0.88911 (80.59) | 1.0 | 0.3108 | 0.905 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 757 | crypto_d|donchian(entry_n=100,exit_n=10) | 9.14/0.42/-17.9 | 268.18 | 30 | 0.02 | 0.76923 (168.08) | 1.0 | 0.411 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 758 | crypto_d|donchian(entry_n=100,exit_n=20) | 5.71/0.28/-20.05 | 268.18 | 26 | 0.02 | 0.82717 (54.19) | 1.0 | 0.3494 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 758

## Engine prereg 20261023_200433_gen_2310231908_000 (gen_2310231908_000, sha256 2408c906133f): rows #759-766 RESERVED (8 variants). Counted in N.
N_cumulative: 766

## Engine run 20261023_200433_gen_2310231908_000 (gen_2310231908_000): rows #759-766. 0/8 pass. PBO 0.7. Bar applied at N=766. Report: engine/runs/20261023_200433_gen_2310231908_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 759 | semis|drop_revert(drop=0.1,hold=3,n=1) | 0.05/0.03/-2.7 | -38.66 | 17 | 0.0221 | 0.11688 (-22.2) | 1.0 | 0.0116 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 760 | semis|drop_revert(drop=0.1,hold=3,n=3) | 0.67/0.13/-3.61 | -38.66 | 37 | 0.0263 | 0.12388 (-22.07) | 1.0 | 0.0034 | 0.2935 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 761 | semis|drop_revert(drop=0.1,hold=5,n=1) | 2.02/0.51/-2.76 | -38.66 | 17 | 0.0221 | 0.1049 (-22.28) | 1.0 | 0.046 | 0.289 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 762 | semis|drop_revert(drop=0.1,hold=5,n=3) | -5.92/-0.85/-6.97 | -38.66 | 35 | 0.0271 | 0.20879 (-21.35) | 1.0 | 0.0 | 0.332 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 763 | semis|drop_revert(drop=0.15,hold=3,n=1) | 0.04/0.04/-0.75 | -38.66 | 6 | 0.002 | 0.12787 (-20.42) | 1.0 | 0.0136 | 0.3 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 764 | semis|drop_revert(drop=0.15,hold=3,n=3) | -0.19/-0.03/-2.73 | -38.66 | 16 | 0.0272 | 0.12987 (-20.55) | 1.0 | 0.0039 | 0.2965 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 765 | semis|drop_revert(drop=0.15,hold=5,n=1) | 0.73/0.64/-0.57 | -38.66 | 6 | 0.002 | 0.10589 (-20.9) | 1.0 | 0.063 | 0.292 | False | min_trades, holm, dsr, spa, pbo |
| 766 | semis|drop_revert(drop=0.15,hold=5,n=3) | -1.23/-0.28/-2.92 | -38.66 | 16 | 0.0272 | 0.13786 (-21.61) | 1.0 | 0.0003 | 0.302 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 766

## Engine prereg 20261023_200458_gen_2310231908_001 (gen_2310231908_001, sha256 0bb941f05c74): rows #767-774 RESERVED (8 variants). Counted in N.
N_cumulative: 774

## Engine run 20261023_200458_gen_2310231908_001 (gen_2310231908_001): rows #767-774. 0/8 pass. PBO 0.526. Bar applied at N=774. Report: engine/runs/20261023_200458_gen_2310231908_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 767 | semis|drop_revert(drop=0.05,hold=3,n=1) | 6.17/0.58/-3.57 | -38.66 | 80 | 0.0343 | 0.12288 (-20.9) | 1.0 | 0.0269 | 0.26 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 768 | semis|drop_revert(drop=0.05,hold=3,n=3) | -8.01/-0.53/-13.02 | -38.66 | 323 | 0.0473 | 0.26474 (-21.93) | 1.0 | 0.0013 | 0.35 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 769 | semis|drop_revert(drop=0.05,hold=10,n=1) | 18.86/1.15/-6.81 | -38.66 | 75 | 0.0354 | 0.03197 (-22.15) | 1.0 | 0.1096 | 0.21 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 770 | semis|drop_revert(drop=0.05,hold=10,n=3) | 6.0/0.33/-14.25 | -38.66 | 276 | 0.0489 | 0.06893 (-21.32) | 1.0 | 0.0306 | 0.228 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 771 | semis|drop_revert(drop=0.1,hold=3,n=1) | 0.05/0.03/-2.7 | -38.66 | 17 | 0.0221 | 0.12488 (-20.4) | 1.0 | 0.0149 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 772 | semis|drop_revert(drop=0.1,hold=3,n=3) | 0.67/0.13/-3.61 | -38.66 | 37 | 0.0263 | 0.12987 (-22.07) | 1.0 | 0.0045 | 0.2935 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 773 | semis|drop_revert(drop=0.1,hold=10,n=1) | 5.53/1.04/-3.18 | -38.66 | 17 | 0.0221 | 0.0999 (-20.22) | 1.0 | 0.1332 | 0.2685 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 774 | semis|drop_revert(drop=0.1,hold=10,n=3) | 3.43/0.41/-6.67 | -38.66 | 34 | 0.0271 | 0.09391 (-20.81) | 1.0 | 0.0187 | 0.278 | False | min_trades, holm, dsr, spa, pbo |

N_cumulative: 774

## Engine prereg 20261023_200502_gen_2310231908_002 (gen_2310231908_002, sha256 f80a0c0dc4a8): rows #775-782 RESERVED (8 variants). Counted in N.
N_cumulative: 782

## Engine run 20261023_200502_gen_2310231908_002 (gen_2310231908_002): rows #775-782. 0/8 pass. PBO 0.393. Bar applied at N=782. Report: engine/runs/20261023_200502_gen_2310231908_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 775 | semis|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.0) | 1.55/0.57/-1.51 | -38.66 | 33 | 0.0375 | 0.12887 (-21.41) | 1.0 | 0.0033 | 0.2885 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 776 | semis|drop_revert(drop=0.05,hold=3,n=3)+relvol(min_ratio=1.0) | -0.51/-0.14/-2.63 | -38.66 | 117 | 0.0458 | 0.13287 (-21.9) | 1.0 | 0.0001 | 0.3005 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 777 | semis|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | 3.0/0.89/-1.45 | -38.66 | 83 | 0.0391 | 0.11289 (-20.3) | 1.0 | 0.0043 | 0.2795 | False | min_trades, cost_stop, holm, dsr, spa |
| 778 | semis|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.0) | 2.89/0.61/-3.32 | -38.66 | 259 | 0.0471 | 0.09391 (-22.3) | 1.0 | 0.0061 | 0.2785 | False | cost_stop, holm, dsr, spa |
| 779 | semis|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.6/0.82/0.0 | -38.66 | 1 | 0.0014 | 0.0979 (-20.27) | 1.0 | 0.0014 | 0.2945 | False | min_trades, walk_forward, holm, dsr, spa |
| 780 | semis|drop_revert(drop=0.15,hold=3,n=3)+relvol(min_ratio=1.0) | 0.74/0.82/-0.13 | -38.66 | 6 | 0.0284 | 0.13686 (-20.57) | 1.0 | 0.0029 | 0.294 | False | min_trades, holm, dsr, spa |
| 781 | semis|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 1.69/1.34/-0.03 | -38.66 | 4 | 0.0046 | 0.16284 (-21.03) | 1.0 | 0.0378 | 0.284 | False | min_trades, holm, dsr, spa |
| 782 | semis|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.0) | 3.1/1.72/-0.19 | -38.66 | 10 | 0.0286 | 0.14386 (-21.89) | 1.0 | 0.0548 | 0.2765 | False | min_trades, holm, dsr, spa |

N_cumulative: 782

## Engine prereg 20261023_200505_gen_2310231908_003 (gen_2310231908_003, sha256 c2f42e65f948): rows #783-786 RESERVED (4 variants). Counted in N.
N_cumulative: 786

## Engine run 20261023_200505_gen_2310231908_003 (gen_2310231908_003): rows #783-786. 0/4 pass. PBO 0.614. Bar applied at N=786. Report: engine/runs/20261023_200505_gen_2310231908_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 783 | semis|supertrend(atr_n=7,mult=3) | 28.4/0.72/-17.9 | -38.66 | 2254 | 0.09 | 0.05395 (-33.22) | 1.0 | 0.5446 | 0.1295 | False | cost_stop, holm, dsr, spa, pbo |
| 784 | semis|supertrend(atr_n=7,mult=4) | 7.65/0.32/-24.6 | -38.66 | 2013 | 0.0925 | 0.21479 (-31.69) | 1.0 | 0.355 | 0.1625 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 785 | semis|supertrend(atr_n=14,mult=3) | 4.7/0.26/-21.67 | -38.66 | 2232 | 0.0906 | 0.23277 (-33.11) | 1.0 | 0.3726 | 0.1785 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 786 | semis|supertrend(atr_n=14,mult=4) | 20.96/0.56/-22.05 | -38.66 | 2011 | 0.0925 | 0.11189 (-30.99) | 1.0 | 0.4623 | 0.118 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 786

## Engine prereg 20261023_201037_gen_2310232009_000 (gen_2310232009_000, sha256 ade992db81a8): rows #787-790 RESERVED (4 variants). Counted in N.
N_cumulative: 790

## Engine run 20261023_201037_gen_2310232009_000 (gen_2310232009_000): rows #787-790. 0/4 pass. PBO 0.713. Bar applied at N=790. Report: engine/runs/20261023_201037_gen_2310232009_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 787 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.83417 (132.6) | 1.0 | 0.323 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 788 | crypto|supertrend(atr_n=10,mult=3) | -9.6/-0.01/-44.27 | 428.6 | 1339 | 0.0981 | 0.91209 (95.61) | 1.0 | 0.3397 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 789 | crypto|supertrend(atr_n=14,mult=2) | -4.81/0.1/-37.43 | 428.6 | 2376 | 0.0958 | 0.76124 (50.17) | 1.0 | 0.3864 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 790 | crypto|supertrend(atr_n=14,mult=3) | 0.35/0.19/-41.76 | 428.6 | 1347 | 0.0966 | 0.82517 (156.31) | 1.0 | 0.4294 | 0.92 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 790

## Engine prereg 20261023_201046_gen_2310232010_000 (gen_2310232010_000, sha256 16762eaafeae): rows #791-798 RESERVED (8 variants). Counted in N.
N_cumulative: 798

## Engine run 20261023_201046_gen_2310232010_000 (gen_2310232010_000): rows #791-798. 0/8 pass. PBO 0.272. Bar applied at N=798. Report: engine/runs/20261023_201046_gen_2310232010_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 791 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.94705 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 792 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 1.09/0.76/-0.48 | 268.18 | 4 | 0.0255 | 0.89111 (176.43) | 1.0 | 0.5559 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 793 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93906 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 794 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 0.88/0.46/-1.56 | 268.18 | 4 | 0.0255 | 0.91508 (44.2) | 1.0 | 0.3983 | 0.892 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 795 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93706 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 796 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93706 (32.26) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 797 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93407 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 798 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.92408 (32.26) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 798

## Engine prereg 20261023_201048_gen_2310232011_000 (gen_2310232011_000, sha256 60bdecd7082b): rows #799-806 RESERVED (8 variants). Counted in N.
N_cumulative: 806

## Engine run 20261023_201048_gen_2310232011_000 (gen_2310232011_000): rows #799-806. 0/8 pass. PBO 0.544. Bar applied at N=806. Report: engine/runs/20261023_201048_gen_2310232011_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 799 | megacap|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.0) | 19.29/0.72/-3.4 | 214.9 | 530 | 0.0441 | 0.999 (76.14) | 1.0 | 0.5125 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 800 | megacap|rsi_revert(entry=10,exit=60,n=5)+relvol(min_ratio=1.0) | 6.54/0.92/-1.23 | 214.9 | 62 | 0.0392 | 0.995 (76.65) | 1.0 | 0.6844 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 801 | megacap|rsi_revert(entry=10,exit=80,n=2)+relvol(min_ratio=1.0) | 22.04/0.76/-5.76 | 214.9 | 661 | 0.0427 | 0.996 (71.98) | 1.0 | 0.5476 | 0.4845 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 802 | megacap|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.0) | 6.03/0.38/-4.96 | 214.9 | 168 | 0.0353 | 0.996 (76.17) | 1.0 | 0.2584 | 0.4995 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 803 | megacap|rsi_revert(entry=20,exit=60,n=2)+relvol(min_ratio=1.0) | 34.07/1.03/-4.04 | 214.9 | 809 | 0.0442 | 0.98102 (71.49) | 1.0 | 0.7782 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 804 | megacap|rsi_revert(entry=20,exit=60,n=5)+relvol(min_ratio=1.0) | 28.8/1.03/-2.97 | 214.9 | 346 | 0.0398 | 0.99401 (77.16) | 1.0 | 0.8145 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 805 | megacap|rsi_revert(entry=20,exit=80,n=2)+relvol(min_ratio=1.0) | 35.14/1.0/-6.16 | 214.9 | 933 | 0.0437 | 0.96803 (70.67) | 1.0 | 0.7467 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 806 | megacap|rsi_revert(entry=20,exit=80,n=5)+relvol(min_ratio=1.0) | 31.85/0.97/-8.24 | 214.9 | 672 | 0.0388 | 0.97902 (74.52) | 1.0 | 0.7108 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 806

## Engine prereg 20261023_201054_gen_2310232012_000 (gen_2310232012_000, sha256 96ec04e9f094): rows #807-822 RESERVED (16 variants). Counted in N.
N_cumulative: 822

## Engine run 20261023_201054_gen_2310232012_000 (gen_2310232012_000): rows #807-822. 0/16 pass. PBO 0.445. Bar applied at N=822. Report: engine/runs/20261023_201054_gen_2310232012_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 807 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=0) | -0.96/-0.12/-3.47 | 63.33 | 1151 | 0.0812 | 1.0 (22.01) | 1.0 | 0.0003 | 0.495 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 808 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=1) | 3.98/0.49/-3.41 | 63.33 | 1275 | 0.0821 | 0.995 (21.97) | 1.0 | 0.0095 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 809 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=2) | -9.05/-1.06/-10.8 | 63.33 | 1275 | 0.0818 | 1.0 (21.47) | 1.0 | 0.0 | 0.4875 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 810 | sector_etf|donchian(entry_n=55,exit_n=10)+day_of_week(days=3) | -5.34/-0.6/-6.87 | 63.33 | 1263 | 0.0822 | 1.0 (21.3) | 1.0 | 0.0 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 811 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=0) | 1.28/0.15/-3.65 | 63.33 | 1500 | 0.0791 | 0.995 (20.79) | 1.0 | 0.0016 | 0.4975 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 812 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=1) | 3.87/0.41/-3.37 | 63.33 | 1666 | 0.08 | 0.98801 (19.72) | 1.0 | 0.007 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 813 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=2) | -11.55/-1.15/-13.35 | 63.33 | 1651 | 0.08 | 1.0 (20.08) | 1.0 | 0.0 | 0.4945 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 814 | sector_etf|donchian(entry_n=55,exit_n=20)+day_of_week(days=3) | -3.72/-0.33/-7.63 | 63.33 | 1630 | 0.0801 | 1.0 (20.03) | 1.0 | 0.0001 | 0.496 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 815 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=0) | -1.35/-0.21/-3.84 | 63.33 | 950 | 0.0844 | 1.0 (23.21) | 1.0 | 0.0002 | 0.498 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 816 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=1) | 3.56/0.52/-4.03 | 63.33 | 1063 | 0.0858 | 0.999 (22.57) | 1.0 | 0.0113 | 0.496 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 817 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=2) | -6.9/-0.93/-8.33 | 63.33 | 1070 | 0.0853 | 1.0 (22.97) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 818 | sector_etf|donchian(entry_n=100,exit_n=10)+day_of_week(days=3) | -4.26/-0.51/-6.22 | 63.33 | 1063 | 0.0857 | 1.0 (22.87) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 819 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=0) | 0.2/0.04/-3.07 | 63.33 | 1256 | 0.0821 | 1.0 (22.21) | 1.0 | 0.0009 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 820 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=1) | 3.44/0.42/-3.08 | 63.33 | 1412 | 0.0829 | 0.99001 (21.08) | 1.0 | 0.0076 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 821 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=2) | -9.72/-1.08/-11.21 | 63.33 | 1402 | 0.0828 | 1.0 (21.21) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 822 | sector_etf|donchian(entry_n=100,exit_n=20)+day_of_week(days=3) | -2.82/-0.26/-7.06 | 63.33 | 1385 | 0.0833 | 1.0 (21.32) | 1.0 | 0.0001 | 0.4975 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 822

## Engine prereg 20261023_201100_gen_2310232013_000 (gen_2310232013_000, sha256 d7e97c82a1ec): rows #823-826 RESERVED (4 variants). Counted in N.
N_cumulative: 826

## Engine run 20261023_201100_gen_2310232013_000 (gen_2310232013_000): rows #823-826. 0/4 pass. PBO 0.491. Bar applied at N=826. Report: engine/runs/20261023_201100_gen_2310232013_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 823 | defensive|sma_cross(fast=20,slow=50)+vol_regime(max_atr_pct=0.02) | 37.47/1.69/-4.97 | 104.36 | 140 | 0.052 | 0.61638 (41.59) | 1.0 | 0.9876 | 0.5005 | False | beats_buy_hold, cost_stop, holm, spa |
| 824 | defensive|sma_cross(fast=20,slow=200)+vol_regime(max_atr_pct=0.02) | 43.79/1.88/-4.06 | 104.36 | 105 | 0.0511 | 0.4975 (43.4) | 1.0 | 0.9947 | 0.501 | False | beats_buy_hold, cost_stop, holm, spa |
| 825 | defensive|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 104.36 | 0 | inf | 1.0 (56.9) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 826 | defensive|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.02) | 43.73/1.92/-4.28 | 104.36 | 97 | 0.0511 | 0.45954 (41.69) | 1.0 | 0.9957 | 0.5075 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |

N_cumulative: 826

## Engine prereg 20261023_201102_gen_2310232014_000 (gen_2310232014_000, sha256 9366729f6098): rows #827-834 RESERVED (8 variants). Counted in N.
N_cumulative: 834

## Engine run 20261023_201102_gen_2310232014_000 (gen_2310232014_000): rows #827-834. 0/8 pass. PBO 0.216. Bar applied at N=834. Report: engine/runs/20261023_201102_gen_2310232014_000/report.md

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

N_cumulative: 834

## Engine prereg 20261023_201105_gen_2310232015_000 (gen_2310232015_000, sha256 5275e1e2e2ce): rows #835-842 RESERVED (8 variants). Counted in N.
N_cumulative: 842

## Engine run 20261023_201105_gen_2310232015_000 (gen_2310232015_000): rows #835-842. 0/8 pass. PBO 0.271. Bar applied at N=842. Report: engine/runs/20261023_201105_gen_2310232015_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 835 | crypto|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=60) | -2.29/-0.47/-4.38 | 428.6 | 184 | 0.025 | 0.91808 (79.52) | 1.0 | 0.0279 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 836 | crypto|drop_revert(drop=0.05,hold=3,n=5)+rsi_band(hi=60) | 2.16/0.2/-9.31 | 428.6 | 711 | 0.0426 | 0.89011 (167.66) | 1.0 | 0.1816 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 837 | crypto|drop_revert(drop=0.05,hold=5,n=1)+rsi_band(hi=60) | -1.98/-0.28/-4.02 | 428.6 | 179 | 0.0251 | 0.91808 (236.54) | 1.0 | 0.0632 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 838 | crypto|drop_revert(drop=0.05,hold=5,n=5)+rsi_band(hi=60) | 2.08/0.17/-13.08 | 428.6 | 690 | 0.043 | 0.89311 (185.76) | 1.0 | 0.1769 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 839 | crypto|drop_revert(drop=0.15,hold=3,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 840 | crypto|drop_revert(drop=0.15,hold=3,n=5)+rsi_band(hi=60) | -0.37/-0.45/-0.6 | 428.6 | 21 | 0.0132 | 0.93806 (234.93) | 1.0 | 0.0255 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 841 | crypto|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 842 | crypto|drop_revert(drop=0.15,hold=5,n=5)+rsi_band(hi=60) | -0.42/-0.26/-1.37 | 428.6 | 22 | 0.0133 | 0.93207 (271.64) | 1.0 | 0.0785 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 842

## Engine prereg 20261023_201113_gen_2310232016_000 (gen_2310232016_000, sha256 592a49880eb9): rows #843-846 RESERVED (4 variants). Counted in N.
N_cumulative: 846

## Engine run 20261023_201113_gen_2310232016_000 (gen_2310232016_000): rows #843-846. 0/4 pass. PBO 0.609. Bar applied at N=846. Report: engine/runs/20261023_201113_gen_2310232016_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 843 | crypto_d|supertrend(atr_n=7,mult=3) | 5.54/0.28/-29.93 | 268.18 | 75 | 0.0184 | 0.84815 (117.51) | 1.0 | 0.45 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 844 | crypto_d|supertrend(atr_n=7,mult=4) | -1.28/0.18/-27.09 | 268.18 | 53 | 0.0189 | 0.9031 (75.97) | 1.0 | 0.4014 | 0.9045 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 845 | crypto_d|supertrend(atr_n=14,mult=3) | -7.44/0.03/-30.33 | 268.18 | 75 | 0.0183 | 0.93906 (108.86) | 1.0 | 0.3325 | 0.904 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 846 | crypto_d|supertrend(atr_n=14,mult=4) | 5.23/0.28/-24.16 | 268.18 | 47 | 0.0189 | 0.84515 (123.56) | 1.0 | 0.4496 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 846

## Engine prereg 20261023_201115_gen_2310232017_000 (gen_2310232017_000, sha256 83553f7bd162): rows #847-878 RESERVED (32 variants). Counted in N.
N_cumulative: 878

## Engine run 20261023_201115_gen_2310232017_000 (gen_2310232017_000): rows #847-878. 0/32 pass. PBO 0.896. Bar applied at N=878. Report: engine/runs/20261023_201115_gen_2310232017_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 847 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=0) | -0.67/-0.02/-8.28 | 214.9 | 349 | 0.0293 | 1.0 (77.45) | 1.0 | 0.0003 | 0.49 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 848 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=1) | 20.28/0.74/-3.77 | 214.9 | 358 | 0.0298 | 1.0 (77.85) | 1.0 | 0.0013 | 0.495 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 849 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=2) | -14.15/-1.21/-19.49 | 214.9 | 352 | 0.0299 | 1.0 (77.92) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 850 | megacap|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=3) | 12.0/0.96/-4.21 | 214.9 | 355 | 0.0293 | 1.0 (76.2) | 1.0 | 0.0479 | 0.4935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 851 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -3.18/-0.18/-9.93 | 214.9 | 443 | 0.0319 | 1.0 (76.06) | 1.0 | 0.0001 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 852 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 13.45/0.5/-5.64 | 214.9 | 465 | 0.0318 | 0.999 (75.7) | 1.0 | 0.0013 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 853 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -8.41/-0.57/-15.07 | 214.9 | 469 | 0.0322 | 1.0 (76.07) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 854 | megacap|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 11.54/0.79/-4.14 | 214.9 | 462 | 0.0313 | 1.0 (76.11) | 1.0 | 0.0258 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 855 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -2.05/-0.09/-9.93 | 214.9 | 562 | 0.0313 | 1.0 (73.84) | 1.0 | 0.0002 | 0.49 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 856 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 23.9/0.8/-5.25 | 214.9 | 599 | 0.0308 | 0.998 (75.84) | 1.0 | 0.0035 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 857 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -16.03/-1.04/-23.14 | 214.9 | 591 | 0.031 | 1.0 (74.3) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 858 | megacap|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 10.75/0.6/-8.07 | 214.9 | 599 | 0.0306 | 1.0 (73.44) | 1.0 | 0.0153 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 859 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -1.68/-0.07/-9.93 | 214.9 | 682 | 0.033 | 1.0 (73.21) | 1.0 | 0.0002 | 0.4935 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 860 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 23.65/0.75/-6.0 | 214.9 | 734 | 0.0331 | 0.99401 (73.11) | 1.0 | 0.0051 | 0.4935 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 861 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -12.45/-0.67/-20.47 | 214.9 | 744 | 0.0331 | 1.0 (72.57) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 862 | megacap|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 9.46/0.52/-7.49 | 214.9 | 725 | 0.0324 | 1.0 (72.65) | 1.0 | 0.0085 | 0.4875 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 863 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=0) | -4.37/-0.58/-4.88 | 214.9 | 54 | 0.0212 | 1.0 (78.43) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 864 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=1) | 9.25/0.59/-1.96 | 214.9 | 53 | 0.0208 | 1.0 (81.47) | 1.0 | 0.0001 | 0.49 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 865 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=2) | -0.58/-0.15/-2.49 | 214.9 | 50 | 0.0217 | 1.0 (79.69) | 1.0 | 0.0001 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 866 | megacap|drop_revert(drop=0.1,hold=5,n=3)+day_of_week(days=3) | 4.56/0.89/-0.54 | 214.9 | 53 | 0.0203 | 1.0 (80.52) | 1.0 | 0.0001 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 867 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | -4.73/-0.56/-7.01 | 214.9 | 94 | 0.023 | 1.0 (78.89) | 1.0 | 0.0 | 0.494 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 868 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 10.08/0.59/-2.47 | 214.9 | 101 | 0.0238 | 1.0 (80.37) | 1.0 | 0.0003 | 0.4925 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 869 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | 0.63/0.14/-3.28 | 214.9 | 90 | 0.023 | 1.0 (79.94) | 1.0 | 0.0008 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 870 | megacap|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | 4.97/0.72/-1.85 | 214.9 | 101 | 0.0234 | 1.0 (78.21) | 1.0 | 0.0094 | 0.495 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 871 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=0) | -2.22/-0.21/-6.78 | 214.9 | 95 | 0.0212 | 1.0 (78.14) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 872 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=1) | 10.12/0.61/-2.85 | 214.9 | 94 | 0.0212 | 1.0 (80.19) | 1.0 | 0.0002 | 0.4925 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 873 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=2) | -1.82/-0.34/-4.17 | 214.9 | 91 | 0.0218 | 1.0 (80.99) | 1.0 | 0.0001 | 0.4945 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 874 | megacap|drop_revert(drop=0.1,hold=10,n=3)+day_of_week(days=3) | 5.22/0.8/-1.55 | 214.9 | 94 | 0.0212 | 1.0 (80.03) | 1.0 | 0.0046 | 0.493 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 875 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=0) | -4.05/-0.39/-8.13 | 214.9 | 152 | 0.0237 | 1.0 (79.3) | 1.0 | 0.0 | 0.493 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 876 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=1) | 12.08/0.66/-3.08 | 214.9 | 166 | 0.0245 | 1.0 (79.16) | 1.0 | 0.0008 | 0.4935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 877 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=2) | -0.41/-0.05/-4.91 | 214.9 | 155 | 0.024 | 1.0 (79.25) | 1.0 | 0.0003 | 0.494 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 878 | megacap|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=3) | 3.72/0.46/-3.6 | 214.9 | 170 | 0.0239 | 1.0 (74.77) | 1.0 | 0.0033 | 0.4975 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 878

## Engine prereg 20261023_201123_gen_2310232018_000 (gen_2310232018_000, sha256 b1ff3521dc9a): rows #879-886 RESERVED (8 variants). Counted in N.
N_cumulative: 886

## Engine run 20261023_201123_gen_2310232018_000 (gen_2310232018_000): rows #879-886. 0/8 pass. PBO 0.051. Bar applied at N=886. Report: engine/runs/20261023_201123_gen_2310232018_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 879 | sector_etf|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 63.33 | 8 | 0.0161 | 1.0 (28.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 880 | sector_etf|drop_revert(drop=0.1,hold=3,n=3) | 5.2/0.34/-3.57 | 63.33 | 26 | 0.0275 | 0.999 (28.56) | 1.0 | 0.3779 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 881 | sector_etf|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 63.33 | 7 | 0.017 | 1.0 (29.67) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 882 | sector_etf|drop_revert(drop=0.1,hold=5,n=3) | 7.44/0.46/-3.57 | 63.33 | 24 | 0.0279 | 0.996 (28.09) | 1.0 | 0.4747 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 883 | sector_etf|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 63.33 | 3 | 0.0153 | 1.0 (29.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 884 | sector_etf|drop_revert(drop=0.15,hold=3,n=3) | 0.27/0.11/-0.93 | 63.33 | 7 | 0.0197 | 0.99001 (28.64) | 1.0 | 0.2531 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 885 | sector_etf|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 63.33 | 3 | 0.0153 | 1.0 (29.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 886 | sector_etf|drop_revert(drop=0.15,hold=5,n=3) | 0.59/0.22/-0.93 | 63.33 | 7 | 0.0197 | 0.99201 (27.92) | 1.0 | 0.321 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 886

## Engine prereg 20261023_210347_gen_2310232101_000 (gen_2310232101_000, sha256 f7eb3cd8a210): rows #887-894 RESERVED (8 variants). Counted in N.
N_cumulative: 894

## Engine run 20261023_210347_gen_2310232101_000 (gen_2310232101_000): rows #887-894. 0/8 pass. PBO 0.167. Bar applied at N=894. Report: engine/runs/20261023_210347_gen_2310232101_000/report.md

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

N_cumulative: 894

## Engine prereg 20261023_210354_gen_2310232101_001 (gen_2310232101_001, sha256 54f33338cf26): rows #895-898 RESERVED (4 variants). Counted in N.
N_cumulative: 898

## Engine run 20261023_210354_gen_2310232101_001 (gen_2310232101_001): rows #895-898. 0/4 pass. PBO 0.625. Bar applied at N=898. Report: engine/runs/20261023_210354_gen_2310232101_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 895 | crypto_d|donchian(entry_n=55,exit_n=10) | 10.59/0.39/-29.59 | 234.6 | 61 | 0.0177 | 0.84615 (103.89) | 1.0 | 0.5456 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 896 | crypto_d|donchian(entry_n=55,exit_n=20) | 15.44/0.47/-32.96 | 234.6 | 50 | 0.0177 | 0.81718 (111.65) | 1.0 | 0.5852 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 897 | crypto_d|donchian(entry_n=100,exit_n=10) | 15.9/0.55/-21.16 | 234.6 | 39 | 0.0184 | 0.75924 (120.42) | 1.0 | 0.6242 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 898 | crypto_d|donchian(entry_n=100,exit_n=20) | 19.48/0.59/-23.98 | 234.6 | 32 | 0.0186 | 0.72028 (94.3) | 1.0 | 0.6411 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 898

## Engine prereg 20261023_210356_gen_2310232101_002 (gen_2310232101_002, sha256 3c32bc280827): rows #899-906 RESERVED (8 variants). Counted in N.
N_cumulative: 906

## Engine run 20261023_210356_gen_2310232101_002 (gen_2310232101_002): rows #899-906. 0/8 pass. PBO 0.818. Bar applied at N=906. Report: engine/runs/20261023_210356_gen_2310232101_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 899 | crypto_d|drop_revert(drop=0.05,hold=5,n=1) | -28.67/-0.4/-41.04 | 234.6 | 375 | 0.0123 | 0.995 (88.84) | 1.0 | 0.0327 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 900 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | -0.07/0.24/-41.85 | 234.6 | 408 | 0.0136 | 0.87812 (96.97) | 1.0 | 0.1401 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 901 | crypto_d|drop_revert(drop=0.05,hold=10,n=1) | -38.74/-0.43/-49.88 | 234.6 | 208 | 0.0141 | 1.0 (79.32) | 1.0 | 0.0304 | 0.9275 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 902 | crypto_d|drop_revert(drop=0.05,hold=10,n=3) | 8.47/0.38/-52.22 | 234.6 | 217 | 0.0148 | 0.82218 (85.9) | 1.0 | 0.182 | 0.911 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 903 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.82018 (122.73) | 1.0 | 0.2038 | 0.8865 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 904 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.93506 (93.25) | 1.0 | 0.0908 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 905 | crypto_d|drop_revert(drop=0.1,hold=10,n=1) | -0.44/0.12/-24.88 | 234.6 | 97 | 0.0098 | 0.92507 (60.92) | 1.0 | 0.111 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 906 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 11.7/0.39/-33.6 | 234.6 | 187 | 0.0118 | 0.79421 (96.94) | 1.0 | 0.1832 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 906

## Engine prereg 20261023_210401_gen_2310232101_003 (gen_2310232101_003, sha256 4154cd85e362): rows #907-910 RESERVED (4 variants). Counted in N.
N_cumulative: 910

## Engine run 20261023_210401_gen_2310232101_003 (gen_2310232101_003): rows #907-910. 0/4 pass. PBO 0.351. Bar applied at N=910. Report: engine/runs/20261023_210401_gen_2310232101_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 907 | crypto_d|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.0) | 12.82/0.48/-18.2 | 234.6 | 667 | 0.0165 | 0.80919 (98.12) | 1.0 | 0.5171 | 0.8915 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 908 | crypto_d|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | 7.1/0.32/-13.84 | 234.6 | 723 | 0.0165 | 0.81618 (108.73) | 1.0 | 0.4399 | 0.894 | False | beats_buy_hold, holm, dsr, spa |
| 909 | crypto_d|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.0) | 15.11/0.55/-16.45 | 234.6 | 671 | 0.0169 | 0.75524 (95.29) | 1.0 | 0.5497 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 910 | crypto_d|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.0) | 18.52/0.66/-13.84 | 234.6 | 680 | 0.0166 | 0.73626 (60.66) | 1.0 | 0.5995 | 0.8875 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 910

## Engine prereg 20261023_210404_gen_2310232111_000 (gen_2310232111_000, sha256 4ec01582c1cc): rows #911-914 RESERVED (4 variants). Counted in N.
N_cumulative: 914

## Engine run 20261023_210404_gen_2310232111_000 (gen_2310232111_000): rows #911-914. 0/4 pass. PBO 0.092. Bar applied at N=914. Report: engine/runs/20261023_210404_gen_2310232111_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 911 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.52/0.72/-5.74 | 50.2 | 378 | 0.0707 | 0.95205 (21.34) | 1.0 | 0.6922 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 912 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.15/0.58/-7.68 | 50.2 | 299 | 0.0624 | 0.97203 (21.8) | 1.0 | 0.6053 | 0.5175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 913 | sectors|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.02) | 5.87/0.54/-3.21 | 50.2 | 245 | 0.0794 | 0.998 (22.46) | 1.0 | 0.5791 | 0.5045 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 914 | sectors|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.02) | 5.18/0.4/-3.92 | 50.2 | 198 | 0.076 | 1.0 (22.19) | 1.0 | 0.4861 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 914

## Engine prereg 20261023_210406_gen_2310232111_001 (gen_2310232111_001, sha256 d3d408584d13): rows #915-918 RESERVED (4 variants). Counted in N.
N_cumulative: 918

## Engine run 20261023_210406_gen_2310232111_001 (gen_2310232111_001): rows #915-918. 0/4 pass. PBO 0.012. Bar applied at N=918. Report: engine/runs/20261023_210406_gen_2310232111_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 915 | sectors|supertrend(atr_n=7,mult=2) | 15.86/0.7/-8.91 | 50.2 | 602 | 0.0657 | 0.77223 (20.85) | 1.0 | 0.5824 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 916 | sectors|supertrend(atr_n=7,mult=4) | 9.21/0.45/-7.41 | 50.2 | 244 | 0.0672 | 0.97902 (22.34) | 1.0 | 0.4141 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 917 | sectors|supertrend(atr_n=10,mult=2) | 18.34/0.78/-9.43 | 50.2 | 601 | 0.0657 | 0.62238 (20.64) | 1.0 | 0.6347 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 918 | sectors|supertrend(atr_n=10,mult=4) | 8.66/0.42/-8.67 | 50.2 | 243 | 0.0666 | 0.99401 (22.11) | 1.0 | 0.3924 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 918

## Engine prereg 20261023_210409_gen_2310232111_002 (gen_2310232111_002, sha256 2e95d3bd5853): rows #919-926 RESERVED (8 variants). Counted in N.
N_cumulative: 926

## Engine run 20261023_210409_gen_2310232111_002 (gen_2310232111_002): rows #919-926. 0/8 pass. PBO 0.584. Bar applied at N=926. Report: engine/runs/20261023_210409_gen_2310232111_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 919 | sectors|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (22.45) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 920 | sectors|drop_revert(drop=0.1,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 2.81/0.37/-1.55 | 50.2 | 35 | 0.035 | 0.999 (22.85) | 1.0 | 0.2468 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 921 | sectors|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.01) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 922 | sectors|drop_revert(drop=0.1,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 2.76/0.37/-1.55 | 50.2 | 36 | 0.0349 | 0.999 (23.18) | 1.0 | 0.2434 | 0.5005 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 923 | sectors|drop_revert(drop=0.15,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.37) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 924 | sectors|drop_revert(drop=0.15,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | -0.03/-0.01/-0.59 | 50.2 | 4 | 0.0304 | 0.999 (24.29) | 1.0 | 0.108 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 925 | sectors|drop_revert(drop=0.15,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 50.2 | 1 | 0.035 | 1.0 (23.01) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 926 | sectors|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | -0.03/-0.01/-0.59 | 50.2 | 4 | 0.0304 | 0.999 (23.4) | 1.0 | 0.108 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 926

## Engine prereg 20261023_210413_gen_2310232111_003 (gen_2310232111_003, sha256 835b70209494): rows #927-934 RESERVED (8 variants). Counted in N.
N_cumulative: 934

## Engine run 20261023_210413_gen_2310232111_003 (gen_2310232111_003): rows #927-934. 0/8 pass. PBO 0.143. Bar applied at N=934. Report: engine/runs/20261023_210413_gen_2310232111_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 927 | sectors|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=50) | 2.18/0.59/-1.08 | 50.2 | 244 | 0.0779 | 1.0 (22.47) | 1.0 | 0.0512 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 928 | sectors|rsi_revert(entry=5,exit=70,n=5)+trend_sma(n=50) | -0.13/-0.47/-0.2 | 50.2 | 2 | 0.0576 | 1.0 (22.96) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 929 | sectors|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=50) | 1.66/0.4/-1.27 | 50.2 | 293 | 0.0765 | 1.0 (22.37) | 1.0 | 0.0275 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 930 | sectors|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=50) | 0.65/0.81/-0.25 | 50.2 | 22 | 0.0457 | 0.999 (22.99) | 1.0 | 0.0707 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 931 | sectors|rsi_revert(entry=10,exit=70,n=2)+trend_sma(n=50) | 5.35/0.83/-1.92 | 50.2 | 556 | 0.0783 | 0.997 (21.09) | 1.0 | 0.1138 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 932 | sectors|rsi_revert(entry=10,exit=70,n=5)+trend_sma(n=50) | 0.0/0.01/-0.2 | 50.2 | 28 | 0.0587 | 0.999 (22.91) | 1.0 | 0.0054 | 0.4975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 933 | sectors|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=50) | 3.53/0.49/-2.28 | 50.2 | 621 | 0.0775 | 1.0 (20.23) | 1.0 | 0.0385 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 934 | sectors|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=50) | 1.96/0.85/-0.9 | 50.2 | 121 | 0.0603 | 1.0 (22.92) | 1.0 | 0.0958 | 0.501 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 934

## Engine prereg 20261023_210417_gen_2310232121_000 (gen_2310232121_000, sha256 f46570f52396): rows #935-938 RESERVED (4 variants). Counted in N.
N_cumulative: 938

## Engine run 20261023_210417_gen_2310232121_000 (gen_2310232121_000): rows #935-938. 0/4 pass. PBO 0.252. Bar applied at N=938. Report: engine/runs/20261023_210417_gen_2310232121_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 935 | megacap|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 9.45/0.47/-17.47 | 26.77 | 3681 | 0.1261 | 0.76823 (-6.97) | 1.0 | 0.0674 | 0.864 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 936 | megacap|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | -13.32/-0.35/-28.81 | 26.77 | 3232 | 0.129 | 0.87612 (-4.96) | 1.0 | 0.0063 | 0.947 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 937 | megacap|supertrend(atr_n=14,mult=2)+vol_regime(max_atr_pct=0.06) | 9.54/0.48/-16.54 | 26.77 | 3700 | 0.1262 | 0.75824 (-7.52) | 1.0 | 0.0703 | 0.8565 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 938 | megacap|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.06) | -16.81/-0.5/-27.96 | 26.77 | 3241 | 0.1291 | 0.91209 (-4.89) | 1.0 | 0.003 | 0.96 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 938

## Engine prereg 20261023_210420_gen_2310232121_001 (gen_2310232121_001, sha256 52ebbac2de93): rows #939-946 RESERVED (8 variants). Counted in N.
N_cumulative: 946

## Engine run 20261023_210420_gen_2310232121_001 (gen_2310232121_001): rows #939-946. 0/8 pass. PBO 0.005. Bar applied at N=946. Report: engine/runs/20261023_210420_gen_2310232121_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 939 | megacap|rsi_revert(entry=5,exit=60,n=2)+rsi_band(hi=60) | -11.51/-0.92/-15.12 | 26.77 | 2320 | 0.1195 | 0.81918 (0.34) | 1.0 | 0.0 | 0.481 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 940 | megacap|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 3.75/1.16/-1.52 | 26.77 | 68 | 0.095 | 0.87712 (13.17) | 1.0 | 0.005 | 0.8695 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 941 | megacap|rsi_revert(entry=5,exit=70,n=2)+rsi_band(hi=60) | -10.14/-0.69/-13.77 | 26.77 | 2193 | 0.1198 | 0.82817 (1.01) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 942 | megacap|rsi_revert(entry=5,exit=70,n=5)+rsi_band(hi=60) | 5.57/1.36/-1.21 | 26.77 | 67 | 0.0958 | 0.86414 (12.5) | 1.0 | 0.0058 | 0.863 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 943 | megacap|rsi_revert(entry=20,exit=60,n=2)+rsi_band(hi=60) | -18.68/-0.98/-24.61 | 26.77 | 4315 | 0.1213 | 0.42258 (-8.95) | 1.0 | 0.0 | 0.4865 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 944 | megacap|rsi_revert(entry=20,exit=60,n=5)+rsi_band(hi=60) | 8.06/0.53/-10.16 | 26.77 | 1034 | 0.1194 | 0.42857 (7.53) | 1.0 | 0.0004 | 0.855 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 945 | megacap|rsi_revert(entry=20,exit=70,n=2)+rsi_band(hi=60) | -14.19/-0.64/-24.48 | 26.77 | 3912 | 0.1215 | 0.54046 (-6.88) | 1.0 | 0.0 | 0.506 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 946 | megacap|rsi_revert(entry=20,exit=70,n=5)+rsi_band(hi=60) | 14.84/0.72/-11.79 | 26.77 | 904 | 0.1193 | 0.51948 (8.17) | 1.0 | 0.001 | 0.8355 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 946

## Engine prereg 20261023_210424_gen_2310232121_002 (gen_2310232121_002, sha256 38d289afa69e): rows #947-954 RESERVED (8 variants). Counted in N.
N_cumulative: 954

## Engine run 20261023_210424_gen_2310232121_002 (gen_2310232121_002): rows #947-954. 0/8 pass. PBO 0.901. Bar applied at N=954. Report: engine/runs/20261023_210424_gen_2310232121_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 947 | megacap|drop_revert(drop=0.05,hold=5,n=1)+rsi_band(hi=80) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.93407 (12.62) | 1.0 | 0.3289 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 948 | megacap|drop_revert(drop=0.05,hold=5,n=3)+rsi_band(hi=80) | 4.24/0.85/-1.6 | 26.77 | 121 | 0.0558 | 0.81918 (12.59) | 1.0 | 0.5977 | 0.864 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 949 | megacap|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=80) | 2.14/0.38/-3.23 | 26.77 | 34 | 0.0455 | 0.94306 (13.0) | 1.0 | 0.3366 | 0.8755 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 950 | megacap|drop_revert(drop=0.05,hold=10,n=3)+rsi_band(hi=80) | 5.05/0.73/-3.31 | 26.77 | 117 | 0.0558 | 0.5994 (12.48) | 1.0 | 0.5256 | 0.8465 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 951 | megacap|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=80) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.93806 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 952 | megacap|drop_revert(drop=0.15,hold=5,n=3)+rsi_band(hi=80) | 0.89/0.83/0.0 | 26.77 | 9 | 0.0083 | 0.89211 (13.07) | 1.0 | 0.6519 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 953 | megacap|drop_revert(drop=0.15,hold=10,n=1)+rsi_band(hi=80) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.94505 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 954 | megacap|drop_revert(drop=0.15,hold=10,n=3)+rsi_band(hi=80) | 0.83/0.65/-0.38 | 26.77 | 9 | 0.0083 | 0.9031 (12.91) | 1.0 | 0.4832 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 954

## Engine prereg 20261023_210427_gen_2310232131_000 (gen_2310232131_000, sha256 4725db6e2300): rows #955-958 RESERVED (4 variants). Counted in N.
N_cumulative: 958

## Engine run 20261023_210427_gen_2310232131_000 (gen_2310232131_000): rows #955-958. 0/4 pass. PBO 0.494. Bar applied at N=958. Report: engine/runs/20261023_210427_gen_2310232131_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 955 | crypto|supertrend(atr_n=7,mult=3) | -5.1/0.08/-43.8 | 428.6 | 1335 | 0.0991 | 0.86513 (66.17) | 1.0 | 0.3164 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 956 | crypto|supertrend(atr_n=7,mult=4) | 3.91/0.25/-42.89 | 428.6 | 886 | 0.0999 | 0.82418 (68.84) | 1.0 | 0.3922 | 0.9215 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 957 | crypto|supertrend(atr_n=14,mult=3) | 0.35/0.19/-41.76 | 428.6 | 1347 | 0.0966 | 0.8042 (96.41) | 1.0 | 0.3642 | 0.92 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 958 | crypto|supertrend(atr_n=14,mult=4) | -13.24/-0.08/-47.58 | 428.6 | 874 | 0.0969 | 0.94106 (131.92) | 1.0 | 0.2495 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 958

## Engine prereg 20261023_210433_gen_2310232131_001 (gen_2310232131_001, sha256 6eb5ea9eb99c): rows #959-962 RESERVED (4 variants). Counted in N.
N_cumulative: 962

## Engine run 20261023_210433_gen_2310232131_001 (gen_2310232131_001): rows #959-962. 0/4 pass. PBO 0.124. Bar applied at N=962. Report: engine/runs/20261023_210433_gen_2310232131_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 959 | crypto|sma_cross(fast=5,slow=100) | 22.9/0.57/-43.01 | 428.6 | 1314 | 0.1048 | 0.62837 (65.9) | 1.0 | 0.443 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 960 | crypto|sma_cross(fast=5,slow=150) | -0.17/0.19/-40.03 | 428.6 | 1068 | 0.1035 | 0.84815 (164.51) | 1.0 | 0.2733 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 961 | crypto|sma_cross(fast=10,slow=100) | 25.71/0.61/-43.88 | 428.6 | 1018 | 0.1042 | 0.66234 (185.84) | 1.0 | 0.4629 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 962 | crypto|sma_cross(fast=10,slow=150) | 4.55/0.27/-43.06 | 428.6 | 800 | 0.1023 | 0.84815 (151.06) | 1.0 | 0.309 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 962

## Engine prereg 20261023_210437_gen_2310232131_002 (gen_2310232131_002, sha256 0a13b104e1c5): rows #963-970 RESERVED (8 variants). Counted in N.
N_cumulative: 970

## Engine run 20261023_210437_gen_2310232131_002 (gen_2310232131_002): rows #963-970. 0/8 pass. PBO 0.429. Bar applied at N=970. Report: engine/runs/20261023_210437_gen_2310232131_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 963 | crypto|rsi_revert(entry=5,exit=60,n=3)+trend_sma(n=200) | -3.7/-0.67/-4.62 | 428.6 | 289 | 0.1028 | 0.94106 (191.75) | 1.0 | 0.0114 | 0.9115 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 964 | crypto|rsi_revert(entry=5,exit=60,n=5)+trend_sma(n=200) | -2.43/-1.23/-2.68 | 428.6 | 22 | 0.1303 | 0.97702 (231.96) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 965 | crypto|rsi_revert(entry=5,exit=80,n=3)+trend_sma(n=200) | -4.13/-0.5/-10.18 | 428.6 | 411 | 0.0972 | 0.94805 (200.89) | 1.0 | 0.0256 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 966 | crypto|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=200) | -3.25/-1.24/-3.96 | 428.6 | 31 | 0.1157 | 0.96304 (60.82) | 1.0 | 0.0001 | 0.911 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 967 | crypto|rsi_revert(entry=20,exit=60,n=3)+trend_sma(n=200) | -16.1/-0.89/-21.44 | 428.6 | 2405 | 0.1037 | 0.89211 (37.59) | 1.0 | 0.0074 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 968 | crypto|rsi_revert(entry=20,exit=60,n=5)+trend_sma(n=200) | -4.72/-0.32/-11.04 | 428.6 | 937 | 0.1023 | 0.91009 (84.91) | 1.0 | 0.0436 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 969 | crypto|rsi_revert(entry=20,exit=80,n=3)+trend_sma(n=200) | -18.67/-0.73/-28.88 | 428.6 | 2346 | 0.1037 | 0.92607 (62.07) | 1.0 | 0.0124 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 970 | crypto|rsi_revert(entry=20,exit=80,n=5)+trend_sma(n=200) | -12.46/-0.56/-21.61 | 428.6 | 1403 | 0.1023 | 0.92607 (122.48) | 1.0 | 0.0229 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 970

## Engine prereg 20261023_210444_gen_2310232131_003 (gen_2310232131_003, sha256 2d9c6dd75f68): rows #971-990 RESERVED (20 variants). Counted in N.
N_cumulative: 990

## Engine run 20261023_210444_gen_2310232131_003 (gen_2310232131_003): rows #971-990. 0/20 pass. PBO 0.778. Bar applied at N=990. Report: engine/runs/20261023_210444_gen_2310232131_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 971 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -22.42/-0.99/-27.47 | 428.6 | 710 | 0.1058 | 0.99101 (64.15) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 972 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | -13.95/-0.6/-23.15 | 428.6 | 660 | 0.0932 | 0.96404 (147.7) | 1.0 | 0.0002 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 973 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 27.59/1.24/-10.54 | 428.6 | 686 | 0.0932 | 0.7043 (190.35) | 1.0 | 0.0466 | 0.884 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 974 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -5.34/-0.16/-22.24 | 428.6 | 639 | 0.0922 | 0.93207 (83.88) | 1.0 | 0.0009 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 975 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | -7.04/-0.3/-13.48 | 428.6 | 616 | 0.0922 | 0.94106 (86.78) | 1.0 | 0.0004 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 976 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -28.3/-1.39/-33.08 | 428.6 | 495 | 0.1136 | 0.999 (90.75) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 977 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -13.21/-0.61/-23.36 | 428.6 | 463 | 0.0992 | 0.96104 (101.82) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 978 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 10.88/0.62/-11.57 | 428.6 | 500 | 0.0971 | 0.83816 (157.61) | 1.0 | 0.0105 | 0.901 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 979 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 4.35/0.26/-15.89 | 428.6 | 462 | 0.0939 | 0.88811 (73.98) | 1.0 | 0.0032 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 980 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -7.63/-0.42/-13.2 | 428.6 | 448 | 0.0987 | 0.94705 (176.6) | 1.0 | 0.0002 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 981 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=0) | -18.39/-0.78/-23.81 | 428.6 | 721 | 0.1047 | 0.96903 (74.99) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 982 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=1) | -18.23/-0.84/-26.93 | 428.6 | 670 | 0.0923 | 0.97802 (135.9) | 1.0 | 0.0001 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 983 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=2) | 33.3/1.41/-10.83 | 428.6 | 686 | 0.0936 | 0.65534 (168.42) | 1.0 | 0.0691 | 0.8795 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 984 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=3) | -7.75/-0.26/-24.61 | 428.6 | 643 | 0.092 | 0.94006 (115.61) | 1.0 | 0.0006 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 985 | crypto|supertrend(atr_n=14,mult=2)+day_of_week(days=4) | -6.46/-0.26/-12.99 | 428.6 | 627 | 0.0909 | 0.93407 (190.71) | 1.0 | 0.0005 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 986 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=0) | -29.62/-1.42/-35.46 | 428.6 | 515 | 0.1102 | 0.996 (68.52) | 1.0 | 0.0 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 987 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=1) | -16.15/-0.72/-26.68 | 428.6 | 475 | 0.0977 | 0.97403 (191.72) | 1.0 | 0.0001 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 988 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=2) | 10.29/0.61/-12.15 | 428.6 | 505 | 0.0976 | 0.82118 (74.98) | 1.0 | 0.0101 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 989 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=3) | -1.1/0.04/-19.38 | 428.6 | 470 | 0.0939 | 0.93706 (101.54) | 1.0 | 0.0016 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 990 | crypto|supertrend(atr_n=14,mult=4)+day_of_week(days=4) | -6.16/-0.31/-12.03 | 428.6 | 446 | 0.0973 | 0.93207 (77.43) | 1.0 | 0.0004 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 990

## Engine prereg 20261023_220741_gen_2310232201_000 (gen_2310232201_000, sha256 6db8a141afc8): rows #991-998 RESERVED (8 variants). Counted in N.
N_cumulative: 998

## Engine run 20261023_220741_gen_2310232201_000 (gen_2310232201_000): rows #991-998. 0/8 pass. PBO 0.395. Bar applied at N=998. Report: engine/runs/20261023_220741_gen_2310232201_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 991 | crypto_d|rsi_revert(entry=5,exit=70,n=3) | 22.9/1.06/-9.99 | 234.6 | 56 | 0.0127 | 0.76024 (121.35) | 1.0 | 0.4693 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 992 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 2.61/0.46/-3.07 | 234.6 | 4 | 0.0148 | 0.98002 (156.36) | 1.0 | 0.2009 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 993 | crypto_d|rsi_revert(entry=5,exit=80,n=3) | 32.13/1.28/-10.04 | 234.6 | 52 | 0.0139 | 0.64535 (128.22) | 1.0 | 0.5851 | 0.873 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 994 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.98601 (152.1) | 1.0 | 0.1688 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 995 | crypto_d|rsi_revert(entry=20,exit=70,n=3) | 47.68/0.84/-24.91 | 234.6 | 290 | 0.0135 | 0.56044 (78.05) | 1.0 | 0.3703 | 0.835 | False | beats_buy_hold, holm, dsr, spa |
| 996 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 72.94/1.2/-24.27 | 234.6 | 120 | 0.0132 | 0.5025 (79.7) | 1.0 | 0.5423 | 0.837 | False | beats_buy_hold, holm, dsr, spa |
| 997 | crypto_d|rsi_revert(entry=20,exit=80,n=3) | 36.62/0.69/-32.11 | 234.6 | 224 | 0.014 | 0.61738 (99.43) | 1.0 | 0.3046 | 0.8595 | False | beats_buy_hold, holm, dsr, spa |
| 998 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 63.41/0.97/-32.5 | 234.6 | 92 | 0.0134 | 0.53447 (108.57) | 1.0 | 0.4307 | 0.8365 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 998

## Engine prereg 20261023_220747_gen_2310232201_001 (gen_2310232201_001, sha256 dc7c827ce6ad): rows #999-1006 RESERVED (8 variants). Counted in N.
N_cumulative: 1006

## Engine run 20261023_220747_gen_2310232201_001 (gen_2310232201_001): rows #999-1006. 0/8 pass. PBO 0.458. Bar applied at N=1006. Report: engine/runs/20261023_220747_gen_2310232201_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 999 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=100) | 14.29/0.71/-10.48 | 234.6 | 112 | 0.0111 | 0.8042 (119.32) | 1.0 | 0.3496 | 0.884 | False | beats_buy_hold, holm, dsr, spa |
| 1000 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=100) | 16.6/0.77/-10.3 | 234.6 | 130 | 0.0114 | 0.77223 (72.34) | 1.0 | 0.3795 | 0.885 | False | beats_buy_hold, holm, dsr, spa |
| 1001 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=100) | 35.78/1.14/-18.85 | 234.6 | 120 | 0.0117 | 0.62438 (93.15) | 1.0 | 0.5582 | 0.868 | False | beats_buy_hold, holm, dsr, spa |
| 1002 | crypto_d|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=100) | 22.58/0.79/-16.17 | 234.6 | 140 | 0.0122 | 0.72028 (61.37) | 1.0 | 0.3867 | 0.8805 | False | beats_buy_hold, holm, dsr, spa |
| 1003 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=100) | 0.14/0.05/-3.6 | 234.6 | 38 | 0.0095 | 0.96903 (48.04) | 1.0 | 0.1194 | 0.8975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1004 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=100) | 9.08/0.71/-8.11 | 234.6 | 57 | 0.0103 | 0.83716 (61.3) | 1.0 | 0.3526 | 0.888 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1005 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+trend_sma(n=100) | 5.24/0.47/-7.16 | 234.6 | 43 | 0.0101 | 0.91409 (38.8) | 1.0 | 0.2479 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1006 | crypto_d|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=100) | 12.89/0.78/-9.77 | 234.6 | 59 | 0.0109 | 0.8022 (117.92) | 1.0 | 0.3837 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 1006

## Engine prereg 20261023_220753_gen_2310232201_002 (gen_2310232201_002, sha256 0db728858630): rows #1007-1022 RESERVED (16 variants). Counted in N.
N_cumulative: 1022

## Engine run 20261023_220753_gen_2310232201_002 (gen_2310232201_002): rows #1007-1022. 0/16 pass. PBO 0.587. Bar applied at N=1022. Report: engine/runs/20261023_220753_gen_2310232201_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1007 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=1) | 7.38/0.39/-15.92 | 234.6 | 558 | 0.0159 | 0.83217 (74.11) | 1.0 | 0.0852 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1008 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=2) | -12.27/-0.4/-16.2 | 234.6 | 562 | 0.0161 | 0.97103 (106.57) | 1.0 | 0.0115 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1009 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=3) | 2.51/0.19/-17.65 | 234.6 | 558 | 0.0158 | 0.88811 (74.86) | 1.0 | 0.0535 | 0.901 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1010 | crypto_d|supertrend(atr_n=7,mult=3)+day_of_week(days=4) | 4.32/0.35/-7.86 | 234.6 | 550 | 0.0158 | 0.84216 (65.12) | 1.0 | 0.0722 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1011 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | 11.46/0.54/-14.95 | 234.6 | 598 | 0.0153 | 0.8002 (104.0) | 1.0 | 0.1192 | 0.8845 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1012 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | -25.72/-0.93/-25.72 | 234.6 | 600 | 0.0152 | 0.997 (67.33) | 1.0 | 0.0015 | 0.921 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1013 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 0.41/0.11/-22.3 | 234.6 | 597 | 0.015 | 0.88511 (72.96) | 1.0 | 0.0459 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1014 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | 4.18/0.33/-7.53 | 234.6 | 594 | 0.0152 | 0.86314 (92.04) | 1.0 | 0.0751 | 0.895 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1015 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=1) | 5.85/0.32/-16.7 | 234.6 | 533 | 0.0161 | 0.85415 (99.73) | 1.0 | 0.0743 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1016 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=2) | -10.19/-0.27/-16.23 | 234.6 | 539 | 0.0163 | 0.95604 (89.32) | 1.0 | 0.0184 | 0.9045 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1017 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=3) | 3.18/0.21/-17.95 | 234.6 | 530 | 0.0161 | 0.88012 (123.68) | 1.0 | 0.057 | 0.8995 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1018 | crypto_d|supertrend(atr_n=10,mult=3)+day_of_week(days=4) | 1.6/0.16/-9.97 | 234.6 | 518 | 0.0161 | 0.87013 (52.6) | 1.0 | 0.0486 | 0.895 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1019 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | 14.35/0.66/-14.65 | 234.6 | 571 | 0.0154 | 0.77822 (85.59) | 1.0 | 0.1505 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1020 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | -24.57/-0.9/-24.62 | 234.6 | 572 | 0.0156 | 0.995 (99.11) | 1.0 | 0.0017 | 0.9205 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1021 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 0.59/0.12/-24.72 | 234.6 | 570 | 0.0153 | 0.86414 (89.31) | 1.0 | 0.0485 | 0.902 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1022 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | 2.66/0.23/-7.54 | 234.6 | 562 | 0.0153 | 0.85814 (79.52) | 1.0 | 0.0604 | 0.8955 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1022

## Engine prereg 20261023_220757_gen_2310232201_003 (gen_2310232201_003, sha256 3ff324181e84): rows #1023-1030 RESERVED (8 variants). Counted in N.
N_cumulative: 1030

## Engine run 20261023_220757_gen_2310232201_003 (gen_2310232201_003): rows #1023-1030. 0/8 pass. PBO 0.315. Bar applied at N=1030. Report: engine/runs/20261023_220757_gen_2310232201_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1023 | crypto_d|drop_revert(drop=0.05,hold=3,n=1) | 1.02/0.18/-26.82 | 234.6 | 492 | 0.0115 | 0.87512 (87.26) | 1.0 | 0.0674 | 0.8875 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1024 | crypto_d|drop_revert(drop=0.05,hold=3,n=3) | 10.38/0.37/-32.2 | 234.6 | 544 | 0.0126 | 0.81019 (86.43) | 1.0 | 0.1008 | 0.8875 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1025 | crypto_d|drop_revert(drop=0.05,hold=5,n=1) | -28.67/-0.4/-41.04 | 234.6 | 375 | 0.0123 | 0.999 (80.59) | 1.0 | 0.0142 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1026 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | -0.07/0.24/-41.85 | 234.6 | 408 | 0.0136 | 0.89111 (81.86) | 1.0 | 0.0764 | 0.898 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1027 | crypto_d|drop_revert(drop=0.1,hold=3,n=1) | 25.7/1.1/-11.52 | 234.6 | 130 | 0.0089 | 0.66933 (62.49) | 1.0 | 0.3101 | 0.875 | False | beats_buy_hold, holm, dsr, spa |
| 1028 | crypto_d|drop_revert(drop=0.1,hold=3,n=3) | 19.15/0.6/-17.49 | 234.6 | 289 | 0.0105 | 0.74825 (72.08) | 1.0 | 0.1499 | 0.8765 | False | beats_buy_hold, holm, dsr, spa |
| 1029 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.83716 (126.33) | 1.0 | 0.1146 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 1030 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.95105 (107.13) | 1.0 | 0.0459 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

N_cumulative: 1030

## Engine prereg 20261023_220800_gen_2310232211_000 (gen_2310232211_000, sha256 38af5e3e37da): rows #1031-1034 RESERVED (4 variants). Counted in N.
N_cumulative: 1034

## Engine run 20261023_220800_gen_2310232211_000 (gen_2310232211_000): rows #1031-1034. 0/4 pass. PBO 0.225. Bar applied at N=1034. Report: engine/runs/20261023_220800_gen_2310232211_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1031 | sectors|sma_cross(fast=10,slow=150) | 7.96/0.34/-12.02 | 50.2 | 148 | 0.0656 | 0.996 (22.66) | 1.0 | 0.4751 | 0.506 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1032 | sectors|sma_cross(fast=10,slow=200) | 12.77/0.49/-13.04 | 50.2 | 119 | 0.0645 | 0.92308 (23.16) | 1.0 | 0.5767 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1033 | sectors|sma_cross(fast=20,slow=150) | 11.03/0.43/-12.34 | 50.2 | 122 | 0.0696 | 0.95205 (23.11) | 1.0 | 0.5426 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1034 | sectors|sma_cross(fast=20,slow=200) | 16.95/0.61/-11.96 | 50.2 | 90 | 0.0688 | 0.75524 (22.77) | 1.0 | 0.6562 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1034

## Engine prereg 20261023_220802_gen_2310232211_001 (gen_2310232211_001, sha256 531923890a4e): rows #1035-1038 RESERVED (4 variants). Counted in N.
N_cumulative: 1038

## Engine run 20261023_220802_gen_2310232211_001 (gen_2310232211_001): rows #1035-1038. 0/4 pass. PBO 0.635. Bar applied at N=1038. Report: engine/runs/20261023_220802_gen_2310232211_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1035 | sectors|donchian(entry_n=20,exit_n=10)+trend_sma(n=200) | 7.67/0.49/-5.74 | 50.2 | 387 | 0.0703 | 0.99101 (21.9) | 1.0 | 0.5158 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1036 | sectors|donchian(entry_n=20,exit_n=20)+trend_sma(n=200) | 5.59/0.32/-7.86 | 50.2 | 343 | 0.0657 | 0.998 (21.53) | 1.0 | 0.3981 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1037 | sectors|donchian(entry_n=55,exit_n=10)+trend_sma(n=200) | 8.56/0.65/-5.2 | 50.2 | 272 | 0.0773 | 0.99001 (21.88) | 1.0 | 0.6198 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1038 | sectors|donchian(entry_n=55,exit_n=20)+trend_sma(n=200) | 9.0/0.58/-5.86 | 50.2 | 223 | 0.0749 | 0.99201 (21.84) | 1.0 | 0.5734 | 0.508 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1038

## Engine prereg 20261023_220805_gen_2310232211_002 (gen_2310232211_002, sha256 35217c793d2b): rows #1039-1042 RESERVED (4 variants). Counted in N.
N_cumulative: 1042

## Engine run 20261023_220805_gen_2310232211_002 (gen_2310232211_002): rows #1039-1042. 0/4 pass. PBO 0.016. Bar applied at N=1042. Report: engine/runs/20261023_220805_gen_2310232211_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1039 | sectors|supertrend(atr_n=10,mult=2) | 18.34/0.78/-9.43 | 50.2 | 601 | 0.0657 | 0.62737 (20.96) | 1.0 | 0.5489 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1040 | sectors|supertrend(atr_n=10,mult=4) | 8.66/0.42/-8.67 | 50.2 | 243 | 0.0666 | 0.98801 (22.38) | 1.0 | 0.3103 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1041 | sectors|supertrend(atr_n=14,mult=2) | 20.22/0.83/-10.15 | 50.2 | 604 | 0.0654 | 0.4985 (20.79) | 1.0 | 0.5808 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1042 | sectors|supertrend(atr_n=14,mult=4) | 9.33/0.44/-9.81 | 50.2 | 244 | 0.0662 | 0.98601 (22.04) | 1.0 | 0.323 | 0.5115 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1042

## Engine prereg 20261023_220808_gen_2310232211_003 (gen_2310232211_003, sha256 d2975f54503b): rows #1043-1050 RESERVED (8 variants). Counted in N.
N_cumulative: 1050

## Engine run 20261023_220808_gen_2310232211_003 (gen_2310232211_003): rows #1043-1050. 0/8 pass. PBO 0.222. Bar applied at N=1050. Report: engine/runs/20261023_220808_gen_2310232211_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1043 | sectors|rsi_revert(entry=10,exit=60,n=2)+vol_regime(max_atr_pct=0.06) | 15.83/0.8/-5.08 | 50.2 | 983 | 0.0699 | 0.7033 (19.09) | 1.0 | 0.6141 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1044 | sectors|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0626 | 0.997 (23.44) | 1.0 | 0.4843 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1045 | sectors|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 24.64/1.02/-5.5 | 50.2 | 836 | 0.071 | 0.1958 (19.71) | 1.0 | 0.7584 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1046 | sectors|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 11.32/1.19/-2.1 | 50.2 | 85 | 0.0601 | 0.92907 (22.98) | 1.0 | 0.8466 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1047 | sectors|rsi_revert(entry=20,exit=60,n=2)+vol_regime(max_atr_pct=0.06) | 16.85/0.73/-8.14 | 50.2 | 1633 | 0.0703 | 0.45954 (16.33) | 1.0 | 0.5457 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1048 | sectors|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0653 | 0.43357 (21.79) | 1.0 | 0.8176 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1049 | sectors|rsi_revert(entry=20,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 28.11/0.99/-10.59 | 50.2 | 1272 | 0.0709 | 0.04795 (17.69) | 1.0 | 0.7222 | 0.95 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1050 | sectors|rsi_revert(entry=20,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 33.87/1.16/-10.14 | 50.2 | 259 | 0.0674 | 0.02897 (22.08) | 1.0 | 0.8112 | 0.8725 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1050

## Engine prereg 20261023_220811_gen_2310232221_000 (gen_2310232221_000, sha256 fcbc286a5585): rows #1051-1058 RESERVED (8 variants). Counted in N.
N_cumulative: 1058

## Engine run 20261023_220811_gen_2310232221_000 (gen_2310232221_000): rows #1051-1058. 0/8 pass. PBO 0.776. Bar applied at N=1058. Report: engine/runs/20261023_220811_gen_2310232221_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1051 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.92408 (12.9) | 1.0 | 0.2905 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1052 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 2.21/0.38/-2.43 | 26.77 | 123 | 0.0556 | 0.89411 (12.46) | 1.0 | 0.2278 | 0.886 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1053 | megacap|drop_revert(drop=0.05,hold=10,n=1) | 2.14/0.38/-3.23 | 26.77 | 34 | 0.0455 | 0.92707 (12.67) | 1.0 | 0.2318 | 0.8755 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1054 | megacap|drop_revert(drop=0.05,hold=10,n=3) | 5.05/0.73/-3.31 | 26.77 | 116 | 0.0558 | 0.6024 (12.75) | 1.0 | 0.4146 | 0.8465 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1055 | megacap|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.93307 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1056 | megacap|drop_revert(drop=0.15,hold=3,n=3) | 0.79/1.12/0.0 | 26.77 | 9 | 0.0083 | 0.9031 (13.21) | 1.0 | 0.7144 | 0.901 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1057 | megacap|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.94006 (13.17) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1058 | megacap|drop_revert(drop=0.15,hold=10,n=3) | 0.83/0.65/-0.38 | 26.77 | 9 | 0.0083 | 0.8981 (13.08) | 1.0 | 0.3424 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1058

## Engine prereg 20261023_220815_gen_2310232221_001 (gen_2310232221_001, sha256 7df32351d297): rows #1059-1062 RESERVED (4 variants). Counted in N.
N_cumulative: 1062

## Engine run 20261023_220815_gen_2310232221_001 (gen_2310232221_001): rows #1059-1062. 0/4 pass. PBO 0.325. Bar applied at N=1062. Report: engine/runs/20261023_220815_gen_2310232221_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1059 | megacap|donchian(entry_n=20,exit_n=10) | -8.39/-0.34/-14.91 | 26.77 | 220 | 0.1111 | 0.70629 (12.45) | 1.0 | 0.0001 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1060 | megacap|donchian(entry_n=20,exit_n=20) | -1.17/0.03/-16.39 | 26.77 | 159 | 0.1097 | 0.27473 (12.43) | 1.0 | 0.0015 | 0.891 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1061 | megacap|donchian(entry_n=55,exit_n=10) | 7.27/1.3/-1.89 | 26.77 | 41 | 0.1094 | 0.83616 (12.3) | 1.0 | 0.0883 | 0.8435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1062 | megacap|donchian(entry_n=55,exit_n=20) | -3.88/-0.12/-14.84 | 26.77 | 37 | 0.1093 | 0.64935 (13.23) | 1.0 | 0.0005 | 0.914 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1062

## Engine prereg 20261023_220817_gen_2310232221_002 (gen_2310232221_002, sha256 ce5e066d74b9): rows #1063-1070 RESERVED (8 variants). Counted in N.
N_cumulative: 1070

## Engine run 20261023_220817_gen_2310232221_002 (gen_2310232221_002): rows #1063-1070. 0/8 pass. PBO 0.422. Bar applied at N=1070. Report: engine/runs/20261023_220817_gen_2310232221_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1063 | megacap|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.0) | 3.1/0.94/-1.27 | 26.77 | 264 | 0.1095 | 0.86114 (11.78) | 1.0 | 0.5602 | 0.879 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1064 | megacap|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.0) | 1.26/0.62/-0.88 | 26.77 | 50 | 0.0602 | 0.92607 (12.77) | 1.0 | 0.401 | 0.8915 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1065 | megacap|rsi_revert(entry=5,exit=80,n=3)+relvol(min_ratio=1.0) | 3.41/0.85/-1.77 | 26.77 | 368 | 0.1037 | 0.82517 (11.7) | 1.0 | 0.4917 | 0.879 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1066 | megacap|rsi_revert(entry=5,exit=80,n=5)+relvol(min_ratio=1.0) | 1.58/0.7/-0.88 | 26.77 | 102 | 0.0637 | 0.91508 (13.07) | 1.0 | 0.4429 | 0.8895 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1067 | megacap|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.0) | 2.19/0.55/-3.55 | 26.77 | 577 | 0.1157 | 0.82118 (10.89) | 1.0 | 0.429 | 0.8905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1068 | megacap|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.0) | 2.67/0.73/-1.66 | 26.77 | 293 | 0.0995 | 0.85814 (11.78) | 1.0 | 0.4347 | 0.889 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1069 | megacap|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.0) | 2.26/0.48/-2.1 | 26.77 | 756 | 0.113 | 0.76424 (9.64) | 1.0 | 0.3686 | 0.8915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1070 | megacap|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.0) | 0.57/0.14/-2.6 | 26.77 | 493 | 0.1007 | 0.88711 (10.32) | 1.0 | 0.189 | 0.9 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1070

## Engine prereg 20261023_220821_gen_2310232221_003 (gen_2310232221_003, sha256 7055433a713d): rows #1071-1078 RESERVED (8 variants). Counted in N.
N_cumulative: 1078

## Engine run 20261023_220821_gen_2310232221_003 (gen_2310232221_003): rows #1071-1078. 0/8 pass. PBO 0.505. Bar applied at N=1078. Report: engine/runs/20261023_220821_gen_2310232221_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1071 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.91409 (13.07) | 1.0 | 0.5154 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1072 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 2.21/0.38/-2.43 | 26.77 | 123 | 0.0556 | 0.87912 (12.57) | 1.0 | 0.3939 | 0.886 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1073 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.93007 (12.77) | 1.0 | 0.3921 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1074 | megacap|drop_revert(drop=0.05,hold=5,n=3) | 4.24/0.85/-1.6 | 26.77 | 121 | 0.0558 | 0.82717 (13.07) | 1.0 | 0.6601 | 0.864 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1075 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.87/0.42/-0.92 | 26.77 | 9 | 0.0287 | 0.94006 (13.35) | 1.0 | 0.4248 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1076 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 1.67/0.65/-1.25 | 26.77 | 14 | 0.0274 | 0.94106 (13.14) | 1.0 | 0.5426 | 0.8895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1077 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.93/0.37/-1.25 | 26.77 | 9 | 0.0287 | 0.93706 (13.07) | 1.0 | 0.4044 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1078 | megacap|drop_revert(drop=0.1,hold=5,n=3) | 1.56/0.64/-1.11 | 26.77 | 14 | 0.0274 | 0.92507 (13.04) | 1.0 | 0.5368 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1078

## Engine prereg 20261023_220824_gen_2310232231_000 (gen_2310232231_000, sha256 a54739b99307): rows #1079-1082 RESERVED (4 variants). Counted in N.
N_cumulative: 1082

## Engine run 20261023_220824_gen_2310232231_000 (gen_2310232231_000): rows #1079-1082. 0/4 pass. PBO 0.002. Bar applied at N=1082. Report: engine/runs/20261023_220824_gen_2310232231_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1079 | crypto|sma_cross(fast=10,slow=50)+relvol(min_ratio=1.0) | -59.24/-3.32/-61.91 | 428.6 | 9374 | 0.1026 | 0.87013 (-23.64) | 1.0 | 0.0003 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1080 | crypto|sma_cross(fast=10,slow=150)+relvol(min_ratio=1.0) | -62.42/-3.62/-64.2 | 428.6 | 9212 | 0.1029 | 0.94206 (14.87) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1081 | crypto|sma_cross(fast=50,slow=50)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1082 | crypto|sma_cross(fast=50,slow=150)+relvol(min_ratio=1.0) | -60.41/-3.42/-62.17 | 428.6 | 9119 | 0.1019 | 0.90709 (-16.67) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1082

## Engine prereg 20261023_220829_gen_2310232231_001 (gen_2310232231_001, sha256 199e7b1b2524): rows #1083-1090 RESERVED (8 variants). Counted in N.
N_cumulative: 1090

## Engine run 20261023_220829_gen_2310232231_001 (gen_2310232231_001): rows #1083-1090. 0/8 pass. PBO 0.614. Bar applied at N=1090. Report: engine/runs/20261023_220829_gen_2310232231_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1083 | crypto|rsi_revert(entry=10,exit=60,n=2)+trend_sma(n=100) | -22.16/-1.28/-26.8 | 428.6 | 2475 | 0.1011 | 0.92807 (135.7) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1084 | crypto|rsi_revert(entry=10,exit=60,n=5)+trend_sma(n=100) | -2.31/-0.95/-2.58 | 428.6 | 97 | 0.1056 | 0.94805 (82.67) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1085 | crypto|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=100) | -29.65/-1.53/-34.68 | 428.6 | 2605 | 0.1018 | 0.97003 (140.24) | 1.0 | 0.0 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1086 | crypto|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=100) | 2.53/0.46/-6.23 | 428.6 | 341 | 0.1122 | 0.90909 (188.4) | 1.0 | 0.0046 | 0.906 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1087 | crypto|rsi_revert(entry=20,exit=60,n=2)+trend_sma(n=100) | -37.59/-1.9/-39.28 | 428.6 | 4713 | 0.1027 | 0.94206 (32.39) | 1.0 | 0.0 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1088 | crypto|rsi_revert(entry=20,exit=60,n=5)+trend_sma(n=100) | -20.45/-2.16/-22.22 | 428.6 | 845 | 0.098 | 0.98302 (65.6) | 1.0 | 0.0 | 0.917 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1089 | crypto|rsi_revert(entry=20,exit=80,n=2)+trend_sma(n=100) | -35.74/-1.52/-44.08 | 428.6 | 4331 | 0.1034 | 0.93706 (34.51) | 1.0 | 0.0 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1090 | crypto|rsi_revert(entry=20,exit=80,n=5)+trend_sma(n=100) | -23.15/-1.36/-28.09 | 428.6 | 1766 | 0.1029 | 0.95704 (48.28) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1090

## Engine prereg 20261023_220836_gen_2310232231_002 (gen_2310232231_002, sha256 123ab1e939d2): rows #1091-1098 RESERVED (8 variants). Counted in N.
N_cumulative: 1098

## Engine run 20261023_220836_gen_2310232231_002 (gen_2310232231_002): rows #1091-1098. 0/8 pass. PBO 0.277. Bar applied at N=1098. Report: engine/runs/20261023_220836_gen_2310232231_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1091 | crypto|drop_revert(drop=0.05,hold=3,n=3) | 6.45/0.7/-3.45 | 428.6 | 527 | 0.0357 | 0.8991 (216.88) | 1.0 | 0.1586 | 0.903 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1092 | crypto|drop_revert(drop=0.05,hold=3,n=5) | 0.61/0.09/-10.68 | 428.6 | 707 | 0.0427 | 0.89211 (196.03) | 1.0 | 0.0395 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1093 | crypto|drop_revert(drop=0.05,hold=10,n=3) | -4.05/-0.18/-10.63 | 428.6 | 412 | 0.0403 | 0.92507 (160.81) | 1.0 | 0.0173 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1094 | crypto|drop_revert(drop=0.05,hold=10,n=5) | -6.89/-0.2/-17.22 | 428.6 | 577 | 0.0473 | 0.95405 (85.8) | 1.0 | 0.0162 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1095 | crypto|drop_revert(drop=0.1,hold=3,n=3) | 0.46/0.34/-0.71 | 428.6 | 47 | 0.0154 | 0.95804 (233.98) | 1.0 | 0.0556 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1096 | crypto|drop_revert(drop=0.1,hold=3,n=5) | 3.36/0.89/-1.65 | 428.6 | 93 | 0.0216 | 0.88811 (84.31) | 1.0 | 0.2016 | 0.906 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1097 | crypto|drop_revert(drop=0.1,hold=10,n=3) | -1.13/-0.36/-1.92 | 428.6 | 39 | 0.0163 | 0.96104 (196.94) | 1.0 | 0.012 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1098 | crypto|drop_revert(drop=0.1,hold=10,n=5) | 4.28/0.67/-3.04 | 428.6 | 76 | 0.0239 | 0.87812 (237.81) | 1.0 | 0.1306 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1098

## Engine prereg 20261023_220842_gen_2310232231_003 (gen_2310232231_003, sha256 d5dcec326c08): rows #1099-1102 RESERVED (4 variants). Counted in N.
N_cumulative: 1102

## Engine run 20261023_220842_gen_2310232231_003 (gen_2310232231_003): rows #1099-1102. 0/4 pass. PBO 0.555. Bar applied at N=1102. Report: engine/runs/20261023_220842_gen_2310232231_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1099 | crypto|sma_cross(fast=20,slow=50)+trend_sma(n=100) | -24.21/-0.41/-47.22 | 428.6 | 1983 | 0.1073 | 0.95005 (121.13) | 1.0 | 0.0448 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1100 | crypto|sma_cross(fast=20,slow=200)+trend_sma(n=100) | -14.62/-0.17/-42.0 | 428.6 | 1690 | 0.1071 | 0.88911 (141.12) | 1.0 | 0.0789 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1101 | crypto|sma_cross(fast=50,slow=50)+trend_sma(n=100) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1102 | crypto|sma_cross(fast=50,slow=200)+trend_sma(n=100) | 1.81/0.19/-36.56 | 428.6 | 1601 | 0.1085 | 0.75225 (65.65) | 1.0 | 0.1643 | 0.918 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1102

## Engine prereg 20261023_230741_gen_2310232301_000 (gen_2310232301_000, sha256 980434409503): rows #1103-1106 RESERVED (4 variants). Counted in N.
N_cumulative: 1106

## Engine run 20261023_230741_gen_2310232301_000 (gen_2310232301_000): rows #1103-1106. 0/4 pass. PBO 0.585. Bar applied at N=1106. Report: engine/runs/20261023_230741_gen_2310232301_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1103 | crypto_d|donchian(entry_n=55,exit_n=10) | 8.89/0.36/-22.01 | 434.62 | 39 | 0.0203 | 0.87612 (190.04) | 1.0 | 0.5272 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1104 | crypto_d|donchian(entry_n=55,exit_n=20) | 15.81/0.49/-26.31 | 434.62 | 32 | 0.0201 | 0.85015 (128.4) | 1.0 | 0.5885 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1105 | crypto_d|donchian(entry_n=100,exit_n=10) | 4.47/0.26/-16.13 | 434.62 | 25 | 0.0211 | 0.88711 (259.81) | 1.0 | 0.4804 | 0.9085 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1106 | crypto_d|donchian(entry_n=100,exit_n=20) | 9.05/0.38/-18.97 | 434.62 | 21 | 0.0211 | 0.82018 (259.52) | 1.0 | 0.5376 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1106

## Engine prereg 20261023_230747_gen_2310232301_001 (gen_2310232301_001, sha256 037702077bd5): rows #1107-1114 RESERVED (8 variants). Counted in N.
N_cumulative: 1114

## Engine run 20261023_230747_gen_2310232301_001 (gen_2310232301_001): rows #1107-1114. 0/8 pass. PBO 0.163. Bar applied at N=1114. Report: engine/runs/20261023_230747_gen_2310232301_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1107 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+relvol(min_ratio=1.0) | 19.17/0.7/-11.78 | 434.62 | 176 | 0.012 | 0.7962 (88.34) | 1.0 | 0.1831 | 0.8925 | False | beats_buy_hold, holm, dsr, spa |
| 1108 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+relvol(min_ratio=1.0) | 32.74/1.03/-11.78 | 434.62 | 210 | 0.0123 | 0.66034 (77.67) | 1.0 | 0.3053 | 0.882 | False | beats_buy_hold, holm, dsr, spa |
| 1109 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+relvol(min_ratio=1.0) | 49.85/1.31/-11.78 | 434.62 | 253 | 0.0126 | 0.59341 (101.92) | 1.0 | 0.4332 | 0.865 | False | beats_buy_hold, holm, dsr, spa |
| 1110 | crypto_d|drop_revert(drop=0.1,hold=10,n=5)+relvol(min_ratio=1.0) | 57.28/1.45/-11.78 | 434.62 | 289 | 0.0131 | 0.57842 (197.21) | 1.0 | 0.5013 | 0.857 | False | beats_buy_hold, holm, dsr, spa |
| 1111 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+relvol(min_ratio=1.0) | -0.11/0.07/-11.85 | 434.62 | 59 | 0.0102 | 0.92408 (207.01) | 1.0 | 0.0501 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1112 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 12.67/0.56/-11.78 | 434.62 | 104 | 0.0107 | 0.81019 (81.78) | 1.0 | 0.1431 | 0.9 | False | beats_buy_hold, holm, dsr, spa |
| 1113 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.0) | 14.88/0.68/-11.78 | 434.62 | 94 | 0.01 | 0.80519 (224.72) | 1.0 | 0.189 | 0.894 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1114 | crypto_d|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 18.33/0.72/-11.78 | 434.62 | 147 | 0.0108 | 0.76224 (183.9) | 1.0 | 0.1929 | 0.8925 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 1114

## Engine prereg 20261023_230752_gen_2310232301_002 (gen_2310232301_002, sha256 e0c1e48f5e10): rows #1115-1122 RESERVED (8 variants). Counted in N.
N_cumulative: 1122

## Engine run 20261023_230752_gen_2310232301_002 (gen_2310232301_002): rows #1115-1122. 0/8 pass. PBO 0.528. Bar applied at N=1122. Report: engine/runs/20261023_230752_gen_2310232301_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1115 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | 15.43/0.45/-33.32 | 434.62 | 225 | 0.0158 | 0.7962 (132.66) | 1.0 | 0.3473 | 0.9055 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1116 | crypto_d|drop_revert(drop=0.05,hold=5,n=5) | 3.07/0.26/-33.84 | 434.62 | 220 | 0.0163 | 0.8971 (119.47) | 1.0 | 0.2663 | 0.9115 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1117 | crypto_d|drop_revert(drop=0.05,hold=10,n=3) | 23.93/0.55/-43.62 | 434.62 | 134 | 0.0168 | 0.75924 (220.78) | 1.0 | 0.3955 | 0.905 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1118 | crypto_d|drop_revert(drop=0.05,hold=10,n=5) | 32.24/0.64/-40.72 | 434.62 | 131 | 0.0176 | 0.7013 (187.25) | 1.0 | 0.4375 | 0.887 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1119 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -5.0/0.02/-26.11 | 434.62 | 126 | 0.012 | 0.94306 (92.09) | 1.0 | 0.1841 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1120 | crypto_d|drop_revert(drop=0.1,hold=5,n=5) | 17.32/0.51/-20.0 | 434.62 | 144 | 0.012 | 0.80619 (92.0) | 1.0 | 0.3752 | 0.896 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1121 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 14.03/0.44/-26.83 | 434.62 | 102 | 0.0129 | 0.8012 (99.23) | 1.0 | 0.342 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1122 | crypto_d|drop_revert(drop=0.1,hold=10,n=5) | 37.03/0.79/-29.19 | 434.62 | 110 | 0.0134 | 0.69431 (190.81) | 1.0 | 0.5083 | 0.874 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 1122

## Engine prereg 20261023_230754_gen_2310232301_003 (gen_2310232301_003, sha256 42af299efcd8): rows #1123-1130 RESERVED (8 variants). Counted in N.
N_cumulative: 1130

## Engine run 20261023_230754_gen_2310232301_003 (gen_2310232301_003): rows #1123-1130. 0/8 pass. PBO 0.122. Bar applied at N=1130. Report: engine/runs/20261023_230754_gen_2310232301_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1123 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+relvol(min_ratio=1.0) | 12.23/0.84/-4.56 | 434.62 | 60 | 0.0102 | 0.86713 (194.43) | 1.0 | 0.5876 | 0.897 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1124 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+relvol(min_ratio=1.0) | 24.22/0.85/-11.78 | 434.62 | 166 | 0.0121 | 0.74326 (206.5) | 1.0 | 0.5689 | 0.8875 | False | beats_buy_hold, holm, dsr, spa |
| 1125 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+relvol(min_ratio=1.0) | 5.73/0.41/-4.89 | 434.62 | 73 | 0.0107 | 0.90909 (188.45) | 1.0 | 0.3472 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1126 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+relvol(min_ratio=1.0) | 32.74/1.03/-11.78 | 434.62 | 210 | 0.0123 | 0.66134 (69.84) | 1.0 | 0.6525 | 0.882 | False | beats_buy_hold, holm, dsr, spa |
| 1127 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.65/0.81/-0.02 | 434.62 | 13 | 0.0073 | 1.0 (156.74) | 1.0 | 0.5955 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1128 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+relvol(min_ratio=1.0) | 22.86/1.03/-4.96 | 434.62 | 81 | 0.0106 | 0.72128 (70.27) | 1.0 | 0.6848 | 0.8865 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1129 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.0) | 0.65/0.81/-0.02 | 434.62 | 16 | 0.0072 | 1.0 (52.21) | 1.0 | 0.5955 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1130 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 12.67/0.56/-11.78 | 434.62 | 104 | 0.0107 | 0.8012 (68.61) | 1.0 | 0.4314 | 0.9 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 1130

## Engine prereg 20261023_230757_gen_2310232311_000 (gen_2310232311_000, sha256 fc01028d05ba): rows #1131-1162 RESERVED (32 variants). Counted in N.
N_cumulative: 1162

## Engine run 20261023_230757_gen_2310232311_000 (gen_2310232311_000): rows #1131-1162. 0/32 pass. PBO 0.729. Bar applied at N=1162. Report: engine/runs/20261023_230757_gen_2310232311_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1131 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=0) | -2.59/-0.24/-6.56 | 64.05 | 97 | 0.0348 | 0.996 (28.22) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1132 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=1) | 4.58/0.26/-4.44 | 64.05 | 95 | 0.0347 | 0.97003 (28.35) | 1.0 | 0.0019 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1133 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=2) | -3.12/-0.41/-4.52 | 64.05 | 93 | 0.0344 | 0.99401 (28.15) | 1.0 | 0.0002 | 0.5075 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1134 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=3) | -0.14/0.0/-5.57 | 64.05 | 92 | 0.0332 | 0.98601 (27.96) | 1.0 | 0.0022 | 0.5065 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1135 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | -2.97/-0.27/-6.6 | 64.05 | 131 | 0.0387 | 0.996 (27.78) | 1.0 | 0.0001 | 0.506 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1136 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 1.41/0.1/-7.71 | 64.05 | 142 | 0.0378 | 0.98501 (27.55) | 1.0 | 0.0022 | 0.4945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1137 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -6.21/-0.78/-7.18 | 64.05 | 139 | 0.0383 | 0.999 (27.47) | 1.0 | 0.0 | 0.5105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1138 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | -4.14/-0.38/-8.31 | 64.05 | 133 | 0.0363 | 0.999 (27.44) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1139 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -0.46/-0.02/-7.41 | 64.05 | 224 | 0.0351 | 0.98202 (27.3) | 1.0 | 0.0019 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1140 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 5.66/0.3/-5.0 | 64.05 | 241 | 0.036 | 0.94206 (27.3) | 1.0 | 0.0025 | 0.4915 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1141 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -6.62/-0.69/-9.17 | 64.05 | 233 | 0.0357 | 0.999 (26.52) | 1.0 | 0.0 | 0.515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1142 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 7.18/0.58/-5.57 | 64.05 | 234 | 0.0356 | 0.93107 (27.05) | 1.0 | 0.0387 | 0.5045 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1143 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -2.66/-0.19/-7.41 | 64.05 | 290 | 0.0379 | 0.99301 (26.28) | 1.0 | 0.0004 | 0.5055 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1144 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 5.38/0.28/-6.61 | 64.05 | 306 | 0.0385 | 0.94605 (25.85) | 1.0 | 0.0026 | 0.4945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1145 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -5.8/-0.54/-8.53 | 64.05 | 313 | 0.0386 | 0.997 (25.96) | 1.0 | 0.0001 | 0.516 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1146 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 4.16/0.35/-5.57 | 64.05 | 315 | 0.0383 | 0.94306 (26.71) | 1.0 | 0.0142 | 0.506 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1147 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=0) | -2.41/-0.75/-2.41 | 64.05 | 6 | 0.0211 | 0.96004 (30.87) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1148 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=1) | 2.37/0.41/-0.88 | 64.05 | 5 | 0.0232 | 0.88911 (32.05) | 1.0 | 0.0011 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1149 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=2) | -1.23/-0.52/-1.36 | 64.05 | 6 | 0.0172 | 0.95704 (31.93) | 1.0 | 0.0 | 0.504 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1150 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=3) | 0.0/0.0/0.0 | 64.05 | 5 | 0.0127 | 1.0 (22.1) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1151 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=0) | -2.41/-0.75/-2.41 | 64.05 | 12 | 0.0149 | 0.94406 (27.3) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1152 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=1) | 2.37/0.41/-0.88 | 64.05 | 12 | 0.0185 | 0.87313 (31.21) | 1.0 | 0.0011 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1153 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=2) | -1.23/-0.52/-1.36 | 64.05 | 7 | 0.0211 | 0.96603 (31.93) | 1.0 | 0.0 | 0.504 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1154 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=3) | 1.42/0.82/0.0 | 64.05 | 8 | 0.0183 | 0.88911 (31.6) | 1.0 | 0.002 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1155 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=0) | -1.61/-0.48/-2.45 | 64.05 | 16 | 0.0203 | 0.96204 (28.09) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1156 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=1) | 2.68/0.46/-0.88 | 64.05 | 15 | 0.0202 | 0.84615 (30.36) | 1.0 | 0.001 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1157 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=2) | -1.32/-0.5/-1.36 | 64.05 | 12 | 0.0201 | 0.95205 (32.84) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1158 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=3) | 1.47/0.75/-0.36 | 64.05 | 12 | 0.0187 | 0.88611 (30.53) | 1.0 | 0.0135 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1159 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | -1.61/-0.48/-2.45 | 64.05 | 19 | 0.0161 | 0.94705 (29.03) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1160 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | 2.61/0.45/-0.94 | 64.05 | 20 | 0.019 | 0.86314 (30.69) | 1.0 | 0.0012 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1161 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -1.32/-0.5/-1.36 | 64.05 | 19 | 0.0156 | 0.97303 (27.38) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1162 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 1.47/0.75/-0.36 | 64.05 | 21 | 0.0178 | 0.87313 (26.11) | 1.0 | 0.0135 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1162

## Engine prereg 20261023_230804_gen_2310232311_001 (gen_2310232311_001, sha256 71dbf48d178d): rows #1163-1166 RESERVED (4 variants). Counted in N.
N_cumulative: 1166

## Engine run 20261023_230804_gen_2310232311_001 (gen_2310232311_001): rows #1163-1166. 0/4 pass. PBO 0.654. Bar applied at N=1166. Report: engine/runs/20261023_230804_gen_2310232311_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1163 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 14.11/0.7/-9.04 | 64.05 | 120 | 0.0607 | 0.86713 (26.84) | 1.0 | 0.755 | 0.5125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1164 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 20.44/0.8/-9.36 | 64.05 | 103 | 0.0521 | 0.70829 (27.46) | 1.0 | 0.8092 | 0.523 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1165 | sectors|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.02) | 13.33/0.86/-3.81 | 64.05 | 77 | 0.0739 | 0.90509 (27.46) | 1.0 | 0.83 | 0.507 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1166 | sectors|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.02) | 17.26/0.9/-5.9 | 64.05 | 63 | 0.0648 | 0.86014 (28.39) | 1.0 | 0.8499 | 0.5115 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1166

## Engine prereg 20261023_230806_gen_2310232311_002 (gen_2310232311_002, sha256 914dafca32d1): rows #1167-1170 RESERVED (4 variants). Counted in N.
N_cumulative: 1170

## Engine run 20261023_230806_gen_2310232311_002 (gen_2310232311_002): rows #1167-1170. 0/4 pass. PBO 0.254. Bar applied at N=1170. Report: engine/runs/20261023_230806_gen_2310232311_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1167 | sectors|sma_cross(fast=10,slow=50) | 11.55/0.4/-16.09 | 64.05 | 96 | 0.0573 | 0.87013 (26.24) | 1.0 | 0.1676 | 0.5065 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1168 | sectors|sma_cross(fast=10,slow=100) | -2.03/-0.0/-21.21 | 64.05 | 61 | 0.0522 | 0.995 (28.05) | 1.0 | 0.0488 | 0.5205 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1169 | sectors|sma_cross(fast=20,slow=50) | 9.39/0.33/-14.08 | 64.05 | 82 | 0.0565 | 0.92907 (27.21) | 1.0 | 0.1392 | 0.5145 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1170 | sectors|sma_cross(fast=20,slow=100) | 24.62/0.71/-11.42 | 64.05 | 43 | 0.055 | 0.57043 (28.09) | 1.0 | 0.3327 | 0.513 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1170

## Engine prereg 20261023_230809_gen_2310232311_003 (gen_2310232311_003, sha256 10581371e635): rows #1171-1174 RESERVED (4 variants). Counted in N.
N_cumulative: 1174

## Engine run 20261023_230809_gen_2310232311_003 (gen_2310232311_003): rows #1171-1174. 0/4 pass. PBO 0.715. Bar applied at N=1174. Report: engine/runs/20261023_230809_gen_2310232311_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1171 | sectors|supertrend(atr_n=10,mult=2) | 21.23/0.7/-11.24 | 64.05 | 213 | 0.0571 | 0.5964 (25.47) | 1.0 | 0.596 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1172 | sectors|supertrend(atr_n=10,mult=3) | 15.56/0.52/-10.92 | 64.05 | 114 | 0.0562 | 0.80619 (26.75) | 1.0 | 0.4778 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1173 | sectors|supertrend(atr_n=14,mult=2) | 22.71/0.73/-11.76 | 64.05 | 216 | 0.0571 | 0.58042 (26.1) | 1.0 | 0.618 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1174 | sectors|supertrend(atr_n=14,mult=3) | 10.77/0.37/-14.75 | 64.05 | 116 | 0.0555 | 0.88012 (27.06) | 1.0 | 0.3764 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1174

## Engine prereg 20261023_230811_gen_2310232321_000 (gen_2310232321_000, sha256 9a02e314cbd5): rows #1175-1178 RESERVED (4 variants). Counted in N.
N_cumulative: 1178

## Engine run 20261023_230811_gen_2310232321_000 (gen_2310232321_000): rows #1175-1178. 0/4 pass. PBO 0.123. Bar applied at N=1178. Report: engine/runs/20261023_230811_gen_2310232321_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1175 | megacap|sma_cross(fast=5,slow=100)+rsi_band(hi=80) | 11.3/0.96/-4.73 | 51.37 | 59 | 0.1033 | 0.7952 (21.99) | 1.0 | 0.7729 | 0.945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1176 | megacap|sma_cross(fast=5,slow=150)+rsi_band(hi=80) | 11.03/1.11/-7.02 | 51.37 | 37 | 0.0982 | 0.7962 (22.76) | 1.0 | 0.8264 | 0.9385 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1177 | megacap|sma_cross(fast=10,slow=100)+rsi_band(hi=80) | 14.68/1.22/-4.4 | 51.37 | 54 | 0.1097 | 0.67133 (21.44) | 1.0 | 0.8567 | 0.932 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1178 | megacap|sma_cross(fast=10,slow=150)+rsi_band(hi=80) | 10.48/1.06/-7.33 | 51.37 | 35 | 0.1065 | 0.79021 (23.05) | 1.0 | 0.808 | 0.9405 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1178

## Engine prereg 20261023_230814_gen_2310232321_001 (gen_2310232321_001, sha256 be0afb40d570): rows #1179-1186 RESERVED (8 variants). Counted in N.
N_cumulative: 1186

## Engine run 20261023_230814_gen_2310232321_001 (gen_2310232321_001): rows #1179-1186. 0/8 pass. PBO 0.6. Bar applied at N=1186. Report: engine/runs/20261023_230814_gen_2310232321_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1179 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.74/0.2/-1.83 | 51.37 | 4 | 0.007 | 0.97702 (23.41) | 1.0 | 0.077 | 0.9645 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1180 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 0.69/0.17/-2.5 | 51.37 | 5 | 0.0082 | 0.96603 (22.9) | 1.0 | 0.0789 | 0.965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1181 | megacap|drop_revert(drop=0.1,hold=10,n=1) | 1.51/0.36/-1.91 | 51.37 | 4 | 0.007 | 0.95604 (22.96) | 1.0 | 0.098 | 0.9595 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1182 | megacap|drop_revert(drop=0.1,hold=10,n=3) | 2.08/0.46/-1.8 | 51.37 | 5 | 0.0082 | 0.97003 (22.59) | 1.0 | 0.1232 | 0.9575 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1183 | megacap|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 51.37 | 2 | 0.004 | 1.0 (34.92) | 1.0 | 0.0 | 0.9715 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1184 | megacap|drop_revert(drop=0.15,hold=3,n=3) | 0.63/0.81/0.0 | 51.37 | 3 | 0.0041 | 0.93107 (22.2) | 1.0 | 0.1101 | 0.9705 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1185 | megacap|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 51.37 | 2 | 0.004 | 1.0 (34.92) | 1.0 | 0.0 | 0.9715 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1186 | megacap|drop_revert(drop=0.15,hold=10,n=3) | -0.4/-0.39/-0.76 | 51.37 | 3 | 0.0041 | 1.0 (23.22) | 1.0 | 0.0071 | 0.971 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1186

## Engine prereg 20261023_230817_gen_2310232321_002 (gen_2310232321_002, sha256 0ce23607530f): rows #1187-1190 RESERVED (4 variants). Counted in N.
N_cumulative: 1190

## Engine run 20261023_230817_gen_2310232321_002 (gen_2310232321_002): rows #1187-1190. 0/4 pass. PBO 0.238. Bar applied at N=1190. Report: engine/runs/20261023_230817_gen_2310232321_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1187 | megacap|sma_cross(fast=10,slow=50) | -2.64/-0.13/-13.2 | 51.37 | 134 | 0.1158 | 0.96404 (21.51) | 1.0 | 0.0008 | 0.5055 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1188 | megacap|sma_cross(fast=10,slow=100) | 14.16/1.18/-4.4 | 51.37 | 41 | 0.1117 | 0.71229 (22.29) | 1.0 | 0.0849 | 0.934 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1189 | megacap|sma_cross(fast=20,slow=50) | 1.13/0.12/-16.11 | 51.37 | 120 | 0.1196 | 0.93806 (20.95) | 1.0 | 0.0026 | 0.9715 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1190 | megacap|sma_cross(fast=20,slow=100) | 11.59/0.95/-5.7 | 51.37 | 38 | 0.1086 | 0.77522 (22.54) | 1.0 | 0.0498 | 0.941 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1190

## Engine prereg 20261023_230819_gen_2310232321_003 (gen_2310232321_003, sha256 58e4b0fb9ffa): rows #1191-1206 RESERVED (16 variants). Counted in N.
N_cumulative: 1206

## Engine run 20261023_230819_gen_2310232321_003 (gen_2310232321_003): rows #1191-1206. 0/16 pass. PBO 0.258. Bar applied at N=1206. Report: engine/runs/20261023_230819_gen_2310232321_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1191 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=0) | 5.47/1.09/-3.98 | 51.37 | 98 | 0.1194 | 0.8961 (21.7) | 1.0 | 0.0012 | 0.9465 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1192 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=1) | -4.59/-0.64/-9.55 | 51.37 | 119 | 0.1176 | 0.99201 (21.42) | 1.0 | 0.0 | 0.5075 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1193 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=2) | 9.93/1.35/-3.16 | 51.37 | 127 | 0.1183 | 0.83816 (22.08) | 1.0 | 0.0037 | 0.94 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1194 | megacap|sma_cross(fast=5,slow=50)+day_of_week(days=3) | -8.07/-1.19/-8.28 | 51.37 | 119 | 0.1089 | 0.99301 (21.61) | 1.0 | 0.0 | 0.5155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1195 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=0) | 1.4/0.38/-3.56 | 51.37 | 34 | 0.1087 | 0.93906 (21.49) | 1.0 | 0.0001 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1196 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=1) | -2.73/-0.53/-6.34 | 51.37 | 37 | 0.1052 | 0.98002 (22.13) | 1.0 | 0.0 | 0.51 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1197 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=2) | 11.73/1.97/-2.44 | 51.37 | 39 | 0.1139 | 0.78422 (21.84) | 1.0 | 0.0138 | 0.9325 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1198 | megacap|sma_cross(fast=5,slow=150)+day_of_week(days=3) | -0.95/-0.24/-3.1 | 51.37 | 40 | 0.1044 | 0.96703 (23.13) | 1.0 | 0.0 | 0.97 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1199 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=0) | 2.55/0.44/-6.7 | 51.37 | 102 | 0.1151 | 0.92308 (20.91) | 1.0 | 0.0001 | 0.961 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1200 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=1) | -4.5/-0.66/-9.49 | 51.37 | 109 | 0.1188 | 0.97902 (20.39) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1201 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=2) | 11.24/1.5/-4.24 | 51.37 | 117 | 0.1216 | 0.78322 (21.76) | 1.0 | 0.0046 | 0.945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1202 | megacap|sma_cross(fast=20,slow=50)+day_of_week(days=3) | -4.84/-0.78/-5.06 | 51.37 | 114 | 0.1135 | 0.98102 (21.76) | 1.0 | 0.0 | 0.5205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1203 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=0) | 2.64/0.7/-3.39 | 51.37 | 34 | 0.1087 | 0.92108 (21.96) | 1.0 | 0.0006 | 0.963 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1204 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=1) | -4.29/-0.78/-7.94 | 51.37 | 37 | 0.1052 | 0.99101 (22.4) | 1.0 | 0.0 | 0.508 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1205 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=2) | 9.95/1.66/-2.93 | 51.37 | 40 | 0.1089 | 0.84316 (22.47) | 1.0 | 0.0049 | 0.9435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1206 | megacap|sma_cross(fast=20,slow=150)+day_of_week(days=3) | -0.27/-0.06/-2.69 | 51.37 | 38 | 0.1075 | 0.96204 (23.72) | 1.0 | 0.0 | 0.968 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1206

## Engine prereg 20261023_230824_gen_2310232331_000 (gen_2310232331_000, sha256 b3b63b1c2030): rows #1207-1210 RESERVED (4 variants). Counted in N.
N_cumulative: 1210

## Engine run 20261023_230824_gen_2310232331_000 (gen_2310232331_000): rows #1207-1210. 0/4 pass. PBO 0.749. Bar applied at N=1210. Report: engine/runs/20261023_230824_gen_2310232331_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1207 | crypto|sma_cross(fast=5,slow=50)+trend_sma(n=50) | 7.71/0.32/-43.26 | 428.6 | 3073 | 0.1048 | 0.61439 (46.99) | 1.0 | 0.2932 | 0.916 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1208 | crypto|sma_cross(fast=5,slow=200)+trend_sma(n=50) | -3.75/0.07/-35.87 | 428.6 | 2603 | 0.1078 | 0.76424 (131.64) | 1.0 | 0.1984 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1209 | crypto|sma_cross(fast=10,slow=50)+trend_sma(n=50) | 13.0/0.41/-41.74 | 428.6 | 2884 | 0.1049 | 0.60839 (59.58) | 1.0 | 0.3326 | 0.9155 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1210 | crypto|sma_cross(fast=10,slow=200)+trend_sma(n=50) | -10.15/-0.09/-38.91 | 428.6 | 2499 | 0.1076 | 0.82018 (126.75) | 1.0 | 0.1501 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1210

## Engine prereg 20261023_230829_gen_2310232331_001 (gen_2310232331_001, sha256 e216f09c887b): rows #1211-1214 RESERVED (4 variants). Counted in N.
N_cumulative: 1214

## Engine run 20261023_230829_gen_2310232331_001 (gen_2310232331_001): rows #1211-1214. 0/4 pass. PBO 0.787. Bar applied at N=1214. Report: engine/runs/20261023_230829_gen_2310232331_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1211 | crypto|sma_cross(fast=10,slow=100)+rsi_band(hi=60) | -23.86/-0.62/-41.52 | 428.6 | 4134 | 0.1022 | 0.8002 (98.52) | 1.0 | 0.0852 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1212 | crypto|sma_cross(fast=10,slow=150)+rsi_band(hi=60) | -33.83/-0.94/-47.04 | 428.6 | 3783 | 0.1018 | 0.91808 (25.06) | 1.0 | 0.0378 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1213 | crypto|sma_cross(fast=20,slow=100)+rsi_band(hi=60) | -24.82/-0.61/-41.68 | 428.6 | 3687 | 0.1021 | 0.86014 (78.91) | 1.0 | 0.0852 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1214 | crypto|sma_cross(fast=20,slow=150)+rsi_band(hi=60) | -28.0/-0.7/-41.45 | 428.6 | 3416 | 0.1018 | 0.91409 (110.64) | 1.0 | 0.0695 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1214

## Engine prereg 20261023_230833_gen_2310232331_002 (gen_2310232331_002, sha256 a0a2c0b5f2a7): rows #1215-1254 RESERVED (40 variants). Counted in N.
N_cumulative: 1254

## Engine run 20261023_230833_gen_2310232331_002 (gen_2310232331_002): rows #1215-1254. 0/40 pass. PBO 0.351. Bar applied at N=1254. Report: engine/runs/20261023_230833_gen_2310232331_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1215 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=0) | -14.57/-0.91/-17.12 | 428.6 | 970 | 0.1017 | 0.95405 (169.18) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1216 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=1) | -11.08/-0.75/-14.59 | 428.6 | 925 | 0.0906 | 0.94306 (133.31) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1217 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=2) | 13.48/1.31/-6.06 | 428.6 | 942 | 0.0938 | 0.77722 (171.22) | 1.0 | 0.0245 | 0.902 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1218 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=3) | -9.03/-0.59/-11.56 | 428.6 | 951 | 0.09 | 0.93506 (91.41) | 1.0 | 0.0 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1219 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=4) | -4.71/-0.43/-6.42 | 428.6 | 908 | 0.091 | 0.91808 (95.46) | 1.0 | 0.0 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1220 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=0) | -1.96/-0.09/-10.87 | 428.6 | 468 | 0.0967 | 0.92208 (210.43) | 1.0 | 0.0001 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1221 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=1) | -8.43/-0.65/-12.14 | 428.6 | 414 | 0.0916 | 0.95704 (69.64) | 1.0 | 0.0 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1222 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=2) | 6.32/0.91/-4.88 | 428.6 | 414 | 0.0884 | 0.87413 (192.63) | 1.0 | 0.008 | 0.907 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1223 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=3) | 2.11/0.28/-6.45 | 428.6 | 413 | 0.087 | 0.9031 (99.46) | 1.0 | 0.0007 | 0.9075 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1224 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=4) | 6.02/0.57/-7.04 | 428.6 | 413 | 0.0819 | 0.87213 (83.45) | 1.0 | 0.0016 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1225 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=0) | -12.84/-0.67/-17.04 | 428.6 | 946 | 0.1016 | 0.95504 (82.96) | 1.0 | 0.0 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1226 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=1) | -9.78/-0.64/-15.01 | 428.6 | 892 | 0.0902 | 0.94406 (180.41) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1227 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=2) | 19.84/1.7/-6.19 | 428.6 | 926 | 0.0933 | 0.71329 (87.96) | 1.0 | 0.0544 | 0.899 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1228 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=3) | -10.48/-0.65/-14.05 | 428.6 | 927 | 0.0902 | 0.94505 (112.8) | 1.0 | 0.0 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1229 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=4) | 3.26/0.29/-6.59 | 428.6 | 896 | 0.0909 | 0.86713 (175.3) | 1.0 | 0.0006 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1230 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=0) | -3.47/-0.16/-13.34 | 428.6 | 480 | 0.0981 | 0.91708 (84.99) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1231 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=1) | -6.19/-0.43/-14.08 | 428.6 | 438 | 0.0903 | 0.93906 (83.08) | 1.0 | 0.0 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1232 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=2) | 11.51/1.5/-5.35 | 428.6 | 427 | 0.0894 | 0.84216 (72.2) | 1.0 | 0.0404 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1233 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=3) | -3.52/-0.3/-9.46 | 428.6 | 428 | 0.0865 | 0.94106 (153.34) | 1.0 | 0.0 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1234 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=4) | 1.08/0.13/-11.56 | 428.6 | 426 | 0.0846 | 0.91508 (102.75) | 1.0 | 0.0004 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1235 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=0) | -22.69/-1.18/-27.76 | 428.6 | 1548 | 0.1027 | 0.97602 (149.58) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1236 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=1) | -11.59/-0.61/-15.49 | 428.6 | 1573 | 0.0937 | 0.92707 (133.3) | 1.0 | 0.0 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1237 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=2) | 22.27/1.61/-5.44 | 428.6 | 1542 | 0.0922 | 0.65834 (66.45) | 1.0 | 0.0437 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1238 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=3) | -17.06/-1.04/-18.19 | 428.6 | 1547 | 0.0912 | 0.93606 (79.99) | 1.0 | 0.0 | 0.9185 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1239 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=4) | -4.73/-0.3/-9.69 | 428.6 | 1462 | 0.0923 | 0.87812 (96.16) | 1.0 | 0.0 | 0.9115 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1240 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=0) | -12.33/-0.59/-18.54 | 428.6 | 889 | 0.1017 | 0.95504 (77.5) | 1.0 | 0.0 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1241 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=1) | -9.17/-0.53/-14.37 | 428.6 | 849 | 0.0904 | 0.92807 (76.33) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1242 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=2) | 16.05/1.4/-5.72 | 428.6 | 893 | 0.0941 | 0.76224 (83.12) | 1.0 | 0.0269 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1243 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=3) | -15.63/-1.12/-19.61 | 428.6 | 882 | 0.0902 | 0.96503 (74.72) | 1.0 | 0.0 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1244 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=4) | 5.26/0.43/-7.26 | 428.6 | 826 | 0.0886 | 0.84515 (167.1) | 1.0 | 0.0012 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1245 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=0) | -20.97/-0.95/-28.89 | 428.6 | 1436 | 0.1043 | 0.96903 (181.03) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1246 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=1) | -6.6/-0.29/-12.86 | 428.6 | 1440 | 0.093 | 0.88112 (88.11) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1247 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=2) | 28.57/1.78/-6.94 | 428.6 | 1444 | 0.0931 | 0.61638 (93.2) | 1.0 | 0.0578 | 0.8925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1248 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=3) | -17.5/-0.97/-20.67 | 428.6 | 1448 | 0.0918 | 0.95504 (119.86) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1249 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=4) | 3.7/0.28/-8.73 | 428.6 | 1389 | 0.0927 | 0.8022 (61.87) | 1.0 | 0.0006 | 0.908 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1250 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=0) | -9.39/-0.36/-21.04 | 428.6 | 840 | 0.1019 | 0.94705 (75.93) | 1.0 | 0.0 | 0.9155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1251 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=1) | -7.58/-0.37/-16.5 | 428.6 | 806 | 0.0915 | 0.93007 (207.47) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1252 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=2) | 17.86/1.36/-7.77 | 428.6 | 839 | 0.093 | 0.73526 (133.87) | 1.0 | 0.0269 | 0.8985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1253 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=3) | -25.27/-1.63/-26.5 | 428.6 | 825 | 0.0904 | 0.99301 (197.0) | 1.0 | 0.0 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1254 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=4) | 6.89/0.49/-8.91 | 428.6 | 795 | 0.0886 | 0.82717 (66.49) | 1.0 | 0.0019 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1254

## Engine prereg 20261023_230901_gen_2310232331_003 (gen_2310232331_003, sha256 352d085d4b23): rows #1255-1262 RESERVED (8 variants). Counted in N.
N_cumulative: 1262

## Engine run 20261023_230901_gen_2310232331_003 (gen_2310232331_003): rows #1255-1262. 0/8 pass. PBO 0.489. Bar applied at N=1262. Report: engine/runs/20261023_230901_gen_2310232331_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1255 | crypto|rsi_revert(entry=10,exit=70,n=2)+rsi_band(hi=60) | -9.95/-0.11/-25.26 | 428.6 | 5375 | 0.1008 | 0.59441 (24.69) | 1.0 | 0.1936 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1256 | crypto|rsi_revert(entry=10,exit=70,n=3)+rsi_band(hi=60) | -16.7/-0.34/-30.56 | 428.6 | 2133 | 0.0977 | 0.91508 (131.27) | 1.0 | 0.1194 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1257 | crypto|rsi_revert(entry=10,exit=80,n=2)+rsi_band(hi=60) | -21.16/-0.32/-37.99 | 428.6 | 4786 | 0.1015 | 0.75824 (38.05) | 1.0 | 0.1282 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1258 | crypto|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=60) | -18.56/-0.28/-33.19 | 428.6 | 1849 | 0.0991 | 0.92408 (64.25) | 1.0 | 0.1369 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1259 | crypto|rsi_revert(entry=20,exit=70,n=2)+rsi_band(hi=60) | -32.9/-0.63/-44.6 | 428.6 | 8290 | 0.1023 | 0.55245 (-22.11) | 1.0 | 0.0651 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1260 | crypto|rsi_revert(entry=20,exit=70,n=3)+rsi_band(hi=60) | -26.85/-0.45/-44.01 | 428.6 | 4242 | 0.1018 | 0.84216 (91.76) | 1.0 | 0.098 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1261 | crypto|rsi_revert(entry=20,exit=80,n=2)+rsi_band(hi=60) | -32.94/-0.53/-50.85 | 428.6 | 7042 | 0.1032 | 0.66733 (-10.65) | 1.0 | 0.0822 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1262 | crypto|rsi_revert(entry=20,exit=80,n=3)+rsi_band(hi=60) | -16.76/-0.12/-41.98 | 428.6 | 3426 | 0.1017 | 0.7952 (27.3) | 1.0 | 0.1901 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1262

## Engine prereg 20261024_000528_gen_2410240001_000 (gen_2410240001_000, sha256 3c9ad29588f4): rows #1263-1266 RESERVED (4 variants). Counted in N.
N_cumulative: 1266

## Engine run 20261024_000528_gen_2410240001_000 (gen_2410240001_000): rows #1263-1266. 0/4 pass. PBO 0.97. Bar applied at N=1266. Report: engine/runs/20261024_000528_gen_2410240001_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1263 | crypto_d|supertrend(atr_n=10,mult=3)+rsi_band(hi=80) | -4.63/0.11/-34.95 | 234.6 | 146 | 0.0162 | 0.93806 (75.0) | 1.0 | 0.3777 | 0.904 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1264 | crypto_d|supertrend(atr_n=10,mult=4)+rsi_band(hi=80) | 3.99/0.28/-31.71 | 234.6 | 114 | 0.0172 | 0.88012 (82.16) | 1.0 | 0.4534 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1265 | crypto_d|supertrend(atr_n=14,mult=3)+rsi_band(hi=80) | -4.84/0.1/-33.24 | 234.6 | 146 | 0.0163 | 0.95504 (73.17) | 1.0 | 0.3695 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1266 | crypto_d|supertrend(atr_n=14,mult=4)+rsi_band(hi=80) | 6.97/0.32/-30.7 | 234.6 | 109 | 0.017 | 0.87013 (69.92) | 1.0 | 0.4738 | 0.9005 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1266

## Engine prereg 20261024_000533_gen_2410240001_001 (gen_2410240001_001, sha256 f88f83f52866): rows #1267-1298 RESERVED (32 variants). Counted in N.
N_cumulative: 1298

## Engine run 20261024_000533_gen_2410240001_001 (gen_2410240001_001): rows #1267-1298. 0/32 pass. PBO 0.702. Bar applied at N=1298. Report: engine/runs/20261024_000533_gen_2410240001_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1267 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=0) | -5.04/-0.36/-9.61 | 234.6 | 247 | 0.0098 | 0.92008 (80.45) | 1.0 | 0.0008 | 0.9005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1268 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=1) | 26.65/1.16/-8.41 | 234.6 | 300 | 0.0106 | 0.68731 (72.73) | 1.0 | 0.032 | 0.87 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1269 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=2) | -15.72/-0.74/-20.82 | 234.6 | 328 | 0.0111 | 0.97902 (75.64) | 1.0 | 0.0005 | 0.9125 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1270 | crypto_d|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=3) | -1.16/0.02/-13.76 | 234.6 | 329 | 0.0111 | 0.91409 (71.62) | 1.0 | 0.0032 | 0.8985 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1271 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | -11.63/-0.59/-18.63 | 234.6 | 447 | 0.0119 | 0.96603 (114.43) | 1.0 | 0.0003 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1272 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 34.89/1.13/-6.89 | 234.6 | 467 | 0.012 | 0.62338 (76.54) | 1.0 | 0.0458 | 0.866 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1273 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -8.12/-0.26/-21.22 | 234.6 | 460 | 0.0121 | 0.93207 (81.39) | 1.0 | 0.0013 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1274 | crypto_d|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | 5.04/0.31/-10.77 | 234.6 | 456 | 0.0118 | 0.86513 (90.76) | 1.0 | 0.0082 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1275 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=0) | -4.44/-0.22/-8.24 | 234.6 | 404 | 0.0107 | 0.92807 (104.9) | 1.0 | 0.0013 | 0.902 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1276 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=1) | 9.21/0.45/-11.79 | 234.6 | 414 | 0.0108 | 0.82118 (69.91) | 1.0 | 0.0084 | 0.8865 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1277 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=2) | -23.25/-1.08/-28.27 | 234.6 | 405 | 0.0108 | 0.995 (93.92) | 1.0 | 0.0001 | 0.92 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1278 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=3) | -1.6/0.02/-14.62 | 234.6 | 450 | 0.011 | 0.92707 (94.92) | 1.0 | 0.0031 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1279 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -9.84/-0.44/-15.31 | 234.6 | 571 | 0.0122 | 0.95405 (77.71) | 1.0 | 0.0005 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1280 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 40.02/1.19/-10.62 | 234.6 | 580 | 0.0123 | 0.58342 (73.27) | 1.0 | 0.0572 | 0.8595 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1281 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -11.26/-0.35/-21.28 | 234.6 | 568 | 0.0123 | 0.95405 (96.23) | 1.0 | 0.0009 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1282 | crypto_d|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 4.04/0.25/-11.31 | 234.6 | 587 | 0.0123 | 0.84416 (92.05) | 1.0 | 0.0067 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1283 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=0) | -3.77/-0.67/-4.92 | 234.6 | 63 | 0.0081 | 0.95105 (67.18) | 1.0 | 0.0 | 0.9005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1284 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=1) | 13.74/0.86/-5.82 | 234.6 | 65 | 0.0089 | 0.8042 (66.86) | 1.0 | 0.0056 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1285 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=2) | 3.32/0.39/-5.12 | 234.6 | 71 | 0.0088 | 0.93606 (125.72) | 1.0 | 0.0056 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1286 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+day_of_week(days=3) | 2.1/1.29/-0.03 | 234.6 | 58 | 0.0082 | 0.94605 (152.54) | 1.0 | 0.0067 | 0.8965 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1287 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=0) | 1.03/0.12/-11.12 | 234.6 | 240 | 0.01 | 0.88711 (64.3) | 1.0 | 0.0042 | 0.898 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1288 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=1) | 8.92/0.51/-6.22 | 234.6 | 229 | 0.0101 | 0.84416 (78.49) | 1.0 | 0.0092 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1289 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=2) | -7.26/-0.37/-15.12 | 234.6 | 222 | 0.0102 | 0.95005 (82.73) | 1.0 | 0.0015 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1290 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+day_of_week(days=3) | 11.01/1.01/-4.48 | 234.6 | 215 | 0.0099 | 0.82617 (106.89) | 1.0 | 0.0368 | 0.888 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1291 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=0) | -6.21/-0.96/-7.32 | 234.6 | 103 | 0.0081 | 0.95704 (99.15) | 1.0 | 0.0 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1292 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=1) | 9.78/0.62/-5.82 | 234.6 | 102 | 0.0086 | 0.83017 (109.17) | 1.0 | 0.0057 | 0.889 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1293 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=2) | -3.77/-0.33/-11.62 | 234.6 | 94 | 0.0085 | 0.95005 (107.06) | 1.0 | 0.0013 | 0.9005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1294 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=3) | 1.8/0.3/-3.42 | 234.6 | 97 | 0.0084 | 0.90809 (126.17) | 1.0 | 0.0069 | 0.895 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1295 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | -1.89/-0.08/-12.54 | 234.6 | 314 | 0.0102 | 0.92108 (68.25) | 1.0 | 0.0022 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1296 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 19.19/0.86/-6.22 | 234.6 | 315 | 0.0103 | 0.75624 (125.06) | 1.0 | 0.0244 | 0.877 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1297 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | -13.75/-0.64/-20.7 | 234.6 | 319 | 0.0105 | 0.97602 (98.32) | 1.0 | 0.0006 | 0.9135 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1298 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | 15.98/1.16/-4.14 | 234.6 | 306 | 0.0106 | 0.76923 (71.76) | 1.0 | 0.0633 | 0.884 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 1298

## Engine prereg 20261024_000539_gen_2410240001_002 (gen_2410240001_002, sha256 0660872cb1f0): rows #1299-1302 RESERVED (4 variants). Counted in N.
N_cumulative: 1302

## Engine run 20261024_000539_gen_2410240001_002 (gen_2410240001_002): rows #1299-1302. 0/4 pass. PBO 0.551. Bar applied at N=1302. Report: engine/runs/20261024_000539_gen_2410240001_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1299 | crypto_d|donchian(entry_n=20,exit_n=10)+trend_sma(n=100) | 6.75/0.3/-27.82 | 234.6 | 111 | 0.0173 | 0.86114 (74.72) | 1.0 | 0.5733 | 0.8975 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1300 | crypto_d|donchian(entry_n=20,exit_n=20)+trend_sma(n=100) | 10.51/0.37/-27.82 | 234.6 | 124 | 0.0172 | 0.82917 (120.52) | 1.0 | 0.6064 | 0.899 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1301 | crypto_d|donchian(entry_n=55,exit_n=10)+trend_sma(n=100) | 6.74/0.3/-29.59 | 234.6 | 66 | 0.0175 | 0.86513 (116.7) | 1.0 | 0.5734 | 0.8955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1302 | crypto_d|donchian(entry_n=55,exit_n=20)+trend_sma(n=100) | 10.75/0.38/-30.69 | 234.6 | 71 | 0.0176 | 0.83217 (73.57) | 1.0 | 0.6116 | 0.8985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1302

## Engine prereg 20261024_000543_gen_2410240001_003 (gen_2410240001_003, sha256 ada8a3e97bc1): rows #1303-1306 RESERVED (4 variants). Counted in N.
N_cumulative: 1306

## Engine run 20261024_000543_gen_2410240001_003 (gen_2410240001_003): rows #1303-1306. 0/4 pass. PBO 0.767. Bar applied at N=1306. Report: engine/runs/20261024_000543_gen_2410240001_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1303 | crypto_d|sma_cross(fast=5,slow=50)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 2 | 0.0545 | 0.98002 (106.5) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1304 | crypto_d|sma_cross(fast=5,slow=100)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 1 | 0.0509 | 0.97902 (42.86) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1305 | crypto_d|sma_cross(fast=20,slow=50)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 234.6 | 1 | 0.0512 | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1306 | crypto_d|sma_cross(fast=20,slow=100)+vol_regime(max_atr_pct=0.02) | -0.45/-0.83/-0.45 | 234.6 | 2 | 0.0512 | 0.97502 (170.14) | 1.0 | 0.0222 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1306

## Engine prereg 20261024_000546_gen_2410240011_000 (gen_2410240011_000, sha256 73204d549a0b): rows #1307-1310 RESERVED (4 variants). Counted in N.
N_cumulative: 1310

## Engine run 20261024_000546_gen_2410240011_000 (gen_2410240011_000): rows #1307-1310. 0/4 pass. PBO 0.524. Bar applied at N=1310. Report: engine/runs/20261024_000546_gen_2410240011_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1307 | crypto|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.04) | -3.36/0.07/-36.1 | 428.6 | 1659 | 0.1026 | 0.83317 (149.02) | 1.0 | 0.3671 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1308 | crypto|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.04) | -3.14/0.12/-44.22 | 428.6 | 1305 | 0.0987 | 0.87013 (158.84) | 1.0 | 0.3906 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1309 | crypto|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.04) | 6.87/0.31/-25.03 | 428.6 | 972 | 0.1028 | 0.8002 (65.86) | 1.0 | 0.4802 | 0.9125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1310 | crypto|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.04) | -0.48/0.13/-37.23 | 428.6 | 801 | 0.0979 | 0.88611 (65.36) | 1.0 | 0.3971 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1310

## Engine prereg 20261024_000550_gen_2410240011_001 (gen_2410240011_001, sha256 cf356faa2175): rows #1311-1318 RESERVED (8 variants). Counted in N.
N_cumulative: 1318

## Engine run 20261024_000550_gen_2410240011_001 (gen_2410240011_001): rows #1311-1318. 0/8 pass. PBO 0.003. Bar applied at N=1318. Report: engine/runs/20261024_000550_gen_2410240011_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1311 | crypto|rsi_revert(entry=5,exit=60,n=2)+relvol(min_ratio=1.2) | -23.44/-1.55/-23.6 | 428.6 | 3293 | 0.0918 | 0.89211 (40.63) | 1.0 | 0.0001 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1312 | crypto|rsi_revert(entry=5,exit=60,n=3)+relvol(min_ratio=1.2) | -12.01/-1.05/-15.77 | 428.6 | 1449 | 0.0866 | 0.91508 (50.97) | 1.0 | 0.0006 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1313 | crypto|rsi_revert(entry=5,exit=70,n=2)+relvol(min_ratio=1.2) | -17.84/-0.95/-18.06 | 428.6 | 3686 | 0.0927 | 0.80519 (36.43) | 1.0 | 0.0035 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1314 | crypto|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.2) | -19.64/-1.58/-23.87 | 428.6 | 1890 | 0.0862 | 0.94505 (79.77) | 1.0 | 0.0 | 0.917 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1315 | crypto|rsi_revert(entry=10,exit=60,n=2)+relvol(min_ratio=1.2) | -36.14/-2.22/-36.09 | 428.6 | 5041 | 0.0945 | 0.8981 (18.45) | 1.0 | 0.0 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1316 | crypto|rsi_revert(entry=10,exit=60,n=3)+relvol(min_ratio=1.2) | -21.66/-1.39/-21.49 | 428.6 | 3275 | 0.0912 | 0.84915 (34.99) | 1.0 | 0.0002 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1317 | crypto|rsi_revert(entry=10,exit=70,n=2)+relvol(min_ratio=1.2) | -33.68/-1.82/-33.47 | 428.6 | 5564 | 0.0952 | 0.82817 (48.52) | 1.0 | 0.0001 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1318 | crypto|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.2) | -31.77/-1.88/-31.8 | 428.6 | 4034 | 0.0921 | 0.91109 (76.87) | 1.0 | 0.0 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1318

## Engine prereg 20261024_000557_gen_2410240011_002 (gen_2410240011_002, sha256 3dae10c8ef23): rows #1319-1322 RESERVED (4 variants). Counted in N.
N_cumulative: 1322

## Engine run 20261024_000557_gen_2410240011_002 (gen_2410240011_002): rows #1319-1322. 0/4 pass. PBO 0.253. Bar applied at N=1322. Report: engine/runs/20261024_000557_gen_2410240011_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1319 | crypto|supertrend(atr_n=7,mult=2) | -12.28/-0.06/-39.69 | 428.6 | 2367 | 0.0975 | 0.82018 (50.96) | 1.0 | 0.2523 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1320 | crypto|supertrend(atr_n=7,mult=4) | 3.91/0.25/-42.89 | 428.6 | 886 | 0.0999 | 0.82817 (84.62) | 1.0 | 0.3858 | 0.9215 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1321 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.83417 (51.3) | 1.0 | 0.2598 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1322 | crypto|supertrend(atr_n=10,mult=4) | -3.46/0.11/-43.75 | 428.6 | 871 | 0.0993 | 0.88811 (108.04) | 1.0 | 0.3229 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1322

## Engine prereg 20261024_000602_gen_2410240011_003 (gen_2410240011_003, sha256 655d422f983d): rows #1323-1326 RESERVED (4 variants). Counted in N.
N_cumulative: 1326

## Engine run 20261024_000602_gen_2410240011_003 (gen_2410240011_003): rows #1323-1326. 0/4 pass. PBO 0.888. Bar applied at N=1326. Report: engine/runs/20261024_000602_gen_2410240011_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1323 | crypto|sma_cross(fast=10,slow=150)+vol_regime(max_atr_pct=0.04) | 8.08/0.33/-41.15 | 428.6 | 840 | 0.0987 | 0.81219 (102.9) | 1.0 | 0.2055 | 0.917 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1324 | crypto|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.04) | 23.26/0.58/-38.14 | 428.6 | 720 | 0.1 | 0.71429 (94.56) | 1.0 | 0.3005 | 0.9095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1325 | crypto|sma_cross(fast=50,slow=150)+vol_regime(max_atr_pct=0.04) | 44.11/0.87/-35.92 | 428.6 | 511 | 0.0982 | 0.5974 (81.61) | 1.0 | 0.4318 | 0.887 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1326 | crypto|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.04) | 53.55/1.01/-35.04 | 428.6 | 423 | 0.0954 | 0.56044 (92.47) | 1.0 | 0.4993 | 0.863 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1326

## Engine prereg 20261024_000606_gen_2410240021_000 (gen_2410240021_000, sha256 fca3039385b1): rows #1327-1330 RESERVED (4 variants). Counted in N.
N_cumulative: 1330

## Engine run 20261024_000606_gen_2410240021_000 (gen_2410240021_000): rows #1327-1330. 0/4 pass. PBO 0.425. Bar applied at N=1330. Report: engine/runs/20261024_000606_gen_2410240021_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1327 | sectors|supertrend(atr_n=10,mult=3)+rsi_band(hi=60) | 6.5/0.47/-5.81 | 50.2 | 1285 | 0.0743 | 0.97602 (17.75) | 1.0 | 0.3822 | 0.5055 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1328 | sectors|supertrend(atr_n=10,mult=4)+rsi_band(hi=60) | 1.39/0.12/-6.64 | 50.2 | 1072 | 0.0781 | 0.998 (18.7) | 1.0 | 0.1843 | 0.5075 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1329 | sectors|supertrend(atr_n=14,mult=3)+rsi_band(hi=60) | 7.05/0.48/-6.44 | 50.2 | 1303 | 0.0741 | 0.96803 (18.08) | 1.0 | 0.3865 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1330 | sectors|supertrend(atr_n=14,mult=4)+rsi_band(hi=60) | 1.98/0.16/-7.61 | 50.2 | 1115 | 0.0765 | 1.0 (18.49) | 1.0 | 0.2023 | 0.512 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1330

## Engine prereg 20261024_000609_gen_2410240021_001 (gen_2410240021_001, sha256 305af9c85b66): rows #1331-1334 RESERVED (4 variants). Counted in N.
N_cumulative: 1334

## Engine run 20261024_000609_gen_2410240021_001 (gen_2410240021_001): rows #1331-1334. 0/4 pass. PBO 0.038. Bar applied at N=1334. Report: engine/runs/20261024_000609_gen_2410240021_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1331 | sectors|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.0) | -4.42/-0.4/-7.02 | 50.2 | 2355 | 0.0772 | 1.0 (14.33) | 1.0 | 0.0045 | 0.505 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1332 | sectors|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | -11.73/-0.99/-14.59 | 50.2 | 2242 | 0.0818 | 1.0 (14.34) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1333 | sectors|supertrend(atr_n=14,mult=2)+relvol(min_ratio=1.0) | -4.52/-0.39/-7.72 | 50.2 | 2449 | 0.0768 | 1.0 (14.59) | 1.0 | 0.0051 | 0.504 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1334 | sectors|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.0) | -11.56/-0.93/-14.5 | 50.2 | 2387 | 0.0805 | 1.0 (14.53) | 1.0 | 0.0002 | 0.515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1334

## Engine prereg 20261024_000613_gen_2410240021_003 (gen_2410240021_003, sha256 9c36bcb6aa9d): rows #1335-1338 RESERVED (4 variants). Counted in N.
N_cumulative: 1338

## Engine run 20261024_000613_gen_2410240021_003 (gen_2410240021_003): rows #1335-1338. 0/4 pass. PBO 0.083. Bar applied at N=1338. Report: engine/runs/20261024_000613_gen_2410240021_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1335 | sectors|donchian(entry_n=20,exit_n=10)+rsi_band(hi=60) | 6.36/0.65/-3.77 | 50.2 | 1105 | 0.0748 | 0.99201 (18.91) | 1.0 | 0.2573 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1336 | sectors|donchian(entry_n=20,exit_n=20)+rsi_band(hi=60) | 7.02/0.49/-5.16 | 50.2 | 1212 | 0.0752 | 0.97403 (18.16) | 1.0 | 0.1771 | 0.5035 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1337 | sectors|donchian(entry_n=100,exit_n=10)+rsi_band(hi=60) | 0.25/0.06/-2.41 | 50.2 | 557 | 0.0836 | 1.0 (20.95) | 1.0 | 0.0478 | 0.4975 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1338 | sectors|donchian(entry_n=100,exit_n=20)+rsi_band(hi=60) | 0.17/0.03/-3.45 | 50.2 | 663 | 0.084 | 1.0 (20.5) | 1.0 | 0.0442 | 0.507 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1338

## Engine prereg 20261024_000615_gen_2410240031_000 (gen_2410240031_000, sha256 151b5d59f9eb): rows #1339-1342 RESERVED (4 variants). Counted in N.
N_cumulative: 1342

## Engine run 20261024_000615_gen_2410240031_000 (gen_2410240031_000): rows #1339-1342. 0/4 pass. PBO 0.199. Bar applied at N=1342. Report: engine/runs/20261024_000615_gen_2410240031_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1339 | semis|sma_cross(fast=5,slow=50) | -11.82/-0.44/-20.99 | -38.66 | 186 | 0.0788 | 0.31668 (-20.19) | 1.0 | 0.0 | 0.3555 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1340 | semis|sma_cross(fast=5,slow=100) | 3.56/0.78/-2.66 | -38.66 | 40 | 0.0835 | 0.07792 (-20.15) | 1.0 | 0.0114 | 0.275 | False | min_trades, cost_stop, holm, dsr, spa |
| 1341 | semis|sma_cross(fast=10,slow=50) | -14.34/-0.58/-21.45 | -38.66 | 165 | 0.0808 | 0.37962 (-21.11) | 1.0 | 0.0 | 0.3715 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1342 | semis|sma_cross(fast=10,slow=100) | 3.5/0.8/-2.58 | -38.66 | 36 | 0.0835 | 0.08292 (-20.56) | 1.0 | 0.0129 | 0.2745 | False | min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1342

## Engine prereg 20261024_000618_gen_2410240031_001 (gen_2410240031_001, sha256 219938c447b8): rows #1343-1346 RESERVED (4 variants). Counted in N.
N_cumulative: 1346

## Engine run 20261024_000618_gen_2410240031_001 (gen_2410240031_001): rows #1343-1346. 0/4 pass. PBO 0.294. Bar applied at N=1346. Report: engine/runs/20261024_000618_gen_2410240031_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1343 | semis|donchian(entry_n=55,exit_n=10)+relvol(min_ratio=1.0) | 0.96/0.25/-1.98 | -38.66 | 270 | 0.0868 | 0.08991 (-22.35) | 1.0 | 0.0607 | 0.287 | False | cost_stop, walk_forward, holm, dsr, spa |
| 1344 | semis|donchian(entry_n=55,exit_n=20)+relvol(min_ratio=1.0) | -1.01/-0.21/-3.77 | -38.66 | 393 | 0.085 | 0.09291 (-23.21) | 1.0 | 0.0079 | 0.301 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 1345 | semis|donchian(entry_n=100,exit_n=10)+relvol(min_ratio=1.0) | 0.62/0.32/-1.14 | -38.66 | 89 | 0.0846 | 0.0979 (-22.33) | 1.0 | 0.0687 | 0.2925 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1346 | semis|donchian(entry_n=100,exit_n=20)+relvol(min_ratio=1.0) | -1.04/-0.44/-1.83 | -38.66 | 123 | 0.0835 | 0.12687 (-20.81) | 1.0 | 0.009 | 0.3055 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1346

## Engine prereg 20261024_000620_gen_2410240031_002 (gen_2410240031_002, sha256 907f12889d77): rows #1347-1350 RESERVED (4 variants). Counted in N.
N_cumulative: 1350

## Engine run 20261024_000620_gen_2410240031_002 (gen_2410240031_002): rows #1347-1350. 0/4 pass. PBO 0.2. Bar applied at N=1350. Report: engine/runs/20261024_000620_gen_2410240031_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1347 | semis|sma_cross(fast=20,slow=50)+trend_sma(n=200) | -0.2/-0.09/-0.89 | -38.66 | 6 | 0.0873 | 0.1049 (-20.98) | 1.0 | 0.2986 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1348 | semis|sma_cross(fast=20,slow=150)+trend_sma(n=200) | 0.19/0.1/-0.89 | -38.66 | 3 | 0.0904 | 0.12088 (-20.75) | 1.0 | 0.3819 | 0.297 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1349 | semis|sma_cross(fast=50,slow=50)+trend_sma(n=200) | 0.0/0.0/0.0 | -38.66 | 0 | inf | 0.1029 (-20.95) | 1.0 | 0.0 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1350 | semis|sma_cross(fast=50,slow=150)+trend_sma(n=200) | 0.11/0.06/-0.89 | -38.66 | 3 | 0.0904 | 0.11788 (-20.49) | 1.0 | 0.3658 | 0.2975 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1350

## Engine prereg 20261024_000622_gen_2410240031_003 (gen_2410240031_003, sha256 5f5e20908c27): rows #1351-1382 RESERVED (32 variants). Counted in N.
N_cumulative: 1382

## Engine run 20261024_000622_gen_2410240031_003 (gen_2410240031_003): rows #1351-1382. 0/32 pass. PBO 0.533. Bar applied at N=1382. Report: engine/runs/20261024_000622_gen_2410240031_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1351 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=0) | 10.01/1.0/-2.31 | -38.66 | 19 | 0.0347 | 0.06893 (-21.88) | 1.0 | 0.0003 | 0.251 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1352 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=1) | -1.61/-0.92/-1.67 | -38.66 | 17 | 0.0253 | 0.13287 (-22.3) | 1.0 | 0.0 | 0.307 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1353 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=2) | -0.83/-0.29/-2.38 | -38.66 | 23 | 0.0338 | 0.16983 (-21.29) | 1.0 | 0.0 | 0.299 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1354 | semis|drop_revert(drop=0.05,hold=3,n=1)+day_of_week(days=3) | -0.72/-0.34/-1.23 | -38.66 | 19 | 0.0424 | 0.15684 (-21.88) | 1.0 | 0.0 | 0.301 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1355 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | 4.98/0.45/-4.93 | -38.66 | 88 | 0.0477 | 0.10889 (-22.38) | 1.0 | 0.0009 | 0.2705 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1356 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 2.83/0.39/-3.57 | -38.66 | 107 | 0.0559 | 0.08492 (-22.42) | 1.0 | 0.0014 | 0.28 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1357 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -7.39/-0.91/-9.57 | -38.66 | 106 | 0.05 | 0.25175 (-21.01) | 1.0 | 0.0 | 0.337 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1358 | semis|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | -9.15/-0.96/-12.81 | -38.66 | 137 | 0.0488 | 0.2048 (-22.26) | 1.0 | 0.0 | 0.354 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1359 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=0) | 14.58/1.1/-3.76 | -38.66 | 28 | 0.0347 | 0.03197 (-21.09) | 1.0 | 0.0019 | 0.2245 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 1360 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=1) | 2.24/0.46/-4.02 | -38.66 | 35 | 0.0272 | 0.0989 (-21.0) | 1.0 | 0.0012 | 0.2885 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1361 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=2) | 0.73/0.13/-4.92 | -38.66 | 33 | 0.0326 | 0.15085 (-20.94) | 1.0 | 0.0005 | 0.2895 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1362 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=3) | -0.62/-0.1/-3.99 | -38.66 | 35 | 0.0388 | 0.16484 (-20.32) | 1.0 | 0.0001 | 0.3005 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1363 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | 16.5/0.83/-9.67 | -38.66 | 150 | 0.0492 | 0.04995 (-21.45) | 1.0 | 0.0029 | 0.217 | False | cost_stop, holm, dsr, spa, pbo |
| 1364 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 2.75/0.29/-11.47 | -38.66 | 179 | 0.0551 | 0.07992 (-22.72) | 1.0 | 0.0007 | 0.2755 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1365 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | 1.21/0.12/-15.49 | -38.66 | 182 | 0.0529 | 0.14785 (-22.52) | 1.0 | 0.0002 | 0.262 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1366 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | -12.49/-0.92/-18.59 | -38.66 | 202 | 0.0502 | 0.21578 (-22.43) | 1.0 | 0.0 | 0.3745 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1367 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=0) | 0.38/1.16/0.0 | -38.66 | 2 | 0.0013 | 0.07992 (-20.6) | 1.0 | 0.0 | 0.297 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1368 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=1) | -1.32/-1.16/-1.32 | -38.66 | 3 | 0.0038 | 0.19281 (-20.52) | 1.0 | 0.0 | 0.3065 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1369 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=2) | 0.8/0.82/0.0 | -38.66 | 1 | 0.0271 | 0.15784 (-20.55) | 1.0 | 0.0 | 0.2915 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1370 | semis|drop_revert(drop=0.15,hold=3,n=1)+day_of_week(days=3) | 0.18/0.82/0.0 | -38.66 | 1 | 0.0309 | 0.03297 (-21.12) | 1.0 | 0.0 | 0.299 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1371 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=0) | -0.76/-0.77/-1.0 | -38.66 | 4 | 0.0026 | 0.0999 (-20.3) | 1.0 | 0.0 | 0.3025 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1372 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=1) | -1.27/-1.17/-1.27 | -38.66 | 3 | 0.0038 | 0.18282 (-20.27) | 1.0 | 0.0 | 0.306 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1373 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=2) | 1.33/0.36/-2.23 | -38.66 | 10 | 0.0299 | 0.12188 (-21.08) | 1.0 | 0.0018 | 0.287 | False | min_trades, holm, dsr, spa, pbo |
| 1374 | semis|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=3) | 2.8/0.84/-1.11 | -38.66 | 4 | 0.0189 | 0.10589 (-21.38) | 1.0 | 0.0007 | 0.2825 | False | min_trades, holm, dsr, spa, pbo |
| 1375 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=0) | 0.06/0.11/-0.33 | -38.66 | 2 | 0.0013 | 0.07093 (-21.0) | 1.0 | 0.0005 | 0.2995 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1376 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=1) | -1.71/-1.5/-1.71 | -38.66 | 5 | 0.0023 | 0.15784 (-20.88) | 1.0 | 0.0 | 0.3085 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1377 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=2) | 2.64/1.02/0.0 | -38.66 | 3 | 0.0107 | 0.13487 (-21.28) | 1.0 | 0.0 | 0.2805 | False | min_trades, holm, dsr, spa, pbo |
| 1378 | semis|drop_revert(drop=0.15,hold=10,n=1)+day_of_week(days=3) | 0.46/0.93/0.0 | -38.66 | 1 | 0.0309 | 0.03896 (-20.26) | 1.0 | 0.0 | 0.295 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1379 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | 0.59/0.51/-0.61 | -38.66 | 5 | 0.0265 | 0.1029 (-20.45) | 1.0 | 0.0007 | 0.2945 | False | min_trades, holm, dsr, spa, pbo |
| 1380 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | -2.07/-1.27/-2.07 | -38.66 | 8 | 0.0064 | 0.16883 (-21.07) | 1.0 | 0.0 | 0.311 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1381 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -0.58/-0.08/-5.2 | -38.66 | 12 | 0.0298 | 0.12987 (-20.87) | 1.0 | 0.0001 | 0.2955 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1382 | semis|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 6.63/1.44/-1.41 | -38.66 | 12 | 0.0274 | 0.07293 (-22.24) | 1.0 | 0.0134 | 0.2615 | False | min_trades, holm, dsr, spa, pbo |

N_cumulative: 1382

## Engine prereg 20261024_010730_gen_2410240101_000 (gen_2410240101_000, sha256 8ce82b86db84): rows #1383-1390 RESERVED (8 variants). Counted in N.
N_cumulative: 1390

## Engine run 20261024_010730_gen_2410240101_000 (gen_2410240101_000): rows #1383-1390. 0/8 pass. PBO 0.163. Bar applied at N=1390. Report: engine/runs/20261024_010730_gen_2410240101_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1383 | crypto_d|rsi_revert(entry=5,exit=60,n=3) | 16.16/0.84/-10.46 | 234.6 | 56 | 0.0127 | 0.7982 (76.05) | 1.0 | 0.1883 | 0.882 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1384 | crypto_d|rsi_revert(entry=5,exit=60,n=5) | 2.03/0.38/-3.07 | 234.6 | 4 | 0.0148 | 0.98801 (65.83) | 1.0 | 0.0784 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1385 | crypto_d|rsi_revert(entry=5,exit=80,n=3) | 32.13/1.28/-10.04 | 234.6 | 52 | 0.0139 | 0.64735 (143.0) | 1.0 | 0.3876 | 0.873 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1386 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.97502 (48.87) | 1.0 | 0.078 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1387 | crypto_d|rsi_revert(entry=10,exit=60,n=3) | 54.19/1.31/-13.67 | 234.6 | 160 | 0.013 | 0.56244 (112.96) | 1.0 | 0.4005 | 0.847 | False | beats_buy_hold, holm, dsr, spa |
| 1388 | crypto_d|rsi_revert(entry=10,exit=60,n=5) | 22.05/1.11/-5.61 | 234.6 | 31 | 0.0124 | 0.74925 (111.5) | 1.0 | 0.289 | 0.8795 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1389 | crypto_d|rsi_revert(entry=10,exit=80,n=3) | 73.05/1.31/-18.43 | 234.6 | 131 | 0.0134 | 0.51349 (100.7) | 1.0 | 0.4091 | 0.8355 | False | beats_buy_hold, holm, dsr, spa |
| 1390 | crypto_d|rsi_revert(entry=10,exit=80,n=5) | 41.28/1.49/-10.29 | 234.6 | 31 | 0.0124 | 0.6004 (134.34) | 1.0 | 0.4976 | 0.8635 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 1390

## Engine prereg 20261024_010736_gen_2410240101_001 (gen_2410240101_001, sha256 ba571775ccf9): rows #1391-1398 RESERVED (8 variants). Counted in N.
N_cumulative: 1398

## Engine run 20261024_010736_gen_2410240101_001 (gen_2410240101_001): rows #1391-1398. 0/8 pass. PBO 0.83. Bar applied at N=1398. Report: engine/runs/20261024_010736_gen_2410240101_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1391 | crypto_d|rsi_revert(entry=5,exit=70,n=2) | 64.66/1.37/-15.7 | 234.6 | 223 | 0.0132 | 0.54346 (102.89) | 1.0 | 0.4977 | 0.8365 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1392 | crypto_d|rsi_revert(entry=5,exit=70,n=5) | 2.61/0.46/-3.07 | 234.6 | 4 | 0.0148 | 0.98302 (60.43) | 1.0 | 0.1198 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1393 | crypto_d|rsi_revert(entry=5,exit=80,n=2) | 57.4/1.13/-17.19 | 234.6 | 208 | 0.0132 | 0.53447 (84.85) | 1.0 | 0.3739 | 0.843 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1394 | crypto_d|rsi_revert(entry=5,exit=80,n=5) | 2.53/0.32/-7.11 | 234.6 | 4 | 0.0148 | 0.98901 (155.65) | 1.0 | 0.1003 | 0.895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1395 | crypto_d|rsi_revert(entry=20,exit=70,n=2) | 10.84/0.38/-29.74 | 234.6 | 563 | 0.0138 | 0.78721 (67.13) | 1.0 | 0.1125 | 0.884 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1396 | crypto_d|rsi_revert(entry=20,exit=70,n=5) | 72.94/1.2/-24.27 | 234.6 | 120 | 0.0132 | 0.52947 (107.75) | 1.0 | 0.4114 | 0.837 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1397 | crypto_d|rsi_revert(entry=20,exit=80,n=2) | 29.46/0.61/-29.15 | 234.6 | 477 | 0.014 | 0.65435 (71.66) | 1.0 | 0.1745 | 0.864 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1398 | crypto_d|rsi_revert(entry=20,exit=80,n=5) | 63.41/0.97/-32.5 | 234.6 | 92 | 0.0134 | 0.53447 (94.02) | 1.0 | 0.3102 | 0.8365 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 1398

## Engine prereg 20261024_010738_gen_2410240101_002 (gen_2410240101_002, sha256 60ebbd789173): rows #1399-1406 RESERVED (8 variants). Counted in N.
N_cumulative: 1406

## Engine run 20261024_010738_gen_2410240101_002 (gen_2410240101_002): rows #1399-1406. 0/8 pass. PBO 0.818. Bar applied at N=1406. Report: engine/runs/20261024_010738_gen_2410240101_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1399 | crypto_d|drop_revert(drop=0.1,hold=5,n=1) | 10.73/0.49/-13.68 | 234.6 | 116 | 0.0092 | 0.83017 (126.08) | 1.0 | 0.2278 | 0.8865 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1400 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -7.21/0.03/-31.39 | 234.6 | 255 | 0.011 | 0.94306 (93.43) | 1.0 | 0.1039 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1401 | crypto_d|drop_revert(drop=0.1,hold=10,n=1) | -0.44/0.12/-24.88 | 234.6 | 97 | 0.0098 | 0.93107 (82.77) | 1.0 | 0.1263 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1402 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 11.7/0.39/-33.6 | 234.6 | 187 | 0.0118 | 0.8002 (62.44) | 1.0 | 0.2044 | 0.886 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1403 | crypto_d|drop_revert(drop=0.15,hold=5,n=1) | 2.44/0.29/-5.48 | 234.6 | 33 | 0.0074 | 0.94605 (132.25) | 1.0 | 0.1668 | 0.895 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1404 | crypto_d|drop_revert(drop=0.15,hold=5,n=3) | 7.63/0.36/-12.4 | 234.6 | 109 | 0.0089 | 0.83916 (120.43) | 1.0 | 0.188 | 0.8895 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1405 | crypto_d|drop_revert(drop=0.15,hold=10,n=1) | -9.04/-0.5/-14.91 | 234.6 | 31 | 0.0075 | 0.999 (136.44) | 1.0 | 0.0275 | 0.906 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1406 | crypto_d|drop_revert(drop=0.15,hold=10,n=3) | 9.36/0.38/-15.09 | 234.6 | 91 | 0.0094 | 0.83017 (131.29) | 1.0 | 0.2005 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 1406

## Engine prereg 20261024_010743_gen_2410240101_003 (gen_2410240101_003, sha256 9da2696f0ade): rows #1407-1414 RESERVED (8 variants). Counted in N.
N_cumulative: 1414

## Engine run 20261024_010743_gen_2410240101_003 (gen_2410240101_003): rows #1407-1414. 0/8 pass. PBO 0.163. Bar applied at N=1414. Report: engine/runs/20261024_010743_gen_2410240101_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1407 | crypto_d|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=100) | 8.92/0.58/-10.1 | 234.6 | 83 | 0.0143 | 0.85315 (125.08) | 1.0 | 0.0138 | 0.889 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1408 | crypto_d|rsi_revert(entry=5,exit=70,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1409 | crypto_d|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=100) | 8.93/0.54/-10.1 | 234.6 | 95 | 0.0143 | 0.82118 (60.34) | 1.0 | 0.012 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1410 | crypto_d|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1411 | crypto_d|rsi_revert(entry=10,exit=70,n=2)+trend_sma(n=100) | -0.29/0.07/-11.62 | 234.6 | 158 | 0.016 | 0.91808 (74.07) | 1.0 | 0.0024 | 0.9 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1412 | crypto_d|rsi_revert(entry=10,exit=70,n=5)+trend_sma(n=100) | 5.31/2.08/-0.34 | 234.6 | 6 | 0.02 | 0.98002 (153.59) | 1.0 | 0.2273 | 0.8925 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1413 | crypto_d|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=100) | 3.03/0.21/-11.38 | 234.6 | 172 | 0.0161 | 0.88511 (82.82) | 1.0 | 0.0039 | 0.896 | False | beats_buy_hold, holm, dsr, spa |
| 1414 | crypto_d|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=100) | 3.4/0.78/-5.78 | 234.6 | 13 | 0.0187 | 0.97802 (46.98) | 1.0 | 0.0224 | 0.8945 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 1414

## Engine prereg 20261024_010746_gen_2410240111_000 (gen_2410240111_000, sha256 43a2c7f38abb): rows #1415-1422 RESERVED (8 variants). Counted in N.
N_cumulative: 1422

## Engine run 20261024_010746_gen_2410240111_000 (gen_2410240111_000): rows #1415-1422. 0/8 pass. PBO 0.288. Bar applied at N=1422. Report: engine/runs/20261024_010746_gen_2410240111_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1415 | megacap|drop_revert(drop=0.05,hold=5,n=1)+relvol(min_ratio=1.0) | -1.54/-0.89/-1.96 | 26.77 | 10 | 0.0458 | 0.98202 (12.42) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1416 | megacap|drop_revert(drop=0.05,hold=5,n=5)+relvol(min_ratio=1.0) | 1.06/0.3/-2.83 | 26.77 | 89 | 0.0537 | 0.92607 (12.26) | 1.0 | 0.0029 | 0.8885 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1417 | megacap|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | -0.22/-0.11/-1.99 | 26.77 | 23 | 0.0449 | 0.97902 (13.06) | 1.0 | 0.0004 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1418 | megacap|drop_revert(drop=0.05,hold=10,n=5)+relvol(min_ratio=1.0) | 0.39/0.1/-3.22 | 26.77 | 126 | 0.0505 | 0.92807 (12.56) | 1.0 | 0.0014 | 0.8945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1419 | megacap|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 26.77 | 1 | 0.0045 | 0.93906 (13.1) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1420 | megacap|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 0.59/1.03/-0.0 | 26.77 | 3 | 0.0385 | 0.95504 (12.97) | 1.0 | 0.0 | 0.9015 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1421 | megacap|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 26.77 | 1 | 0.0045 | 0.93806 (13.1) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1422 | megacap|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 1.66/1.16/-0.0 | 26.77 | 7 | 0.0385 | 0.92907 (13.41) | 1.0 | 0.0 | 0.89 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1422

## Engine prereg 20261024_010749_gen_2410240111_001 (gen_2410240111_001, sha256 bfb318a84462): rows #1423-1426 RESERVED (4 variants). Counted in N.
N_cumulative: 1426

## Engine run 20261024_010749_gen_2410240111_001 (gen_2410240111_001): rows #1423-1426. 0/4 pass. PBO 0.155. Bar applied at N=1426. Report: engine/runs/20261024_010749_gen_2410240111_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1423 | megacap|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.04) | -11.03/-0.47/-16.44 | 26.77 | 922 | 0.1269 | 0.77123 (9.31) | 1.0 | 0.0 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1424 | megacap|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.04) | -9.2/-0.32/-21.91 | 26.77 | 1986 | 0.1239 | 0.61139 (5.54) | 1.0 | 0.0 | 0.9305 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1425 | megacap|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.04) | 6.05/1.15/-1.62 | 26.77 | 156 | 0.1681 | 0.85415 (11.19) | 1.0 | 0.0369 | 0.8525 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1426 | megacap|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.04) | -7.82/-0.34/-16.55 | 26.77 | 232 | 0.1502 | 0.76623 (10.28) | 1.0 | 0.0 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1426

## Engine prereg 20261024_010752_gen_2410240111_003 (gen_2410240111_003, sha256 0d74e5fef3c4): rows #1427-1430 RESERVED (4 variants). Counted in N.
N_cumulative: 1430

## Engine run 20261024_010752_gen_2410240111_003 (gen_2410240111_003): rows #1427-1430. 0/4 pass. PBO 0.245. Bar applied at N=1430. Report: engine/runs/20261024_010752_gen_2410240111_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1427 | megacap|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.06) | -10.41/-0.44/-15.86 | 26.77 | 921 | 0.1269 | 0.75624 (9.12) | 1.0 | 0.0001 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1428 | megacap|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.06) | -7.31/-0.24/-20.28 | 26.77 | 1984 | 0.124 | 0.45455 (5.06) | 1.0 | 0.001 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1429 | megacap|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 1.95/0.82/-0.9 | 26.77 | 15 | 0.1217 | 0.93207 (13.31) | 1.0 | 0.0432 | 0.8975 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1430 | megacap|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | 1.31/0.5/-1.43 | 26.77 | 20 | 0.1268 | 0.94406 (12.93) | 1.0 | 0.0263 | 0.9025 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1430

## Engine prereg 20261024_010754_gen_2410240121_000 (gen_2410240121_000, sha256 c7a386e4747a): rows #1431-1434 RESERVED (4 variants). Counted in N.
N_cumulative: 1434

## Engine run 20261024_010754_gen_2410240121_000 (gen_2410240121_000): rows #1431-1434. 0/4 pass. PBO 0.889. Bar applied at N=1434. Report: engine/runs/20261024_010754_gen_2410240121_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1431 | crypto|donchian(entry_n=55,exit_n=10)+rsi_band(hi=70) | 191.15/0.79/-28.31 | 428.6 | 2083 | 0.0967 | 0.36663 (141.98) | 1.0 | 0.9212 | 0.97 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1432 | crypto|donchian(entry_n=55,exit_n=20)+rsi_band(hi=70) | 157.95/0.75/-42.7 | 428.6 | 2024 | 0.0973 | 0.43756 (121.61) | 1.0 | 0.8952 | 0.5095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1433 | crypto|donchian(entry_n=100,exit_n=10)+rsi_band(hi=70) | 245.17/0.86/-17.53 | 428.6 | 1478 | 0.0944 | 0.24875 (102.81) | 1.0 | 0.9523 | 0.9355 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1434 | crypto|donchian(entry_n=100,exit_n=20)+rsi_band(hi=70) | 244.41/0.86/-27.45 | 428.6 | 1453 | 0.0953 | 0.27772 (132.1) | 1.0 | 0.9514 | 0.942 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |

N_cumulative: 1434

## Engine prereg 20261024_010758_gen_2410240121_001 (gen_2410240121_001, sha256 adba4a9c1d23): rows #1435-1438 RESERVED (4 variants). Counted in N.
N_cumulative: 1438

## Engine run 20261024_010758_gen_2410240121_001 (gen_2410240121_001): rows #1435-1438. 0/4 pass. PBO 0.693. Bar applied at N=1438. Report: engine/runs/20261024_010758_gen_2410240121_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1435 | crypto|sma_cross(fast=10,slow=50)+vol_regime(max_atr_pct=0.06) | 35.06/0.74/-43.8 | 428.6 | 1635 | 0.1034 | 0.57542 (73.68) | 1.0 | 0.4845 | 0.902 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1436 | crypto|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.06) | 19.26/0.52/-40.09 | 428.6 | 701 | 0.1024 | 0.74126 (177.96) | 1.0 | 0.3783 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1437 | crypto|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.06) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1438 | crypto|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.06) | 51.37/0.98/-35.78 | 428.6 | 391 | 0.1035 | 0.54246 (66.01) | 1.0 | 0.5966 | 0.866 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1438

## Engine prereg 20261024_010802_gen_2410240121_002 (gen_2410240121_002, sha256 fd2b3fc267e4): rows #1439-1446 RESERVED (8 variants). Counted in N.
N_cumulative: 1446

## Engine run 20261024_010802_gen_2410240121_002 (gen_2410240121_002): rows #1439-1446. 0/8 pass. PBO 0.843. Bar applied at N=1446. Report: engine/runs/20261024_010802_gen_2410240121_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1439 | crypto|drop_revert(drop=0.05,hold=5,n=3) | 14.64/1.01/-5.04 | 428.6 | 482 | 0.0373 | 0.82218 (185.26) | 1.0 | 0.1733 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1440 | crypto|drop_revert(drop=0.05,hold=5,n=5) | -2.22/-0.04/-14.4 | 428.6 | 675 | 0.0434 | 0.92707 (149.25) | 1.0 | 0.0132 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1441 | crypto|drop_revert(drop=0.05,hold=10,n=3) | -4.05/-0.18/-10.63 | 428.6 | 412 | 0.0403 | 0.95305 (155.61) | 1.0 | 0.008 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1442 | crypto|drop_revert(drop=0.05,hold=10,n=5) | -6.89/-0.2/-17.22 | 428.6 | 577 | 0.0473 | 0.95205 (137.0) | 1.0 | 0.0074 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1443 | crypto|drop_revert(drop=0.1,hold=5,n=3) | 1.51/0.69/-0.6 | 428.6 | 44 | 0.0155 | 0.94406 (56.48) | 1.0 | 0.0351 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1444 | crypto|drop_revert(drop=0.1,hold=5,n=5) | 3.97/0.75/-2.84 | 428.6 | 89 | 0.0219 | 0.86513 (65.12) | 1.0 | 0.1121 | 0.9065 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1445 | crypto|drop_revert(drop=0.1,hold=10,n=3) | -1.13/-0.36/-1.92 | 428.6 | 39 | 0.0163 | 0.95904 (69.95) | 1.0 | 0.0055 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1446 | crypto|drop_revert(drop=0.1,hold=10,n=5) | 4.28/0.67/-3.04 | 428.6 | 76 | 0.0239 | 0.88811 (219.54) | 1.0 | 0.0761 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1446

## Engine prereg 20261024_010809_gen_2410240121_003 (gen_2410240121_003, sha256 63106dd35788): rows #1447-1450 RESERVED (4 variants). Counted in N.
N_cumulative: 1450

## Engine run 20261024_010809_gen_2410240121_003 (gen_2410240121_003): rows #1447-1450. 0/4 pass. PBO 0.191. Bar applied at N=1450. Report: engine/runs/20261024_010809_gen_2410240121_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1447 | crypto|sma_cross(fast=5,slow=100)+relvol(min_ratio=1.0) | -59.26/-3.25/-61.3 | 428.6 | 9289 | 0.1026 | 0.87612 (-30.06) | 1.0 | 0.0001 | 0.931 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1448 | crypto|sma_cross(fast=5,slow=150)+relvol(min_ratio=1.0) | -62.92/-3.64/-64.77 | 428.6 | 9277 | 0.1025 | 0.94406 (19.58) | 1.0 | 0.0 | 0.933 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1449 | crypto|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.0) | -56.49/-2.9/-58.35 | 428.6 | 9172 | 0.1021 | 0.83317 (-27.04) | 1.0 | 0.0 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1450 | crypto|sma_cross(fast=50,slow=150)+relvol(min_ratio=1.0) | -60.41/-3.42/-62.17 | 428.6 | 9119 | 0.1019 | 0.91309 (2.43) | 1.0 | 0.0 | 0.932 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1450

## Engine prereg 20261024_010813_gen_2410240131_000 (gen_2410240131_000, sha256 0dec490a410f): rows #1451-1458 RESERVED (8 variants). Counted in N.
N_cumulative: 1458

## Engine run 20261024_010813_gen_2410240131_000 (gen_2410240131_000): rows #1451-1458. 0/8 pass. PBO 0.359. Bar applied at N=1458. Report: engine/runs/20261024_010813_gen_2410240131_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1451 | sectors|rsi_revert(entry=5,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 1.44/0.25/-2.7 | 50.2 | 138 | 0.0653 | 1.0 (22.28) | 1.0 | 0.063 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1452 | sectors|rsi_revert(entry=5,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 1.87/0.76/-0.84 | 50.2 | 22 | 0.0597 | 1.0 (23.19) | 1.0 | 0.2515 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1453 | sectors|rsi_revert(entry=5,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 6.2/0.85/-2.45 | 50.2 | 136 | 0.0653 | 0.999 (22.87) | 1.0 | 0.3131 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1454 | sectors|rsi_revert(entry=5,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 4.69/1.29/-0.86 | 50.2 | 26 | 0.0513 | 0.997 (23.96) | 1.0 | 0.6183 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1455 | sectors|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 9.6/0.57/-5.27 | 50.2 | 368 | 0.0666 | 0.98002 (21.6) | 1.0 | 0.1163 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1456 | sectors|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0626 | 0.998 (22.78) | 1.0 | 0.191 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1457 | sectors|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 20.84/0.92/-7.58 | 50.2 | 339 | 0.0675 | 0.55744 (21.95) | 1.0 | 0.3407 | 0.955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1458 | sectors|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 11.32/1.19/-2.1 | 50.2 | 85 | 0.0601 | 0.92507 (23.08) | 1.0 | 0.5459 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1458

## Engine prereg 20261024_010817_gen_2410240131_001 (gen_2410240131_001, sha256 9e306d5bea8e): rows #1459-1462 RESERVED (4 variants). Counted in N.
N_cumulative: 1462

## Engine run 20261024_010817_gen_2410240131_001 (gen_2410240131_001): rows #1459-1462. 0/4 pass. PBO 0.155. Bar applied at N=1462. Report: engine/runs/20261024_010817_gen_2410240131_001/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1459 | sectors|donchian(entry_n=20,exit_n=10) | 14.67/0.77/-5.33 | 50.2 | 386 | 0.0703 | 0.85514 (21.6) | 1.0 | 0.7849 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1460 | sectors|donchian(entry_n=20,exit_n=20) | 15.73/0.68/-7.57 | 50.2 | 276 | 0.0645 | 0.84316 (22.69) | 1.0 | 0.7372 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1461 | sectors|donchian(entry_n=55,exit_n=10) | 8.71/0.64/-5.6 | 50.2 | 284 | 0.0777 | 0.997 (22.29) | 1.0 | 0.7093 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1462 | sectors|donchian(entry_n=55,exit_n=20) | 8.86/0.55/-6.55 | 50.2 | 209 | 0.0752 | 0.99201 (22.42) | 1.0 | 0.6567 | 0.513 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1462

## Engine prereg 20261024_010819_gen_2410240131_002 (gen_2410240131_002, sha256 eccb90b0b5f2): rows #1463-1494 RESERVED (32 variants). Counted in N.
N_cumulative: 1494

## Engine run 20261024_010819_gen_2410240131_002 (gen_2410240131_002): rows #1463-1494. 0/32 pass. PBO 0.608. Bar applied at N=1494. Report: engine/runs/20261024_010819_gen_2410240131_002/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1463 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=0) | -4.34/-0.56/-5.93 | 50.2 | 260 | 0.0366 | 1.0 (22.52) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1464 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=1) | 4.89/0.33/-2.62 | 50.2 | 269 | 0.0386 | 1.0 (22.93) | 1.0 | 0.0003 | 0.5015 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1465 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=2) | -3.22/-0.77/-4.03 | 50.2 | 268 | 0.0378 | 1.0 (22.52) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1466 | sectors|drop_revert(drop=0.05,hold=5,n=3)+day_of_week(days=3) | 2.54/0.52/-1.89 | 50.2 | 273 | 0.0367 | 0.999 (22.96) | 1.0 | 0.0059 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1467 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | -4.65/-0.54/-6.33 | 50.2 | 373 | 0.0406 | 1.0 (22.09) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1468 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 3.28/0.23/-4.25 | 50.2 | 389 | 0.041 | 1.0 (21.78) | 1.0 | 0.0005 | 0.497 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1469 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -2.02/-0.41/-3.83 | 50.2 | 403 | 0.0409 | 1.0 (22.08) | 1.0 | 0.0001 | 0.4995 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1470 | sectors|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | 1.69/0.28/-3.18 | 50.2 | 405 | 0.0408 | 1.0 (21.77) | 1.0 | 0.0038 | 0.494 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1471 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -1.47/-0.15/-5.93 | 50.2 | 431 | 0.0375 | 1.0 (22.55) | 1.0 | 0.0001 | 0.503 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1472 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 3.91/0.27/-3.47 | 50.2 | 469 | 0.0387 | 0.999 (22.29) | 1.0 | 0.0005 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1473 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -2.82/-0.58/-4.1 | 50.2 | 453 | 0.0383 | 1.0 (21.88) | 1.0 | 0.0 | 0.4995 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1474 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 5.33/0.83/-1.87 | 50.2 | 458 | 0.038 | 0.997 (22.51) | 1.0 | 0.0367 | 0.49 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1475 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -2.14/-0.21/-6.32 | 50.2 | 600 | 0.0411 | 1.0 (21.56) | 1.0 | 0.0001 | 0.5 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1476 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 3.67/0.25/-3.71 | 50.2 | 641 | 0.0415 | 0.998 (21.64) | 1.0 | 0.0006 | 0.4965 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1477 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -2.27/-0.37/-4.24 | 50.2 | 650 | 0.0411 | 1.0 (21.36) | 1.0 | 0.0001 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1478 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 3.61/0.47/-3.11 | 50.2 | 654 | 0.0411 | 0.998 (21.3) | 1.0 | 0.0108 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1479 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=0) | -0.81/-0.75/-0.81 | 50.2 | 11 | 0.0153 | 1.0 (23.21) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1480 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=1) | 0.79/0.41/-0.29 | 50.2 | 11 | 0.0155 | 0.998 (22.95) | 1.0 | 0.0002 | 0.5025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1481 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=2) | -0.41/-0.52/-0.45 | 50.2 | 9 | 0.0145 | 1.0 (23.36) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1482 | sectors|drop_revert(drop=0.15,hold=5,n=3)+day_of_week(days=3) | 0.47/0.82/0.0 | 50.2 | 9 | 0.0148 | 0.999 (23.54) | 1.0 | 0.0002 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1483 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=0) | -0.76/-0.7/-0.82 | 50.2 | 21 | 0.0151 | 0.999 (23.02) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1484 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=1) | 0.79/0.41/-0.29 | 50.2 | 21 | 0.0155 | 0.997 (23.29) | 1.0 | 0.0002 | 0.5025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1485 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=2) | -0.41/-0.52/-0.45 | 50.2 | 22 | 0.0146 | 1.0 (23.16) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1486 | sectors|drop_revert(drop=0.15,hold=5,n=5)+day_of_week(days=3) | 0.47/0.82/0.0 | 50.2 | 25 | 0.0173 | 0.998 (23.15) | 1.0 | 0.0002 | 0.4955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1487 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=0) | -0.54/-0.48/-0.82 | 50.2 | 20 | 0.0155 | 1.0 (23.32) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1488 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=1) | 0.9/0.46/-0.29 | 50.2 | 19 | 0.0154 | 0.998 (23.03) | 1.0 | 0.0002 | 0.5005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1489 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=2) | -0.44/-0.5/-0.45 | 50.2 | 16 | 0.0144 | 1.0 (22.87) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1490 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=3) | 0.49/0.75/-0.12 | 50.2 | 16 | 0.015 | 1.0 (23.84) | 1.0 | 0.0041 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1491 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | -0.54/-0.48/-0.82 | 50.2 | 32 | 0.0155 | 1.0 (23.25) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1492 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | 0.88/0.45/-0.31 | 50.2 | 33 | 0.0155 | 0.99401 (23.36) | 1.0 | 0.0003 | 0.5005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1493 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -0.44/-0.5/-0.45 | 50.2 | 33 | 0.0148 | 0.998 (22.97) | 1.0 | 0.0 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1494 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 0.49/0.75/-0.12 | 50.2 | 37 | 0.0164 | 0.998 (22.6) | 1.0 | 0.0041 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1494

## Engine prereg 20261024_010826_gen_2410240131_003 (gen_2410240131_003, sha256 86011a87fdda): rows #1495-1498 RESERVED (4 variants). Counted in N.
N_cumulative: 1498

## Engine run 20261024_010826_gen_2410240131_003 (gen_2410240131_003): rows #1495-1498. 0/4 pass. PBO 0.344. Bar applied at N=1498. Report: engine/runs/20261024_010826_gen_2410240131_003/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1495 | sectors|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 18.34/0.78/-9.43 | 50.2 | 603 | 0.0656 | 0.60739 (20.75) | 1.0 | 0.838 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1496 | sectors|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | 16.41/0.72/-7.36 | 50.2 | 349 | 0.0645 | 0.79221 (22.04) | 1.0 | 0.8108 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1497 | sectors|supertrend(atr_n=14,mult=2)+vol_regime(max_atr_pct=0.06) | 20.22/0.83/-10.15 | 50.2 | 606 | 0.0653 | 0.53746 (21.31) | 1.0 | 0.8571 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1498 | sectors|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.06) | 16.65/0.7/-8.46 | 50.2 | 353 | 0.063 | 0.76024 (21.5) | 1.0 | 0.8034 | 0.496 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1498

## Engine prereg 20261024_020750_gen_2410240207_000 (gen_2410240207_000, sha256 e1c0ef1c5144): rows #1499-1502 RESERVED (4 variants). Counted in N.
N_cumulative: 1502

## Engine run 20261024_020750_gen_2410240207_000 (gen_2410240207_000): rows #1499-1502. 0/4 pass. PBO 0.635. Bar applied at N=1502. Report: engine/runs/20261024_020750_gen_2410240207_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1499 | crypto|sma_cross(fast=10,slow=100) | 25.71/0.61/-43.88 | 428.6 | 1018 | 0.1042 | 0.63437 (63.18) | 1.0 | 0.7166 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1500 | crypto|sma_cross(fast=10,slow=200) | 19.26/0.52/-40.09 | 428.6 | 682 | 0.1043 | 0.75524 (128.44) | 1.0 | 0.6772 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1501 | crypto|sma_cross(fast=20,slow=100) | 23.33/0.57/-42.12 | 428.6 | 793 | 0.1029 | 0.69331 (90.33) | 1.0 | 0.7008 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1502 | crypto|sma_cross(fast=20,slow=200) | 21.23/0.55/-39.12 | 428.6 | 529 | 0.1034 | 0.76124 (185.6) | 1.0 | 0.6893 | 0.906 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1502

## Engine prereg 20261024_020758_gen_2410240208_000 (gen_2410240208_000, sha256 c1e36a313d2d): rows #1503-1510 RESERVED (8 variants). Counted in N.
N_cumulative: 1510

## Engine run 20261024_020758_gen_2410240208_000 (gen_2410240208_000): rows #1503-1510. 0/8 pass. PBO 0.561. Bar applied at N=1510. Report: engine/runs/20261024_020758_gen_2410240208_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1503 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+relvol(min_ratio=1.2) | -18.73/-0.71/-26.21 | 268.18 | 375 | 0.0122 | 0.97303 (114.3) | 1.0 | 0.0012 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1504 | crypto_d|drop_revert(drop=0.05,hold=5,n=3)+relvol(min_ratio=1.2) | -4.66/-0.04/-23.27 | 268.18 | 459 | 0.0133 | 0.89111 (73.44) | 1.0 | 0.0129 | 0.9015 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1505 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.2) | -25.47/-0.79/-29.27 | 268.18 | 486 | 0.0128 | 0.98801 (122.18) | 1.0 | 0.0007 | 0.912 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1506 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.2) | -8.26/-0.12/-31.02 | 268.18 | 601 | 0.0139 | 0.89111 (134.18) | 1.0 | 0.01 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1507 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.2) | 2.21/0.6/-2.07 | 268.18 | 27 | 0.0074 | 0.92807 (48.08) | 1.0 | 0.0504 | 0.8875 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1508 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+relvol(min_ratio=1.2) | -1.65/-0.03/-9.6 | 268.18 | 90 | 0.0095 | 0.89411 (142.71) | 1.0 | 0.0132 | 0.8925 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1509 | crypto_d|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.2) | -6.23/-0.79/-8.67 | 268.18 | 38 | 0.0077 | 0.96803 (179.55) | 1.0 | 0.0 | 0.8955 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1510 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.2) | 7.77/0.41/-15.72 | 268.18 | 127 | 0.0095 | 0.7972 (140.14) | 1.0 | 0.056 | 0.8835 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1510

## Engine prereg 20261024_020800_gen_2410240209_000 (gen_2410240209_000, sha256 624f6a233fc8): rows #1511-1518 RESERVED (8 variants). Counted in N.
N_cumulative: 1518

## Engine run 20261024_020800_gen_2410240209_000 (gen_2410240209_000): rows #1511-1518. 0/8 pass. PBO 0.004. Bar applied at N=1518. Report: engine/runs/20261024_020800_gen_2410240209_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1511 | megacap|rsi_revert(entry=5,exit=70,n=2) | -9.75/-0.65/-13.23 | 26.77 | 2215 | 0.1195 | 0.82218 (1.35) | 1.0 | 0.0023 | 0.4935 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1512 | megacap|rsi_revert(entry=5,exit=70,n=3) | 2.75/0.28/-7.43 | 26.77 | 639 | 0.1191 | 0.85415 (9.05) | 1.0 | 0.0406 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1513 | megacap|rsi_revert(entry=5,exit=80,n=2) | -0.32/0.03/-11.32 | 26.77 | 1999 | 0.12 | 0.67333 (2.3) | 1.0 | 0.0224 | 0.949 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1514 | megacap|rsi_revert(entry=5,exit=80,n=3) | 8.82/0.67/-9.16 | 26.77 | 605 | 0.1188 | 0.76424 (8.99) | 1.0 | 0.107 | 0.858 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1515 | megacap|rsi_revert(entry=20,exit=70,n=2) | -15.3/-0.68/-25.16 | 26.77 | 4047 | 0.1213 | 0.5025 (-7.54) | 1.0 | 0.0014 | 0.5075 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1516 | megacap|rsi_revert(entry=20,exit=70,n=3) | -0.62/0.04/-16.97 | 26.77 | 2115 | 0.1214 | 0.73127 (1.91) | 1.0 | 0.0209 | 0.9365 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1517 | megacap|rsi_revert(entry=20,exit=80,n=2) | -8.89/-0.31/-23.93 | 26.77 | 3454 | 0.122 | 0.53247 (-4.99) | 1.0 | 0.0064 | 0.96 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1518 | megacap|rsi_revert(entry=20,exit=80,n=3) | 8.42/0.4/-16.14 | 26.77 | 1746 | 0.1211 | 0.6014 (4.08) | 1.0 | 0.0543 | 0.9065 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1518

## Engine prereg 20261024_020806_gen_2410240210_000 (gen_2410240210_000, sha256 3b21b211f148): rows #1519-1526 RESERVED (8 variants). Counted in N.
N_cumulative: 1526

## Engine run 20261024_020806_gen_2410240210_000 (gen_2410240210_000): rows #1519-1526. 0/8 pass. PBO 0.346. Bar applied at N=1526. Report: engine/runs/20261024_020806_gen_2410240210_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1519 | sectors|drop_revert(drop=0.05,hold=3,n=1) | 2.85/0.27/-2.54 | 50.2 | 50 | 0.0305 | 0.999 (23.08) | 1.0 | 0.539 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1520 | sectors|drop_revert(drop=0.05,hold=3,n=5) | 5.76/0.36/-5.1 | 50.2 | 284 | 0.0438 | 0.998 (22.38) | 1.0 | 0.6086 | 0.502 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1521 | sectors|drop_revert(drop=0.05,hold=5,n=1) | 4.7/0.34/-3.02 | 50.2 | 45 | 0.0315 | 0.999 (22.96) | 1.0 | 0.5998 | 0.4975 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1522 | sectors|drop_revert(drop=0.05,hold=5,n=5) | 7.65/0.45/-5.73 | 50.2 | 272 | 0.0438 | 0.99201 (22.55) | 1.0 | 0.6786 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1523 | sectors|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 50.2 | 9 | 0.0153 | 1.0 (23.47) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1524 | sectors|drop_revert(drop=0.1,hold=3,n=5) | 5.25/0.43/-2.63 | 50.2 | 45 | 0.0291 | 0.996 (23.12) | 1.0 | 0.6706 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1525 | sectors|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 50.2 | 8 | 0.0163 | 1.0 (23.37) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1526 | sectors|drop_revert(drop=0.1,hold=5,n=5) | 4.44/0.37/-2.63 | 50.2 | 42 | 0.0317 | 0.999 (23.31) | 1.0 | 0.6191 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1526

## Engine prereg 20261024_020810_gen_2410240211_000 (gen_2410240211_000, sha256 6ccb3148f8f7): rows #1527-1566 RESERVED (40 variants). Counted in N.
N_cumulative: 1566

## Engine run 20261024_020810_gen_2410240211_000 (gen_2410240211_000): rows #1527-1566. 0/40 pass. PBO 0.81. Bar applied at N=1566. Report: engine/runs/20261024_020810_gen_2410240211_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1527 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=0) | 8.87/0.87/-3.31 | -38.66 | 19 | 0.0347 | 0.08292 (-21.02) | 1.0 | 0.0029 | 0.256 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1528 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=1) | -1.98/-0.74/-1.99 | -38.66 | 17 | 0.0253 | 0.15385 (-20.06) | 1.0 | 0.0001 | 0.3115 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1529 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=2) | -0.48/-0.14/-1.64 | -38.66 | 23 | 0.0338 | 0.16184 (-20.44) | 1.0 | 0.0005 | 0.2995 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1530 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=3) | -1.98/-0.96/-1.98 | -38.66 | 19 | 0.0424 | 0.16484 (-20.35) | 1.0 | 0.0 | 0.312 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1531 | semis|drop_revert(drop=0.05,hold=5,n=1)+day_of_week(days=4) | -2.09/-0.87/-2.09 | -38.66 | 12 | 0.0313 | 0.16983 (-21.06) | 1.0 | 0.0 | 0.31 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1532 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=0) | 12.6/0.84/-4.78 | -38.66 | 114 | 0.0479 | 0.07393 (-23.15) | 1.0 | 0.0076 | 0.233 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1533 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=1) | 4.57/0.49/-5.78 | -38.66 | 135 | 0.0555 | 0.1029 (-21.63) | 1.0 | 0.0053 | 0.2745 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1534 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=2) | -3.55/-0.31/-9.67 | -38.66 | 152 | 0.0514 | 0.21179 (-20.9) | 1.0 | 0.0003 | 0.3045 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1535 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=3) | -11.04/-0.94/-15.75 | -38.66 | 166 | 0.0494 | 0.20679 (-23.09) | 1.0 | 0.0 | 0.375 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1536 | semis|drop_revert(drop=0.05,hold=5,n=5)+day_of_week(days=4) | -13.18/-0.99/-17.9 | -38.66 | 166 | 0.0507 | 0.31868 (-21.83) | 1.0 | 0.0 | 0.3775 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1537 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=0) | 14.58/1.1/-3.76 | -38.66 | 28 | 0.0347 | 0.02398 (-21.55) | 1.0 | 0.0098 | 0.2245 | False | min_trades, cost_stop, holm, dsr, spa, pbo |
| 1538 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=1) | 2.24/0.46/-4.02 | -38.66 | 35 | 0.0272 | 0.07692 (-21.95) | 1.0 | 0.0047 | 0.2885 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1539 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=2) | 0.73/0.13/-4.92 | -38.66 | 33 | 0.0326 | 0.16184 (-20.82) | 1.0 | 0.0022 | 0.2895 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1540 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=3) | -0.62/-0.1/-3.99 | -38.66 | 35 | 0.0388 | 0.14086 (-21.2) | 1.0 | 0.0007 | 0.3005 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1541 | semis|drop_revert(drop=0.05,hold=10,n=1)+day_of_week(days=4) | 0.48/0.13/-1.71 | -38.66 | 30 | 0.0393 | 0.14885 (-19.12) | 1.0 | 0.0 | 0.2935 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1542 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | 16.5/0.83/-9.67 | -38.66 | 150 | 0.0492 | 0.04396 (-20.88) | 1.0 | 0.0116 | 0.217 | False | cost_stop, holm, dsr, spa, pbo |
| 1543 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 2.75/0.29/-11.47 | -38.66 | 179 | 0.0551 | 0.07293 (-21.97) | 1.0 | 0.0027 | 0.2755 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1544 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | 1.21/0.12/-15.49 | -38.66 | 182 | 0.0529 | 0.14985 (-21.46) | 1.0 | 0.001 | 0.262 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1545 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | -12.49/-0.92/-18.59 | -38.66 | 202 | 0.0502 | 0.21678 (-22.24) | 1.0 | 0.0 | 0.3745 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1546 | semis|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=4) | -10.5/-0.61/-17.16 | -38.66 | 214 | 0.0509 | 0.32967 (-22.58) | 1.0 | 0.0 | 0.36 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1547 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=0) | 1.61/0.53/-1.5 | -38.66 | 5 | 0.0204 | 0.13487 (-22.65) | 1.0 | 0.0061 | 0.292 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1548 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=1) | -1.0/-0.88/-1.0 | -38.66 | 5 | 0.0183 | 0.11389 (-20.91) | 1.0 | 0.0 | 0.305 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1549 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=2) | 1.99/0.83/-1.11 | -38.66 | 6 | 0.031 | 0.12587 (-20.65) | 1.0 | 0.0157 | 0.286 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1550 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=3) | -0.63/-0.48/-1.01 | -38.66 | 3 | 0.025 | 0.12987 (-22.42) | 1.0 | 0.0 | 0.302 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1551 | semis|drop_revert(drop=0.1,hold=5,n=1)+day_of_week(days=4) | 0.0/0.0/0.0 | -38.66 | 2 | 0.0227 | 0.1049 (-20.95) | 1.0 | 0.0 | 0.2995 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1552 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=0) | 3.83/0.65/-3.2 | -38.66 | 16 | 0.0269 | 0.13487 (-20.47) | 1.0 | 0.0077 | 0.2805 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1553 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=1) | 1.09/0.28/-2.04 | -38.66 | 13 | 0.0209 | 0.07592 (-22.08) | 1.0 | 0.0015 | 0.2925 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1554 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=2) | 0.24/0.06/-6.52 | -38.66 | 17 | 0.0311 | 0.14885 (-19.81) | 1.0 | 0.0014 | 0.29 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1555 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=3) | -1.88/-0.42/-4.44 | -38.66 | 20 | 0.0309 | 0.11289 (-20.96) | 1.0 | 0.0001 | 0.3075 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1556 | semis|drop_revert(drop=0.1,hold=5,n=5)+day_of_week(days=4) | -1.0/-0.28/-2.52 | -38.66 | 16 | 0.0374 | 0.18482 (-20.83) | 1.0 | 0.0 | 0.3025 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1557 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=0) | 1.43/0.44/-2.02 | -38.66 | 6 | 0.0209 | 0.15884 (-20.25) | 1.0 | 0.003 | 0.287 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1558 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=1) | -1.68/-1.23/-1.7 | -38.66 | 11 | 0.0188 | 0.13886 (-20.55) | 1.0 | 0.0 | 0.309 | False | oos_positive, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1559 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=2) | 3.95/1.21/-0.55 | -38.66 | 8 | 0.0289 | 0.11788 (-20.42) | 1.0 | 0.005 | 0.273 | False | min_trades, holm, dsr, spa, pbo |
| 1560 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=3) | 1.32/0.53/-1.41 | -38.66 | 6 | 0.0236 | 0.11389 (-19.88) | 1.0 | 0.0031 | 0.2895 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1561 | semis|drop_revert(drop=0.1,hold=10,n=1)+day_of_week(days=4) | 0.22/0.24/-0.4 | -38.66 | 4 | 0.0231 | 0.1039 (-20.75) | 1.0 | 0.0015 | 0.2965 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1562 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=0) | 10.92/1.01/-3.04 | -38.66 | 24 | 0.0269 | 0.07493 (-20.39) | 1.0 | 0.0108 | 0.2405 | False | min_trades, holm, dsr, spa, pbo |
| 1563 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=1) | 1.17/0.25/-4.22 | -38.66 | 24 | 0.0272 | 0.12987 (-20.03) | 1.0 | 0.0022 | 0.294 | False | min_trades, walk_forward, holm, dsr, spa, pbo |
| 1564 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=2) | -0.92/-0.12/-6.19 | -38.66 | 23 | 0.0303 | 0.15884 (-21.53) | 1.0 | 0.0005 | 0.296 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1565 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=3) | 2.77/0.47/-5.5 | -38.66 | 27 | 0.0352 | 0.06394 (-21.74) | 1.0 | 0.0054 | 0.282 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1566 | semis|drop_revert(drop=0.1,hold=10,n=5)+day_of_week(days=4) | -5.32/-0.91/-6.01 | -38.66 | 23 | 0.0409 | 0.19181 (-21.01) | 1.0 | 0.0 | 0.332 | False | oos_positive, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1566

## Engine prereg 20261024_020821_gen_2410240212_000 (gen_2410240212_000, sha256 89212d665db4): rows #1567-1570 RESERVED (4 variants). Counted in N.
N_cumulative: 1570

## Engine run 20261024_020821_gen_2410240212_000 (gen_2410240212_000): rows #1567-1570. 0/4 pass. PBO 0.622. Bar applied at N=1570. Report: engine/runs/20261024_020821_gen_2410240212_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1567 | hibeta|supertrend(atr_n=7,mult=3) | 291.77/1.56/-31.99 | 809.88 | 164 | 0.0236 | 0.2028 (215.41) | 1.0 | 0.9232 | 0.503 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1568 | hibeta|supertrend(atr_n=7,mult=4) | 210.85/1.29/-24.5 | 809.88 | 104 | 0.0231 | 0.47952 (221.67) | 1.0 | 0.8247 | 0.514 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1569 | hibeta|supertrend(atr_n=10,mult=3) | 355.71/1.77/-23.24 | 809.88 | 162 | 0.024 | 0.07393 (216.81) | 1.0 | 0.9652 | 0.5005 | False | beats_buy_hold, holm, spa, pbo |
| 1570 | hibeta|supertrend(atr_n=10,mult=4) | 222.71/1.33/-26.1 | 809.88 | 105 | 0.0231 | 0.45355 (225.02) | 1.0 | 0.8428 | 0.511 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 1570

## Engine prereg 20261024_020824_gen_2410240213_000 (gen_2410240213_000, sha256 81ae0b2884e4): rows #1571-1578 RESERVED (8 variants). Counted in N.
N_cumulative: 1578

## Engine run 20261024_020824_gen_2410240213_000 (gen_2410240213_000): rows #1571-1578. 0/8 pass. PBO 0.439. Bar applied at N=1578. Report: engine/runs/20261024_020824_gen_2410240213_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1571 | defensive|rsi_revert(entry=5,exit=60,n=2) | 26.3/1.79/-2.29 | 104.36 | 251 | 0.0654 | 0.84715 (40.18) | 1.0 | 0.6303 | 0.516 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1572 | defensive|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 104.36 | 3 | 0.0393 | 1.0 (30.69) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1573 | defensive|rsi_revert(entry=5,exit=80,n=2) | 30.49/1.49/-4.81 | 104.36 | 231 | 0.0658 | 0.75025 (41.19) | 1.0 | 0.405 | 0.51 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1574 | defensive|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 104.36 | 3 | 0.0393 | 1.0 (30.69) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1575 | defensive|rsi_revert(entry=20,exit=60,n=2) | 11.41/0.53/-8.81 | 104.36 | 702 | 0.0677 | 0.97203 (36.37) | 1.0 | 0.0291 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1576 | defensive|rsi_revert(entry=20,exit=60,n=5) | 20.91/1.07/-6.91 | 104.36 | 144 | 0.0625 | 0.92408 (41.0) | 1.0 | 0.1578 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1577 | defensive|rsi_revert(entry=20,exit=80,n=2) | 22.68/0.81/-7.38 | 104.36 | 554 | 0.0671 | 0.87612 (38.06) | 1.0 | 0.0808 | 0.51 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1578 | defensive|rsi_revert(entry=20,exit=80,n=5) | 41.58/1.5/-6.97 | 104.36 | 104 | 0.0625 | 0.53646 (43.36) | 1.0 | 0.4133 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1578

## Engine prereg 20261024_020827_gen_2410240214_000 (gen_2410240214_000, sha256 163c13dbc947): rows #1579-1586 RESERVED (8 variants). Counted in N.
N_cumulative: 1586

## Engine run 20261024_020827_gen_2410240214_000 (gen_2410240214_000): rows #1579-1586. 0/8 pass. PBO 0.457. Bar applied at N=1586. Report: engine/runs/20261024_020827_gen_2410240214_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1579 | crypto|drop_revert(drop=0.05,hold=3,n=1)+vol_regime(max_atr_pct=0.06) | -2.53/-0.52/-3.98 | 428.6 | 147 | 0.0281 | 0.92108 (77.02) | 1.0 | 0.0001 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1580 | crypto|drop_revert(drop=0.05,hold=3,n=3)+vol_regime(max_atr_pct=0.06) | 5.75/0.65/-3.45 | 428.6 | 507 | 0.0364 | 0.89111 (87.23) | 1.0 | 0.0322 | 0.9035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1581 | crypto|drop_revert(drop=0.05,hold=5,n=1)+vol_regime(max_atr_pct=0.06) | -3.07/-0.47/-4.02 | 428.6 | 154 | 0.0274 | 0.91808 (87.24) | 1.0 | 0.0002 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1582 | crypto|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.06) | 13.89/0.98/-5.04 | 428.6 | 482 | 0.0373 | 0.81518 (75.54) | 1.0 | 0.0696 | 0.896 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1583 | crypto|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.06) | -0.6/-0.82/-0.6 | 428.6 | 6 | 0.0188 | 0.95105 (296.69) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1584 | crypto|drop_revert(drop=0.1,hold=3,n=3)+vol_regime(max_atr_pct=0.06) | 0.46/0.34/-0.71 | 428.6 | 21 | 0.0216 | 0.95704 (59.06) | 1.0 | 0.0066 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1585 | crypto|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.06) | 0.35/0.26/-0.6 | 428.6 | 7 | 0.0181 | 0.95305 (46.47) | 1.0 | 0.0056 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1586 | crypto|drop_revert(drop=0.1,hold=5,n=3)+vol_regime(max_atr_pct=0.06) | 1.51/0.69/-0.6 | 428.6 | 25 | 0.0207 | 0.96204 (74.49) | 1.0 | 0.006 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 1586

## Engine prereg 20261024_020833_gen_2410240215_000 (gen_2410240215_000, sha256 2ff544d11c85): rows #1587-1590 RESERVED (4 variants). Counted in N.
N_cumulative: 1590

## Engine run 20261024_020833_gen_2410240215_000 (gen_2410240215_000): rows #1587-1590. 0/4 pass. PBO 0.833. Bar applied at N=1590. Report: engine/runs/20261024_020833_gen_2410240215_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1587 | crypto_d|sma_cross(fast=5,slow=50) | 11.81/0.39/-28.07 | 268.18 | 93 | 0.0177 | 0.80519 (102.73) | 1.0 | 0.3342 | 0.8845 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1588 | crypto_d|sma_cross(fast=5,slow=200) | -1.73/0.15/-25.63 | 268.18 | 31 | 0.0191 | 0.89311 (127.13) | 1.0 | 0.2357 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1589 | crypto_d|sma_cross(fast=10,slow=50) | 22.99/0.56/-28.64 | 268.18 | 77 | 0.0175 | 0.70929 (92.52) | 1.0 | 0.4101 | 0.8595 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1590 | crypto_d|sma_cross(fast=10,slow=200) | -5.13/0.08/-28.47 | 268.18 | 25 | 0.0197 | 0.91508 (106.21) | 1.0 | 0.2115 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1590

## Engine prereg 20261024_020835_gen_2410240216_000 (gen_2410240216_000, sha256 9a7ba414493b): rows #1591-1598 RESERVED (8 variants). Counted in N.
N_cumulative: 1598

## Engine run 20261024_020835_gen_2410240216_000 (gen_2410240216_000): rows #1591-1598. 0/8 pass. PBO 0.606. Bar applied at N=1598. Report: engine/runs/20261024_020835_gen_2410240216_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1591 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.8991 (12.54) | 1.0 | 0.5372 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1592 | megacap|drop_revert(drop=0.05,hold=3,n=5) | 3.92/0.71/-2.86 | 26.77 | 203 | 0.0576 | 0.75125 (12.25) | 1.0 | 0.5905 | 0.863 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1593 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.92308 (12.92) | 1.0 | 0.4099 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1594 | megacap|drop_revert(drop=0.05,hold=5,n=5) | 3.66/0.52/-6.0 | 26.77 | 193 | 0.0582 | 0.63137 (12.72) | 1.0 | 0.5007 | 0.8535 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1595 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.87/0.42/-0.92 | 26.77 | 9 | 0.0287 | 0.96004 (13.24) | 1.0 | 0.4409 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1596 | megacap|drop_revert(drop=0.1,hold=3,n=5) | 1.39/0.58/-1.11 | 26.77 | 16 | 0.029 | 0.94306 (13.69) | 1.0 | 0.5244 | 0.8915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1597 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.93/0.37/-1.25 | 26.77 | 9 | 0.0287 | 0.93407 (12.56) | 1.0 | 0.4195 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1598 | megacap|drop_revert(drop=0.1,hold=5,n=5) | 1.57/0.82/-0.9 | 26.77 | 16 | 0.029 | 0.92507 (13.01) | 1.0 | 0.643 | 0.894 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1598

## Engine prereg 20261024_030905_gen_2410240307_000 (gen_2410240307_000, sha256 147e15467c1d): rows #1599-1602 RESERVED (4 variants). Counted in N.
N_cumulative: 1602

## Engine run 20261024_030905_gen_2410240307_000 (gen_2410240307_000): rows #1599-1602. 0/4 pass. PBO 0.736. Bar applied at N=1602. Report: engine/runs/20261024_030905_gen_2410240307_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1599 | megacap|sma_cross(fast=5,slow=50) | 99.16/1.47/-12.02 | 214.9 | 191 | 0.0428 | 0.18282 (78.28) | 1.0 | 0.9883 | 0.4985 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 1600 | megacap|sma_cross(fast=5,slow=150) | 91.05/1.36/-16.72 | 214.9 | 92 | 0.0409 | 0.34266 (78.63) | 1.0 | 0.9767 | 0.511 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 1601 | megacap|sma_cross(fast=10,slow=50) | 102.65/1.49/-10.83 | 214.9 | 151 | 0.0446 | 0.14585 (78.64) | 1.0 | 0.9889 | 0.501 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 1602 | megacap|sma_cross(fast=10,slow=150) | 99.98/1.46/-14.43 | 214.9 | 67 | 0.0419 | 0.27273 (79.89) | 1.0 | 0.985 | 0.5145 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

N_cumulative: 1602

## Engine prereg 20261024_030911_gen_2410240308_000 (gen_2410240308_000, sha256 dd09fb2aeeb1): rows #1603-1606 RESERVED (4 variants). Counted in N.
N_cumulative: 1606

## Engine run 20261024_030911_gen_2410240308_000 (gen_2410240308_000): rows #1603-1606. 0/4 pass. PBO 0.844. Bar applied at N=1606. Report: engine/runs/20261024_030911_gen_2410240308_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1603 | megacap|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.0) | 10.85/0.4/-7.77 | 214.9 | 1182 | 0.0507 | 1.0 (66.78) | 1.0 | 0.6208 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1604 | megacap|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | 10.81/0.39/-7.91 | 214.9 | 1144 | 0.0518 | 1.0 (67.56) | 1.0 | 0.6098 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1605 | megacap|supertrend(atr_n=14,mult=3)+relvol(min_ratio=1.0) | 15.48/0.53/-7.83 | 214.9 | 1217 | 0.0506 | 1.0 (65.79) | 1.0 | 0.707 | 0.4845 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1606 | megacap|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.0) | 13.64/0.47/-8.23 | 214.9 | 1180 | 0.0511 | 1.0 (67.01) | 1.0 | 0.6676 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1606

## Engine prereg 20261024_030914_gen_2410240309_000 (gen_2410240309_000, sha256 4ebaf45ae1f6): rows #1607-1614 RESERVED (8 variants). Counted in N.
N_cumulative: 1614

## Engine run 20261024_030914_gen_2410240309_000 (gen_2410240309_000): rows #1607-1614. 0/8 pass. PBO 0.276. Bar applied at N=1614. Report: engine/runs/20261024_030914_gen_2410240309_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1607 | sectors|drop_revert(drop=0.05,hold=3,n=3) | 8.85/0.47/-4.13 | 57.67 | 157 | 0.0389 | 0.96204 (25.63) | 1.0 | 0.3625 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1608 | sectors|drop_revert(drop=0.05,hold=3,n=5) | 5.79/0.3/-6.67 | 57.67 | 196 | 0.0419 | 0.99001 (24.97) | 1.0 | 0.2632 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1609 | sectors|drop_revert(drop=0.05,hold=10,n=3) | 20.92/0.86/-5.39 | 57.67 | 116 | 0.042 | 0.68232 (26.08) | 1.0 | 0.6678 | 0.9275 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1610 | sectors|drop_revert(drop=0.05,hold=10,n=5) | 18.09/0.71/-6.08 | 57.67 | 143 | 0.0446 | 0.78621 (25.99) | 1.0 | 0.5515 | 0.9655 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1611 | sectors|drop_revert(drop=0.1,hold=3,n=3) | 4.61/0.31/-3.58 | 57.67 | 19 | 0.0257 | 0.99201 (25.98) | 1.0 | 0.253 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1612 | sectors|drop_revert(drop=0.1,hold=3,n=5) | 7.62/0.49/-3.58 | 57.67 | 30 | 0.0289 | 0.96803 (26.99) | 1.0 | 0.3664 | 0.9795 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1613 | sectors|drop_revert(drop=0.1,hold=10,n=3) | 7.38/0.44/-4.5 | 57.67 | 17 | 0.0269 | 0.97203 (26.26) | 1.0 | 0.3409 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1614 | sectors|drop_revert(drop=0.1,hold=10,n=5) | 7.92/0.48/-4.5 | 57.67 | 24 | 0.0317 | 0.97403 (26.32) | 1.0 | 0.3641 | 0.9805 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1614

## Engine prereg 20261024_030917_gen_2410240310_000 (gen_2410240310_000, sha256 0df351676369): rows #1615-1622 RESERVED (8 variants). Counted in N.
N_cumulative: 1622

## Engine run 20261024_030917_gen_2410240310_000 (gen_2410240310_000): rows #1615-1622. 0/8 pass. PBO 0.955. Bar applied at N=1622. Report: engine/runs/20261024_030917_gen_2410240310_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1615 | sectors|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.02) | 0.11/0.04/-1.04 | 57.67 | 36 | 0.0578 | 1.0 (26.42) | 1.0 | 0.0137 | 0.4885 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1616 | sectors|drop_revert(drop=0.05,hold=5,n=5)+vol_regime(max_atr_pct=0.02) | -0.03/0.0/-2.26 | 57.67 | 67 | 0.0562 | 1.0 (26.1) | 1.0 | 0.0116 | 0.4885 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1617 | sectors|drop_revert(drop=0.05,hold=10,n=3)+vol_regime(max_atr_pct=0.02) | 2.84/0.77/-1.11 | 57.67 | 50 | 0.0547 | 1.0 (26.55) | 1.0 | 0.1811 | 0.488 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1618 | sectors|drop_revert(drop=0.05,hold=10,n=5)+vol_regime(max_atr_pct=0.02) | 3.67/0.6/-2.58 | 57.67 | 85 | 0.0535 | 0.998 (26.16) | 1.0 | 0.1125 | 0.4855 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1619 | sectors|drop_revert(drop=0.15,hold=5,n=3)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1620 | sectors|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (27.27) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1621 | sectors|drop_revert(drop=0.15,hold=10,n=3)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 0 | inf | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1622 | sectors|drop_revert(drop=0.15,hold=10,n=5)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 57.67 | 1 | 0.0509 | 1.0 (26.03) | 1.0 | 0.0 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1622

## Engine prereg 20261024_030920_gen_2410240311_000 (gen_2410240311_000, sha256 6e4e181d0465): rows #1623-1626 RESERVED (4 variants). Counted in N.
N_cumulative: 1626

## Engine run 20261024_030920_gen_2410240311_000 (gen_2410240311_000): rows #1623-1626. 0/4 pass. PBO 0.455. Bar applied at N=1626. Report: engine/runs/20261024_030920_gen_2410240311_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1623 | crypto|supertrend(atr_n=10,mult=2)+trend_sma(n=50) | -8.58/-0.04/-32.08 | 428.6 | 3240 | 0.1024 | 0.73227 (108.51) | 1.0 | 0.3168 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1624 | crypto|supertrend(atr_n=10,mult=4)+trend_sma(n=50) | 2.77/0.22/-38.65 | 428.6 | 2505 | 0.1067 | 0.68731 (46.15) | 1.0 | 0.4309 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1625 | crypto|supertrend(atr_n=14,mult=2)+trend_sma(n=50) | -0.59/0.14/-30.62 | 428.6 | 3241 | 0.1017 | 0.68631 (67.39) | 1.0 | 0.3966 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1626 | crypto|supertrend(atr_n=14,mult=4)+trend_sma(n=50) | -1.79/0.12/-40.68 | 428.6 | 2520 | 0.1054 | 0.75025 (107.31) | 1.0 | 0.3861 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1626

## Engine prereg 20261024_030926_gen_2410240312_000 (gen_2410240312_000, sha256 14ef478e19f2): rows #1627-1634 RESERVED (8 variants). Counted in N.
N_cumulative: 1634

## Engine run 20261024_030926_gen_2410240312_000 (gen_2410240312_000): rows #1627-1634. 0/8 pass. PBO 0.174. Bar applied at N=1634. Report: engine/runs/20261024_030926_gen_2410240312_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1627 | crypto|rsi_revert(entry=5,exit=70,n=2) | -1.97/0.06/-16.18 | 428.6 | 3220 | 0.0973 | 0.6963 (50.87) | 1.0 | 0.0274 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1628 | crypto|rsi_revert(entry=5,exit=70,n=3) | -33.58/-1.43/-37.94 | 428.6 | 918 | 0.0921 | 0.998 (178.03) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1629 | crypto|rsi_revert(entry=5,exit=80,n=2) | -8.09/-0.07/-25.09 | 428.6 | 2973 | 0.0981 | 0.75225 (51.66) | 1.0 | 0.0184 | 0.9155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1630 | crypto|rsi_revert(entry=5,exit=80,n=3) | -28.75/-0.91/-33.41 | 428.6 | 846 | 0.0923 | 0.996 (156.3) | 1.0 | 0.0004 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1631 | crypto|rsi_revert(entry=10,exit=70,n=2) | -13.03/-0.19/-27.38 | 428.6 | 5399 | 0.1007 | 0.5994 (21.4) | 1.0 | 0.0126 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1632 | crypto|rsi_revert(entry=10,exit=70,n=3) | -17.11/-0.36/-30.56 | 428.6 | 2131 | 0.0978 | 0.91009 (50.9) | 1.0 | 0.0061 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1633 | crypto|rsi_revert(entry=10,exit=80,n=2) | -26.82/-0.47/-40.98 | 428.6 | 4730 | 0.1014 | 0.78422 (14.83) | 1.0 | 0.0044 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1634 | crypto|rsi_revert(entry=10,exit=80,n=3) | -18.34/-0.28/-33.41 | 428.6 | 1826 | 0.099 | 0.94406 (54.95) | 1.0 | 0.0086 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1634

## Engine prereg 20261024_030935_gen_2410240313_000 (gen_2410240313_000, sha256 f8887bc14aee): rows #1635-1638 RESERVED (4 variants). Counted in N.
N_cumulative: 1638

## Engine run 20261024_030935_gen_2410240313_000 (gen_2410240313_000): rows #1635-1638. 0/4 pass. PBO 0.5. Bar applied at N=1638. Report: engine/runs/20261024_030935_gen_2410240313_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1635 | crypto|sma_cross(fast=20,slow=150)+rsi_band(hi=80) | 9.9/0.36/-37.69 | 428.6 | 928 | 0.0972 | 0.78721 (129.44) | 1.0 | 0.2892 | 0.9185 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1636 | crypto|sma_cross(fast=20,slow=200)+rsi_band(hi=80) | 13.9/0.43/-38.8 | 428.6 | 817 | 0.1002 | 0.77922 (150.75) | 1.0 | 0.3175 | 0.9125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1637 | crypto|sma_cross(fast=50,slow=150)+rsi_band(hi=80) | 34.85/0.75/-35.56 | 428.6 | 728 | 0.0996 | 0.63237 (143.97) | 1.0 | 0.462 | 0.893 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1638 | crypto|sma_cross(fast=50,slow=200)+rsi_band(hi=80) | 42.1/0.87/-34.57 | 428.6 | 623 | 0.1001 | 0.61738 (169.75) | 1.0 | 0.5192 | 0.882 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1638

## Engine prereg 20261024_030939_gen_2410240314_000 (gen_2410240314_000, sha256 7d5246bd2ab2): rows #1639-1646 RESERVED (8 variants). Counted in N.
N_cumulative: 1646

## Engine run 20261024_030939_gen_2410240314_000 (gen_2410240314_000): rows #1639-1646. 0/8 pass. PBO 0.09. Bar applied at N=1646. Report: engine/runs/20261024_030939_gen_2410240314_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1639 | crypto|rsi_revert(entry=10,exit=60,n=2) | -28.7/-0.77/-30.12 | 428.6 | 5809 | 0.1004 | 0.75225 (63.8) | 1.0 | 0.0051 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1640 | crypto|rsi_revert(entry=10,exit=60,n=3) | -12.19/-0.29/-23.96 | 428.6 | 2329 | 0.0961 | 0.86214 (73.53) | 1.0 | 0.026 | 0.9185 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1641 | crypto|rsi_revert(entry=10,exit=80,n=2) | -26.82/-0.47/-40.98 | 428.6 | 4730 | 0.1014 | 0.7952 (16.69) | 1.0 | 0.0154 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1642 | crypto|rsi_revert(entry=10,exit=80,n=3) | -18.34/-0.28/-33.41 | 428.6 | 1826 | 0.099 | 0.92108 (74.12) | 1.0 | 0.0271 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1643 | crypto|rsi_revert(entry=20,exit=60,n=2) | -49.65/-1.35/-51.19 | 428.6 | 9537 | 0.1013 | 0.72527 (2.35) | 1.0 | 0.0004 | 0.926 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1644 | crypto|rsi_revert(entry=20,exit=60,n=3) | -28.41/-0.59/-39.75 | 428.6 | 4920 | 0.1012 | 0.81119 (25.89) | 1.0 | 0.0101 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1645 | crypto|rsi_revert(entry=20,exit=80,n=2) | -37.55/-0.65/-54.44 | 428.6 | 6954 | 0.103 | 0.75624 (6.62) | 1.0 | 0.0084 | 0.926 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1646 | crypto|rsi_revert(entry=20,exit=80,n=3) | -17.84/-0.13/-44.65 | 428.6 | 3211 | 0.1017 | 0.83716 (27.55) | 1.0 | 0.0425 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1646

## Engine prereg 20261024_030947_gen_2410240315_000 (gen_2410240315_000, sha256 84811ff60c9f): rows #1647-1662 RESERVED (16 variants). Counted in N.
N_cumulative: 1662

## Engine run 20261024_030947_gen_2410240315_000 (gen_2410240315_000): rows #1647-1662. 0/16 pass. PBO 0.138. Bar applied at N=1662. Report: engine/runs/20261024_030947_gen_2410240315_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1647 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | -12.8/-0.53/-25.49 | 234.6 | 548 | 0.0158 | 0.95205 (105.21) | 1.0 | 0.003 | 0.9025 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1648 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | 6.77/0.37/-13.04 | 234.6 | 531 | 0.0155 | 0.82817 (59.78) | 1.0 | 0.052 | 0.888 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1649 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | -1.68/0.03/-13.1 | 234.6 | 529 | 0.0159 | 0.90809 (100.6) | 1.0 | 0.0202 | 0.901 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1650 | crypto_d|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -5.44/-0.14/-27.16 | 234.6 | 523 | 0.0158 | 0.91309 (64.19) | 1.0 | 0.0121 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1651 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | -15.3/-0.66/-23.2 | 234.6 | 596 | 0.0156 | 0.97003 (96.27) | 1.0 | 0.0022 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1652 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | 11.46/0.54/-14.95 | 234.6 | 598 | 0.0153 | 0.8022 (85.03) | 1.0 | 0.0752 | 0.8845 | False | beats_buy_hold, holm, dsr, spa |
| 1653 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | -25.72/-0.93/-25.72 | 234.6 | 600 | 0.0152 | 0.99401 (65.56) | 1.0 | 0.0006 | 0.921 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1654 | crypto_d|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 0.41/0.11/-22.3 | 234.6 | 597 | 0.015 | 0.88511 (97.3) | 1.0 | 0.026 | 0.903 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1655 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -10.68/-0.4/-25.51 | 234.6 | 546 | 0.0162 | 0.95105 (90.6) | 1.0 | 0.0053 | 0.8995 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1656 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | 5.02/0.31/-13.17 | 234.6 | 530 | 0.0159 | 0.84116 (66.5) | 1.0 | 0.0441 | 0.8895 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1657 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | -3.72/-0.06/-12.46 | 234.6 | 528 | 0.0161 | 0.92408 (113.6) | 1.0 | 0.0164 | 0.9005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1658 | crypto_d|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -7.58/-0.24/-27.63 | 234.6 | 518 | 0.0162 | 0.94306 (79.49) | 1.0 | 0.0082 | 0.9105 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1659 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -16.8/-0.81/-22.58 | 234.6 | 569 | 0.0156 | 0.98901 (62.8) | 1.0 | 0.0011 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1660 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | 14.35/0.66/-14.65 | 234.6 | 571 | 0.0154 | 0.76823 (92.61) | 1.0 | 0.0981 | 0.8815 | False | beats_buy_hold, holm, dsr, spa |
| 1661 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | -24.57/-0.9/-24.62 | 234.6 | 572 | 0.0156 | 0.99001 (89.57) | 1.0 | 0.0007 | 0.9205 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1662 | crypto_d|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 0.59/0.12/-24.72 | 234.6 | 570 | 0.0153 | 0.87313 (73.4) | 1.0 | 0.0278 | 0.902 | False | beats_buy_hold, walk_forward, holm, dsr, spa |

N_cumulative: 1662

## Engine prereg 20261024_030951_gen_2410240316_000 (gen_2410240316_000, sha256 6cd6ed2700b2): rows #1663-1666 RESERVED (4 variants). Counted in N.
N_cumulative: 1666

## Engine run 20261024_030951_gen_2410240316_000 (gen_2410240316_000): rows #1663-1666. 0/4 pass. PBO 0.794. Bar applied at N=1666. Report: engine/runs/20261024_030951_gen_2410240316_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1663 | crypto_d|donchian(entry_n=20,exit_n=10) | -12.9/-0.11/-31.6 | 234.6 | 110 | 0.0173 | 0.97003 (77.95) | 1.0 | 0.0698 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1664 | crypto_d|donchian(entry_n=20,exit_n=20) | -2.02/0.17/-38.62 | 234.6 | 80 | 0.0168 | 0.91608 (77.66) | 1.0 | 0.1263 | 0.91 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1665 | crypto_d|donchian(entry_n=100,exit_n=10) | 15.9/0.55/-21.16 | 234.6 | 39 | 0.0184 | 0.78022 (142.29) | 1.0 | 0.2438 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1666 | crypto_d|donchian(entry_n=100,exit_n=20) | 19.48/0.59/-23.98 | 234.6 | 32 | 0.0186 | 0.71029 (55.56) | 1.0 | 0.2583 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1666

## Engine prereg 20261024_030953_gen_2410240317_000 (gen_2410240317_000, sha256 4089134b3efd): rows #1667-1674 RESERVED (8 variants). Counted in N.
N_cumulative: 1674

## Engine run 20261024_030953_gen_2410240317_000 (gen_2410240317_000): rows #1667-1674. 0/8 pass. PBO 0.805. Bar applied at N=1674. Report: engine/runs/20261024_030953_gen_2410240317_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1667 | semis|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 1.53/0.55/-0.47 | 440.15 | 3 | 0.0179 | 0.998 (142.87) | 1.0 | 0.171 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1668 | semis|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=50) | 0.77/0.17/-2.47 | 440.15 | 27 | 0.0195 | 1.0 (137.67) | 1.0 | 0.0962 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1669 | semis|drop_revert(drop=0.1,hold=10,n=1)+trend_sma(n=50) | 3.12/0.54/-1.23 | 440.15 | 9 | 0.0185 | 1.0 (139.7) | 1.0 | 0.2512 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1670 | semis|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=50) | 10.87/1.12/-2.12 | 440.15 | 56 | 0.019 | 1.0 (141.29) | 1.0 | 0.6447 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1671 | semis|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 1.01/0.59/-0.25 | 440.15 | 1 | 0.0179 | 0.996 (144.66) | 1.0 | 0.1883 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1672 | semis|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=50) | 0.99/0.51/-0.32 | 440.15 | 5 | 0.0195 | 0.99301 (143.83) | 1.0 | 0.1812 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1673 | semis|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=50) | 2.21/0.7/-0.62 | 440.15 | 2 | 0.0141 | 0.99301 (141.49) | 1.0 | 0.3242 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1674 | semis|drop_revert(drop=0.15,hold=10,n=3)+trend_sma(n=50) | 2.53/0.8/-0.62 | 440.15 | 10 | 0.0183 | 0.99201 (137.24) | 1.0 | 0.4008 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1674

## Engine prereg 20261024_030956_gen_2410240318_000 (gen_2410240318_000, sha256 e015e0abdf1a): rows #1675-1690 RESERVED (16 variants). Counted in N.
N_cumulative: 1690

## Engine run 20261024_030956_gen_2410240318_000 (gen_2410240318_000): rows #1675-1690. 0/16 pass. PBO 0.004. Bar applied at N=1690. Report: engine/runs/20261024_030956_gen_2410240318_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1675 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=1) | 26.01/0.56/-25.23 | 872.11 | 1255 | 0.0242 | 1.0 (195.55) | 1.0 | 0.0015 | 0.502 | False | beats_buy_hold, holm, dsr, spa |
| 1676 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=2) | -29.52/-0.67/-35.62 | 872.11 | 1240 | 0.024 | 1.0 (198.59) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1677 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=3) | 30.31/0.63/-15.68 | 872.11 | 1222 | 0.0241 | 1.0 (199.1) | 1.0 | 0.0025 | 0.495 | False | beats_buy_hold, holm, dsr, spa |
| 1678 | hibeta|sma_cross(fast=5,slow=100)+day_of_week(days=4) | 55.27/1.12/-14.7 | 872.11 | 1232 | 0.0241 | 0.996 (199.19) | 1.0 | 0.0236 | 0.502 | False | beats_buy_hold, holm, dsr, spa |
| 1679 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=1) | 36.57/0.73/-21.31 | 872.11 | 1237 | 0.024 | 0.999 (198.82) | 1.0 | 0.0036 | 0.499 | False | beats_buy_hold, holm, dsr, spa |
| 1680 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=2) | -27.47/-0.61/-36.15 | 872.11 | 1219 | 0.0239 | 1.0 (200.48) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1681 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=3) | 28.57/0.58/-14.56 | 872.11 | 1201 | 0.0239 | 1.0 (196.14) | 1.0 | 0.0022 | 0.493 | False | beats_buy_hold, holm, dsr, spa |
| 1682 | hibeta|sma_cross(fast=5,slow=150)+day_of_week(days=4) | 46.62/0.97/-13.95 | 872.11 | 1208 | 0.024 | 0.997 (193.16) | 1.0 | 0.0112 | 0.504 | False | beats_buy_hold, holm, dsr, spa |
| 1683 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=1) | 19.28/0.45/-27.07 | 872.11 | 1258 | 0.0241 | 0.999 (196.48) | 1.0 | 0.0008 | 0.4985 | False | beats_buy_hold, holm, dsr, spa |
| 1684 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=2) | -29.02/-0.66/-36.34 | 872.11 | 1245 | 0.0239 | 1.0 (195.6) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1685 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=3) | 25.97/0.55/-16.13 | 872.11 | 1228 | 0.024 | 0.999 (194.99) | 1.0 | 0.002 | 0.5005 | False | beats_buy_hold, holm, dsr, spa |
| 1686 | hibeta|sma_cross(fast=10,slow=100)+day_of_week(days=4) | 71.43/1.34/-14.42 | 872.11 | 1234 | 0.024 | 0.98302 (202.41) | 1.0 | 0.0462 | 0.5065 | False | beats_buy_hold, holm, dsr, spa |
| 1687 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=1) | 35.24/0.7/-21.59 | 872.11 | 1240 | 0.0238 | 0.997 (195.5) | 1.0 | 0.0033 | 0.5 | False | beats_buy_hold, holm, dsr, spa |
| 1688 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=2) | -27.43/-0.61/-37.07 | 872.11 | 1227 | 0.0238 | 1.0 (203.77) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1689 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=3) | 29.81/0.59/-16.43 | 872.11 | 1212 | 0.0239 | 1.0 (203.59) | 1.0 | 0.0024 | 0.489 | False | beats_buy_hold, holm, dsr, spa |
| 1690 | hibeta|sma_cross(fast=10,slow=150)+day_of_week(days=4) | 45.49/0.93/-14.13 | 872.11 | 1210 | 0.0239 | 0.996 (199.35) | 1.0 | 0.0094 | 0.5025 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 1690

## Engine prereg 20261024_031001_gen_2410240319_000 (gen_2410240319_000, sha256 8877a526da32): rows #1691-1694 RESERVED (4 variants). Counted in N.
N_cumulative: 1694

## Engine run 20261024_031001_gen_2410240319_000 (gen_2410240319_000): rows #1691-1694. 0/4 pass. PBO 0.045. Bar applied at N=1694. Report: engine/runs/20261024_031001_gen_2410240319_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1691 | crypto|sma_cross(fast=5,slow=100)+trend_sma(n=200) | 14.11/0.44/-37.52 | 428.6 | 1585 | 0.106 | 0.70629 (122.21) | 1.0 | 0.5015 | 0.915 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1692 | crypto|sma_cross(fast=5,slow=150)+trend_sma(n=200) | 0.56/0.19/-38.36 | 428.6 | 1478 | 0.1041 | 0.81219 (54.02) | 1.0 | 0.3821 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1693 | crypto|sma_cross(fast=20,slow=100)+trend_sma(n=200) | 7.34/0.31/-35.27 | 428.6 | 1320 | 0.1041 | 0.77023 (134.72) | 1.0 | 0.4404 | 0.9165 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1694 | crypto|sma_cross(fast=20,slow=150)+trend_sma(n=200) | 15.74/0.47/-34.13 | 428.6 | 1240 | 0.1026 | 0.70629 (73.99) | 1.0 | 0.5143 | 0.912 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1694

## Engine prereg 20261024_040939_gen_2410240408_000 (gen_2410240408_000, sha256 1e6739aec37e): rows #1695-1702 RESERVED (8 variants). Counted in N.
N_cumulative: 1702

## Engine run 20261024_040939_gen_2410240408_000 (gen_2410240408_000): rows #1695-1702. 0/8 pass. PBO 0.008. Bar applied at N=1702. Report: engine/runs/20261024_040939_gen_2410240408_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1695 | BROAD|drop_revert(drop=0.05,hold=3,n=1) | 0.09/0.03/-3.97 | 64.52 | 480 | 0.0302 | 1.0 (28.3) | 1.0 | 0.0649 | 0.4905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1696 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 10.7/0.65/-5.87 | 64.52 | 1450 | 0.0377 | 1.0 (27.38) | 1.0 | 0.3097 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1697 | BROAD|drop_revert(drop=0.05,hold=5,n=1) | 1.29/0.12/-4.22 | 64.52 | 448 | 0.0309 | 1.0 (28.65) | 1.0 | 0.0825 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1698 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 14.45/0.81/-6.15 | 64.52 | 1381 | 0.0381 | 0.998 (27.5) | 1.0 | 0.4271 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1699 | BROAD|drop_revert(drop=0.1,hold=3,n=1) | 0.59/0.42/-0.77 | 64.52 | 61 | 0.0187 | 1.0 (28.49) | 1.0 | 0.2079 | 0.497 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1700 | BROAD|drop_revert(drop=0.1,hold=3,n=5) | 3.98/0.35/-2.57 | 64.52 | 287 | 0.0275 | 1.0 (28.27) | 1.0 | 0.1346 | 0.485 | False | beats_buy_hold, holm, dsr, spa |
| 1701 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.32/0.19/-0.94 | 64.52 | 57 | 0.02 | 1.0 (29.15) | 1.0 | 0.1061 | 0.498 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1702 | BROAD|drop_revert(drop=0.1,hold=5,n=5) | 4.9/0.42/-2.63 | 64.52 | 281 | 0.0276 | 1.0 (28.73) | 1.0 | 0.1624 | 0.484 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 1702

## Engine prereg 20261024_040948_gen_2410240409_000 (gen_2410240409_000, sha256 c45d1d60f2e4): rows #1703-1710 RESERVED (8 variants). Counted in N.
N_cumulative: 1710

## Engine run 20261024_040948_gen_2410240409_000 (gen_2410240409_000): rows #1703-1710. 0/8 pass. PBO 0.316. Bar applied at N=1710. Report: engine/runs/20261024_040948_gen_2410240409_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1703 | ALTS|rsi_revert(entry=5,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 2.15/0.25/-5.19 | 193.2 | 64 | 0.0178 | 0.94406 (116.09) | 1.0 | 0.0398 | 0.897 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1704 | ALTS|rsi_revert(entry=5,exit=70,n=5)+vol_regime(max_atr_pct=0.06) | 0.41/0.35/-0.48 | 193.2 | 3 | 0.017 | 0.99101 (149.91) | 1.0 | 0.0301 | 0.899 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1705 | ALTS|rsi_revert(entry=5,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 5.31/0.47/-6.1 | 193.2 | 74 | 0.0173 | 0.89411 (54.23) | 1.0 | 0.06 | 0.898 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1706 | ALTS|rsi_revert(entry=5,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | -1.36/-0.39/-3.94 | 193.2 | 8 | 0.0169 | 0.98701 (43.01) | 1.0 | 0.0048 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1707 | ALTS|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 4.16/0.35/-5.84 | 193.2 | 119 | 0.0183 | 0.93007 (103.15) | 1.0 | 0.0476 | 0.8975 | False | beats_buy_hold, holm, dsr, spa |
| 1708 | ALTS|rsi_revert(entry=10,exit=70,n=5)+vol_regime(max_atr_pct=0.06) | 2.94/1.45/-0.48 | 193.2 | 13 | 0.0172 | 0.97502 (146.62) | 1.0 | 0.3229 | 0.8965 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1709 | ALTS|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 6.28/0.44/-7.94 | 193.2 | 128 | 0.0177 | 0.8961 (104.93) | 1.0 | 0.0551 | 0.8975 | False | beats_buy_hold, holm, dsr, spa |
| 1710 | ALTS|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 4.59/0.61/-8.14 | 193.2 | 25 | 0.017 | 0.94106 (118.75) | 1.0 | 0.094 | 0.892 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1710

## Engine prereg 20261024_040953_gen_2410240410_000 (gen_2410240410_000, sha256 ba25faf73843): rows #1711-1718 RESERVED (8 variants). Counted in N.
N_cumulative: 1718

## Engine run 20261024_040953_gen_2410240410_000 (gen_2410240410_000): rows #1711-1718. 0/8 pass. PBO 0.719. Bar applied at N=1718. Report: engine/runs/20261024_040953_gen_2410240410_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1711 | COUNTRIES|rsi_revert(entry=5,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 5.31/0.32/-8.62 | 64.42 | 377 | 0.0675 | 0.99401 (27.53) | 1.0 | 0.2926 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1712 | COUNTRIES|rsi_revert(entry=5,exit=70,n=3)+vol_regime(max_atr_pct=0.06) | 7.84/0.66/-4.32 | 64.42 | 96 | 0.0634 | 0.98601 (28.87) | 1.0 | 0.5305 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1713 | COUNTRIES|rsi_revert(entry=5,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 12.13/0.59/-8.62 | 64.42 | 347 | 0.0682 | 0.95604 (27.35) | 1.0 | 0.4798 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1714 | COUNTRIES|rsi_revert(entry=5,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 8.1/0.61/-4.51 | 64.42 | 95 | 0.063 | 0.98202 (29.12) | 1.0 | 0.488 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1715 | COUNTRIES|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 10.62/0.48/-10.49 | 64.42 | 648 | 0.0665 | 0.94406 (24.87) | 1.0 | 0.3983 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1716 | COUNTRIES|rsi_revert(entry=10,exit=70,n=3)+vol_regime(max_atr_pct=0.06) | 17.27/0.86/-8.62 | 64.42 | 243 | 0.0657 | 0.88112 (27.5) | 1.0 | 0.6745 | 0.971 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1717 | COUNTRIES|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 19.46/0.74/-11.09 | 64.42 | 574 | 0.0666 | 0.73127 (25.41) | 1.0 | 0.5798 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1718 | COUNTRIES|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 19.12/0.85/-8.62 | 64.42 | 222 | 0.067 | 0.80519 (27.31) | 1.0 | 0.6607 | 0.9725 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1718

## Engine prereg 20261024_040957_gen_2410240412_000 (gen_2410240412_000, sha256 410c897bfe7a): rows #1719-1726 RESERVED (8 variants). Counted in N.
N_cumulative: 1726

## Engine run 20261024_040957_gen_2410240412_000 (gen_2410240412_000): rows #1719-1726. 0/8 pass. PBO 0.625. Bar applied at N=1726. Report: engine/runs/20261024_040957_gen_2410240412_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1719 | BTC_ETH|drop_revert(drop=0.05,hold=3,n=1) | -12.42/-0.24/-30.86 | 56.21 | 150 | 0.0162 | 0.92507 (26.08) | 1.0 | 0.079 | 0.9145 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1720 | BTC_ETH|drop_revert(drop=0.05,hold=3,n=3) | 1.76/0.19/-19.93 | 56.21 | 186 | 0.0167 | 0.78422 (24.1) | 1.0 | 0.1771 | 0.851 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1721 | BTC_ETH|drop_revert(drop=0.05,hold=5,n=1) | -18.7/-0.31/-36.37 | 56.21 | 126 | 0.0167 | 0.95904 (26.61) | 1.0 | 0.0667 | 0.9305 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1722 | BTC_ETH|drop_revert(drop=0.05,hold=5,n=3) | 9.05/0.34/-25.03 | 56.21 | 150 | 0.0175 | 0.67033 (24.59) | 1.0 | 0.2311 | 0.8465 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1723 | BTC_ETH|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 56.21 | 6 | 0.0081 | 1.0 (36.28) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1724 | BTC_ETH|drop_revert(drop=0.15,hold=3,n=3) | 4.36/0.31/-6.5 | 56.21 | 26 | 0.0122 | 0.76424 (27.02) | 1.0 | 0.2121 | 0.84 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1725 | BTC_ETH|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 56.21 | 6 | 0.0081 | 1.0 (25.91) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1726 | BTC_ETH|drop_revert(drop=0.15,hold=5,n=3) | 0.53/0.1/-7.44 | 56.21 | 25 | 0.0124 | 0.77922 (27.74) | 1.0 | 0.1508 | 0.8555 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1726

## Engine prereg 20261024_041000_gen_2410240413_000 (gen_2410240413_000, sha256 85374cd34552): rows #1727-1730 RESERVED (4 variants). Counted in N.
N_cumulative: 1730

## Engine run 20261024_041000_gen_2410240413_000 (gen_2410240413_000): rows #1727-1730. 0/4 pass. PBO 0.619. Bar applied at N=1730. Report: engine/runs/20261024_041000_gen_2410240413_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1727 | CREDIT|donchian(entry_n=20,exit_n=10)+relvol(min_ratio=1.0) | -7.0/-1.09/-8.42 | 32.7 | 914 | 0.2288 | 1.0 (6.47) | 1.0 | 0.0004 | 0.5095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1728 | CREDIT|donchian(entry_n=20,exit_n=20)+relvol(min_ratio=1.0) | -7.22/-0.92/-9.12 | 32.7 | 1117 | 0.2261 | 1.0 (4.47) | 1.0 | 0.001 | 0.5145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1729 | CREDIT|donchian(entry_n=100,exit_n=10)+relvol(min_ratio=1.0) | -3.46/-0.69/-5.29 | 32.7 | 584 | 0.2689 | 1.0 (9.28) | 1.0 | 0.0046 | 0.512 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1730 | CREDIT|donchian(entry_n=100,exit_n=20)+relvol(min_ratio=1.0) | -3.14/-0.51/-5.48 | 32.7 | 731 | 0.2598 | 0.998 (7.48) | 1.0 | 0.0093 | 0.5155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1730

## Engine prereg 20261024_041002_gen_2410240414_000 (gen_2410240414_000, sha256 16b5b25728f2): rows #1731-1738 RESERVED (8 variants). Counted in N.
N_cumulative: 1738

## Engine run 20261024_041002_gen_2410240414_000 (gen_2410240414_000): rows #1731-1738. 0/8 pass. PBO 0.141. Bar applied at N=1738. Report: engine/runs/20261024_041002_gen_2410240414_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1731 | US_INDEX|drop_revert(drop=0.05,hold=3,n=3) | 15.13/0.74/-3.91 | 68.31 | 121 | 0.0421 | 0.94006 (30.0) | 1.0 | 0.4374 | 0.951 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1732 | US_INDEX|drop_revert(drop=0.05,hold=3,n=5) | 9.09/0.47/-5.07 | 68.31 | 163 | 0.0477 | 0.99101 (30.24) | 1.0 | 0.2396 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1733 | US_INDEX|drop_revert(drop=0.05,hold=5,n=3) | 16.12/0.77/-3.91 | 68.31 | 118 | 0.0425 | 0.9021 (30.34) | 1.0 | 0.4684 | 0.948 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1734 | US_INDEX|drop_revert(drop=0.05,hold=5,n=5) | 11.71/0.57/-5.65 | 68.31 | 159 | 0.048 | 0.98901 (30.52) | 1.0 | 0.3087 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1735 | US_INDEX|drop_revert(drop=0.1,hold=3,n=3) | 1.04/0.09/-4.45 | 68.31 | 16 | 0.0285 | 1.0 (30.82) | 1.0 | 0.1013 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1736 | US_INDEX|drop_revert(drop=0.1,hold=3,n=5) | 8.39/0.45/-3.91 | 68.31 | 23 | 0.031 | 0.98302 (31.1) | 1.0 | 0.2072 | 0.981 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1737 | US_INDEX|drop_revert(drop=0.1,hold=5,n=3) | 4.04/0.23/-4.45 | 68.31 | 14 | 0.0292 | 0.99101 (30.28) | 1.0 | 0.1417 | 0.49 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1738 | US_INDEX|drop_revert(drop=0.1,hold=5,n=5) | 6.45/0.36/-3.91 | 68.31 | 23 | 0.031 | 0.98901 (31.15) | 1.0 | 0.1669 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1738

## Engine prereg 20261024_041006_gen_2410240415_000 (gen_2410240415_000, sha256 b075505c7b55): rows #1739-1742 RESERVED (4 variants). Counted in N.
N_cumulative: 1742

## Engine run 20261024_041006_gen_2410240415_000 (gen_2410240415_000): rows #1739-1742. 0/4 pass. PBO 0.249. Bar applied at N=1742. Report: engine/runs/20261024_041006_gen_2410240415_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1739 | MEGA|supertrend(atr_n=7,mult=2)+vol_regime(max_atr_pct=0.06) | -0.7/0.05/-20.28 | 26.86 | 6944 | 0.1268 | 0.86813 (-9.28) | 1.0 | 0.2491 | 0.8815 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1740 | MEGA|supertrend(atr_n=7,mult=3)+vol_regime(max_atr_pct=0.06) | 5.85/0.32/-14.89 | 26.86 | 6332 | 0.1288 | 0.77522 (-7.53) | 1.0 | 0.3402 | 0.8585 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1741 | MEGA|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 1.98/0.16/-19.16 | 26.86 | 6990 | 0.1269 | 0.77922 (-9.11) | 1.0 | 0.3003 | 0.8575 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1742 | MEGA|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | -4.35/-0.08/-18.37 | 26.86 | 6323 | 0.1292 | 0.77822 (-7.22) | 1.0 | 0.1926 | 0.9285 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1742

## Engine prereg 20261024_041010_gen_2410240416_000 (gen_2410240416_000, sha256 427562a37e32): rows #1743-1746 RESERVED (4 variants). Counted in N.
N_cumulative: 1746

## Engine run 20261024_041010_gen_2410240416_000 (gen_2410240416_000): rows #1743-1746. 0/4 pass. PBO 0.605. Bar applied at N=1746. Report: engine/runs/20261024_041010_gen_2410240416_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1743 | crypto|donchian(entry_n=20,exit_n=10) | 217.84/0.83/-35.62 | 428.6 | 1641 | 0.1029 | 0.31469 (130.15) | 1.0 | 0.9623 | 0.5165 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1744 | crypto|donchian(entry_n=20,exit_n=20) | 204.93/0.83/-45.63 | 428.6 | 1263 | 0.1008 | 0.36663 (115.85) | 1.0 | 0.9568 | 0.508 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1745 | crypto|donchian(entry_n=55,exit_n=10) | 250.98/0.87/-24.68 | 428.6 | 959 | 0.1037 | 0.30969 (77.66) | 1.0 | 0.974 | 0.9495 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |
| 1746 | crypto|donchian(entry_n=55,exit_n=20) | 212.99/0.83/-38.82 | 428.6 | 771 | 0.1005 | 0.43556 (203.26) | 1.0 | 0.9601 | 0.9705 | False | beats_buy_hold, cost_stop, walk_forward, holm, spa, pbo |

N_cumulative: 1746

## Engine prereg 20261024_041015_gen_2410240417_000 (gen_2410240417_000, sha256 6d3cddbb3cde): rows #1747-1754 RESERVED (8 variants). Counted in N.
N_cumulative: 1754

## Engine run 20261024_041015_gen_2410240417_000 (gen_2410240417_000): rows #1747-1754. 0/8 pass. PBO 0.645. Bar applied at N=1754. Report: engine/runs/20261024_041015_gen_2410240417_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1747 | REAL|rsi_revert(entry=5,exit=60,n=3)+rsi_band(hi=60) | 12.35/1.06/-1.4 | 86.94 | 96 | 0.0463 | 0.96404 (36.94) | 1.0 | 0.5452 | 0.5175 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1748 | REAL|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 1.19/0.57/-0.92 | 86.94 | 9 | 0.041 | 0.98002 (38.75) | 1.0 | 0.2179 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1749 | REAL|rsi_revert(entry=5,exit=80,n=3)+rsi_band(hi=60) | 18.42/1.26/-2.68 | 86.94 | 91 | 0.0459 | 0.90509 (36.62) | 1.0 | 0.7114 | 0.513 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1750 | REAL|rsi_revert(entry=5,exit=80,n=5)+rsi_band(hi=60) | 4.04/0.69/-2.75 | 86.94 | 12 | 0.0455 | 0.96304 (39.02) | 1.0 | 0.2766 | 0.4995 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1751 | REAL|rsi_revert(entry=10,exit=60,n=3)+rsi_band(hi=60) | 23.16/1.34/-4.1 | 86.94 | 217 | 0.0493 | 0.84416 (35.8) | 1.0 | 0.7533 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1752 | REAL|rsi_revert(entry=10,exit=60,n=5)+rsi_band(hi=60) | 7.31/1.21/-1.39 | 86.94 | 52 | 0.0446 | 0.97802 (37.13) | 1.0 | 0.6484 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1753 | REAL|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=60) | 30.98/1.36/-4.48 | 86.94 | 184 | 0.049 | 0.64635 (35.97) | 1.0 | 0.743 | 0.949 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1754 | REAL|rsi_revert(entry=10,exit=80,n=5)+rsi_band(hi=60) | 9.32/0.9/-2.75 | 86.94 | 55 | 0.0472 | 0.98202 (37.76) | 1.0 | 0.4137 | 0.5015 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1754

## Engine prereg 20261024_041019_gen_2410240418_000 (gen_2410240418_000, sha256 627c726be703): rows #1755-1762 RESERVED (8 variants). Counted in N.
N_cumulative: 1762

## Engine run 20261024_041019_gen_2410240418_000 (gen_2410240418_000): rows #1755-1762. 0/8 pass. PBO 0.403. Bar applied at N=1762. Report: engine/runs/20261024_041019_gen_2410240418_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1755 | SECTORS|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.2) | 1.27/0.2/-2.25 | 56.34 | 262 | 0.0609 | 1.0 (25.42) | 1.0 | 0.1148 | 0.5005 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1756 | SECTORS|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.2) | 1.67/0.75/-0.61 | 56.34 | 60 | 0.0515 | 1.0 (25.69) | 1.0 | 0.4185 | 0.4965 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1757 | SECTORS|rsi_revert(entry=5,exit=80,n=3)+relvol(min_ratio=1.2) | 2.08/0.32/-1.9 | 56.34 | 337 | 0.0593 | 1.0 (24.41) | 1.0 | 0.1539 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1758 | SECTORS|rsi_revert(entry=5,exit=80,n=5)+relvol(min_ratio=1.2) | 2.19/0.93/-0.61 | 56.34 | 93 | 0.0552 | 1.0 (24.55) | 1.0 | 0.5495 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1759 | SECTORS|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.2) | 5.85/0.38/-2.99 | 56.34 | 675 | 0.0651 | 1.0 (23.98) | 1.0 | 0.1637 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1760 | SECTORS|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.2) | 1.55/0.29/-1.98 | 56.34 | 226 | 0.0522 | 1.0 (25.18) | 1.0 | 0.1461 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1761 | SECTORS|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.2) | 5.34/0.34/-4.18 | 56.34 | 841 | 0.0639 | 0.999 (23.39) | 1.0 | 0.1535 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1762 | SECTORS|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.2) | 2.65/0.38/-2.03 | 56.34 | 372 | 0.0557 | 0.999 (25.17) | 1.0 | 0.172 | 0.5005 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1762

## Engine prereg 20261024_041022_gen_2410240420_000 (gen_2410240420_000, sha256 879d40f8a307): rows #1763-1766 RESERVED (4 variants). Counted in N.
N_cumulative: 1766

## Engine run 20261024_041022_gen_2410240420_000 (gen_2410240420_000): rows #1763-1766. 0/4 pass. PBO 0.846. Bar applied at N=1766. Report: engine/runs/20261024_041022_gen_2410240420_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1763 | sector_etf|sma_cross(fast=5,slow=50)+vol_regime(max_atr_pct=0.04) | 20.82/0.71/-10.65 | 63.33 | 292 | 0.0609 | 0.73027 (27.18) | 1.0 | 0.7252 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1764 | sector_etf|sma_cross(fast=5,slow=100)+vol_regime(max_atr_pct=0.04) | 15.45/0.53/-11.84 | 63.33 | 195 | 0.0587 | 0.91808 (27.62) | 1.0 | 0.6125 | 0.5145 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1765 | sector_etf|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 63.33 | 0 | inf | 1.0 (29.82) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1766 | sector_etf|sma_cross(fast=50,slow=100)+vol_regime(max_atr_pct=0.04) | 22.22/0.71/-9.58 | 63.33 | 90 | 0.0712 | 0.75425 (28.29) | 1.0 | 0.7252 | 0.519 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1766

## Engine prereg 20261024_041026_gen_2410240421_000 (gen_2410240421_000, sha256 501cfdf952de): rows #1767-1770 RESERVED (4 variants). Counted in N.
N_cumulative: 1770

## Engine run 20261024_041026_gen_2410240421_000 (gen_2410240421_000): rows #1767-1770. 0/4 pass. PBO 0.819. Bar applied at N=1770. Report: engine/runs/20261024_041026_gen_2410240421_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1767 | defensive|sma_cross(fast=10,slow=50)+trend_sma(n=100) | 51.13/1.68/-6.25 | 104.36 | 178 | 0.0692 | 0.26274 (40.16) | 1.0 | 0.9284 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1768 | defensive|sma_cross(fast=10,slow=200)+trend_sma(n=100) | 56.23/1.71/-7.99 | 104.36 | 180 | 0.0692 | 0.23177 (40.87) | 1.0 | 0.9372 | 0.494 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1769 | defensive|sma_cross(fast=20,slow=50)+trend_sma(n=100) | 36.14/1.28/-7.99 | 104.36 | 165 | 0.0671 | 0.68332 (41.19) | 1.0 | 0.7829 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1770 | defensive|sma_cross(fast=20,slow=200)+trend_sma(n=100) | 59.89/1.83/-7.99 | 104.36 | 174 | 0.068 | 0.18581 (42.15) | 1.0 | 0.9583 | 0.9725 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

N_cumulative: 1770

## Engine prereg 20261024_041028_gen_2410240422_000 (gen_2410240422_000, sha256 68036752d411): rows #1771-1774 RESERVED (4 variants). Counted in N.
N_cumulative: 1774

## Engine run 20261024_041028_gen_2410240422_000 (gen_2410240422_000): rows #1771-1774. 0/4 pass. PBO 0.474. Bar applied at N=1774. Report: engine/runs/20261024_041028_gen_2410240422_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1771 | semis|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 157.01/1.6/-20.63 | 440.15 | 258 | 0.033 | 0.2967 (136.8) | 1.0 | 0.9881 | 0.502 | False | beats_buy_hold, cost_stop, holm, spa |
| 1772 | semis|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 216.03/1.7/-20.41 | 440.15 | 199 | 0.0321 | 0.03796 (136.87) | 1.0 | 0.9907 | 0.5145 | False | beats_buy_hold, cost_stop, holm, spa |
| 1773 | semis|donchian(entry_n=55,exit_n=10)+rsi_band(hi=80) | 101.57/1.45/-16.8 | 440.15 | 202 | 0.0352 | 0.79221 (133.95) | 1.0 | 0.9747 | 0.5055 | False | beats_buy_hold, cost_stop, holm, spa |
| 1774 | semis|donchian(entry_n=55,exit_n=20)+rsi_band(hi=80) | 136.58/1.56/-18.81 | 440.15 | 161 | 0.0344 | 0.48951 (138.35) | 1.0 | 0.9827 | 0.521 | False | beats_buy_hold, cost_stop, holm, spa |

N_cumulative: 1774

## Engine prereg 20261024_041031_gen_2410240423_000 (gen_2410240423_000, sha256 b19998ead7fc): rows #1775-1778 RESERVED (4 variants). Counted in N.
N_cumulative: 1778

## Engine run 20261024_041031_gen_2410240423_000 (gen_2410240423_000): rows #1775-1778. 0/4 pass. PBO 0.5. Bar applied at N=1778. Report: engine/runs/20261024_041031_gen_2410240423_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1775 | BONDS_INTL|sma_cross(fast=5,slow=50) | 14.83/0.64/-9.35 | 40.38 | 207 | 0.0874 | 0.64336 (17.56) | 1.0 | 0.5669 | 0.9745 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1776 | BONDS_INTL|sma_cross(fast=5,slow=200) | 5.07/0.25/-10.73 | 40.38 | 88 | 0.091 | 0.97602 (17.34) | 1.0 | 0.3093 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1777 | BONDS_INTL|sma_cross(fast=20,slow=50) | 9.61/0.43/-9.8 | 40.38 | 125 | 0.0888 | 0.87512 (17.65) | 1.0 | 0.4259 | 0.4865 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1778 | BONDS_INTL|sma_cross(fast=20,slow=200) | 9.97/0.43/-11.19 | 40.38 | 52 | 0.0955 | 0.90809 (18.52) | 1.0 | 0.426 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1778

## Engine prereg 20261024_041034_gen_2410240424_000 (gen_2410240424_000, sha256 44f50248c749): rows #1779-1786 RESERVED (8 variants). Counted in N.
N_cumulative: 1786

## Engine run 20261024_041034_gen_2410240424_000 (gen_2410240424_000): rows #1779-1786. 0/8 pass. PBO 0.413. Bar applied at N=1786. Report: engine/runs/20261024_041034_gen_2410240424_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1779 | MEGA|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=50) | 8.51/0.88/-4.26 | 287.89 | 330 | 0.0281 | 1.0 (98.47) | 1.0 | 0.1573 | 0.4835 | False | beats_buy_hold, holm, dsr, spa |
| 1780 | MEGA|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=50) | 2.46/0.26/-7.19 | 287.89 | 378 | 0.0308 | 1.0 (96.66) | 1.0 | 0.0178 | 0.4855 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1781 | MEGA|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=50) | 9.18/0.79/-5.39 | 287.89 | 398 | 0.0287 | 1.0 (98.67) | 1.0 | 0.1188 | 0.4885 | False | beats_buy_hold, holm, dsr, spa |
| 1782 | MEGA|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=50) | -0.78/-0.04/-8.9 | 287.89 | 459 | 0.031 | 1.0 (96.7) | 1.0 | 0.0042 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1783 | MEGA|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=50) | 4.5/1.31/-0.48 | 287.89 | 39 | 0.0195 | 1.0 (103.3) | 1.0 | 0.3357 | 0.4905 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1784 | MEGA|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 2.5/0.66/-1.31 | 287.89 | 56 | 0.0218 | 1.0 (101.39) | 1.0 | 0.0674 | 0.489 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1785 | MEGA|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=50) | 2.78/0.62/-1.79 | 287.89 | 49 | 0.0192 | 1.0 (99.04) | 1.0 | 0.0651 | 0.4905 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1786 | MEGA|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=50) | 0.79/0.16/-3.44 | 287.89 | 74 | 0.0217 | 1.0 (101.85) | 1.0 | 0.0119 | 0.488 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1786

## Engine prereg 20261024_041038_gen_2410240426_000 (gen_2410240426_000, sha256 2091393362f2): rows #1787-1790 RESERVED (4 variants). Counted in N.
N_cumulative: 1790

## Engine run 20261024_041038_gen_2410240426_000 (gen_2410240426_000): rows #1787-1790. 0/4 pass. PBO 1.0. Bar applied at N=1790. Report: engine/runs/20261024_041038_gen_2410240426_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1787 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1788 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1789 | SOL|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (0.0) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1790 | SOL|supertrend(atr_n=14,mult=4)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 41.29 | 0 | inf | 1.0 (41.22) | 1.0 | 0.0 | 0.8365 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1790

## Engine prereg 20261024_051216_gen_2410240510_000 (gen_2410240510_000, sha256 4000880e79b0): rows #1791-1798 RESERVED (8 variants). Counted in N.
N_cumulative: 1798

## Engine run 20261024_051216_gen_2410240510_000 (gen_2410240510_000): rows #1791-1798. 0/8 pass. PBO 0.35. Bar applied at N=1798. Report: engine/runs/20261024_051216_gen_2410240510_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1791 | BROAD|rsi_revert(entry=5,exit=60,n=2) | 14.89/0.93/-3.42 | 78.13 | 293 | 0.0793 | 0.96903 (31.4) | 1.0 | 0.8925 | 0.512 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1792 | BROAD|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 78.13 | 5 | 0.0439 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1793 | BROAD|rsi_revert(entry=5,exit=80,n=2) | 20.18/1.02/-5.65 | 78.13 | 272 | 0.0801 | 0.9011 (31.45) | 1.0 | 0.8981 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1794 | BROAD|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 78.13 | 4 | 0.0491 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1795 | BROAD|rsi_revert(entry=20,exit=60,n=2) | 22.96/0.97/-7.78 | 78.13 | 898 | 0.0798 | 0.63636 (26.07) | 1.0 | 0.8588 | 0.5135 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1796 | BROAD|rsi_revert(entry=20,exit=60,n=5) | 19.95/1.1/-5.46 | 78.13 | 183 | 0.077 | 0.93506 (33.15) | 1.0 | 0.9214 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1797 | BROAD|rsi_revert(entry=20,exit=80,n=2) | 38.14/1.26/-9.33 | 78.13 | 714 | 0.0808 | 0.13387 (28.85) | 1.0 | 0.9404 | 0.5185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1798 | BROAD|rsi_revert(entry=20,exit=80,n=5) | 31.04/1.1/-11.15 | 78.13 | 126 | 0.0803 | 0.56044 (33.0) | 1.0 | 0.8905 | 0.5265 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1798

## Engine prereg 20261024_051222_gen_2410240511_000 (gen_2410240511_000, sha256 62edf9bc36e1): rows #1799-1802 RESERVED (4 variants). Counted in N.
N_cumulative: 1802

## Engine run 20261024_051222_gen_2410240511_000 (gen_2410240511_000): rows #1799-1802. 0/4 pass. PBO 0.413. Bar applied at N=1802. Report: engine/runs/20261024_051222_gen_2410240511_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1799 | crypto|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.2) | -4.64/-0.07/-17.98 | 434.62 | 357 | 0.02 | 0.92108 (83.93) | 1.0 | 0.3768 | 0.914 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1800 | crypto|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.2) | -5.67/-0.1/-19.45 | 434.62 | 397 | 0.0192 | 0.92108 (205.32) | 1.0 | 0.3628 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1801 | crypto|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.2) | -6.09/-0.13/-17.98 | 434.62 | 368 | 0.02 | 0.94206 (107.41) | 1.0 | 0.3512 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1802 | crypto|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -8.19/-0.2/-21.64 | 434.62 | 393 | 0.0194 | 0.94206 (166.64) | 1.0 | 0.3192 | 0.913 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

N_cumulative: 1802

## Engine prereg 20261024_051227_gen_2410240512_000 (gen_2410240512_000, sha256 bed159dd800b): rows #1803-1806 RESERVED (4 variants). Counted in N.
N_cumulative: 1806

## Engine run 20261024_051227_gen_2410240512_000 (gen_2410240512_000): rows #1803-1806. 0/4 pass. PBO 0.24. Bar applied at N=1806. Report: engine/runs/20261024_051227_gen_2410240512_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1803 | BROAD|sma_cross(fast=5,slow=100) | 200.12/1.84/-19.07 | 386.25 | 114 | 0.0349 | 0.05894 (127.56) | 1.0 | 0.9977 | 0.5205 | False | beats_buy_hold, cost_stop, holm, spa |
| 1804 | BROAD|sma_cross(fast=5,slow=150) | 192.42/1.77/-16.32 | 386.25 | 90 | 0.0321 | 0.11988 (121.74) | 1.0 | 0.9961 | 0.5235 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |
| 1805 | BROAD|sma_cross(fast=10,slow=100) | 217.23/1.92/-16.37 | 386.25 | 81 | 0.0348 | 0.02198 (124.64) | 1.0 | 0.9984 | 0.531 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |
| 1806 | BROAD|sma_cross(fast=10,slow=150) | 188.06/1.76/-16.93 | 386.25 | 68 | 0.0325 | 0.18082 (125.06) | 1.0 | 0.9957 | 0.533 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |

N_cumulative: 1806

## Engine prereg 20261024_051230_gen_2410240513_000 (gen_2410240513_000, sha256 011bf831cc28): rows #1807-1814 RESERVED (8 variants). Counted in N.
N_cumulative: 1814

## Engine run 20261024_051230_gen_2410240513_000 (gen_2410240513_000): rows #1807-1814. 0/8 pass. PBO 0.233. Bar applied at N=1814. Report: engine/runs/20261024_051230_gen_2410240513_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1807 | BROAD|drop_revert(drop=0.05,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 2 | 0.0297 | 1.0 (11.06) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1808 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 2 | 0.041 | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1809 | BROAD|drop_revert(drop=0.05,hold=10,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 1 | 0.038 | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1810 | BROAD|drop_revert(drop=0.05,hold=10,n=5)+trend_sma(n=100) | 0.13/0.44/-0.04 | 23.43 | 3 | 0.0621 | 0.99001 (11.34) | 1.0 | nan | 0.956 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1811 | BROAD|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.49) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1812 | BROAD|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1813 | BROAD|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1814 | BROAD|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.16) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1814

## Engine prereg 20261024_051233_gen_2410240514_000 (gen_2410240514_000, sha256 886b982d3769): rows #1815-1818 RESERVED (4 variants). Counted in N.
N_cumulative: 1818

## Engine run 20261024_051233_gen_2410240514_000 (gen_2410240514_000): rows #1815-1818. 0/4 pass. PBO 0.541. Bar applied at N=1818. Report: engine/runs/20261024_051233_gen_2410240514_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1815 | BROAD|donchian(entry_n=55,exit_n=10) | -5.77/-0.24/-11.41 | 62.38 | 167 | 0.0818 | 1.0 (25.92) | 1.0 | 0.1581 | 0.5085 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1816 | BROAD|donchian(entry_n=55,exit_n=20) | -3.66/-0.09/-16.52 | 62.38 | 106 | 0.0768 | 1.0 (27.33) | 1.0 | 0.2305 | 0.521 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1817 | BROAD|donchian(entry_n=100,exit_n=10) | -5.42/-0.28/-10.7 | 62.38 | 137 | 0.086 | 1.0 (26.67) | 1.0 | 0.1431 | 0.4955 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1818 | BROAD|donchian(entry_n=100,exit_n=20) | -7.65/-0.32/-18.22 | 62.38 | 88 | 0.0795 | 1.0 (27.24) | 1.0 | 0.1284 | 0.5095 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1818

## Engine prereg 20261024_051235_gen_2410240515_000 (gen_2410240515_000, sha256 30ead876d2f6): rows #1819-1822 RESERVED (4 variants). Counted in N.
N_cumulative: 1822

## Engine run 20261024_051235_gen_2410240515_000 (gen_2410240515_000): rows #1819-1822. 0/4 pass. PBO 0.381. Bar applied at N=1822. Report: engine/runs/20261024_051235_gen_2410240515_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1819 | BROAD|sma_cross(fast=20,slow=100)+relvol(min_ratio=1.2) | -7.84/-0.55/-10.8 | 57.67 | 1091 | 0.0751 | 0.999 (18.12) | 1.0 | 0.0198 | 0.505 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1820 | BROAD|sma_cross(fast=20,slow=200)+relvol(min_ratio=1.2) | -5.78/-0.35/-10.71 | 57.67 | 1060 | 0.0743 | 0.999 (17.75) | 1.0 | 0.045 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1821 | BROAD|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.2) | -4.35/-0.28/-8.41 | 57.67 | 1067 | 0.0745 | 0.999 (18.67) | 1.0 | 0.0573 | 0.4975 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1822 | BROAD|sma_cross(fast=50,slow=200)+relvol(min_ratio=1.2) | -2.45/-0.11/-9.34 | 57.67 | 1039 | 0.0734 | 0.99201 (18.68) | 1.0 | 0.1035 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1822

## Engine prereg 20261024_051238_gen_2410240517_000 (gen_2410240517_000, sha256 55206d85fb38): rows #1823-1826 RESERVED (4 variants). Counted in N.
N_cumulative: 1826

## Engine run 20261024_051238_gen_2410240517_000 (gen_2410240517_000): rows #1823-1826. 0/4 pass. PBO 0.655. Bar applied at N=1826. Report: engine/runs/20261024_051238_gen_2410240517_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1823 | BROAD|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.2) | -9.11/-0.44/-15.19 | 5.92 | 855 | 0.0575 | 0.67932 (-2.1) | 1.0 | 0.0407 | 0.8005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1824 | BROAD|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -4.52/-0.2/-13.45 | 5.92 | 819 | 0.0573 | 0.55744 (-3.03) | 1.0 | 0.0898 | 0.7355 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1825 | BROAD|supertrend(atr_n=14,mult=3)+relvol(min_ratio=1.2) | -9.61/-0.48/-15.42 | 5.92 | 849 | 0.0576 | 0.67133 (-2.53) | 1.0 | 0.0343 | 0.8095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1826 | BROAD|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.2) | -3.18/-0.14/-12.76 | 5.92 | 802 | 0.0571 | 0.56643 (-1.58) | 1.0 | 0.1105 | 0.7235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1826

## Engine prereg 20261024_051241_gen_2410240518_000 (gen_2410240518_000, sha256 de4f81afb6b2): rows #1827-1834 RESERVED (8 variants). Counted in N.
N_cumulative: 1834

## Engine run 20261024_051241_gen_2410240518_000 (gen_2410240518_000): rows #1827-1834. 0/8 pass. PBO 1.0. Bar applied at N=1834. Report: engine/runs/20261024_051241_gen_2410240518_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1827 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0175 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1828 | BROAD|drop_revert(drop=0.1,hold=5,n=3) | 3.23/0.27/-2.57 | 78.13 | 10 | 0.0287 | 0.996 (33.6) | 1.0 | 0.6384 | 0.503 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1829 | BROAD|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0175 | 1.0 (32.58) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1830 | BROAD|drop_revert(drop=0.1,hold=10,n=3) | 3.99/0.31/-3.42 | 78.13 | 10 | 0.0287 | 0.995 (32.5) | 1.0 | 0.6638 | 0.504 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1831 | BROAD|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 78.13 | 0 | inf | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1832 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1833 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 78.13 | 0 | inf | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1834 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1834

## Engine prereg 20261024_051244_gen_2410240519_000 (gen_2410240519_000, sha256 08304097483d): rows #1835-1842 RESERVED (8 variants). Counted in N.
N_cumulative: 1842

## Engine run 20261024_051244_gen_2410240519_000 (gen_2410240519_000): rows #1835-1842. 0/8 pass. PBO 0.448. Bar applied at N=1842. Report: engine/runs/20261024_051244_gen_2410240519_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1835 | crypto|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=80) | 2.0/0.18/-24.25 | 434.62 | 251 | 0.0126 | 0.89411 (122.65) | 1.0 | 0.0736 | 0.904 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1836 | crypto|drop_revert(drop=0.05,hold=3,n=5)+rsi_band(hi=80) | -8.1/0.03/-34.55 | 434.62 | 265 | 0.0154 | 0.96104 (101.29) | 1.0 | 0.0531 | 0.9175 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1837 | crypto|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=80) | -24.09/-0.28/-39.44 | 434.62 | 130 | 0.0162 | 0.997 (108.45) | 1.0 | 0.0238 | 0.9225 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1838 | crypto|drop_revert(drop=0.05,hold=10,n=5)+rsi_band(hi=80) | 32.98/0.65/-40.72 | 434.62 | 135 | 0.0172 | 0.68731 (71.98) | 1.0 | 0.1886 | 0.8855 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1839 | crypto|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=80) | 11.68/0.77/-5.29 | 434.62 | 61 | 0.01 | 0.84116 (69.66) | 1.0 | 0.1797 | 0.8985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1840 | crypto|drop_revert(drop=0.1,hold=3,n=5)+rsi_band(hi=80) | 17.61/0.53/-22.52 | 434.62 | 152 | 0.0118 | 0.81319 (187.41) | 1.0 | 0.1511 | 0.8935 | False | beats_buy_hold, holm, dsr, spa |
| 1841 | crypto|drop_revert(drop=0.1,hold=10,n=1)+rsi_band(hi=80) | -3.05/-0.0/-21.5 | 434.62 | 50 | 0.0106 | 0.94605 (196.53) | 1.0 | 0.0488 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1842 | crypto|drop_revert(drop=0.1,hold=10,n=5)+rsi_band(hi=80) | 37.03/0.79/-29.19 | 434.62 | 113 | 0.0131 | 0.66334 (93.38) | 1.0 | 0.2375 | 0.874 | False | beats_buy_hold, holm, dsr, spa |

N_cumulative: 1842

## Engine prereg 20261024_051247_gen_2410240520_000 (gen_2410240520_000, sha256 b90d1137610b): rows #1843-1850 RESERVED (8 variants). Counted in N.
N_cumulative: 1850

## Engine run 20261024_051247_gen_2410240520_000 (gen_2410240520_000): rows #1843-1850. 0/8 pass. PBO 0.093. Bar applied at N=1850. Report: engine/runs/20261024_051247_gen_2410240520_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1843 | BROAD|rsi_revert(entry=5,exit=60,n=2) | 33.37/0.87/-10.83 | 386.25 | 286 | 0.0319 | 1.0 (121.49) | 1.0 | 0.6827 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1844 | BROAD|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 386.25 | 2 | 0.0349 | 1.0 (143.13) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1845 | BROAD|rsi_revert(entry=5,exit=70,n=2) | 37.09/0.91/-11.36 | 386.25 | 276 | 0.0324 | 0.997 (121.51) | 1.0 | 0.7048 | 0.504 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1846 | BROAD|rsi_revert(entry=5,exit=70,n=5) | 0.0/0.0/0.0 | 386.25 | 2 | 0.0349 | 1.0 (113.02) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1847 | BROAD|rsi_revert(entry=10,exit=60,n=2) | 67.27/1.25/-16.9 | 386.25 | 551 | 0.0323 | 0.95005 (117.93) | 1.0 | 0.8876 | 0.5165 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1848 | BROAD|rsi_revert(entry=10,exit=60,n=5) | 13.98/0.83/-2.96 | 386.25 | 28 | 0.0341 | 0.98801 (130.04) | 1.0 | 0.6456 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1849 | BROAD|rsi_revert(entry=10,exit=70,n=2) | 70.89/1.22/-18.16 | 386.25 | 522 | 0.0326 | 0.93906 (120.91) | 1.0 | 0.8634 | 0.513 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1850 | BROAD|rsi_revert(entry=10,exit=70,n=5) | 14.95/0.82/-5.51 | 386.25 | 27 | 0.0341 | 0.98801 (127.27) | 1.0 | 0.619 | 0.505 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 1850

## Engine prereg 20261024_051250_gen_2410240521_000 (gen_2410240521_000, sha256 3cbec9bb290e): rows #1851-1854 RESERVED (4 variants). Counted in N.
N_cumulative: 1854

## Engine run 20261024_051250_gen_2410240521_000 (gen_2410240521_000): rows #1851-1854. 0/4 pass. PBO 0.609. Bar applied at N=1854. Report: engine/runs/20261024_051250_gen_2410240521_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1851 | BROAD|donchian(entry_n=55,exit_n=10) | -1.18/-0.11/-4.45 | 23.43 | 145 | 0.2021 | 0.998 (10.26) | 1.0 | 0.0514 | 0.49 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1852 | BROAD|donchian(entry_n=55,exit_n=20) | 3.03/0.29/-5.46 | 23.43 | 102 | 0.187 | 0.97802 (10.37) | 1.0 | 0.17 | 0.9565 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1853 | BROAD|donchian(entry_n=100,exit_n=10) | 1.43/0.24/-3.48 | 23.43 | 117 | 0.2232 | 0.999 (10.62) | 1.0 | 0.1492 | 0.9665 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1854 | BROAD|donchian(entry_n=100,exit_n=20) | 3.6/0.47/-3.55 | 23.43 | 85 | 0.2214 | 0.98901 (10.8) | 1.0 | 0.2645 | 0.9625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1854

## Engine prereg 20261024_051253_gen_2410240522_000 (gen_2410240522_000, sha256 85a0e9f98ac6): rows #1855-1862 RESERVED (8 variants). Counted in N.
N_cumulative: 1862

## Engine run 20261024_051253_gen_2410240522_000 (gen_2410240522_000): rows #1855-1862. 0/8 pass. PBO 0.151. Bar applied at N=1862. Report: engine/runs/20261024_051253_gen_2410240522_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1855 | BROAD|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 62.38 | 5 | 0.0228 | 1.0 (28.31) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1856 | BROAD|drop_revert(drop=0.1,hold=5,n=3) | 6.45/0.43/-3.61 | 62.38 | 20 | 0.029 | 0.99301 (28.52) | 1.0 | 0.2823 | 0.494 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1857 | BROAD|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 62.38 | 5 | 0.0228 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1858 | BROAD|drop_revert(drop=0.1,hold=10,n=3) | 12.17/0.74/-3.69 | 62.38 | 19 | 0.0291 | 0.95105 (28.22) | 1.0 | 0.521 | 0.976 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1859 | BROAD|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 62.38 | 2 | 0.0151 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1860 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.81/0.23/-1.14 | 62.38 | 4 | 0.0212 | 0.998 (28.54) | 1.0 | 0.1962 | 0.4945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1861 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 62.38 | 2 | 0.0151 | 1.0 (28.74) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1862 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 1.61/0.43/-1.14 | 62.38 | 4 | 0.0212 | 0.98901 (28.2) | 1.0 | 0.3034 | 0.494 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1862

## Engine prereg 20261024_051256_gen_2410240523_000 (gen_2410240523_000, sha256 72cdedd8cf39): rows #1863-1870 RESERVED (8 variants). Counted in N.
N_cumulative: 1870

## Engine run 20261024_051256_gen_2410240523_000 (gen_2410240523_000): rows #1863-1870. 0/8 pass. PBO 0.017. Bar applied at N=1870. Report: engine/runs/20261024_051256_gen_2410240523_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1863 | BROAD|drop_revert(drop=0.05,hold=5,n=3) | 6.13/0.32/-5.05 | 57.67 | 146 | 0.0403 | 0.98701 (26.24) | 1.0 | 0.0942 | 0.491 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1864 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 8.31/0.4/-7.79 | 57.67 | 187 | 0.042 | 0.96204 (25.29) | 1.0 | 0.1216 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1865 | BROAD|drop_revert(drop=0.05,hold=10,n=3) | 20.92/0.86/-5.39 | 57.67 | 116 | 0.042 | 0.65335 (25.08) | 1.0 | 0.3734 | 0.9275 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1866 | BROAD|drop_revert(drop=0.05,hold=10,n=5) | 18.09/0.71/-6.08 | 57.67 | 143 | 0.0446 | 0.77622 (25.64) | 1.0 | 0.2783 | 0.9655 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1867 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.82/0.22/-1.31 | 57.67 | 6 | 0.0211 | 0.96304 (27.2) | 1.0 | 0.0815 | 0.4895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1868 | BROAD|drop_revert(drop=0.15,hold=5,n=5) | -0.19/-0.04/-1.31 | 57.67 | 9 | 0.0228 | 0.98202 (27.36) | 1.0 | 0.0348 | 0.491 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1869 | BROAD|drop_revert(drop=0.15,hold=10,n=3) | 1.59/0.39/-1.31 | 57.67 | 5 | 0.0228 | 0.96204 (26.98) | 1.0 | 0.1355 | 0.488 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1870 | BROAD|drop_revert(drop=0.15,hold=10,n=5) | 0.44/0.11/-1.31 | 57.67 | 7 | 0.0232 | 0.98102 (26.96) | 1.0 | 0.059 | 0.4895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1870

## Engine prereg 20261024_051259_gen_2410240524_000 (gen_2410240524_000, sha256 5a9423c89a4c): rows #1871-1874 RESERVED (4 variants). Counted in N.
N_cumulative: 1874

## Engine run 20261024_051259_gen_2410240524_000 (gen_2410240524_000): rows #1871-1874. 0/4 pass. PBO 0.243. Bar applied at N=1874. Report: engine/runs/20261024_051259_gen_2410240524_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1871 | crypto|donchian(entry_n=55,exit_n=10) | 38.79/1.02/-15.0 | 56.21 | 28 | 0.0218 | 0.42757 (31.83) | 1.0 | 0.4587 | 0.7445 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1872 | crypto|donchian(entry_n=55,exit_n=20) | 45.08/1.08/-14.84 | 56.21 | 24 | 0.0218 | 0.31169 (27.15) | 1.0 | 0.4873 | 0.7205 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1873 | crypto|donchian(entry_n=100,exit_n=10) | 13.94/0.52/-18.64 | 56.21 | 20 | 0.0224 | 0.63037 (25.4) | 1.0 | 0.2379 | 0.8355 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1874 | crypto|donchian(entry_n=100,exit_n=20) | 12.91/0.47/-23.93 | 56.21 | 18 | 0.0224 | 0.63736 (26.34) | 1.0 | 0.2206 | 0.8415 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1874

## Engine prereg 20261024_051301_gen_2410240525_000 (gen_2410240525_000, sha256 e98c14cafff6): rows #1875-1878 RESERVED (4 variants). Counted in N.
N_cumulative: 1878

## Engine run 20261024_051301_gen_2410240525_000 (gen_2410240525_000): rows #1875-1878. 0/4 pass. PBO 0.257. Bar applied at N=1878. Report: engine/runs/20261024_051301_gen_2410240525_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1875 | BROAD|donchian(entry_n=20,exit_n=10) | -23.59/-0.82/-26.98 | 5.92 | 201 | 0.0539 | 0.98002 (1.64) | 1.0 | 0.0 | 0.9515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1876 | BROAD|donchian(entry_n=20,exit_n=20) | -20.98/-0.56/-30.95 | 5.92 | 148 | 0.0529 | 0.98102 (2.44) | 1.0 | 0.0 | 0.9535 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1877 | BROAD|donchian(entry_n=100,exit_n=10) | 0.2/0.04/-11.16 | 5.92 | 80 | 0.0602 | 0.58342 (2.68) | 1.0 | 0.0006 | 0.6325 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1878 | BROAD|donchian(entry_n=100,exit_n=20) | 9.41/0.43/-6.67 | 5.92 | 60 | 0.0581 | 0.3996 (3.13) | 1.0 | 0.005 | 0.505 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1878

## Engine prereg 20261024_051304_gen_2410240526_000 (gen_2410240526_000, sha256 557905cef14d): rows #1879-1886 RESERVED (8 variants). Counted in N.
N_cumulative: 1886

## Engine run 20261024_051304_gen_2410240526_000 (gen_2410240526_000): rows #1879-1886. 0/8 pass. PBO 0.463. Bar applied at N=1886. Report: engine/runs/20261024_051304_gen_2410240526_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1879 | BROAD|drop_revert(drop=0.05,hold=3,n=3) | 11.27/0.79/-2.08 | 78.13 | 88 | 0.0408 | 0.96603 (32.86) | 1.0 | 0.7958 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1880 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 7.47/0.52/-4.63 | 78.13 | 125 | 0.0483 | 0.996 (34.29) | 1.0 | 0.5368 | 0.508 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1881 | BROAD|drop_revert(drop=0.05,hold=5,n=3) | 12.27/0.83/-2.08 | 78.13 | 85 | 0.041 | 0.97602 (33.79) | 1.0 | 0.825 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1882 | BROAD|drop_revert(drop=0.05,hold=5,n=5) | 9.8/0.65/-4.91 | 78.13 | 122 | 0.0489 | 0.99001 (33.34) | 1.0 | 0.644 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1883 | BROAD|drop_revert(drop=0.15,hold=3,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1884 | BROAD|drop_revert(drop=0.15,hold=3,n=5) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0222 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1885 | BROAD|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 78.13 | 1 | 0.0147 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1886 | BROAD|drop_revert(drop=0.15,hold=5,n=5) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0222 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 1886

## Engine prereg 20261024_051307_gen_2410240527_000 (gen_2410240527_000, sha256 f131ddb7b479): rows #1887-1890 RESERVED (4 variants). Counted in N.
N_cumulative: 1890

## Engine run 20261024_051307_gen_2410240527_000 (gen_2410240527_000): rows #1887-1890. 0/4 pass. PBO 0.712. Bar applied at N=1890. Report: engine/runs/20261024_051307_gen_2410240527_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1887 | crypto|supertrend(atr_n=7,mult=2) | 1.98/0.22/-36.38 | 434.62 | 105 | 0.0188 | 0.92607 (184.25) | 1.0 | 0.379 | 0.9205 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1888 | crypto|supertrend(atr_n=7,mult=3) | 14.1/0.44/-22.62 | 434.62 | 57 | 0.0198 | 0.83816 (108.71) | 1.0 | 0.4834 | 0.9125 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1889 | crypto|supertrend(atr_n=14,mult=2) | 8.75/0.34/-27.63 | 434.62 | 104 | 0.0185 | 0.87113 (98.31) | 1.0 | 0.4358 | 0.915 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1890 | crypto|supertrend(atr_n=14,mult=3) | -2.86/0.12/-29.83 | 434.62 | 59 | 0.0195 | 0.92907 (77.38) | 1.0 | 0.337 | 0.922 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1890

## Engine prereg 20261024_060448_gen_2410240600_000 (gen_2410240600_000, sha256 a3034070e0d1): rows #1891-1894 RESERVED (4 variants). Counted in N.
N_cumulative: 1894

## Engine run 20261024_060448_gen_2410240600_000 (gen_2410240600_000): rows #1891-1894. 0/4 pass. PBO 0.49. Bar applied at N=1894. Report: engine/runs/20261024_060448_gen_2410240600_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1891 | crypto|donchian(entry_n=55,exit_n=10) | 250.98/0.87/-24.68 | 428.6 | 959 | 0.1037 | 0.27972 (121.87) | 1.0 | 0.949 | 0.9495 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1892 | crypto|donchian(entry_n=55,exit_n=20) | 212.99/0.83/-38.82 | 428.6 | 771 | 0.1005 | 0.38561 (76.95) | 1.0 | 0.928 | 0.9705 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1893 | crypto|donchian(entry_n=100,exit_n=10) | 328.47/0.94/-15.33 | 428.6 | 689 | 0.0994 | 0.15185 (73.39) | 1.0 | 0.9763 | 0.8875 | False | beats_buy_hold, cost_stop, holm, spa |
| 1894 | crypto|donchian(entry_n=100,exit_n=20) | 329.19/0.94/-22.39 | 428.6 | 554 | 0.0976 | 0.15485 (132.47) | 1.0 | 0.9757 | 0.8905 | False | beats_buy_hold, cost_stop, holm, spa |

N_cumulative: 1894

## Engine prereg 20261024_060455_gen_2410240601_000 (gen_2410240601_000, sha256 0109fea4e70f): rows #1895-1898 RESERVED (4 variants). Counted in N.
N_cumulative: 1898

## Engine run 20261024_060455_gen_2410240601_000 (gen_2410240601_000): rows #1895-1898. 0/4 pass. PBO 0.109. Bar applied at N=1898. Report: engine/runs/20261024_060455_gen_2410240601_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1895 | sectors|sma_cross(fast=5,slow=100) | 9.94/0.41/-11.71 | 50.2 | 256 | 0.0635 | 0.96803 (22.19) | 1.0 | 0.6449 | 0.519 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1896 | sectors|sma_cross(fast=5,slow=200) | 11.83/0.47/-11.94 | 50.2 | 168 | 0.0605 | 0.95105 (22.23) | 1.0 | 0.6778 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1897 | sectors|sma_cross(fast=10,slow=100) | 8.43/0.36/-12.66 | 50.2 | 193 | 0.0644 | 0.98901 (22.35) | 1.0 | 0.6097 | 0.5095 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1898 | sectors|sma_cross(fast=10,slow=200) | 12.77/0.49/-13.04 | 50.2 | 119 | 0.0645 | 0.93606 (22.94) | 1.0 | 0.6886 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1898

## Engine prereg 20261024_060500_gen_2410240602_000 (gen_2410240602_000, sha256 88e74d32d495): rows #1899-1906 RESERVED (8 variants). Counted in N.
N_cumulative: 1906

## Engine run 20261024_060500_gen_2410240602_000 (gen_2410240602_000): rows #1899-1906. 0/8 pass. PBO 0.556. Bar applied at N=1906. Report: engine/runs/20261024_060500_gen_2410240602_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1899 | crypto_d|drop_revert(drop=0.05,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | -3.32/-1.19/-3.88 | 234.6 | 10 | 0.0264 | 0.98901 (170.62) | 1.0 | 0.001 | 0.9 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1900 | crypto_d|drop_revert(drop=0.05,hold=5,n=3)+vol_regime(max_atr_pct=0.04) | -1.74/-0.43/-2.46 | 234.6 | 23 | 0.0258 | 0.97602 (151.75) | 1.0 | 0.018 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1901 | crypto_d|drop_revert(drop=0.05,hold=10,n=1)+vol_regime(max_atr_pct=0.04) | -0.4/-0.1/-3.42 | 234.6 | 17 | 0.0256 | 0.98501 (159.16) | 1.0 | 0.0487 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1902 | crypto_d|drop_revert(drop=0.05,hold=10,n=3)+vol_regime(max_atr_pct=0.04) | -1.8/-0.3/-3.87 | 234.6 | 33 | 0.0255 | 0.97502 (151.07) | 1.0 | 0.028 | 0.899 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1903 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (173.95) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1904 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+vol_regime(max_atr_pct=0.04) | -0.47/-0.37/-1.25 | 234.6 | 3 | 0.0258 | 0.99001 (175.27) | 1.0 | 0.0292 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1905 | crypto_d|drop_revert(drop=0.1,hold=10,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (40.99) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1906 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+vol_regime(max_atr_pct=0.04) | -0.6/-0.4/-1.57 | 234.6 | 6 | 0.0257 | 0.98701 (173.46) | 1.0 | 0.0248 | 0.8975 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1906

## Engine prereg 20261024_060503_gen_2410240603_000 (gen_2410240603_000, sha256 a4e5e243904f): rows #1907-1914 RESERVED (8 variants). Counted in N.
N_cumulative: 1914

## Engine run 20261024_060503_gen_2410240603_000 (gen_2410240603_000): rows #1907-1914. 0/8 pass. PBO 0.044. Bar applied at N=1914. Report: engine/runs/20261024_060503_gen_2410240603_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1907 | megacap|rsi_revert(entry=5,exit=60,n=3) | -0.11/0.02/-10.43 | 26.77 | 667 | 0.1179 | 0.87413 (10.21) | 1.0 | 0.0052 | 0.929 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1908 | megacap|rsi_revert(entry=5,exit=60,n=5) | 3.75/1.16/-1.52 | 26.77 | 68 | 0.095 | 0.89211 (13.76) | 1.0 | 0.131 | 0.8695 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1909 | megacap|rsi_revert(entry=5,exit=70,n=3) | 2.75/0.28/-7.43 | 26.77 | 639 | 0.1191 | 0.84016 (9.65) | 1.0 | 0.0128 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1910 | megacap|rsi_revert(entry=5,exit=70,n=5) | 5.57/1.36/-1.21 | 26.77 | 67 | 0.0958 | 0.86114 (12.4) | 1.0 | 0.1738 | 0.863 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1911 | megacap|rsi_revert(entry=20,exit=60,n=3) | -6.13/-0.28/-15.23 | 26.77 | 2437 | 0.1198 | 0.71129 (0.72) | 1.0 | 0.0018 | 0.971 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1912 | megacap|rsi_revert(entry=20,exit=60,n=5) | 7.76/0.51/-10.16 | 26.77 | 1030 | 0.1194 | 0.45954 (7.93) | 1.0 | 0.0273 | 0.8585 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1913 | megacap|rsi_revert(entry=20,exit=70,n=3) | -0.62/0.04/-16.97 | 26.77 | 2115 | 0.1214 | 0.75025 (2.09) | 1.0 | 0.0059 | 0.9365 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1914 | megacap|rsi_revert(entry=20,exit=70,n=5) | 14.28/0.7/-11.79 | 26.77 | 892 | 0.1193 | 0.56244 (8.72) | 1.0 | 0.0453 | 0.8445 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1914

## Engine prereg 20261024_060506_gen_2410240604_000 (gen_2410240604_000, sha256 630af81a08ea): rows #1915-1930 RESERVED (16 variants). Counted in N.
N_cumulative: 1930

## Engine run 20261024_060506_gen_2410240604_000 (gen_2410240604_000): rows #1915-1930. 0/16 pass. PBO 0.347. Bar applied at N=1930. Report: engine/runs/20261024_060506_gen_2410240604_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1915 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=1) | 3.83/0.31/-5.22 | 78.13 | 1619 | 0.0875 | 0.98801 (20.53) | 1.0 | 0.0034 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1916 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=2) | -12.15/-1.02/-14.78 | 78.13 | 1594 | 0.0869 | 1.0 (20.26) | 1.0 | 0.0 | 0.492 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1917 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=3) | -6.32/-0.51/-10.46 | 78.13 | 1562 | 0.087 | 0.999 (20.31) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1918 | BROAD|sma_cross(fast=10,slow=50)+day_of_week(days=4) | -3.8/-0.33/-10.54 | 78.13 | 1565 | 0.0873 | 0.999 (21.09) | 1.0 | 0.0001 | 0.4885 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1919 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=1) | 1.46/0.13/-7.1 | 78.13 | 1692 | 0.0871 | 0.99401 (19.35) | 1.0 | 0.0014 | 0.5115 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1920 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=2) | -12.53/-1.0/-14.03 | 78.13 | 1671 | 0.0868 | 1.0 (19.67) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1921 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=3) | -11.12/-0.86/-14.36 | 78.13 | 1650 | 0.087 | 1.0 (20.2) | 1.0 | 0.0 | 0.498 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1922 | BROAD|sma_cross(fast=10,slow=150)+day_of_week(days=4) | -2.03/-0.17/-7.79 | 78.13 | 1651 | 0.0873 | 0.999 (19.15) | 1.0 | 0.0002 | 0.4885 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1923 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=1) | 4.29/0.34/-3.92 | 78.13 | 1618 | 0.0868 | 0.98701 (20.94) | 1.0 | 0.004 | 0.507 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1924 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=2) | -15.77/-1.34/-18.01 | 78.13 | 1595 | 0.0863 | 1.0 (21.39) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1925 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=3) | -9.25/-0.72/-11.93 | 78.13 | 1569 | 0.0865 | 1.0 (21.09) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1926 | BROAD|sma_cross(fast=20,slow=50)+day_of_week(days=4) | 0.65/0.08/-6.45 | 78.13 | 1563 | 0.0871 | 0.995 (21.47) | 1.0 | 0.0009 | 0.485 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1927 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=1) | 2.65/0.22/-6.11 | 78.13 | 1691 | 0.087 | 0.98302 (19.34) | 1.0 | 0.0023 | 0.507 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1928 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=2) | -12.66/-1.01/-14.06 | 78.13 | 1672 | 0.0865 | 1.0 (19.57) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1929 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=3) | -10.97/-0.83/-14.16 | 78.13 | 1651 | 0.0865 | 1.0 (19.65) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1930 | BROAD|sma_cross(fast=20,slow=150)+day_of_week(days=4) | -2.65/-0.22/-7.98 | 78.13 | 1658 | 0.0872 | 0.998 (19.99) | 1.0 | 0.0001 | 0.488 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1930

## Engine prereg 20261024_060511_gen_2410240605_000 (gen_2410240605_000, sha256 144f7b8c3b7d): rows #1931-1938 RESERVED (8 variants). Counted in N.
N_cumulative: 1938

## Engine run 20261024_060511_gen_2410240605_000 (gen_2410240605_000): rows #1931-1938. 0/8 pass. PBO 0.062. Bar applied at N=1938. Report: engine/runs/20261024_060511_gen_2410240605_000/report.md

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

N_cumulative: 1938

## Engine prereg 20261024_060515_gen_2410240606_000 (gen_2410240606_000, sha256 b99b8e550a08): rows #1939-1942 RESERVED (4 variants). Counted in N.
N_cumulative: 1942

## Engine run 20261024_060515_gen_2410240606_000 (gen_2410240606_000): rows #1939-1942. 0/4 pass. PBO 0.911. Bar applied at N=1942. Report: engine/runs/20261024_060515_gen_2410240606_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1939 | hibeta|sma_cross(fast=10,slow=150)+relvol(min_ratio=1.0) | 162.25/1.59/-25.81 | 809.88 | 970 | 0.0239 | 0.63037 (189.19) | 1.0 | 0.9855 | 0.5165 | False | beats_buy_hold, holm, spa, pbo |
| 1940 | hibeta|sma_cross(fast=10,slow=200)+relvol(min_ratio=1.0) | 134.57/1.4/-29.16 | 809.88 | 1003 | 0.0239 | 0.78721 (194.0) | 1.0 | 0.9664 | 0.5095 | False | beats_buy_hold, holm, spa, pbo |
| 1941 | hibeta|sma_cross(fast=20,slow=150)+relvol(min_ratio=1.0) | 156.92/1.54/-28.56 | 809.88 | 959 | 0.0238 | 0.69431 (198.03) | 1.0 | 0.9811 | 0.5125 | False | beats_buy_hold, holm, spa, pbo |
| 1942 | hibeta|sma_cross(fast=20,slow=200)+relvol(min_ratio=1.0) | 130.91/1.38/-29.08 | 809.88 | 995 | 0.0238 | 0.83317 (204.16) | 1.0 | 0.9626 | 0.509 | False | beats_buy_hold, holm, spa, pbo |

N_cumulative: 1942

## Engine prereg 20261024_060517_gen_2410240607_000 (gen_2410240607_000, sha256 d98b48e04a01): rows #1943-1950 RESERVED (8 variants). Counted in N.
N_cumulative: 1950

## Engine run 20261024_060517_gen_2410240607_000 (gen_2410240607_000): rows #1943-1950. 0/8 pass. PBO 0.52. Bar applied at N=1950. Report: engine/runs/20261024_060517_gen_2410240607_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1943 | crypto|rsi_revert(entry=10,exit=70,n=3)+rsi_band(hi=70) | -17.11/-0.36/-30.56 | 428.6 | 2130 | 0.0978 | 0.9001 (59.7) | 1.0 | 0.03 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1944 | crypto|rsi_revert(entry=10,exit=70,n=5)+rsi_band(hi=70) | -23.84/-0.81/-30.67 | 428.6 | 535 | 0.0927 | 0.995 (99.34) | 1.0 | 0.0055 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1945 | crypto|rsi_revert(entry=10,exit=80,n=3)+rsi_band(hi=70) | -18.34/-0.28/-33.41 | 428.6 | 1825 | 0.099 | 0.92108 (89.13) | 1.0 | 0.0388 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1946 | crypto|rsi_revert(entry=10,exit=80,n=5)+rsi_band(hi=70) | -9.13/-0.11/-31.65 | 428.6 | 478 | 0.0931 | 0.95305 (185.96) | 1.0 | 0.0625 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1947 | crypto|rsi_revert(entry=20,exit=70,n=3)+rsi_band(hi=70) | -28.83/-0.49/-45.79 | 428.6 | 4170 | 0.1017 | 0.86414 (86.09) | 1.0 | 0.0212 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1948 | crypto|rsi_revert(entry=20,exit=70,n=5)+rsi_band(hi=70) | -14.67/-0.17/-26.48 | 428.6 | 1621 | 0.0995 | 0.92408 (162.47) | 1.0 | 0.0528 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1949 | crypto|rsi_revert(entry=20,exit=80,n=3)+rsi_band(hi=70) | -17.84/-0.13/-44.65 | 428.6 | 3212 | 0.1017 | 0.84815 (62.7) | 1.0 | 0.0589 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1950 | crypto|rsi_revert(entry=20,exit=80,n=5)+rsi_band(hi=70) | 9.82/0.37/-28.5 | 428.6 | 1186 | 0.1002 | 0.78422 (171.8) | 1.0 | 0.1716 | 0.899 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 1950

## Engine prereg 20261024_060524_gen_2410240608_000 (gen_2410240608_000, sha256 76ced2f1c187): rows #1951-1958 RESERVED (8 variants). Counted in N.
N_cumulative: 1958

## Engine run 20261024_060524_gen_2410240608_000 (gen_2410240608_000): rows #1951-1958. 0/8 pass. PBO 0.461. Bar applied at N=1958. Report: engine/runs/20261024_060524_gen_2410240608_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1951 | sectors|rsi_revert(entry=10,exit=60,n=2) | 15.83/0.8/-5.08 | 50.2 | 993 | 0.0698 | 0.71329 (19.45) | 1.0 | 0.719 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1952 | sectors|rsi_revert(entry=10,exit=60,n=5) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0631 | 0.997 (23.0) | 1.0 | 0.5832 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1953 | sectors|rsi_revert(entry=10,exit=70,n=2) | 21.31/0.99/-5.61 | 50.2 | 941 | 0.0701 | 0.34266 (19.15) | 1.0 | 0.8308 | 0.9455 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1954 | sectors|rsi_revert(entry=10,exit=70,n=5) | 6.29/0.96/-1.66 | 50.2 | 79 | 0.0631 | 0.99101 (23.72) | 1.0 | 0.7811 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1955 | sectors|rsi_revert(entry=20,exit=60,n=2) | 16.85/0.73/-8.14 | 50.2 | 1652 | 0.0701 | 0.45854 (16.32) | 1.0 | 0.6469 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1956 | sectors|rsi_revert(entry=20,exit=60,n=5) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0656 | 0.44755 (21.9) | 1.0 | 0.8857 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1957 | sectors|rsi_revert(entry=20,exit=70,n=2) | 22.98/0.91/-9.13 | 50.2 | 1505 | 0.0703 | 0.16484 (17.06) | 1.0 | 0.764 | 0.965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1958 | sectors|rsi_revert(entry=20,exit=70,n=5) | 24.67/1.02/-7.08 | 50.2 | 312 | 0.0674 | 0.32567 (22.48) | 1.0 | 0.8322 | 0.9265 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 1958

## Engine prereg 20261024_060528_gen_2410240609_000 (gen_2410240609_000, sha256 31729bacc063): rows #1959-1966 RESERVED (8 variants). Counted in N.
N_cumulative: 1966

## Engine run 20261024_060528_gen_2410240609_000 (gen_2410240609_000): rows #1959-1966. 0/8 pass. PBO 0.731. Bar applied at N=1966. Report: engine/runs/20261024_060528_gen_2410240609_000/report.md

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

N_cumulative: 1966

## Engine prereg 20261024_060530_gen_2410240610_000 (gen_2410240610_000, sha256 2c4547688263): rows #1967-1986 RESERVED (20 variants). Counted in N.
N_cumulative: 1986

## Engine run 20261024_060530_gen_2410240610_000 (gen_2410240610_000): rows #1967-1986. 0/20 pass. PBO 0.18. Bar applied at N=1986. Report: engine/runs/20261024_060530_gen_2410240610_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1967 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | 7.21/0.97/-3.59 | 26.77 | 963 | 0.1248 | 0.81518 (7.83) | 1.0 | 0.0036 | 0.8365 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1968 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | 0.76/0.1/-9.01 | 26.77 | 1127 | 0.1258 | 0.90809 (6.67) | 1.0 | 0.0002 | 0.904 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1969 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | 6.99/0.63/-6.08 | 26.77 | 1109 | 0.1247 | 0.69231 (7.4) | 1.0 | 0.0016 | 0.8295 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1970 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -11.18/-1.13/-14.65 | 26.77 | 1064 | 0.1213 | 0.99401 (8.01) | 1.0 | 0.0 | 0.4985 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1971 | megacap|supertrend(atr_n=7,mult=2)+day_of_week(days=4) | 0.78/0.11/-5.69 | 26.77 | 977 | 0.1276 | 0.96503 (7.83) | 1.0 | 0.0001 | 0.918 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1972 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | 10.03/1.45/-3.83 | 26.77 | 830 | 0.1299 | 0.58042 (8.2) | 1.0 | 0.0328 | 0.7915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1973 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | -5.89/-0.64/-7.61 | 26.77 | 954 | 0.1293 | 0.98601 (8.01) | 1.0 | 0.0 | 0.9515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1974 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | 6.65/0.58/-7.26 | 26.77 | 979 | 0.1289 | 0.77223 (7.71) | 1.0 | 0.0007 | 0.8365 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1975 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | -11.69/-1.18/-14.32 | 26.77 | 959 | 0.1265 | 0.997 (8.2) | 1.0 | 0.0 | 0.5005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1976 | megacap|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | -18.39/-0.91/-23.11 | 26.77 | 920 | 0.1291 | 0.97303 (8.34) | 1.0 | 0.0 | 0.9545 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1977 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | 4.27/0.57/-3.66 | 26.77 | 970 | 0.1248 | 0.86314 (7.92) | 1.0 | 0.0008 | 0.878 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1978 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | 0.15/0.05/-9.27 | 26.77 | 1117 | 0.1259 | 0.92607 (7.17) | 1.0 | 0.0001 | 0.914 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1979 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 7.72/0.69/-6.09 | 26.77 | 1113 | 0.1256 | 0.70729 (7.91) | 1.0 | 0.002 | 0.8175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1980 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -9.78/-0.89/-15.24 | 26.77 | 1083 | 0.1212 | 0.99401 (7.7) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1981 | megacap|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | 0.8/0.11/-4.75 | 26.77 | 995 | 0.1273 | 0.95405 (7.92) | 1.0 | 0.0001 | 0.9235 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1982 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | 9.49/1.37/-3.76 | 26.77 | 828 | 0.1292 | 0.58841 (8.22) | 1.0 | 0.0264 | 0.7955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1983 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -4.73/-0.52/-7.22 | 26.77 | 954 | 0.1281 | 0.97403 (7.51) | 1.0 | 0.0 | 0.945 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1984 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 5.56/0.48/-8.74 | 26.77 | 988 | 0.1283 | 0.78821 (8.6) | 1.0 | 0.0006 | 0.8475 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1985 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | -10.68/-1.06/-13.34 | 26.77 | 959 | 0.1274 | 0.995 (8.56) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1986 | megacap|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -18.5/-0.91/-23.44 | 26.77 | 927 | 0.1289 | 0.97403 (8.22) | 1.0 | 0.0 | 0.9545 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 1986

## Engine prereg 20261024_070438_gen_2410240700_000 (gen_2410240700_000, sha256 72e98423df03): rows #1987-1994 RESERVED (8 variants). Counted in N.
N_cumulative: 1994

## Engine run 20261024_070438_gen_2410240700_000 (gen_2410240700_000): rows #1987-1994. 0/8 pass. PBO 0.679. Bar applied at N=1994. Report: engine/runs/20261024_070438_gen_2410240700_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1987 | crypto|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0165 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1988 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 21 | 0.0165 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1989 | crypto|drop_revert(drop=0.1,hold=10,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 5 | 0.017 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1990 | crypto|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=50) | 0.37/0.83/0.0 | 428.6 | 37 | 0.0179 | 0.92607 (42.33) | 1.0 | nan | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1991 | crypto|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 1 | 0.016 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1992 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 3 | 0.0143 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1993 | crypto|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 1 | 0.016 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1994 | crypto|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 428.6 | 3 | 0.0143 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 1994

## Engine prereg 20261024_070447_gen_2410240701_000 (gen_2410240701_000, sha256 43b432e663df): rows #1995-2002 RESERVED (8 variants). Counted in N.
N_cumulative: 2002

## Engine run 20261024_070447_gen_2410240701_000 (gen_2410240701_000): rows #1995-2002. 0/8 pass. PBO 0.644. Bar applied at N=2002. Report: engine/runs/20261024_070447_gen_2410240701_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1995 | sectors|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=50) | -0.63/-0.54/-0.63 | 50.2 | 36 | 0.0368 | 1.0 (23.24) | 1.0 | 0.0055 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1996 | sectors|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=50) | -0.59/-0.48/-0.78 | 50.2 | 63 | 0.0423 | 1.0 (23.28) | 1.0 | 0.0123 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1997 | sectors|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=50) | -0.61/-0.49/-0.8 | 50.2 | 54 | 0.0422 | 1.0 (23.58) | 1.0 | 0.0091 | 0.4945 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1998 | sectors|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=50) | -0.16/-0.1/-0.88 | 50.2 | 89 | 0.0438 | 1.0 (22.82) | 1.0 | 0.084 | 0.498 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1999 | sectors|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 1 | 0.0197 | 1.0 (23.8) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2000 | sectors|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.42) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2001 | sectors|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 1 | 0.0197 | 1.0 (22.82) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2002 | sectors|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.61) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2002

## Engine prereg 20261024_070450_gen_2410240702_000 (gen_2410240702_000, sha256 41895e3b6438): rows #2003-2010 RESERVED (8 variants). Counted in N.
N_cumulative: 2010

## Engine run 20261024_070450_gen_2410240702_000 (gen_2410240702_000): rows #2003-2010. 0/8 pass. PBO 0.674. Bar applied at N=2010. Report: engine/runs/20261024_070450_gen_2410240702_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2003 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 6.01/0.64/-4.06 | 234.6 | 36 | 0.0099 | 0.9041 (35.77) | 1.0 | 0.4524 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2004 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 8.29/0.67/-5.16 | 234.6 | 108 | 0.0112 | 0.85415 (120.03) | 1.0 | 0.4715 | 0.89 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2005 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=50) | 6.95/0.7/-5.32 | 234.6 | 37 | 0.0099 | 0.91508 (164.53) | 1.0 | 0.4867 | 0.891 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2006 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=50) | 5.44/0.38/-11.33 | 234.6 | 126 | 0.0113 | 0.84116 (67.71) | 1.0 | 0.3386 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2007 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 3.48/1.12/-0.17 | 234.6 | 8 | 0.0071 | 0.93906 (47.74) | 1.0 | 0.8125 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2008 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 4.16/0.68/-2.48 | 234.6 | 47 | 0.0101 | 0.8991 (66.33) | 1.0 | 0.4762 | 0.8935 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2009 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+trend_sma(n=50) | 2.18/0.65/-1.26 | 234.6 | 8 | 0.0071 | 0.96404 (43.86) | 1.0 | 0.4561 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2010 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=50) | 3.91/0.51/-4.47 | 234.6 | 56 | 0.0102 | 0.89411 (68.41) | 1.0 | 0.398 | 0.8935 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 2010

## Engine prereg 20261024_070453_gen_2410240703_000 (gen_2410240703_000, sha256 dbc33d271d90): rows #2011-2014 RESERVED (4 variants). Counted in N.
N_cumulative: 2014

## Engine run 20261024_070453_gen_2410240703_000 (gen_2410240703_000): rows #2011-2014. 0/4 pass. PBO 0.776. Bar applied at N=2014. Report: engine/runs/20261024_070453_gen_2410240703_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2011 | BROAD|supertrend(atr_n=7,mult=2) | 32.86/1.25/-6.21 | 78.13 | 361 | 0.0821 | 0.41059 (30.94) | 1.0 | 0.9618 | 0.497 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2012 | BROAD|supertrend(atr_n=7,mult=3) | 35.38/1.26/-7.12 | 78.13 | 210 | 0.081 | 0.33766 (31.78) | 1.0 | 0.9627 | 0.492 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2013 | BROAD|supertrend(atr_n=10,mult=2) | 29.4/1.12/-7.62 | 78.13 | 365 | 0.0811 | 0.56743 (31.45) | 1.0 | 0.939 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2014 | BROAD|supertrend(atr_n=10,mult=3) | 34.44/1.21/-7.52 | 78.13 | 215 | 0.0797 | 0.40659 (32.43) | 1.0 | 0.955 | 0.496 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

N_cumulative: 2014

## Engine prereg 20261024_070455_gen_2410240704_000 (gen_2410240704_000, sha256 8afcc958c2fc): rows #2015-2018 RESERVED (4 variants). Counted in N.
N_cumulative: 2018

## Engine run 20261024_070455_gen_2410240704_000 (gen_2410240704_000): rows #2015-2018. 0/4 pass. PBO 0.367. Bar applied at N=2018. Report: engine/runs/20261024_070455_gen_2410240704_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | hibeta|donchian(entry_n=55,exit_n=10) | 159.02/1.43/-19.92 | 809.88 | 117 | 0.0268 | 0.76623 (222.91) | 1.0 | 0.8463 | 0.512 | False | beats_buy_hold, holm, dsr, spa |
| 2016 | hibeta|donchian(entry_n=55,exit_n=20) | 112.02/1.06/-33.06 | 809.88 | 89 | 0.0253 | 0.91109 (223.74) | 1.0 | 0.6389 | 0.5175 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2017 | hibeta|donchian(entry_n=100,exit_n=10) | 145.61/1.59/-11.11 | 809.88 | 86 | 0.029 | 0.7982 (221.45) | 1.0 | 0.908 | 0.51 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2018 | hibeta|donchian(entry_n=100,exit_n=20) | 96.24/1.13/-18.86 | 809.88 | 67 | 0.0278 | 0.95704 (227.74) | 1.0 | 0.6844 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 2018

## Engine prereg 20261024_070500_gen_2410240705_000 (gen_2410240705_000, sha256 ace82fb80a25): rows #2019-2022 RESERVED (4 variants). Counted in N.
N_cumulative: 2022

## Engine run 20261024_070500_gen_2410240705_000 (gen_2410240705_000): rows #2019-2022. 0/4 pass. PBO 0.047. Bar applied at N=2022. Report: engine/runs/20261024_070500_gen_2410240705_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | crypto|sma_cross(fast=5,slow=100) | 22.9/0.57/-43.01 | 428.6 | 1314 | 0.1048 | 0.65135 (87.62) | 1.0 | 0.4713 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2020 | crypto|sma_cross(fast=5,slow=150) | -0.17/0.19/-40.03 | 428.6 | 1068 | 0.1035 | 0.84515 (75.5) | 1.0 | 0.2974 | 0.921 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2021 | crypto|sma_cross(fast=20,slow=100) | 23.33/0.57/-42.12 | 428.6 | 793 | 0.1029 | 0.71628 (175.09) | 1.0 | 0.4746 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2022 | crypto|sma_cross(fast=20,slow=150) | 15.42/0.45/-39.27 | 428.6 | 621 | 0.1018 | 0.78222 (111.07) | 1.0 | 0.4175 | 0.9165 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2022

## Engine prereg 20261024_070504_gen_2410240706_000 (gen_2410240706_000, sha256 abeda84459c4): rows #2023-2026 RESERVED (4 variants). Counted in N.
N_cumulative: 2026

## Engine run 20261024_070504_gen_2410240706_000 (gen_2410240706_000): rows #2023-2026. 0/4 pass. PBO 0.055. Bar applied at N=2026. Report: engine/runs/20261024_070504_gen_2410240706_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2023 | sectors|supertrend(atr_n=10,mult=2)+trend_sma(n=50) | 10.18/0.55/-6.87 | 50.2 | 730 | 0.0665 | 0.95604 (20.21) | 1.0 | 0.6768 | 0.4895 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2024 | sectors|supertrend(atr_n=10,mult=4)+trend_sma(n=50) | 7.64/0.4/-7.82 | 50.2 | 466 | 0.072 | 0.98302 (21.26) | 1.0 | 0.583 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2025 | sectors|supertrend(atr_n=14,mult=2)+trend_sma(n=50) | 11.25/0.59/-6.86 | 50.2 | 735 | 0.0659 | 0.93207 (19.8) | 1.0 | 0.7028 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2026 | sectors|supertrend(atr_n=14,mult=4)+trend_sma(n=50) | 10.08/0.51/-7.69 | 50.2 | 488 | 0.0694 | 0.97103 (21.02) | 1.0 | 0.6524 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 2026

## Engine prereg 20261024_070508_gen_2410240707_000 (gen_2410240707_000, sha256 46909b500375): rows #2027-2030 RESERVED (4 variants). Counted in N.
N_cumulative: 2030

## Engine run 20261024_070508_gen_2410240707_000 (gen_2410240707_000): rows #2027-2030. 0/4 pass. PBO 0.785. Bar applied at N=2030. Report: engine/runs/20261024_070508_gen_2410240707_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027 | crypto_d|sma_cross(fast=20,slow=50) | 15.82/0.45/-31.97 | 234.6 | 89 | 0.0168 | 0.79321 (86.88) | 1.0 | 0.3143 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2028 | crypto_d|sma_cross(fast=20,slow=200) | -8.3/0.06/-33.75 | 234.6 | 29 | 0.0157 | 0.90609 (114.05) | 1.0 | 0.169 | 0.9155 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2029 | crypto_d|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 234.6 | 0 | inf | 1.0 (31.54) | 1.0 | 0.0 | 0.897 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2030 | crypto_d|sma_cross(fast=50,slow=200) | -11.26/-0.0/-38.28 | 234.6 | 24 | 0.0165 | 0.94406 (72.9) | 1.0 | 0.1518 | 0.9165 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2030

## Engine prereg 20261024_070510_gen_2410240708_000 (gen_2410240708_000, sha256 4edbf656f733): rows #2031-2038 RESERVED (8 variants). Counted in N.
N_cumulative: 2038

## Engine run 20261024_070510_gen_2410240708_000 (gen_2410240708_000): rows #2031-2038. 0/8 pass. PBO 0.716. Bar applied at N=2038. Report: engine/runs/20261024_070510_gen_2410240708_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2031 | BROAD|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=100) | 1.85/1.0/-0.26 | 78.13 | 26 | 0.0474 | 0.99301 (34.36) | 1.0 | 0.8917 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2032 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=100) | 2.97/1.03/-0.67 | 78.13 | 43 | 0.0514 | 0.999 (34.15) | 1.0 | 0.8186 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2033 | BROAD|drop_revert(drop=0.05,hold=10,n=3)+trend_sma(n=100) | 4.52/1.13/-0.74 | 78.13 | 47 | 0.0475 | 0.998 (34.32) | 1.0 | 0.9075 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2034 | BROAD|drop_revert(drop=0.05,hold=10,n=5)+trend_sma(n=100) | 7.47/1.36/-1.01 | 78.13 | 65 | 0.0515 | 0.998 (33.41) | 1.0 | 0.9417 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2035 | BROAD|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 2 | 0.0315 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2036 | BROAD|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 2 | 0.0384 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2037 | BROAD|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 3 | 0.0351 | 1.0 (32.63) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2038 | BROAD|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 78.13 | 4 | 0.0363 | 1.0 (35.42) | 1.0 | 0.0 | 0.499 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2038

## Engine prereg 20261024_070513_gen_2410240709_000 (gen_2410240709_000, sha256 c924508fa280): rows #2039-2046 RESERVED (8 variants). Counted in N.
N_cumulative: 2046

## Engine run 20261024_070513_gen_2410240709_000 (gen_2410240709_000): rows #2039-2046. 0/8 pass. PBO 0.733. Bar applied at N=2046. Report: engine/runs/20261024_070513_gen_2410240709_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2039 | hibeta|drop_revert(drop=0.05,hold=3,n=1) | 124.02/1.2/-17.41 | 809.88 | 503 | 0.0161 | 0.85315 (212.35) | 1.0 | 0.3551 | 0.5095 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2040 | hibeta|drop_revert(drop=0.05,hold=3,n=5) | 53.09/0.62/-25.79 | 809.88 | 516 | 0.0199 | 0.98901 (212.02) | 1.0 | 0.0869 | 0.5175 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2041 | hibeta|drop_revert(drop=0.05,hold=5,n=1) | 200.16/1.38/-22.26 | 809.88 | 410 | 0.0174 | 0.51349 (211.32) | 1.0 | 0.4934 | 0.5125 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2042 | hibeta|drop_revert(drop=0.05,hold=5,n=5) | 82.08/0.76/-33.74 | 809.88 | 460 | 0.0204 | 0.96004 (212.06) | 1.0 | 0.1329 | 0.515 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2043 | hibeta|drop_revert(drop=0.1,hold=3,n=1) | 55.83/1.62/-4.01 | 809.88 | 87 | 0.0113 | 0.98102 (230.3) | 1.0 | 0.6909 | 0.5065 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2044 | hibeta|drop_revert(drop=0.1,hold=3,n=5) | 47.38/0.68/-17.67 | 809.88 | 293 | 0.0155 | 0.998 (215.67) | 1.0 | 0.0936 | 0.514 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2045 | hibeta|drop_revert(drop=0.1,hold=5,n=1) | 68.15/1.58/-4.95 | 809.88 | 80 | 0.0114 | 0.96703 (219.85) | 1.0 | 0.6545 | 0.499 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2046 | hibeta|drop_revert(drop=0.1,hold=5,n=5) | 87.69/0.95/-18.89 | 809.88 | 276 | 0.0155 | 0.96004 (219.9) | 1.0 | 0.2067 | 0.5015 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 2046

## Engine prereg 20261024_070516_gen_2410240710_000 (gen_2410240710_000, sha256 ab53e20ca2ba): rows #2047-2050 RESERVED (4 variants). Counted in N.
N_cumulative: 2050

## Engine run 20261024_070516_gen_2410240710_000 (gen_2410240710_000): rows #2047-2050. 0/4 pass. PBO 0.161. Bar applied at N=2050. Report: engine/runs/20261024_070516_gen_2410240710_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2047 | crypto|supertrend(atr_n=10,mult=2) | -11.55/-0.04/-36.31 | 428.6 | 2369 | 0.0971 | 0.82517 (37.29) | 1.0 | 0.3215 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2048 | crypto|supertrend(atr_n=10,mult=4) | -3.46/0.11/-43.75 | 428.6 | 871 | 0.0993 | 0.88112 (63.16) | 1.0 | 0.3902 | 0.9235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2049 | crypto|supertrend(atr_n=14,mult=2) | -4.81/0.1/-37.43 | 428.6 | 2376 | 0.0958 | 0.75824 (37.06) | 1.0 | 0.3848 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2050 | crypto|supertrend(atr_n=14,mult=4) | -13.24/-0.08/-47.58 | 428.6 | 874 | 0.0969 | 0.94605 (164.26) | 1.0 | 0.3043 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2050

## Engine prereg 20261024_070521_gen_2410240711_000 (gen_2410240711_000, sha256 d8e606d6bfae): rows #2051-2054 RESERVED (4 variants). Counted in N.
N_cumulative: 2054

## Engine run 20261024_070521_gen_2410240711_000 (gen_2410240711_000): rows #2051-2054. 0/4 pass. PBO 0.754. Bar applied at N=2054. Report: engine/runs/20261024_070521_gen_2410240711_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2051 | sectors|sma_cross(fast=20,slow=50) | 11.89/0.51/-8.59 | 50.2 | 243 | 0.0704 | 0.96603 (22.32) | 1.0 | 0.7172 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2052 | sectors|sma_cross(fast=20,slow=100) | 15.48/0.61/-10.18 | 50.2 | 150 | 0.0692 | 0.86613 (22.34) | 1.0 | 0.7711 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2053 | sectors|sma_cross(fast=50,slow=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.63) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2054 | sectors|sma_cross(fast=50,slow=100) | 13.98/0.57/-11.04 | 50.2 | 116 | 0.075 | 0.92807 (22.92) | 1.0 | 0.7469 | 0.5215 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2054

## Engine prereg 20261024_070524_gen_2410240713_000 (gen_2410240713_000, sha256 ddd1d7ca306c): rows #2055-2058 RESERVED (4 variants). Counted in N.
N_cumulative: 2058

## Engine run 20261024_070524_gen_2410240713_000 (gen_2410240713_000): rows #2055-2058. 0/4 pass. PBO 0.053. Bar applied at N=2058. Report: engine/runs/20261024_070524_gen_2410240713_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2055 | BROAD|donchian(entry_n=20,exit_n=10) | 26.5/1.13/-4.46 | 78.13 | 220 | 0.0831 | 0.72328 (31.57) | 1.0 | 0.3952 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2056 | BROAD|donchian(entry_n=20,exit_n=20) | 45.05/1.49/-5.88 | 78.13 | 148 | 0.0798 | 0.07493 (32.59) | 1.0 | 0.638 | 0.9785 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2057 | BROAD|donchian(entry_n=100,exit_n=10) | 8.43/0.58/-5.38 | 78.13 | 137 | 0.0899 | 0.997 (31.94) | 1.0 | 0.1179 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2058 | BROAD|donchian(entry_n=100,exit_n=20) | 20.34/1.04/-5.13 | 78.13 | 92 | 0.0844 | 0.94505 (32.95) | 1.0 | 0.3393 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2058

## Engine prereg 20261024_070526_gen_2410240714_000 (gen_2410240714_000, sha256 8de884eba0b2): rows #2059-2062 RESERVED (4 variants). Counted in N.
N_cumulative: 2062

## Engine run 20261024_070526_gen_2410240714_000 (gen_2410240714_000): rows #2059-2062. 0/4 pass. PBO 0.816. Bar applied at N=2062. Report: engine/runs/20261024_070526_gen_2410240714_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2059 | hibeta|sma_cross(fast=20,slow=150)+rsi_band(hi=70) | 186.39/1.24/-32.19 | 809.88 | 239 | 0.0247 | 0.62138 (214.73) | 1.0 | 0.927 | 0.5105 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2060 | hibeta|sma_cross(fast=20,slow=200)+rsi_band(hi=70) | 151.25/1.1/-32.7 | 809.88 | 222 | 0.024 | 0.75425 (217.08) | 1.0 | 0.8873 | 0.515 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2061 | hibeta|sma_cross(fast=50,slow=150)+rsi_band(hi=70) | 196.85/1.27/-32.7 | 809.88 | 210 | 0.0247 | 0.55345 (214.05) | 1.0 | 0.9353 | 0.5105 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2062 | hibeta|sma_cross(fast=50,slow=200)+rsi_band(hi=70) | 138.09/1.03/-32.7 | 809.88 | 199 | 0.024 | 0.81918 (219.53) | 1.0 | 0.8655 | 0.5125 | False | beats_buy_hold, holm, dsr, spa, pbo |

N_cumulative: 2062

## Engine prereg 20261024_070529_gen_2410240715_000 (gen_2410240715_000, sha256 1c10ff2f9cfe): rows #2063-2082 RESERVED (20 variants). Counted in N.
N_cumulative: 2082

## Engine run 20261024_070529_gen_2410240715_000 (gen_2410240715_000): rows #2063-2082. 0/20 pass. PBO 0.704. Bar applied at N=2082. Report: engine/runs/20261024_070529_gen_2410240715_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2063 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=0) | -29.22/-1.21/-36.37 | 428.6 | 506 | 0.1124 | 0.998 (73.8) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2064 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=1) | -10.64/-0.49/-18.55 | 428.6 | 501 | 0.1 | 0.95804 (173.1) | 1.0 | 0.0001 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2065 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=2) | 16.51/0.85/-14.34 | 428.6 | 517 | 0.0981 | 0.78921 (163.72) | 1.0 | 0.012 | 0.8995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2066 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=3) | 0.69/0.11/-16.29 | 428.6 | 505 | 0.0932 | 0.88911 (192.17) | 1.0 | 0.001 | 0.913 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2067 | crypto|sma_cross(fast=10,slow=100)+day_of_week(days=4) | -0.64/0.02/-13.4 | 428.6 | 470 | 0.0993 | 0.91409 (91.16) | 1.0 | 0.0008 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2068 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=0) | -36.99/-1.63/-41.64 | 428.6 | 487 | 0.1123 | 1.0 (91.7) | 1.0 | 0.0 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2069 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=1) | -8.99/-0.34/-18.41 | 428.6 | 484 | 0.1014 | 0.96304 (91.42) | 1.0 | 0.0002 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2070 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=2) | 20.66/0.97/-13.21 | 428.6 | 482 | 0.1006 | 0.75125 (160.47) | 1.0 | 0.0176 | 0.8965 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2071 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=3) | -3.52/-0.06/-15.81 | 428.6 | 477 | 0.0933 | 0.93307 (76.19) | 1.0 | 0.0006 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2072 | crypto|sma_cross(fast=10,slow=150)+day_of_week(days=4) | 0.21/0.07/-14.86 | 428.6 | 446 | 0.0965 | 0.89311 (90.36) | 1.0 | 0.0009 | 0.9095 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2073 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=0) | -29.34/-1.09/-37.73 | 428.6 | 461 | 0.1132 | 0.997 (138.29) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2074 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=1) | -2.5/-0.05/-16.43 | 428.6 | 458 | 0.0993 | 0.92607 (107.64) | 1.0 | 0.0006 | 0.9065 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2075 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=2) | 10.76/0.62/-12.45 | 428.6 | 448 | 0.0977 | 0.83417 (75.51) | 1.0 | 0.0052 | 0.9075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2076 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=3) | 6.56/0.36/-14.3 | 428.6 | 465 | 0.0949 | 0.85315 (112.03) | 1.0 | 0.0026 | 0.909 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2077 | crypto|sma_cross(fast=50,slow=100)+day_of_week(days=4) | 9.62/0.57/-11.52 | 428.6 | 452 | 0.0964 | 0.83217 (119.95) | 1.0 | 0.0049 | 0.905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2078 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=0) | -31.93/-1.36/-37.34 | 428.6 | 430 | 0.1123 | 0.998 (174.59) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2079 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=1) | 1.46/0.14/-23.98 | 428.6 | 420 | 0.1002 | 0.91009 (183.11) | 1.0 | 0.0012 | 0.901 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2080 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=2) | 18.74/0.97/-8.05 | 428.6 | 433 | 0.0983 | 0.76024 (197.05) | 1.0 | 0.0153 | 0.8985 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2081 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=3) | -2.8/-0.05/-14.54 | 428.6 | 428 | 0.0956 | 0.93007 (130.43) | 1.0 | 0.0006 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2082 | crypto|sma_cross(fast=50,slow=150)+day_of_week(days=4) | 8.6/0.57/-12.09 | 428.6 | 432 | 0.0981 | 0.85714 (189.12) | 1.0 | 0.0053 | 0.906 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2082

## Engine prereg 20261024_070543_gen_2410240716_000 (gen_2410240716_000, sha256 f0c8042613c5): rows #2083-2090 RESERVED (8 variants). Counted in N.
N_cumulative: 2090

## Engine run 20261024_070543_gen_2410240716_000 (gen_2410240716_000): rows #2083-2090. 0/8 pass. PBO 0.491. Bar applied at N=2090. Report: engine/runs/20261024_070543_gen_2410240716_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2083 | sectors|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.0) | 3.03/0.28/-2.54 | 50.2 | 59 | 0.0286 | 1.0 (23.07) | 1.0 | 0.3585 | 0.4975 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2084 | sectors|drop_revert(drop=0.05,hold=3,n=5)+relvol(min_ratio=1.0) | 3.06/0.21/-4.74 | 50.2 | 321 | 0.043 | 1.0 (22.34) | 1.0 | 0.3229 | 0.502 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2085 | sectors|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | 5.04/0.36/-3.02 | 50.2 | 83 | 0.0296 | 0.997 (22.93) | 1.0 | 0.4223 | 0.4985 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2086 | sectors|drop_revert(drop=0.05,hold=10,n=5)+relvol(min_ratio=1.0) | 3.14/0.21/-4.93 | 50.2 | 501 | 0.043 | 1.0 (21.72) | 1.0 | 0.324 | 0.505 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2087 | sectors|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 50.2 | 4 | 0.0213 | 1.0 (23.03) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2088 | sectors|drop_revert(drop=0.15,hold=3,n=5)+relvol(min_ratio=1.0) | 0.07/0.03/-0.73 | 50.2 | 23 | 0.0205 | 1.0 (23.3) | 1.0 | 0.2344 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2089 | sectors|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 50.2 | 9 | 0.0153 | 1.0 (23.93) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2090 | sectors|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 0.07/0.03/-0.73 | 50.2 | 32 | 0.021 | 1.0 (22.94) | 1.0 | 0.2344 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2090

## Engine prereg 20261024_080310_gen_2610240800_000 (gen_2610240800_000, sha256 9a536ad8f6d5): rows #2091-2094 RESERVED (4 variants). Counted in N.
N_cumulative: 2094

## Engine run 20261024_080310_gen_2610240800_000 (gen_2610240800_000): rows #2091-2094. 0/4 pass. PBO 0.792. Bar applied at N=2094. Report: engine/runs/20261024_080310_gen_2610240800_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2091 | crypto|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.2) | -54.62/-2.7/-58.67 | 428.6 | 8076 | 0.1032 | 0.88212 (-2.04) | 1.0 | 0.0038 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2092 | crypto|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.2) | -54.47/-2.95/-57.55 | 428.6 | 8140 | 0.1034 | 0.88911 (-11.3) | 1.0 | 0.0008 | 0.929 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2093 | crypto|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.2) | -56.97/-2.85/-60.54 | 428.6 | 8141 | 0.103 | 0.90909 (-24.78) | 1.0 | 0.0029 | 0.931 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2094 | crypto|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -57.46/-3.23/-59.97 | 428.6 | 8200 | 0.1037 | 0.92507 (12.05) | 1.0 | 0.0005 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2094

## Engine prereg 20261024_080319_gen_2610240801_000 (gen_2610240801_000, sha256 92e1b5764e89): rows #2095-2098 RESERVED (4 variants). Counted in N.
N_cumulative: 2098

## Engine run 20261024_080319_gen_2610240801_000 (gen_2610240801_000): rows #2095-2098. 0/4 pass. PBO 0.496. Bar applied at N=2098. Report: engine/runs/20261024_080319_gen_2610240801_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2095 | crypto|sma_cross(fast=5,slow=100) | 44.16/0.89/-22.2 | 56.21 | 31 | 0.0223 | 0.32268 (28.17) | 1.0 | 0.6655 | 0.7085 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2096 | crypto|sma_cross(fast=5,slow=150) | 21.78/0.54/-29.95 | 56.21 | 20 | 0.0236 | 0.56943 (27.55) | 1.0 | 0.5051 | 0.8575 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2097 | crypto|sma_cross(fast=20,slow=100) | 28.54/0.66/-29.52 | 56.21 | 22 | 0.0258 | 0.45455 (25.69) | 1.0 | 0.5607 | 0.792 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2098 | crypto|sma_cross(fast=20,slow=150) | 24.18/0.58/-31.93 | 56.21 | 14 | 0.0233 | 0.52348 (28.72) | 1.0 | 0.522 | 0.85 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 2098

## Engine prereg 20261024_080321_gen_2610240802_000 (gen_2610240802_000, sha256 3806c9a17a9f): rows #2099-2102 RESERVED (4 variants). Counted in N.
N_cumulative: 2102

## Engine run 20261024_080321_gen_2610240802_000 (gen_2610240802_000): rows #2099-2102. 0/4 pass. PBO 0.423. Bar applied at N=2102. Report: engine/runs/20261024_080321_gen_2610240802_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2099 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.52/0.72/-5.74 | 50.2 | 378 | 0.0707 | 0.96104 (21.44) | 1.0 | 0.6942 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2100 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.15/0.58/-7.68 | 50.2 | 299 | 0.0624 | 0.97203 (21.78) | 1.0 | 0.6075 | 0.5175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2101 | sectors|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.16/0.87/-3.85 | 50.2 | 282 | 0.0778 | 0.98102 (22.02) | 1.0 | 0.7774 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2102 | sectors|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.04/0.72/-4.44 | 50.2 | 225 | 0.0723 | 0.97702 (22.17) | 1.0 | 0.6951 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 2102

## Engine prereg 20261024_080326_gen_2610240803_000 (gen_2610240803_000, sha256 aea6bf9c0a06): rows #2103-2122 RESERVED (20 variants). Counted in N.
N_cumulative: 2122

## Engine run 20261024_080326_gen_2610240803_000 (gen_2610240803_000): rows #2103-2122. 0/20 pass. PBO 0.31. Bar applied at N=2122. Report: engine/runs/20261024_080326_gen_2610240803_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2103 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=0) | -9.41/-0.87/-10.5 | 5.92 | 804 | 0.054 | 0.72627 (-1.61) | 1.0 | 0.0 | 0.7565 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2104 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=1) | -4.99/-0.36/-8.3 | 5.92 | 899 | 0.0548 | 0.59341 (-2.05) | 1.0 | 0.0002 | 0.7245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2105 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=2) | -16.5/-1.23/-18.42 | 5.92 | 888 | 0.0551 | 0.88112 (-2.4) | 1.0 | 0.0 | 0.851 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2106 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=3) | -8.88/-0.57/-11.91 | 5.92 | 875 | 0.0549 | 0.71029 (-2.32) | 1.0 | 0.0001 | 0.7675 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2107 | BROAD|donchian(entry_n=20,exit_n=10)+day_of_week(days=4) | -9.56/-0.75/-10.62 | 5.92 | 871 | 0.055 | 0.72927 (-1.48) | 1.0 | 0.0 | 0.7575 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2108 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=0) | -4.54/-0.29/-6.91 | 5.92 | 1078 | 0.0533 | 0.4955 (-4.1) | 1.0 | 0.0004 | 0.691 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2109 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=1) | -2.99/-0.17/-10.34 | 5.92 | 1202 | 0.054 | 0.45954 (-4.79) | 1.0 | 0.0009 | 0.688 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2110 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=2) | -17.17/-1.02/-18.62 | 5.92 | 1195 | 0.0543 | 0.85115 (-4.6) | 1.0 | 0.0 | 0.8665 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2111 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=3) | -15.98/-0.85/-22.56 | 5.92 | 1187 | 0.0537 | 0.83916 (-4.0) | 1.0 | 0.0 | 0.8655 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2112 | BROAD|donchian(entry_n=20,exit_n=20)+day_of_week(days=4) | -17.28/-1.13/-18.35 | 5.92 | 1179 | 0.0537 | 0.85015 (-3.97) | 1.0 | 0.0 | 0.8455 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2113 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=0) | -4.24/-0.48/-7.78 | 5.92 | 510 | 0.0559 | 0.61738 (-0.38) | 1.0 | 0.0001 | 0.6915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2114 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=1) | -0.12/0.0/-4.97 | 5.92 | 576 | 0.0558 | 0.51449 (0.02) | 1.0 | 0.0023 | 0.6565 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2115 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=2) | -4.86/-0.55/-7.35 | 5.92 | 561 | 0.0565 | 0.63137 (-0.44) | 1.0 | 0.0 | 0.714 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2116 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=3) | 4.15/0.35/-4.15 | 5.92 | 557 | 0.0567 | 0.36563 (-0.08) | 1.0 | 0.0103 | 0.5765 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2117 | BROAD|donchian(entry_n=55,exit_n=10)+day_of_week(days=4) | -9.87/-0.99/-11.08 | 5.92 | 548 | 0.0561 | 0.80719 (0.45) | 1.0 | 0.0 | 0.7635 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2118 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=0) | -4.58/-0.45/-7.33 | 5.92 | 685 | 0.0563 | 0.60539 (-1.19) | 1.0 | 0.0001 | 0.696 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2119 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=1) | 1.33/0.13/-4.55 | 5.92 | 773 | 0.0559 | 0.3986 (-2.34) | 1.0 | 0.0044 | 0.628 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2120 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=2) | -4.49/-0.36/-9.06 | 5.92 | 766 | 0.0563 | 0.57143 (-2.41) | 1.0 | 0.0002 | 0.714 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2121 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=3) | 3.15/0.24/-9.03 | 5.92 | 756 | 0.0565 | 0.35864 (-1.18) | 1.0 | 0.0068 | 0.5955 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2122 | BROAD|donchian(entry_n=55,exit_n=20)+day_of_week(days=4) | -13.83/-1.19/-16.45 | 5.92 | 743 | 0.0555 | 0.86214 (-0.84) | 1.0 | 0.0 | 0.8085 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2122

## Engine prereg 20261024_080332_gen_2610240804_000 (gen_2610240804_000, sha256 701035cf6902): rows #2123-2142 RESERVED (20 variants). Counted in N.
N_cumulative: 2142

## Engine run 20261024_080332_gen_2610240804_000 (gen_2610240804_000): rows #2123-2142. 0/20 pass. PBO 0.5. Bar applied at N=2142. Report: engine/runs/20261024_080332_gen_2610240804_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2123 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=0) | -26.56/-1.26/-31.06 | 428.6 | 696 | 0.1057 | 0.98801 (72.42) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2124 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=1) | -13.62/-0.57/-21.88 | 428.6 | 659 | 0.0945 | 0.96404 (88.6) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2125 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=2) | 22.77/1.09/-11.1 | 428.6 | 681 | 0.0938 | 0.71728 (128.41) | 1.0 | 0.0189 | 0.8915 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2126 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=3) | -0.93/0.04/-20.07 | 428.6 | 634 | 0.0925 | 0.91608 (164.25) | 1.0 | 0.0008 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2127 | crypto|supertrend(atr_n=7,mult=2)+day_of_week(days=4) | -12.18/-0.59/-13.7 | 428.6 | 622 | 0.0918 | 0.94905 (155.53) | 1.0 | 0.0001 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2128 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=0) | -29.11/-1.44/-33.83 | 428.6 | 498 | 0.1132 | 0.996 (70.6) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2129 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=1) | -9.62/-0.41/-22.16 | 428.6 | 464 | 0.0987 | 0.95205 (201.39) | 1.0 | 0.0002 | 0.915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2130 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=2) | 12.72/0.71/-10.78 | 428.6 | 500 | 0.0963 | 0.81219 (110.32) | 1.0 | 0.0079 | 0.8995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2131 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=3) | 5.42/0.3/-13.41 | 428.6 | 460 | 0.0942 | 0.87612 (114.66) | 1.0 | 0.002 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2132 | crypto|supertrend(atr_n=7,mult=4)+day_of_week(days=4) | -4.88/-0.25/-12.38 | 428.6 | 443 | 0.098 | 0.93207 (76.6) | 1.0 | 0.0003 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2133 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=0) | -22.42/-0.99/-27.47 | 428.6 | 710 | 0.1058 | 0.98501 (110.4) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2134 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=1) | -13.95/-0.6/-23.15 | 428.6 | 660 | 0.0932 | 0.96404 (161.65) | 1.0 | 0.0001 | 0.9145 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2135 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=2) | 27.59/1.24/-10.54 | 428.6 | 686 | 0.0932 | 0.67832 (97.57) | 1.0 | 0.0288 | 0.884 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2136 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=3) | -5.34/-0.16/-22.24 | 428.6 | 639 | 0.0922 | 0.92507 (161.21) | 1.0 | 0.0005 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2137 | crypto|supertrend(atr_n=10,mult=2)+day_of_week(days=4) | -7.04/-0.3/-13.48 | 428.6 | 616 | 0.0922 | 0.93407 (190.06) | 1.0 | 0.0002 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2138 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=0) | -28.3/-1.39/-33.08 | 428.6 | 495 | 0.1136 | 0.996 (91.27) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2139 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=1) | -13.21/-0.61/-23.36 | 428.6 | 463 | 0.0992 | 0.96404 (83.0) | 1.0 | 0.0001 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2140 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=2) | 10.88/0.62/-11.57 | 428.6 | 500 | 0.0971 | 0.81419 (72.4) | 1.0 | 0.0061 | 0.901 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2141 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=3) | 4.35/0.26/-15.89 | 428.6 | 462 | 0.0939 | 0.88212 (187.67) | 1.0 | 0.0017 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2142 | crypto|supertrend(atr_n=10,mult=4)+day_of_week(days=4) | -7.63/-0.42/-13.2 | 428.6 | 448 | 0.0987 | 0.94505 (182.04) | 1.0 | 0.0001 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2142

## Engine prereg 20261024_080353_gen_2610240805_000 (gen_2610240805_000, sha256 fdf6867d378e): rows #2143-2150 RESERVED (8 variants). Counted in N.
N_cumulative: 2150

## Engine run 20261024_080353_gen_2610240805_000 (gen_2610240805_000): rows #2143-2150. 0/8 pass. PBO 0.514. Bar applied at N=2150. Report: engine/runs/20261024_080353_gen_2610240805_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2143 | crypto|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=200) | 9.64/0.48/-11.27 | 56.21 | 76 | 0.0183 | 0.72128 (27.23) | 1.0 | 0.0897 | 0.82 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2144 | crypto|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | 4.71/0.27/-12.71 | 56.21 | 82 | 0.0192 | 0.75524 (26.89) | 1.0 | 0.0557 | 0.859 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2145 | crypto|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | -5.31/-0.11/-12.9 | 56.21 | 71 | 0.0183 | 0.83716 (25.11) | 1.0 | 0.0215 | 0.8935 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2146 | crypto|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 21.99/0.74/-14.45 | 56.21 | 83 | 0.0191 | 0.53946 (26.62) | 1.0 | 0.1496 | 0.792 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2147 | crypto|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=200) | 10.11/0.9/-2.83 | 56.21 | 20 | 0.0159 | 0.72428 (25.91) | 1.0 | 0.1402 | 0.818 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2148 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=200) | 24.96/1.32/-5.89 | 56.21 | 28 | 0.0171 | 0.53546 (28.57) | 1.0 | 0.3531 | 0.746 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2149 | crypto|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=200) | 8.04/0.56/-7.17 | 56.21 | 22 | 0.0161 | 0.76024 (27.76) | 1.0 | 0.096 | 0.8255 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2150 | crypto|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=200) | 21.82/1.05/-7.17 | 56.21 | 29 | 0.0176 | 0.58242 (27.28) | 1.0 | 0.242 | 0.76 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2150

## Engine prereg 20261024_080355_gen_2610240806_000 (gen_2610240806_000, sha256 96177cf1128a): rows #2151-2158 RESERVED (8 variants). Counted in N.
N_cumulative: 2158

## Engine run 20261024_080355_gen_2610240806_000 (gen_2610240806_000): rows #2151-2158. 0/8 pass. PBO 0.147. Bar applied at N=2158. Report: engine/runs/20261024_080355_gen_2610240806_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2151 | sectors|rsi_revert(entry=10,exit=60,n=2) | 15.83/0.8/-5.08 | 50.2 | 993 | 0.0698 | 0.71429 (19.51) | 1.0 | 0.5813 | 0.9615 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2152 | sectors|rsi_revert(entry=10,exit=60,n=5) | 3.83/0.64/-1.67 | 50.2 | 81 | 0.0631 | 0.99401 (23.24) | 1.0 | 0.4552 | 0.5 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2153 | sectors|rsi_revert(entry=10,exit=80,n=2) | 24.64/1.02/-5.5 | 50.2 | 843 | 0.0711 | 0.18981 (19.78) | 1.0 | 0.7328 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2154 | sectors|rsi_revert(entry=10,exit=80,n=5) | 11.32/1.19/-2.1 | 50.2 | 77 | 0.0633 | 0.92707 (23.07) | 1.0 | 0.8271 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2155 | sectors|rsi_revert(entry=20,exit=60,n=2) | 16.85/0.73/-8.14 | 50.2 | 1652 | 0.0701 | 0.46953 (16.52) | 1.0 | 0.5152 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2156 | sectors|rsi_revert(entry=20,exit=60,n=5) | 22.63/1.09/-4.87 | 50.2 | 354 | 0.0656 | 0.44056 (21.84) | 1.0 | 0.7936 | 0.9185 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2157 | sectors|rsi_revert(entry=20,exit=80,n=2) | 28.11/0.99/-10.59 | 50.2 | 1283 | 0.0709 | 0.04795 (18.03) | 1.0 | 0.6968 | 0.95 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2158 | sectors|rsi_revert(entry=20,exit=80,n=5) | 33.87/1.16/-10.14 | 50.2 | 251 | 0.0684 | 0.03497 (21.96) | 1.0 | 0.791 | 0.8725 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

N_cumulative: 2158

## Engine prereg 20261024_080359_gen_2610240807_000 (gen_2610240807_000, sha256 28b3ebfb06b9): rows #2159-2166 RESERVED (8 variants). Counted in N.
N_cumulative: 2166

## Engine run 20261024_080359_gen_2610240807_000 (gen_2610240807_000): rows #2159-2166. 0/8 pass. PBO 0.206. Bar applied at N=2166. Report: engine/runs/20261024_080359_gen_2610240807_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2159 | BROAD|drop_revert(drop=0.05,hold=3,n=1) | -14.73/-0.69/-17.79 | 5.92 | 159 | 0.0202 | 0.88511 (2.74) | 1.0 | 0.0 | 0.8665 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2160 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 3.68/0.17/-18.78 | 5.92 | 316 | 0.032 | 0.44555 (1.55) | 1.0 | 0.0047 | 0.6075 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2161 | BROAD|drop_revert(drop=0.05,hold=10,n=1) | -8.67/-0.25/-27.86 | 5.92 | 98 | 0.0228 | 0.75325 (2.13) | 1.0 | 0.0005 | 0.803 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2162 | BROAD|drop_revert(drop=0.05,hold=10,n=5) | 5.09/0.19/-19.18 | 5.92 | 208 | 0.0375 | 0.40959 (2.91) | 1.0 | 0.0053 | 0.5715 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2163 | BROAD|drop_revert(drop=0.15,hold=3,n=1) | -3.05/-0.94/-3.24 | 5.92 | 6 | 0.0118 | 0.60539 (3.23) | 1.0 | 0.0 | 0.682 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2164 | BROAD|drop_revert(drop=0.15,hold=3,n=5) | 3.34/0.3/-6.33 | 5.92 | 36 | 0.0149 | 0.48751 (2.66) | 1.0 | 0.0088 | 0.5995 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2165 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | -3.17/-0.72/-3.72 | 5.92 | 5 | 0.0122 | 0.58242 (1.86) | 1.0 | 0.0 | 0.683 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2166 | BROAD|drop_revert(drop=0.15,hold=10,n=5) | -9.82/-0.59/-17.76 | 5.92 | 28 | 0.0164 | 0.7962 (3.72) | 1.0 | 0.0 | 0.796 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2166

## Engine prereg 20261024_080402_gen_2610240808_000 (gen_2610240808_000, sha256 b035e50230d9): rows #2167-2170 RESERVED (4 variants). Counted in N.
N_cumulative: 2170

## Engine run 20261024_080402_gen_2610240808_000 (gen_2610240808_000): rows #2167-2170. 0/4 pass. PBO 0.579. Bar applied at N=2170. Report: engine/runs/20261024_080402_gen_2610240808_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2167 | crypto|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 197.99/0.81/-35.0 | 428.6 | 1994 | 0.1011 | 0.35265 (106.38) | 1.0 | 0.9096 | 0.5085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2168 | crypto|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 185.89/0.8/-46.24 | 428.6 | 1618 | 0.0983 | 0.4046 (146.76) | 1.0 | 0.9014 | 0.5015 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2169 | crypto|donchian(entry_n=100,exit_n=10)+rsi_band(hi=80) | 302.2/0.91/-14.37 | 428.6 | 963 | 0.0961 | 0.17183 (66.37) | 1.0 | 0.9643 | 0.904 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2170 | crypto|donchian(entry_n=100,exit_n=20)+rsi_band(hi=80) | 302.89/0.92/-22.62 | 428.6 | 833 | 0.0947 | 0.18881 (92.05) | 1.0 | 0.9637 | 0.9115 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

N_cumulative: 2170

## Engine prereg 20261024_080407_gen_2610240809_000 (gen_2610240809_000, sha256 2d451de6e9b5): rows #2171-2174 RESERVED (4 variants). Counted in N.
N_cumulative: 2174

## Engine run 20261024_080407_gen_2610240809_000 (gen_2610240809_000): rows #2171-2174. 0/4 pass. PBO 0.896. Bar applied at N=2174. Report: engine/runs/20261024_080407_gen_2610240809_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2171 | crypto|donchian(entry_n=20,exit_n=10) | 6.16/0.29/-23.85 | 56.21 | 48 | 0.0223 | 0.73526 (28.33) | 1.0 | 0.1155 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2172 | crypto|donchian(entry_n=20,exit_n=20) | 24.86/0.62/-26.12 | 56.21 | 34 | 0.0221 | 0.50749 (27.16) | 1.0 | 0.2092 | 0.824 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2173 | crypto|donchian(entry_n=55,exit_n=10) | 38.79/1.02/-15.0 | 56.21 | 28 | 0.0218 | 0.3966 (28.03) | 1.0 | 0.3716 | 0.7445 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2174 | crypto|donchian(entry_n=55,exit_n=20) | 45.08/1.08/-14.84 | 56.21 | 24 | 0.0218 | 0.33566 (27.81) | 1.0 | 0.3991 | 0.7205 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

N_cumulative: 2174

## Engine prereg 20261024_080409_gen_2610240810_000 (gen_2610240810_000, sha256 209f7a916cc1): rows #2175-2178 RESERVED (4 variants). Counted in N.
N_cumulative: 2178

## Engine run 20261024_080409_gen_2610240810_000 (gen_2610240810_000): rows #2175-2178. 0/4 pass. PBO 0.032. Bar applied at N=2178. Report: engine/runs/20261024_080409_gen_2610240810_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2175 | sectors|sma_cross(fast=5,slow=50)+trend_sma(n=50) | 8.03/0.38/-9.03 | 50.2 | 584 | 0.0662 | 0.97502 (20.39) | 1.0 | 0.2612 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2176 | sectors|sma_cross(fast=5,slow=150)+trend_sma(n=50) | 3.66/0.21/-8.71 | 50.2 | 643 | 0.0679 | 0.997 (19.85) | 1.0 | 0.1732 | 0.4905 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2177 | sectors|sma_cross(fast=50,slow=50)+trend_sma(n=50) | 0.0/0.0/0.0 | 50.2 | 0 | inf | 1.0 (23.52) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2178 | sectors|sma_cross(fast=50,slow=150)+trend_sma(n=50) | -1.42/-0.05/-7.64 | 50.2 | 610 | 0.0692 | 1.0 (20.39) | 1.0 | 0.0826 | 0.511 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2178

## Engine prereg 20261024_080412_gen_2610240811_000 (gen_2610240811_000, sha256 cc1c34a66bcb): rows #2179-2186 RESERVED (8 variants). Counted in N.
N_cumulative: 2186

## Engine run 20261024_080412_gen_2610240811_000 (gen_2610240811_000): rows #2179-2186. 0/8 pass. PBO 0.254. Bar applied at N=2186. Report: engine/runs/20261024_080412_gen_2610240811_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2179 | BROAD|rsi_revert(entry=10,exit=60,n=2)+vol_regime(max_atr_pct=0.04) | 17.93/1.01/-4.3 | 5.92 | 448 | 0.053 | 0.10589 (0.58) | 1.0 | 0.4172 | 0.4015 | False | cost_stop, holm, dsr, spa |
| 2180 | BROAD|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.04) | 18.46/1.36/-4.15 | 5.92 | 180 | 0.0495 | 0.0999 (1.28) | 1.0 | 0.6774 | 0.399 | False | cost_stop, holm, dsr, spa |
| 2181 | BROAD|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.04) | 22.42/1.11/-4.19 | 5.92 | 432 | 0.0526 | 0.04795 (-0.4) | 1.0 | 0.493 | 0.357 | False | cost_stop, holm, dsr, spa |
| 2182 | BROAD|rsi_revert(entry=10,exit=70,n=3)+vol_regime(max_atr_pct=0.04) | 25.28/1.6/-3.88 | 5.92 | 174 | 0.0476 | 0.04895 (1.99) | 1.0 | 0.8206 | 0.322 | False | cost_stop, holm, dsr, spa |
| 2183 | BROAD|rsi_revert(entry=20,exit=60,n=2)+vol_regime(max_atr_pct=0.04) | 19.15/0.89/-5.83 | 5.92 | 704 | 0.0539 | 0.07992 (-1.06) | 1.0 | 0.3392 | 0.3895 | False | cost_stop, holm, dsr, spa |
| 2184 | BROAD|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.04) | 32.22/1.46/-4.52 | 5.92 | 399 | 0.0524 | 0.01499 (0.9) | 1.0 | 0.7312 | 0.266 | False | cost_stop, holm, dsr, spa |
| 2185 | BROAD|rsi_revert(entry=20,exit=70,n=2)+vol_regime(max_atr_pct=0.04) | 23.16/0.99/-6.21 | 5.92 | 659 | 0.0534 | 0.04795 (-0.86) | 1.0 | 0.4042 | 0.348 | False | cost_stop, holm, dsr, spa |
| 2186 | BROAD|rsi_revert(entry=20,exit=70,n=3)+vol_regime(max_atr_pct=0.04) | 47.31/1.78/-4.14 | 5.92 | 365 | 0.0522 | 0.003 (-0.1) | 1.0 | 0.8794 | 0.142 | False | cost_stop, holm, dsr, spa |

N_cumulative: 2186

## Engine prereg 20261024_091132_gen_2610240900_000 (gen_2610240900_000, sha256 526c23dbfc82): rows #2187-2190 RESERVED (4 variants). Counted in N.
N_cumulative: 2190

## Engine run 20261024_091132_gen_2610240900_000 (gen_2610240900_000): rows #2187-2190. 0/4 pass. PBO 0.491. Bar applied at N=2190. Report: engine/runs/20261024_091132_gen_2610240900_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2187 | crypto|donchian(entry_n=20,exit_n=10) | 6.16/0.29/-23.85 | 56.21 | 48 | 0.0223 | 0.72228 (25.71) | 1.0 | 0.4089 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2188 | crypto|donchian(entry_n=20,exit_n=20) | 24.86/0.62/-26.12 | 56.21 | 34 | 0.0221 | 0.49351 (25.77) | 1.0 | 0.5665 | 0.824 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2189 | crypto|donchian(entry_n=100,exit_n=10) | 13.94/0.52/-18.64 | 56.21 | 20 | 0.0224 | 0.67433 (28.7) | 1.0 | 0.5184 | 0.8355 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2190 | crypto|donchian(entry_n=100,exit_n=20) | 12.91/0.47/-23.93 | 56.21 | 18 | 0.0224 | 0.63736 (25.52) | 1.0 | 0.4957 | 0.8415 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2190

## Engine prereg 20261024_091137_gen_2610240901_000 (gen_2610240901_000, sha256 277b14e348f6): rows #2191-2194 RESERVED (4 variants). Counted in N.
N_cumulative: 2194

## Engine run 20261024_091137_gen_2610240901_000 (gen_2610240901_000): rows #2191-2194. 0/4 pass. PBO 0.798. Bar applied at N=2194. Report: engine/runs/20261024_091137_gen_2610240901_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2191 | crypto|sma_cross(fast=5,slow=50) | 23.53/0.59/-26.67 | 434.62 | 71 | 0.019 | 0.77323 (155.02) | 1.0 | 0.4452 | 0.9025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2192 | crypto|sma_cross(fast=5,slow=200) | 7.15/0.31/-24.64 | 434.62 | 23 | 0.0205 | 0.85315 (227.64) | 1.0 | 0.3189 | 0.9085 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2193 | crypto|sma_cross(fast=20,slow=50) | 29.11/0.67/-23.71 | 434.62 | 50 | 0.0202 | 0.77822 (201.97) | 1.0 | 0.486 | 0.903 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2194 | crypto|sma_cross(fast=20,slow=200) | 4.8/0.26/-21.46 | 434.62 | 15 | 0.0209 | 0.82218 (92.36) | 1.0 | 0.2997 | 0.9135 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2194

## Engine prereg 20261024_091142_gen_2610240902_000 (gen_2610240902_000, sha256 fce0f1616153): rows #2195-2198 RESERVED (4 variants). Counted in N.
N_cumulative: 2198

## Engine run 20261024_091142_gen_2610240902_000 (gen_2610240902_000): rows #2195-2198. 0/4 pass. PBO 0.856. Bar applied at N=2198. Report: engine/runs/20261024_091142_gen_2610240902_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2195 | crypto|sma_cross(fast=10,slow=150)+rsi_band(hi=60) | 20.47/0.51/-39.25 | 31.3 | 52 | 0.0199 | 0.44456 (12.32) | 1.0 | 0.3196 | 0.6915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2196 | crypto|sma_cross(fast=10,slow=200)+rsi_band(hi=60) | -3.78/0.14/-44.58 | 31.3 | 49 | 0.0202 | 0.61738 (14.51) | 1.0 | 0.1825 | 0.807 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2197 | crypto|sma_cross(fast=50,slow=150)+rsi_band(hi=60) | 7.52/0.33/-45.78 | 31.3 | 46 | 0.02 | 0.53047 (13.61) | 1.0 | 0.2466 | 0.7265 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2198 | crypto|sma_cross(fast=50,slow=200)+rsi_band(hi=60) | -19.76/-0.09/-56.3 | 31.3 | 45 | 0.0195 | 0.73127 (13.09) | 1.0 | 0.1197 | 0.872 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2198

## Engine prereg 20261024_091146_gen_2610240903_000 (gen_2610240903_000, sha256 aca2c32e7956): rows #2199-2206 RESERVED (8 variants). Counted in N.
N_cumulative: 2206

## Engine run 20261024_091146_gen_2610240903_000 (gen_2610240903_000): rows #2199-2206. 0/8 pass. PBO 0.453. Bar applied at N=2206. Report: engine/runs/20261024_091146_gen_2610240903_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2199 | crypto|drop_revert(drop=0.1,hold=3,n=1) | 25.31/1.18/-6.2 | 41.29 | 31 | 0.008 | 0.41858 (16.58) | 1.0 | 0.0719 | 0.7325 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2200 | crypto|drop_revert(drop=0.1,hold=3,n=5) | -1.92/0.22/-37.63 | 41.29 | 69 | 0.0097 | 0.67133 (17.94) | 1.0 | 0.0174 | 0.8255 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2201 | crypto|drop_revert(drop=0.1,hold=5,n=1) | 15.99/0.69/-11.59 | 41.29 | 28 | 0.0081 | 0.51049 (17.82) | 1.0 | 0.0381 | 0.7595 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2202 | crypto|drop_revert(drop=0.1,hold=5,n=5) | -4.76/0.2/-39.37 | 41.29 | 61 | 0.01 | 0.65335 (16.42) | 1.0 | 0.0163 | 0.8295 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2203 | crypto|drop_revert(drop=0.15,hold=3,n=1) | -2.09/-0.24/-6.2 | 41.29 | 9 | 0.0069 | 0.93207 (18.52) | 1.0 | 0.0027 | 0.8425 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2204 | crypto|drop_revert(drop=0.15,hold=3,n=5) | 74.79/1.61/-15.21 | 41.29 | 41 | 0.0089 | 0.12787 (17.92) | 1.0 | 0.1914 | 0.5365 | False | min_trades, holm, dsr, spa |
| 2205 | crypto|drop_revert(drop=0.15,hold=5,n=1) | -2.47/-0.15/-6.64 | 41.29 | 9 | 0.0069 | 0.84316 (17.65) | 1.0 | 0.0067 | 0.8405 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2206 | crypto|drop_revert(drop=0.15,hold=5,n=5) | 10.91/0.43/-31.25 | 41.29 | 39 | 0.0089 | 0.57043 (17.86) | 1.0 | 0.0286 | 0.761 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2206

## Engine prereg 20261024_091148_gen_2610240904_000 (gen_2610240904_000, sha256 b971ce2a3371): rows #2207-2210 RESERVED (4 variants). Counted in N.
N_cumulative: 2210

## Engine run 20261024_091148_gen_2610240904_000 (gen_2610240904_000): rows #2207-2210. 0/4 pass. PBO 0.66. Bar applied at N=2210. Report: engine/runs/20261024_091148_gen_2610240904_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2207 | crypto|sma_cross(fast=5,slow=100)+rsi_band(hi=80) | 47.54/0.99/-24.09 | 72.28 | 23 | 0.0273 | 0.32468 (29.82) | 1.0 | 0.3664 | 0.806 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2208 | crypto|sma_cross(fast=5,slow=200)+rsi_band(hi=80) | -4.31/0.11/-39.91 | 72.28 | 21 | 0.0266 | 0.88611 (31.47) | 1.0 | 0.0818 | 0.5005 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2209 | crypto|sma_cross(fast=20,slow=100)+rsi_band(hi=80) | 21.44/0.57/-35.04 | 72.28 | 20 | 0.0275 | 0.57842 (28.42) | 1.0 | 0.1968 | 0.922 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2210 | crypto|sma_cross(fast=20,slow=200)+rsi_band(hi=80) | 33.85/0.7/-26.05 | 72.28 | 13 | 0.0273 | 0.45654 (30.29) | 1.0 | 0.2423 | 0.9115 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2210

## Engine prereg 20261024_091150_gen_2610240905_000 (gen_2610240905_000, sha256 84ede1718b13): rows #2211-2214 RESERVED (4 variants). Counted in N.
N_cumulative: 2214

## Engine run 20261024_091150_gen_2610240905_000 (gen_2610240905_000): rows #2211-2214. 0/4 pass. PBO 0.711. Bar applied at N=2214. Report: engine/runs/20261024_091150_gen_2610240905_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2211 | crypto|supertrend(atr_n=7,mult=2)+vol_regime(max_atr_pct=0.04) | 5.76/0.35/-9.35 | 637.22 | 38 | 0.0258 | 0.86813 (394.46) | 1.0 | 0.6149 | 0.912 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2212 | crypto|supertrend(atr_n=7,mult=4)+vol_regime(max_atr_pct=0.04) | 6.4/0.36/-13.47 | 637.22 | 31 | 0.0255 | 0.84815 (55.15) | 1.0 | 0.6224 | 0.915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2213 | crypto|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.04) | 6.25/0.37/-9.35 | 637.22 | 38 | 0.026 | 0.86513 (384.52) | 1.0 | 0.6253 | 0.9115 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2214 | crypto|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.04) | 5.08/0.3/-14.19 | 637.22 | 31 | 0.0255 | 0.87013 (52.01) | 1.0 | 0.594 | 0.9155 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2214

## Engine prereg 20261024_091153_gen_2610240906_000 (gen_2610240906_000, sha256 6eca92573028): rows #2215-2222 RESERVED (8 variants). Counted in N.
N_cumulative: 2222

## Engine run 20261024_091153_gen_2610240906_000 (gen_2610240906_000): rows #2215-2222. 0/8 pass. PBO 0.455. Bar applied at N=2222. Report: engine/runs/20261024_091153_gen_2610240906_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2215 | sectors|rsi_revert(entry=5,exit=70,n=2) | 13.47/0.75/-5.21 | 50.2 | 560 | 0.0683 | 0.90909 (20.63) | 1.0 | 0.663 | 0.9705 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2216 | sectors|rsi_revert(entry=5,exit=70,n=5) | 2.94/0.93/-0.86 | 50.2 | 22 | 0.0635 | 0.998 (22.68) | 1.0 | 0.7449 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2217 | sectors|rsi_revert(entry=5,exit=80,n=2) | 19.68/0.99/-4.72 | 50.2 | 532 | 0.0683 | 0.54246 (20.64) | 1.0 | 0.8223 | 0.937 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2218 | sectors|rsi_revert(entry=5,exit=80,n=5) | 4.69/1.29/-0.86 | 50.2 | 22 | 0.0635 | 0.99401 (23.19) | 1.0 | 0.9136 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2219 | sectors|rsi_revert(entry=10,exit=70,n=2) | 21.31/0.99/-5.61 | 50.2 | 941 | 0.0701 | 0.33267 (18.92) | 1.0 | 0.8105 | 0.9455 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2220 | sectors|rsi_revert(entry=10,exit=70,n=5) | 6.29/0.96/-1.66 | 50.2 | 79 | 0.0631 | 0.98801 (23.88) | 1.0 | 0.7607 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2221 | sectors|rsi_revert(entry=10,exit=80,n=2) | 24.64/1.02/-5.5 | 50.2 | 843 | 0.0711 | 0.2048 (20.01) | 1.0 | 0.8159 | 0.933 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2222 | sectors|rsi_revert(entry=10,exit=80,n=5) | 11.32/1.19/-2.1 | 50.2 | 77 | 0.0633 | 0.92108 (22.95) | 1.0 | 0.8887 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2222

## Engine prereg 20261024_091156_gen_2610240907_000 (gen_2610240907_000, sha256 7b2d4f4c76fc): rows #2223-2230 RESERVED (8 variants). Counted in N.
N_cumulative: 2230

## Engine run 20261024_091156_gen_2610240907_000 (gen_2610240907_000): rows #2223-2230. 0/8 pass. PBO 0.047. Bar applied at N=2230. Report: engine/runs/20261024_091156_gen_2610240907_000/report.md

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

N_cumulative: 2230

## Engine prereg 20261024_091159_gen_2610240908_000 (gen_2610240908_000, sha256 da98888f8833): rows #2231-2238 RESERVED (8 variants). Counted in N.
N_cumulative: 2238

## Engine run 20261024_091159_gen_2610240908_000 (gen_2610240908_000): rows #2231-2238. 0/8 pass. PBO 0.531. Bar applied at N=2238. Report: engine/runs/20261024_091159_gen_2610240908_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2231 | index|rsi_revert(entry=5,exit=60,n=3)+vol_regime(max_atr_pct=0.02) | -0.41/-0.12/-1.83 | 75.73 | 42 | 0.0798 | 1.0 (33.69) | 1.0 | 0.003 | 0.494 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2232 | index|rsi_revert(entry=5,exit=60,n=5)+vol_regime(max_atr_pct=0.02) | 0.32/0.22/-0.81 | 75.73 | 5 | 0.0877 | 0.98801 (33.84) | 1.0 | 0.0149 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2233 | index|rsi_revert(entry=5,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 1.53/0.42/-1.83 | 75.73 | 43 | 0.0718 | 1.0 (32.78) | 1.0 | 0.0342 | 0.494 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2234 | index|rsi_revert(entry=5,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 0.58/0.39/-0.81 | 75.73 | 5 | 0.0877 | 0.98501 (34.8) | 1.0 | 0.0286 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2235 | index|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.02) | 13.16/0.8/-6.52 | 75.73 | 307 | 0.0836 | 0.97802 (30.15) | 1.0 | 0.1222 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2236 | index|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.02) | 12.63/1.01/-6.17 | 75.73 | 126 | 0.0736 | 0.98501 (32.48) | 1.0 | 0.214 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2237 | index|rsi_revert(entry=20,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 18.58/0.92/-8.09 | 75.73 | 286 | 0.0843 | 0.9041 (30.33) | 1.0 | 0.1637 | 0.509 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2238 | index|rsi_revert(entry=20,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 17.61/1.07/-6.4 | 75.73 | 132 | 0.0705 | 0.94306 (31.81) | 1.0 | 0.2415 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2238

## Engine prereg 20261024_091203_gen_2610240909_000 (gen_2610240909_000, sha256 3fdb7bafe293): rows #2239-2242 RESERVED (4 variants). Counted in N.
N_cumulative: 2242

## Engine run 20261024_091203_gen_2610240909_000 (gen_2610240909_000): rows #2239-2242. 0/4 pass. PBO 0.863. Bar applied at N=2242. Report: engine/runs/20261024_091203_gen_2610240909_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2239 | megacap|supertrend(atr_n=7,mult=2) | 157.58/1.9/-15.61 | 311.91 | 395 | 0.041 | 0.02498 (103.38) | 1.0 | 0.993 | 0.475 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2240 | megacap|supertrend(atr_n=7,mult=4) | 123.46/1.61/-11.54 | 311.91 | 141 | 0.0405 | 0.24875 (106.6) | 1.0 | 0.9715 | 0.505 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2241 | megacap|supertrend(atr_n=10,mult=2) | 164.25/1.93/-16.52 | 311.91 | 394 | 0.0404 | 0.01499 (103.27) | 1.0 | 0.994 | 0.469 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2242 | megacap|supertrend(atr_n=10,mult=4) | 136.31/1.73/-11.04 | 311.91 | 143 | 0.0405 | 0.13087 (105.63) | 1.0 | 0.9829 | 0.503 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

N_cumulative: 2242

## Engine prereg 20261024_091206_gen_2610240910_000 (gen_2610240910_000, sha256 01e672489b32): rows #2243-2246 RESERVED (4 variants). Counted in N.
N_cumulative: 2246

## Engine run 20261024_091206_gen_2610240910_000 (gen_2610240910_000): rows #2243-2246. 0/4 pass. PBO 0.135. Bar applied at N=2246. Report: engine/runs/20261024_091206_gen_2610240910_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2243 | index|sma_cross(fast=10,slow=50)+trend_sma(n=200) | 41.23/1.07/-10.59 | 107.42 | 58 | 0.0679 | 0.53447 (43.88) | 1.0 | 0.7775 | 0.5205 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2244 | index|sma_cross(fast=10,slow=200)+trend_sma(n=200) | 67.91/1.4/-10.87 | 107.42 | 27 | 0.0561 | 0.16384 (45.59) | 1.0 | 0.9034 | 0.9305 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2245 | index|sma_cross(fast=50,slow=50)+trend_sma(n=200) | 0.0/0.0/0.0 | 107.42 | 0 | inf | 1.0 (54.95) | 1.0 | 0.0 | 0.4835 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2246 | index|sma_cross(fast=50,slow=200)+trend_sma(n=200) | 63.29/1.37/-10.89 | 107.42 | 34 | 0.0563 | 0.26474 (46.7) | 1.0 | 0.8967 | 0.945 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2246

## Engine prereg 20261024_091208_gen_2610240911_000 (gen_2610240911_000, sha256 fee0f29db860): rows #2247-2250 RESERVED (4 variants). Counted in N.
N_cumulative: 2250

## Engine run 20261024_091208_gen_2610240911_000 (gen_2610240911_000): rows #2247-2250. 0/4 pass. PBO 0.508. Bar applied at N=2250. Report: engine/runs/20261024_091208_gen_2610240911_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2247 | sectors|supertrend(atr_n=10,mult=2) | 40.09/1.15/-11.25 | 90.03 | 258 | 0.0562 | 0.35964 (36.21) | 1.0 | 0.7384 | 0.486 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2248 | sectors|supertrend(atr_n=10,mult=4) | 22.32/0.75/-8.16 | 90.03 | 97 | 0.0553 | 0.9001 (37.68) | 1.0 | 0.4819 | 0.522 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2249 | sectors|supertrend(atr_n=14,mult=2) | 40.86/1.14/-12.96 | 90.03 | 261 | 0.0561 | 0.32567 (36.04) | 1.0 | 0.7314 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2250 | sectors|supertrend(atr_n=14,mult=4) | 24.08/0.77/-9.77 | 90.03 | 93 | 0.0551 | 0.87113 (38.16) | 1.0 | 0.4967 | 0.528 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2250

## Engine prereg 20261024_091211_gen_2610240913_000 (gen_2610240913_000, sha256 07a36bf4a244): rows #2251-2254 RESERVED (4 variants). Counted in N.
N_cumulative: 2254

## Engine run 20261024_091211_gen_2610240913_000 (gen_2610240913_000): rows #2251-2254. 0/4 pass. PBO 0.748. Bar applied at N=2254. Report: engine/runs/20261024_091211_gen_2610240913_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2251 | crypto|donchian(entry_n=20,exit_n=10) | 3.84/0.24/-19.06 | 434.62 | 66 | 0.02 | 0.90509 (171.24) | 1.0 | 0.354 | 0.912 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2252 | crypto|donchian(entry_n=20,exit_n=20) | 24.28/0.6/-25.97 | 434.62 | 46 | 0.0198 | 0.77123 (121.4) | 1.0 | 0.5253 | 0.907 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2253 | crypto|donchian(entry_n=55,exit_n=10) | 8.89/0.36/-22.01 | 434.62 | 39 | 0.0203 | 0.87712 (189.33) | 1.0 | 0.4107 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2254 | crypto|donchian(entry_n=55,exit_n=20) | 15.81/0.49/-26.31 | 434.62 | 32 | 0.0201 | 0.82617 (111.18) | 1.0 | 0.4714 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2254

## Engine prereg 20261024_091213_gen_2610240914_000 (gen_2610240914_000, sha256 fc05a8b15ee5): rows #2255-2262 RESERVED (8 variants). Counted in N.
N_cumulative: 2262

## Engine run 20261024_091213_gen_2610240914_000 (gen_2610240914_000): rows #2255-2262. 0/8 pass. PBO 0.386. Bar applied at N=2262. Report: engine/runs/20261024_091213_gen_2610240914_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2255 | index|drop_revert(drop=0.05,hold=3,n=1) | 2.22/0.19/-2.67 | 84.67 | 13 | 0.0375 | 0.99201 (36.7) | 1.0 | 0.0168 | 0.489 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2256 | index|drop_revert(drop=0.05,hold=3,n=3) | 16.45/0.74/-4.28 | 84.67 | 80 | 0.0406 | 0.8981 (36.09) | 1.0 | 0.0938 | 0.973 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2257 | index|drop_revert(drop=0.05,hold=10,n=1) | 2.51/0.15/-5.31 | 84.67 | 11 | 0.0385 | 0.99001 (36.43) | 1.0 | 0.0179 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2258 | index|drop_revert(drop=0.05,hold=10,n=3) | 26.89/1.02/-5.69 | 84.67 | 62 | 0.0438 | 0.73626 (36.21) | 1.0 | 0.269 | 0.927 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2259 | index|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 84.67 | 3 | 0.0175 | 1.0 (34.39) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2260 | index|drop_revert(drop=0.1,hold=3,n=3) | 2.02/0.13/-4.63 | 84.67 | 11 | 0.0277 | 0.997 (37.9) | 1.0 | 0.0174 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2261 | index|drop_revert(drop=0.1,hold=10,n=1) | 0.0/0.0/0.0 | 84.67 | 3 | 0.0175 | 1.0 (40.44) | 1.0 | 0.0 | 0.497 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2262 | index|drop_revert(drop=0.1,hold=10,n=3) | 6.39/0.31/-5.69 | 84.67 | 9 | 0.0281 | 0.98601 (35.92) | 1.0 | 0.0306 | 0.483 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2262

## Engine prereg 20261024_091216_gen_2610240915_000 (gen_2610240915_000, sha256 9b85522a2c85): rows #2263-2266 RESERVED (4 variants). Counted in N.
N_cumulative: 2266

## Engine run 20261024_091216_gen_2610240915_000 (gen_2610240915_000): rows #2263-2266. 0/4 pass. PBO 0.879. Bar applied at N=2266. Report: engine/runs/20261024_091216_gen_2610240915_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2263 | megacap|supertrend(atr_n=7,mult=2) | 138.59/1.72/-20.27 | 273.72 | 260 | 0.0404 | 0.06693 (92.1) | 1.0 | 0.9597 | 0.4915 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2264 | megacap|supertrend(atr_n=7,mult=4) | 91.79/1.31/-16.01 | 273.72 | 98 | 0.0419 | 0.51748 (96.34) | 1.0 | 0.8511 | 0.511 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2265 | megacap|supertrend(atr_n=10,mult=2) | 146.25/1.75/-21.28 | 273.72 | 263 | 0.0403 | 0.04196 (90.14) | 1.0 | 0.9645 | 0.4805 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2266 | megacap|supertrend(atr_n=10,mult=4) | 108.34/1.5/-16.14 | 273.72 | 98 | 0.0414 | 0.33167 (95.45) | 1.0 | 0.9135 | 0.5115 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2266

## Engine prereg 20261024_091219_gen_2610240916_000 (gen_2610240916_000, sha256 42d81797515f): rows #2267-2270 RESERVED (4 variants). Counted in N.
N_cumulative: 2270

## Engine run 20261024_091219_gen_2610240916_000 (gen_2610240916_000): rows #2267-2270. 0/4 pass. PBO 0.71. Bar applied at N=2270. Report: engine/runs/20261024_091219_gen_2610240916_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2267 | BROAD|donchian(entry_n=55,exit_n=10) | 0.41/0.05/-8.63 | 33.23 | 66 | 0.101 | 0.97203 (14.55) | 1.0 | 0.0197 | 0.4895 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2268 | BROAD|donchian(entry_n=55,exit_n=20) | 7.36/0.43/-6.86 | 33.23 | 49 | 0.0979 | 0.83616 (14.36) | 1.0 | 0.0807 | 0.483 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2269 | BROAD|donchian(entry_n=100,exit_n=10) | 3.06/0.27/-5.82 | 33.23 | 53 | 0.1036 | 0.97003 (14.81) | 1.0 | 0.0472 | 0.4965 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2270 | BROAD|donchian(entry_n=100,exit_n=20) | 13.34/0.9/-4.34 | 33.23 | 37 | 0.1031 | 0.66134 (15.49) | 1.0 | 0.2756 | 0.9575 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2270

## Engine prereg 20261024_100927_gen_2610241000_000 (gen_2610241000_000, sha256 5a8bf8024b45): rows #2271-2278 RESERVED (8 variants). Counted in N.
N_cumulative: 2278

## Engine run 20261024_100927_gen_2610241000_000 (gen_2610241000_000): rows #2271-2278. 0/8 pass. PBO 0.75. Bar applied at N=2278. Report: engine/runs/20261024_100927_gen_2610241000_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2271 | crypto|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=200) | 10.39/0.5/-9.6 | 434.62 | 103 | 0.0169 | 0.80519 (227.2) | 1.0 | 0.1066 | 0.8965 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2272 | crypto|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | -5.19/-0.12/-13.14 | 434.62 | 106 | 0.0175 | 0.94306 (258.43) | 1.0 | 0.0276 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2273 | crypto|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | -4.54/-0.08/-13.06 | 434.62 | 92 | 0.0172 | 0.92108 (232.92) | 1.0 | 0.0298 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2274 | crypto|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 8.4/0.37/-14.26 | 434.62 | 103 | 0.0178 | 0.82817 (252.08) | 1.0 | 0.085 | 0.905 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2275 | crypto|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=200) | 8.0/0.84/-1.96 | 434.62 | 7 | 0.0105 | 0.89011 (44.84) | 1.0 | 0.1071 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2276 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=200) | 12.17/1.16/-1.96 | 434.62 | 16 | 0.0112 | 0.81518 (245.48) | 1.0 | 0.2505 | 0.896 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2277 | crypto|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=200) | 2.74/0.29/-6.67 | 434.62 | 7 | 0.0105 | 0.92408 (312.31) | 1.0 | 0.0562 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2278 | crypto|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=200) | 4.71/0.45/-6.67 | 434.62 | 16 | 0.0112 | 0.88312 (65.06) | 1.0 | 0.0784 | 0.9025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2278

## Engine prereg 20261024_100933_gen_2610241001_000 (gen_2610241001_000, sha256 1ed1ac17db85): rows #2279-2282 RESERVED (4 variants). Counted in N.
N_cumulative: 2282

## Engine run 20261024_100933_gen_2610241001_000 (gen_2610241001_000): rows #2279-2282. 0/4 pass. PBO 0.837. Bar applied at N=2282. Report: engine/runs/20261024_100933_gen_2610241001_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2279 | index|supertrend(atr_n=10,mult=2) | 57.8/1.35/-13.15 | 107.42 | 136 | 0.0734 | 0.15085 (41.06) | 1.0 | 0.9808 | 0.4875 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2280 | index|supertrend(atr_n=10,mult=4) | 52.07/1.29/-11.25 | 107.42 | 54 | 0.0728 | 0.27373 (43.94) | 1.0 | 0.9738 | 0.522 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2281 | index|supertrend(atr_n=14,mult=2) | 59.49/1.38/-13.51 | 107.42 | 140 | 0.0712 | 0.11688 (41.71) | 1.0 | 0.9833 | 0.978 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2282 | index|supertrend(atr_n=14,mult=4) | 56.84/1.36/-11.63 | 107.42 | 51 | 0.0647 | 0.1978 (43.55) | 1.0 | 0.9808 | 0.967 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

N_cumulative: 2282

## Engine prereg 20261024_100935_gen_2610241002_000 (gen_2610241002_000, sha256 ed090ef4ed38): rows #2283-2290 RESERVED (8 variants). Counted in N.
N_cumulative: 2290

## Engine run 20261024_100935_gen_2610241002_000 (gen_2610241002_000): rows #2283-2290. 0/8 pass. PBO 0.171. Bar applied at N=2290. Report: engine/runs/20261024_100935_gen_2610241002_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2283 | megacap|drop_revert(drop=0.05,hold=3,n=1) | -1.43/-0.07/-6.46 | 118.49 | 32 | 0.0288 | 0.998 (48.17) | 1.0 | 0.0115 | 0.4905 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2284 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 26.06/0.87/-6.6 | 118.49 | 93 | 0.0334 | 0.7982 (47.77) | 1.0 | 0.1474 | 0.974 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2285 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 6.46/0.41/-6.02 | 118.49 | 29 | 0.0329 | 0.97502 (49.04) | 1.0 | 0.032 | 0.5015 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2286 | megacap|drop_revert(drop=0.05,hold=5,n=3) | 34.21/0.97/-7.24 | 118.49 | 89 | 0.034 | 0.6963 (47.69) | 1.0 | 0.2081 | 0.957 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2287 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0135 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2288 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 9.6/0.6/-2.49 | 118.49 | 11 | 0.0244 | 0.92108 (58.62) | 1.0 | 0.048 | 0.4975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2289 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0135 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2290 | megacap|drop_revert(drop=0.1,hold=5,n=3) | 6.12/0.42/-2.49 | 118.49 | 9 | 0.025 | 0.95405 (57.16) | 1.0 | 0.0265 | 0.5 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2290

## Engine prereg 20261024_100939_gen_2610241003_000 (gen_2610241003_000, sha256 ac1069c72156): rows #2291-2294 RESERVED (4 variants). Counted in N.
N_cumulative: 2294

## Engine run 20261024_100939_gen_2610241003_000 (gen_2610241003_000): rows #2291-2294. 0/4 pass. PBO 0.855. Bar applied at N=2294. Report: engine/runs/20261024_100939_gen_2610241003_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2291 | sectors|sma_cross(fast=5,slow=100) | 34.35/0.84/-12.06 | 94.31 | 78 | 0.0566 | 0.5994 (38.7) | 1.0 | 0.7937 | 0.524 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2292 | sectors|sma_cross(fast=5,slow=150) | 38.78/0.91/-12.45 | 94.31 | 49 | 0.0558 | 0.50649 (40.36) | 1.0 | 0.8241 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2293 | sectors|sma_cross(fast=20,slow=100) | 47.23/1.09/-11.15 | 94.31 | 39 | 0.0605 | 0.26474 (40.06) | 1.0 | 0.8903 | 0.5195 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2294 | sectors|sma_cross(fast=20,slow=150) | 40.86/0.93/-13.98 | 94.31 | 32 | 0.0553 | 0.46753 (40.54) | 1.0 | 0.8318 | 0.515 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2294

## Engine prereg 20261024_100941_gen_2610241004_000 (gen_2610241004_000, sha256 3304fae26b5b): rows #2295-2298 RESERVED (4 variants). Counted in N.
N_cumulative: 2298

## Engine run 20261024_100941_gen_2610241004_000 (gen_2610241004_000): rows #2295-2298. 0/4 pass. PBO 0.409. Bar applied at N=2298. Report: engine/runs/20261024_100941_gen_2610241004_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2295 | BROAD|sma_cross(fast=5,slow=50)+relvol(min_ratio=1.0) | 1.59/0.11/-16.71 | 83.36 | 753 | 0.087 | 0.98202 (24.85) | 1.0 | 0.3211 | 0.501 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2296 | BROAD|sma_cross(fast=5,slow=100)+relvol(min_ratio=1.0) | 0.85/0.08/-15.26 | 83.36 | 770 | 0.0875 | 0.99101 (23.17) | 1.0 | 0.3025 | 0.4985 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2297 | BROAD|sma_cross(fast=50,slow=50)+relvol(min_ratio=1.0) | 0.0/0.0/0.0 | 83.36 | 0 | inf | 1.0 (38.63) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2298 | BROAD|sma_cross(fast=50,slow=100)+relvol(min_ratio=1.0) | 5.83/0.28/-12.75 | 83.36 | 724 | 0.0876 | 0.96004 (24.9) | 1.0 | 0.4317 | 0.4955 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2298

## Engine prereg 20261024_100944_gen_2610241005_000 (gen_2610241005_000, sha256 3e6e83aaaa03): rows #2299-2302 RESERVED (4 variants). Counted in N.
N_cumulative: 2302

## Engine run 20261024_100944_gen_2610241005_000 (gen_2610241005_000): rows #2299-2302. 0/4 pass. PBO 0.396. Bar applied at N=2302. Report: engine/runs/20261024_100944_gen_2610241005_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2299 | crypto|donchian(entry_n=20,exit_n=10)+trend_sma(n=50) | 10.05/0.37/-19.61 | 434.62 | 86 | 0.0197 | 0.83816 (89.13) | 1.0 | 0.2415 | 0.9075 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2300 | crypto|donchian(entry_n=20,exit_n=20)+trend_sma(n=50) | 35.15/0.82/-22.99 | 434.62 | 98 | 0.0197 | 0.69331 (94.0) | 1.0 | 0.4349 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2301 | crypto|donchian(entry_n=100,exit_n=10)+trend_sma(n=50) | 2.1/0.17/-18.03 | 434.62 | 33 | 0.0206 | 0.88811 (240.45) | 1.0 | 0.1727 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2302 | crypto|donchian(entry_n=100,exit_n=20)+trend_sma(n=50) | 8.86/0.38/-18.92 | 434.62 | 40 | 0.0217 | 0.82617 (253.34) | 1.0 | 0.2447 | 0.907 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2302

## Engine prereg 20261024_100948_gen_2610241006_000 (gen_2610241006_000, sha256 89a64a4e54c1): rows #2303-2306 RESERVED (4 variants). Counted in N.
N_cumulative: 2306

## Engine run 20261024_100948_gen_2610241006_000 (gen_2610241006_000): rows #2303-2306. 0/4 pass. PBO 0.643. Bar applied at N=2306. Report: engine/runs/20261024_100948_gen_2610241006_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2303 | index|sma_cross(fast=5,slow=150)+vol_regime(max_atr_pct=0.06) | 65.5/1.34/-10.67 | 107.42 | 25 | 0.0561 | 0.08791 (43.42) | 1.0 | 0.9744 | 0.9555 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2304 | index|sma_cross(fast=5,slow=200)+vol_regime(max_atr_pct=0.06) | 69.69/1.39/-11.79 | 107.42 | 17 | 0.0595 | 0.17682 (45.87) | 1.0 | 0.9784 | 0.934 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2305 | index|sma_cross(fast=10,slow=150)+vol_regime(max_atr_pct=0.06) | 64.42/1.31/-11.61 | 107.42 | 19 | 0.0591 | 0.14086 (42.86) | 1.0 | 0.9706 | 0.9525 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |
| 2306 | index|sma_cross(fast=10,slow=200)+vol_regime(max_atr_pct=0.06) | 72.12/1.43/-11.61 | 107.42 | 13 | 0.0596 | 0.12687 (45.19) | 1.0 | 0.9818 | 0.9185 | False | beats_buy_hold, min_trades, cost_stop, holm, spa, pbo |

N_cumulative: 2306

## Engine prereg 20261024_100951_gen_2610241007_000 (gen_2610241007_000, sha256 4b940179d69e): rows #2307-2314 RESERVED (8 variants). Counted in N.
N_cumulative: 2314

## Engine run 20261024_100951_gen_2610241007_000 (gen_2610241007_000): rows #2307-2314. 0/8 pass. PBO 0.434. Bar applied at N=2314. Report: engine/runs/20261024_100951_gen_2610241007_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2307 | megacap|rsi_revert(entry=5,exit=60,n=2)+rsi_band(hi=60) | 25.49/0.84/-6.22 | 118.49 | 113 | 0.0492 | 0.84515 (44.99) | 1.0 | 0.5578 | 0.4865 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2308 | megacap|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2309 | megacap|rsi_revert(entry=5,exit=80,n=2)+rsi_band(hi=60) | 32.99/0.93/-7.01 | 118.49 | 105 | 0.0501 | 0.72428 (47.12) | 1.0 | 0.6281 | 0.971 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2310 | megacap|rsi_revert(entry=5,exit=80,n=5)+rsi_band(hi=60) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2311 | megacap|rsi_revert(entry=20,exit=60,n=2)+rsi_band(hi=60) | 28.14/0.69/-12.21 | 118.49 | 337 | 0.0486 | 0.6983 (39.7) | 1.0 | 0.4335 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2312 | megacap|rsi_revert(entry=20,exit=60,n=5)+rsi_band(hi=60) | 30.41/0.91/-6.44 | 118.49 | 64 | 0.0471 | 0.78921 (47.74) | 1.0 | 0.6191 | 0.9635 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2313 | megacap|rsi_revert(entry=20,exit=80,n=2)+rsi_band(hi=60) | 31.82/0.7/-12.66 | 118.49 | 266 | 0.0501 | 0.7003 (44.08) | 1.0 | 0.4465 | 0.511 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2314 | megacap|rsi_revert(entry=20,exit=80,n=5)+rsi_band(hi=60) | 67.51/1.3/-11.58 | 118.49 | 64 | 0.049 | 0.17383 (47.13) | 1.0 | 0.8454 | 0.8545 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2314

## Engine prereg 20261024_100954_gen_2610241008_000 (gen_2610241008_000, sha256 2be5c2b648e6): rows #2315-2322 RESERVED (8 variants). Counted in N.
N_cumulative: 2322

## Engine run 20261024_100954_gen_2610241008_000 (gen_2610241008_000): rows #2315-2322. 0/8 pass. PBO 0.618. Bar applied at N=2322. Report: engine/runs/20261024_100954_gen_2610241008_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2315 | sectors|rsi_revert(entry=5,exit=60,n=3) | -0.52/-0.06/-4.16 | 94.31 | 45 | 0.0597 | 1.0 (38.94) | 1.0 | 0.0438 | 0.4985 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2316 | sectors|rsi_revert(entry=5,exit=60,n=5) | 0.58/0.47/-0.27 | 94.31 | 6 | 0.0564 | 0.96104 (41.53) | 1.0 | 0.1765 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2317 | sectors|rsi_revert(entry=5,exit=70,n=3) | 1.51/0.22/-4.16 | 94.31 | 45 | 0.0597 | 0.997 (40.49) | 1.0 | 0.1116 | 0.497 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2318 | sectors|rsi_revert(entry=5,exit=70,n=5) | 1.01/0.39/-1.22 | 94.31 | 6 | 0.0564 | 0.96903 (41.72) | 1.0 | 0.1716 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2319 | sectors|rsi_revert(entry=10,exit=60,n=3) | 14.04/0.57/-8.07 | 94.31 | 124 | 0.0629 | 0.98302 (38.72) | 1.0 | 0.2276 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2320 | sectors|rsi_revert(entry=10,exit=60,n=5) | 1.61/0.24/-3.71 | 94.31 | 23 | 0.0554 | 0.98002 (43.76) | 1.0 | 0.1203 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2321 | sectors|rsi_revert(entry=10,exit=70,n=3) | 23.84/0.84/-8.07 | 94.31 | 120 | 0.063 | 0.86613 (38.88) | 1.0 | 0.4229 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2322 | sectors|rsi_revert(entry=10,exit=70,n=5) | 3.05/0.42/-3.71 | 94.31 | 23 | 0.0554 | 0.97303 (38.27) | 1.0 | 0.193 | 0.4985 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |

N_cumulative: 2322

## Engine prereg 20261024_100957_gen_2610241009_000 (gen_2610241009_000, sha256 00eb88188d6e): rows #2323-2326 RESERVED (4 variants). Counted in N.
N_cumulative: 2326

## Engine run 20261024_100957_gen_2610241009_000 (gen_2610241009_000): rows #2323-2326. 0/4 pass. PBO 0.771. Bar applied at N=2326. Report: engine/runs/20261024_100957_gen_2610241009_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2323 | BROAD|sma_cross(fast=10,slow=100) | 38.46/0.91/-12.92 | 83.36 | 66 | 0.0816 | 0.42557 (34.74) | 1.0 | 0.7657 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2324 | BROAD|sma_cross(fast=10,slow=150) | 35.27/0.84/-18.5 | 83.36 | 56 | 0.0882 | 0.51748 (35.09) | 1.0 | 0.7292 | 0.5095 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2325 | BROAD|sma_cross(fast=50,slow=100) | 40.46/0.96/-9.92 | 83.36 | 47 | 0.079 | 0.40859 (35.97) | 1.0 | 0.7924 | 0.4845 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2326 | BROAD|sma_cross(fast=50,slow=150) | 54.12/1.16/-11.83 | 83.36 | 30 | 0.0883 | 0.17283 (36.1) | 1.0 | 0.8754 | 0.929 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2326

## Engine prereg 20261024_101000_gen_2610241010_000 (gen_2610241010_000, sha256 008d209a34f6): rows #2327-2334 RESERVED (8 variants). Counted in N.
N_cumulative: 2334

## Engine run 20261024_101000_gen_2610241010_000 (gen_2610241010_000): rows #2327-2334. 0/8 pass. PBO 0.161. Bar applied at N=2334. Report: engine/runs/20261024_101000_gen_2610241010_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2327 | crypto|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 15.69/0.94/-7.05 | 434.62 | 49 | 0.0202 | 0.79121 (67.27) | 1.0 | 0.5452 | 0.898 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2328 | crypto|rsi_revert(entry=10,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 13.26/1.4/-3.82 | 434.62 | 14 | 0.0188 | 0.82218 (68.45) | 1.0 | 0.7909 | 0.899 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2329 | crypto|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 32.59/1.36/-12.39 | 434.62 | 65 | 0.0175 | 0.67632 (168.28) | 1.0 | 0.7333 | 0.8885 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2330 | crypto|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 19.77/1.07/-12.98 | 434.62 | 22 | 0.0171 | 0.81319 (157.65) | 1.0 | 0.6086 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2331 | crypto|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.06) | 18.7/0.73/-16.22 | 434.62 | 117 | 0.0211 | 0.75125 (75.9) | 1.0 | 0.4449 | 0.8945 | False | beats_buy_hold, holm, dsr, spa |
| 2332 | crypto|rsi_revert(entry=20,exit=60,n=5)+vol_regime(max_atr_pct=0.06) | 15.49/0.83/-13.47 | 434.62 | 57 | 0.0181 | 0.78022 (237.16) | 1.0 | 0.4976 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2333 | crypto|rsi_revert(entry=20,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 34.19/0.97/-18.4 | 434.62 | 124 | 0.0181 | 0.63636 (190.65) | 1.0 | 0.5658 | 0.8905 | False | beats_buy_hold, holm, dsr, spa |
| 2334 | crypto|rsi_revert(entry=20,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 40.0/1.17/-14.26 | 434.62 | 76 | 0.0172 | 0.60839 (74.1) | 1.0 | 0.6571 | 0.8775 | False | beats_buy_hold, min_trades, holm, dsr, spa |

N_cumulative: 2334

## Engine prereg 20261024_101002_gen_2610241013_000 (gen_2610241013_000, sha256 535a36828fb2): rows #2335-2338 RESERVED (4 variants). Counted in N.
N_cumulative: 2338

## Engine run 20261024_101002_gen_2610241013_000 (gen_2610241013_000): rows #2335-2338. 0/4 pass. PBO 0.068. Bar applied at N=2338. Report: engine/runs/20261024_101002_gen_2610241013_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2335 | sectors|donchian(entry_n=20,exit_n=10) | 36.82/1.18/-7.3 | 94.31 | 130 | 0.0661 | 0.52947 (38.41) | 1.0 | 0.8233 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2336 | sectors|donchian(entry_n=20,exit_n=20) | 44.61/1.16/-10.27 | 94.31 | 88 | 0.0592 | 0.30569 (38.55) | 1.0 | 0.8188 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2337 | sectors|donchian(entry_n=55,exit_n=10) | 20.42/0.86/-6.2 | 94.31 | 103 | 0.0778 | 0.92108 (39.27) | 1.0 | 0.6512 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2338 | sectors|donchian(entry_n=55,exit_n=20) | 24.42/0.85/-8.69 | 94.31 | 70 | 0.0724 | 0.87912 (39.19) | 1.0 | 0.6421 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2338

## Engine prereg 20261024_101005_gen_2610241014_000 (gen_2610241014_000, sha256 a73304071e54): rows #2339-2346 RESERVED (8 variants). Counted in N.
N_cumulative: 2346

## Engine run 20261024_101005_gen_2610241014_000 (gen_2610241014_000): rows #2339-2346. 0/8 pass. PBO 0.234. Bar applied at N=2346. Report: engine/runs/20261024_101005_gen_2610241014_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2339 | BROAD|drop_revert(drop=0.05,hold=3,n=1)+trend_sma(n=200) | -0.71/-0.3/-1.48 | 83.36 | 14 | 0.0312 | 0.99101 (35.66) | 1.0 | 0.0001 | 0.4975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2340 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | 4.4/0.49/-4.32 | 83.36 | 50 | 0.0424 | 0.98402 (33.06) | 1.0 | 0.0251 | 0.502 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2341 | BROAD|drop_revert(drop=0.05,hold=5,n=1)+trend_sma(n=200) | -0.24/-0.07/-1.33 | 83.36 | 14 | 0.0342 | 0.98102 (36.61) | 1.0 | 0.0014 | 0.4965 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2342 | BROAD|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 7.0/0.65/-5.43 | 83.36 | 52 | 0.043 | 0.96903 (34.4) | 1.0 | 0.0441 | 0.501 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2343 | BROAD|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=200) | 0.0/0.0/0.0 | 83.36 | 1 | 0.0201 | 1.0 (38.63) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2344 | BROAD|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=200) | 0.33/0.41/-0.12 | 83.36 | 4 | 0.036 | 0.97203 (37.13) | 1.0 | 0.0011 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2345 | BROAD|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=200) | 0.0/0.0/0.0 | 83.36 | 1 | 0.0201 | 1.0 (33.7) | 1.0 | 0.0 | 0.501 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2346 | BROAD|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=200) | 1.18/0.99/0.0 | 83.36 | 4 | 0.036 | 0.96903 (35.23) | 1.0 | 0.0079 | 0.505 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

N_cumulative: 2346

## Engine prereg 20261024_101008_gen_2610241015_000 (gen_2610241015_000, sha256 4c791a55227c): rows #2347-2350 RESERVED (4 variants). Counted in N.
N_cumulative: 2350

## Engine run 20261024_101008_gen_2610241015_000 (gen_2610241015_000): rows #2347-2350. 0/4 pass. PBO 0.16. Bar applied at N=2350. Report: engine/runs/20261024_101008_gen_2610241015_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2347 | crypto|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.06) | 16.32/0.61/-17.72 | 434.62 | 49 | 0.0182 | 0.8012 (187.34) | 1.0 | 0.3139 | 0.9005 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2348 | crypto|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.06) | 18.21/0.6/-16.37 | 434.62 | 55 | 0.0172 | 0.74326 (66.28) | 1.0 | 0.3088 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2349 | crypto|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 5.02/0.29/-15.71 | 434.62 | 30 | 0.02 | 0.84815 (136.93) | 1.0 | 0.1918 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2350 | crypto|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | -2.77/0.0/-19.5 | 434.62 | 38 | 0.0174 | 0.91309 (86.56) | 1.0 | 0.1132 | 0.9125 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2350

## Engine prereg 20261024_101010_gen_2610241016_000 (gen_2610241016_000, sha256 acb344f6b1a1): rows #2351-2354 RESERVED (4 variants). Counted in N.
N_cumulative: 2354

## Engine run 20261024_101010_gen_2610241016_000 (gen_2610241016_000): rows #2351-2354. 0/4 pass. PBO 0.13. Bar applied at N=2354. Report: engine/runs/20261024_101010_gen_2610241016_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2351 | index|donchian(entry_n=20,exit_n=10) | 51.31/1.36/-6.81 | 107.42 | 87 | 0.0757 | 0.28771 (42.67) | 1.0 | 0.7663 | 0.4955 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2352 | index|donchian(entry_n=20,exit_n=20) | 76.06/1.58/-8.36 | 107.42 | 53 | 0.0657 | 0.02398 (43.71) | 1.0 | 0.8691 | 0.923 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2353 | index|donchian(entry_n=100,exit_n=10) | 24.69/0.97/-5.84 | 107.42 | 66 | 0.0901 | 0.92308 (43.91) | 1.0 | 0.5247 | 0.5005 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2354 | index|donchian(entry_n=100,exit_n=20) | 36.13/1.11/-7.92 | 107.42 | 41 | 0.0835 | 0.66234 (43.3) | 1.0 | 0.6187 | 0.517 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2354

## Engine prereg 20261024_101013_gen_2610241017_000 (gen_2610241017_000, sha256 87cca3dcb796): rows #2355-2358 RESERVED (4 variants). Counted in N.
N_cumulative: 2358

## Engine run 20261024_101013_gen_2610241017_000 (gen_2610241017_000): rows #2355-2358. 0/4 pass. PBO 0.532. Bar applied at N=2358. Report: engine/runs/20261024_101013_gen_2610241017_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2355 | megacap|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 54.49/1.24/-15.63 | 118.49 | 105 | 0.0518 | 0.34965 (46.99) | 1.0 | 0.8861 | 0.9665 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2356 | megacap|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 46.85/0.94/-19.22 | 118.49 | 84 | 0.0509 | 0.45554 (46.49) | 1.0 | 0.7527 | 0.512 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2357 | megacap|donchian(entry_n=100,exit_n=10)+rsi_band(hi=80) | 43.3/1.29/-9.05 | 118.49 | 70 | 0.061 | 0.53646 (46.66) | 1.0 | 0.9063 | 0.962 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2358 | megacap|donchian(entry_n=100,exit_n=20)+rsi_band(hi=80) | 38.18/1.08/-10.9 | 118.49 | 58 | 0.0602 | 0.64735 (46.78) | 1.0 | 0.8237 | 0.503 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2358

## Engine prereg 20261024_101015_gen_2610241018_000 (gen_2610241018_000, sha256 5431a4c3410b): rows #2359-2362 RESERVED (4 variants). Counted in N.
N_cumulative: 2362

## Engine run 20261024_101015_gen_2610241018_000 (gen_2610241018_000): rows #2359-2362. 0/4 pass. PBO 0.866. Bar applied at N=2362. Report: engine/runs/20261024_101015_gen_2610241018_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2359 | sectors|donchian(entry_n=55,exit_n=10) | 20.42/0.86/-6.2 | 94.31 | 103 | 0.0778 | 0.92408 (39.64) | 1.0 | 0.7842 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2360 | sectors|donchian(entry_n=55,exit_n=20) | 24.42/0.85/-8.69 | 94.31 | 70 | 0.0724 | 0.87413 (40.06) | 1.0 | 0.7781 | 0.516 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2361 | sectors|donchian(entry_n=100,exit_n=10) | 12.94/0.66/-5.27 | 94.31 | 89 | 0.0806 | 0.98002 (38.38) | 1.0 | 0.6738 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2362 | sectors|donchian(entry_n=100,exit_n=20) | 15.8/0.66/-8.29 | 94.31 | 59 | 0.0777 | 0.97203 (39.39) | 1.0 | 0.6738 | 0.514 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

N_cumulative: 2362

## Engine prereg 20261024_101018_gen_2610241019_000 (gen_2610241019_000, sha256 bfacb821fc76): rows #2363-2366 RESERVED (4 variants). Counted in N.
N_cumulative: 2366

## Engine run 20261024_101018_gen_2610241019_000 (gen_2610241019_000): rows #2363-2366. 0/4 pass. PBO 0.32. Bar applied at N=2366. Report: engine/runs/20261024_101018_gen_2610241019_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2363 | BROAD|supertrend(atr_n=10,mult=3) | 30.56/0.82/-14.65 | 83.36 | 140 | 0.0873 | 0.61239 (34.32) | 1.0 | 0.7477 | 0.482 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2364 | BROAD|supertrend(atr_n=10,mult=4) | 36.86/0.96/-12.17 | 83.36 | 87 | 0.0839 | 0.47153 (34.95) | 1.0 | 0.8161 | 0.484 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2365 | BROAD|supertrend(atr_n=14,mult=3) | 29.55/0.8/-13.75 | 83.36 | 143 | 0.0873 | 0.62038 (33.48) | 1.0 | 0.7411 | 0.491 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2366 | BROAD|supertrend(atr_n=14,mult=4) | 41.64/1.06/-11.32 | 83.36 | 88 | 0.0838 | 0.35165 (35.15) | 1.0 | 0.8577 | 0.4915 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2366

## Engine prereg 20261024_101021_gen_2610241020_000 (gen_2610241020_000, sha256 7f59042b90e3): rows #2367-2374 RESERVED (8 variants). Counted in N.
N_cumulative: 2374

## Engine run 20261024_101021_gen_2610241020_000 (gen_2610241020_000): rows #2367-2374. 0/8 pass. PBO 0.119. Bar applied at N=2374. Report: engine/runs/20261024_101021_gen_2610241020_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2367 | crypto|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=100) | 1.63/0.49/-1.02 | 434.62 | 20 | 0.0103 | 0.91009 (46.99) | 1.0 | 0.027 | 0.905 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2368 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=100) | 5.13/0.4/-6.87 | 434.62 | 67 | 0.0123 | 0.91608 (224.56) | 1.0 | 0.048 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2369 | crypto|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=100) | -1.94/-0.37/-4.45 | 434.62 | 21 | 0.0112 | 0.97602 (43.39) | 1.0 | 0.005 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2370 | crypto|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=100) | 4.42/0.31/-11.09 | 434.62 | 69 | 0.0133 | 0.88312 (91.9) | 1.0 | 0.0408 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2371 | crypto|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 434.62 | 3 | 0.0044 | 1.0 (41.55) | 1.0 | 0.0 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2372 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=100) | 6.7/1.15/-1.96 | 434.62 | 21 | 0.0112 | 0.89411 (239.02) | 1.0 | 0.1919 | 0.9015 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2373 | crypto|drop_revert(drop=0.15,hold=5,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 434.62 | 3 | 0.0044 | 1.0 (311.64) | 1.0 | 0.0 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2374 | crypto|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=100) | 0.34/0.07/-4.45 | 434.62 | 23 | 0.0103 | 0.94505 (150.78) | 1.0 | 0.022 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

N_cumulative: 2374

## Engine prereg 20261024_101023_gen_2610241022_000 (gen_2610241022_000, sha256 598f62542555): rows #2375-2382 RESERVED (8 variants). Counted in N.
N_cumulative: 2382

## Engine run 20261024_101023_gen_2610241022_000 (gen_2610241022_000): rows #2375-2382. 0/8 pass. PBO 0.341. Bar applied at N=2382. Report: engine/runs/20261024_101023_gen_2610241022_000/report.md

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2375 | megacap|rsi_revert(entry=5,exit=60,n=2) | 25.47/0.84/-6.22 | 118.49 | 113 | 0.0486 | 0.84316 (46.21) | 1.0 | 0.5678 | 0.487 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2376 | megacap|rsi_revert(entry=5,exit=60,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (56.85) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2377 | megacap|rsi_revert(entry=5,exit=80,n=2) | 34.23/0.96/-7.01 | 118.49 | 102 | 0.0501 | 0.71229 (46.37) | 1.0 | 0.6609 | 0.97 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2378 | megacap|rsi_revert(entry=5,exit=80,n=5) | 0.0/0.0/0.0 | 118.49 | 2 | 0.0349 | 1.0 (42.72) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2379 | megacap|rsi_revert(entry=20,exit=60,n=2) | 31.65/0.75/-10.83 | 118.49 | 359 | 0.0491 | 0.67832 (39.95) | 1.0 | 0.4901 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2380 | megacap|rsi_revert(entry=20,exit=60,n=5) | 30.41/0.91/-6.44 | 118.49 | 65 | 0.0471 | 0.75624 (47.33) | 1.0 | 0.6296 | 0.9635 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2381 | megacap|rsi_revert(entry=20,exit=80,n=2) | 35.25/0.75/-13.68 | 118.49 | 270 | 0.0509 | 0.61439 (43.05) | 1.0 | 0.4907 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2382 | megacap|rsi_revert(entry=20,exit=80,n=5) | 72.05/1.34/-11.58 | 118.49 | 50 | 0.0502 | 0.14186 (49.27) | 1.0 | 0.8654 | 0.848 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

N_cumulative: 2382
