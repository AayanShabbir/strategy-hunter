# Contributing

Private repo; this applies to the owner and to automated agents committing here.

## Hard rules
* **Research only.** No order placement, no live-routing code, no broker keys. Paper-data keys come from the environment and are never written to files, logs or commits.
* **No secrets, market data, sealed-vault data, `*.pt` weights or the live SDE ledger in git.** CI rejects forbidden tracked files.
* **Do not change `engine/` pass-bar gates, the vault or ledger-N counting** without written approval from Aayan; record the change and approval in CHANGELOG.md.
* **Keep paths stable:** `engine/` internals, `ledger/`, and the SDE module paths (`src/dsl`, `src/models`, `src/gflownet`, `src/rewards`, `src/audit`, `src/data`, `src/portfolio`, `src/validation`, `src/train`, `tests_sde`) are fixed by running jobs and the blueprint.
* **Report honestly.** Misses against targets are reported as misses; unspecified blueprint items are listed as open questions, not silently adapted.

## Branching and commits
* Work lands on `main` (single owner). Larger or risky changes: branch `feat/<topic>` / `fix/<topic>`, open a PR using the template, squash-merge. No force-push, no history rewrites.
* The hourly/nightly routines commit `specs(hourly): ...` and `ledger: mirror ...` to `main`; always `git pull --rebase` before committing and check `git status` right before `git commit`. Never touch `engine/` files by hand while a drain is running.
* Commit message style: `YYYY-MM-DD <area>: <imperative summary>` (e.g. `2026-10-23 SDE Phase 3: ...`); routines keep their own `specs(hourly)` / `ledger:` prefixes.
* Do not commit in-progress run folders in `runs_sde/` until they are scored.

## Tests
* `make test` must be green before a push (SDE 73, engine 18 as of v0.3.0; update counts in the PR when they change).
* New SDE code needs tests in `tests_sde/` that use synthetic data (mark data-dependent tests `@pytest.mark.data`; CI skips them).
* Statistical code (DSR, PBO, SPA, e-process) needs a calibration/null test, not only a smoke test.
* `make lint` (ruff correctness rules). `ruff format` is intentionally not enforced on the dense blueprint-faithful SDE code.

## Docs
Update `CHANGELOG.md` and the phase doc under `docs/` with every behavioural change; add new docs to `docs/README.md`.
