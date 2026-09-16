# -*- coding: utf-8 -*-
import json, sys, urllib.request
from engine import *
from extras import shape, tb, BLUE, WHITE, BLACK
from content import grid_rows
from countries import ROLES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service(); EMU=12700
CANADA='g3db2d1d8a08_1_85'; CHINA='g3db2d1d8a08_1_589'; RANK='g3db258e17b2_3_268'; BUB='g3db0b697a2f_0_12850'; TOP='g3db0b697a2f_0_11825'
# 1) duplicate
resp=svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'duplicateObject':{'objectId':CANADA}},{'duplicateObject':{'objectId':CHINA}}]}).execute()
US=resp['replies'][0]['duplicateObject']['objectId']; RU=resp['replies'][1]['duplicateObject']['objectId']; print("new slides:",US,RU)
P=svc.presentations().get(presentationId=COPY).execute(); SP={s['objectId']:Slide(s) for s in P['slides']}
reqs=[]
def near(s,role,tol=5):
    x,y=ROLES[role]; m=s.near(x,y,tol=tol); return m[0] if len(m)==1 else None
def fill_roles(s,vals):
    miss=[]
    for role,v in vals.items():
        el=near(s,role)
        if el: reqs.extend(replace_requests(el,v))
        else: miss.append(role)
    return miss
def by_text(s,txt):
    return [el for el,tr in s.els if text_of(el).strip()==txt]
