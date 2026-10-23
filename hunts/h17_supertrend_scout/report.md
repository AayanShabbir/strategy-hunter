# Hunt #17: Supertrend independent scout. Verdict: FAIL (0/15). Research only, no orders, no desk changes.

Rules (prereg.yaml, written before any results): Supertrend 10/3 (Wilder ATR, hl2 ± 3·ATR, trailing bands). Signal at close, fill at next open. Stocks 7 bps/side (5 fee + 2 slippage), crypto 20 bps/side, no borrow cost on shorts. OOS = newest 30%. Variants: long/short (SPY, QQQ, BTC, ETH); +close>SMA200 (SPY, QQQ, 10-megacap basket); +relvol (entry only on a flip-up bar with vol ≥ 1.5× the prior-20 average; SPY, QQQ, basket); 1h intraday flat by close (SPY, QQQ); top-50 by IS dollar volume long/flat; BTC/ETH long/flat. None of these repeat h16's 29 trials.

Daily OOS 2023-07-19..2026-10-14: SPY 75.2% / Sharpe 1.22 / maxDD -19.8%; 70/30 49.3% / 1.22 / -14.2%. 1h OOS 2024-11-27..2026-10-14: SPY 32.5%. Crypto OOS 2025-01-24..2026-10-22: BTC B&H -21.7%, ETH B&H -28.6%.

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

PBO = 0.82 across the stock trials. DSR = 0 for every trial at N=392. Holm = 1.0 for all.
Best variant (by OOS Sharpe): T11_TOP50_LF, 39.6% vs SPY 75.2%, so it loses to SPY. It has a lower drawdown (-9.2%), which is just less time in the market, not an edge (twin p 0.96). Best raw return: T15_ETH_LS, +124% vs ETH B&H -28.6%, but that's from 13 trades, it was -74% IS, twin p 0.14, and SPA 0.195, so it's a single-regime fluke.
Caveats: survivor-biased stock universe; 1h twin uses a sign-flip proxy; vectorbt isn't installed, so it's a numpy engine with the same logic; the venv is .venv17 (arch/quantstats added).
Coordination: h16 (research_lab/hunts/h16_supertrend) crashed on a missing `arch` module and logged no rows. Its 29 trials are reserved as #349-377; h17 = #378-392. N = 392.
