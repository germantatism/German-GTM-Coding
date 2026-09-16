import json, sys, urllib.request
from engine import *
from extras import shape, tb, BLUE, BLACK, WHITE
from countries import COUNTRIES, ROLES, OVERRIDES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
P=svc.presentations().get(presentationId=COPY).execute(); SP={s['objectId']:Slide(s) for s in P['slides']}; SL=[Slide(s) for s in P['slides']]
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
reqs=[]
# S1 cover: remove background image with logo cubes, add Higgsfield tile
cov=SP['g3db0b697a2f_0_6033']
if any(el['objectId']=='g3db0b697a2f_0_6035' for el,tr in cov.els): reqs.append({'deleteObject':{'objectId':'g3db0b697a2f_0_6035'}})
reqs+=shape(cov.id,'ROUND_RECTANGLE',700,150,200,200,spans=[("Higgsfield",22,True,WHITE)],fill={'red':0.18,'green':0.29,'blue':0.90},outline='none',valign='MIDDLE',align='CENTER')
# S4 chart axis labels: delete scaled ones, recreate
sp=SP['g3dbb3d0b7de_0_2408']
for el,tr in sp.els:
    if el['objectId'].startswith('hf_text') and text_of(el).strip() in ('M0','M6','M12','M18','M24'): reqs.append({'deleteObject':{'objectId':el['objectId']}})
x0,y0,w,h=95,180,430,250
for m in (0,6,12,18,24):
    reqs+=tb(sp.id,x0+w*m/24-20,y0+h+3,40,12,[(f"M{m}",7.5,False,BLACK)],align='CENTER')
# S6 architecture: replace merchant logo image with text
ar=SP['g3dbb3d0b7de_0_3107']
if any(el['objectId']=='g3dbb3d0b7de_0_3117' for el,tr in ar.els): reqs.append({'deleteObject':{'objectId':'g3dbb3d0b7de_0_3117'}})
reqs+=tb(ar.id,395,98,190,36,[("Higgsfield",24,True,BLACK)],align='CENTER',valign='MIDDLE')
# S10: make priority label boxes transparent so the colored pills show
w2=SP['g3dbb3d0b7de_0_4441']
for el,tr in w2.els:
    if text_of(el).strip() in ('Very high','High','Medium') and 390<=pos(el,tr)[0]<=402:
        reqs.append({'updateShapeProperties':{'objectId':el['objectId'],'shapeProperties':{'shapeBackgroundFill':{'propertyState':'NOT_RENDERED'}},'fields':'shapeBackgroundFill.propertyState'}})
# S17 required inputs
reqs+=replace_requests(SP['g3db258e17b2_3_1130'].by_suffix('1143'),"Replaces the SimilarWeb-triangulated MAU with Higgsfield's actual demand baseline.")
# S42 UK row colors
lv=SP['g3db258e17b2_3_614']; hi=fill_of(lv.by_suffix('704')); med=fill_of(lv.by_suffix('706'))
for suf,col in (('712',med),('714',hi)):
    if col: reqs.append({'updateShapeProperties':{'objectId':lv.by_suffix(suf)['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':col},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# S46 worked example line
l2=SP['g3db258e17b2_3_809']; el=l2.by_suffix('851'); reqs+=replace_requests(el,"×  ~$20/month ARPU × 0.685 partial year  =  ~$15K/month")
reqs.append({'updateTextStyle':{'objectId':el['objectId'],'textRange':{'type':'ALL'},'style':{'fontSize':{'magnitude':12,'unit':'PT'}},'fields':'fontSize'}})
# country titles / so-what shortening
TITLES={'United Kingdom':"United Kingdom: PayPal, Open Banking and wallets lift a card market",'Germany':"Germany: PayPal + SEPA Direct Debit are 43% of online revenue; cards 14%",
 'Turkey':"Turkey: TROY is 1 in 4 card payments; local acquiring beats global cards",'Vietnam':"Vietnam: QR, bank transfers and wallets define payment expectations",
 'South Korea':"South Korea: easy-pay is live; local acquiring and Toss complete the play",'France':"France: CB routing plus PayPal / SEPA make renewals the play",
 'Mexico':"Mexico: cross-border declines and the cash-to-digital gap cap conversion",'Netherlands':"Netherlands: iDEAL is 71% of e-commerce payments and table stakes",
 'United Arab Emirates':"UAE: local AED acquiring and wallets on a high-ARPU base",'Japan':"Japan: 75M PayPay users; local methods still decide conversion",
 'Pakistan':"Pakistan: Raast, mobile wallets and local debit are the unlocks"}
SOWHAT={'United Kingdom':"The UK is Higgsfield's #4 market: a preferred-method and renewal-recovery play, not a card-access problem.",
 'Germany':"Germany's opportunity is preferred local methods plus recovery logic; a Regional GTM Director for Germany was posted in Jul 2026.",
 'South Korea':"Korea is a top-five market by users; the gap is local acquiring and renewal continuity at high ARPU, not wallet coverage.",
 'France':"France is a strong card market; the upside is CB routing, PayPal / SEPA and renewal recovery. A GTM Director for France was posted Jul 2026.",
 'Canada':"Canada is a preferred-method market (credit 33%, debit 30%, EFT 14% of transactions); local CAD processing, Interac and PayPal are the play.",
 'Pakistan':"Pakistan's path is wallets and instant rails, not cards; a subscriber reported a card re-verification lockout in Sep 2026."}
for k,d in enumerate(COUNTRIES):
    s=SL[22+k]; roles=dict(ROLES); roles.update(OVERRIDES.get(21+k,{}))
    for role,table in (('title',TITLES),('sowhat',SOWHAT)):
        if d['c'] in table:
            x,y=roles[role]; m=s.near(x,y,tol=5)
            if len(m)==1: reqs+=replace_requests(m[0],table[d['c']])
print("requests:",len(reqs)); run(svc,COPY,reqs,label='fixes5')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w"))
for n in [1,4,6,9,10,17,27,31,33,42,46]:
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=Q['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/thumbs/S{n:02d}.png")
print("thumbs refreshed")
