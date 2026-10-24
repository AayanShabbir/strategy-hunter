"""Structural novelty: Zhang-Shasha tree-edit distance (d_TED) and frequent-subtree avoidance.

d_TED is the minimum number of node insertions, deletions and relabelings (unit costs) turning one ordered tree into
the other (Zhang & Shasha 1989; applied to formula ASTs following Sidorov et al. 2015). Because the DSL canonicalises
commutative operators (`Add`), argument order carries no spurious distance.

Novelty rule (blueprint 4): min over memory of d_TED(cand, T_m) / max(|cand|, |T_m|) >= 0.35.
Frequent-subtree rule: every subtree of depth <= 3 (and size >= 3, otherwise every formula contains `$close`) is counted
across the memory; a candidate containing a subtree whose support exceeds 15% of the memory is rejected. This is an exact
support count over a bounded subtree universe (the same quantity gSpan/FP-Growth would report for rooted induced subtrees
of this depth), so no mining library is needed.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from src.dsl.grammar import Node


def _prep(root: Node):
    """1-based postorder labels, leftmost-leaf-descendant indices, and keyroots."""
    labels, lml = [None], [0]

    def walk(n: Node) -> int:
        first = None
        for c in n.children:
            li = walk(c)
            if first is None:
                first = li
        labels.append(n.op)
        idx = len(labels) - 1
        lml.append(first if first is not None else idx)
        return lml[idx]

    walk(root)
    seen, keyroots = set(), []
    for i in range(len(labels) - 1, 0, -1):
        if lml[i] not in seen:
            seen.add(lml[i])
            keyroots.append(i)
    return labels, lml, sorted(keyroots)


def tree_edit_distance(a: Node, b: Node) -> int:
    """Zhang-Shasha ordered tree edit distance with unit insert/delete/relabel costs."""
    l1, m1, k1 = _prep(a)
    l2, m2, k2 = _prep(b)
    n, m = len(l1) - 1, len(l2) - 1
    td = [[0] * (m + 1) for _ in range(n + 1)]
    for i in k1:
        for j in k2:
            ai, bj = i - m1[i] + 2, j - m2[j] + 2
            fd = [[0] * bj for _ in range(ai)]
            for x in range(1, ai):
                fd[x][0] = fd[x - 1][0] + 1
            for y in range(1, bj):
                fd[0][y] = fd[0][y - 1] + 1
            for x in range(1, ai):
                for y in range(1, bj):
                    ix, jy = m1[i] + x - 1, m2[j] + y - 1
                    if m1[ix] == m1[i] and m2[jy] == m2[j]:
                        v = min(fd[x - 1][y] + 1, fd[x][y - 1] + 1, fd[x - 1][y - 1] + (0 if l1[ix] == l2[jy] else 1))
                        fd[x][y] = td[ix][jy] = v
                    else:
                        p, q = m1[ix] - m1[i], m2[jy] - m2[j]
                        fd[x][y] = min(fd[x - 1][y] + 1, fd[x][y - 1] + 1, fd[p][q] + td[ix][jy])
    return td[n][m]


def label_counter(n: Node) -> Counter:
    c: Counter = Counter()

    def walk(x: Node):
        c[x.op] += 1
        for k in x.children:
            walk(k)

    walk(n)
    return c


def normalized_ted(a: Node, b: Node, ca: Counter | None = None, cb: Counter | None = None, stop_below: float | None = None) -> float:
    """d_TED / max(|a|,|b|). Uses the exact lower bound max(|a|,|b|) - |common labels| to skip the O(n^2 k^2) DP when the
    pair is already provably far apart (the bound never overestimates, so the verdict is unchanged)."""
    sa, sb = a.size(), b.size()
    mx = max(sa, sb)
    ca = ca if ca is not None else label_counter(a)
    cb = cb if cb is not None else label_counter(b)
    lb = mx - sum((ca & cb).values())
    if stop_below is not None and lb / mx >= stop_below:
        return lb / mx                     # a valid lower bound that already clears the threshold
    return tree_edit_distance(a, b) / mx


def subtree_set(n: Node, max_depth: int = 3, min_size: int = 3) -> set[str]:
    """Canonical strings of all subtrees rooted at any node with depth <= max_depth and size >= min_size."""
    out: set[str] = set()

    def depth(x: Node) -> int:
        return 1 + max((depth(c) for c in x.children), default=0)

    def walk(x: Node):
        if x.size() >= min_size and depth(x) <= max_depth:
            out.add(x.canonical())
        for c in x.children:
            walk(c)

    walk(n)
    return out


@dataclass
class _Entry:
    hash: str
    node: Node
    size: int
    labels: Counter
    subtrees: set


@dataclass
class NoveltyMemory:
    """In-process mirror of the 'memory vault' of accepted ASTs (the shared ledger is the durable copy)."""
    min_ted: float = 0.35
    support_max: float = 0.15
    min_history: int = 30            # support is meaningless on a handful of formulas
    subtree_depth: int = 3
    subtree_min_size: int = 3
    entries: list = field(default_factory=list)
    hashes: set = field(default_factory=set)
    support: Counter = field(default_factory=Counter)

    def __len__(self) -> int:
        return len(self.entries)

    def add(self, node: Node, h: str) -> bool:
        if h in self.hashes:
            return False
        subs = subtree_set(node, self.subtree_depth, self.subtree_min_size)
        self.entries.append(_Entry(h, node, node.size(), label_counter(node), subs))
        self.hashes.add(h)
        self.support.update(subs)
        return True

    def blacklist(self) -> list[str]:
        """Subtrees whose support (share of memory formulas containing them) exceeds `support_max`."""
        n = len(self.entries)
        if n < self.min_history:
            return []
        return sorted(s for s, c in self.support.items() if c / n > self.support_max)

    def check(self, node: Node, h: str) -> tuple[bool, str, dict]:
        """(accepted, reason, detail). Order: duplicate -> frequent subtree -> tree-edit distance."""
        if h in self.hashes:
            return False, "duplicate", {}
        n = len(self.entries)
        if n >= self.min_history:
            bl = {s for s, c in self.support.items() if c / n > self.support_max}
            hit = sorted(subtree_set(node, self.subtree_depth, self.subtree_min_size) & bl)
            if hit:
                return False, "frequent_subtree", {"subtrees": hit[:3]}
        ca, sz = label_counter(node), node.size()
        best = float("inf")
        for e in self.entries:
            d = normalized_ted(node, e.node, ca, e.labels, stop_below=self.min_ted)
            best = min(best, d)
            if d < self.min_ted:
                return False, "ted", {"min_normalized_ted": round(d, 4), "nearest": e.hash[:12]}
        return True, "ok", {"min_normalized_ted": None if best == float("inf") else round(best, 4), "size": sz}
