"""Publisher end to end: ledger survivor -> standalone survivor_alpha.py (run in a clean subprocess) + QuantStats tearsheet + MLflow + manifest."""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import textwrap

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from swarm.auditor import AuditConfig, Auditor  # noqa: E402,F401
from swarm.ast_json import node_hash, node_to_json  # noqa: E402
from swarm.data import synthetic_panel  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402
from swarm.trader import Trader  # noqa: E402
from swarm.worker import Worker  # noqa: E402
from src.dsl.grammar import parse_expr  # noqa: E402
from vault.publisher import compile_survivor_source, publish_pool  # noqa: E402


def _make_survivor(d):
    led = SharedLedger(os.path.join(d, "t.db"))
    led.set_baseline({"engine_n": 1498, "sde_n": 0, "note": "t"})
    panel = synthetic_panel(700, 60, seed=0, drift_signal=0.004)
    led.set_meta("calendar", panel.calendar())
    n = parse_expr("Log($volume)")
    led.record_proposal("Log($volume)", "t", "m", "PENDING", ast_hash=node_hash(n), canonical=n.canonical(), ast_json=node_to_json(n), task_json={
        "ast": node_to_json(n), "ast_hash": node_hash(n), "expression": n.canonical()})
    assert Worker(led, panel, "w").run_once() == 1
    row = led.get_trial(1)
    gate = {"pass": True}
    led.set_audit(1, "APPROVED", {"overall_status": "APPROVED", "n_trials_at_audit": led.n_trials(), "scope": "test",
                                  "gates": {"cpcv": dict(gate, median_path_sharpe=2.0), "pbo": dict(gate, pbo=0.0), "dsr": dict(gate, p_value=0.01), "spa": dict(gate, p_candidate=0.01)}})
    tr = Trader.from_panel(led, panel)
    assert tr.run_once()[0]["decision"] == "INTEGRATED"
    return led, panel


def test_publish_end_to_end_and_standalone_script_runs_and_matches_engine():
    with tempfile.TemporaryDirectory() as d:
        led, panel = _make_survivor(d)
        out = os.path.join(d, "survivors")
        made = publish_pool(led, out_root=out, mlflow_uri=f"sqlite:///{d}/mlflow.db")
        assert len(made) == 1
        h = made[0]["ast_hash"]
        sd = os.path.join(out, h)
        assert sorted(os.listdir(sd)) == ["manifest.json", "returns.csv", "survivor_alpha.py", "tearsheet.html"]
        man = json.load(open(os.path.join(sd, "manifest.json")))
        assert man["mlflow_run_id"] and man["expression"] == "Log($volume)" and man["n_trials_at_audit"] == led.n_trials()
        assert man["calendar"].startswith("real")
        for fn, sha in man["sha256"].items():
            assert hashlib.sha256(open(os.path.join(sd, fn), "rb").read()).hexdigest() == sha
        html = open(os.path.join(sd, "tearsheet.html")).read()
        assert "<html" in html.lower() and len(html) > 50_000
        # idempotent
        assert publish_pool(led, out_root=out, mlflow_uri=f"sqlite:///{d}/mlflow.db") == []
        # the script is STANDALONE: no repo imports, runs in a clean interpreter from another directory with an empty PYTHONPATH
        src = open(os.path.join(sd, "survivor_alpha.py")).read()
        assert "import src" not in src and "from src" not in src and "swarm" not in src.replace("swarm survivor", "")
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        r = subprocess.run([sys.executable, os.path.join(sd, "survivor_alpha.py")], cwd=d, env=env, capture_output=True, text=True, timeout=120)
        assert r.returncode == 0, r.stderr
        assert json.loads(r.stdout.strip().splitlines()[-1])["ok"] is True
        # numerical agreement with the swarm's own backtest: same panel -> same net return vector
        np.savez(os.path.join(d, "panel.npz"), **{k[1:]: v for k, v in panel.data.items()})
        code = textwrap.dedent(f"""
            import importlib.util, numpy as np, pandas as pd
            spec = importlib.util.spec_from_file_location("sa", {os.path.join(sd, 'survivor_alpha.py')!r}); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            z = np.load({os.path.join(d, 'panel.npz')!r})
            idx = pd.RangeIndex(z["close"].shape[0]); cols = list(range(z["close"].shape[1]))
            P = {{"$" + k: pd.DataFrame(z[k], index=idx, columns=cols) for k in ("close", "high", "low", "volume")}}
            net = m.backtest(m.target_weights(m.compute_signal(P)), P["$close"])
            np.save({os.path.join(d, 'net.npy')!r}, net.to_numpy())
        """)
        r = subprocess.run([sys.executable, "-c", code], cwd=d, env=env, capture_output=True, text=True, timeout=120)
        assert r.returncode == 0, r.stderr
        net = np.load(os.path.join(d, "net.npy"))[panel.start_idx:]
        ref = led.get_returns(1)["net"]
        assert len(net) == len(ref) and np.allclose(net, ref, atol=1e-9)


def test_compile_source_is_valid_python_and_embeds_provenance():
    with tempfile.TemporaryDirectory() as d:
        led, _ = _make_survivor(d)
        src = compile_survivor_source(led.get_trial(1))
        compile(src, "x", "exec")
        for s in ("EXPRESSION = 'Log($volume)'", "RESEARCH candidate", "NOT tradable on the desk", "N_trials at audit"):
            assert s in src
