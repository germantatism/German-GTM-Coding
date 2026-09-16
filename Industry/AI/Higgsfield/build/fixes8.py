# -*- coding: utf-8 -*-
import json, sys, math
from engine import *
from extras import tb, BLACK, BUBBLES
from content import grid_rows, TOP20
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
P=svc.presentations().get(presentationId=COPY).execute(); SL=[Slide(s) for s in P['slides']]; SP={s.id:s for s in SL}
BLUE={'red':0.24,'green':0.31,'blue':0.88}; GREY={'red':0.45,'green':0.47,'blue':0.55}
EMU=12700
reqs=[]
def style(oid,st): reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
# S2 / S7 new slides: title 28pt blue one line, kicker grey
for sid,title in (('hf_industry',"AI video at a glance: a category that Higgsfield leads"),('hf_model',"From one processor to one global financial infrastructure")):
    s=SP[sid]
    for el,tr in s.els:
        t=text_of(el).strip(); x,y=pos(el,tr)
        if y==46 and x==60: reqs+=replace_requests(el,title); style(el['objectId'],{'fontSize':{'magnitude':28,'unit':'PT'},'foregroundColor':{'opaqueColor':{'rgbColor':BLUE}}})
        if y==23 and x==60: style(el['objectId'],{'foregroundColor':{'opaqueColor':{'rgbColor':GREY}}})
        if sid=='hf_model' and t.startswith('Failover + Recovery'):
            reqs+=replace_requests(el,"Failover + Recovery\nCross-processor cascade and retry logic recovers renewals that a single retry schedule gives up on, covering the dunning scope of Higgsfield's Lifecycle & Retention role.")
# S3 unit split
ex=SP['g3dbb3d0b7de_0_1786']; reqs+=replace_requests(ex.by_suffix('1803'),"~$21M/year"); reqs+=replace_requests(ex.by_suffix('1809'),"~$4M/year")
# S4
sp=SP['g3dbb3d0b7de_0_2408']; reqs+=replace_requests(sp.by_suffix('2414'),"~6.1M Higgsfield MAU in 18 addressable markets (~12M globally). No AI-video competitor has localized checkout yet: Kling sells globally in USD via Stripe.")
# S5
fg=SP['g3dbb3d0b7de_0_2720']
reqs+=replace_requests(fg.by_suffix('2725'),"STRATEGIC CONTEXT  ·  THE DECISION FRAME")
reqs+=replace_requests(fg.by_suffix('2752'),"Better, but EM gaps remain")
reqs.append({'deleteObject':{'objectId':fg.by_suffix('2727')['objectId']}})
reqs+=replace_requests(fg.by_suffix('2782'),"~$0.24M/mo at stake"); reqs+=replace_requests(fg.by_suffix('2778'),"~$0.11M/mo at stake")
reqs+=replace_requests(fg.by_suffix('2826'),"Option A captures a fraction of the $25M. Option B captures the full $25M, because Yuno includes redundancy plus the local rails and people a second PSP can't deliver alone.")
# S6, S8, S11, S12, S16
reqs+=replace_requests(SP['g3dbb3d0b7de_0_3107'].by_suffix('3122'),"New integration: a single API unlocks everything below")
reqs+=replace_requests(SP['g3dbb3d0b7de_0_3430'].by_suffix('3444'),"Embedded with 30+ local APMs")
reqs+=replace_requests(SP['g3dbb3d0b7de_0_5140'].by_suffix('5151'),"Estimated Higgsfield monthly active users")
reqs+=replace_requests(SP['g3dbb3d0b7de_0_5468'].by_suffix('5489'),"Payment infra is the moat that models can't catch up to")
reqs+=replace_requests(SP['g3dbb3d0b7de_0_6081'].by_suffix('6090'),"Includes Adyen + Stripe + 30 local PSPs per market\nCross-PSP retry unlocks full Lever 3 (~$2.8M/yr)\nMulti-acquirer routing maximizes Lever 2 (~$1.3M/yr)\n100% of the addressable opportunity")
# S9: kicker + bars (width by value, color by archetype)
t20=SP['g3db0b697a2f_0_11825']; reqs+=tb(t20.id,60,23,338,15,[("PRIORITY MARKETS  ·  TOP 20 BY TRAFFIC",12,False,GREY)])
rows=[r for r in grid_rows(t20,30,680,160,470) if len(r)>=6]
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
chipfill={}
for r,d in zip(rows,TOP20):
    y=r[0][0]
    for el,tr in t20.els:
        if not text_of(el).strip() and 'shape' in el and 575<=pos(el,tr)[0]<=590 and abs(pos(el,tr)[1]-y)<=6 and fill_of(el): chipfill.setdefault(d[5],fill_of(el))
