# SDE Phase 3 — portfolio, validity checks, pool combination, multi-universe runs

Status date: 2026-10-23 (America/New_York). Research only: no orders, no broker keys, no secrets or price data committed.
Every number below is produced by `src/train/phase3_eval.py` and stored in `runs_sde/<run>/phase3.json`
(tables regenerated with `python -m src.train.phase3_table`).

## What was built

| module | content |
|---|---|
| `src/portfolio/long_short.py` | long-short **leverage-normalized** weights `w = G (s - mean s) / sum|s - mean s|` (dollar-neutral, gross = 1 every day), drifted-weight turnover, bps cost per dollar of one-way turnover, Sharpe/AR/MDD/turnover (AlphaSAGE App. D.1: K=252, r_f=0) |
| `src/portfolio/combine.py` | pool combination: AlphaForge-style dynamic filter + linear regression ("Mega-Alpha", AlphaSAGE Sec. 3.5) and the static equal-weight ensemble as a reference |
| `src/validation/dsr.py` | Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014) with the ledger's N |
| `src/validation/cscv.py` | CSCV / PBO (16 slices, all 12,870 IS/OOS splits) |
| `src/validation/cpcv.py` | Combinatorial Purged CV (10 groups, k=2 -> 45 splits, 9 paths, purge 20 days, embargo 5) |
| `src/validation/spa.py` | Hansen SPA (stationary bootstrap, studentised; lower / consistent / upper p-values) |
| `src/validation/eprocess.py` | Ville e-process promotion gate ("Promote", Benhamou et al. 2026) written into the hash-chained ledger (`candidate` + `escore` rows) |
| `src/train/phase3_eval.py` | scores one finished run; writes `phase3.json` and a `p3_eval` ledger entry |
| `tests_sde/test_phase3.py` | 25 tests (weights, costs, causality, DSR/CSCV/CPCV/SPA calibration, e-process null rate, budget, ledger chain, end-to-end smoke) |

