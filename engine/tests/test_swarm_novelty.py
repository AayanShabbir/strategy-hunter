"""Tree-edit-distance and frequent-subtree constraints of the Miner."""
import itertools
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.dsl.grammar import ast_hash, parse_expr  # noqa: E402
from swarm.ast_json import json_to_node, node_hash, node_to_json, payload_to_node  # noqa: E402
from swarm.miner import Miner, SymbolicGenerator  # noqa: E402
from swarm.novelty import NoveltyMemory, normalized_ted, subtree_set, tree_edit_distance  # noqa: E402
from swarm.shared_ledger import SharedLedger  # noqa: E402


def test_ted_known_values_and_metric_axioms():
    p = parse_expr
    assert tree_edit_distance(p("Add($close, $high)"), p("Add($close, $high)")) == 0
    assert tree_edit_distance(p("Add($close, $high)"), p("Add($close, $low)")) == 1          # one relabel
    assert tree_edit_distance(p("Div($close, $high)"), p("Sub($close, $high)")) == 1
    assert tree_edit_distance(p("Log($close)"), p("$close")) == 1                          # one insertion
    assert tree_edit_distance(p("Add($close, $high)"), p("Add($high, $close)")) == 0         # commutative canonicalisation
    rng = random.Random(0)
    g = SymbolicGenerator(0)
    ts = [p(g.sample("cross_contrast", 0.6)) for _ in range(12)]
    for a, b, c in itertools.combinations(ts, 3):
        dab, dbc, dac = (tree_edit_distance(x, y) for x, y in ((a, b), (b, c), (a, c)))
        assert dac <= dab + dbc                                                                 # triangle inequality
        assert tree_edit_distance(a, b) == tree_edit_distance(b, a)


def test_normalized_ted_lower_bound_shortcut_is_consistent():
    p = parse_expr
    a, b = p("Div(TsStd($close, 20d), $volume)"), p("Add(Log($high), Log($low))")
    full = normalized_ted(a, b)
    lb = normalized_ted(a, b, stop_below=0.35)
    assert lb <= full + 1e-12 and (lb >= 0.35) == (full >= 0.35)


def test_memory_rejects_near_duplicates_and_accepts_distant():
    m = NoveltyMemory(min_ted=0.35, min_history=10_000)
    base = parse_expr("Div(TsStd($close, 20d), Add($volume, $high))")
    m.add(base, node_hash(base))
    near = parse_expr("Div(TsStd($close, 10d), Add($volume, $high))")              # one relabel of 7 nodes -> d = 1/7 < 0.35
    ok, reason, _ = m.check(near, node_hash(near))
    assert (ok, reason) == (False, "ted")
    far = parse_expr("Sub(Log($low), TsStd($volume, 5d))")
    assert m.check(far, node_hash(far))[0]
    assert m.check(base, node_hash(base))[1] == "duplicate"


def test_frequent_subtree_avoidance():
    m = NoveltyMemory(min_ted=0.0, support_max=0.15, min_history=10)
    common = "TsStd($close, 20d)"
    for i, w in enumerate(["Add", "Sub", "Div"] * 4):
        n = parse_expr(f"{w}({common}, {['$high', '$low', '$volume', '$close'][i % 4]})#" if False else f"{w}({common}, {['$high', '$low', '$volume', '$close'][i % 4]})")
        m.add(n, f"h{i}{w}")
    assert common in m.blacklist() or parse_expr(common).canonical() in m.blacklist()
    cand = parse_expr(f"Log(Add({common}, $low))")
    ok, reason, detail = m.check(cand, "new")
    assert not ok and reason == "frequent_subtree" and detail["subtrees"]
    # leaves are never blacklisted (size >= 3 rule)
    assert all(len(s) > 8 for s in m.blacklist())
    assert subtree_set(parse_expr("$close")) == set()


def test_miner_outputs_task_payloads_with_ast_trees_and_every_proposal_is_counted():
    with tempfile.TemporaryDirectory() as d:
        led = SharedLedger(os.path.join(d, "t.db"))
        led.set_baseline({"engine_n": 0, "sde_n": 0, "note": "test"})
        mn = Miner(led, seed=3)
        tasks = mn.propose_batch(40, max_attempts=2000)
        assert len(tasks) == 40
        for t in tasks:
            node = payload_to_node(t["ast"])                                     # strict re-parse of the AST JSON
            assert node_hash(node) == t["ast_hash"] and t["expression"] == node.canonical() and node.size() <= 32
            assert json_to_node(node_to_json(node)).canonical() == node.canonical()
        # pairwise: every accepted formula is >= 0.35 normalised TED from all earlier accepted ones
        nodes = [parse_expr(t["expression"]) for t in tasks]
        for i in range(len(nodes)):
            for j in range(i):
                assert normalized_ted(nodes[i], nodes[j]) >= 0.35 - 1e-12
        assert led.n_swarm_trials() == mn.stats["generated"]                     # rejected proposals count as trials too
        assert led.n_trials() == led.n_swarm_trials()
        # off-grammar / oversized proposals are rejected and counted
        r = mn.screen("Foo($close)", "test")
        assert r["status"] == "REJECTED_SYNTAX" and led.n_swarm_trials() == mn.stats["generated"] + 1
