# -*- coding: utf-8 -*-
"""Bubble chart remap (S12) and the two new slides (industry context, what Higgsfield gets)."""
from engine import replace_requests, text_of, pos, Slide
EMU=12700
BLUE={'red':0.24,'green':0.31,'blue':0.88}; LILAC={'red':0.95,'green':0.96,'blue':0.99}; BAR={'red':0.91,'green':0.92,'blue':0.96}
WHITE={'red':1,'green':1,'blue':1}; BLACK={'red':0,'green':0,'blue':0}; GREY={'red':0.95,'green':0.95,'blue':0.98}
FONT='Titillium Web'

BUBBLES=[  # (new label, ellipse suffix, center x, center y)
 ("India","12931",470,210),("United Kingdom","12932",190,212),("South Korea","12933",325,208),("Germany","12940",385,235),
 ("Brazil","12959",525,240),("Indonesia","12960",490,300),("Spain","12935",320,298),("Italy","12938",375,322),
 ("France","12941",168,298),("Canada","12956",222,325),("Turkey","12957",455,372),("Vietnam","12950",500,398),
 ("Netherlands","12951",305,380),("UAE","12952",350,402),("China","12953",540,372),("Japan","12954",395,380),
 ("Mexico","12955",475,420),("Pakistan","12934",530,425)]
BUBBLE_DELETE=["12943","12944"]

def bubble_requests(s12, sim=None):
    reqs=[]
    for label,suf,cx,cy in BUBBLES:
        el=s12.by_suffix(suf); tr=el['transform']; sz=el['size']
        w=sz['width']['magnitude']*tr.get('scaleX',1); h=sz['height']['magnitude']*tr.get('scaleY',1)
        reqs+=replace_requests(el,label)
        if sim is not None: sim[el['objectId']]=label
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE',
            'transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,
                         'translateX':cx*EMU-w/2,'translateY':cy*EMU-h/2,'unit':'EMU'}}})
    for suf in BUBBLE_DELETE:
        el=s12.by_suffix(suf); reqs.append({'deleteObject':{'objectId':el['objectId']}})
        if sim is not None: sim[el['objectId']]=''
    return reqs

# ---------- shape helpers ----------
import time
_n=[0]; _run=str(int(time.time()))[-6:]
def _id(prefix):
    _n[0]+=1; return f"hf_{prefix}_{_run}_{_n[0]}"
def shape(page,kind,x,y,w,h,spans=None,fill=None,outline=None,valign=None,align=None,radius=None):
    """spans: list of (text,size,bold,color) joined by newlines. returns requests"""
    oid=_id(kind.lower()[:4]); r=[{'createShape':{'objectId':oid,'shapeType':kind,'elementProperties':{'pageObjectId':page,
        'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':h*EMU,'unit':'EMU'}},
        'transform':{'scaleX':1,'scaleY':1,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'}}}}]
    sp={}
    if fill: sp['shapeBackgroundFill']={'solidFill':{'color':{'rgbColor':fill},'alpha':1}}
    if outline=='none': sp['outline']={'propertyState':'NOT_RENDERED'}
    elif outline: sp['outline']={'outlineFill':{'solidFill':{'color':{'rgbColor':outline},'alpha':1}},'weight':{'magnitude':0.75*EMU,'unit':'EMU'},'dashStyle':'SOLID'}
    if valign: sp['contentAlignment']=valign
    if sp: r.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':sp,'fields':','.join(sp.keys())}})
    if spans:
        text='\n'.join(t for t,_,_,_ in spans)
        r.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':text}})
        start=0
        for t,size,bold,color in spans:
            end=start+len(t)
            if end>start:
                r.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},
                    'style':{'fontFamily':FONT,'fontSize':{'magnitude':size,'unit':'PT'},'bold':bool(bold),'foregroundColor':{'opaqueColor':{'rgbColor':color or BLACK}}},
                    'fields':'fontFamily,fontSize,bold,foregroundColor'}})
            start=end+1
        if align:
            r.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':{'alignment':align},'fields':'alignment'}})
        r.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'autofit':{'autofitType':'NONE'}},'fields':'autofit.autofitType'}})
    return r
