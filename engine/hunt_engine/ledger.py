"""Machine ledger (append-only ledger.jsonl + state.json) mirrored into the human ledger README.txt.
All mutations hold one FileLock so parallel runs cannot double-count N. N is reserved BEFORE any backtest."""
import os, json
from .util import paths, atomic_json, atomic_write, now_et, ledger_lock
def _state_f(): return os.path.join(paths()["ledger"], "state.json")
def _jsonl(): return os.path.join(paths()["ledger"], "ledger.jsonl")
def _append(rec):
    with open(_jsonl(), "a") as f:
        f.write(json.dumps(rec, default=str) + "\n"); f.flush(); os.fsync(f.fileno())
def state():
    f = _state_f(); return json.load(open(f)) if os.path.exists(f) else None
def current_N(): return state()["N"]
def migrate(N, source):
    with ledger_lock():
        if state(): return state()
        _append(dict(type="migration", N=N, source=source, ts=now_et().isoformat(),
                     note="rows 1..N from hand-run hunts; their p-values treated as 1.0 for Holm (conservative for us)"))
        st = dict(N=N, migrated_N=N, updated=now_et().isoformat()); atomic_json(_state_f(), st); return st
def records(t=None):
    if not os.path.exists(_jsonl()): return []
    return [r for r in (json.loads(l) for l in open(_jsonl()) if l.strip()) if t is None or r["type"] == t]
def spec_hash_used(h): return any(r["spec_hash"] == h for r in records("prereg"))
def reserve(run_id, spec_id, spec_hash, variant_names, allow_rerun=False):
    with ledger_lock():
        st = state()
        if st is None: raise RuntimeError("ledger not migrated; run `hunt init`")
        if spec_hash_used(spec_hash) and not allow_rerun: raise RuntimeError("identical spec already pre-registered (no re-rolls); use --allow-rerun to pay N again")
        k = len(variant_names); first = st["N"] + 1
        rows = {v: first + i for i, v in enumerate(variant_names)}
        _append(dict(type="prereg", run_id=run_id, spec_id=spec_id, spec_hash=spec_hash, rows=[first, first + k - 1],
                     variants=rows, ts=now_et().isoformat()))
        st["N"] += k; st["updated"] = now_et().isoformat(); atomic_json(_state_f(), st)
        _human_append(f"\n## Engine prereg {run_id} ({spec_id}, sha256 {spec_hash[:12]}): rows #{first}-{first+k-1} RESERVED ({k} variants). Counted in N.\nN_cumulative: {st['N']}\n")
        return rows, st["N"]
def all_pvalues():
    """Ledger-wide p-values for Holm: 1.0 for migrated rows and reserved-but-unscored rows."""
    st = state(); p = {i: 1.0 for i in range(1, st["N"] + 1)}
    for r in records("result"):
        if r.get("p") is not None: p[r["row"]] = float(r["p"])
    return p
def write_results(run_id, rows_out, md_block):
    with ledger_lock():
        for r in rows_out: _append(dict(type="result", run_id=run_id, ts=now_et().isoformat(), **r))
        _human_append(md_block)
def _human_append(text):
    f = paths()["human_ledger"]
    old = open(f).read() if os.path.exists(f) else ""
    atomic_write(f, old + text)
