# Swarm LLM mailbox protocol (v1)

The swarm's Miner can ask an LLM for formula ideas. There is no API key, so the LLM is a dedicated Grok Bot agent,
**"Swarm Miner"**, reached through a **file mailbox**. This document is the contract for that agent. If you are the
Swarm Miner agent, this is everything you need.

Research only. Nothing here places orders or touches a broker. Formulas you propose are *hypotheses*; they are
back-tested and audited by code you cannot influence. Most will fail, and that is expected and fine.

## 1. Where things live

Mailbox root (git-ignored runtime data, on the box): `/workspace/research_lab/data/swarm/llm_mailbox/`

| dir | who writes | meaning |
|---|---|---|
| `requests/`  | swarm miner | one `<id>.json` per open request |
| `responses/` | **you (the agent)** | one `<id>.json` per answered request |
| `done/`      | swarm miner | requests/responses already ingested or abandoned (you never touch it) |

`<id>` looks like `req_20261024T020000Z_ab12cd34` (UTC time + 8 hex chars). The response file **must use exactly the
same id**: request `requests/req_X.json` is answered by `responses/req_X.json`.

## 2. Your job loop (run every ~10 minutes)

1. List `requests/*.json` (ignore names starting with `.`). For each one with **no** `responses/<id>.json` yet:
2. Read it. Skip it (write nothing) if `expires_at` is already in the past.
3. Produce proposals per section 3 and write the response per section 4.
4. Write **atomically**: write to `responses/.<id>.json.tmp`, then rename (`mv`) to `responses/<id>.json`. A half-written
   response is never picked up if you do this; do not write directly to the final name.
5. Never edit or delete files in `requests/` or `done/`. Never write anywhere outside `responses/`.

Answer every request at most once. If you cannot produce anything useful, still answer with `"status": "error"` and a
`"notes"` explanation (section 6) so the swarm does not wait for nothing. Late responses are still ingested until
`abandon_after_utc` (see request), so a slow answer is fine.

## 3. Request file

```json
{
  "protocol": 1,
  "id": "req_20261024T020000Z_ab12cd34",
  "created_utc": "2026-10-24T02:00:00Z",
  "expires_at": "2026-10-24T03:00:00Z",
  "kind": "propose",
  "persona": "volatility",
  "persona_brief": "Ideas about how risky a stock has been recently, and how that compares with price or volume.",
  "n": 8,
  "dsl": {
    "features": ["$close", "$high", "$low", "$volume"],
    "unary": ["Log(x)", "TsStd(x, W)"],
    "binary": ["Add(x, y)", "Sub(x, y)", "Div(x, y)"],
    "windows": ["5d", "10d", "20d", "60d"],
    "max_nodes": 32,
    "notes": "TsStd is the rolling standard deviation and its 2nd argument must be one of the windows. Log(x)=log(|x|+1e-8). Add is commutative (argument order is ignored)."
  },
  "constraints": {"min_normalized_ted": 0.35, "frequent_subtree_support_max": 0.15, "subtree_max_depth": 3},
  "avoid": {
    "n_total_tried": 412,
    "recent": [{"hash": "9f2c...", "expression": "Div(TsStd($close, 20d), $close)"}],
    "blacklisted_subtrees": ["TsStd($close, 20d)", "Sub($high, $low)"]
  },
  "feedback": [],
  "data_scope": "S&P 500 daily bars, search data only (train 2010-2016 + validation 2017). Test years and the sealed vault are never used or described."
}
```

* `kind`: `"propose"` (fresh ideas for the `persona`) or `"refine"` (improve the formulas listed in `feedback`).
* `n`: how many formulas the swarm wants. Send **at most `n`**; extras are ignored. Quality over quantity; fewer is fine.
* `persona`: one of `momentum`, `mean_reversion`, `volatility`, `liquidity`, `range_microstructure`,
  `cross_contrast`. `persona_brief` is a plain-English hint. Follow it loosely; novelty matters more.
* `avoid.recent`: formulas already tried (most recent up to 200, with `hash` and `expression`). Do **not** repeat them or
  make trivial variations (changing only a window, swapping the Add arguments).
* `avoid.blacklisted_subtrees`: sub-expressions that already appear in more than 15% of past formulas. A proposal that
  *contains* any of them (as an exact sub-expression) is rejected. Build from other pieces.
* `feedback` (only for `refine`; empty for `propose`): list of objects, one per earlier formula:

