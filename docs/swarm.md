# Multi-agent strategy discovery swarm

Research-only: the swarm places no orders, holds no broker keys, and reads **search data only** (S&P 500 daily bars, train
2010-2016 + validation 2017). The SDE test years 2018-2020 and the sealed engine vault are never loaded (enforced by a source-scan
test, `test_panel_never_contains_test_years_and_code_never_loads_them`). Blueprint: `/workspace/swarm_blueprint.md`.
LLM idea source: [swarm_llm_mailbox.md](swarm_llm_mailbox.md).

```
 Miner ──tasks (AST JSON)──► shared trial ledger (SQLite WAL, data/ledger/trials.db) ◄── Workers x W (separate processes)
   ▲  novelty memory (TED, frequent subtrees)        │  returns, metrics, N_trials          tensor backtest, CPU/GPU
   │  LLM mailbox / HTTP (async, never blocks)        ▼
   └────── feedback ◄── Auditor (CPCV, PBO, DSR, SPA) ──► Trader (rho<0.30, dIC>0) ──► Publisher (survivor_alpha.py, tearsheet, MLflow)
```

## Run it

```bash
cd /workspace/research_lab
./engine/hunt swarm-start --workers 4                    # bounded: 200 new formulas, then audit, then stop (default)
./engine/hunt swarm-start --workers 4 --max-trials 1000  # bounded, bigger
./engine/hunt swarm-start --workers 4 --continuous       # until Ctrl-C / SIGTERM / `touch data/swarm/STOP`
./engine/hunt swarm-start --workers 2 --synthetic --max-trials 24 --db /tmp/t.db   # smoke test on synthetic noise
./engine/hunt swarm-status                               # N_trials, status counts, audit verdicts, factor pool
./engine/hunt swarm-llm-check 'Div(TsStd($close, 20d), $volume)'
./engine/hunt swarm-llm-ping                             # round trip through the LLM mailbox (see swarm_llm_mailbox.md)
./engine/hunt swarm-start --workers 4 --llm mailbox      # also take formulas from the Swarm Miner agent (async)
```

Flags: `--max-seconds`, `--seed`, `--llm none|mailbox|openai`, `--no-publish`, `--no-tearsheet`, `--no-mlflow`, `--db`, `--json`.
Shutdown (any reason) sets a stop event, joins the workers (terminating only if they ignore it), re-queues anything still leased,
then audits whatever finished. Workers also exit if the coordinator disappears, so a killed run leaves no orphans.
`data/` is git-ignored: the ledger, panel cache, LLM mailbox and MLflow store are local state.

## Connected to the SDE (one command, one count)

```bash
./engine/hunt swarm-start --sde-policy sp500_s2 --workers 4              # trained GFlowNet as an extra proposal source + SDE pool + shared N
./engine/hunt swarm-start --sde-policy sp500_s2 --workers 4 --policy-share 0.7 --max-trials 300
./engine/hunt swarm-start --workers 4 --dsl mixed --allocation erc --redis embedded --duckdb data/swarm/analytics.duckdb
```

`--sde-policy` takes a run id, a prefix (`sp500_s2`, the newest match wins) or a directory holding `policy.pt`. It turns on three things:

1. **Policy proposals.** `GFlowNetPolicy.load_state_dict(torch.load(policy.pt))`, sampled with a seeded generator under `no_grad`; `--policy-share` of every
   generator batch (default 0.5) comes from it, tagged `source=sde_policy`. They pass exactly the same gates as every other proposal
   (grammar and node limit → degenerate check → AST hash/novelty/TED >= 0.35 against everything tried → worker re-validation → audit).
   An AST the SDE already evaluated (read from the SDE ledger) is a counted `sde_seen` duplicate, not re-evaluated.
2. **SDE pool re-evaluation.** `runs_sde/<run>/pool.json` members are proposed once as `source=sde_pool` and run through the *same* worker/auditor
   (so they face the swarm's CPCV/DSR/SPA at the global N, not the SDE's own bar). No parallel implementation: workers call
   `src.portfolio.long_short.{tradable_mask, zscore_rows, leverage_normalized_weights, backtest}` and the Auditor `src.validation.*`; the trader's IC is
   `src.portfolio` IC. `test_swarm_connect.py::test_swarm_and_sde_evaluators_agree_on_returns` asserts the swarm net-return vector equals
   `phase3_eval.trial_returns` (rtol 1e-6) on the same panel and the same AST hash.
