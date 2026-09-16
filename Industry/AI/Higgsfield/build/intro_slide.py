# -*- coding: utf-8 -*-
import json, sys, urllib.request
from engine import *
from extras import shape, tb, line, frame, BLUE, LILAC, BAR, WHITE, BLACK, GREY
FINAL='1LQarKMJTA7qh_sDFT_9CYwc9QP_78GtxpZlgmSb8fRQ'; OUT=sys.argv[1]; svc=service()
P=svc.presentations().get(presentationId=FINAL).execute()
def title(sl):
    ts=[(pos(el,tr)[1],pos(el,tr)[0],text_of(el).strip()) for el,tr in Slide(sl).els if text_of(el).strip()]
    ts=[t for t in ts if t[0]<130 and len(t[2])>12] or ts
    return min(ts)[2] if ts else '(no text)'
print("slides now:",len(P['slides'])); print("tail:",[(i+1,title(s)[:40]) for i,s in enumerate(P['slides']) if i>=49])
# layout: 'DEFAULT' layout of the master used by the executive summary slide
exec_sl=next(s for s in P['slides'] if s['objectId']=='g3dbb3d0b7de_0_1786')
lay={l['objectId']:l for l in P['layouts']}; master=lay[P['slides'][0]['slideProperties']['layoutObjectId']]['layoutProperties']['masterObjectId']
layout=sorted([(len(l.get('pageElements',[])),l['objectId']) for l in P['layouts'] if l['layoutProperties'].get('masterObjectId')==master])[0][1]
logo=next((el['image'].get('contentUrl') for el,tr in Slide(exec_sl).els if 'image' in el and pos(el,tr)[1]<40), None)
print("layout:",layout,"| logo:",bool(logo))
old=[s['objectId'] for s in P['slides'] if s['objectId'].startswith('hf_intro_')]
if old: run(svc,FINAL,[{'deleteObject':{'objectId':o}} for o in old],label='delete old intro')
page='hf_intro_'+str(int(__import__('time').time()))[-6:]
r=[{'createSlide':{'objectId':page,'insertionIndex':1,'slideLayoutReference':{'layoutId':layout}}}]
r+=frame(page,"WHY WE ARE HERE","Higgsfield scaled to $700M on one processor. Everything that leaks from here, Yuno can solve.",logo)
tid=r[-2]['createShape']['objectId'] if 'createShape' in r[-2] else None
for q in r:
    if 'createShape' in q and q['createShape']['elementProperties']['transform']['translateY']==46*12700: tid=q['createShape']['objectId']
    if 'createShape' in q and q['createShape']['elementProperties']['transform']['translateY']==23*12700: kid=q['createShape']['objectId']
r.append({'updateTextStyle':{'objectId':tid,'textRange':{'type':'ALL'},'style':{'fontSize':{'magnitude':26,'unit':'PT'},'foregroundColor':{'opaqueColor':{'rgbColor':BLUE}}},'fields':'fontSize,foregroundColor'}})
r.append({'updateTextStyle':{'objectId':kid,'textRange':{'type':'ALL'},'style':{'foregroundColor':{'opaqueColor':{'rgbColor':GREY}}},'fields':'foregroundColor'}})
# left column: what we see
r+=tb(page,60,126,400,16,[("WHAT WE SEE TODAY",11,True,BLUE)])
seen=[("75% of revenue outside the US, on one US-anchored processor","Stripe's published 95.6% authorization covers only the US, Europe and Australia. India, South Korea and Brazil are three of your four largest markets, with no local entity and no local acquiring."),
      ("Local methods stop where one provider's catalog stops","Cards, Apple Pay and bank payments today; PayPal is not supported per your help center. UPI, QRIS, iDEAL, Bizum and SPEI are the default way to pay in the markets that drive your traffic."),
      ("Renewals and chargebacks are being staffed right now","A Lifecycle & Retention PM (July) and a Head of Revenue Accounting (September) own dunning, refunds and chargebacks on a single retry schedule.")]
y=148
for h,b in seen:
    r+=shape(page,'ROUND_RECTANGLE',60,y,400,2,fill=BLUE,outline='none')
    r+=tb(page,60,y+7,400,20,[(h,12,True,BLACK)])
    r+=tb(page,60,y+27,400,56,[(b,9.5,False,BLACK)])
    y+=98
# arrow column
r+=tb(page,470,268,40,30,[("→",26,False,BLUE)],align='CENTER')
# right column: what Yuno solves
r+=shape(page,'RECTANGLE',520,122,400,318,fill=LILAC,outline='none')
r+=tb(page,540,130,360,16,[("WHAT YUNO SOLVES, ABOVE STRIPE",11,True,BLUE)])
sol=[("Local ways to pay in 18 markets","UPI, Pix Automático, QRIS, PayPal, iDEAL, Bizum, PayPay, SPEI and 1,000+ more through one integration.","~83K new paid subscribers"),
     ("Local acquiring and smart routing","Domestic schemes and issuer-aware routing recover the cross-border declines Stripe cannot reach.","~7K recovered per year"),
     ("Retries and redundancy on every renewal","Cross-processor retries, network tokens and account updater on subscriptions and auto-refills.","~27K renewals saved per year"),
     ("Everything around the payment","KYC / KYB for creators and workspaces, taxes and merchant-of-record coverage, and wallet distribution deals negotiated for you.","Stripe stays as your baseline")]
y=152
for h,b,k in sol:
    r+=tb(page,540,y,250,18,[(h,11,True,BLACK)])
    r+=tb(page,540,y+17,250,48,[(b,8.5,False,BLACK)])
    r+=tb(page,795,y+2,115,40,[(k,10,True,BLUE)],align='END')
    y+=70
# bottom bar
r+=shape(page,'ROUND_RECTANGLE',60,452,860,44,fill=BLUE,outline='none')
r+=tb(page,72,455,836,38,[("One integration, live in weeks, with Stripe untouched: ~$25M a year of subscription and credit revenue at conservative inputs. The rest of this deck shows the math, market by market.",12,True,WHITE)],valign='MIDDLE')
r+=tb(page,60,510,860,16,[("Source: Stripe customer story; Higgsfield help center (Aug 1 2026); Ashby job postings (Jul 28 and Sep 1 2026); SimilarWeb (Aug 2026); Yuno three-lever model",7,False,BLACK)])
run(svc,FINAL,r,label='intro slide')
Q=svc.presentations().get(presentationId=FINAL).execute()
for sl in Q['slides']:
    if sl['objectId']==page:
        ids=[el['objectId'] for el in sl.get('pageElements',[]) if not el['objectId'].startswith('hf_')]
        if ids: run(svc,FINAL,[{'deleteObject':{'objectId':o}} for o in ids],label='strip placeholders')
th=svc.presentations().pages().getThumbnail(presentationId=FINAL,pageObjectId=page,thumbnailProperties_thumbnailSize='LARGE').execute(); urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/final/thumbs/INTRO.png")
print("intro slide id:",page,"| deck now:",len(Q['slides']))
