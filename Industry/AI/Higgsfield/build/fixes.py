# -*- coding: utf-8 -*-
import json, sys, math
from engine import *
from extras import shape, tb, line, BLUE, BLACK, WHITE, LILAC, EMU
from countries import COUNTRIES, ROLES, OVERRIDES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
OUT=sys.argv[1]; svc=service()
O=json.load(open(f"{OUT}/copy_deck.json"))          # pre-build geometry (same IDs)
P=svc.presentations().get(presentationId=COPY).execute()
S=[Slide(s) for s in P['slides']]; SO={s['objectId']:Slide(s) for s in O['slides']}
def cur(oid):  # current slide by original objectId
    return next(s for s in S if s.id==oid)
reqs=[]
def font(el,size):
    reqs.append({'updateTextStyle':{'objectId':el['objectId'],'textRange':{'type':'ALL'},'style':{'fontSize':{'magnitude':size,'unit':'PT'}},'fields':'fontSize'}})
# ---- (1) industry title, (2) exec hero, (3) speed-to-market paragraph + four-gaps small lines, (9) bridge ----
ind=next(s for s in S if s.id=='hf_industry')
for el,tr in ind.els:
    if text_of(el).startswith('AI video at a glance'): reqs+=replace_requests(el,"AI video at a glance: a fast-scaling category that Higgsfield leads")
ex=cur('g3dbb3d0b7de_0_1786'); font(ex.by_suffix('1794'),34)
sp=cur('g3dbb3d0b7de_0_2408')
reqs+=replace_requests(sp.by_suffix('2414'),"~6M Higgsfield MAU in the 18 addressable markets (~12M globally, Yuno-estimated). No AI-video competitor has localized checkout yet: Kling sells its global plans in USD via Stripe.")
fg=cur('g3dbb3d0b7de_0_2720')
reqs+=replace_requests(fg.by_suffix('2777'),"25% EM cross-border decline (Yuno model)")
reqs+=replace_requests(fg.by_suffix('2781'),"3.5% monthly renewal failure in EM (model)")
br=cur('g3dbb3d0b7de_0_5140')
for suf,t in [('5148',"~$2.1M/mo"),('5156',"~$1.8M/mo"),('5160',"~$0.11M/mo"),('5164',"~$0.24M/mo"),('5153',"Across 18 addressable markets.")]: reqs+=replace_requests(br.by_suffix(suf),t)
# ---- (5) top-20: Russia text + MRR bars ----
t20=cur('g3db0b697a2f_0_11825')
reqs+=replace_requests(t20.by_suffix('11880'),"Not addressable: sanctions since 2022")
MRR=[None,0.67,None,0.14,0.09,0.13,0.11,0.15,0.09,0.08,0.08,0.08,0.11,0.09,0.06,0.06,0.02,0.05,0.07,0.05]
rows=[r for r in __import__('content').grid_rows(t20,30,680,160,470) if len(r)>=6]
bars=[(el,tr) for el,tr in t20.els if not text_of(el).strip() and 'shape' in el and 520<=pos(el,tr)[0]<=620 and 150<=pos(el,tr)[1]<=480]
print("S9 bar candidates:",len(bars), [(el['shape'].get('shapeType'),pos(el,tr)) for el,tr in bars[:3]])
for r,m in zip(rows,MRR):
    y=r[0][0]; cand=[(el,tr) for el,tr in bars if abs(pos(el,tr)[1]-y)<=8]
    for el,tr in cand:
        if m is None: reqs.append({'deleteObject':{'objectId':el['objectId']}})
        else:
            base_w=el['size']['width']['magnitude']; sx=(40*EMU*m/0.67)/base_w
            reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':sx,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
# ---- (6) ranking bars ----
rk=cur('g3db258e17b2_3_268'); USERS=[30.1,6.9,4.5,4.0,4.7,3.9,3.9,2.8,2.6,3.2,2.4,2.4,2.2,1.9,1.9,1.8,2.3,0.9]
rbars=sorted([(pos(el,tr)[1],el,tr) for el,tr in rk.els if not text_of(el).strip() and 'shape' in el and 470<=pos(el,tr)[0]<=485 and 150<=pos(el,tr)[1]<=470],key=lambda x:x[0])
print("S41 bars:",len(rbars))
for (y,el,tr),u in zip(rbars,USERS):
    reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':0.61*u/30.1,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
