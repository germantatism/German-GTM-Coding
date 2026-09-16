import json, sys
from engine import *
from extras import model_slide
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
lay={l['objectId']:l for l in P['layouts']}
arch=P['slides'][5]  # architecture slide now at index 5 (0-based) after industry insertion
master=lay[arch['slideProperties']['layoutObjectId']]['layoutProperties']['masterObjectId']
cands=sorted([(len(l.get('pageElements',[])),l['objectId'],l['layoutProperties'].get('displayName')) for l in P['layouts'] if l['layoutProperties'].get('masterObjectId')==master])
print("arch slide:",text_of(Slide(arch).els[0][0]) if Slide(arch).els else '', "| master:",master,"| layouts:",cands[:4]); layout=cands[0][1]
def img_url(slide_idx,suffix):
    for el,tr in Slide(P['slides'][slide_idx]).els:
        if el['objectId'].endswith('_'+suffix) and 'image' in el: return el['image'].get('contentUrl')
logo=img_url(2,'1791'); psp=[(img_url(5,s),w,h) for s,w,h in [('3135',37,14),('3138',40,13),('3141',43,13)]]
print("logo:",bool(logo),"psp:",all(u for u,_,_ in psp))
run(svc,COPY,model_slide('hf_model',layout,logo,psp,None),label='model slide')
Q=svc.presentations().get(presentationId=COPY).execute()
for sl in Q['slides']:
    if sl['objectId']=='hf_model':
        ids=[el['objectId'] for el in sl.get('pageElements',[]) if not el['objectId'].startswith('hf_')]
        if ids: run(svc,COPY,[{'deleteObject':{'objectId':o}} for o in ids],label='strip placeholders')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{sys.argv[1]}/final_deck.json","w"))
FORBID=['OpenAI','ChatGPT','Claude','Grok','WAU','Adyen-only','Agent Pay','$2.5B','$1.4B','~410M','~16.8M','~$210M/month','$190M','$600M','1.2B ','595m','Open AI','Philippines','Saudi','Egypt','Malaysia','Argentina','Colombia','Poland','Thailand']
bad=[]; titles=[]
for i,sl in enumerate(Q['slides'],1):
    s=Slide(sl); ts=[text_of(el).strip() for el,tr in s.els if text_of(el).strip()]
    titles.append((i,sl['objectId'],(ts[0][:70] if ts else '(no text)')))
    for t in ts:
        for f in FORBID:
            if f in t and not (i==10 and f in ('Philippines','Saudi','Egypt','Malaysia','Argentina','Colombia','Poland','Thailand')) and not (f=='OpenAI' and 'Sora' in t):
                bad.append((i,f,t[:80])); break
print("slides:",len(Q['slides'])); print("FORBIDDEN leftovers:",bad if bad else "none")
for i,oid,t in titles: print(f"  S{i:02d} {oid[-10:]:>10s} | {t}")
