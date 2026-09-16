import json, sys
from engine import *
from extras import tb, BLACK
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
O=json.load(open(f"{OUT}/copy_deck.json")); P=svc.presentations().get(presentationId=COPY).execute()
SO={s['objectId']:Slide(s) for s in O['slides']}; SP={s['objectId']:Slide(s) for s in P['slides']}
def desc(el,tr):
    sp=el.get('shape',{}).get('shapeProperties',{}); f=sp.get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}); o=sp.get('outline',{})
    oc=o.get('outlineFill',{}).get('solidFill',{}).get('color',{}); w=el['size']['width']['magnitude']*tr.get('scaleX',1)/12700; h=el['size']['height']['magnitude']*tr.get('scaleY',1)/12700
    kind='image' if 'image' in el else ('line' if 'line' in el else el.get('shape',{}).get('shapeType'))
    return f"{el['objectId'][-6:]} {kind:16s} x={pos(el,tr)[0]:3d} y={pos(el,tr)[1]:3d} w={w:5.1f} h={h:4.1f} fill={f.get('rgbColor',f.get('themeColor','-'))} outline={oc.get('rgbColor',oc.get('themeColor','-'))} ow={o.get('weight',{}).get('magnitude','-')} | {text_of(el).strip()[:14]}"
print("== S7 (orig) row 1 band y 160..176, x 430..640 ==")
for el,tr in SO['g3db0b697a2f_0_11825'].els:
    x,y=pos(el,tr)
    if 430<=x<=640 and 158<=y<=178: print("  ",desc(el,tr))
print("== S8 (orig) row 1 (y 160..176) and row 12 (y 330..346), x 380..470 ==")
for el,tr in SO['g3dbb3d0b7de_0_4441'].els:
    x,y=pos(el,tr)
    if 380<=x<=470 and (160<=y<=176 or 330<=y<=346): print("  ",desc(el,tr))
print("== S1 images ==")
for el,tr in SO['g3db0b697a2f_0_6033'].els:
    if 'image' in el and el['size']['width']['magnitude']/12700>20: print("  ",desc(el,tr))
print("== flags on country slides (images y<70 x<130) ==")
for sl in P['slides'][22:40]:
    s=SP[sl['objectId']]
    for el,tr in s.els:
        x,y=pos(el,tr)
        if 'image' in el and y<70 and x<130: print("  ",sl['objectId'][-8:],desc(el,tr))
# ---------- independent fixes ----------
reqs=[]
# S04 chart x labels widen + paragraph
sp=SP['g3dbb3d0b7de_0_2408']
for el,tr in sp.els:
    t=text_of(el).strip()
    if el['objectId'].startswith('hf_text') and t in ('M0','M6','M12','M18','M24'):
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':1.6,'scaleY':1,'shearX':0,'shearY':0,'translateX':tr['translateX']-8*12700,'translateY':tr['translateY'],'unit':'EMU'}}})
el=sp.by_suffix('2414'); reqs+=replace_requests(el,"~6M Higgsfield MAU in 18 addressable markets (~12M globally). No AI-video competitor has localized checkout yet: Kling sells globally in USD via Stripe.")
reqs.append({'updateTextStyle':{'objectId':el['objectId'],'textRange':{'type':'ALL'},'style':{'fontSize':{'magnitude':12,'unit':'PT'}},'fields':'fontSize'}})
# S20 BD: title, regions, texts
bd=SP['g3dbb3d0b7de_0_6732']
reqs+=replace_requests(bd.by_suffix('6737'),"A 60-day Yuno BD sprint secures wallet and distribution commitments across four regions")
reqs+=replace_requests(bd.by_suffix('6739'),"Integration alone isn't enough. Many wallets only activate marketing, co-branding and full market support when the merchant has a direct relationship. Yuno's BD team builds those relationships on Higgsfield's behalf, PayPal, iDEAL, Bizum and Satispay enablement in Europe included.")
reqs+=replace_requests(bd.by_suffix('6785'),"LATIN AMERICA")
reqs+=replace_requests(bd.by_suffix('6787'),"SOUTH & SE ASIA")
reqs+=replace_requests(bd.by_suffix('6786'),"EAST ASIA")
reqs+=replace_requests(bd.by_suffix('6788'),"MENA / AFRICA")
reqs+=replace_requests(bd.by_suffix('6741'),"Pix Automático recurring commitment + Mercado Pago co-marketing in Brazil and Mexico; SPEI / OXXO activation")
reqs+=replace_requests(bd.by_suffix('6742'),"UPI AutoPay mandates + Paytm / PhonePe placement; QRIS + GoPay / DANA in Indonesia; MoMo in Vietnam; JazzCash / Easypaisa in Pakistan")
reqs+=replace_requests(bd.by_suffix('6743'),"Korea easy-pay completion (Toss, Samsung Pay) on top of Kakao / Naver / PayCo; Japan PayPay / Konbini; Alipay for Chinese users")
reqs+=replace_requests(bd.by_suffix('6744'),"UAE local acquirer contracts + Tabby / Tamara; mada / STC Pay (Saudi) and Fawry / InstaPay (Egypt) queued as wave-2 markets")
# S1 cover: remove the partner-logo cube image
reqs.append({'deleteObject':{'objectId':'g3db0b697a2f_0_6081'}})
# flags: replace on the 17 reassigned country slides
ISO=['in','id','gb','de','tr','br','es','vn','kr','it','fr','ca','mx','nl','ae','jp','pk','cn']
for sl,iso in zip(P['slides'][22:40],ISO):
    s=SP[sl['objectId']]
    for el,tr in s.els:
        x,y=pos(el,tr)
        if 'image' in el and y<70 and x<130:
            if iso=='in': continue
            w=el['size']['width']['magnitude']*tr.get('scaleX',1); h=el['size']['height']['magnitude']*tr.get('scaleY',1)
            reqs.append({'deleteObject':{'objectId':el['objectId']}})
            reqs.append({'createImage':{'objectId':f"hf_flag_{iso}",'url':f"https://flagcdn.com/w160/{iso}.png",'elementProperties':{'pageObjectId':sl['objectId'],'size':{'width':{'magnitude':w,'unit':'EMU'},'height':{'magnitude':h,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}}})
print("independent fix requests:",len(reqs))
try: run(svc,COPY,reqs,label='fixes3')
except Exception as e:
    print("batch failed:",str(e)[:200]); 
    # retry without flag images (fallback: delete only)
    reqs2=[r for r in reqs if 'createImage' not in r]; run(svc,COPY,reqs2,label='fixes3 (no flag images)')