```json
{"hash": "9f2c...", "expression": "Div(TsStd($close, 20d), $close)",
 "failed_gates": ["pbo", "dsr"],
 "summary": {"search_sharpe_annual": 0.31, "search_ic": 0.004, "turnover_annual": 38.0,
             "pbo": 0.58, "dsr": 0.02, "spa_p": 0.41, "delta_ic": null, "max_abs_corr_with_pool": 0.12},
 "note": "In-search Sharpe was weak and unstable across time blocks."}
```

  Gate names: `ted` (too similar to something tried), `subtree` (contains an over-used sub-expression), `cpcv`
  (leakage/purge check), `pbo` (probability of backtest overfitting >= 0.10), `dsr` (deflated Sharpe p >= 0.05),
  `spa` (Hansen SPA p > 0.05), `corr` (correlation >= 0.30 with a pool member), `delta_ic` (adds no information).
  Everything in `summary` comes from the **search data** (train + validation) only.

### Data you may and may not see
You only ever get the summaries above. The request will never contain raw returns, prices, test-year results or anything
from the sealed vault, and **you must not look for them**: do not open anything under `/workspace/research_lab/data/`
except the mailbox, `engine/vault/`, `engine/runs/`, `runs_sde/`, or `src/audit/ledger.jsonl`. Do not try to improve a
formula by reading results other than what the request gives you. Do not contact any trading or broker system.

## 4. Response file

Formulas are written as **DSL strings** exactly as the swarm's parser (`src.dsl.grammar.parse_ast`) accepts them.

```json
{
  "protocol": 1,
  "id": "req_20261024T020000Z_ab12cd34",
  "responder": "swarm_miner",
  "created_utc": "2026-10-24T02:07:31Z",
  "status": "ok",
  "proposals": [
    {"expression": "Div(Sub($high, $low), TsStd($volume, 10d))",
     "hypothesis": "Daily range relative to how erratic volume has been; wide ranges on stable volume may signal informed trading."},
    {"expression": "Sub(Log($volume), Log(TsStd($close, 60d)))",
     "hypothesis": "Liquidity per unit of long-run price risk."}
  ],
  "notes": ""
}
```

Rules for every `expression`:

* Allowed tokens only: features `$close $high $low $volume`; `Log(x)`; `TsStd(x, W)` with `W` in `5d 10d 20d 60d`;
  `Add(x, y)`, `Sub(x, y)`, `Div(x, y)`. Case-sensitive. Function-call syntax with commas. No numbers other than the
  window tokens, no `$returns`/`$open`/`$vwap`, no other operators (`cs_rank`, `ts_mean`, ... do **not** exist here).
* A window token appears only as the 2nd argument of `TsStd`.
* At most `dsl.max_nodes` (32) nodes in total (every operator, feature and window token counts as one node).
* Each formula should reference **different structure**, not only different windows. The swarm rejects a formula whose
  normalized tree-edit distance to *any* earlier formula is below 0.35.
* Optional per-proposal field `"parent_hash"` (for `refine`): the hash of the formula you are improving.
* Do not add other top-level fields that change behaviour; unknown fields are ignored.

Valid examples: `Div($close, TsStd($close, 20d))`, `Sub(Log($volume), Log(Div($high, $low)))`,
`Add(Div(Sub($high, $low), $close), Log(TsStd($volume, 60d)))`.
Invalid examples: `ts_mean(close, 20)` (unknown syntax), `TsStd($close, 15d)` (window not allowed), `Log($close, 2)` (arity),
`Div($close)` (arity), `$returns` (unknown feature).

## 5. What the swarm does with your response (so you know what happens)

1. Strictly validates JSON (`protocol`, `id`, `status`, `proposals`).
2. Parses each `expression` with `parse_ast`. Invalid ones are rejected and counted as rejected proposals.
3. Applies the novelty filters (tree-edit distance and frequent-subtree). Rejected ones are logged.
4. Every proposal you send, valid or not, is counted as a trial in the global trial counter N (that only makes the
   statistical bar stricter, so sending junk costs the swarm). Survivors are back-tested by workers and audited.
5. The request and response files are moved to `done/`.

## 6. Failure handling

* **You cannot answer**: write `{"protocol":1,"id":...,"responder":"swarm_miner","status":"error","proposals":[],"notes":"why"}`.
* **Malformed or unreadable response**: the swarm ignores it, logs it, and moves it to `done/`. Do not rewrite it; a
  second response for the same id is ignored. If you made a mistake, wait for the next request.
* **No response**: after `timeout` the swarm keeps backtesting its own generator's proposals and keeps polling; if
  nothing arrives before `abandon_after_utc` the request is abandoned and moved to `done/`.
* **Duplicate/invalid ids, wrong protocol number**: ignored.
* If a request has an unknown `protocol` value or `kind`, reply with `status: "error"`.

## 7. Helper commands (optional, read-only)

* `cd /workspace/research_lab && ./engine/hunt swarm-llm-check '<expression>' ['<expression>' ...]` prints, for each
  string, `VALID <hash> <node_count>` or `INVALID <reason>`. Use it to self-check formulas before answering.
* `./engine/hunt swarm-llm-ping` writes one small `propose` request and waits for the response (used to test the loop).
