import json, sys
from engine import *
from extras import industry_slide, model_slide
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
first_master=P['masters'][0]['objectId']
cands=[(len(l.get('pageElements',[])),l['objectId'],l.get('layoutProperties',{}).get('displayName')) for l in P['layouts'] if l.get('layoutProperties',{}).get('masterObjectId')==first_master]
cands.sort(); print("layouts in first master:",cands[:6]); layout=cands[0][1]
def img_url(slide_idx,suffix):
    for el,tr in Slide(P['slides'][slide_idx]).els:
        if el['objectId'].endswith('_'+suffix) and 'image' in el: return el['image'].get('contentUrl')
logo=img_url(1,'1791'); psp=[(img_url(4,s),w,h) for s,w,h in [('3135',37,14),('3138',40,13),('3141',43,13)]]
print("logo url ok:",bool(logo),"| psp urls ok:",all(u for u,_,_ in psp))
def strip_placeholders(page):
    Q=svc.presentations().get(presentationId=COPY).execute()
    for sl in Q['slides']:
        if sl['objectId']==page:
            ids=[el['objectId'] for el in sl.get('pageElements',[]) if not el['objectId'].startswith('hf_')]
            if ids: run(svc,COPY,[{'deleteObject':{'objectId':o}} for o in ids],label=f'strip placeholders {page}')
            return
run(svc,COPY,industry_slide('hf_industry',layout,logo),label='industry slide'); strip_placeholders('hf_industry')
hf_logo=None
try:
    svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'createImage':{'objectId':'hf_logo_probe','url':'https://logo.clearbit.com/higgsfield.ai','elementProperties':{'pageObjectId':'hf_industry','size':{'width':{'magnitude':10*12700,'unit':'EMU'},'height':{'magnitude':10*12700,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'translateX':0,'translateY':0,'unit':'EMU'}}}}]}).execute()
    svc.presentations().batchUpdate(presentationId=COPY,body={'requests':[{'deleteObject':{'objectId':'hf_logo_probe'}}]}).execute()
    hf_logo='https://logo.clearbit.com/higgsfield.ai'; print("Higgsfield logo: clearbit OK")
except Exception as e: print("Higgsfield logo unavailable, using text box:",str(e)[:90])
run(svc,COPY,model_slide('hf_model',layout,logo,psp,hf_logo),label='model slide'); strip_placeholders('hf_model')
# ===== final scan =====
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{sys.argv[1]}/final_deck.json","w"))
FORBID=['OpenAI','ChatGPT','Claude','Grok','WAU','Adyen-only','Agent Pay','$2.5B','$1.4B','~410M','~16.8M','~$210M/month','$190M','$600M','1.2B ','595m','Open AI','Philippines','Saudi','Egypt','Malaysia','Argentina','Colombia','Poland','Thailand']
bad=[]; titles=[]
for i,sl in enumerate(Q['slides'],1):
    s=Slide(sl); ts=[text_of(el).strip() for el,tr in s.els if text_of(el).strip()]
    titles.append((i,(ts[0][:60] if ts else '(no text)')))
    for t in ts:
        for f in FORBID:
            if f in t and not (i==10 and f in ('Philippines','Saudi','Egypt','Malaysia','Argentina','Colombia','Poland','Thailand')) and not (i==4 and f=='OpenAI' and 'Sora' in t):
                bad.append((i,f,t[:80])); break
print("slides:",len(Q['slides'])); print("FORBIDDEN leftovers:",bad if bad else "none")
for i,t in titles: print(f"  S{i:02d} {t}")
