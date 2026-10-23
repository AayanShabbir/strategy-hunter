# Changelog
All dates America/New_York.

## 2026-10-23
### Added
- `hunt optimize` (Optuna TPE, IS-only, every trial counted in ledger N), `hunt generate` (grammar spec generator, `--schema` for LLM proposers).
- CPCV path diagnostic, drawdown-vs-B&H diagnostic, `day_of_week` filter.
- numba-compiled random-entry control (~20x faster).
- docs/frontier_upgrade.md, repo .gitignore, README.
### Fixed
- Sharpe annualisation: √365 for crypto, √252 for stocks.
- Queue ordering for symlinked specs (lstat mtime).
### Unchanged
- Every pass-bar gate and the sealed 12-month vault.

## 2026-10-23 (earlier)
- Baseline import: engine, ledger (N=679), hunts h7–h17, crypto batch (221 strategies, 0 passed), ORB reel test.