def tb(page,x,y,w,h,spans,align=None,valign='TOP'):
    return shape(page,'TEXT_BOX',x,y,w,h,spans,outline='none',valign=valign,align=align)
def image(page,url,x,y,w,h):
    return [{'createImage':{'objectId':_id('img'),'url':url,'elementProperties':{'pageObjectId':page,
        'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':h*EMU,'unit':'EMU'}},
        'transform':{'scaleX':1,'scaleY':1,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'}}}}]
def line(page,x1,y1,x2,y2,color=None):
    oid=_id('line'); w=max(x2-x1,0.5); h=max(y2-y1,0.5)
    r=[{'createLine':{'objectId':oid,'lineCategory':'STRAIGHT','elementProperties':{'pageObjectId':page,
        'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':h*EMU,'unit':'EMU'}},
        'transform':{'scaleX':1,'scaleY':1,'translateX':x1*EMU,'translateY':y1*EMU,'unit':'EMU'}}}}]
    r.append({'updateLineProperties':{'objectId':oid,'lineProperties':{'lineFill':{'solidFill':{'color':{'rgbColor':color or BAR},'alpha':1}},'weight':{'magnitude':0.75*EMU,'unit':'EMU'}},'fields':'lineFill,weight'}})
    return r
def frame(page,kicker,title,logo_url):
    r=shape(page,'RECTANGLE',36,1,2,540,fill=BAR,outline='none')+shape(page,'ROUND_RECTANGLE',36,57,2,14,fill=BLUE,outline='none')
    r+=tb(page,60,23,338,15,[(kicker,12,False,BLACK)])+tb(page,60,46,860,39,[(title,26,False,BLACK)])
    if logo_url: r+=image(page,logo_url,888,24,47,13)
    return r

def industry_slide(page,layout,logo_url):
    r=[{'createSlide':{'objectId':page,'insertionIndex':1,'slideLayoutReference':{'layoutId':layout}}}]
    r+=frame(page,"INDUSTRY CONTEXT","AI video at a glance: a category that scaled 10x in a year, and Higgsfield leads it",logo_url)
    # right box
    r+=shape(page,'RECTANGLE',662,108,257,253,fill=LILAC,outline='none')
    r+=tb(page,684,118,217,50,[("#1",42,True,BLUE)])
    r+=tb(page,684,170,217,34,[("THE CATEGORY, CONCENTRATED IN ONE COMPANY",12,True,BLUE)])
    r+=tb(page,684,214,217,140,[("30M+ users. $700M annualized revenue (Aug 2026), the highest disclosed in the category. Valued at $5.4B, level with Runway ($5.3B) and Luma ($4B+). 75% of revenue outside the US. Where this category monetizes internationally is decided at Higgsfield's checkout.",11,False,BLACK)])
    rows=[("$847M TAM","AI video generator market 2026; ~$3.35B by 2034, 18.8% CAGR (Fortune Business Insights, Aug 2026)",
           "Analyst sizing lags the category: Higgsfield alone books ~$700M against an $847M 2026 estimate (The Business Research Company puts 2026 at $1.04B). The category is being re-sized in real time, and most of that revenue now comes from businesses buying production capacity."),
          ("$700M","Annualized revenue, Aug 2026, from ~$10M in April 2025",
           "Disclosed run-rates put Higgsfield first: Kling AI (Kuaishou) ~$500M ARR in March 2026; Runway $200M ARR in September 2026; MiniMax (Hailuo) $79.0M revenue in 2025. On traffic, higgsfield.ai ranks #1,228 globally vs kling.ai #4,223 and runwayml.com #7,435 (SimilarWeb, Aug 2026)."),
          ("30M+","Users across 238 countries and territories; 390 of the Fortune 500 (Aug 2026)",
           "Usage is global by default and monetization is card-led by default. Stripe's case study puts 75% of Higgsfield's revenue outside the US, while the 95.6% authorization rate it quotes covers only the US, Europe and Australia.")]
    y=108
    for num,cap,txt in rows:
        r+=tb(page,60,y,250,34,[(num,28,True,BLACK)])
        r+=tb(page,60,y+36,250,38,[(cap,9,True,BLUE)])
        r+=tb(page,322,y+2,322,80,[(txt,10,False,BLACK)])
        if y<270: r+=line(page,60,y+84,640,y+84)
        y+=88
    r+=tb(page,60,372,400,16,[("WHAT DEFINES THE CATEGORY IN 2026",9.5,True,BLUE)])
    cards=[("The aggregation era","Higgsfield sells one workflow over 30+ models: Kling 3.0, Seedance 2.0, Wan 2.7, Sora 2, Veo 3.1, Hailuo 2.3, plus its own Soul model. Switching cost is low; the winner is whoever removes friction fastest."),
           ("The enterprise turn","Businesses were under a quarter of revenue in January 2026 and the majority by August (FT via ContentGrip). Consumer and prosumer is now the ~30% that has to be monetized efficiently."),
           ("Big tech retreated from the standalone app","OpenAI discontinued the Sora app (Mar 2026; Sora 2 stays available through partners such as Higgsfield). Google ships Veo inside Gemini and Flow; Meta discloses no Vibes numbers.")]
    x=60
    for t,b in cards:
        r+=shape(page,'ROUND_RECTANGLE',x,390,274,72,fill=BLUE,outline='none')
        r+=tb(page,x+10,394,254,66,[(t,10.5,True,WHITE),(b,8,False,WHITE)])
        x+=293
    r+=shape(page,'ROUND_RECTANGLE',60,470,860,34,fill=LILAC,outline='none')
    r+=tb(page,68,472,844,30,[("When 75% of revenue sits outside the home market and the checkout is card-led, payments infrastructure becomes the growth lever. Every point of conversion, approval and renewal recovery lands directly on revenue.",10.5,True,BLUE)],valign='MIDDLE')
    r+=tb(page,60,510,860,22,[("Sources: Fortune Business Insights (Aug 31 2026); The Business Research Company (Feb 2026); PR Newswire, Higgsfield Series B (Aug 17 2026); Stripe customer story; Kuaishou Q1 and Q2 2026 results; PYMNTS (Sep 8 2026); SimilarWeb (Aug 2026); ContentGrip citing FT (Aug 18 2026); TechCrunch (Mar 24 2026); Google (Oct 15 2025); higgsfield.ai (Sep 16 2026).",7,False,BLACK)])
    return r

def model_slide(page,layout,logo_url,psp_logos,hf_logo=None):
    r=[{'createSlide':{'objectId':page,'insertionIndex':6,'slideLayoutReference':{'layoutId':layout}}}]
    r+=frame(page,"HIGGSFIELD PROPOSED MODEL","From a single processor to one scalable Global Financial Infrastructure",logo_url)
    # merchant box
    if hf_logo: r+=image(page,hf_logo,285,108,40,40)+tb(page,330,118,120,24,[("Higgsfield",14,True,BLACK)])
    else: r+=shape(page,'ROUND_RECTANGLE',255,112,150,32,spans=[("Higgsfield",14,True,BLACK)],fill=WHITE,outline=BLUE,valign='MIDDLE',align='CENTER')
    surfaces=[("Web Studio","subscriptions, credit packs, auto-refill"),("Team / Scale / Enterprise","per-seat, invoice or PO"),("Higgsfield Earn","creator payouts, 10,000+ creators")]
    x=60
    for t,b in surfaces:
        r+=shape(page,'ROUND_RECTANGLE',x,168,160,34,fill=WHITE,outline=BLUE,outline_note=None) if False else shape(page,'ROUND_RECTANGLE',x,168,160,34,fill=WHITE,outline=BLUE)
        r+=tb(page,x+6,169,148,32,[(t,9,True,BLACK),(b,7.5,False,BLACK)],valign='MIDDLE')
        r+=line(page,x+80,144,x+80,168,color=BLUE)
        x+=175
    r+=line(page,140,144,490,144,color=BLUE)
    r+=tb(page,60,214,150,22,[("One integration owned by Higgsfield",8,False,BLACK)],valign='MIDDLE')
    r+=shape(page,'ROUND_RECTANGLE',255,214,110,22,spans=[("API",10,True,WHITE)],fill=BLUE,outline='none',valign='MIDDLE',align='CENTER')
    r+=line(page,310,202,310,214,color=BLUE)+line(page,310,236,310,250,color=BLUE)
    r+=shape(page,'ROUND_RECTANGLE',60,250,510,78,fill=GREY,outline='none')
    r+=tb(page,70,252,80,16,[("yuno",11,True,BLUE)])
    chips=["Smart Routing","Risk Conditions","Tokenization","Checkout Builder","Fraud & Risk (Nova)","KYC / KYB","Payouts","Insights","Connectors","Reconciliation*"]
    for k,c in enumerate(chips):
        cx=70+(k%5)*100; cy=272 if k<5 else 298
        r+=shape(page,'ROUND_RECTANGLE',cx,cy,94,19,spans=[(c,7.5,False,BLACK)],fill=WHITE,outline='none',valign='MIDDLE',align='CENTER')
    r+=line(page,310,328,310,340,color=BLUE)
    r+=shape(page,'ROUND_RECTANGLE',60,340,510,50,fill=GREY,outline='none')
    lx=80
    for url,w,h in psp_logos:
        r+=image(page,url,lx,352,w,h); lx+=w+40
    r+=tb(page,lx+10,356,520-lx,20,[("+1,000 Global Payment Partners & Methods",9,True,BLACK)],valign='MIDDLE')
    r+=tb(page,60,404,80,30,[("Expected\nImpact",9,True,BLACK)])
    r+=tb(page,150,398,90,34,[("+7%",22,True,BLUE)])+tb(page,240,404,110,30,[("Avg. approval-rate uplift (published)",8.5,False,BLACK)])
    r+=tb(page,360,398,90,34,[("30%",22,True,BLUE)])+tb(page,450,404,120,30,[("Recovered revenue on failed payments (published)",8.5,False,BLACK)])
    cards=[("Smart Routing Engine","Route every subscription, credit pack and auto-refill across Stripe and local acquirers by BIN, issuer and market. Stripe keeps the traffic it already wins."),
           ("Failover + Recovery","Cross-processor cascade and retry logic recovers renewals a single retry schedule gives up on: the dunning scope of the Lifecycle & Retention PM role."),
           ("1,000+ Local Methods","UPI, Pix Automático, QRIS, PayPal, iDEAL, Bizum, PayPay, SPEI and OXXO through one API, beyond card-only web checkout."),
           ("KYC / KYB, orchestrated","Onboard creators for Higgsfield Earn payouts (KYC already mandatory per the Trust page) and verify Team / Scale / Enterprise workspaces (KYB), with provider choice per market."),
           ("Taxes and merchant-of-record coverage","Sell locally without opening 18 entities: local tax handling, invoicing and settlement through Yuno's MoR and PSP-of-record partners per market."),
           ("Distribution deals","Yuno's BD team negotiates wallet co-marketing, priority placement, badge inclusion and promotional rates (UPI apps, Mercado Pago, GCash, Kaspi) on Higgsfield's behalf.")]
    y=108
    for t,b in cards:
        r+=shape(page,'ROUND_RECTANGLE',600,y,320,60,fill=WHITE,outline=BLUE)
        r+=tb(page,608,y+3,304,54,[(t,10,True,BLACK),(b,7.5,False,BLACK)])
        y+=66
    r+=tb(page,60,510,860,20,[("*Reconciliation: confirm general-availability status before external use. Impact figures are Yuno published benchmarks.",7,False,BLACK)])
    return r
