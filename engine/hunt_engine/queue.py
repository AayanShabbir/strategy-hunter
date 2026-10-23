"""queue/pending/*.yaml -> `hunt drain` runs them oldest-first under a nightly false-discovery budget
(variants per ET night, default 200). Over-budget specs wait for the next night. One drain at a time."""
import os, json, shutil, glob, traceback
from filelock import FileLock, Timeout
from . import spec as specmod, runner
from .util import paths, atomic_json, now_et
def _night(): t = now_et(); return (t if t.hour >= 12 else t - __import__("datetime").timedelta(days=1)).date().isoformat()
def _budget_f(): return os.path.join(paths()["queue"], "budget.json")
def used_tonight():
    f = _budget_f(); b = json.load(open(f)) if os.path.exists(f) else {}; return b.get(_night(), 0), b
def pending_specs():
    """Single source of truth for status and drain: *.yaml/*.yml in queue/pending, oldest first (symlinks followed)."""
    d = os.path.join(paths()["queue"], "pending")
    return sorted((f for f in glob.glob(os.path.join(d, "*.y*ml")) if os.path.isfile(f)), key=os.path.getmtime)
def drain(cap=200, max_specs=None, dry=False):
    q = paths()["queue"]; [os.makedirs(os.path.join(q, d), exist_ok=True) for d in ("pending", "done", "failed")]
    try: lk = FileLock(os.path.join(q, ".drain.lock"), timeout=0); lk.acquire()
    except Timeout: print("another drain is running; exiting"); return []
    done = []
    try:
        for sp in pending_specs():
            if max_specs and len(done) >= max_specs: break
            used, b = used_tonight()
            try: s, _ = specmod.load(sp); k = len(specmod.variants(s))
            except Exception as e:
                _move(sp, "failed", f"invalid spec: {e}"); continue
            if used + k > cap: print(f"budget: {used}/{cap} used tonight; {os.path.basename(sp)} needs {k}; deferred"); continue
            if dry:
                print(f"DRY would run {os.path.basename(sp)} ({k} variants)"); b[_night()] = used + k; done.append(dict(spec=os.path.basename(sp), variants=k)); continue
            b[_night()] = used + k; atomic_json(_budget_f(), b)          # charge budget before running
            try:
                res, rd = runner.run(sp); _move(sp, "done", f"run {res['run_id']}: {res['n_pass']}/{k} pass")
                done.append(dict(spec=os.path.basename(sp), run=res["run_id"], n_pass=res["n_pass"], variants=k))
            except Exception as e:
                _move(sp, "failed", traceback.format_exc())
        if dry: print(f"DRY: {len(done)} specs, {sum(x['variants'] for x in done)} variants would run; nothing executed, budget unchanged"); return done
        used, _ = used_tonight(); print(f"drain finished: {len(done)} specs run; budget {used}/{cap} tonight ({_night()})")
        return done
    finally: lk.release()
def _move(sp, where, note):
    dst = os.path.join(paths()["queue"], where, f"{now_et():%Y%m%d_%H%M%S}_" + os.path.basename(sp))
    shutil.move(sp, dst); open(dst + ".log", "w").write(note + "\n"); print(f"{os.path.basename(sp)} -> {where}: {note.splitlines()[0] if note else ''}")
