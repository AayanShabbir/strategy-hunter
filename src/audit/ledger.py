"""SDE trial ledger (blueprint: append-only, built first so every trial is counted).

JSON-lines, hash-chained: each entry carries `n` (1-based sequence), `prev` (previous entry hash) and `hash`
= sha256(prev || canonical-json(entry without hash)). Writes are O_APPEND + flock, one line per fsync'd write.
Nothing in this module rewrites or truncates the file. `verify()` detects edits, deletions and reordering.
This feeds the DSR trial count N, PBO/CSCV, and the Ville e-process in Phase 4.
"""
from __future__ import annotations
import fcntl, hashlib, json, os, time
from pathlib import Path

DEFAULT_PATH = Path(__file__).with_name("ledger.jsonl")
GENESIS = "0" * 64


def _digest(prev: str, body: dict) -> str:
    return hashlib.sha256((prev + json.dumps(body, sort_keys=True, separators=(",", ":"))).encode()).hexdigest()


def _clean(o):
    """JSON-safe: NaN/inf -> None, numpy scalars -> python."""
    if isinstance(o, dict): return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_clean(v) for v in o]
    if hasattr(o, "item") and not isinstance(o, (str, bytes)):
        try: o = o.item()
        except Exception: return str(o)
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))): return None
    return o


class Ledger:
    def __init__(self, path=DEFAULT_PATH):
        self.path = Path(path); self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def append(self, record: dict) -> dict:
        """Append one entry atomically; returns the stored entry (with n, prev, hash)."""
        fd = os.open(self.path, os.O_RDWR | os.O_APPEND)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            n, prev = self._tail(fd)
            body = {"n": n + 1, "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "prev": prev, **_clean(record)}
            entry = {**body, "hash": _digest(prev, body)}
            os.write(fd, (json.dumps(entry, sort_keys=True, separators=(",", ":")) + "\n").encode())
            os.fsync(fd)
            return entry
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)

    @staticmethod
    def _tail(fd):
        size = os.lseek(fd, 0, os.SEEK_END)
        if size == 0: return 0, GENESIS
        back = min(size, 65536)
        os.lseek(fd, size - back, os.SEEK_SET)
        data = os.read(fd, back)
        lines = [l for l in data.split(b"\n") if l.strip()]
        last = json.loads(lines[-1])
        return last["n"], last["hash"]

    def entries(self):
        with open(self.path) as f:
            for line in f:
                if line.strip(): yield json.loads(line)

    def count(self, kind: str | None = "trial") -> int:
        """Number of trials counted (every sampled formula, duplicates included)."""
        return sum(1 for e in self.entries() if kind is None or e.get("kind") == kind)

    def distinct(self) -> int:
        """Number of distinct formulas (by canonical AST hash) among trials."""
        return len({e.get("ast_hash") for e in self.entries() if e.get("kind") == "trial"})

    def verify(self):
        """Returns (ok, n_entries, message). Checks sequence numbers, prev links and hashes."""
        prev, n = GENESIS, 0
        for e in self.entries():
            n += 1
            h = e.pop("hash", None)
            if e.get("n") != n: return False, n, f"sequence break at entry {n} (n={e.get('n')})"
            if e.get("prev") != prev: return False, n, f"prev-link break at entry {n}"
            if _digest(prev, e) != h: return False, n, f"hash mismatch at entry {n}"
            prev = h
        return True, n, "ok"
