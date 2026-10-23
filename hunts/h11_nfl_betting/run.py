import pandas as pd, numpy as np, json, math
from scipy.stats import binomtest
d=pd.read_csv('data/games.csv'); d=d[d.result.notna()&d.spread_line.notna()].sort_values(['gameday','game_id']).reset_index(drop=True)
# Elo (pre-game)
elo={}; last=None; pre=[]
for _,g in d.iterrows():
    if g.season!=last:
        elo={k:1500+(v-1500)*2/3 for k,v in elo.items()}; last=g.season
    h=elo.get(g.home_team,1500); a=elo.get(g.away_team,1500); pre.append((h+65-a)/25)
    dif=h+65-a; eh=1/(1+10**(-dif/400)); mov=g.result
    s=1.0 if mov>0 else (0.5 if mov==0 else 0.0)
    wd=dif if mov>0 else -dif
    mult=math.log(abs(mov)+1)*2.2/(wd*0.001+2.2) if mov!=0 else 1
    ch=20*mult*(s-eh); elo[g.home_team]=h+ch; elo[g.away_team]=a-ch
d['elo_pred']=pre
cover=d.result-d.spread_line  # >0 home covers
ou=d.total-d.total_line       # >0 over
outd=d.roof.isin(['outdoors','open'])
PAC={'SEA','SF','LA','LAC','OAK','LV','SD'}; EAST={'NE','NYJ','NYG','BUF','MIA','PHI','PIT','BAL','WAS','CLE','CIN','ATL','CAR','TB','JAX','IND','DET'}
S={}
def side(mask,o): return o[mask]
S['S1_home_dog']=cover[d.spread_line<0]
S['S2_div_home_dog']=cover[(d.spread_line<0)&(d.div_game==1)]
S['S3_wind_under']=-ou[outd&(d.wind>=15)]
S['S4_cold_under']=-ou[outd&(d.temp<=32)]
hr=(d.home_rest>=13)&(d.away_rest<=8); ar=(d.away_rest>=13)&(d.home_rest<=8)
S['S5_rest_edge']=pd.concat([cover[hr],-cover[ar]])
hs=(d.home_rest<=4)&(d.away_rest>=7); as_=(d.away_rest<=4)&(d.home_rest>=7)
S['S6_short_week_fade']=pd.concat([-cover[hs],cover[as_]])
S['S7_west_early_east']=cover[d.away_team.isin(PAC)&d.home_team.isin(EAST)&(d.gametime<='13:05')]
e=d.elo_pred-d.spread_line
S['S8_elo_vs_line']=pd.concat([cover[e>=3],-cover[e<=-3]])
S['S9_big_dog']=pd.concat([cover[d.spread_line<=-10],-cover[d.spread_line>=10]])
N0=298; N=N0+len(S); rng=np.random.default_rng(11)
def stats(m):
    w=(m>0).sum(); l=(m<0).sum(); p=(m==0).sum(); pnl=np.where(m>0,1/1.1,np.where(m<0,-1,0.0))
    bs=rng.choice(pnl,(10000,len(pnl))).mean(1) if len(pnl) else np.array([np.nan])
    return dict(bets=int(len(m)),push=int(p),win=round(100*w/max(w+l,1),2),roi=round(100*pnl.mean(),2),
      p=binomtest(int(w),int(w+l),0.5238,alternative='greater').pvalue if w+l else 1.0,
      ci=(round(100*np.percentile(bs,2.5),2),round(100*np.percentile(bs,97.5),2)))
rows=[]
for k,m in S.items():
    seas=d.loc[m.index,'season']; r={'name':k}
    for t,msk in [('IS',seas<=2018),('OOS',seas>=2019)]:
        r.update({f'{t}_{a}':b for a,b in stats(m[msk.values]).items()})
    rows.append(r)
R=pd.DataFrame(rows).sort_values('OOS_p'); adj=[];run=0
for i,p in enumerate(R.OOS_p): run=max(run,min(1,(N-i)*p)); adj.append(run)
R['OOS_holm']=adj; R['pass']=(R.OOS_roi>0)&(R.OOS_holm<0.05)&(R.IS_roi>0)
R=R.sort_values('name'); R.to_csv('results.csv',index=False); print(R.to_string()); print('N',N)
