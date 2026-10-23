"""Guard: nautilus/ is backtest-only. No live nodes, exec/data clients, or adapters."""
import os, re, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
BANNED = re.compile(r"(nautilus_trader\.adapters|nautilus_trader\.live|\bTradingNode\b|LiveExecClient|LiveDataClient|LiveMarketDataClient|ExecClient|DataClientConfig|ExecClientConfig)")

def _py_files():
    return [p for p in ROOT.rglob("*.py") if ".venv" not in p.parts and p.name != "test_guard.py"]

def test_no_live_imports():
    bad = [f"{p}:{i}" for p in _py_files() for i, l in enumerate(p.read_text().splitlines(), 1) if BANNED.search(l)]
    assert not bad, f"live/adapter usage found: {bad}"

def test_wrapper_strips_keys():
    env = dict(os.environ, ALPACA_API_KEY="x", ALPACA_SECRET_KEY="x", KALSHI_KEY_ID="x", FINNHUB_API_KEY="x",
               FMP_API_KEY="x", APCA_API_KEY_ID="x", FOO_API_KEY="x", BAR_SECRET_TOKEN="x", HARMLESS="ok")
    out = subprocess.run([str(ROOT / "run.sh"), "-c",
        "import os;print(sorted(k for k in os.environ if any(s in k for s in ('ALPACA','KALSHI','FINNHUB','FMP','APCA','API_KEY','SECRET'))));print(os.environ.get('HARMLESS'))"],
        env=env, capture_output=True, text=True, check=True).stdout.split("\n")
    assert out[0] == "[]", out
    assert out[1] == "ok"

def test_guard_catches_violation(tmp_path):
    assert BANNED.search("from nautilus_trader.live.node import TradingNode")
    assert BANNED.search("from nautilus_trader.adapters.alpaca import x")
