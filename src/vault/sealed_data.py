"""Builds, pins and (vault-only) loads the sealed 2021+ S&P 500 panel.

Layout (all under the git-ignored data/sealed_sde/; nothing in it is ever committed):
  panel.npz                  dates, assets, $close/$high/$low/$volume (D x N), member (D x N bool), eval_start_idx
  membership_fja05680.csv    the PIT membership file used (fresh download, hashed)
  provenance.json            per-ticker source/QC (no prices)
  finsaber_ge2021.csv        the 2021+ rows of the FINSABER file (the search-side copy is cut at 2020-12-31)
  cache/                     raw yfinance / Alpaca fetches
What IS committed: src/vault/sealed_manifest.json, the SHA-256 pre-registration of exactly what the set contains (window, tickers, per-file
hashes, a content hash of the arrays, coverage, source counts). Rows before 2021-01-01 (from 2020-07-01) are warm-up for rolling windows;
they are search-window data and are never scored (`eval_start_idx` marks the first sealed row).
Building only fetches, counts and hashes. It computes no returns, factors or statistics from the sealed data."""
from __future__ import annotations
import hashlib, json, os, stat, time
from pathlib import Path
import numpy as np
from src.data import guard

ROOT = guard.ROOT
MANIFEST = ROOT / "src" / "vault" / "sealed_manifest.json"
EVAL_START = "2021-01-01"
WARMUP_START = "2020-07-01"
MEMBERSHIP_URL = "https://raw.githubusercontent.com/fja05680/sp500/master/sp500_ticker_start_end.csv"
PANEL, MEMB, PROV, FIN = "panel.npz", "membership_fja05680.csv", "provenance.json", "finsaber_ge2021.csv"


def sha256_file(p) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""): h.update(b)
    return h.hexdigest()


def content_hash(dates, assets, data: dict, member) -> str:
    """Hash of the numeric content independent of container bytes (zip timestamps)."""
    h = hashlib.sha256()
    h.update(("|".join(str(d) for d in dates) + "#" + "|".join(assets)).encode())
    for k in ("$close", "$high", "$low", "$volume"): h.update(np.ascontiguousarray(data[k], dtype="<f8").tobytes())
    h.update(np.ascontiguousarray(member, dtype=np.uint8).tobytes())
    return h.hexdigest()


def _file_hashes(d: Path) -> dict:
    return {n: sha256_file(d / n) for n in (PANEL, MEMB, PROV, FIN) if (d / n).exists()}


def verify_manifest(sealed_dir=None, manifest_path=MANIFEST):
    """(ok, message): the files on disk match the committed pre-registration (file hashes + content hash)."""
    d = Path(sealed_dir) if sealed_dir else guard.sealed_dir()
    m = json.loads(Path(manifest_path).read_text())
    with guard.vault_access():
        if not (d / PANEL).exists(): return False, f"sealed panel missing under {d}"
        have = _file_hashes(d)
        for n, h in m["files"].items():
            if have.get(n) != h: return False, f"{n} does not match the manifest"
        z = np.load(d / PANEL, allow_pickle=False)
        data = {k: z[k] for k in ("$close", "$high", "$low", "$volume")}
        ch = content_hash([str(x) for x in z["dates"]], [str(x) for x in z["assets"]], data, z["member"])
    return (ch == m["content_sha256"], "ok" if ch == m["content_sha256"] else "array content hash mismatch")


def load_sealed_panel(sealed_dir=None):
    """Vault-only: returns a Panel-like object (dates, assets, data, member, meta, eval_start_idx). Verifies nothing; the vault does."""
    from src.data.loader import Panel
    d = Path(sealed_dir) if sealed_dir else guard.sealed_dir()
    with guard.vault_access():
        z = np.load(d / PANEL, allow_pickle=False)
        p = Panel(z["dates"].astype("datetime64[D]"), [str(a) for a in z["assets"]], {k: z[k] for k in ("$close", "$high", "$low", "$volume")},
                  z["member"].astype(bool), json.loads(str(z["meta"])))
        p.eval_start_idx = int(z["eval_start_idx"])
    return p


def _last_weekday(today=None):
    import pandas as pd
    t = pd.Timestamp(today or time.strftime("%Y-%m-%d"))
    t -= pd.Timedelta(days=1)
    while t.weekday() >= 5: t -= pd.Timedelta(days=1)
    return t.strftime("%Y-%m-%d")


