"""CLI smoke test: `hunt swarm-start` runs a small bounded swarm to completion and leaves no orphan processes."""
import json
import os
import subprocess
import sys
import tempfile
import time

ENGINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUNT = os.path.join(ENGINE, "hunt")


def _run(args, env_extra, timeout=300):
    env = dict(os.environ, **env_extra)
    return subprocess.run([HUNT] + args, capture_output=True, text=True, timeout=timeout, env=env)


def _alive(pids):
    out = []
    for p in pids:
        try:
            os.kill(p, 0)
            out.append(p)
        except OSError:
            pass
    return out


def test_swarm_start_bounded_run_completes_cleanly():
    with tempfile.TemporaryDirectory() as d:
        env = {"SWARM_DATA_DIR": os.path.join(d, "swarm"), "SWARM_LLM_MAILBOX": os.path.join(d, "mb")}
        db = os.path.join(d, "trials.db")
        r = _run(["swarm-start", "--workers", "2", "--max-trials", "24", "--synthetic", "--db", db, "--no-mlflow", "--no-tearsheet", "--json"], env)
        assert r.returncode == 0, r.stderr[-2000:]
        rep = json.loads(r.stdout.strip().splitlines()[-1])
        assert rep["stop_reason"] == "completed" and rep["new_tasks_issued"] == 24
        assert rep["ledger_counts"]["by_status"].get("EVALUATED", 0) + rep["ledger_counts"]["by_status"].get("ERROR", 0) == 24
        assert sum(rep["audit"].values()) >= 20 and rep["survivors_in_pool"] == 0          # honest null result on synthetic noise
        assert rep["workers"]["still_alive"] == [] and rep["workers"]["force_terminated"] == 0
        assert rep["n_trials_end"] - rep["n_trials_start"] == rep["ledger_counts"]["swarm_trials"]
        st = _run(["swarm-status", "--db", db], env)
        assert st.returncode == 0 and json.loads(st.stdout)["swarm_trials"] == rep["ledger_counts"]["swarm_trials"]
        out = subprocess.run(["pgrep", "-f", "swarm-worker"], capture_output=True, text=True).stdout.split()
        assert not [p for p in out if p.isdigit() and os.path.exists(f"/proc/{p}") and db in open(f"/proc/{p}/cmdline").read()]