for r,d in zip(rows,TOP20):
    y=r[0][0]; m=d[3]
    for el,tr in t20.els:
        if text_of(el).strip() or 'shape' not in el or abs(pos(el,tr)[1]-y)>6: continue
        x=pos(el,tr)[0]; w=el['size']['width']['magnitude']*tr.get('scaleX',1)/EMU
        if 300<=x<=345 and w<80:
            if m in ('Baseline','n/a'): reqs.append({'deleteObject':{'objectId':el['objectId']}}); continue
            v=float(m.strip('$M')); sx=(45*EMU*v/0.67)/el['size']['width']['magnitude']
            reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':sx,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
            if chipfill.get(d[5]): reqs.append({'updateShapeProperties':{'objectId':el['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':chipfill[d[5]]},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# S14: kicker, bubble sizes by MAU, label fixes
bb=SP['g3db0b697a2f_0_12850']; reqs+=tb(bb.id,60,23,600,15,[("PRIORITY MARKETS  ·  TRAFFIC VS LOCAL-PAYMENT INTENSITY",12,False,GREY)])
MAU={"India":1.50,"United Kingdom":0.45,"South Korea":0.45,"Germany":0.40,"Brazil":0.39,"Indonesia":0.35,"Spain":0.28,"Italy":0.26,"France":0.24,"Canada":0.24,"Turkey":0.24,"Vietnam":0.20,"Netherlands":0.19,"UAE":0.19,"China":0.19,"Japan":0.18,"Mexico":0.16,"Pakistan":0.15}
def center(el,tr):
    w=el['size']['width']['magnitude']*tr.get('scaleX',1); h=el['size']['height']['magnitude']*tr.get('scaleY',1); return tr['translateX']+w/2,tr['translateY']+h/2,w,h
small=[(el,tr) for el,tr in bb.els if el.get('shape',{}).get('shapeType')=='ELLIPSE' and not text_of(el).strip()]
def rescale(el,tr,d):
    cx,cy,w,h=center(el,tr); bw=el['size']['width']['magnitude']; bh=el['size']['height']['magnitude']
    sx=d*EMU/bw; sy=d*EMU/bh
    reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':sx,'scaleY':sy,'shearX':0,'shearY':0,'translateX':cx-d*EMU/2,'translateY':cy-d*EMU/2,'unit':'EMU'}}})
for label,suf,_,_ in BUBBLES:
    el=bb.by_suffix(suf); tr=next(t for e,t in bb.els if e['objectId']==el['objectId']); cx,cy,w,h=center(el,tr)
    d=10+60*math.sqrt(MAU[label]/1.5)
    if h/EMU>=30: rescale(el,tr,d)   # filled ellipse with text inside
    else:
        best=min(small,key=lambda st: math.hypot(center(st[0],st[1])[0]-cx,center(st[0],st[1])[1]-cy))
        if math.hypot(center(best[0],best[1])[0]-cx,center(best[0],best[1])[1]-cy)/EMU<60: rescale(best[0],best[1],d)
        # widen label ellipse so words don't break
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1)*max(1,70/(w/EMU)),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':cx-max(w,70*EMU)/2,'translateY':tr['translateY'],'unit':'EMU'}}})
for suf,size in (('12940',6),('12934',5.5),('12941',6)):
    style(bb.by_suffix(suf)['objectId'],{'fontSize':{'magnitude':size,'unit':'PT'}})
print("requests:",len(reqs))
if len(sys.argv)>2 and sys.argv[2]=='apply':
    run(svc,COPY,reqs,label='fixes8'); print("applied")
