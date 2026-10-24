"""SDE Phase 2: one-shot out-of-sample read of a finished run's pool (validation + test splits).

    .venv17/bin/python -m src.train.evaluate_pool --run-id csi300_s0_20261023

Per-factor and equal-weight-ensemble IC / ICIR on train, val, test (factor signs fixed from TRAIN IC). The test split is
read once per run: a second call refuses unless --force (and every evaluation is appended to the ledger).
No parameters are fitted here; nothing flows back into the search.
"""
from __future__ import annotations
import argparse, json, warnings
from pathlib import Path
import numpy as np
warnings.filterwarnings("ignore")
from src.audit.ledger import Ledger, DEFAULT_PATH
from src.data.loader import load_panel, SPLITS
from src.rewards.multi_faceted import Cells, MultiFacetedReward, FactorPool

ROOT = Path(__file__).resolve().parents[2]


def evaluate_run(run_id: str, ledger_path=DEFAULT_PATH, force=False):
    out = ROOT / "runs_sde" / run_id
    cfg = json.loads((out / "config.json").read_text()); pool = json.loads((out / "pool.json").read_text())
    uni = cfg["universe"]; ev_path = out / "eval.json"
    if ev_path.exists() and not force: raise SystemExit(f"{ev_path} exists: test split already read for this run (use --force to re-read)")
    panel = load_panel(uni, upto="test"); ledger = Ledger(ledger_path)
    res = {"run_id": run_id, "universe": uni, "pool_size": pool["size"], "splits": {}, "members": []}
    zs = {}
    for split, (s, e) in SPLITS[uni].items():
        cells = Cells(panel, s, e); cells.set_label(panel.label(e)); rw = MultiFacetedReward(panel, cells, FactorPool(cells))
        ics, icirs, ens = [], [], np.zeros(len(cells.flat)); k = 0
        for m in pool["members"]:
            z = rw.signal(m["expr"]); ic, icir, n = cells.ic_stats(z)
            ics.append(m["sign"] * ic); icirs.append(m["sign"] * icir)
            if split == "train": res["members"].append(dict(m))
            res["members"][k]["%s_ic" % split] = m["sign"] * ic; res["members"][k]["%s_icir" % split] = m["sign"] * icir
            ens += m["sign"] * np.nan_to_num(z); k += 1
        if pool["members"]:
            ens_ic, ens_icir, nd = cells.ic_stats(cells.zscore(ens / len(pool["members"])))
        else: ens_ic = ens_icir = float("nan")
        res["splits"][split] = dict(
            n_days=int(cells.D), mean_factor_ic=float(np.mean(ics)) if ics else None, mean_factor_icir=float(np.mean(icirs)) if icirs else None,
            frac_factors_positive_ic=float(np.mean(np.array(ics) > 0)) if ics else None, ensemble_ic=ens_ic, ensemble_icir=ens_icir)
        ledger.append(dict(kind="eval", run_id=run_id, universe=uni, split=split, pool_size=pool["size"], **res["splits"][split]))
    ev_path.write_text(json.dumps(res, indent=1))
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--run-id", required=True); ap.add_argument("--force", action="store_true")
    ap.add_argument("--ledger", default=str(DEFAULT_PATH)); a = ap.parse_args()
    r = evaluate_run(a.run_id, a.ledger, a.force); print(json.dumps(r["splits"], indent=1))
