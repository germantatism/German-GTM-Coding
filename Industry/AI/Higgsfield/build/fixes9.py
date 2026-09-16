# -*- coding: utf-8 -*-
import json, sys, urllib.request
from engine import *
from extras import tb, shape, BLACK, WHITE
from countries import ROLES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service(); EMU=12700
P=svc.presentations().get(presentationId=COPY).execute(); SL=[Slide(s) for s in P['slides']]; SP={s.id:s for s in SL}
US=SL[22]; RU=SL[41]; RANK=SP['g3db258e17b2_3_268']; TOP=SP['g3db0b697a2f_0_11825']
NAVY={'red':0.118,'green':0.153,'blue':0.380}
def near(s,role,tol=5):
    x,y=ROLES[role]; m=s.near(x,y,tol=tol); return m[0] if len(m)==1 else None
def by_prefix(s,p): return [el for el,tr in s.els if text_of(el).strip().startswith(p)]
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
reqs=[]
# ---- US ----
reqs+=replace_requests(near(US,'title'),"United States: Stripe stays; PayPal, Venmo and redundancy are the upside")
reqs+=replace_requests(near(US,'stat_label'),"Stripe auth rate (US, Europe, Australia)")
reqs+=replace_requests(near(US,'stat_sub'),"Link on 40%+ of transactions (Stripe)")
reqs+=replace_requests(near(US,'tot_sub'),"new + recovered subs · ~$4.0M/yr upside")
for el in by_prefix(US,"Source: Interac"): reqs+=replace_requests(el,"Source: Stripe customer story; Higgsfield help center (Aug 1 2026); SimilarWeb  ·  TO VALIDATE: Higgsfield US MAU, checkout starts, current paid conversion, payment-method mix, decline codes")
# ---- Russia ----
reqs+=replace_requests(near(RU,'title'),"Russia: #3 by traffic, not addressable under current sanctions")
reqs+=replace_requests(near(RU,'stat_label'),"Share of Higgsfield traffic (SimilarWeb)")
reqs+=replace_requests(near(RU,'l1_label'),"Visa and Mastercard suspended"); reqs+=replace_requests(near(RU,'l1_sub'),"foreign-issued cards stopped working")
reqs+=replace_requests(near(RU,'tot_label'),"NSPK (Mir) sanctioned by US Treasury"); reqs+=replace_requests(near(RU,'tot_sub'),"no compliant rail for a US merchant")
reqs+=replace_requests(near(RU,'L2h'),"Domestic rails are off-limits")
for el in by_prefix(RU,"Local methods move conversion"): reqs+=replace_requests(el,"No revenue is modeled for Russia; the traffic is shown for completeness only.")
chips=[el for el,tr in RU.els if text_of(el).strip()=='Blocked']
for el in chips:
    f=fill_of(el)
    if f and f.get('red',0)>0.3: reqs.append({'updateShapeProperties':{'objectId':el['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':NAVY},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# ---- S9 row text ----
for el in by_prefix(TOP,"Stripe baseline; PayPal"): reqs+=replace_requests(el,"Stripe baseline; PayPal / Venmo upside in appendix")
# ---- ranking rows 19-20: rebuild as inset-free text boxes ----
for el,tr in RANK.els:
    if el['objectId'].startswith('hf_r19_') or el['objectId'].startswith('hf_r20_'): reqs.append({'deleteObject':{'objectId':el['objectId']}})
# styles from row 18 cells (y ~ 421..433)
row18=sorted([(pos(el,tr)[0],el) for el,tr in RANK.els if text_of(el).strip() and 415<=pos(el,tr)[1]<=440 and pos(el,tr)[0]<700],key=lambda c:c[0])
print("row18 cells:",[(x,text_of(el).strip()[:8]) for x,el in row18])
def stl(el):
    for te in el['shape']['text'].get('textElements',[]):
        if 'textRun' in te and te['textRun'].get('content','').strip(): return {k:v for k,v in te['textRun'].get('style',{}).items() if k in TEXT_FIELDS}
    return {}
y18=pos(row18[0][1],next(t for e,t in RANK.els if e['objectId']==row18[0][1]['objectId']))[1]
ROWS=[(y18+15.5,["19","United States","1.82M","~3%","baseline","not in base case","appendix"]),(y18+31,["20","Russia","0.46M","n/a","n/a","not addressable","$0"])]
widths=[40,150,70,70,90,220,120]
for yy,vals in ROWS:
    reqs+=shape(RANK.id,'RECTANGLE',52,yy-2,1075-52,14,fill={'red':0.98,'green':0.98,'blue':1.0},outline='none')
    for ci,((x,el18),v,w) in enumerate(zip(row18,vals,widths)):
        st=stl(el18); oid=f"hf_r{int(yy)}_{ci}_{int(__import__('time').time())%100000}"
        reqs.append({'createShape':{'objectId':oid,'shapeType':'TEXT_BOX','elementProperties':{'pageObjectId':RANK.id,'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':14*EMU,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'translateX':(x-7)*EMU,'translateY':(yy-3)*EMU,'unit':'EMU'}}}})
        reqs.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':v}})
        if st: reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
        reqs.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'autofit':{'autofitType':'NONE'},'contentAlignment':'MIDDLE'},'fields':'autofit.autofitType,contentAlignment'}})
print("requests:",len(reqs)); run(svc,COPY,reqs,label='fixes9')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w"))
for n in (9,23,42,43):
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=Q['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute(); urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/thumbs/N{n:02d}.png")
print("thumbs ok")
