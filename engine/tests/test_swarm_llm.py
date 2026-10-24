"""LLM idea backends: file-mailbox protocol with a FAKE responder thread, and the OpenAI-compatible backend against a local fake server.
The live Swarm Miner agent is NOT exercised here."""
import http.server
import json
import os
import sys
import tempfile
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from swarm.llm import MailboxLLM, OpenAICompatLLM, build_request, validate_response  # noqa: E402
from swarm.miner import Miner  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402

GOOD = ["Div(TsStd($close, 20d), $volume)", "Sub(Log($high), Log($low))", "Add(TsStd($volume, 5d), Log($close))"]


def _req(n=3):
    return build_request("propose", "momentum", n, avoid_recent=[], n_total_tried=0, blacklisted_subtrees=[])


def _respond(root, rid, proposals, status="ok", atomic=True, resp_id=None):
    body = {"protocol": 1, "id": resp_id or rid, "responder": "fake", "created_utc": "2026-10-24T00:00:00Z", "status": status,
            "proposals": [{"expression": e, "hypothesis": "h"} for e in proposals], "notes": ""}
    p = os.path.join(root, "responses", f"{rid}.json")
    if atomic:
        json.dump(body, open(p + ".tmp", "w")); os.replace(p + ".tmp", p)
    else:
        json.dump(body, open(p, "w"))


def test_mailbox_roundtrip_and_archive():
    with tempfile.TemporaryDirectory() as d:
        mb = MailboxLLM(d)
        req = _req()
        mb.submit(req)
        assert os.path.exists(os.path.join(d, "requests", f"{req['id']}.json")) and mb.n_pending() == 1
        assert mb.poll() == []                                                        # non-blocking: nothing yet
        _respond(d, req["id"], GOOD)
        got = mb.poll()
        assert len(got) == 1 and got[0][0]["id"] == req["id"] and mb.n_pending() == 0
        assert os.path.exists(os.path.join(d, "done", f"request_{req['id']}.json")) and os.path.exists(os.path.join(d, "done", f"response_{req['id']}.json"))
        ok, props, err = validate_response(got[0][1], req)
        assert ok and [p["expression"] for p in props] == GOOD


def test_validate_response_is_strict():
    req = _req()
    base = {"protocol": 1, "id": req["id"], "status": "ok", "proposals": [{"expression": GOOD[0]}]}
    assert validate_response(base, req)[0]
    for bad in (dict(base, id="req_other"), dict(base, protocol=2), dict(base, status="weird"), dict(base, proposals="x"),
                dict(base, proposals=[{"expr": "x"}]), [1, 2], "text"):
        assert not validate_response(bad, req)[0], bad
    assert not validate_response(dict(base, status="error", notes="cannot"), req)[0]


def test_miner_ingests_mailbox_answers_counts_everything_and_survives_garbage():
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        mb = MailboxLLM(os.path.join(d, "mb"))
        mn = Miner(led, seed=0, llm=mb, llm_min_interval_s=0.0, llm_n=3)
        rid = mn.request_llm("propose", "momentum")
        assert rid and mn.request_llm() is None                                       # max one outstanding request
        n0 = led.n_swarm_trials()
        # 3 proposals ok, one more than asked (excess), plus a syntactically bad one and a duplicate of the first
        _respond(os.path.join(d, "mb"), rid, GOOD + ["Foo($close)"])
        tasks = mn.ingest_llm()
        assert len(tasks) == 3
        assert led.n_swarm_trials() - n0 == 4                                        # all 4 proposals counted as trials (1 excess)
        assert led.counts()["by_status"].get("REJECTED_EXCESS") == 1
        # second round: duplicates of accepted formulas are rejected by the novelty memory, still counted
        rid2 = mn.request_llm("propose", "volatility")
        _respond(os.path.join(d, "mb"), rid2, GOOD[:2])
        assert mn.ingest_llm() == []
        # wrong id / malformed JSON never crash the loop
        rid3 = mn.request_llm("propose", "liquidity")
        open(os.path.join(d, "mb", "responses", f"{rid3}.json"), "w").write("{not json")
        time.sleep(3.2)
        assert mn.ingest_llm() == []
        kinds = [e["kind"] for e in led.events(limit=50)]
        assert "llm_failed" in kinds


def test_mailbox_fake_responder_thread_end_to_end_without_blocking():
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        root = os.path.join(d, "mb")
        mb = MailboxLLM(root)
        mn = Miner(led, seed=1, llm=mb, llm_min_interval_s=0.0, llm_n=2)
        stop = threading.Event()

        def responder():
            seen = set()
            while not stop.is_set():
                for fn in os.listdir(os.path.join(root, "requests")):
                    if fn.endswith(".json") and not fn.startswith(".") and fn not in seen:
                        seen.add(fn)
                        rid = fn[:-5]
                        time.sleep(0.3)
                        _respond(root, rid, GOOD[:2])
                time.sleep(0.05)

        th = threading.Thread(target=responder, daemon=True)
        th.start()
        t0 = time.time()
        rid = mn.request_llm("propose", "cross_contrast")
        assert time.time() - t0 < 0.5                                                  # submit does not wait for the agent
        got = []
        for _ in range(100):
            got = mn.ingest_llm()
            if got:
                break
            time.sleep(0.1)
        stop.set(); th.join(2)
        assert len(got) == 2 and mb.n_pending() == 0
        assert {r["status"] for r in led.conn.execute("SELECT status FROM llm_requests")} == {"ingested"}


def test_mailbox_adopts_unanswered_request_after_restart_and_abandons():
    with tempfile.TemporaryDirectory() as d:
        mb = MailboxLLM(d)
        req = _req()
        mb.submit(req)
        mb2 = MailboxLLM(d, abandon_after_s=0.0)                                       # a "restarted" coordinator
        assert mb2.n_pending() == 1
        time.sleep(0.05)
        out = mb2.poll()
        assert len(out) == 1 and "_error" in out[0][1] and "abandoned" in out[0][1]["_error"]
        assert os.path.exists(os.path.join(d, "done", f"request_{req['id']}.json"))


def test_request_carries_no_market_data_only_formulas_and_summaries():
    r = _req()
    txt = json.dumps(r)
    assert r["protocol"] == 1 and r["dsl"]["max_nodes"] == 32 and "abandon_after_utc" in r
    assert "2018" not in txt and "2019" not in txt and "2020" not in txt and "vault" not in txt.lower().replace("sealed vault", "")


class _H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(n))
        assert self.headers.get("Authorization") == "Bearer k"
        user = json.loads(body["messages"][-1]["content"])
        content = json.dumps({"protocol": 1, "id": user["id"], "responder": "fake-http", "status": "ok",
                              "proposals": [{"expression": GOOD[0], "hypothesis": "h"}], "notes": ""})
        out = json.dumps({"choices": [{"message": {"content": "```json\n" + content + "\n```"}}]}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(out))); self.end_headers()
        self.wfile.write(out)

    def log_message(self, *a):
        pass


def test_openai_compat_backend_against_local_fake_server():
    srv = http.server.HTTPServer(("127.0.0.1", 0), _H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    try:
        be = OpenAICompatLLM(base_url=f"http://127.0.0.1:{srv.server_port}/v1", api_key="k", model="m", timeout_s=10)
        req = _req(1)
        be.submit(req)
        got = be.wait(req["id"], 10, 0.1)
        assert got is not None
        ok, props, err = validate_response(got[1], req)
        assert ok, err
        assert props[0]["expression"] == GOOD[0] and be.n_pending() == 0
    finally:
        srv.shutdown()
