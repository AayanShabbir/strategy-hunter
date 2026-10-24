"""Cross-process trial logging: N_trials must be exact and every task claimed exactly once, with real processes."""
import multiprocessing as mp
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from swarm.shared_ledger import SharedLedger, compute_baseline  # noqa: E402


def _proposer(db, k, tag):
    led = SharedLedger(db)
    for i in range(k):
        led.record_proposal(f"Add($close, $high)#{tag}{i}", "test", f"p{tag}", "REJECTED_NOVELTY", ast_hash=f"h{tag}_{i}", reject_reason="ted")
    led.close()


def _claimer(db, name, out_q):
    led = SharedLedger(db)
    got = []
    while True:
        t = led.claim_task(name)
        if t is None:
            break
        r = np.zeros(10)
        led.complete_task(t["trial_id"], name, metrics={"w": name}, net=r, gross=r, turnover=r, sharpe_daily=0.01, sign=1)
        got.append(t["trial_id"])
    out_q.put((name, got))


def test_concurrent_counting_is_exact(tmp_path):
    db = str(tmp_path / "trials.db")
    led = SharedLedger(db)
    led.set_baseline({"engine_n": 1000, "sde_n": 500})
    ctx = mp.get_context("spawn")
    procs = [ctx.Process(target=_proposer, args=(db, 60, t)) for t in range(6)]
    [p.start() for p in procs]
    [p.join(120) for p in procs]
    assert all(p.exitcode == 0 for p in procs)
    assert led.n_swarm_trials() == 360
    assert led.n_trials() == 1860                    # baseline offset + swarm rows
    ids = [r[0] for r in led.conn.execute("SELECT id FROM trials ORDER BY id")]
    assert ids == list(range(1, 361))                # no lost or duplicated rows


def test_each_task_claimed_exactly_once(tmp_path):
    db = str(tmp_path / "trials.db")
    led = SharedLedger(db)
    for i in range(80):
        led.record_proposal(f"e{i}", "test", "m", "PENDING", ast_hash=f"h{i}", task_json={"expression": f"e{i}"})
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    procs = [ctx.Process(target=_claimer, args=(db, f"w{i}", q)) for i in range(4)]
    [p.start() for p in procs]
    res = [q.get(timeout=120) for _ in procs]
    [p.join(60) for p in procs]
    all_ids = sorted(i for _, got in res for i in got)
    assert all_ids == list(range(1, 81))             # every task done once, none twice
    assert led.counts()["by_status"] == {"EVALUATED": 80}
    assert led.get_returns(5)["net"].shape == (10,)


def test_lease_expiry_requeues_and_release(tmp_path):
    led = SharedLedger(str(tmp_path / "t.db"))
    tid = led.record_proposal("x", "test", "m", "PENDING", ast_hash="h", task_json={"expression": "x"})
    t = led.claim_task("w1", lease_s=-1)             # lease already expired
    assert t["trial_id"] == tid and led.claim_task("w2")["trial_id"] == tid     # re-queued, claimed by another worker
    led.release_task(tid, "w2")
    assert led.get_trial(tid)["status"] == "PENDING"
    try:
        led.complete_task(tid, "w9", metrics={}, net=np.zeros(3), gross=np.zeros(3), turnover=np.zeros(3), sharpe_daily=0.0, sign=1)
        raise AssertionError("complete by a non-owner must fail")
    except RuntimeError:
        pass


def test_baseline_is_read_only_and_first_writer_wins(tmp_path):
    state = tmp_path / "state.json"; state.write_text('{"N": 1498}')
    sde = tmp_path / "l.jsonl"; sde.write_text('{"kind":"trial","n":1}\n{"kind":"eval","n":2}\n{"kind":"trial","n":3}\n')
    b = compute_baseline(str(state), str(sde))
    assert (b["engine_n"], b["sde_n"]) == (1498, 2)
    assert state.read_text() == '{"N": 1498}' and sde.read_text().count("\n") == 3
    led = SharedLedger(str(tmp_path / "t.db"))
    led.set_baseline(b); led.set_baseline({"engine_n": 1, "sde_n": 1})            # second call must not overwrite
    assert led.baseline_n() == 1500
