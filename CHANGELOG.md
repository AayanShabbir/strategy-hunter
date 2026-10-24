# Changelog
All dates America/New_York.

## 2026-10-24 (v0.3.0-sde-phase3, repo restructure)
### Added
- Root README (architecture diagram, quickstart, status), ARCHITECTURE.md, CONTRIBUTING.md, docs/README.md index, docs/runs_sde.md, LICENSE (proprietary), pyproject.toml (pytest + ruff), Makefile, .editorconfig, PR template, CI workflow (.github/workflows/ci.yml).
### Changed
- Old root README's manual-hunt section moved verbatim to docs/hunt_howto.md; docs/sde_plan.md status updated (Phase 3 done, Phase 4 components built).
### Unchanged
- engine/ (behaviour, gates, vault), ledger/, all SDE module paths, all code. Research folders deliberately not moved (absolute-path citations; see ARCHITECTURE.md).

## 2026-10-23 (SDE Phase 3)
- src/portfolio, src/validation (DSR, CSCV/PBO, CPCV, SPA, Ville e-process), src/train/phase3_eval + phase3_table; 25 new tests (73 total); CSI300 and S&P 500 scored, no blueprint target met — see docs/sde_phase3.md.

## 2026-10-23 (SDE Phase 2)
- src/audit, src/data, src/gflownet, src/rewards, src/train; vectorized TsStd; 33 new tests; first CSI300 run (3 seeds) — see docs/sde_phase2.md.

## 2026-10-23
### Changed
- Nightly/daily false-discovery variant budget for `hunt drain` raised from 200 to 2400 (default `--cap`), approved in writing by Aayan on 2026-10-23 19:57 ET so the hourly strategy search truly runs hourly. Pass-bar gates, vault, and ledger N counting are unchanged; every variant still counts toward N.
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
