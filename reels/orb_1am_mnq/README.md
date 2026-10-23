# ORB 1am NY – MNQ (research only, not a desk strategy)
Source: Instagram reel by @theagent_trades ("profitable bot in 15 seconds"). Prompt reproduced in Pine v6.

## Paste into TradingView
1. Open a chart of `MNQ1!`, set timeframe to **5m**, and enable extended hours (ETH) – the range is overnight.
2. Pine Editor (bottom panel) → Open → New blank strategy → delete contents → paste `orb_1am.pine` → Save → Add to chart.
3. Strategy Tester tab shows results. Costs are preset: $0.62/side/contract commission, 1 tick slippage, 1 contract.
4. Toggle F1–F5 in the strategy Settings → Inputs one at a time to compare regimes. Note TV's 5m history on free plans is short; use Deep Backtesting (paid) for longer.

Exits: stop at the opposite side of the range, target 0.5R, flatten at end of trade window (default 09:30 NY). One trade per day.
Note: entries fill at the next bar open (TV default); target is computed from the signal close, so realised R is slightly off 0.5.
Break-even win rate at 0.5R before costs = 1/(1+0.5) = 66.7%; costs push it higher.
Offline backtest: `backtest.py` → `results.json`.
