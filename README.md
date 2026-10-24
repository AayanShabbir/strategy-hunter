# strategy-hunter

Research-only strategy finder and backtest engine for Aayan's paper desk. **Places no orders; never touches the live desk.**

## Structure
- `engine/` — Strategy Hunter (`./engine/hunt`): spec → pre-register (ledger N) → vectorbt backtest → pass bar (OOS, B&H, ≥100 trades, cost/stop ≤3%, walk-forward, random-entry twin + ledger-wide Holm, DSR, SPA, PBO) → one vault look for survivors. Tests: `engine/tests`.
- `crypto/`, `reels/` — crypto research notes, ORB reel test. `hunts/` — hand-run hunts h7–h17. `ledger/` — human ledger. `nautilus/` — NautilusTrader confirmation harness. `docs/` — design notes (see `docs/frontier_upgrade.md`).

## Run
```
./engine/hunt status | validate SPEC | run SPEC | enqueue SPEC | drain [--dry]
./engine/hunt generate --n 20 --seed 1 --universe '{"crypto":["SOL/USD","BTC/USD"]}' --out /tmp/gen
./engine/hunt optimize SPEC --trials 50 --objective calmar
cd engine && ../.venv17/bin/python -m pytest -q
```
Market-data keys come from env (`ALPACA_API_KEY`/`ALPACA_SECRET_KEY`) and are never stored. Data caches and the sealed vault data are git-ignored; re-fetch with `hunt seed-cache`.

## Credits
vectorbt (polakowo, Apache-2.0 w/ Commons Clause), NautilusTrader (LGPL-3.0), Optuna (MIT), numba (BSD-2), arch (K. Sheppard, NCSA), pypbo (esvhd, MIT, vendored), skfolio (BSD-3), quantstats (Apache-2.0), alpaca-py (Apache-2.0), scipy/numpy/pandas (BSD). Methods: Bailey & López de Prado (PBO, DSR, False Strategy Theorem), Hansen (SPA), Holm. Full list: `THIRD_PARTY_LICENSES.md`.

---
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

## Strategy Discovery Engine (SDE, in progress)
New package `src/` per the SDE blueprint, see `docs/sde_plan.md`. Phase 1 (DSL AST grammar + RGCN encoder) done;
tests: `.venv17/bin/python -m pytest tests_sde`. Credits: AlphaGen, GFlowNets/TB, R-GCN, Benhamou et al. 2026 (see THIRD_PARTY_LICENSES.md).
