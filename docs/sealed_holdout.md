# Sealed fresh holdout (2021-01-01 → 2026-10-22) and the single-use vault

Research only. Nothing here places orders or talks to a broker. As of 2026-10-24 **nothing has been evaluated on the sealed set**; building it only fetched, counted and hashed.

## Why
Every SDE/swarm search window ends **2020-12-31** (train 2010–2016, validation 2017, test 2018–2020). The old test split has been looked at many times, so it is no longer a clean holdout. 2021-01-01 → latest has never been used by any search, reward, selection or report. It is the only data left that can give an honest out-of-sample answer, and it can be spent once.

## Where the data lives
`data/sealed_sde/` (git-ignored by `/data/sealed_sde/` and by the anchored `/data/` rule; files are chmod 0440). Contents: `panel.npz` (dates, assets, $close/$high/$low/$volume, member mask, `eval_start_idx`), `membership_fja05680.csv` (fresh PIT membership), `provenance.json` (per-ticker sources, no prices), `finsaber_ge2021.csv`, `cache/` (raw fetches).
Rows from 2020-07-01 are rolling-window warm-up and are never scored; scoring starts at the row of 2021-01-01 (`eval_start_idx`).
Built by `src/vault/sealed_data.py` with the Task A multi-source merge (yfinance > Alpaca > FINSABER, validated alternate tickers). Last date **2026-10-22** (Alpaca's free plan refuses SIP data from the last 15 minutes; FINSABER stops at 2024-12-31, so 2025+ comes from yfinance/Alpaca only).

Counts (from the manifest, no returns): 1,586 dates (1,458 scored), 623 tickers; 99.9% of PIT member-days priced (733,682 / 734,570); 121 of 122 names removed in the window priced. These are window-local numbers, not comparable to the 95.9% whole-history figure in `data_quality_sp500.md`.

## Pre-registration
`src/vault/sealed_manifest.json` is committed: window, ticker list and its hash, SHA-256 of every sealed file, a content hash of the arrays (independent of zip bytes), coverage, per-source counts, and the hashes of the four builder source files. The data is not committed. Anyone can later check that the data used for the look is the data that was frozen, and every pre-registered candidate pins the manifest hash.

## The vault (`src/vault/vault.py`)
Reuses the old engine vault's ideas (one look per candidate; a failure is final; recorded under a lock before the result is usable); `engine/` is untouched.
1. **Pre-register** a candidate (`Vault.preregister(spec)`). A spec is a formula `{kind:"formula", expr, sign}` or a pool `{kind:"pool", members:[{expr, sign}], combiner:"equal"}`. The candidate id is the SHA-256 of the canonical spec (expressions canonicalised by the DSL parser, `ast_hash` per member, members sorted). The log entry records spec, AST hashes, manifest hash and pass-rule id (`default_v1`).
2. **Swarm approval.** Every constituent `ast_hash` must have `audit_status='APPROVED'` in `data/ledger/trials.db` (read-only). Today that table has 590 NULL, 598 REJECTED and **0 APPROVED, so the vault refuses every candidate**. That is intended.
3. **One look per spec hash** and a **global cap on total looks, default 3**, set in the committed `src/vault/vault_config.json`. The only way to change it is to edit that file (a git commit). The vault logs a `config` entry (old and new cap, file SHA) the first time it sees a changed file, before applying it.
4. **Order of an open:** flock; verify the hash chain and the sealed data against the manifest; refuse (logged, no look consumed) if unregistered, manifest-mismatched, already opened, cap reached or not approved; write the `open` entry **before** the panel is read, so a crashing evaluator still uses its look; evaluate; write `result` or `error`.
5. **Audit log** `src/vault/vault_log.jsonl`: append-only, sha256-chained, flock-guarded (the same `Ledger` class as the SDE ledger), tracked in git so every look is also a commit. `Vault.verify_log()` runs before every open; a tampered log blocks the vault.
6. **Pass rule `default_v1`** (fixed now, before any look): long-short net Sharpe > 0 **and** the long-flat and long-only variants both have positive excess Sharpe against the equal-weight benchmark, scored on 2021+ only, 5 bps/side costs.

## Guard against search code touching it
`src/data/guard.py` + `tests_sde/test_sealed_guard.py`:
* **Static:** no module in `src/` (outside `src/vault/`, `guard.py`, `external.py`), `engine/hunt_engine` or `engine/swarm` may contain `sealed_sde`, `src.vault`, `vault_access`, `load_finsaber_full` or `load_sealed_panel`.
* **Runtime:** `install_audit_guard()` adds a `sys.addaudithook` that raises `PermissionError` on open/listdir/scandir/rename/remove/chmod/truncate under the sealed dir unless inside `vault_access()`. A subprocess test proves open, listdir, scandir, `pathlib`, and `np.load` are blocked and allowed only within the context.
* The search-side FINSABER loader is capped at 2020-12-31 (it reads a ≤2020 copy; the original file with 2021+ rows was removed from the search cache). The Alpaca cache helper refuses the sealed dir.
* **Limit, stated plainly:** this is a tripwire against accidents, not a security boundary. Any process on this box with the same OS user can read the file, and the audit hook only exists in processes that install it. The real protections are the review of who may import `src.vault` (the static test) and that the log is public and chained.

## Long-only / flat deployability (`src/portfolio/deployability.py`)
`long_flat_check(panel, signal=… | expr=…, sign=… | pool=[…])` reports, on a search-window panel: the long-short book; `long_flat` (its long leg, remainder cash); `long_only_topq` (equal-weight top 20%, fully invested); and the equal-weight benchmark, plus excess return/Sharpe, beta and alpha for both long variants and `survives` (both excess Sharpes > 0). It raises if the panel reaches past 2020-12-31 (`max_date`); only the vault passes `max_date=None`. It was not run on any survivor in this change; the survivor list is empty.

## Not done / open
* The vault has never been opened. It cannot be until the swarm auditor approves something.
* The pass rule is simple on purpose; richer ones (DSR at the then-current N) should be registered **before** the first look and are a separate decision.
* Prices are adjusted on the fetch-date basis; a long holdout in a different adjustment basis would differ slightly (documented in the manifest).
* 2021+ includes names that left the S&P 500 and were later delisted; 1 removed name has no price at all.