### Definitions used (and where they come from)
* **Portfolio**: signal known at close t, weights set at close t, earned over close t -> t+1, rebalanced daily, gross leverage 1, net 0.
  Cost: **5 bp per $ of one-way turnover** (the Promote paper's replay cost; it also uses drifted pre-trade weights). 0/5/10/20 bp sensitivity is reported.
  Not modelled: shorting borrow/availability (CSI300/500/1000 shorting is in practice restricted — the blueprint's long-short math is applied as written), spreads/impact beyond bps, limit-up/down, capacity.
* **Combination**: at each 20-day refresh, keep members whose trailing (250-day, label-purged) IC is > 0, regress the z-scored 20-day forward return on their z-scores (pooled cells, ridge 1e-6), combined signal = sum beta_k z_k for the next 20 days. Labels used at refresh t only for days <= t-20 (tested). The first 270 train days are flat (no label history yet) and are excluded from train metrics.
* **DSR**: N = ledger trial count (total over all universes at evaluation time = conservative; universe-only N also stored). V[SR_n] = variance of per-period long-short Sharpe over a random 200 distinct ledger formulas of that universe (train window, sign by train IC). DSR is reported on train and on test; headline = test, N total.
* **CSCV/PBO and SPA family**: the top-100 distinct ledger formulas of the universe by |train IC| (+ pool members), sign from train IC, daily net long-short returns. PBO uses train+val only (never test). SPA (H0: best candidate does not beat zero) uses the test split. A second SPA on the combined portfolio alone is also stored (a single candidate, so it is a plain bootstrap test).
* **CPCV**: static pooled OLS re-fit per split on purged/embargoed rows of train+val; path Sharpe distribution. With a 1-member pool the fit only decides the sign, so all 9 paths coincide (stated, not hidden).
* **Ville e-process**: exactly the paper's construction — clipped net score, scale = max(50 bp, train 99.5th pct |net|), mixture over lambda in {.025,.05,.10,.20,.35}, evidence restarts at 1 after birth (birth = last validation day, scoring = test days only), library of 8 equal slots (mass 1/8, alpha 0.05 -> boundary 160), delayed execution clock (credit starts at t+2), cumulative debit <= 1 enforced. It does not use N: the guarantee already covers the adaptive search because only post-freeze data counts.

## Results (cost 5 bp per side; test = out-of-sample split of the blueprint)

Blueprint targets available in `docs/sde_plan.md`: **Sharpe >= 5.5, annual return >= 18%, PBO <= 10%**; the plan says "among others" and the remaining rows of the target table are not stored anywhere on the box (see open questions). I additionally report the DSR (>0.95 convention), SPA p (<0.05) and e-process boundary.

<!--TABLE:main-->
| run | pool | N (total / universe) | combiner | test Sharpe | test AR | test MDD | test turnover/yr | val Sharpe | PBO | DSR test (N total) | SPA p (combined, test) | CPCV mean path SR | e-process (max / bound) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| csi300_s0_20261023 | 1 | 51623 / 30000 | rolling_ols | 0.04 | 0.11% | -6.5% | 11.2 | -0.50 | 74.4% | 0.000 | 0.500 | 0.49 | 1.90 / 160 |
| csi300_s0_20261023 | 1 | 51623 / 30000 | equal | -0.20 | -1.13% | -10.9% | 37.8 | -0.59 | 74.4% | 0.000 |  |  |  |
| csi300_s1_20261023 | 1 | 52604 / 30000 | rolling_ols | 0.01 | 0.03% | -7.0% | 10.2 | -0.28 | 74.4% | 0.000 | 0.475 | 0.76 | 1.54 / 160 |
| csi300_s1_20261023 | 1 | 52604 / 30000 | equal | -0.23 | -1.18% | -13.7% | 20.3 | -0.28 | 74.4% | 0.000 |  |  |  |
| csi300_s2_20261023 | 0 | 53584 / 30000 | - | no portfolio (empty pool) | | | | | 74.4% | | | | |
| sp500_s0_20261023 | 50 | 63900 / 20000 | rolling_ols | 0.49 | 3.76% | -10.7% | 116.7 | 1.27 | 56.7% | 0.000 | 0.158 | 0.87 | 2.33 / 160 |
| sp500_s0_20261023 | 50 | 63900 / 20000 | equal | 1.10 | 9.81% | -12.3% | 27.8 | 1.36 | 56.7% | 0.000 |  |  |  |
| sp500_s1_20261024 | 50 | 89479 / 40000 | rolling_ols | 0.02 | 0.15% | -16.3% | 134.0 | -0.29 | 60.0% | 0.000 | 0.477 | 0.90 | 1.13 / 160 |
| sp500_s1_20261024 | 50 | 89479 / 40000 | equal | 0.91 | 7.36% | -12.0% | 24.4 | 1.22 | 60.0% | 0.000 |  |  |  |
<!--/TABLE:main-->

Cost sensitivity of the rolling-OLS portfolio (test split):

<!--TABLE:cost-->
| run | cost (bps/side) | test Sharpe | test AR | test MDD | test turnover/yr |
|---|---|---|---|---|---|
| csi300_s0_20261023 | 0 | 0.22 | 0.67% | -6.3% | 11.2 |
| csi300_s0_20261023 | 5 | 0.04 | 0.11% | -6.5% | 11.2 |
| csi300_s0_20261023 | 10 | -0.15 | -0.45% | -6.8% | 11.2 |
| csi300_s0_20261023 | 20 | -0.50 | -1.58% | -7.9% | 11.2 |
| csi300_s1_20261023 | 0 | 0.16 | 0.54% | -6.7% | 10.2 |
| csi300_s1_20261023 | 5 | 0.01 | 0.03% | -7.0% | 10.2 |
| csi300_s1_20261023 | 10 | -0.14 | -0.48% | -7.3% | 10.2 |
| csi300_s1_20261023 | 20 | -0.45 | -1.50% | -7.9% | 10.2 |
| sp500_s0_20261023 | 0 | 1.24 | 9.59% | -6.8% | 116.7 |
| sp500_s0_20261023 | 5 | 0.49 | 3.76% | -10.7% | 116.7 |
| sp500_s0_20261023 | 10 | -0.27 | -2.08% | -19.0% | 116.7 |
| sp500_s0_20261023 | 20 | -1.78 | -13.75% | -37.3% | 116.7 |
| sp500_s1_20261024 | 0 | 0.78 | 6.85% | -12.7% | 134.0 |
| sp500_s1_20261024 | 5 | 0.02 | 0.15% | -16.3% | 134.0 |
| sp500_s1_20261024 | 10 | -0.75 | -6.55% | -26.2% | 134.0 |
| sp500_s1_20261024 | 20 | -2.27 | -19.94% | -47.4% | 134.0 |
<!--/TABLE:cost-->

### Reading the numbers (honest summary)
* **No run meets any of the three blueprint targets.** Best test Sharpe is below 1.2 (S&P 500 equal-weight, survivorship-biased); the target is 5.5. Best annual return 9.8% vs 18%. PBO is 74% (CSI300) and 57% (S&P 500) vs <= 10%. No candidate crosses the e-process boundary (max evidence ~2 vs 160).
* For scale: AlphaSAGE's own best published Sharpe in its Table 1 is 1.71 (CSI300, top-20% long-only), so the 5.5 target is ~3x the best number in the paper the search is built on; nothing here approaches it either.
* **CSI300**: pools have 1 member each (seed 2: none). Train IC ~0.04 does not survive: val IC -0.02 / +0.004, test IC +0.006 / -0.004. Net Sharpe on test 0.04 and 0.01, i.e. zero after 5 bp; negative at 10 bp.
* **S&P 500** (train 2010-16, val 2017, test 2018-20): pool is full (50 members). Out-of-sample IC is real-looking (test ensemble IC 0.063, ICIR 0.40) and the equal-weight long-short earns Sharpe 1.10 / AR 9.8% at 5 bp, but (i) **the universe is today's S&P 500 constituents (survivorship bias, yfinance has no point-in-time membership) which inflates a long-short book's returns and IC**, (ii) DSR with N = ledger total is 0.000 (SR0 ~ 4.6 annualised because trial Sharpe dispersion is large), (iii) PBO 57%, (iv) the dynamic rolling-OLS combiner trades ~117x per year and is cost-fragile (Sharpe 0.49 at 5 bp, negative at 10 bp). SPA over the top-100 family gives p = 0.007 on test (the best frozen candidate does beat zero before the family-wide cost of N), but the bias caveat applies.
* **Flat reward / missing operators**: not touched (see open questions); the SA/NOV terms still dominate the reward and the sampler drifts to large trees.

### S&P 500 additional seeds (US focus, added 2026-10-24; same blueprint settings as seed 0: 20,000 episodes, 2010-16 / 2017 / 2018-20)
All still **survivorship-biased** (today's constituents applied to all dates). N is the global ledger count at scoring time, so it is larger for later runs.
<!--SEEDS-->
* **seed 1 (`sp500_s1_20261024`)**: pool 50. Out-of-sample IC holds up but is weaker than seed 0: ensemble IC train 0.066 / val 0.038 / test 0.049 (ICIR 0.34; seed 0 test 0.063 / 0.40). Long-short test Sharpe: **rolling-OLS combiner 0.02 (AR 0.15%, MDD -16.3%, turnover 134/yr)**, **equal-weight 0.91 (AR 7.36%, MDD -12.0%, turnover 24/yr)**; at 0 bp the OLS combiner earns 0.78 and at 10 bp -0.75 (costs eat it: turnover is 134x/yr). PBO 60.0%, DSR(test, N=89,479) 0.000, SPA p 0.477 (single combined candidate), CPCV mean path Sharpe 0.90, e-process max 1.13 vs boundary 160. **No target met** (Sharpe >= 5.5, AR >= 18%, PBO <= 10%, DSR > 0.95, SPA < 0.05, e-process >= 160). Seed 1 reproduces seed 0's pattern: real-looking but small IC, a ~1.0 Sharpe only for the equal-weight book on the biased universe, nothing statistically significant after deflation.
<!--/SEEDS-->

## Runs
* CSI300: existing pools s0/s1/s2 (Phase 2, 10,000 episodes each, the paper's CSI300 setting) re-scored; no re-run (the blueprint setting is what was run).
* S&P 500: 20,000 episodes (AlphaSAGE App. D.2 setting for CSI500/S&P500), seed 0, splits 2010-16 / 2017 / 2018-20, survivorship-biased universe (`data_meta.survivorship = BIASED (current members only)`).
* CSI500 / CSI1000: **deliberately stopped partway at Aayan's request (2026-10-24 ~1:06 AM ET); not scored, no results, and not a failure of the method.** Reasons: Chinese A-shares are not tradable by the desk, and each run needed hours of compute. Last logged episodes: CSI500 13,600 of 20,000; CSI1000 5,800 of 20,000 (the buffered `curve.csv` files lagged at 10,100 / 5,100). The partial run folders (config, pool, curve, weights) were moved out of the repo to a local scratch directory and are not committed. Their sampled formulas remain counted as trials in the ledger (and therefore in N for DSR). Nothing is claimed for these universes.

<!--STATUS-->
CSI500 / CSI1000: stopped at Aayan's request, not scored (see Runs). US focus: S&P 500 seed 1 scored (above); seed 2 and the survivorship-reduced re-score are in progress (the table is regenerated after each is scored).
<!--/STATUS-->

## Blockers / things that could not be done exactly as written
1. The blueprint document itself is not on the box; `docs/sde_plan.md` only summarizes it. Unavailable to me: the exact long-short weight formula, the cost value, the combination step, the remaining rows of the target table. I used the formula described in the summary (leverage-normalized long-short), the Promote paper's 5 bp / drifted-weight cost convention and the AlphaSAGE Sec. 3.5 combination (the paper the blueprint is built on), and exposed every free parameter in `phase3.json` -> `combiner_params`.
2. S&P 500 point-in-time membership: not available from free sources -> survivorship-biased.
3. Dataset sizes limit CSCV/PBO to a top-100 family (not all ~23k distinct ledger trials).

## Open questions for Aayan / the blueprint
1. **Flat-reward problem** (SA 1.0 + NOV 0.3 swamp |IC| ~ 0.01-0.04): does the blueprint specify a fix (reward rescaling, smaller lambda_max/eta_max, rank-based reward)? Not adapted.
2. **Missing DSL operators** (return/lag/delta, cross-sectional rank, mean/correlation windows): which does the blueprint add? Without them the language only expresses volatility-of-volume style factors (all pools are TsStd/Log of volume-price differences).
3. **24-token vocabulary**: the real list is not in `docs/sde_plan.md`; 14 real tokens + 10 masked reserved slots remain.
4. Blueprint cost value, rebalance frequency, gross-leverage target, and the other rows of its target table.
5. Combination parameters (lookback / refresh / filter threshold) and whether combination should be re-tuned on validation.
6. Whether the N used in the DSR is the global ledger count (used here) or per universe/seed.
