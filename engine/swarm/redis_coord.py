"""Optional Redis coordination layer (blueprint: Redis as the shared state / queue / lock / counter).

SQLite stays authoritative for every fact (trial rows, leases, N, verdicts). Redis only accelerates and coordinates:
  * task queue  : list of PENDING trial ids; workers LPOP an id as a *hint* and SQLite `claim_task(hint_id)` still decides atomically,
                  so a lost/duplicated Redis entry can never cause a double evaluation (the queue is rebuilt from SQLite by `resync`).
  * audit lock  : Redlock-style single-node lock (SET NX PX + compare-and-delete release) so two auditors never audit one cohort.
  * heartbeats  : SETEX per node, `live_nodes()` for the dashboard / stall detection.
  * N counter   : mirror of the SQLite N, incremented as trials are recorded and reconciled with SQLite (drift reported, SQLite wins).
Every call degrades to a no-op (and flips `.ok` False) if Redis is unreachable: the swarm keeps running on SQLite alone.
`start_server()` launches a private `redis-server` (apt package) or, when the binary is absent, a pure-python fakeredis TCP server,
so the option works on any box that can `pip install`.
"""
from __future__ import annotations

import contextlib
import os
import shutil
import socket
import subprocess
import tempfile
import threading
import time
import uuid
from typing import Optional


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class EmbeddedRedis:
    """A private loopback Redis: real `redis-server` if installed, else fakeredis' TCP server (same wire protocol)."""

    def __init__(self, prefer: str = "auto", port: Optional[int] = None):
        self.port = port or _free_port()
        self.url = f"redis://127.0.0.1:{self.port}/0"
        self.kind = ""
        self._proc = self._srv = self._thr = self._tmp = None
        exe = shutil.which("redis-server")
        if prefer in ("auto", "redis-server") and exe:
            self._tmp = tempfile.mkdtemp(prefix="swarm_redis_")
            self._proc = subprocess.Popen([exe, "--port", str(self.port), "--bind", "127.0.0.1", "--save", "", "--appendonly", "no",
                                           "--dir", self._tmp, "--daemonize", "no"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.kind = "redis-server"
        elif prefer == "redis-server":
            raise RuntimeError("redis-server binary not found")
        else:
            from fakeredis import TcpFakeServer
            self._srv = TcpFakeServer(("127.0.0.1", self.port), server_type="redis")
            self._thr = threading.Thread(target=self._srv.serve_forever, daemon=True)
            self._thr.start()
            self.kind = "fakeredis"
        self._wait()

    def _wait(self, timeout: float = 10.0) -> None:
        import redis
        t0 = time.time()
        while time.time() - t0 < timeout:
            try:
                if redis.Redis.from_url(self.url, socket_connect_timeout=0.5).ping():
                    return
            except Exception:
                time.sleep(0.1)
        raise RuntimeError(f"embedded redis ({self.kind}) did not start")

    def stop(self) -> None:
        if self._proc is not None:
            self._proc.terminate()
            try:
                self._proc.wait(5)
            except Exception:
                self._proc.kill()
            shutil.rmtree(self._tmp or "", ignore_errors=True)
        if self._srv is not None:
            self._srv.shutdown()
            self._srv.server_close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.stop()


class Coordinator:
    def __init__(self, url: str, prefix: str = "swarm", node: Optional[str] = None):
        import redis
        self.prefix, self.node = prefix, node or f"{os.uname().nodename}:{os.getpid()}"
        self.r = redis.Redis.from_url(url, decode_responses=True, socket_connect_timeout=2, socket_timeout=5)
        self.ok = True
        self._guard(self.r.ping)

    def _k(self, name: str) -> str:
        return f"{self.prefix}:{name}"

    def _guard(self, fn, *a, default=None, **kw):
        try:
            r = fn(*a, **kw)
            self.ok = True
            return r
        except Exception:                                   # connection refused / timeout / server gone: degrade, never crash the swarm
            self.ok = False
            return default

    # ---- task queue (hints)
    def push_task(self, trial_id: int) -> None:
        self._guard(self.r.rpush, self._k("queue"), int(trial_id))

    def pop_task(self) -> Optional[int]:
        v = self._guard(self.r.lpop, self._k("queue"))
        return int(v) if v is not None else None

    def queue_len(self) -> int:
        return int(self._guard(self.r.llen, self._k("queue"), default=0) or 0)

    def resync(self, pending_ids: list[int]) -> None:
        """Rebuild the hint queue from SQLite truth (after a Redis restart, a crashed worker's expired lease, or drift)."""
        def _do():
            p = self.r.pipeline()
            p.delete(self._k("queue"))
            if pending_ids:
                p.rpush(self._k("queue"), *[int(i) for i in pending_ids])
            p.execute()
        self._guard(_do)

    # ---- distributed lock (single-node Redlock: SET NX PX + token-checked delete)
    @contextlib.contextmanager
    def lock(self, name: str, ttl_ms: int = 60_000, wait_s: float = 0.0):
        key, token = self._k(f"lock:{name}"), uuid.uuid4().hex
        got, t0 = False, time.time()
        if not self.ok and self._guard(self.r.ping) is None:
            yield True                                      # Redis down: SQLite's BEGIN IMMEDIATE still serialises writers
            return
        while True:
            got = bool(self._guard(self.r.set, key, token, nx=True, px=ttl_ms, default=False))
            if got or time.time() - t0 >= wait_s:
                break
            time.sleep(0.05)
        try:
            yield got
        finally:
            if got:
                def _release():
                    with self.r.pipeline() as p:
                        p.watch(key)
                        if p.get(key) == token:
                            p.multi()
                            p.delete(key)
                            p.execute()
                self._guard(_release)

    # ---- heartbeats
    def heartbeat(self, role: str, info: str = "", ttl_s: int = 15) -> None:
        self._guard(self.r.setex, self._k(f"hb:{role}:{self.node}"), ttl_s, f"{time.time():.0f}|{info}")

    def live_nodes(self) -> dict:
        def _do():
            out = {}
            for k in self.r.scan_iter(self._k("hb:*")):
                out[k[len(self.prefix) + 4:]] = self.r.get(k)
            return out
        return self._guard(_do, default={}) or {}

    # ---- N counter mirror
    def incr_n(self, by: int = 1) -> None:
        self._guard(self.r.incrby, self._k("n_trials"), by)

    def n_counter(self) -> Optional[int]:
        v = self._guard(self.r.get, self._k("n_trials"))
        return int(v) if v is not None else None

    def reconcile_n(self, sqlite_n: int) -> int:
        """Compare with the SQLite count (authoritative); returns drift = redis - sqlite BEFORE correction, then sets redis := sqlite."""
        cur = self.n_counter()
        self._guard(self.r.set, self._k("n_trials"), int(sqlite_n))
        return 0 if cur is None else cur - int(sqlite_n)
