"""Sealed holdout vault: the most recent 12 months (from the seal date) are invisible to hunt runs.
Only `hunt vault-test <run_id> --variant <name>` reads them, once per candidate, logged under the ledger lock."""
import os, json, pandas as pd
from .util import paths, atomic_json, now_et, ledger_lock
def seal_file(): return os.path.join(paths()["vault"], "seal.json")
def seal(months=12):
    f = seal_file()
    if os.path.exists(f): return json.load(open(f))
    start = (pd.Timestamp(now_et().date()) - pd.DateOffset(months=months)).date().isoformat()
    s = dict(vault_start=start, sealed_at=now_et().isoformat(), months=months,
             rule="hunt runs see bars strictly before vault_start; vault-test only, once per candidate")
    atomic_json(f, s); return s
def vault_start_ts(tf="1Day"):
    s = seal(); t = pd.Timestamp(s["vault_start"])
    return t if tf == "1Day" else t.tz_localize("America/New_York")
def log_file(): return os.path.join(paths()["vault"], "log.jsonl")
def already_tested(cand):
    f = log_file()
    return os.path.exists(f) and any(json.loads(l)["candidate"] == cand for l in open(f) if l.strip())
def record(cand, result):
    with ledger_lock():
        if already_tested(cand): raise RuntimeError(f"vault already used for {cand}; a vault fail is final")
        with open(log_file(), "a") as f:
            f.write(json.dumps(dict(candidate=cand, ts=now_et().isoformat(), **result), default=str) + "\n"); f.flush(); os.fsync(f.fileno())
