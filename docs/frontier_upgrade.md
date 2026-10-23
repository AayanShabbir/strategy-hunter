# Frontier upgrade note — Strategy Hunter engine (2026-10-23)

Research side only. No orders, no desk config, no live keys. The pass bar and the sealed 12-month vault are unchanged.

## What the current open-source frontier does (and what we took)
| Project / method | What it offers | Adopted here |
|---|---|---|
| **vectorbt / vectorbt PRO** (polakowo) | Vectorised, numba-compiled backtests over large parameter grids | Already the simulator; random-entry control now numba-compiled too (~20x: 2.1 s → 0.11 s per 1,000 twins on 1,500×5) |
| **NautilusTrader** | Event-driven, Rust-core backtest/live parity | Kept as the separate confirmation harness in `nautilus/` (not in the search loop — too slow for mass search) |
| **Microsoft Qlib + RD-Agent(-Quant)** (2024–25) | LLM agents propose factors/models, then run them through a fixed evaluation loop | `hunt generate --schema` exposes the spec grammar as JSON so an LLM proposer can emit specs; every one still goes through pre-registration |
| **Alpha-GPT / AlphaGen / LLM alpha mining** | Human/LLM-in-the-loop or RL formula search | Same interface; deferred: the actual LLM proposer loop |
| **gplearn (genetic programming)** | Symbolic formula search | Deferred (large implicit N; needs trial accounting first — now available) |
| **Optuna (TPE)** | Efficient hyper-parameter search | `hunt optimize`: IS-only objective, **every trial reserved in the ledger before it runs**, top-k re-queued to face the full bar |
| **CPCV** (López de Prado, *AFML* ch. 12) | Many back-test paths instead of one split | `CPCV` diagnostic per variant (C(6,2)=15 paths: median Sharpe, % positive). Reported, not a gate |
| **PBO / CSCV** (Bailey, Borwein, López de Prado, Zhu 2014) | Probability the IS-best is OOS-mediocre | Already a gate |
| **Deflated Sharpe / False Strategy Theorem** (Bailey & López de Prado 2014; LdP 2018) | Sharpe hurdle grows with number of trials | Already a gate at ledger-wide N; Optuna trials now feed N |
| **Hansen SPA / Holm** | Data-snooping-robust tests | Already gates |
| **FinRL** | Deep-RL trading envs | Not adopted: RL on <10y daily bars overfits; no credible OOS edge in the literature at our data size |

## Implemented today
1. Sharpe annualisation: √365 for crypto (symbols with `/`), √252 for stocks (`gauntlet.ann_factor`). Earlier crypto Sharpes were understated by ~17%; no pass/fail changes (Sharpe isn't a gate; DSR uses per-period SR).
2. numba random-entry twin (`fast=True` default; pure-Python reference kept, test checks they agree in distribution).
3. CPCV path diagnostic in every result.
4. Drawdown diagnostic `dd_improvement_vs_bh` (+ = shallower OOS max-DD than buy-and-hold) and `--objective calmar` for Optuna. Diagnostic only; the beats-buy-and-hold gate stays.
5. `day_of_week` filter.
6. Grammar spec generator (`hunt generate`), LLM-ready schema.
7. Optuna search with honest ledger counting (`hunt optimize`).
8. Fix: queue ordering used the symlink target's mtime; now `lstat` (pre-existing test failure).

## Deferred (and why)
- **Vol-targeting / position sizing**: the random-twin and cost model assume 0/1 sleeves; changing that needs a matched sizing in the control first.
- **Drawdown-based *gate*** (instead of beats-B&H): changes the pass bar, needs Aayan's sign-off.
- **LLM proposer loop, gplearn**: interface ready; needs a nightly N budget decision because they inflate N fast.
- **polars data layer, Databento futures data**: no bottleneck there yet / paid data.

## Sources
- vectorbt: https://github.com/polakowo/vectorbt · vectorbt PRO: https://vectorbt.pro
- NautilusTrader: https://github.com/nautechsystems/nautilus_trader
- Qlib: https://github.com/microsoft/qlib · RD-Agent: https://github.com/microsoft/RD-Agent · R&D-Agent-Quant paper: https://arxiv.org/abs/2505.15155
- Alpha-GPT: https://arxiv.org/abs/2308.00016 · AlphaGen: https://github.com/RL-MLDM/alphagen
- FinRL: https://github.com/AI4Finance-Foundation/FinRL · gplearn: https://github.com/trevorstephens/gplearn
- Optuna: https://github.com/optuna/optuna (Akiba et al., KDD 2019)
- Bailey et al., "The Probability of Backtest Overfitting" (2014): https://ssrn.com/abstract=2326253
- Bailey & López de Prado, "The Deflated Sharpe Ratio" (2014): https://ssrn.com/abstract=2460551
- López de Prado, *Advances in Financial Machine Learning* (2018), ch. 7 & 12 (purged k-fold, CPCV)
- López de Prado & Bailey, "The False Strategy Theorem" (2018/2021): https://ssrn.com/abstract=3221798
- Hansen, "A Test for Superior Predictive Ability" (2005), via `arch` (K. Sheppard)
