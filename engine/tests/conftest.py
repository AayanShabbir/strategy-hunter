import os, sys, numpy as np, pandas as pd, pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    hl = tmp_path / "README.txt"; hl.write_text("N_cumulative: 392\n")
    monkeypatch.setenv("HUNT_ROOT", str(tmp_path)); monkeypatch.setenv("HUNT_HUMAN_LEDGER", str(hl))
    for d in ("queue/pending", "queue/done", "queue/failed", "runs"): (tmp_path / d).mkdir(parents=True)
    from hunt_engine import ledger, vault
    ledger.migrate(392, str(hl)); vault.seal(); return tmp_path
def synth_loader(symbols, tf, allow_vault=False, refresh=False, seed=3):
    from hunt_engine import vault
    idx = pd.bdate_range("2016-01-04", "2026-10-22"); rng = np.random.default_rng(seed); D = {}
    c = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0.0003, 0.012, (len(idx), len(symbols))), 0)), index=idx, columns=symbols)
    D["close"] = c; D["open"] = c.shift(1).fillna(c.iloc[0]) * (1 + rng.normal(0, 0.002, c.shape))
    D["high"] = np.maximum(D["open"], c) * 1.01; D["low"] = np.minimum(D["open"], c) * 0.99
    D["volume"] = pd.DataFrame(rng.integers(1e5, 1e6, c.shape), index=idx, columns=symbols).astype(float)
    if not allow_vault:
        cut = vault.vault_start_ts(tf); D = {k: v[v.index < cut] for k, v in D.items()}
    return D
