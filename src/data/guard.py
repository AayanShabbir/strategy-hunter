"""Runtime guard for the sealed 2021+ holdout (data/sealed_sde/). Two layers, both tested in tests_sde/test_sealed_guard.py:
  1. static: a source scan fails CI if any search/swarm/SDE module names the sealed directory or imports src.vault;
  2. runtime: `install_audit_guard()` registers a Python audit hook that raises PermissionError on open/listdir/scandir/rename of any path
     under the sealed directory unless the call happens inside `vault_access()`, which only src.vault uses.
This is a tripwire against accidents and against careless code, NOT a security boundary: code running as the same OS user can still
read the files. The real protection is procedural (single-use vault, hash-chained log, pre-registered candidates, manifest hash).
Search entry points should call `install_audit_guard()` once (the guard test proves the hook works; wiring it into existing entry points
is left out on purpose so running jobs and existing run results are not touched)."""
from __future__ import annotations
import contextlib, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEALED_NAME = "sealed_sde"


def sealed_dir() -> Path:
    return Path(os.environ.get("SDE_SEALED_DIR") or (ROOT / "data" / SEALED_NAME)).resolve()


def is_sealed_path(p) -> bool:
    try: q = Path(os.fsdecode(p)).resolve()
    except Exception: return False
    s = sealed_dir()
    return q == s or s in q.parents


def forbid_sealed(p, what: str = "read") -> None:
    if is_sealed_path(p) and not _STATE["depth"]:
        raise PermissionError(f"refusing to {what} {p}: the 2021+ holdout is sealed (use src.vault)")


_STATE = {"depth": 0, "installed": False}


@contextlib.contextmanager
def vault_access():
    """Only src.vault may enter this (guard test forbids the name elsewhere)."""
    _STATE["depth"] += 1
    try: yield
    finally: _STATE["depth"] -= 1


def _hook(event: str, args: tuple) -> None:
    if _STATE["depth"] or event not in ("open", "os.listdir", "os.scandir", "os.rename", "os.remove", "os.chmod", "os.truncate"): return
    p = args[0] if args else None
    if p is None or isinstance(p, int): return
    if is_sealed_path(p): raise PermissionError(f"sealed holdout: {event} {p!s} refused outside the vault")


def install_audit_guard() -> None:
    if not _STATE["installed"]:
        sys.addaudithook(_hook); _STATE["installed"] = True
