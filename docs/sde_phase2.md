# SDE Phase 2 — GFlowNet search, reward, ledger, data (2026-10-23)

Research only. No trading, no broker keys, no market data or secrets committed.

## What was built
| Path | Purpose |
|---|---|
| `src/audit/ledger.py` | Append-only, hash-chained JSONL trial ledger (flock + fsync, `verify()` detects edit/delete/reorder). Built first; every sampled formula is one trial. Feeds DSR N, PBO, Ville e-process (Phase 4). |
| `src/data/loader.py` | CSI300 from Qlib public cn_data (read directly from the qlib_bin files; point-in-time membership), akshare fallback, S&P 500 via yfinance. Blueprint splits. Cache in `data/sde/` (gitignored). |
| `src/dsl/grammar.py` | `TsStd` vectorized (pandas rolling kernel; python loop kept as `_ts_std_loop` for cross-checks). |
| `src/gflownet/policy.py` | Policy over 24 actions, prefix-order AST construction with validity masks (MaxLen 32), RGCN 128-d embedding -> MLP -> logits, Trajectory Balance (learned log Z, P_B = 1) + entropy term. |
| `src/rewards/multi_faceted.py` | R = \|IC\| + λ(T)·R_SA + η(T)·R_NOV (AlphaSAGE Eq. 9–14, λmax 1.0, ηmax 0.3, linear anneal); `FactorPool` (IC ≥ 0.03, ICIR ≥ 0.35, reject \|corr\| > 0.70, capacity 50). |
| `src/train/train_gfn.py`, `evaluate_pool.py` | Training on the train split only (val/test prices never loaded); one-shot val/test read of the final pool. |
| `tests_sde/test_phase2.py`, `conftest.py` | 33 new tests. |
| `runs_sde/csi300_s{0,1,2}_20261023/` | config, final pool, val/test evaluation (model weights and curve.csv stay local, gitignored). |
| `src/audit/ledger_<date>.jsonl.gz` | Snapshot of the ledger (the Phase 2 snapshot had 30,012 entries; the 2026-10-24 refresh `ledger_20261024.jsonl.gz` has 71,707, head hash `10cedad9…8dd3`). `gunzip` then `Ledger(path).verify()`. |

## Choices the blueprint text I had does not pin down (all logged in `config.json`)
- **24 actions**: the DSL defines 14 tokens (4 features, Log, TsStd, Add, Sub, Div, 4 windows, SEP). The other 10 slots are reserved and permanently masked so the head is 24-wide without inventing operators. If the blueprint has a specific 24-token list, tell me and the vocabulary changes in one place.
- Label: 20-day forward return `close[t+20]/close[t]-1` (AlphaGen/AlphaSAGE), purged at split ends. Factor evaluated on point-in-time CSI300 members.
- Hyper-params from AlphaSAGE Table 4 (hidden 128, entropy 0.01, lr 1e-4, pool 50, 10,000 episodes). Not specified there: update every 16 episodes, log Z lr 0.1, KNN K = 5, empty pool => R_SA = 0, R_NOV = 1. Factor sign is taken from train IC (`|IC|` as in Eq. 12).
- Root must be an operator (a bare feature is not a formula); P_B = 1 (each partial AST has one parent), so Add(a,b)/Add(b,a) are two paths to one formula.

## First CSI300 run (train 2010–2020; 3 seeds × 10,000 episodes, ~40 min each on 1 CPU core, ~0.25 s/episode)
Real numbers, no tuning after seeing them.

| Seed | Pool size | Train IC / ICIR | Val 2021 IC / ICIR | Test 2022–24 IC / ICIR |
|---|---|---|---|---|
| 0 | 1 | 0.0435 / 0.354 | −0.0200 / −0.191 | 0.0058 / 0.053 |
| 1 | 1 | 0.0411 / 0.357 | 0.0039 / 0.023 | −0.0036 / −0.028 |
| 2 | 0 | — | — | — |

(IC = mean daily cross-sectional Pearson; sign fixed from train. Pool members: seed 0 `TsStd(TsStd(Log(Sub(Log(Sub(Add($close, Add($volume, Log(Add($high, Div(...))))…` (32 nodes), seed 1 `TsStd(Log(TsStd($volume, 5d)), 60d)`; full text in `pool.json`.)

Across all 30,000 trials (23,457 distinct formulas): best |IC| 0.0435, best |ICIR| 0.357; 215 trials had |IC| ≥ 0.03, 2 had |ICIR| ≥ 0.35, and exactly those 2 passed both (they are the two pool members). Median |IC| 0.0145. 320 trials were degenerate (constant/NaN).

### Against the blueprint targets
- Phase 2 can report only IC/ICIR/pool. **Pool size**: 1/1/0 vs. a 50-capacity pool — **missed**. **IC ≥ 0.03 and ICIR ≥ 0.35**: met on train by 2 formulas, only just (ICIR 0.354/0.357), and **failed out of sample** (val/test IC ≈ 0, ICIR ≈ 0): the two admits look like selection noise from 30k trials, not edges.
- Sharpe ≥ 5.5, annual return ≥ 18%, PBO ≤ 10% and the other portfolio targets need the Phase 3 long-short portfolio; **not measured yet**. CSI500/1000 and S&P 500 runs not done (S&P loader tested on 8 tickers only, current-constituent list = survivorship-biased).
- Learning did not visibly improve search quality: mean |IC| of sampled formulas was flat (0.0140 → 0.0132 first vs last 1,000 episodes) while mean formula size grew from ~10 to ~29 nodes. Reasons I can see: with an annealed SA/NOV bonus (up to 1.0 + 0.3) the reward is almost flat for most of training, so the sampler drifts toward the (much more numerous) large trees; the DSL has only 4 raw fields, Log, rolling std and +,−,÷ (no returns/lag/rank operators), so strong signals are scarce; and 10k updates/16 at lr 1e-4 is a short training budget. These are findings, not fixes — nothing was adapted.

## Caveats
- Qlib prices are adjusted and normalized per stock (ratios valid, absolute levels not). Membership is point-in-time; delisted names are included as Qlib provides them.
- yfinance/akshare fallbacks are survivorship-biased (current constituents) and flagged in `Panel.meta`.
- The test split was read once per run (3 reads total); the ledger contains the 9 `eval` entries. The search never saw val/test prices.

## Tests
`.venv17/bin/python -m pytest tests_sde` → 48 passed (15 Phase 1 + 33 Phase 2). `cd engine && ../.venv17/bin/python -m pytest` → 18 passed.

## Phase 3 needs
Long-short leverage-normalized portfolio construction and costs, Sharpe/return/drawdown/turnover vs the blueprint's target table, DSR + CSCV/PBO (< 0.10) + CPCV + SPA on the ledger's N, the Ville e-process over the append-only ledger, the factor-combination step on the pool, the CSI500/1000 and S&P 500 runs (needs a point-in-time S&P membership source to avoid survivorship bias), and a decision on the 24-token vocabulary and reward-flatness issue above.
