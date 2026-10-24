# `runs_sde/` conventions

One folder per training run: `runs_sde/<universe>_s<seed>_<YYYYMMDD>/`.

| file | committed | content |
|---|---|---|
| `config.json` | yes | hyper-parameters, splits, data meta (incl. `survivorship` flag) |
| `pool.json` | yes | final factor pool (formulas, train IC/ICIR, sign) |
| `eval.json` | yes | one-shot val/test IC/ICIR of the pool (`train.evaluate_pool`) |
| `phase3.json` | yes | long-short metrics, cost sensitivity, DSR/CSCV/CPCV/SPA, e-process, combiner params (`train.phase3_eval`) |
| `curve.csv` | no (`*.csv`) | training curve |
| `policy.pt` | no (`*.pt`) | model weights |
| `*.log` | no | stdout of long jobs |

Rules: a run folder is committed only after it is scored (`phase3.json` exists); in-progress folders stay untracked. Market data lives in `data/` (git-ignored) and is re-downloadable. The live ledger `src/audit/ledger.jsonl` is never committed; refresh the gzip snapshot (`src/audit/ledger_<date>.jsonl.gz`) after `Ledger(path).verify()` passes, when no training job is appending.

Regenerate the result tables in `docs/sde_phase3.md`: `PYTHONPATH=. .venv17/bin/python -m src.train.phase3_table --inject docs/sde_phase3.md`.
