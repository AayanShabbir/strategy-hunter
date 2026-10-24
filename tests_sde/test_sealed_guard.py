"""Sealed-holdout guard: static scan (search/swarm/SDE code cannot name or import the vault or the sealed dir), runtime audit hook,
gitignore, and that the committed pre-registration manifest is structurally sound. Nothing here reads or evaluates sealed data."""
import json, os, re, subprocess, sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = ("sealed_sde", "src.vault", "from src import vault", "vault_access", "load_finsaber_full", "load_sealed_panel")
# the only files allowed to name them: the vault package itself, the guard, the one sealed-only loader, and tests/docs
ALLOWED = {"src/data/guard.py", "src/data/external.py"}


def py_files():
    for base in ("src", "engine/hunt_engine", "engine/swarm", "engine/dsl", "engine/hunt", "engine/specs", "crypto", "nautilus"):
        for p in (ROOT / base).rglob("*.py"):
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith("src/vault/") or rel in ALLOWED or "__pycache__" in rel: continue
            yield rel, p


def test_no_search_swarm_or_sde_module_names_the_sealed_dir_or_imports_the_vault():
    bad = []
    for rel, p in py_files():
        t = p.read_text(errors="ignore")
        for tok in FORBIDDEN:
            if tok in t: bad.append((rel, tok))
    assert not bad, bad


def test_only_the_vault_package_may_call_the_sealed_loaders():
    names = ("allow_sealed", "SealedStore")
    for rel, p in py_files(): assert not any(n in p.read_text(errors="ignore") for n in names), rel


def test_engine_scripts_without_py_suffix_also_clean():
    for f in (ROOT / "engine").glob("hunt*"):
        if f.is_file() and f.suffix == "": assert "sealed_sde" not in f.read_text(errors="ignore")


def test_sealed_dir_is_gitignored():
    r = subprocess.run(["git", "check-ignore", "-q", "data/sealed_sde/panel.npz"], cwd=ROOT)
    assert r.returncode == 0
    gi = (ROOT / ".gitignore").read_text(); assert "/data/sealed_sde/" in gi


def test_runtime_hook_blocks_open_listdir_scandir_and_vault_access_allows(tmp_path):
    sealed = tmp_path / "sealed_sde"; sealed.mkdir(); (sealed / "panel.npz").write_bytes(b"x")
    code = r'''
import os, sys
sys.path.insert(0, %r)
from src.data import guard
guard.install_audit_guard()
import src.data.loader, src.data.multisource, src.portfolio.long_short, src.portfolio.deployability      # search-side imports work
def blocked(fn):
    try: fn()
    except PermissionError: return True
    return False
f = os.path.join(%r, "panel.npz")
assert blocked(lambda: open(f, "rb")), "open"
assert blocked(lambda: os.listdir(%r)), "listdir"
assert blocked(lambda: list(os.scandir(%r))), "scandir"
import pathlib
assert blocked(lambda: pathlib.Path(f).read_bytes()), "pathlib"
try:
    import numpy as np; np.load(f)
except PermissionError: pass
except Exception: pass
else: raise SystemExit("np.load was not blocked")
with guard.vault_access():
    assert open(f, "rb").read() == b"x"
assert blocked(lambda: open(f, "rb")), "closed again"
open(os.path.join(%r, "..", "other.txt"), "w").write("fine")                     # outside the sealed dir stays allowed
print("OK")
''' % (str(ROOT), str(sealed), str(sealed), str(sealed), str(sealed))
    r = subprocess.run([sys.executable, "-c", code], env={**os.environ, "SDE_SEALED_DIR": str(sealed), "PYTHONPATH": str(ROOT)}, capture_output=True, text=True)
    assert r.returncode == 0 and "OK" in r.stdout, r.stderr[-800:]


def test_new_loader_cache_refuses_the_sealed_dir(tmp_path, monkeypatch):
    from src.data import alpaca_bars as AB
    sealed = tmp_path / "sealed_sde"; monkeypatch.setenv("SDE_SEALED_DIR", str(sealed))
    with pytest.raises(PermissionError): AB.fetch_cached(["AAA"], "2016-01-01", "2016-02-01", sealed / "cache")


def test_search_side_finsaber_loader_is_capped_at_2020():
    from src.data import external as E
    with pytest.raises(ValueError): E.load_finsaber(Path("/nonexistent"), end="2021-01-01")


def test_committed_manifest_is_a_preregistration_not_data():
    m = ROOT / "src/vault/sealed_manifest.json"
    if not m.exists(): pytest.skip("sealed set not built on this checkout")
    d = json.loads(m.read_text())
    assert d["window"]["eval_start"] == "2021-01-01" and len(d["content_sha256"]) == 64 and d["files"]["panel.npz"]
    assert d["n_assets"] == len(d["assets"])
    assert all(isinstance(v, (str, int, float, dict, list)) for v in d.values())
    assert not any(isinstance(x, list) and x and isinstance(x[0], (int, float)) for x in d.values())   # no numeric series, only hashes/counts
    assert set(d["files"]) <= {"panel.npz", "membership_fja05680.csv", "provenance.json", "finsaber_ge2021.csv"}