def test_continuous_mode_stops_on_sigterm_without_orphans():
    import signal
    with tempfile.TemporaryDirectory() as d:
        env = dict(os.environ, SWARM_DATA_DIR=os.path.join(d, "swarm"), SWARM_LLM_MAILBOX=os.path.join(d, "mb"))
        db = os.path.join(d, "trials.db")
        p = subprocess.Popen([HUNT, "swarm-start", "--workers", "2", "--continuous", "--synthetic", "--db", db, "--no-mlflow", "--no-tearsheet", "--json"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
        time.sleep(12)
        kids = subprocess.run(["pgrep", "-P", str(p.pid)], capture_output=True, text=True).stdout.split()
        # spawn-ed workers are grandchildren via the resource tracker, so look them up by command line instead
        workers = [int(x) for x in subprocess.run(["pgrep", "-f", "multiprocessing.spawn"], capture_output=True, text=True).stdout.split()
                   if int(x) != os.getpid() and _is_descendant(int(x), p.pid)]
        assert workers, "no worker processes found while the swarm was running"
        p.send_signal(signal.SIGTERM)
        out, err = p.communicate(timeout=90)
        assert p.returncode == 0, err[-2000:]
        rep = json.loads(out.strip().splitlines()[-1])
        assert rep["stop_reason"] == "signal" and rep["workers"]["still_alive"] == []
        time.sleep(1)
        assert _alive(workers) == []
        assert rep["ledger_counts"]["swarm_trials"] > 0


def _is_descendant(pid, ancestor):
    while pid > 1:
        try:
            stat = open(f"/proc/{pid}/stat").read().rsplit(")", 1)[1].split()
        except OSError:
            return False
        pid = int(stat[1])
        if pid == ancestor:
            return True
    return False


def test_llm_check_and_status_commands():
    r = _run(["swarm-llm-check", "Div(TsStd($close, 20d), $volume)", "Nope($close)"], {})
    assert r.returncode == 1 and r.stdout.splitlines()[0].startswith("VALID ") and r.stdout.splitlines()[1].startswith("INVALID ")


def test_llm_ping_with_fake_responder(capsys):
    import threading
    sys.path.insert(0, ENGINE)
    sys.path.insert(0, os.path.dirname(ENGINE))
    from swarm.cli import llm_ping
    with tempfile.TemporaryDirectory() as d:
        for sub in ("requests", "responses", "done"):
            os.makedirs(os.path.join(d, sub))

        def responder():
            for _ in range(200):
                for fn in os.listdir(os.path.join(d, "requests")):
                    if fn.endswith(".json") and not fn.startswith("."):
                        rid = fn[:-5]
                        body = {"protocol": 1, "id": rid, "responder": "fake", "status": "ok",
                                "proposals": [{"expression": "Sub(Log($high), Log($low))", "hypothesis": "range"}, {"expression": "Bad(", "hypothesis": ""}]}
                        json.dump(body, open(os.path.join(d, "responses", rid + ".tmp"), "w"))
                        os.replace(os.path.join(d, "responses", rid + ".tmp"), os.path.join(d, "responses", fn))
                        return
                time.sleep(0.05)

        th = threading.Thread(target=responder, daemon=True)
        th.start()
        rc = llm_ping("mailbox", 20, d, poll_interval=0.1)
        th.join(5)
        out = capsys.readouterr().out
        assert rc == 0 and "OK    Sub(Log($high), Log($low))" in out and "BAD" in out and "ping complete: 2 proposals" in out


def test_llm_ping_times_out_cleanly():
    sys.path.insert(0, ENGINE)
    sys.path.insert(0, os.path.dirname(ENGINE))
    from swarm.cli import llm_ping
    with tempfile.TemporaryDirectory() as d:
        assert llm_ping("mailbox", 0.3, d, poll_interval=0.1) == 2


def test_signing_works_across_worker_processes_and_audits_are_judged_on_merit_and_mirrored():
    """Regression: workers once ran unsigned in the cluster (key dir not passed), so every audit failed on the 'signature' gate."""
    with tempfile.TemporaryDirectory() as d:
        env = {"SWARM_DATA_DIR": os.path.join(d, "swarm"), "SWARM_LLM_MAILBOX": os.path.join(d, "mb")}
        db, sde = os.path.join(d, "trials.db"), os.path.join(d, "sde_ledger.jsonl")
        r = _run(["swarm-start", "--workers", "2", "--max-trials", "20", "--synthetic", "--db", db, "--no-mlflow", "--no-tearsheet", "--json",
                  "--mirror", "--sde-ledger", sde, "--sde-pool", ""], env)
        assert r.returncode == 0, r.stderr[-2000:]
        rep = json.loads(r.stdout.strip().splitlines()[-1])
        assert sorted(os.listdir(os.path.join(d, "swarm", "keys"))) == ["auditor.key", "miner.key", "worker.key"]
        import sqlite3
        c = sqlite3.connect(db)
        gates = [json.loads(a).get("failed_gates") or [] for (a,) in c.execute("SELECT audit_json FROM trials WHERE audit_status IS NOT NULL")]
        assert len(gates) >= 15 and not any("signature" in g for g in gates)
        assert rep["global_count"]["in_sync"] and rep["global_count"]["swarm_mirrored_in_sde"] == rep["ledger_counts"]["swarm_trials"]
        lines = [json.loads(x) for x in open(sde)]
        assert sum(1 for x in lines if x["kind"] == "swarm_audit") == len(gates)