def build(end: str | None = None, sealed_dir=None, manifest_path=MANIFEST, write_manifest: bool = True) -> dict:
    """Fetch + merge + store. Returns the manifest dict. Refuses to overwrite an existing sealed panel."""
    import pandas as pd, urllib.request
    from src.data import multisource as M, external as E, sp500_pit as P
    from src.data.alpaca_bars import fetch_cached
    d = Path(sealed_dir) if sealed_dir else guard.sealed_dir()
    end = end or _last_weekday()
    with guard.vault_access():
        if (d / PANEL).exists(): raise FileExistsError(f"{d / PANEL} exists: the sealed set is built once (delete it deliberately, and re-register, to rebuild)")
        d.mkdir(parents=True, exist_ok=True); (d / "cache").mkdir(exist_ok=True)
        req = urllib.request.Request(MEMBERSHIP_URL, headers={"User-Agent": "Mozilla/5.0"})
        (d / MEMB).write_bytes(urllib.request.urlopen(req, timeout=60).read())
        win = pd.read_csv(d / MEMB, parse_dates=["start_date", "end_date"]); win["yt"] = win["ticker"].map(P._y)
        pit = win[(win.start_date <= end) & (win.end_date.isna() | (win.end_date >= EVAL_START))]
        names = sorted(set(pit.yt)); alts = sorted({v for k, v in M.ALT_TICKERS.items() if k in names})
        yf = M._yf_frames(sorted(set(names) | set(alts)), WARMUP_START, end)
        al = fetch_cached(names, WARMUP_START, end, d / "cache", tag="sealed_alpaca")
        fs = E.load_finsaber_full(P.CACHE, start=WARMUP_START, end="2024-12-31")
        frames, prov, dates = M.merge_sources(win, yf, al, EVAL_START, end, WARMUP_START, end, fs=fs)
        cov = M.coverage_numbers(win, frames, prov, EVAL_START, end, dates)
        pan = M.panel_from_merge(frames, prov, win, EVAL_START, end, {"coverage": cov})
        ds = pd.DatetimeIndex(pan.dates); e0 = int(np.searchsorted(ds.values, np.datetime64(EVAL_START)))
        meta = {"universe": "sp500_merged_sealed_2021plus", "window": [EVAL_START, end], "warmup_from": WARMUP_START, "coverage": cov,
                "membership": "PIT windows fja05680/sp500 (MIT) downloaded " + time.strftime("%Y-%m-%d")}
        np.savez_compressed(d / PANEL, dates=np.array([str(x)[:10] for x in ds]), assets=np.array(pan.assets), member=pan.member, eval_start_idx=e0,
                            meta=json.dumps(meta), **{k: v for k, v in pan.data.items()})
        (d / PROV).write_text(json.dumps({"coverage": cov, "tickers": prov}, sort_keys=True))
        fin = E.finsaber_path(P.CACHE)
        import pandas as _pd
        _pd.read_csv(fin, parse_dates=["date"]).query("date >= @EVAL_START").to_csv(d / FIN, index=False)
        ch = content_hash([str(x)[:10] for x in ds], pan.assets, pan.data, pan.member)
        files = _file_hashes(d)
        for n in files: os.chmod(d / n, stat.S_IRUSR | stat.S_IRGRP)
        by_src = {}
        for r in prov.values():
            if r["status"] == "kept": by_src[r["source"]] = by_src.get(r["source"], 0) + 1
        man = {"schema": 1, "purpose": "pre-registration of the sealed holdout contents; the data itself is never committed",
               "window": {"eval_start": EVAL_START, "last_date": str(ds[-1])[:10], "warmup_from": WARMUP_START, "requested_end": end},
               "n_dates": int(len(ds)), "n_eval_dates": int(len(ds) - e0), "n_assets": len(pan.assets),
               "assets_sha256": hashlib.sha256("|".join(pan.assets).encode()).hexdigest(), "assets": list(pan.assets),
               "content_sha256": ch, "files": files, "membership_file": "fja05680/sp500 sp500_ticker_start_end.csv (MIT), sha256 in files",
               "coverage": cov, "kept_by_source": by_src, "built_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "builder_sha256": {f: sha256_file(ROOT / f) for f in ("src/vault/sealed_data.py", "src/data/multisource.py", "src/data/alpaca_bars.py", "src/data/external.py")},
               "adjustment_note": "adjusted closes on the fetch-date basis; sources rescaled to the primary on their overlap (see provenance.json)"}
    if write_manifest:
        Path(manifest_path).write_text(json.dumps(man, indent=1, sort_keys=True) + "\n")
    return man


if __name__ == "__main__":
    m = build(); print(json.dumps({k: m[k] for k in ("window", "n_dates", "n_eval_dates", "n_assets", "coverage", "kept_by_source", "content_sha256")}, indent=1))
