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
