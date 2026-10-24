# Swarm vs. the blueprint (`/workspace/swarm_blueprint.md`)

Status: **done** (as specified), **changed** (deliberately different, reason given), **impossible** (cannot be done on this box / data),
**not run** (built and tested, never exercised live). 8 CPUs, 16 GB, no GPU.

| Blueprint item | Status | Reason |
|---|---|---|
| Miner / Worker / Auditor / Trader as separate processes on a shared trial ledger | done | SQLite WAL, `BEGIN IMMEDIATE` atomic N and leases; real multiprocessing tests. |
| Every proposal (accepted or rejected) is a trial and counts toward N | done | One ledger row each; degenerate formulas are the one exception, rejected free before costing (they carry no information). |
| Global N shared with the SDE ledger and the engine, no double count | done | N = engine N + SDE-own trials (live read, not a frozen number) + swarm rows; swarm rows mirrored to `src/audit/ledger.jsonl` with `origin:"swarm"` and excluded from the SDE-side term. |
| Trained GFlowNet as a proposal source | done | `--sde-policy`; same novelty/TED and worker/auditor gates as every source. |
| Reuse SDE portfolio / validation code | done | `src.portfolio.*`, `src.validation.*`; a test asserts the swarm and SDE net returns agree. |
| Richer operator set (`ts_mean`, `ts_decay_linear`, `cs_rank`, …) | done, opt-in | `--dsl ext|mixed`; SDE grammar and its results untouched. 10 nodes, depth 4, windows 1-252, JSON schema validated. |
| Features `open`, `vwap` | impossible | The panel is adjusted daily OHLCV for the S&P 500 with no open or vwap column; `tp = (h+l+c)/3` and `returns` are provided instead. |
| Forbidden operators (`future_shift`, `lookahead_max`, `unadjusted_close`, `target_return`) | done | Syntax errors in the ext grammar; causality of the evaluator is tested. |
| AST novelty: tree edit distance + frequent-subtree blacklist | done | Zhang-Shasha (exact label lower bound shortcut, cross-checked with `zss`); TED >= 0.35. Works on both dialects. |
| Tensor backtest (unfold, no time loops) | done | torch on CPU; asset-block chunking with halve-on-OOM. |
| GPU execution | impossible | No GPU on the box. Code is device-agnostic and untested on CUDA. |
| float32 / NaN policy | changed | float64 and explicit NaN masking, for exact agreement with the SDE evaluator; float32 is a speed trade not needed at this size. |
| Square-root market impact cost | done | η·(participation)^0.5·σ plus 5 bp, causal ADV/σ; trades tested to sum to turnover. Assumed AUM $50M, η=1: assumptions, not calibration. |
| Auditor gates: CPCV, PBO, DSR at global N, SPA | done | SDE `src.validation`. PBO/SPA are cohort-level (a per-formula PBO does not exist); the "80% positive CPCV paths" rule is a swarm choice. |
| Trader correlation threshold 0.40 | changed | Aayan's directive says ρ < 0.30; kept at 0.30. |
| Gram-Schmidt orthogonalisation in the Trader | done | Modified Gram-Schmidt; residual share and IC are recorded. Admission still uses the directive's ρ and ΔIC rule. |
| Risk-parity / MV weights | done | ERC and max-Sharpe MVO on a Ledoit-Wolf covariance, 5% asset cap. Weights are research output, nothing is traded. |
| Signed bundles | done, narrow scope | Ed25519 per role over task, result digest and verdict. Same OS user holds all keys: integrity and provenance, not a security boundary. |
| Redis queue / locks | done, as accelerator | SQLite remains authoritative; Redis gives a hint queue, audit lock, heartbeats and an N mirror, and everything works if it is down. A single node does not need it. |
| DuckDB analytics | done | Incremental mirror; SQL subtree blacklist tested equal to the in-process one. |
| Immutable survivor vault with point-in-time hash | done | sha256(AST ‖ float64 search returns ‖ timestamp), content-addressed manifest. |
| Docker image promotion, S3 object store | impossible / replaced | No container registry or S3 here; replaced by local content-addressed SHA256 files and manifest. |
| MLflow registry | done, best-effort | Registered model `swarm_survivors`, alias `research_candidate`, SQLite store. Skipped silently if MLflow fails. |
| LLM idea source (agent in the loop) | not run | Mailbox and OpenAI-compatible backends are built and tested with fake responders, and `llm:<id>` proposals are tested through the ledger. The live Swarm Miner agent path has never been run. |
| Survivors are tradable | changed | They are research candidates only. Long-short, search window 2010-2017, never saw 2018-2020 or the engine vault. Next step is the SDE test years then `vault-test`. |

## What the numbers say

The dry-run result is the expected null: with N around 113k, DSR rejects everything (see `docs/swarm.md`, "Honest expectations"). Zero survivors is a result, not a bug.
