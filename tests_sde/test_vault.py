"""Single-use vault: synthetic sealed data in tmp dirs only. Never touches data/sealed_sde or the real vault log."""
import json, os
from pathlib import Path
import numpy as np
import pytest
from src.vault import sealed_data as SD
from src.vault import vault as V

EXPR = "TsStd(Log($close), 5d)"; EXPR2 = "Div($high, $volume)"


def make_sealed(tmp, D=60, N=30, seed=0):
    rng = np.random.default_rng(seed); d = Path(tmp) / "sealed"; d.mkdir()
    dates = np.arange(np.datetime64("2020-12-01"), np.datetime64("2020-12-01") + D).astype("datetime64[D]")
    close = 50 * np.cumprod(1 + 0.01 * rng.standard_normal((D, N)), 0)
    data = {"$close": close, "$high": close * 1.01, "$low": close * 0.99, "$volume": rng.uniform(1e5, 1e6, (D, N))}
    member = np.ones((D, N), bool); assets = [f"T{i}" for i in range(N)]
    np.savez(d / SD.PANEL, dates=dates, assets=np.array(assets), member=member, eval_start_idx=31, meta=json.dumps({}), **data)
    for n in (SD.MEMB, SD.PROV, SD.FIN): (d / n).write_text("x")
    man = {"window": {"eval_start": SD.EVAL_START}, "files": SD._file_hashes(d), "content_sha256": SD.content_hash([str(x) for x in dates], assets, data, member)}
    mp = Path(tmp) / "manifest.json"; mp.write_text(json.dumps(man))
    return d, mp


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setenv("SDE_SEALED_DIR", str(tmp_path / "sealed"))
    d, mp = make_sealed(tmp_path)
    cfg = tmp_path / "cfg.json"; cfg.write_text(json.dumps({"max_looks": 3}))
    def mk(auditor=lambda hs: (True, "ok")): return V.Vault(tmp_path / "log.jsonl", cfg, d, mp, auditor_check=auditor)
    return mk, cfg, d, mp, tmp_path


F = lambda e=EXPR, s=1: {"kind": "formula", "expr": e, "sign": s}
GOOD = lambda p, s: {"ok": True, "PASS": False}


def test_default_cap_is_three_in_committed_config():
    assert json.loads(V.CONFIG_PATH.read_text())["max_looks"] == 3


def test_must_be_preregistered(env):
    mk, *_ = env; v = mk()
    with pytest.raises(V.VaultRefused, match="not pre-registered"): v.open(F(), GOOD)
    assert v.looks_used() == 0 and any(e["kind"] == "refused" for e in v.entries())


def test_swarm_auditor_approval_required(env):
    mk, *_ = env; v = mk(lambda hs: (False, "not APPROVED by the swarm auditor"))
    v.preregister(F())
    with pytest.raises(V.VaultRefused, match="APPROVED"): v.open(F(), GOOD)
    assert v.looks_used() == 0


def test_swarm_approved_reads_trials_db_readonly(tmp_path):
    import sqlite3
    db = tmp_path / "t.db"; c = sqlite3.connect(db); c.execute("create table trials(ast_hash text, audit_status text)")
    h = V.ast_hashes(F())[0]; c.execute("insert into trials values (?,?)", (h, "REJECTED")); c.commit()
    assert not V.swarm_approved([h], db)[0]
    c.execute("insert into trials values (?,?)", (h, "APPROVED")); c.commit(); c.close()
    assert V.swarm_approved([h], db)[0]
    assert not V.swarm_approved([h], tmp_path / "missing.db")[0]


def test_one_look_per_candidate_and_result_logged(env):
    mk, *_ = env; v = mk(); v.preregister(F())
    r = v.open(F(), GOOD); assert r["ok"]
    with pytest.raises(V.VaultRefused, match="already opened"): v.open(F(), GOOD)
    assert v.looks_used() == 1 and [e["kind"] for e in v.entries()].count("result") == 1