def swap_flag(s,iso):
    for el,tr in s.els:
        if 'image' in el and pos(el,tr)[1]<70 and pos(el,tr)[0]<130:
            w=el['size']['width']['magnitude']*tr.get('scaleX',1); h=el['size']['height']['magnitude']*tr.get('scaleY',1)
            reqs.append({'deleteObject':{'objectId':el['objectId']}})
            reqs.append({'createImage':{'objectId':f"hf_flag_{iso}",'url':f"https://flagcdn.com/w160/{iso}.png",'elementProperties':{'pageObjectId':s.id,'size':{'width':{'magnitude':w,'unit':'EMU'},'height':{'magnitude':h,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}}})
            reqs.append({'updateImageProperties':{'objectId':f"hf_flag_{iso}",'imageProperties':{'outline':{'outlineFill':{'solidFill':{'color':{'rgbColor':{'red':0.75,'green':0.77,'blue':0.85}},'alpha':1}},'weight':{'magnitude':0.75*EMU,'unit':'EMU'},'dashStyle':'SOLID'}},'fields':'outline'}})
# ---- United States ----
su=SP[US]
US_VALS={'title':"United States: Stripe stays as the baseline; PayPal, Venmo and redundancy are the upside",
 'stat':"95.6%",'stat_label':"Stripe authorization rate (US, Europe, Australia)",'stat_sub':"Link on 40%+ of transactions (Stripe case study)",
 'mau':"~1.8M",'mau_label':"Estimated Higgsfield MAU",'mau_sub':"1.5–2.1M range; 15.1% of traffic (#1)",
 'l1':"~9K",'l1_label':"Incremental paid subscribers",'l1_sub':"upside, not in the ~$25M base case",
 'tot':"~11K",'tot_label':"Total paid-subscriber impact",'tot_sub':"new + recovered subs · ~$4.0M/yr upside, all levers",
 'L1h':"+~9K new paid subscribers",'L1u':"~$2.7M/year (upside)",'L1p':"Add PayPal, Venmo and Cash App Pay; Stripe keeps cards, Link, Apple Pay, Klarna and Affirm",
 'L2h':"+~1.9K recovered approvals/yr",'L2u':"~$0.4M/year (upside)",'L2p':"Second processor as failover; network tokens on both routes",
 'L3h':"+~7.9K renewals saved/yr",'L3u':"~$0.9M/year (upside)",'L3p':"Cross-PSP retries and account updater on the largest paid base",
 'role_hdr':"Role for Higgsfield",
 'r1p':"Must-have",'r1m':"Cards + Link + Apple Pay (live)",'r1s':"95.6% auth; Link on 40%+ of transactions",'r1r':"Baseline stays on Stripe",
 'r2p':"Must-have",'r2m':"PayPal / Venmo",'r2s':"Help center: PayPal not supported today",'r2r':"Preferred-method acquisition",
 'r3p':"Optional",'r3m':"Cash App Pay, ACH / bank debit",'r3s':"Failed-card rescue",'r3r':"Coverage / fallback",
 'b1v':"~3%",'b2l':"With PayPal + Venmo added",'b2v':"~3.5%",'b3v':"+0.5pp",'b4v':"~$300/year",
 'sowhat':"The home market stays on Stripe. Yuno adds a second route for redundancy, PayPal and Venmo at checkout, and renewal recovery on the largest paid base: ~$4M/yr of upside kept out of the base case.",
 'src':"Source: Stripe customer story; Higgsfield help center (Aug 1 2026); SimilarWeb  ·  TO VALIDATE: Higgsfield US MAU, checkout starts, current paid conversion, payment-method mix, decline codes"}
print("US missing roles:",fill_roles(su,US_VALS)); swap_flag(su,'us')
# ---- Russia ----
sr=SP[RU]
RU_VALS={'title':"Russia: #3 by traffic, not addressable while card schemes and NSPK are under sanctions",
 'stat':"3.82%",'stat_label':"Share of Higgsfield web traffic (SimilarWeb)",'stat_sub':"#3 market by traffic",
 'mau':"~0.46M",'mau_label':"Estimated Higgsfield MAU",'mau_sub':"0.39–0.53M range (Yuno-estimated)",
 'l1':"Mar 2022",'l1_label':"Visa and Mastercard suspended operations",'l1_sub':"foreign-issued cards stopped working in Russia",
 'tot':"Feb 2024",'tot_label':"NSPK (Mir) designated by the US Treasury",'tot_sub':"no compliant domestic rail for a US merchant",
 'L1h':"No international card acquiring",'L1u':"$0 modeled",'L1p':"Visa and Mastercard suspended Russian operations in March 2022; foreign-issued cards do not work in Russia",
 'L2h':"Mir and Bank of Russia rails are off-limits",'L2u':"$0 modeled",'L2p':"NSPK, the operator of Mir, is under US sanctions since February 2024",
 'L3h':"Monitor, do not build",'L3u':"excluded from the ~$25M",'L3p':"Traffic stays in the top-20 view for completeness; revisit only if sanctions change",
 'role_hdr':"Status for Higgsfield",
 'r1p':"Blocked",'r1m':"Mir (NSPK)",'r1s':"Domestic scheme; sanctioned Feb 2024",'r1r':"Not available",
 'r2p':"Blocked",'r2m':"Visa / Mastercard",'r2s':"Operations suspended Mar 2022",'r2r':"Not available",
 'r3p':"Blocked",'r3m':"SBP (Bank of Russia rail)",'r3s':"Central bank rail",'r3r':"Not available under current US sanctions",
 'b1v':"n/a",'b2l':"Modeled contribution",'b2v':"$0",'b3v':"0pp",'b4v':"n/a",
 'sowhat':"Demand is real (#3 by traffic) but there is no compliant rail for a US merchant today. Russia is excluded from the business case and kept visible in the top 20 for completeness.",
 'src':"Source: The Moscow Times (Mar 6 2022); US Treasury designation of NSPK (Feb 23 2024) via Wikipedia; SimilarWeb"}
print("RU missing roles:",fill_roles(sr,RU_VALS)); swap_flag(sr,'ru')
for old,new in (("AUDIENCE EXPANSION","WHY EXCLUDED"),("AUTHORIZATION UPLIFT","DOMESTIC RAILS"),("RENEWAL CONTINUITY","RECOMMENDATION")):
    for el in by_text(sr,old): reqs+=replace_requests(el,new)
# ---- S41 rows 19-20 recreated from the original geometry ----
O=json.load(open(f"{OUT}/copy_deck.json")); so=Slide(next(s for s in O['slides'] if s['objectId']==RANK))
rows=[r for r in grid_rows(so,40,700,135,480) if len(r)>=7]; ys=[r[0][0] for r in rows[18:]]; y0=min(ys)-5; y1=max(ys)+13
VALS=[["19","United States","1.82M","~3%","Stripe baseline","upside, not in base case","see appendix"],["20","Russia","0.46M","n/a","not addressable","sanctions since 2022","$0"]]
n=0
for ri,r in enumerate(rows[18:20]):
    y=r[0][0]
    for el,tr in so.els:
        x,yy=pos(el,tr)
        if not (30<=x<=700 and abs(yy-y)<=8): continue
        w=el['size']['width']['magnitude']*tr.get('scaleX',1)/EMU
        if not text_of(el).strip() and 470<=x<=485 and w<150: continue   # skip bars
        if 'shape' not in el: continue
        oid=f"hf_r{ri+19}_{n}"; n+=1
        reqs.append({'createShape':{'objectId':oid,'shapeType':el['shape'].get('shapeType','RECTANGLE'),'elementProperties':{'pageObjectId':RANK,'size':el['size'],'transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}}})
        sp=el['shape'].get('shapeProperties',{}); props={}; fields=[]
        bf=sp.get('shapeBackgroundFill',{})
        if 'solidFill' in bf: props['shapeBackgroundFill']={'solidFill':bf['solidFill']}; fields.append('shapeBackgroundFill.solidFill')
        else: props['shapeBackgroundFill']={'propertyState':'NOT_RENDERED'}; fields.append('shapeBackgroundFill.propertyState')
        ol=sp.get('outline',{})
        if ol.get('outlineFill',{}).get('solidFill'): props['outline']={'outlineFill':{'solidFill':ol['outlineFill']['solidFill']},'weight':ol.get('weight',{'magnitude':9525,'unit':'EMU'})}; fields.append('outline')
        else: props['outline']={'propertyState':'NOT_RENDERED'}; fields.append('outline.propertyState')
        if sp.get('contentAlignment'): props['contentAlignment']=sp['contentAlignment']; fields.append('contentAlignment')
        reqs.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':props,'fields':','.join(fields)}})
        t=text_of(el).strip()
        if t:
            cells=sorted([c for c in r],key=lambda c:c[1]); idx=[c[2]['objectId'] for c in cells].index(el['objectId']) if el['objectId'] in [c[2]['objectId'] for c in cells] else None
            newt=VALS[ri][idx] if idx is not None and idx<7 else t
            reqs.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':newt}})
            st=None; ps=None
            for te in el['shape']['text'].get('textElements',[]):
                if 'paragraphMarker' in te and ps is None: ps=te['paragraphMarker'].get('style',{})
                if 'textRun' in te and te['textRun'].get('content','').strip() and st is None: st=te['textRun'].get('style',{})
            st={k:v for k,v in (st or {}).items() if k in TEXT_FIELDS}
            if st: reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
            ps={k:v for k,v in (ps or {}).items() if k in PARA_FIELDS}
            if ps: reqs.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':ps,'fields':','.join(ps.keys())}})
            reqs.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'autofit':{'autofitType':'NONE'}},'fields':'autofit.autofitType'}})
print("S41 recreated elements:",n)
# ---- S14: US bubble ----
reqs+=shape(BUB,'ELLIPSE',245-35,255-35,70,70,spans=[("United States",7.7,False,WHITE)],fill=BLUE,outline='none',valign='MIDDLE',align='CENTER')
# ---- S9: US row play text ----
for el in by_text(SP[TOP],"Stripe direct, unchanged (home market)"): reqs+=replace_requests(el,"Stripe baseline; PayPal / Venmo + redundancy upside (appendix)")
run(svc,COPY,reqs,label='US+RU build')
# move US slide after "How to read the numbers" (index 21 -> insertion 22)
P=svc.presentations().get(presentationId=COPY).execute(); ids=[s['objectId'] for s in P['slides']]
idx_read=ids.index('g3db258e17b2_3_991')
svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'updateSlidesPosition':{'slideObjectIds':[US],'insertionIndex':idx_read+1}}]}).execute()
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w")); ids=[s['objectId'] for s in Q['slides']]
print("slides:",len(ids),"| US at",ids.index(US)+1,"| RU at",ids.index(RU)+1)
for n_,sid in ((ids.index(US)+1,US),(ids.index(RU)+1,RU),(ids.index(RANK)+1,RANK),(ids.index(BUB)+1,BUB)):
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=sid,thumbnailProperties_thumbnailSize='LARGE').execute(); urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/thumbs/N{n_:02d}.png"); print("thumb N%02d"%n_)
