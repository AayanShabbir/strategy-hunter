"""LLM idea backends for the Miner. Protocol spec: docs/swarm_llm_mailbox.md (that file is the contract the agent reads).

* `MailboxLLM`  - file mailbox under data/swarm/llm_mailbox/{requests,responses,done}; the "Swarm Miner" Grok Bot agent answers it
                  on its own schedule. Fully asynchronous: `submit` never blocks, `poll` returns whatever has arrived.
* `OpenAICompatLLM` - optional HTTP backend (env SWARM_LLM_BASE_URL, SWARM_LLM_API_KEY, SWARM_LLM_MODEL), same interface.
Neither backend ever sees prices, returns, test-year data or anything from the sealed vault: requests carry formula strings and
search-window summary statistics only (`build_request`).
Every response is untrusted text: `validate_response` is strict; the Miner then re-parses each formula through src.dsl.grammar.
"""
from __future__ import annotations

import abc
import json
import os
import re
import threading
import time
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from . import DATA_DIR, PROTOCOL

DEFAULT_MAILBOX = os.environ.get("SWARM_LLM_MAILBOX", os.path.join(DATA_DIR, "llm_mailbox"))
PERSONAS = {
    "momentum": "Ideas about recent price direction and trend strength, possibly scaled by risk.",
    "mean_reversion": "Ideas where an unusually high or low price/range relative to its own recent behaviour should snap back.",
    "volatility": "Ideas about how risky a stock has been recently, and how that compares with price or volume.",
    "liquidity": "Ideas built on trading volume and how it relates to price level or price risk.",
    "range_microstructure": "Ideas based on the daily high-low range versus the close or versus volume.",
    "cross_contrast": "Ideas that contrast two different features or two different horizons of the same feature.",
}
DSL_SPEC = {
    "features": ["$close", "$high", "$low", "$volume"], "unary": ["Log(x)", "TsStd(x, W)"], "binary": ["Add(x, y)", "Sub(x, y)", "Div(x, y)"],
    "windows": ["5d", "10d", "20d", "60d"], "max_nodes": 32,
    "notes": "TsStd is the rolling standard deviation and its 2nd argument must be one of the windows. Log(x)=log(|x|+1e-8). "
             "Add is commutative (argument order is ignored).",
}
DATA_SCOPE = ("S&P 500 daily bars, search data only (train 2010-2016 + validation 2017). Test years and the sealed vault are never "
              "used or described.")


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def new_request_id() -> str:
    return f"req_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:8]}"


def build_request(kind: str, persona: str, n: int, *, avoid_recent: list[dict], n_total_tried: int, blacklisted_subtrees: list[str],
                  feedback: Optional[list[dict]] = None, max_nodes: int = 32, ttl_s: float = 3600.0, abandon_after_s: float = 3600.0,
                  min_ted: float = 0.35, support_max: float = 0.15, subtree_max_depth: int = 3) -> dict:
    if kind not in ("propose", "refine"):
        raise ValueError(kind)
    now = datetime.now(timezone.utc)
    return {
        "protocol": PROTOCOL, "id": new_request_id(), "created_utc": _iso(now), "expires_at": _iso(now + timedelta(seconds=ttl_s)),
        "abandon_after_utc": _iso(now + timedelta(seconds=abandon_after_s)),
        "kind": kind, "persona": persona, "persona_brief": PERSONAS.get(persona, ""), "n": int(n),
        "dsl": dict(DSL_SPEC, max_nodes=max_nodes),
        "constraints": {"min_normalized_ted": min_ted, "frequent_subtree_support_max": support_max, "subtree_max_depth": subtree_max_depth},
        "avoid": {"n_total_tried": int(n_total_tried), "recent": avoid_recent[:200], "blacklisted_subtrees": blacklisted_subtrees[:100]},
        "feedback": feedback or [], "data_scope": DATA_SCOPE,
    }


