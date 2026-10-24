# Strategy Hunter engine — guide for Strategy Scout (Phase 1)
Research/paper only. The engine has no order code and never reads/writes /workspace/trading-desk (except a one-time read-only copy of cached bars by `hunt seed-cache`).

## Your loop
1. Write ONE spec per idea family (YAML, below). `./hunt validate <spec>` prints the variant count.
2. `./hunt enqueue <spec>` copies it into `queue/pending/`. Don't run hand-made one-off hunts any more.
3. The nightly job runs `./hunt drain --cap 2400`: oldest specs first, at most 2400 variants per night (raised from 200 on 2026-10-23, Aayan-approved, so the hourly search truly runs hourly) (false-discovery budget). Specs over budget wait for the next night. Bad specs go to `queue/failed/` with a `.log`.
4. Next morning read `runs/<run_id>/report.md` (and `results.json`), write a short post-mortem, propose at most 5 new families.
5. A variant with `pass: true` may take exactly ONE `./hunt vault-test <run_id> --variant "<name>"`. A vault fail is final. Vault survivors go to paper incubation (Phase 3) and then to Aayan for a written OK. Nothing reaches the desk otherwise.

## Spec fields
- `id` (unique), `author`, `hypothesis` (write it before seeing results).
- `base.idea`: one of supertrend(atr_n, mult), sma_cross(fast, slow), donchian(entry_n, exit_n), rsi_revert(n, entry, exit), random_entry(p_switch, seed). `base.params`: lists = grid.
- `filters`: at most 4; each `{name, params}`, names: trend_sma(n), relvol(n, min_ratio), vol_regime(n, max_atr_pct), rsi_band(n, lo, hi), session(start, end). Filter params are grids too and multiply the variant count.
- `universe`: map of basket -> symbols. Each basket is an equal-weight set of per-symbol sleeves; variants = baskets x grid. Max 200 variants per spec, min 2.
- `timeframe`: 1Day | 1Hour | 15Min (`flat_eod: true` for intraday). `direction`: long_flat only (shorts blocked).
- `costs`: fee_bps, slippage_bps per side. `stop.atr_mult` optional ATR stop. `min_trades` >= 100. `split.is_frac` (0.7), `split.wf_folds` (2). `n_random` (1000).
- Every variant counts in ledger N **before** it runs. Identical specs are refused (no re-rolls); changing anything is a new pre-registration.

## The bar (all required; `failed checks` column tells you which missed)
OOS return > 0 and > buy-and-hold of the same basket; trades >= min_trades; round-trip cost <= 3% of stop distance (stop = atr_mult x ATR14, or 1 x ATR14 if no stop); every walk-forward OOS fold > 0; random-entry twin p (same exposure and switch count) Holm-adjusted across the WHOLE ledger < 0.05; DSR > 0.95 at ledger N; Hansen SPA vs buy-and-hold < 0.05; family PBO (CSCV, 16 blocks) < 0.5.
Data: Alpaca IEX bars, parquet cache `data_cache/<tf>/<SYM>.parquet` (misses fetched from Alpaca). Hunt runs only see bars before `vault/seal.json:vault_start`.
Tip: daily SPY/QQQ with 5 bps/side fails the 3% cost/stop rule unless the stop is wide (>= ~3.5 ATR); more volatile names pass it more easily.

## Files
`hunt` CLI | `hunt_engine/` code | `specs/examples/` | `queue/{pending,done,failed}` + `budget.json` | `runs/<run_id>/{spec.yaml,prereg.json,results.json,report.md}` | `ledger/{ledger.jsonl,state.json}` (mirrored into ../ledger/README.txt) | `vault/{seal.json,log.jsonl}` | `tests/`.
Credits: vectorbt, arch (SPA), CSCV/PBO after Bailey et al. 2014 and esvhd/pypbo, DSR after Bailey & Lopez de Prado 2014.
