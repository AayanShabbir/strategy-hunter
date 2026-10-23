"""Stub: `hunt retest <run_id> --variant <id>` — realistic Nautilus re-test of an engine survivor.
Backtest-only. Loads the run's variant spec, rebuilds bars from engine/data_cache (pre-vault unless
--vault is explicitly given for the final one-shot check), and runs it in BacktestEngine with fees/slippage.
Currently: resolves the run/variant and reports what would run; strategy translation is TODO."""
import argparse, json, pathlib, sys
LAB = pathlib.Path(__file__).resolve().parents[1]
def main(argv=None):
    ap = argparse.ArgumentParser(prog="hunt retest")
    ap.add_argument("run_id"); ap.add_argument("--variant", required=True)
    a = ap.parse_args(argv)
    run = LAB / "engine/runs" / a.run_id
    if not run.exists():
        sys.exit(f"run not found: {run}")
    hits = [p for p in run.rglob("*.json") if a.variant in p.read_text(errors="ignore")]
    print(json.dumps({"run": str(run), "variant": a.variant, "matching_files": [str(h) for h in hits[:5]],
                      "status": "STUB - translation to Nautilus Strategy not implemented yet"}, indent=2))
if __name__ == "__main__":
    main()
