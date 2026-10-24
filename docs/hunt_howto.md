# Hand-run hunt how-to (legacy research_lab notes)

Moved verbatim from the former root README on 2026-10-24. This describes the *manual* hunt protocol used for `hunts/h7`–`h17` before the automated `engine/` existed. New work should go through `engine/` (see `engine/ENGINE.md`). Note: the `.venv`, `lab/` and `data/alpaca/` paths below are historical; the live interpreter is `.venv17/` (git-ignored).
## research_lab — shared hunt stack (research only, never places orders)

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

## Strategy Discovery Engine (SDE, in progress)
New package `src/` per the SDE blueprint, see `docs/sde_plan.md`. Phase 1 (DSL AST grammar + RGCN encoder) and Phase 2 (GFlowNet search, reward/pool, ledger, data; `docs/sde_phase2.md`) done;
tests: `.venv17/bin/python -m pytest tests_sde`. Credits: AlphaGen, GFlowNets/TB, R-GCN, Benhamou et al. 2026 (see THIRD_PARTY_LICENSES.md).
