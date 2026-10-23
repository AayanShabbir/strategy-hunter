# research_lab — shared hunt stack (research only, never places orders)

Isolated env: `/workspace/research_lab/.venv` (separate from the trading desk runtime). Run with `.venv/bin/python`.
Layout: `data/alpaca/` (one shared parquet cache of Alpaca bars), `lab/` (shared glue), `hunts/<hunt_id>/`, `ledger/` (cumulative tried-variant count N).

## How an agent runs a hunt
1. `mkdir hunts/<id>` and write **prereg.yaml first** (rule, params, costs ≥5 bps/side, IS/OOS split, benchmark, pass bar). Commit nothing else until it exists; never edit it after results.
2. Load bars from `data/alpaca/` (fetch once with alpaca-py paper data keys from env; never print keys).
3. Backtest with **vectorbt** (signal on completed bar, fill next bar open, fees from prereg).
4. Robustness checks:
   - **CPCV**: `skfolio.model_selection.CombinatorialPurgedCV` — distribution of OOS Sharpe across paths.
   - **PBO + DSR**: `pypbo` (CSCV PBO; deflated Sharpe using the ledger's cumulative N).
   - **Holm**: `statsmodels.stats.multitest.multipletests(method="holm")` over all N variants in the ledger.
   - **SPA**: `arch.bootstrap.SPA` — strategy (or 70/15/15 blend) vs SPY / 70% SPY core.
5. `quantstats.reports.html(strategy, benchmark=SPY)` → `hunts/<id>/tearsheet.html`.
6. Append the result and new N to `ledger/`. Pass only if every check passes; nothing is switched on without Aayan's OK.

Example: `hunts/h7_overnight_repro/` (reproduces Hunt #7 overnight_after_down1 exactly).
