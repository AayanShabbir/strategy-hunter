import pandas as pd, numpy as np, torch, json
from chronos import BaseChronosPipeline
torch.set_num_threads(4)
o=pd.read_pickle('/workspace/trading-desk/validation/data/ALL_1d.pkl').loc['SPY']
c=o['close'].values.astype('float32'); idx=o.index
p=BaseChronosPipeline.from_pretrained("amazon/chronos-bolt-small",device_map="cpu",torch_dtype=torch.float32)
L=256;H=5;rows=[]
ts=list(range(L-1,len(c)))
for b in range(0,len(ts),64):
    bt=ts[b:b+64]; ctx=[torch.tensor(c[t-L+1:t+1]) for t in bt]
    q,m=p.predict_quantiles(ctx,prediction_length=H,quantile_levels=[0.1,0.5,0.9])
    for t,qq in zip(bt,q.numpy()): rows.append((idx[t],c[t],qq[H-1,0],qq[H-1,1],qq[H-1,2]))
pd.DataFrame(rows,columns=['ts','close','q10','q50','q90']).to_parquet('forecasts.parquet')
from huggingface_hub import model_info
try: rev=model_info("amazon/chronos-bolt-small").sha
except Exception as e: rev=str(e)
open('model_rev.txt','w').write(str(rev)); print(len(rows),rev)
