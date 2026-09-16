import json, sys, urllib.request
from engine import *
from content import grid_rows, TOP20
from countries import COUNTRIES, ROLES, OVERRIDES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
P=svc.presentations().get(presentationId=COPY).execute(); SP={s['objectId']:Slide(s) for s in P['slides']}; SL=[Slide(s) for s in P['slides']]
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
WHITE={'red':1,'green':1,'blue':1}; BLACK={'red':0,'green':0,'blue':0}
reqs=[]
# S9 archetype label colors
t=SP['g3db0b697a2f_0_11825']; rows=[r for r in grid_rows(t,30,680,160,470) if len(r)>=6]
for r,d in zip(rows,TOP20):
    el=r[5][2]; col=WHITE if d[5] in ('Full-stack','APM-led') else BLACK
    reqs.append({'updateTextStyle':{'objectId':el['objectId'],'textRange':{'type':'ALL'},'style':{'foregroundColor':{'opaqueColor':{'rgbColor':col}}},'fields':'foregroundColor'}})
# S42 UK cells: transparent label boxes + recolor underlying cells
lv=SP['g3db258e17b2_3_614']
def under(x,y):
    return [el for el,tr in lv.els if not text_of(el).strip() and 'shape' in el and abs(pos(el,tr)[0]-x)<=6 and abs(pos(el,tr)[1]-y)<=4]
green=[fill_of(e) for e in under(199,448) if fill_of(e)]; orange=[fill_of(e) for e in under(386,448) if fill_of(e)]
print("green:",green[:1],"orange:",orange[:1])
for suf,x,col in (('712',199,orange),('714',386,green)):
    el=lv.by_suffix(suf); reqs.append({'updateShapeProperties':{'objectId':el['objectId'],'shapeProperties':{'shapeBackgroundFill':{'propertyState':'NOT_RENDERED'}},'fields':'shapeBackgroundFill.propertyState'}})
    for u in under(x,459):
        if col: reqs.append({'updateShapeProperties':{'objectId':u['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':col[0]},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# country captions
LABEL={'Turkey':"TROY cards (BKM, end 2025)",'South Korea':"Easy-pay usage per day (BoK, 2025)",'France':"Cartes Bancaires cards (2024)",'United Kingdom':"Open Banking payments 2025 (+57%)",
 'Germany':"PayPal share of online retail (2025)",'Canada':"Interac e-Transfers in 2024 ($554B)",'United Arab Emirates':"UAE e-commerce on cards; wallets 24%",'Pakistan':"JazzCash registered users (Mar 2026)",'China':"Weixin + WeChat MAU (Tencent, 2025)"}
SUB={'Turkey':"25.3% of card value (+7pp YoY)",'South Korea':"Non-bank Pay apps: 54.9% of easy-pay",'Indonesia':"44.9M merchants; wallets 35% of e-com",'United Kingdom':"16.5M user connections (OBL, 2026)",
 'Germany':"SEPA DD 14.4%; all cards 13.7% (EHI)",'Brazil':"Cards 40%; 170M+ Brazilians use Pix",'Spain':"1.24B ops; 105.6M online buys (+82%)",'Vietnam':"QR payments +106.7% YoY (SBV, 2024)",
 'Italy':"450K+ merchants; wallets 35% of e-com",'Mexico':"Banxico: SPEI tops cards by end-2026",'Netherlands':"71% of Dutch e-commerce payments",'United Arab Emirates':"M-commerce 60%+; cross-border 37%",
 'Japan':"8.88B PayPay txns 2025; cashless 58%",'Pakistan':"Easypaisa 59M+; 92% of retail digital",'China':"E-wallets 65% of Chinese e-commerce"}
for k,d in enumerate(COUNTRIES):
    s=SL[22+k]; roles=dict(ROLES); roles.update(OVERRIDES.get(21+k,{}))
    def near(role):
        x,y=roles[role]; m=s.near(x,y,tol=5); return m[0] if len(m)==1 else None
    if d['c'] in LABEL and near('stat_label'): reqs+=replace_requests(near('stat_label'),LABEL[d['c']])
    if d['c'] in SUB and near('stat_sub'): reqs+=replace_requests(near('stat_sub'),SUB[d['c']])
    el=near('tot_sub')
    if el: reqs+=replace_requests(el,d['tot'][1].replace('including auth + renewals · ','incl. auth + renewals · ').replace(' total',''))
print("requests:",len(reqs)); run(svc,COPY,reqs,label='fixes6')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w"))
for n in [9,26,27,31,33,37,40,42,48,49]:
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=Q['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/thumbs/S{n:02d}.png")
print("thumbs refreshed")
