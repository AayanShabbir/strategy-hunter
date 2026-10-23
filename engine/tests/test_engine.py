import os, json, multiprocessing as mp, numpy as np, pandas as pd, pytest, yaml
from conftest import synth_loader
SPEC = dict(id="t_spec", hypothesis="test", base=dict(idea="sma_cross", params=dict(fast=[10, 20], slow=[50, 100])),
            filters=[], universe=dict(A=["AAA", "BBB"]), timeframe="1Day", costs=dict(fee_bps=0, slippage_bps=5), min_trades=100, n_random=200)
def write(p, **over):
    s = {**SPEC, **over}; f = p / f"{s['id']}.yaml"; f.write_text(yaml.safe_dump(s)); return str(f)
# ---------- spec validation
def test_spec_limits(tmp_path):
    from hunt_engine import spec as S
    with pytest.raises(S.SpecError): S.validate({**SPEC, "filters": [dict(name="trend_sma")] * 5})
    with pytest.raises(S.SpecError): S.validate({**SPEC, "min_trades": 50})
    with pytest.raises(S.SpecError): S.validate({**SPEC, "direction": "long_short"})
    with pytest.raises(S.SpecError): S.validate({**SPEC, "base": dict(idea="supertrend", params=dict(atr_n=10, mult=3))})  # 1 variant
    assert len(S.variants(SPEC)) == 4
# ---------- ledger lock / N accounting
def _reserve(i):
    from hunt_engine import ledger
    rows, _ = ledger.reserve(f"r{i}", "x", f"hash{i}", [f"v{j}" for j in range(5)]); return sorted(rows.values())
def test_parallel_reservations_do_not_double_count(sandbox):
    from hunt_engine import ledger
    with mp.get_context("fork").Pool(8) as pool: got = pool.map(_reserve, range(16))
    allrows = [r for g in got for r in g]
    assert ledger.current_N() == 392 + 80 and len(set(allrows)) == 80 and min(allrows) == 393 and max(allrows) == 472
def test_N_reserved_before_results_and_kept_on_crash(sandbox, tmp_path):
    from hunt_engine import runner, ledger
    def boom(*a, **k): raise RuntimeError("data down")
    with pytest.raises(RuntimeError): runner.run(write(tmp_path), loader=boom, quiet=True)
    assert ledger.current_N() == 396                     # 4 variants stay counted
    with pytest.raises(RuntimeError, match="already pre-registered"): runner.run(write(tmp_path), loader=synth_loader, quiet=True)
    res, rd = runner.run(write(tmp_path), loader=synth_loader, quiet=True, allow_rerun=True)
    assert res["N"] == 400 and ledger.current_N() == 400
    assert {"results.json", "report.md", "prereg.json", "spec.yaml"} <= set(os.listdir(rd))
    assert len(ledger.records("result")) == 4 and "N_cumulative: 400" in open(os.environ["HUNT_HUMAN_LEDGER"]).read()
# ---------- gauntlet
def test_random_walk_family_fails_gauntlet(sandbox, tmp_path):
    from hunt_engine import runner
    res, _ = runner.run(write(tmp_path, id="rw"), loader=synth_loader, quiet=True)
    assert res["n_pass"] == 0 and all(v["holm"] >= 0.05 for v in res["variants"].values())
def test_holm_ledger_wide():
    from hunt_engine.gauntlet import holm_adjusted
    p = {i: 1.0 for i in range(1, 393)}; p[393] = 1e-5; p[394] = 0.01
    a = holm_adjusted(p, [393, 394]); assert abs(a[393] - 394e-5) < 1e-9 and a[394] == 1.0
def test_verdict_requires_every_check():
    from hunt_engine.gauntlet import verdict
    good = dict(OOS=dict(ret=50), BH_OOS=dict(ret=10), trades=300, cost_stop=0.01, WF=[5, 5], holm=0.001, DSR=0.99, SPA=0.01)
    assert verdict(good, 100, 0.2)[0]
    for k, bad in [("trades", 99), ("cost_stop", 0.04), ("WF", [5, -1]), ("holm", 0.06), ("DSR", 0.9), ("SPA", 0.2)]:
        assert not verdict({**good, k: bad}, 100, 0.2)[0], k
    assert not verdict(good, 100, 0.6)[0] and not verdict({**good, "OOS": dict(ret=5)}, 100, 0.2)[0]
def test_pbo_detects_noise():
    from hunt_engine.gauntlet import pbo_cscv
    M = np.random.default_rng(0).normal(0, 0.01, (1000, 20)); assert 0.25 < pbo_cscv(M) < 0.85
# ---------- vault
def test_vault_sealed_from_hunt_runs(sandbox):
    from hunt_engine import vault
    D = synth_loader(["AAA"], "1Day"); assert D["close"].index.max() < vault.vault_start_ts()
    Dv = synth_loader(["AAA"], "1Day", allow_vault=True); assert Dv["close"].index.max() >= vault.vault_start_ts()
def test_vault_once_per_survivor(sandbox, tmp_path):
    from hunt_engine import runner, vault_test as VT
    res, rd = runner.run(write(tmp_path, id="vt"), loader=synth_loader, quiet=True); name = next(iter(res["variants"]))
    with pytest.raises(SystemExit, match="only gauntlet survivors"): VT.vault_test(res["run_id"], name, loader=synth_loader)
    r = json.load(open(os.path.join(rd, "results.json"))); r["variants"][name]["pass"] = True   # simulate a survivor
    json.dump(r, open(os.path.join(rd, "results.json"), "w"))
    out = VT.vault_test(res["run_id"], name, loader=synth_loader, n_random=100); assert "pass" in out
    with pytest.raises(SystemExit, match="one look only"): VT.vault_test(res["run_id"], name, loader=synth_loader)
# ---------- queue budget
def test_drain_respects_nightly_budget(sandbox, tmp_path, monkeypatch):
    from hunt_engine import queue, runner
    real = runner.run; monkeypatch.setattr(runner, "run", lambda sp, **k: real(sp, loader=synth_loader, quiet=True))
    for i in range(3): write(sandbox / "queue" / "pending", id=f"q{i}")
    done = queue.drain(cap=8)
    assert len(done) == 2 and len(os.listdir(sandbox / "queue" / "pending")) == 1 and queue.used_tonight()[0] == 8
def test_status_and_drain_see_same_pending(sandbox, tmp_path, capsys):
    """Regression (Scout 2026-10-23): status must list exactly what drain will run, for .yaml/.yml/symlinks, never .log."""
    from hunt_engine import queue, cli
    pend = sandbox / "queue" / "pending"; src = tmp_path / "src"; src.mkdir()
    a = write(src, id="qa"); b = write(src, id="qb")
    cli.main(["enqueue", a]); os.symlink(b, pend / "qb.yml"); (pend / "x.yaml.log").write_text("note")
    cli.main(["status"]); st = json.loads(capsys.readouterr().out.split("\n", 1)[1])
    names = [p["file"] for p in st["pending"]]
    assert names == ["qa.yaml", "qb.yml"] and all(p["variants"] == 4 for p in st["pending"])
    done = queue.drain(cap=200, dry=True)
    assert [d["spec"] for d in done] == names and queue.used_tonight()[0] == 0 and len(os.listdir(pend)) == 3