def test_spec_hash_is_canonical(env):
    assert V.spec_hash(F("TsStd(Log($close),5d)")) == V.spec_hash(F(" TsStd( Log( $close ) , 5d ) ")) and V.spec_hash(F(s=1)) != V.spec_hash(F(s=-1))
    p1 = {"kind": "pool", "members": [F(EXPR), F(EXPR2, -1)]}; p2 = {"kind": "pool", "members": [F(EXPR2, -1), F(EXPR)]}
    assert V.spec_hash(p1) == V.spec_hash(p2)


def test_global_cap_three_then_refuse_fourth(env):
    mk, *_ = env; v = mk(); exprs = [f"TsStd(Log($close), {k}d)" for k in ("5", "10", "20", "60")]
    for e in exprs: v.preregister(F(e))
    for e in exprs[:3]: v.open(F(e), GOOD)
    with pytest.raises(V.VaultRefused, match="global cap"): v.open(F(exprs[3]), GOOD)
    assert v.looks_used() == 3


def test_cap_edit_is_logged_and_takes_effect(env):
    mk, cfg, *_ = env; v = mk(); v.preregister(F()); assert v.cap() == 3
    cfg.write_text(json.dumps({"max_looks": 1})); assert v.cap() == 1
    cs = [e for e in v.entries() if e["kind"] == "config"]
    assert [c["max_looks"] for c in cs] == [3, 1] and cs[1]["previous_max_looks"] == 3 and cs[0]["config_sha"] != cs[1]["config_sha"]
    assert v.verify_log()[0]


def test_tampering_with_the_log_blocks_opening(env):
    mk, _, _, _, tmp = env; v = mk(); v.preregister(F()); v.cap()
    p = tmp / "log.jsonl"; lines = p.read_text().splitlines(); e = json.loads(lines[0]); e["note"] = "edited"; lines[0] = json.dumps(e)
    p.write_text("\n".join(lines) + "\n")
    assert not v.verify_log()[0]
    with pytest.raises(V.VaultRefused, match="verification"): v.open(F(), GOOD)


def test_evaluator_crash_still_consumes_the_look(env):
    mk, *_ = env; v = mk(); v.preregister(F())
    def boom(panel, spec): raise RuntimeError("crash")
    with pytest.raises(RuntimeError): v.open(F(), boom)
    assert v.looks_used() == 1 and v.entries()[-1]["kind"] == "error"
    with pytest.raises(V.VaultRefused, match="already opened"): v.open(F(), GOOD)


def test_manifest_mismatch_refuses_and_burns_no_look(env):
    mk, _, d, mp, _ = env; v = mk(); v.preregister(F())
    os.chmod(d / SD.PANEL, 0o644); (d / SD.PANEL).write_bytes((d / SD.PANEL).read_bytes() + b"0")
    with pytest.raises(V.VaultRefused, match="manifest"): v.open(F(), GOOD)
    assert v.looks_used() == 0


def test_preregistration_pins_the_manifest(env):
    mk, _, _, mp, _ = env; v = mk(); v.preregister(F())
    m = json.loads(mp.read_text()); m["n"] = 1; mp.write_text(json.dumps(m))
    with pytest.raises(V.VaultRefused, match="different sealed manifest"): v.open(F(), GOOD)


def test_default_evaluator_runs_on_synthetic_panel_and_logs_result(env):
    mk, *_ = env; v = mk(); p = {"kind": "pool", "members": [F(EXPR), F(EXPR2, -1)]}; v.preregister(p)
    r = v.open(p)
    assert r["rule_id"] == V.RULE_ID and isinstance(r["PASS"], bool) and "long_only_topq" in r and r["params"]["n_scored_days"] > 0
    assert v.entries()[-1]["kind"] == "result" and v.verify_log()[0]


def test_preregister_is_idempotent_and_status(env):
    mk, *_ = env; v = mk(); a = v.preregister(F()); b = v.preregister(F())
    assert a["hash"] == b["hash"] and v.status()["preregistered"] == 1 and v.status()["log_ok"]


def test_vault_module_has_no_trading_or_broker_calls():
    t = Path(V.__file__).read_text() + Path(SD.__file__).read_text()
    for bad in ("alpaca.markets/v2/orders", "submit_order", "paper-api", "TradingClient"): assert bad not in t
