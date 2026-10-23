"""Optuna (TPE) search inside a spec's grid with honest trial accounting.
EVERY trial is reserved as a ledger row BEFORE it runs (N grows by n_trials), the objective uses the in-sample
segment only (OOS and the sealed vault are never seen), and the top-k parameter sets are written as a NEW spec for
the normal queue, where they are pre-registered again and face the full unchanged pass bar (double counting N is
deliberately conservative). Objectives: 'sharpe' (IS Sharpe) or 'calmar' (IS return / |maxDD|, drawdown-aware).
Credit: Optuna (Akiba et al. 2019, MIT)."""
import os, json, copy, numpy as np, pandas as pd, yaml
from . import spec as specmod, ledger, data, gauntlet as G
from .backtest import run_variant, to_daily
from .util import paths, now_et, sha256_bytes, atomic_json
def optimize(spec_path, n_trials=50, objective="sharpe", top_k=4, loader=None, seed=0, out_dir=None):
    import optuna
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    s, raw = specmod.load(spec_path); grid = s["base"].get("params") or {}
    space = {k: (v if isinstance(v, list) else [v]) for k, v in grid.items()}
    run_id = f"{now_et():%Y%m%d_%H%M%S}_opt_{s['id']}"
    names = [f"trial_{i:04d}" for i in range(n_trials)]
    rows, N = ledger.reserve(run_id, s["id"] + "::optuna", sha256_bytes(raw + f"|opt{n_trials}|{objective}|{seed}".encode()), names)
    syms = sorted({x for b in s["universe"].values() for x in b}); ann = G.ann_factor(syms, s["timeframe"])
    Dall = (loader or data.load)(syms, s["timeframe"], allow_vault=False); basket = next(iter(s["universe"]))
    D = {c: x[s["universe"][basket]] for c, x in Dall.items()}; is_frac = s.get("split", {}).get("is_frac", 0.7)
    def obj(trial):
        b = {k: trial.suggest_categorical(k, v) for k, v in space.items()}
        bt = run_variant(D, s, dict(name="t", basket=basket, base=b, filters=[(f["name"], f.get("params") or {}) for f in s.get("filters") or []]))
        dr = to_daily(bt["bar_ret"], s["timeframe"]); dr = dr.iloc[: int(len(dr) * is_frac)]   # IN-SAMPLE ONLY
        st = G.stats(dr, ann)
        return st["sharpe"] if objective == "sharpe" else st["ret"] / max(abs(st["maxdd"]), 1e-6)
    study = optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler(seed=seed))
    study.optimize(obj, n_trials=n_trials)
    trials = sorted((t for t in study.trials if t.value is not None), key=lambda t: -t.value)
    best = []
    for t in trials:
        if t.params not in best: best.append(t.params)
        if len(best) >= top_k: break
    ns = copy.deepcopy(s); ns["id"] = s["id"] + f"_opt{seed}"; ns["hypothesis"] = s["hypothesis"] + f" | Optuna {objective} IS-only top{top_k} of {n_trials} trials (ledger rows {min(rows.values())}-{max(rows.values())})"
    ns["base"]["params"] = {k: sorted({b[k] for b in best}) for k in space}
    log = dict(run_id=run_id, rows=[min(rows.values()), max(rows.values())], objective=objective, n_trials=n_trials,
               trials=[dict(n=t.number, params=t.params, value=t.value) for t in study.trials])
    rd = os.path.join(paths()["runs"], run_id); os.makedirs(rd, exist_ok=True); atomic_json(os.path.join(rd, "optuna.json"), log)
    ledger.write_results(run_id, [], f"\n## Optuna search {run_id}: {n_trials} IS-only trials counted (rows #{log['rows'][0]}-{log['rows'][1]}); top-{top_k} -> spec {ns['id']} (must pass full bar).\nN_cumulative: {ledger.current_N()}\n")
    try: specmod.validate(ns)
    except specmod.SpecError as e: return dict(log=log, spec=None, error=str(e))
    f = os.path.join(out_dir or rd, ns["id"] + ".yaml"); open(f, "w").write(yaml.safe_dump(ns, sort_keys=False))
    return dict(log=log, spec=f)