# ---- (8) wave-2: penetration bars + chip fills + note ----
w2=cur('g3dbb3d0b7de_0_4441'); w2o=SO['g3dbb3d0b7de_0_4441']
from content import WAVE2
orows=[r for r in __import__('content').grid_rows(w2o,55,760,160,470) if len(r)>=7]
nrows=[r for r in __import__('content').grid_rows(w2,55,760,160,470) if len(r)>=7]
pbars=[(el,tr) for el,tr in w2.els if not text_of(el).strip() and 'shape' in el and 255<=pos(el,tr)[0]<=300 and 150<=pos(el,tr)[1]<=480]
print("S10 penetration bars:",len(pbars))
chips={}
for r in orows:
    pr=[c for c in r if text_of(c[2]).strip() in ('Very high','High','Medium','Medum')]
    if pr:
        el=pr[0][2]; f=el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
        chips.setdefault(text_of(el).strip().replace('Medum','Medium'),f)
print("chip fills:",chips)
for orow,nrow,d in zip(orows,nrows,WAVE2):
    y=nrow[0][0]; opct=float(text_of(orow[3][2]).strip().rstrip('%')); npct=float(d[3].rstrip('%'))
    for el,tr in pbars:
        if abs(pos(el,tr)[1]-y)<=8:
            reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1)*npct/opct,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
    chip=[c for c in nrow if text_of(c[2]).strip() in ('Very high','High','Medium')]
    if chip and chips.get(d[5]):
        reqs.append({'updateShapeProperties':{'objectId':chip[0][2]['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':chips[d[5]]},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
reqs+=replace_requests(w2.by_suffix('4788'),"Note: *First-mover priority = population × AI-video headroom × payment-localization gap × feasibility. Sources: DataReportal Digital 2026; PPRO country pages.")
# ---- (10) bubble twins ----
bb=cur('g3db0b697a2f_0_12850'); bbo=SO['g3db0b697a2f_0_12850']
from extras import BUBBLES
def center(el,tr):
    w=el['size']['width']['magnitude']*tr.get('scaleX',1); h=el['size']['height']['magnitude']*tr.get('scaleY',1); return (tr['translateX']+w/2, tr['translateY']+h/2)
small=[(el,tr) for el,tr in bbo.els if el.get('shape',{}).get('shapeType')=='ELLIPSE' and not text_of(el).strip()]
used=set()
for label,suf,cx,cy in BUBBLES:
    oel=bbo.by_suffix(suf); otr=next(tr for el,tr in bbo.els if el['objectId']==oel['objectId']); ocx,ocy=center(oel,otr)
    # label-style ellipses are small in height; pair with nearest small circle within 60pt
    best=None
    for el,tr in small:
        if el['objectId'] in used: continue
        scx,scy=center(el,tr); d=math.hypot((scx-ocx)/EMU,(scy-ocy)/EMU)
        if d<60 and (best is None or d<best[0]): best=(d,el,tr,scx,scy)
    oh=oel['size']['height']['magnitude']*otr.get('scaleY',1)/EMU
    if best and oh<30:   # only label-style ellipses have twins
        d,el,tr,scx,scy=best; used.add(el['objectId'])
        dx=cx*EMU-ocx; dy=cy*EMU-ocy
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX']+dx,'translateY':tr['translateY']+dy,'unit':'EMU'}}})
        print(f"  twin moved: {label} <- {el['objectId'][-5:]} (d={d:.0f})")
reqs+=replace_requests(bb.by_suffix('12916'),"Priority markets, ranked by Higgsfield web traffic (SimilarWeb)")
# ---- (11) country headlines / captions ----
SHORT_LABEL={'Germany':"PayPal share of online retail revenue (2025)",'Canada':"Interac e-Transfer transactions 2024 ($554B)",'United Arab Emirates':"Share of UAE e-commerce on cards; wallets 24%",'China':"Weixin + WeChat MAU (Tencent, Sep 2025)"}
SHORT_SUB={'India':"85.5% of digital payment volume (RBI)",'Indonesia':"44.9M merchants; wallets 35% of e-com (PCMI)",'United Kingdom':"16.5M user connections (OBL, Jan 2026)",'Germany':"SEPA DD 14.4%; all cards 13.7% (EHI 2026)",'Brazil':"Cards 40%; 170M+ Brazilians use Pix (BCB)",'Spain':"1.24B ops; 105.6M online purchases (+82%)",'Vietnam':"QR payments +106.7% volume YoY (SBV, 2024)",'South Korea':"Non-bank Pay apps 54.9% of easy-pay (BoK)",'Italy':"450K+ merchants; e-wallets 35% of e-com",'France':"14.5B CB transactions per year",'Canada':"88% of Canadians have used e-Transfer",'Mexico':"Banxico: SPEI to overtake cards by end-2026",'Netherlands':"71% of Dutch e-commerce payments (2025)",'Japan':"8.88B PayPay txns 2025; cashless 58% (METI)",'Pakistan':"Easypaisa 59M+; 92% of retail volume digital"}
import re
def short_head(t):
    t=t.replace(' incremental paid subscribers',' new paid subscribers').replace(' recovered card approvals/year',' recovered approvals/yr').replace(' renewals saved/year',' renewals saved/yr'); return t
for k,d in enumerate(COUNTRIES):
    i=23+k; s=S[i-1]; roles=dict(ROLES); roles.update(OVERRIDES.get(21+k,{}))
    def near(role):
        x,y=roles[role]; m=s.near(x,y,tol=5); return m[0] if len(m)==1 else None
    for role,val in [('L1h',short_head(d['L1'][0])),('L2h',short_head(d['L2'][0])),('L3h',short_head(d['L3'][0]))]:
        el=near(role)
        if el: reqs+=replace_requests(el,val)
    if d['c'] in SHORT_LABEL:
        el=near('stat_label'); 
        if el: reqs+=replace_requests(el,SHORT_LABEL[d['c']])
    if d['c'] in SHORT_SUB:
        el=near('stat_sub')
        if el: reqs+=replace_requests(el,SHORT_SUB[d['c']])
# ---- (3c) speed-to-market chart rebuild ----
page=sp.id
old=[el for el,tr in sp.els if el['objectId'].endswith('_2439')]
if old: reqs.append({'deleteObject':{'objectId':old[0]['objectId']}})
x0,y0,w,h=95,180,430,250   # plot area
GREY={'red':0.6,'green':0.6,'blue':0.6}; RED={'red':0.86,'green':0.2,'blue':0.2}
months=list(range(0,25,2)); L1=83.0
yuno=[0,0.06,0.15,0.28,0.42,0.56,0.68,0.78,0.86,0.92,0.96,0.99,1.0]
comp=[0,0.03,0.07,0.11,0.22,0.33,0.44,0.53,0.63,0.72,0.77,0.81,0.86]
noloc=[m/24*0.2 for m in months]
def X(m): return x0+w*m/24
def Y(v): return y0+h-(h*v*L1/90)
reqs+=line(page,x0,y0,x0,y0+h,color=BLACK)+line(page,x0,y0+h,x0+w,y0+h,color=BLACK)
for v in (0,30,60,90):
    reqs+=tb(page,x0-38,Y(v/L1)-7,34,14,[(f"{v}K",7.5,False,BLACK)],align='END')
for m in (0,6,12,18,24):
    reqs+=tb(page,X(m)-14,y0+h+3,28,12,[(f"M{m}",7.5,False,BLACK)],align='CENTER')
for series,color in ((yuno,BLUE),(comp,RED),(noloc,GREY)):
    for a in range(len(months)-1):
        x1,y1,x2,y2=X(months[a]),Y(series[a]),X(months[a+1]),Y(series[a+1])
        oid=f"hf_seg_{color['red']}_{a}".replace('.','')+str(int(y1))
        reqs.append({'createLine':{'objectId':oid,'lineCategory':'STRAIGHT','elementProperties':{'pageObjectId':page,'size':{'width':{'magnitude':(x2-x1)*EMU,'unit':'EMU'},'height':{'magnitude':abs(y2-y1)*EMU or 1,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1 if y2>=y1 else -1,'translateX':x1*EMU,'translateY':y1*EMU,'unit':'EMU'}}}})
        reqs.append({'updateLineProperties':{'objectId':oid,'lineProperties':{'lineFill':{'solidFill':{'color':{'rgbColor':color},'alpha':1}},'weight':{'magnitude':2.25*EMU,'unit':'EMU'}},'fields':'lineFill,weight'}})
leg=[("Higgsfield + Yuno (moves now)",BLUE),("Higgsfield without localization",GREY),("Competitor localizes first",RED)]
lx=x0
for t,c in leg:
    reqs+=shape(page,'ELLIPSE',lx,y0+h+22,8,8,fill=c,outline='none')+tb(page,lx+11,y0+h+18,150,14,[(t,8,False,BLACK)]); lx+=150
reqs+=tb(page,x0-40,y0-16,470,14,[("Paid subscribers captured in the 18 markets over 24 months (Yuno model, illustrative)",8,False,BLACK)])
print("total fix requests:",len(reqs))
run(svc,COPY,reqs,label='fixes')
print("FIXES DONE")
