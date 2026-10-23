# Hunt #11 - candle/trend setups (6 setups x 15m/1h), 2024-10-14..2026-10-14, 5 bps/side - FAIL
Pre-registered (prereg.yaml), no tuning. 46 symbols (survivorship-biased), shorts assume borrow.
- 72,939 signal trades; average -0.9 bps/trade BEFORE costs, about -10.9 bps after 10 bps round trip. Win rate 37-46%.
- Combined portfolio (10%/trade, max 5 open, ~13.7 trades/day): -52.5% total (CAGR -31%), Sharpe -3.78, maxDD -53.6%.
- SPY: +31.8% (Sharpe 0.93, maxDD -19.1%). 70/30: +22.0%.
- Best single test 1h:S_TREND_PB +1.3 bps/trade (p 0.40, Holm 1.0 at N=310). No test passes.
Going live on paper anyway per Aayan's call; expect the active pool to bleed roughly costs per trade. Scoreboard tracks it.
