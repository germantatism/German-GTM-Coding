# -*- coding: utf-8 -*-
"""QA agent findings pass. Extend EXTRA list with (slide_idx, suffix, new_text) from agents 1 and 3."""
import json, sys, urllib.request
from engine import *
from countries import COUNTRIES, ROLES, OVERRIDES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
P=svc.presentations().get(presentationId=COPY).execute(); SL=[Slide(s) for s in P['slides']]; SP={s.id:s for s in SL}
NAVY={'red':0.118,'green':0.153,'blue':0.380}
def run_style(el):
    for te in el['shape']['text'].get('textElements',[]):
        if 'textRun' in te and te['textRun'].get('content','').strip(): return te['textRun'].get('style',{})
    return {}
def copy_style(src,dst,fields=('foregroundColor','fontSize','bold','italic')):
    st={k:v for k,v in run_style(src).items() if k in fields}
    return [{'updateTextStyle':{'objectId':dst['objectId'],'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}}] if st else []
reqs=[]
# --- agent 2 items ---
reqs.append({'updateTextStyle':{'objectId':'g3db258e17b2_3_1179','textRange':{'type':'ALL'},'style':{'foregroundColor':{'opaqueColor':{'rgbColor':NAVY}}},'fields':'foregroundColor'}})
reqs+=replace_requests(SP['g3db258e17b2_3_956'].by_suffix('974'),"Sequence top markets by combined opportunity vs implementation effort. Identify 2 to 3 pilot countries and their priority methods.")
reqs+=replace_requests(SP['g3dbb3d0b7de_0_6732'].by_suffix('6742'),"UPI AutoPay mandates + Paytm / PhonePe placement; QRIS + GoPay / DANA in Indonesia; MoMo in Vietnam; JazzCash in Pakistan")
reqs+=replace_requests(SP['g3db258e17b2_3_991'].by_suffix('1025'),"Recurring-native methods (UPI AutoPay, Pix Automático, SEPA DD) differ from acquisition-only methods (Konbini, OXXO, cash vouchers)")
# country slides: L2 colors = L1 colors; tile-4 caption wording; flags outline; India band restyle
ref=SL[23]  # Indonesia (standard template)
def near(s,roles,role):
    x,y=roles[role]; m=s.near(x,y,tol=5); return m[0] if len(m)==1 else None
for k,d in enumerate(COUNTRIES):
    s=SL[22+k]; roles=dict(ROLES); roles.update(OVERRIDES.get(21+k,{}))
    for a,b in (('L1h','L2h'),('L1u','L2u'),('L1p','L2p')):
        ea,eb=near(s,roles,a),near(s,roles,b)
        if ea and eb: reqs+=copy_style(ea,eb,('foregroundColor',))
    el=near(s,roles,'tot_sub')
    if el:
        usd=d['tot'][1].split('· ')[1].replace(' total','').replace('~$0.66M','~$0.7M').replace('~$0.62M','~$0.6M').replace('~$0.26M','~$0.3M').replace('~$1.05M','~$1.1M')
        reqs+=replace_requests(el,f"new + recovered subs · {usd} incl. renewals")
    # snap blue-band captions to the reference y
    if k!=1:
        for role in ('stat_label','mau_label','l1_label','tot_label','stat_sub','mau_sub','l1_sub','tot_sub'):
            e=near(s,roles,role)
            if e and k!=0:
                tr=next(t for x,t in s.els if x['objectId']==e['objectId'])
                reqs.append({'updatePageElementTransform':{'objectId':e['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':ROLES[role][1]*12700,'unit':'EMU'}}})
    for el,tr in s.els:
        if 'image' in el and pos(el,tr)[1]<70 and pos(el,tr)[0]<130:
            reqs.append({'updateImageProperties':{'objectId':el['objectId'],'imageProperties':{'outline':{'outlineFill':{'solidFill':{'color':{'rgbColor':{'red':0.75,'green':0.77,'blue':0.85}},'alpha':1}},'weight':{'magnitude':0.75*12700,'unit':'EMU'},'dashStyle':'SOLID'}},'fields':'outline'}})
# India band: copy caption/sub styles from Indonesia and align y
ind=SL[22]; rI=dict(ROLES); rI.update(OVERRIDES[21]); rR=dict(ROLES)
for role in ('stat_label','mau_label','l1_label','tot_label','stat_sub','mau_sub','l1_sub','tot_sub'):
    ei,er=near(ind,rI,role),near(ref,rR,role)
    if ei and er:
        reqs+=copy_style(er,ei)
        tr=next(t for e,t in ind.els if e['objectId']==ei['objectId']); ty=rR[role][1]*12700
        reqs.append({'updatePageElementTransform':{'objectId':ei['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':ty,'unit':'EMU'}}})
# --- agent 3 items ---
rk=SP['g3db258e17b2_3_268']
reqs.append({'deleteObject':{'objectId':rk.by_suffix('613')['objectId']}})
tot=sorted([(pos(el,tr)[0],el) for el,tr in rk.els if text_of(el).strip() and 455<=pos(el,tr)[1]<=500 and pos(el,tr)[0]<700],key=lambda c:c[0])
vals=["PORTFOLIO TOTAL","~1.7%","~3.1% (+1.4pp)","~83K","~$1.80M/mo"]
for (x,el),v in zip(tot,vals): reqs+=replace_requests(el,v)
print("S41 total cells:",[(x,text_of(el).strip()[:14]) for x,el in tot])
for el,tr in rk.els:
    if not text_of(el).strip() and 'shape' in el and 470<=pos(el,tr)[0]<=485 and 150<=pos(el,tr)[1]<=470:
        reqs.append({'updateShapeProperties':{'objectId':el['objectId'],'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':NAVY},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# divider stat lines on S43 and S45 (copy geometry/style from S47's line)
s47=SP['g3db258e17b2_3_860']; ref=s47.by_suffix('866'); rtr=next(t for e,t in s47.els if e['objectId']==ref['objectId']); rst=run_style(ref)
for sid,txt in (('g3db258e17b2_3_735',"~$1.8M/mo · ~$21M annualized · ~83K incremental paid subscribers"),('g3db258e17b2_3_803',"~$0.11M/mo · ~$1.3M annualized · ~7K recovered subscribers")):
    oid='hf_divstat_'+sid[-4:]
    reqs.append({'createShape':{'objectId':oid,'shapeType':'TEXT_BOX','elementProperties':{'pageObjectId':sid,'size':ref['size'],'transform':{'scaleX':rtr.get('scaleX',1),'scaleY':rtr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':rtr['translateX'],'translateY':rtr['translateY'],'unit':'EMU'}}}})
    reqs.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':txt}})
    st={k:v for k,v in rst.items() if k in ('fontSize','bold','foregroundColor','fontFamily','italic')}
    if st: reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
reqs+=replace_requests(SP['g3db258e17b2_3_741'].by_suffix('757'),"Estimated monthly active Higgsfield users per priority market.")
reqs+=replace_requests(SP['g3db258e17b2_3_809'].by_suffix('810'),"Lever 2 sizing: how local processing converts failed card attempts into paid subscribers")
# UAE label
s37=SL[36]; r37=dict(ROLES); e=near(s37,r37,'stat_label')
if e: reqs+=replace_requests(e,"Cards 52%; wallets 24% of e-com")
# --- EXTRA items from agents 1 and 3: (slide_objectId, suffix, new_text) ---
EXTRA=json.load(open(f"{OUT}/build/extra.json")) if __import__('os').path.exists(f"{OUT}/build/extra.json") else []
for sid,suf,new in EXTRA: reqs+=replace_requests(SP[sid].by_suffix(suf),new)
print("requests:",len(reqs))
if len(sys.argv)>2 and sys.argv[2]=='apply':
    run(svc,COPY,reqs,label='fixes7')
    Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w")); print("applied")
