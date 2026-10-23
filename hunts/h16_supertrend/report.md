# Hunt #16: Supertrend (friend's Robinhood claim). Verdict: FAIL (0/29). Research only, paper only, no orders, no desk changes.

**What it is:** a trailing band set at hl2 ± mult×ATR(n), using Wilder ATR (default 10/3). It shows green or "up" while the close stays above the trailing lower band and flips when the close crosses the opposite band. Robinhood offers it as a chart indicator in Legend and in mobile advanced charts. It is a display tool, not a tested strategy.

**Rules** (prereg.yaml, written before any results): long/flat only (shorts are blocked). Signal at the close, fill at the next open, 5 bps/side. ATR {7,10,14} × mult {2,3,4} on SPY, QQQ and an equal-weight 10 mega-cap basket (AAPL MSFT NVDA AMZN GOOGL META AVGO JPM LLY TSLA, survivor-biased). Plus 15m 10/3 on SPY and QQQ, flat by 15:45. IS = oldest 70% (2016-01-04..2023-07-18), OOS = 2023-07-19..2026-10-14. Ledger #349-377; bar applied at N=392.

## Results (OOS ret% / Sharpe / maxDD%)
| variant | IS | OOS | twin p | Holm@392 | DSR | SPA vs SPY | pass |
|---|---|---|---|---|---|---|---|
| SPY buy&hold | 156.9/0.80/-32.1 | **75.2/1.22/-19.8** | | | | | |
| QQQ buy&hold | 275.6/0.90/-36.6 | 89.2/1.07/-24.2 | | | | | |
| Basket buy&hold | 870.1/1.32/-37.3 | 170.7/1.39/-28.2 | | | | | |
| SPY 14/3 (best Sharpe) | 49.6/0.54/-16.9 | 58.0/1.52/-8.3 | 0.064 | 1 | 0.008 | 0.84 | no |
| SPY 10/3 default | 53.8/0.59/-16.1 | 45.8/1.43/-7.5 | 0.19 | 1 | 0.006 | 0.93 | no |
| QQQ 14/4 | 104.6/0.76/-28.9 | 61.9/1.30/-12.3 | 0.17 | 1 | 0.003 | 0.72 | no |
| QQQ 10/3 default | 123.7/0.86/-19.8 | 37.5/0.85/-13.0 | 0.46 | 1 | 0.000 | 0.92 | no |
| Basket 7/2 (best basket) | 284.3/1.34/-23.8 | 67.3/1.22/-14.2 | 0.42 | 1 | 0.002 | 0.63 | no |
| Basket 10/3 default | 321.0/1.42/-22.5 | 58.4/1.16/-11.1 | 0.66 | 1 | 0.001 | 0.74 | no |
| SPY 15m 10/3 | -44.5/-1.52/-45.0 | -36.8/-3.02/-37.0 | 1.0 | 1 | 0 | 0.51 | no |
| QQQ 15m 10/3 | -43.8/-1.10/-44.9 | -30.6/-1.99/-32.1 | 0.996 | 1 | 0 | 0.50 | no |

PBO = 0.381 (CSCV, 16 blocks, all 29 trials). Full table: results.json and the ledger.

**Findings:** no variant beat its own buy-and-hold in IS or OOS. Every variant's IS return also trails SPY's. Supertrend is in the market about 60-70% of the time, so it cuts drawdown roughly in half, and that is the only reason the Sharpe looks okay. The random-twin p-values (same run lengths, shuffled) show the timing adds nothing; the best is 0.064 before correction. The 15m version is ruined by whipsaw and costs. Scout's h17 (filters, long/short, 1h, crypto; 0/15) agrees.

**Friend's claim:** consistent with a bull-market and mega-cap tailwind. Any long exposure to NVDA, PLTR or similar in 2023-26 made money, and Supertrend only kept him in part of the time. Also likely: survivorship and selective memory, discretionary use (not the mechanical rule), or leverage/options. There is no evidence of an edge.

External: quant4free.com/analysis/supertrend (SPY 10/3: 5.3% CAGR vs 10.9% B&H); kagels-trading.com/blog/supertrend-indicator (long-only lags B&H; shorts lose); backtestingmax.com/backtests/supertrend (all 9 15m tests lost after costs).
Caveats: numpy engine (no vectorbt); 15m twin uses a sign-flip proxy; basket is survivor-biased (which flatters it).
