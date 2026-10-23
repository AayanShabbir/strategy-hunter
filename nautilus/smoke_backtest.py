"""Smoke backtest: SPY daily SMA(20/50) cross, pre-vault data only, with fees."""
from decimal import Decimal
import json, pathlib
import pandas as pd
from nautilus_trader.backtest.engine import BacktestEngine, BacktestEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import AccountType, OmsType, OrderSide
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Money, Quantity
from nautilus_trader.model.data import BarType
from nautilus_trader.persistence.wranglers import BarDataWrangler
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.backtest.models import FixedFeeModel
from nautilus_trader.trading.strategy import Strategy, StrategyConfig
from nautilus_trader.indicators import SimpleMovingAverage

HERE = pathlib.Path(__file__).parent
VAULT = pd.Timestamp("2025-10-23", tz="UTC")

class SmaCfg(StrategyConfig, frozen=True):
    bar_type: str
    fast: int = 20
    slow: int = 50
    qty: int = 10

class SmaCross(Strategy):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.bt = BarType.from_str(cfg.bar_type)
        self.f = SimpleMovingAverage(cfg.fast); self.s = SimpleMovingAverage(cfg.slow)
    def on_start(self):
        self.inst = self.cache.instrument(self.bt.instrument_id)
        self.register_indicator_for_bars(self.bt, self.f); self.register_indicator_for_bars(self.bt, self.s)
        self.subscribe_bars(self.bt)
    def on_bar(self, bar):
        if not self.s.initialized: return
        flat = self.portfolio.is_flat(self.bt.instrument_id)
        if self.f.value > self.s.value and flat:
            self.submit_order(self.order_factory.market(self.bt.instrument_id, OrderSide.BUY, Quantity.from_int(self.config.qty)))
        elif self.f.value < self.s.value and not flat:
            self.close_all_positions(self.bt.instrument_id)
    def on_stop(self):
        self.close_all_positions(self.bt.instrument_id)

def main():
    df = pd.read_parquet(HERE.parent / "engine/data_cache/1Day/SPY.parquet")
    df = df[df.index < VAULT].copy(deep=True)
    df.index = df.index.astype("datetime64[ns, UTC]")
    assert df.index.max() < VAULT
    eng = BacktestEngine(BacktestEngineConfig(logging=LoggingConfig(log_level="ERROR")))
    inst = TestInstrumentProvider.equity(symbol="SPY", venue="XNAS")
    eng.add_venue(Venue("XNAS"), oms_type=OmsType.NETTING, account_type=AccountType.CASH,
                  base_currency=USD, starting_balances=[Money(10_000, USD)],
                  fee_model=FixedFeeModel(Money(1.00, USD)))
    eng.add_instrument(inst)
    bt = BarType.from_str(f"{inst.id}-1-DAY-LAST-EXTERNAL")
    bars = BarDataWrangler(bt, inst).process(pd.DataFrame(df.to_numpy(copy=True), index=df.index, columns=df.columns))
    eng.add_data(bars)
    eng.add_strategy(SmaCross(SmaCfg(bar_type=str(bt))))
    eng.run()
    acct = eng.trader.generate_account_report(Venue("XNAS"))
    fills = eng.trader.generate_order_fills_report()
    pos = eng.trader.generate_positions_report()
    end_bal = float(str(acct["total"].iloc[-1]).split()[0])
    rep = {"nautilus_version": __import__("nautilus_trader").__version__,
           "data": f"SPY 1Day {df.index.min().date()}..{df.index.max().date()} ({len(df)} bars, pre-vault)",
           "strategy": "SMA20/50 long-flat, 10 sh, FixedFeeModel $1.00 per fill",
           "fills": len(fills), "positions": len(pos), "commissions_usd": float(sum(float(str(c).split()[0]) for c in fills["commissions"].apply(lambda x: x[0] if isinstance(x,list) and x else "0 USD"))) if "commissions" in fills else None,
           "start_usd": 10000, "end_usd": end_bal,
           "return_pct": round((end_bal/10000-1)*100, 2),
           "buyhold_spy_pct": round((df.close.iloc[-1]/df.close.iloc[0]-1)*100, 2)}
    eng.dispose()
    (HERE/"reports").mkdir(exist_ok=True)
    (HERE/"reports/smoke_report.json").write_text(json.dumps(rep, indent=2))
    print(json.dumps(rep, indent=2))

if __name__ == "__main__":
    main()