3. **Shared ledger.** Every swarm trial (accepted *or* rejected) is appended to `src/audit/ledger.jsonl` (hash-chained, flock) as
   `kind:"trial", origin:"swarm", universe:"swarm:sp500"` (no `ic`, so the SDE's duplicate logic and `phase3_eval.ledger_trials` ignore it) and every audit
   verdict as `kind:"swarm_audit"`. A re-audit that changes a verdict is appended as a superseding line (the ledger is append-only).
   The swarm resumes the mirror from the ledger itself (highest mirrored `swarm_trial_id` for this db id, under a flock), so re-running never duplicates.

### The N rule (no frozen baseline)

`N = engine N (data/state.json) + SDE ledger `trial` lines excluding origin:"swarm" + swarm rows`. Engine and SDE parts are **re-read live** at every run start,
every audit pass (`maybe_refresh_baseline`) and at the end of a run (report keys `baseline`, `baseline_at_end`, `global_count`); they are cached by file size/mtime.
The old hard-coded 84,610 is gone. `global_count()` reports the swarm's view and the SDE ledger's view and `in_sync`; swarm rows are counted once because
mirrored lines are excluded from the SDE-side term. If the engine hunts while the swarm runs, the next audit pass sees the larger N.

### Degenerate formulas (free rejects)

`simplify.py` detects `self_cancel` (`Sub(x,x)`), `self_ratio` (`Div(x,x)`), `redundant_term` (a self-cancelling sub-term inside an Add/Sub), `div_by_const0`,
and `constant` signals. The miner rejects them before a trial is costed (`REJECTED_DEGENERATE`, no trial id, no N) and reports them in
`stats["degenerate"]` / the `degenerate_rejected` event; the worker re-checks. SDE pool results are not altered: degenerate members are simply not re-proposed.
Several SDE pool members are of this form (the SDE spends trials on them; the swarm does not).

### Dialects

Default is the SDE grammar. `--dsl ext` (or `mixed`) enables the opt-in blueprint operator set in `dsl_ext.py`: features `close high low volume returns tp`; ops
`add subtract multiply divide abs log sign ts_mean ts_std ts_delta ts_decay_linear cs_rank cs_normalize` (look-back 1-252); <= 10 nodes, operator depth <= 4;
the draft-07 JSON schema is validated; blueprint "forbidden" operators (`future_shift`, `lookahead_max`, `unadjusted_close`, `target_return`) are syntax errors.
Evaluation is torch `unfold` on the swarm path and cross-checked against an independent numpy/pandas reference; causality is tested. `open` and `vwap` are
impossible: the panel is daily OHLCV-adjusted with no open/vwap column. `$`-prefixed SDE formulas stay SDE-only unless `allow_ext` is set, so default behaviour and every
SDE number are unchanged. The standalone survivor script supports both dialects.

### Cost, trader, signing, coordination

* **Square-root impact** (`costs.py`, default on in the CLI; `--no-impact`): slippage per asset = η·(|Δw|·AUM/ADV$)^0.5·σ with η=1, AUM $50M, 20-day trailing ADV$ and σ
  through t-1 (no look-ahead; NaN → cross-sectional median), added to the flat 5 bp. Per-asset trades are computed from the backtest's own drifted weights and
  asserted to sum to the backtest turnover. The cost vector is stored with the returns; the Auditor re-applies it per CPCV fold.
* **Sign handling**: the worker stores the sign +1 gross/turnover/cost (the Auditor re-orients per fold) and the exact flipped-book net when sign = -1, as the SDE flips
  the signal (a flipped book's pre-trade weights drift differently at second order, so `-W` is not exactly `W` under impact).
* **Trader**: modified Gram-Schmidt orthogonalises each candidate against the pool signals (`orth_residual_frac/ic` recorded); admission is still ρ < 0.30 and ΔIC > 0 on the
  equal-weight pool (so the directive's rule is unchanged); after each admission `allocate()` stores `allocation` in the ledger meta: Ledoit-Wolf shrinkage covariance,
  ERC (log-barrier) or max-Sharpe MVO (SLSQP, long-only simplex; ERC fallback when no positive mean), 5% per-asset cap on the combined book. `--allocation mvo|erc|equal`.
* **Signed bundles**: Ed25519 per role (miner signs tasks, worker signs result digests including the return vectors, auditor signs verdicts); keys in
  `data/swarm/keys/<role>.key` (0600, O_EXCL create). Workers refuse a task with a bad signature; the Auditor rejects (gate `signature`) a result whose digest does not verify;
  the Trader refuses an unsigned/forged APPROVED verdict. **Honest scope**: all roles run as the same OS user on one box, so this is integrity/provenance against accidents and
  tampering with the DB, not a security boundary against someone who can read the key files.
* **Redis** (`--redis embedded|redis://…`): accelerator only; SQLite stays authoritative. Hint queue of pending ids (a claim still goes through `BEGIN IMMEDIATE`), Redlock-style
  audit lock with TTL, heartbeats, an N counter mirror with drift reconciliation. If Redis dies everything degrades to the SQLite path. `embedded` starts a private `redis-server`
  (apt `redis-server` 8.x) or falls back to fakeredis.
* **DuckDB** (`--duckdb path`): incremental analytics mirror of trials (funnel by source/status, novelty-subtree support). The SQL blacklist is tested equal to `NoveltyMemory.blacklist()`.

## Components (`engine/swarm/`, `engine/vault/publisher.py`)

| Module | Role |
|---|---|
| `shared_ledger.py` | SQLite WAL trial manager. Every proposal (accepted **or** rejected) is one trial; `BEGIN IMMEDIATE` makes N_trials counting and task claiming atomic across processes. Lease-based queue (300 s lease, 3 attempts). Tables: trials, returns, pool, events, llm_requests, meta. |
| `miner.py` | Generator with six personas plus LLM ingestion. Screens every proposal: syntax (grammar, 32 nodes) → novelty (normalised Zhang-Shasha TED >= 0.35 against every earlier formula; frequent-subtree avoidance: subtrees of depth <= 3 and size >= 3 in > 15% of history are blacklisted) → task JSON. After > 3 consecutive structural rejections it "reheats" (temperature 0.9). |
| `ast_json.py`, `novelty.py` | AST <-> JSON payloads (strict re-validation in the worker); TED with an exact label-multiset lower bound shortcut (cross-checked against the `zss` library on 200 pairs). |
| `tensor_eval.py`, `worker.py`, `data.py` | Formula evaluation with torch (`unfold`, no time loops, asset-block chunking with halve-on-OOM retry, GPU if present, CPU here) matching `src.dsl.grammar.evaluate`; long-short dollar-neutral leverage-normalised backtest from `src.portfolio.long_short`, 5 bp one-way cost. Logs net/gross/turnover vectors + metrics to the ledger. Long/short **sign is chosen on train 2010-2016 only**. |
| `auditor.py` | The four gates below. |
| `trader.py` | Factor pool: pairwise signal correlation, marginal IC. |
| `llm.py` | `MailboxLLM` (file mailbox, async), `OpenAICompatLLM` (optional HTTP, env `SWARM_LLM_BASE_URL/API_KEY/MODEL`). |
| `cluster.py`, `cli.py` | Coordinator and the `swarm-*` subcommands registered in `engine/hunt_engine/cli.py` (additive change). |
| `engine/vault/publisher.py` | Survivors → `engine/vault/survivors/<hash>/{survivor_alpha.py, tearsheet.html, returns.csv, manifest.json}` + one MLflow run each. |
| `engine/dsl/grammar.py` | Shim re-exporting `src.dsl.grammar` (the blueprint's path). The DSL itself lives in `src/dsl/`. |

All validators are the SDE's own (`src/validation/{dsr,cscv,cpcv,spa}.py`, `src/portfolio/*`); nothing under `src/` was changed.

## The four audit gates (a formula needs all four)

1. **CPCV purge + embargo**: 10 groups, 2 test groups (45 splits, 9 paths), purge 20 rows (label horizon), embargo 5. A formula has no
   fitted parameters except its long/short sign, so CPCV here guards exactly that: the sign is re-chosen on the *purged* training rows
   of each split and applied out of sample. Pass: median path Sharpe > 0 and >= 80% of paths positive (the 80% is our choice).
2. **PBO < 0.10 via CSCV** (16 slices, 12,870 splits) over the *cohort*: the audited batch plus recent evaluated trials (cap 100).
   PBO describes a selection procedure, so it is cohort-level, and every member of a cohort shares one value.
3. **DSR p-value < 0.05** (p = 1 − DSR) using the **global** N_trials and the cross-trial variance of per-period Sharpe ratios
   (empirical from 10+ trials).
4. **Hansen SPA**: stationary bootstrap (1,000 resamples, mean block 10) with consistent re-centring against the zero benchmark; a candidate
   passes if its studentised statistic beats the bootstrap distribution of the *maximum* statistic over the cohort (family-wise 5%).

Verdicts and every gate's numbers are stored as JSON on the trial row (`audit_json`).

### N_trials baseline offset

N_trials = **baseline offset + swarm rows**. The baseline is read once, read-only, when the ledger is first used and stored in `meta`:
engine N (1,498, `engine/ledger/state.json`) + SDE trial entries (83,112, `src/audit/ledger.jsonl`, `kind: trial`) = **84,610**.
Rationale: the same data has been searched before, so the swarm's deflation bar must be no looser than the cumulative search. This is
deliberately conservative (SDE trials ran on other markets/windows too); it is a decision, not a measurement, and can be changed in the
`meta` table (`SharedLedger.set_baseline(..., overwrite=True)`) before auditing.

### Data caveat

The panel is the SDE's S&P 500 loader, which its own docs call survivorship-biased (current constituents' history, point-in-time membership
mask where available). The strongest dry-run formulas are price-level contrasts (`Log(Add($close, ...))`) with annual search Sharpe ~1.9,
which is the signature of that bias rather than of an edge. DSR rejects them at N ≈ 85k; treat any future survivor with the same suspicion
and re-score it on the PIT windows (`src/` PIT tool) before believing it.

## Trader

For each APPROVED formula (ledger order): max |mean daily cross-sectional correlation| with every pool member must be < 0.30, and
ΔIC = IC(equal-weight pool + candidate) − IC(pool) must be > 0 (IC = mean daily rank-free cross-sectional IC vs the 20-day forward
return, SDE definitions). Pool cap 50. Decisions are logged (`INTEGRATED`, `REJECTED_CORRELATED`, `REJECTED_NO_DELTA_IC`, `REJECTED_POOL_FULL`,
`REJECTED_BAD_SIGNATURE`). Gram-Schmidt residual diagnostics and ERC / MVO allocation weights: see "Cost, trader, signing, coordination".

## Publisher

`survivor_alpha.py` depends on numpy + pandas only (tested in a clean interpreter from another directory with empty `PYTHONPATH`, and
numerically equal to the swarm's own backtest to 1e-9). Run it directly for a self-test, or import `compute_signal` / `target_weights` /
`backtest`. `tearsheet.html` is a QuantStats report of the search-window net returns. MLflow uses a **SQLite** store at
`data/swarm/mlflow/mlflow.db` (MLflow's file store is in maintenance mode and refuses to start by default). Survivors are **research
candidates**: long-short, not tradable on the desk, never seen 2018-2020 or any sealed holdout; the next step for any survivor is the
SDE's untouched test years and then the engine's one-shot `vault-test`, not capital.

## Deviations from the blueprint

See [swarm_vs_blueprint.md](swarm_vs_blueprint.md) (table: item → done / changed / impossible → reason).

## Honest expectations

Bounded dry run on the real S&P 500 search window, 2026-10-24 (`swarm-start --sde-policy sp500_s2 --workers 4 --max-trials 150 --redis embedded --duckdb …`, ~75 s,
two consecutive runs): 300 new formulas (policy / pool / generator sources), 0 approved, **0 survivors**, nothing published; every audited formula (598 in the ledger) failed DSR; most also failed SPA, and
many CPCV. Live N at the end: engine 2,578 + SDE 109,479 + swarm 1,188 = 113,245 = the SDE ledger's own count (`in_sync`). 104 degenerate samples were rejected free in the
second run. A first version of that run had workers unsigned in the cluster and every audit failed on the `signature` gate; that was a bug, fixed (CLI regression test), and the 150
affected formulas were re-audited on merit (superseding `swarm_audit` lines in the SDE ledger).

The null result is the expected one. With N ≈ 112k (engine + SDE + swarm, read live) the DSR bar is very high; in the first real 300-formula dry run every formula failed
DSR and none survived (see the report in the commit message / `swarm-status`). Rejected formulas are kept (with all gate numbers), because
they are the evidence for what N means. Do not read PBO < 0.10 on a cohort of look-alike formulas as evidence of an edge.

## Tests

`cd engine && ../.venv17/bin/python -m pytest -q` (engine suite: 96 tests = the original 55 + 19 connection + 21 blueprint-feature + 1 CLI signing regression; `tests_sde/` has the SDE's 76): real multiprocessing counting and claiming;
TED/frequent-subtree constraints; tensor == SDE evaluator, causality; auditor on known-null (0 survivors) vs planted-signal data;
trader ρ/ΔIC; publisher end-to-end incl. standalone script; mailbox protocol with a fake responder; OpenAI-compatible backend
against a local fake server; CLI bounded run, SIGTERM in continuous mode, no orphans. LLM-sourced proposals (`source=llm:<id>`) are tested through the ledger with a fake responder. **The live Swarm Miner agent
(agent-in-the-loop) path has never been run.**
