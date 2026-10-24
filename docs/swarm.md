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
return, SDE definitions). Pool cap 50. Decisions are logged (`INTEGRATED`, `REJECTED_CORRELATED`, `REJECTED_NO_DELTA_IC`, `REJECTED_POOL_FULL`).

## Publisher

`survivor_alpha.py` depends on numpy + pandas only (tested in a clean interpreter from another directory with empty `PYTHONPATH`, and
numerically equal to the swarm's own backtest to 1e-9). Run it directly for a self-test, or import `compute_signal` / `target_weights` /
`backtest`. `tearsheet.html` is a QuantStats report of the search-window net returns. MLflow uses a **SQLite** store at
`data/swarm/mlflow/mlflow.db` (MLflow's file store is in maintenance mode and refuses to start by default). Survivors are **research
candidates**: long-short, not tradable on the desk, never seen 2018-2020 or any sealed holdout; the next step for any survivor is the
SDE's untouched test years and then the engine's one-shot `vault-test`, not capital.

## Deviations from the blueprint (and why)

* **Operators**: the blueprint JSON used a richer operator set; the repo's DSL has `Log, TsStd, Add, Sub, Div` over `$close $high $low $volume`.
  AST JSON and the LLM prompt use the real grammar. A richer grammar needs `src/dsl/grammar.py` changes (out of scope).
* **Path**: DSL is `src/dsl/grammar.py`, not `engine/dsl/grammar.py` (shim added).
* **Cohort-level PBO / SPA** instead of per-formula numbers (statistically they cannot be per formula), see above.
* **Storage**: SQLite WAL only. No Redis, no DuckDB (not trivial to add, and unnecessary at 8 CPUs).
* **Not implemented**: signed bundles / cryptographic signatures on task payloads (the worker instead re-hashes the AST), the square-root
  market-impact slippage model (flat 5 bp one-way; turnover > 12x and net Sharpe < 0.8 are recorded as informational flags, not gates),
  Gram-Schmidt orthogonalisation and risk-parity weights in the Trader (equal-weight pool), GPU path (code is device-agnostic but untested: no GPU on the box).
* The LLM layer was added by a later change of plan (file mailbox to a Grok Bot agent instead of an API key).

## Honest expectations

The null result is the expected one. With N ≈ 85k the DSR bar is very high; in the first real 300-formula dry run every formula failed
DSR and none survived (see the report in the commit message / `swarm-status`). Rejected formulas are kept (with all gate numbers), because
they are the evidence for what N means. Do not read PBO < 0.10 on a cohort of look-alike formulas as evidence of an edge.

## Tests

`cd engine && ../.venv17/bin/python -m pytest -q` (37 swarm tests + 18 engine tests): real multiprocessing counting and claiming;
TED/frequent-subtree constraints; tensor == SDE evaluator, causality; auditor on known-null (0 survivors) vs planted-signal data;
trader ρ/ΔIC; publisher end-to-end incl. standalone script; mailbox protocol with a fake responder; OpenAI-compatible backend
against a local fake server; CLI bounded run, SIGTERM in continuous mode, no orphans. **The live Swarm Miner agent has not been tested
by these tests.**
