# Architecture

## Top-level layout
```
research_lab/
├── engine/            LIVE. Strategy Hunter (hunt CLI, hunt_engine/, specs/, queue/, runs/, ledger/, vault/, tests/)
├── ledger/            LIVE. Human ledger README.txt (engine reads N from it; mirrored to trading-desk HUNT_LEDGER)
├── src/               SDE blueprint modules (module paths fixed by the blueprint)
│   ├── dsl/ models/ gflownet/ rewards/   search: grammar, RGCN encoder, policy, reward + pool
│   ├── data/ audit/                      Qlib/yfinance loader; hash-chained trial ledger
│   ├── portfolio/ validation/            long-short backtest, combiner; DSR, CSCV, CPCV, SPA, e-process
│   └── train/                            train_gfn, evaluate_pool, phase3_eval, phase3_table
├── tests_sde/         SDE tests (73)
├── runs_sde/          per-run artifacts (convention: docs/runs_sde.md)
├── hunts/ crypto/ reels/ nautilus/ vendor/   frozen hand-run research (see "Why research folders did not move")
├── docs/              design notes and per-phase reports (index: docs/README.md)
├── data/  .venv17/  .venv_ts/                git-ignored (market data, interpreters)
└── pyproject.toml Makefile .github/ ...      tooling
```

## Engine vs SDE vs research
* **engine/** is a self-contained, unattended system. Hourly search and nightly drain run `cd engine && ./hunt ...`; they write `engine/ledger`, `engine/queue`, `engine/specs`, `engine/runs`, mirror N to `ledger/README.txt` and `/workspace/trading-desk/validation/results/`, and commit to this repo. Pass-bar gates, the sealed vault and ledger-N counting are controlled changes (recorded in CHANGELOG with the approval).
* **src/** is the SDE. It shares only the principle (count every trial) with the engine, not code or state. Its ledger is `src/audit/ledger.jsonl` (hash-chained, flock-guarded, git-ignored; snapshot committed as `.jsonl.gz`).
* **research folders** are historical, pre-registered artifacts. They are not imported by either system (engine only mentions `vendor/pypbo` in a docstring).

## SDE data flow
`data.loader` (Qlib cn_data / yfinance, point-in-time for CSI, *survivorship-biased* for S&P 500) → `dsl.grammar` evaluates a formula on the panel → `rewards.multi_faceted` (|IC| + λ·SA + η·NOV, `FactorPool` cap 50) → `gflownet.policy` samples next formulas with trajectory balance. After training, `train.evaluate_pool` reads val/test once; `train.phase3_eval` builds the long-short book (`portfolio/`), runs `validation/` checks with N from the ledger, appends `candidate`/`escore`/`p3_eval` rows, and writes `runs_sde/<run>/phase3.json`.

## Sealed holdout (2021+) and the vault
`data/sealed_sde/` (git-ignored) holds the 2021-01-01→2026-10-22 S&P 500 panel that no search ever saw; `src/vault/sealed_manifest.json` is the committed SHA-256 pre-registration. `src/vault/vault.py` opens it at most once per candidate (spec hash), at most 3 times in total (`vault_config.json`), only for candidates pre-registered and APPROVED by the swarm auditor, with every step in the chained `src/vault/vault_log.jsonl`. `src/data/guard.py` + `tests_sde/test_sealed_guard.py` keep `src/`, `engine/hunt_engine` and `engine/swarm` from naming or importing it (a tripwire, not a security boundary). `src/portfolio/deployability.py` gives the long-only/flat check for survivors on the search window. `src/data/multisource.py` is the survivorship-reduced loader (`load_sp500` / `load_sp500_pit` are unchanged). See `docs/sealed_holdout.md`, `docs/data_quality_sp500.md`.

## Swarm (engine/swarm, engine/vault/publisher.py)
Miner → backtest workers → Auditor (CPCV, PBO, DSR at global N, SPA) → Trader (ρ<0.30, ΔIC) → Publisher, coordinated through an SQLite WAL trial ledger at `data/ledger/trials.db` and launched by `./engine/hunt swarm-start`. It imports the SDE's DSL and validators from `src/` and reads search data only (train 2010-2016 + validation 2017). It never touches the engine ledger/vault. Global N = engine N + SDE ledger trials, both re-read live at each run start/audit (no frozen number), + swarm rows; with `--sde-policy` the swarm mirrors its trials and verdicts into the SDE ledger (`origin:"swarm"`, appended under flock, excluded from the SDE-side term so nothing is counted twice) and uses the trained GFlowNet and pool as proposal sources. See `docs/swarm.md`, `docs/swarm_vs_blueprint.md` and `docs/swarm_llm_mailbox.md`.

## Invariants
1. Research only: no order code, no broker keys, no live routing.
2. Every sampled formula / variant is a counted trial *before* its result is seen.
3. Validation/test prices are not loaded during training; test split is read once per evaluation.
4. Append-only ledgers: never edited or rewritten; `Ledger.verify()` must pass.
5. No secrets, market data, vault data, weights or live ledger in git.
6. Nothing is evaluated on the sealed 2021+ set except through `src/vault/vault.py`, once per candidate, under the global look cap.

## Why research folders (`hunts/`, `crypto/`, `reels/`, `nautilus/`, `vendor/`) did not move
They would normally live under `research/`, but they are referenced by absolute path from pre-registered scripts (`hunts/h9.../run.py` imports `/workspace/research_lab/vendor/pypbo`, `hunts/h15_lit4/run_nfl.py` reads `hunts/h11_nfl_betting/data`), from the append-only human ledger and the external `/workspace/trading-desk/validation/results/HUNT_LEDGER.md` (both cite `research_lab/hunts/...` as the provenance of each result), and `engine/hunt` hard-codes the interpreter path. Editing frozen pre-registered scripts or rewriting historical ledger citations would defeat their purpose, so they stay in place and are documented here.
