"""Re-score an existing S&P 500 run's FIXED pool on the survivorship-reduced point-in-time universe (src/data/sp500_pit.py).

An addition, clearly labelled: the pool is NOT re-trained and the blueprint run is not replaced. Writes
runs_sde/<run>/phase3_pit.json. Does not write to the ledger (write_ledger=False) so it cannot disturb a live job;
DSR still uses the ledger's current N. Usage: python -m src.train.phase3_pit --run-id sp500_s0_20261023
"""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
import src.train.phase3_eval as P
from src.data.sp500_pit import load_sp500_pit, coverage_report


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run-id", required=True); ap.add_argument("--cost-bps", type=float, default=5.0)
    a = ap.parse_args(); t0 = time.time()
    pan = load_sp500_pit(); cov = coverage_report(pan)
    P.load_panel = lambda uni, upto="test": pan          # same evaluation code, different panel
    res = P.evaluate_run_p3(a.run_id, cost_bps=a.cost_bps, write_ledger=False, out_name="phase3_pit.json")
    p = Path("runs_sde") / a.run_id / "phase3_pit.json"; r = json.loads(p.read_text())
    r["universe_variant"] = {"name": "sp500_pit (survivorship-REDUCED, not eliminated)", **cov}; p.write_text(json.dumps(r, indent=1))
    print(f"[{a.run_id}] PIT re-score written to {p} in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
