# Strategy Discovery Engine (SDE) — implementation plan

Source: Aayan's Google deep-research blueprint (2026-10-23). Per Aayan (2026-10-23 ~8:19 PM ET) the blueprint is
followed **exactly**: module paths, long-short leverage-normalized weights (Phase 3), dataset splits
(CSI300/500/1000 train 2010–2020 / val 2021 / test 2022–2024; S&P500 train 2010–2016 / val 2017 / test 2018–2020),
and the benchmark table as the reported acceptance targets. Results are reported honestly against each target;
nothing is fabricated. Research only: never touches the live desk, orders, or vault data.
Every trial is recorded in the blueprint's append-only ledger (Phase 4, `src/audit/ledger.jsonl`).

## Status
- Phase 1 (DSL + RGCN): DONE — `src/dsl/grammar.py`, `src/models/rgcn_encoder.py`, tests `tests_sde/test_phase1.py`.
  Blueprint assertions pass verbatim. Extra: invalid-syntax rejection, MaxLen=32, SHA-256 canonical hash,
  300-tree fuzz (parse/eval/encode), no-lookahead test (perturbing rows >= t cannot change rows < t).
  Implementation note: r1/r2 messages flow operand->operator (operator aggregates children), r3 = W_0 self-loop.
- Phase 2 (GFlowNet policy, multi-faceted reward + factor pool, ledger, data loader, vectorized TsStd): DONE 2026-10-23 — see `docs/sde_phase2.md` (first CSI300 run: pool 1/1/0 of 50, no out-of-sample IC).
- Phase 3 (long-short portfolio, combiner, DSR/CSCV/CPCV/SPA, Ville e-process, multi-universe runs): DONE 2026-10-23 for CSI300 and S&P 500 — see `docs/sde_phase3.md`. No blueprint target met. CSI500/CSI1000 were deliberately stopped partway (13,600 / 5,800 of 20,000 episodes) at Aayan's request on 2026-10-24: not scored, no results, not a method failure (Chinese markets are not tradable by the desk; hours of compute). Focus moved to US stocks: S&P 500 seeds 1 and 2, then a survivorship-reduced S&P 500 addition. The ledger snapshot was refreshed (`src/audit/ledger_20261024.jsonl.gz`).
- Phase 4 (append-only ledger + e-process promotion gate): the components are built (`src/audit/ledger.py` in Phase 2, `src/validation/eprocess.py` writing `candidate`/`escore` rows in Phase 3). The blueprint's full Phase-4 definition is not on the box; anything beyond these is an open question (see `docs/sde_phase3.md`).

## Data plan (Phase 2+)
Free public sources: Qlib public cn_data / us_data, akshare for CSI constituents, yfinance for S&P500.
Survivorship caveat: free constituent lists are typically *current* members; delisted names are missing,
which biases returns upward. Will be logged per run.

## Citation check (fact record)
"Benhamou et al. (2026)" is real: E. Benhamou, J.-J. Ohana, B. Guez, T. Jacquot, E. Setrouk, C. Saadi (Ai For Alpha),
"Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents",
SETSCI, published 2026-10-06, doi:10.36287/setsci.25.3.001. Abstract matches the blueprint's numbers
(94.5% unadjusted crossings vs 0/3,000 funded; 1.77% adaptive; 2015–2026 replay promotes no rule after costs).
Note its library was 24 calendar rules on ETFs/FF industries, not alpha factors.
