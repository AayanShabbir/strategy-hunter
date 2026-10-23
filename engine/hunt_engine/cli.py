import argparse, json, os, re, sys, shutil
from . import ledger, vault, data, runner, queue, spec as specmod
from .util import paths
def _readme_N():
    t = open(paths()["human_ledger"]).read(); return max(int(x) for x in re.findall(r"N_cumulative:\s*\**(\d+)", t))
def _nv(f):
    try: return len(specmod.variants(specmod.load(f)[0]))
    except Exception as e: return f"INVALID: {e}"
def main(argv=None):
    ap = argparse.ArgumentParser(prog="hunt", description="Strategy Hunter engine (research/paper only; places no orders)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="migrate ledger N from ledger/README.txt and seal the 12-month vault")
    sub.add_parser("seed-cache", help="copy existing research bars into the parquet cache (read-only source)")
    r = sub.add_parser("run"); r.add_argument("spec"); r.add_argument("--allow-rerun", action="store_true")
    v = sub.add_parser("validate"); v.add_argument("spec")
    q = sub.add_parser("enqueue"); q.add_argument("spec")
    d = sub.add_parser("drain"); d.add_argument("--cap", type=int, default=200); d.add_argument("--max-specs", type=int); d.add_argument("--dry", action="store_true", help="list what would run; runs nothing")
    t = sub.add_parser("vault-test"); t.add_argument("run_id"); t.add_argument("--variant", required=True)
    sub.add_parser("status")
    a = ap.parse_args(argv)
    if a.cmd == "init":
        st = ledger.migrate(_readme_N(), paths()["human_ledger"]); print("ledger:", st); print("vault:", vault.seal())
    elif a.cmd == "seed-cache": print("cached files:", data.seed_cache())
    elif a.cmd == "validate":
        s, _ = specmod.load(a.spec); print(f"OK: {len(specmod.variants(s))} variants")
    elif a.cmd == "enqueue":
        s, _ = specmod.load(a.spec); dst = os.path.join(paths()["queue"], "pending", os.path.basename(a.spec))
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copyfile(a.spec, dst); os.utime(dst); print("queued", dst, f"({len(specmod.variants(s))} variants)")
    elif a.cmd == "run": runner.run(a.spec, allow_rerun=a.allow_rerun)
    elif a.cmd == "drain": queue.drain(a.cap, a.max_specs, dry=a.dry)
    elif a.cmd == "vault-test":
        from .vault_test import vault_test; vault_test(a.run_id, a.variant)
    elif a.cmd == "status":
        used, _ = queue.used_tonight()
        print(json.dumps(dict(ledger=ledger.state(), vault=vault.seal(), queue_dir=paths()["queue"], hunt_root_override=os.environ.get("HUNT_ROOT"),
                              pending=[dict(file=os.path.basename(f), variants=_nv(f)) for f in queue.pending_specs()],
                              budget_used_tonight=used), indent=1))
if __name__ == "__main__": main()
