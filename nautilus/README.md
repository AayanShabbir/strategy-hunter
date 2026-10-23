# Nautilus re-test lab (BACKTEST ONLY)

Isolated install of NautilusTrader 1.231.0 for *realistic re-tests* of strategy-engine survivors.
No broker keys, no live nodes, no adapters, no orders. Separate from /workspace/trading-desk and .venv17.

- `.venv/` — Python 3.13.5, `nautilus_trader==1.231.0`, `pandas<3` (pandas 3 breaks BarDataWrangler: read-only buffer). No Redis.
- `requirements.lock` — full pip freeze.
- `run.sh` — the ONLY way to run code here; unsets ALPACA_*, APCA_*, KALSHI_*, FINNHUB_*, FMP_*, *_API_KEY*, *_SECRET*, *_TOKEN, *_KEY.
- `tests/test_guard.py` — fails on any live/adapter import; verifies run.sh strips keys. Run: `./run.sh -m pytest -q tests`.
- `smoke_backtest.py` — SPY daily SMA20/50, $1/fill fees, pre-vault (< 2025-10-23). Report: `reports/smoke_report.json`.
- `retest.py` — stub for `hunt retest <run_id> --variant <id>`.

## Realistic re-test step (pipeline)
1. Nightly engine (vectorized) runs the full pass bar; survivors are listed in `engine/runs/<run_id>/`.
2. `./run.sh retest.py <run_id> --variant <id>` translates the variant into a Nautilus `Strategy`, replays
   pre-vault bars through `BacktestEngine` with fee model + slippage (FillModel), cash account, no margin.
3. Pass only if Nautilus result is within tolerance of the engine result (same trade count ±10%, net return
   not materially worse after realistic fills). Divergence = engine bug or cost-fragile edge → reject.
4. Only then the one-shot vault test, then 30–60 days paper, then Aayan's written OK.

## License / credit
NautilusTrader © Nautech Systems Pty Ltd, licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0).
https://github.com/nautechsystems/nautilus_trader — used unmodified as a library dependency; source available upstream.
