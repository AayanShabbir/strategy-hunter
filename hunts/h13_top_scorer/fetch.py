import os, json, time, pandas as pd
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.enums import DataFeed
syms = json.load(open("/workspace/trading-desk/state/liquid500_2026-10-16.json"))["symbols"]
c = StockHistoricalDataClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"])
out = "/workspace/research_lab/data/alpaca/h13_15m"; os.makedirs(out, exist_ok=True)
for k in range(0, len(syms), 25):
    ch = [s for s in syms[k:k+25] if not os.path.exists(f"{out}/{s}.parquet")]
    if not ch: continue
    for att in range(5):
        try:
            df = c.get_stock_bars(StockBarsRequest(symbol_or_symbols=ch, timeframe=TimeFrame(15, TimeFrameUnit.Minute),
                 start=pd.Timestamp("2024-09-01", tz="UTC"), end=pd.Timestamp("2026-10-22", tz="UTC"), feed=DataFeed.IEX)).df
            break
        except Exception as e: print("err", e, flush=True); time.sleep(30)
    for s in ch:
        if s in df.index.get_level_values(0): df.xs(s, level=0).to_parquet(f"{out}/{s}.parquet")
        else: pd.DataFrame().to_parquet(f"{out}/{s}.parquet")
    print(k, len(df), time.strftime("%X"), flush=True)
print("DONE")
