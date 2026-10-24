"""Combinatorial Purged Cross-Validation (Lopez de Prado 2018, ch. 12) for the pool-combination step.

T observations are cut into n_groups contiguous groups; every k-subset of groups is a test set (C(n,k) splits, phi = C(n,k)*k/n
backtest paths). Training rows within `purge` rows of a test group (labels overlap: 20-day horizon) and `embargo` rows after it
are removed. `cpcv_paths` assembles the phi paths so each group appears exactly once per path.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np


def group_bounds(T: int, n_groups: int):
    edges = np.linspace(0, T, n_groups + 1).astype(int)
    return [(int(edges[i]), int(edges[i + 1])) for i in range(n_groups)]


def cpcv_splits(T: int, n_groups: int = 10, k: int = 2, purge: int = 20, embargo: int = 5):
    """List of dicts: test_groups, test_idx (bool T), train_idx (bool T) with purge/embargo applied."""
    gb = group_bounds(T, n_groups); out = []
    for tg in combinations(range(n_groups), k):
        test = np.zeros(T, bool); excl = np.zeros(T, bool)
        for g in tg:
            a, b = gb[g]; test[a:b] = True
            excl[max(0, a - purge):min(T, b + embargo)] = True               # training rows whose label window touches the test block
        out.append(dict(test_groups=tg, test=test, train=~excl & ~test))
    return out


def n_paths(n_groups: int, k: int) -> int:
    from math import comb
    return comb(n_groups, k) * k // n_groups


def cpcv_paths(splits, n_groups: int):
    """Return list of paths; each path is list[(group, split_index)] covering every group exactly once."""
    by_group = {g: [i for i, s in enumerate(splits) if g in s["test_groups"]] for g in range(n_groups)}
    phi = len(by_group[0]); return [[(g, by_group[g][j]) for g in range(n_groups)] for j in range(phi)]
