# -*- coding: utf-8 -*-
import json, sys, re, copy as cp
from engine import *
from content import BY_ID, BY_TEXT, TOP20, WAVE2, L1RANK, L1TOTAL, grid_rows
from countries import COUNTRIES, ROLES, role_values
from extras import bubble_requests, industry_slide, model_slide
import countries
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
DRY = len(sys.argv)>1 and sys.argv[1]=='dry'
OUT='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/f4e2fd5c-1a7c-44b0-a3b3-2d885642142e/scratchpad'
if DRY: P=json.load(open(f"{OUT}/copy_deck.json")); svc=None
else:
    svc=service(); P=svc.presentations().get(presentationId=COPY).execute(); json.dump(P,open(f"{OUT}/copy_deck_prebuild.json","w"))
SL=[Slide(s) for s in P['slides']]
FORBID=['OpenAI','ChatGPT','Claude','Grok','WAU','Adyen-only','Agent Pay','$2.5B','$1.4B','~410M','~16.8M','~$210M/month','$190M','$600M','1.2B','595m','Open AI','ChatGPT Go']
COUNTRY_FORBID=['Philippines','Saudi','Egypt','Malaysia','Argentina','Colombia','Poland','Thailand']
sim={}   # objectId -> new text (for dry-run forbidden check)
all_reqs={}  # slide index -> requests
MISSING=[]
def add(i,reqs):
    all_reqs.setdefault(i,[]).extend(reqs)
def rep(i,el,new):
    sim[el['objectId']]=new; add(i,replace_requests(el,new))

# 1) BY_ID and BY_TEXT
for i,m in BY_ID.items():
    s=SL[i-1]
    for suf,new in m.items(): rep(i,s.by_suffix(suf),new)
for i,lst in BY_TEXT.items():
    s=SL[i-1]
    for prefix,new in lst:
        try: els=s.by_text(prefix)
        except KeyError as e: MISSING.append((i,prefix)); continue
        for el in els:
            if el['objectId'] in sim: continue
            rep(i,el,new)
# 2) grids
def fill(i,data,xr,yr,cols,skip_prefix=None):
    s=SL[i-1]; rows=[r for r in grid_rows(s,xr[0],xr[1],yr[0],yr[1]) if len(r)>=cols]
    if skip_prefix: rows=[r for r in rows if not text_of(r[0][2]).strip().startswith(skip_prefix)]
    for r,d in zip(rows,data):
        for (y,x,el),val in zip(r[:cols],d): rep(i,el,str(val))
    return rows
r7=fill(7,TOP20,(30,680),(160,470),6)
r8=fill(8,[(n,c,p,pen,iu,pr,gap) for n,c,p,pen,iu,pr,gap in WAVE2],(55,760),(160,470),7)
r41=fill(41,L1RANK,(40,700),(135,480),7)
# S41 total row (7 cells at ~y 460+, starts 'PORTFOLIO TOTAL')
s41=SL[40]; tot=[r for r in grid_rows(s41,40,700,135,500) if text_of(r[0][2]).strip().startswith('PORTFOLIO')]
if tot:
    for (y,x,el),val in zip(tot[0],L1TOTAL): rep(41,el,val)
print("MISSING text prefixes:",MISSING)
print(f"grid rows: S7={len(r7)} S8={len(r8)} S41={len(r41)} S41total={len(tot)}")
# rows 19-20 of S41 to delete (data rows beyond 18)
del_ids=[]
if len(r41)>18:
    ys=[r[0][0] for r in r41[18:]]; y0=min(ys)-5; y1=max(ys)+13
    for el,tr in s41.els:
        x,y=pos(el,tr)
        if 30<=x<=700 and y0<=y<=y1: del_ids.append(el['objectId'])
print("S41 extra-row elements to delete:",len(del_ids))
# 3) country slides S21..S38
unmatched=[]
for k,d in enumerate(COUNTRIES):
    i=21+k; s=SL[i-1]; vals=role_values(d)
    roles=dict(ROLES); roles.update(getattr(countries,'OVERRIDES',{}).get(i,{}))
    for role,(x,y) in roles.items():
        m=s.near(x,y,tol=5)
        if len(m)!=1 and role=='src': m=[el for el,tr in s.els if text_of(el).strip().startswith('Source:')]
        if len(m)!=1: unmatched.append((i,d['c'],role,len(m))); continue
        rep(i,m[0],vals[role])
print("country roles unmatched:",unmatched[:20], "..." if len(unmatched)>20 else "")
# 3b) bubble chart
add(12,bubble_requests(SL[11],sim))
# 4) dry-run forbidden scan
if DRY:
    bad=[]
    for i,s in enumerate(SL,1):
        if i in (39,40): continue
        for el,tr in s.els:
            t=sim.get(el['objectId'], text_of(el)).strip()
            if not t: continue
            for f in FORBID+([] if i==8 else COUNTRY_FORBID):
                if f in t: bad.append((i,el['objectId'].split('_')[-1],f,t[:70])); break
    print(f"\nFORBIDDEN leftovers: {len(bad)}")
    for b in bad: print("  ",b)
    print("\ntotal requests:",sum(len(v) for v in all_reqs.values()))
    sys.exit(0)
# ===== APPLY =====
for i in sorted(all_reqs): run(svc,COPY,all_reqs[i],label=f"S{i}")
if del_ids: run(svc,COPY,[{'deleteObject':{'objectId':o}} for o in del_ids],label='S41 rows')
run(svc,COPY,[{'deleteObject':{'objectId':SL[38].id}},{'deleteObject':{'objectId':SL[39].id}}],label='delete 2 country slides')
print("core apply done")
# ===== new slides =====
P2=svc.presentations().get(presentationId=COPY).execute()
def img_url(slide_idx,suffix):
    for el,tr in Slide(P2['slides'][slide_idx]).els:
        if el['objectId'].endswith('_'+suffix) and 'image' in el: return el['image'].get('contentUrl')
logo=img_url(1,'1791'); psp=[(img_url(4,s),w,h) for s,w,h in [('3135',37,14),('3138',40,13),('3141',43,13)]]
layout=P2['slides'][1]['slideProperties']['layoutObjectId']
run(svc,COPY,industry_slide('hf_industry',layout,logo),label='industry slide')
hf_logo=None
try:
    svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'createImage':{'objectId':'hf_logo_probe','url':'https://logo.clearbit.com/higgsfield.ai','elementProperties':{'pageObjectId':'hf_industry','size':{'width':{'magnitude':10*12700,'unit':'EMU'},'height':{'magnitude':10*12700,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'translateX':0,'translateY':0,'unit':'EMU'}}}}]}).execute()
    svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'deleteObject':{'objectId':'hf_logo_probe'}}]}).execute()
    hf_logo='https://logo.clearbit.com/higgsfield.ai'; print("Higgsfield logo: clearbit OK")
except Exception as e: print("Higgsfield logo unavailable, using text:",str(e)[:100])
run(svc,COPY,model_slide('hf_model',layout,logo,psp,hf_logo),label='model slide')
print("ALL DONE")
