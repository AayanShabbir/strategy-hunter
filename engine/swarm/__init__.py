"""Distributed multi-agent strategy discovery swarm (research only; places no orders, holds no broker keys).

Roles (docs/swarm.md): Miner -> Backtest Workers -> Auditor -> Trader/Combiner -> Publisher, synchronised through the
SQLite (WAL) trial ledger in `shared_ledger.py`. The DSL, validators and portfolio maths are imported from `src/`
(the SDE), never duplicated.
"""
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if REPO_ROOT not in sys.path:          # make `import src...` work wherever the process was started
    sys.path.insert(0, REPO_ROOT)

PROTOCOL = 1
DATA_DIR = os.environ.get("SWARM_DATA_DIR", os.path.join(REPO_ROOT, "data", "swarm"))
DEFAULT_DB = os.environ.get("SWARM_DB", os.path.join(REPO_ROOT, "data", "ledger", "trials.db"))
