# Offline replica of orb_1am.pine. Data: yfinance MNQ=F 5m continuous (free, ~60 days max). Research only.
import json, warnings, numpy as np, pandas as pd, yfinance as yf
warnings.filterwarnings("ignore")
d = yf.download("MNQ=F", period="60d", interval="5m", prepost=True, progress=False, auto_adjust=False)
d.columns = [c[0] for c in d.columns]; d = d.tz_convert("America/New_York")
d.to_csv("mnq_5m_yf.csv")
PT, TICK = 2.0, 0.25
COST_PTS = (2*0.62)/PT + 2*TICK          # round trip: commission + 1 tick slip each side, in points
tr = pd.concat([d.High-d.Low,(d.High-d.Close.shift()).abs(),(d.Low-d.Close.shift()).abs()],axis=1).max(axis=1)
d["atr"] = tr.rolling(14).mean(); d["ema"] = d.Close.ewm(span=50,adjust=False).mean()
sess = (d.index - pd.Timedelta(hours=18)).date      # VWAP anchored 18:00 ET (Globex open)
tp=(d.High+d.Low+d.Close)/3; d["vwap"]=(tp*d.Volume).groupby(sess).cumsum()/d.Volume.groupby(sess).cumsum().replace(0,np.nan)
days=[]
for day,g in d.groupby(d.index.date):
    t=g.index.time; r=g[(t>=pd.Timestamp("01:00").time())&(t<pd.Timestamp("01:15").time())]
    w=g[(t>=pd.Timestamp("01:15").time())&(t<pd.Timestamp("09:30").time())]
    if len(r)<3 or len(w)<10: continue
    days.append(dict(day=day,rh=r.High.max(),rl=r.Low.min(),atr=r.atr.iloc[-1],w=w))
W=pd.Series([x["rh"]-x["rl"] for x in days]); A=pd.Series([x["atr"] for x in days])
medW=W.shift(1).rolling(20,min_periods=5).median(); medA=A.shift(1).rolling(20,min_periods=5).median()
def sim(w,i,side,rh,rl):           # entry next bar open after signal bar i
    if i+1>=len(w): return None
    e=w.Open.iloc[i+1]; stop=rl if side>0 else rh; risk=abs(e-stop)
    if risk<=0 or (side>0 and e<=stop) or (side<0 and e>=stop): return None
    tgt=e+side*0.5*risk
    for j in range(i+1,len(w)):
        h,l=w.High.iloc[j],w.Low.iloc[j]
        if (side>0 and l<=stop) or (side<0 and h>=stop): px=stop; break   # stop first if both (conservative)
        if (side>0 and h>=tgt) or (side<0 and l<=tgt): px=tgt; break
    else: px=w.Close.iloc[-1]
    return (side*(px-e)-COST_PTS)/risk, side*(px-e)-COST_PTS, COST_PTS/risk
def run(f, rng=None):
    out=[]
    for k,x in enumerate(days):
        w=x["w"]; rh,rl=x["rh"],x["rl"]
        if f=="F2_atr_calm" and not (x["atr"]<medA[k]): continue
        if f=="F3_width" and not (0.5*medW[k]<=rh-rl<=2*medW[k]): continue
        if f=="F4_tue_thu" and pd.Timestamp(x["day"]).dayofweek not in (1,2,3): continue
        sig=np.where(w.Close>rh,1,np.where(w.Close<rl,-1,0)); idx=np.flatnonzero(sig)
        if not len(idx): continue
        i=idx[0]; side=sig[i]
        if rng is not None: side=rng.choice([-1,1])            # random-direction control at same time/stop
        c=w.Close.iloc[i]
        if f=="F1_ema" and side*(c-w.ema.iloc[i])<=0: continue
        if f=="F5_vwap" and side*(c-w.vwap.iloc[i])<=0: continue
        res=sim(w,i,side,rh,rl)
        if res: out.append((x["day"],)+res)
    return pd.DataFrame(out,columns=["day","R","pts","cost_frac"])
def stats(t):
    if not len(t): return dict(n=0)
    g,l=t.R[t.R>0].sum(),-t.R[t.R<0].sum(); eq=(t.pts*PT).cumsum()
    return dict(n=len(t),win=round((t.R>0).mean(),3),avgR=round(t.R.mean(),3),PF=round(g/l,2) if l else None,
                net_usd=round(eq.iloc[-1],1),maxDD_usd=round((eq-eq.cummax()).min(),1),med_cost_of_stop=round(t.cost_frac.median(),3))
split=days[int(len(days)*0.6)]["day"]; res={"data":f"MNQ=F 5m yfinance {days[0]['day']}..{days[-1]['day']}, {len(days)} days","oos_from":str(split),"cost_pts_rt":COST_PTS}
for f in ["base","F1_ema","F2_atr_calm","F3_width","F4_tue_thu","F5_vwap"]:
    t=run(f); rs=np.random.default_rng(7); ctrl=[run(f,rs).R.mean() for _ in range(200)]
    p=float(np.mean(np.array(ctrl)>=t.R.mean())) if len(t) else 1.0
    res[f]=dict(all=stats(t),IS=stats(t[t.day<split]),OOS=stats(t[t.day>=split]),rand_ctrl_avgR=round(float(np.mean(ctrl)),3),p_vs_random=p)
json.dump(res,open("results.json","w"),indent=1,default=str); print(json.dumps(res,indent=1,default=str))