def validate_response(resp: Any, req: dict) -> tuple[bool, list[dict], str]:
    """Strict schema check. Returns (ok, proposals, error). `proposals` are dicts with str `expression` (+ optional fields)."""
    if not isinstance(resp, dict):
        return False, [], "response is not a JSON object"
    if resp.get("protocol") != PROTOCOL:
        return False, [], f"unsupported protocol {resp.get('protocol')!r}"
    if resp.get("id") != req.get("id"):
        return False, [], "response id does not match request id"
    st = resp.get("status")
    if st == "error":
        return False, [], f"agent reported error: {str(resp.get('notes', ''))[:300]}"
    if st != "ok":
        return False, [], f"bad status {st!r}"
    props = resp.get("proposals")
    if not isinstance(props, list):
        return False, [], "proposals must be a list"
    out = []
    for p in props:
        if not isinstance(p, dict) or not isinstance(p.get("expression"), str):
            return False, [], "every proposal needs a string 'expression'"
        out.append({"expression": p["expression"].strip()[:2000], "hypothesis": str(p.get("hypothesis", ""))[:1000],
                    "parent_hash": str(p.get("parent_hash", ""))[:80]})
    return True, out, ""


class LLMBackend(abc.ABC):
    name = "abstract"

    @abc.abstractmethod
    def submit(self, request: dict) -> None:
        """Send a request; must not block on the answer."""

    @abc.abstractmethod
    def poll(self) -> list[tuple[dict, Any]]:
        """Non-blocking: [(request, response_or_error)] for everything that finished since the last call. An error is
        a dict {'_error': str}."""

    @abc.abstractmethod
    def n_pending(self) -> int: ...

    def wait(self, request_id: str, timeout: float, poll_interval: float = 2.0) -> Optional[tuple[dict, Any]]:
        """Blocking convenience (used by swarm-llm-ping and tests only; the swarm itself never blocks on the LLM)."""
        end = time.time() + timeout
        while True:
            for req, resp in self.poll():
                if req["id"] == request_id:
                    return req, resp
            if time.time() >= end:
                return None
            time.sleep(poll_interval)


class MailboxLLM(LLMBackend):
    name = "mailbox"

    def __init__(self, root: Optional[str] = None, timeout_s: float = 600.0, abandon_after_s: float = 3600.0, adopt_existing: bool = True):
        self.root = root or DEFAULT_MAILBOX
        self.timeout_s, self.abandon_after_s = timeout_s, abandon_after_s
        for d in ("requests", "responses", "done"):
            os.makedirs(os.path.join(self.root, d), exist_ok=True)
        self.pending: dict[str, tuple[dict, float]] = {}
        self.late_notified: set[str] = set()
        if adopt_existing:                      # requests left by a previous run: keep listening for their answers
            for fn in sorted(os.listdir(self._d("requests"))):
                if fn.endswith(".json") and not fn.startswith("."):
                    try:
                        req = json.load(open(os.path.join(self._d("requests"), fn)))
                        self.pending[req["id"]] = (req, os.path.getmtime(os.path.join(self._d("requests"), fn)))
                    except (OSError, ValueError, KeyError):
                        pass

    def _d(self, name: str) -> str:
        return os.path.join(self.root, name)

    def submit(self, request: dict) -> None:
        rid = request["id"]
        if not re.fullmatch(r"req_[0-9A-Za-z_]+", rid):
            raise ValueError("bad request id")
        tmp = os.path.join(self._d("requests"), f".{rid}.json.tmp")
        with open(tmp, "w") as f:
            json.dump(request, f, indent=1)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, os.path.join(self._d("requests"), f"{rid}.json"))      # atomic: the agent never sees a half-written request
        self.pending[rid] = (request, time.time())

    def n_pending(self) -> int:
        return len(self.pending)

    def overdue(self) -> list[str]:
        """Ids past `timeout_s` that have not been reported yet (informational; they stay pending until abandoned)."""
        now, out = time.time(), []
        for rid, (_, t0) in self.pending.items():
            if now - t0 > self.timeout_s and rid not in self.late_notified:
                self.late_notified.add(rid)
                out.append(rid)
        return out

    def _archive(self, rid: str) -> None:
        for d in ("requests", "responses"):
            src = os.path.join(self._d(d), f"{rid}.json")
            if os.path.exists(src):
                os.replace(src, os.path.join(self._d("done"), f"{d[:-1]}_{rid}.json"))

    def poll(self) -> list[tuple[dict, Any]]:
        out, now = [], time.time()
        for rid in list(self.pending):
            req, t0 = self.pending[rid]
            rp = os.path.join(self._d("responses"), f"{rid}.json")
            if os.path.exists(rp):
                try:
                    resp: Any = json.load(open(rp))
                except ValueError as e:
                    if now - os.path.getmtime(rp) < 3:        # a non-atomic writer may still be writing; look again next poll
                        continue
                    resp = {"_error": f"malformed JSON in response: {e}"}
                out.append((req, resp))
                del self.pending[rid]
                self._archive(rid)
            elif now - t0 > self.abandon_after_s:
                out.append((req, {"_error": "abandoned: no response before abandon_after"}))
                del self.pending[rid]
                self._archive(rid)
        return out


