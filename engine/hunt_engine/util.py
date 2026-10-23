import os, json, tempfile, hashlib, datetime as dt
from zoneinfo import ZoneInfo
from filelock import FileLock
from . import ROOT
ET = ZoneInfo("America/New_York")
def paths():
    r = os.environ.get("HUNT_ROOT", ROOT)   # tests point this at a tmp dir
    return dict(root=r, ledger=os.path.join(r, "ledger"), vault=os.path.join(r, "vault"),
                runs=os.path.join(r, "runs"), queue=os.path.join(r, "queue"),
                cache=os.environ.get("HUNT_CACHE", os.path.join(ROOT, "data_cache")),
                human_ledger=os.environ.get("HUNT_HUMAN_LEDGER", os.path.join(os.path.dirname(ROOT), "ledger", "README.txt")))
def now_et(): return dt.datetime.now(ET)
def atomic_write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp_")
    with os.fdopen(fd, "w") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
def atomic_json(path, obj): atomic_write(path, json.dumps(obj, indent=1, default=str))
def ledger_lock(): 
    p = paths()["ledger"]; os.makedirs(p, exist_ok=True); return FileLock(os.path.join(p, ".ledger.lock"), timeout=600)
def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
