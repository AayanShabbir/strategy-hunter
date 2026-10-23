"""Port of Hunt #16 (daily grid) on real cached Alpaca bars: must reproduce 0 passes."""
import os, shutil, pytest
HERE = os.path.dirname(os.path.abspath(__file__))
@pytest.mark.skipif(not os.path.exists(os.path.join(HERE, "..", "data_cache", "1Day", "SPY.parquet")), reason="cache not seeded")
def test_h16_port_zero_passes(sandbox):
    from hunt_engine import runner
    sp = sandbox / "h16.yaml"; shutil.copy(os.path.join(HERE, "h16_supertrend_port.yaml"), sp)
    res, _ = runner.run(str(sp), quiet=True, n_random=500)
    assert len(res["variants"]) == 27 and res["n_pass"] == 0