SYSTEM_PROMPT = ("You are the Swarm Miner: a quantitative researcher proposing formulas in a tiny DSL. Reply with ONE JSON object "
                 '{"protocol":1,"id":<request id>,"responder":"swarm_miner","status":"ok","proposals":[{"expression":"...","hypothesis":"..."}],"notes":""} '
                 "and nothing else. Use only the DSL in the request ($close,$high,$low,$volume; Log, TsStd(x, 5d|10d|20d|60d), Add, Sub, Div); "
                 "at most `n` proposals, each structurally different from the `avoid` list.")


class OpenAICompatLLM(LLMBackend):
    """Optional alternative: any OpenAI-compatible /chat/completions endpoint, configured only through env vars."""
    name = "openai-compat"

    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None, model: Optional[str] = None, timeout_s: float = 120.0):
        self.base = (base_url or os.environ.get("SWARM_LLM_BASE_URL", "")).rstrip("/")
        self.key = api_key or os.environ.get("SWARM_LLM_API_KEY", "")
        self.model = model or os.environ.get("SWARM_LLM_MODEL", "")
        if not (self.base and self.model):
            raise RuntimeError("OpenAI-compatible backend needs SWARM_LLM_BASE_URL and SWARM_LLM_MODEL (and SWARM_LLM_API_KEY if the server wants one)")
        self.timeout_s = timeout_s
        self._lock = threading.Lock()
        self._done: list[tuple[dict, Any]] = []
        self._inflight = 0

    def _call(self, req: dict) -> None:
        try:
            body = json.dumps({"model": self.model, "temperature": 0.9,
                               "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": json.dumps(req)}]}).encode()
            r = urllib.request.Request(self.base + "/chat/completions", data=body, method="POST",
                                       headers={"Content-Type": "application/json", **({"Authorization": f"Bearer {self.key}"} if self.key else {})})
            with urllib.request.urlopen(r, timeout=self.timeout_s) as fh:
                text = json.load(fh)["choices"][0]["message"]["content"]
            m = re.search(r"\{.*\}", text, re.S)
            resp: Any = json.loads(m.group(0)) if m else {"_error": "no JSON object in model output"}
        except Exception as e:                                         # network/parse errors become an error result, never a crash
            resp = {"_error": f"{type(e).__name__}: {str(e)[:200]}"}
        with self._lock:
            self._done.append((req, resp))
            self._inflight -= 1

    def submit(self, request: dict) -> None:
        with self._lock:
            self._inflight += 1
        threading.Thread(target=self._call, args=(request,), daemon=True).start()

    def poll(self) -> list[tuple[dict, Any]]:
        with self._lock:
            out, self._done = self._done, []
        return out

    def n_pending(self) -> int:
        with self._lock:
            return self._inflight + len(self._done)


def make_backend(kind: str, **kw) -> Optional[LLMBackend]:
    if kind in ("none", "", None):
        return None
    if kind == "mailbox":
        return MailboxLLM(**kw)
    if kind in ("openai", "http", "openai-compat"):
        return OpenAICompatLLM()
    raise ValueError(f"unknown LLM backend {kind!r} (none|mailbox|openai)")
