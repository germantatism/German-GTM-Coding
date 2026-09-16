# -*- coding: utf-8 -*-
"""Appendix consistency pass across all 20 country slides + agent findings. Usage: python3 fixes11.py OUT [apply]"""
import json, sys, re
from engine import *
from countries import ROLES, OVERRIDES
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service(); EMU=12700
P=svc.presentations().get(presentationId=COPY).execute(); SL=[Slide(s) for s in P['slides']]
def title(s):
    for el,tr in s.els:
        t=text_of(el).strip()
        if t and pos(el,tr)[1]<70 and pos(el,tr)[0]>=50: return t
    return ''
ORDER=["United States","India","Russia","United Kingdom","South Korea","Germany","Brazil","Indonesia","Spain","Italy","France","Canada","Turkey","Vietnam","Netherlands","UAE","China","Japan","Mexico","Pakistan"]
CS={}  # country -> Slide
for s in SL:
    t=title(s)
    for c in ORDER:
        if t.startswith(c+":"): CS[c]=s
print("country slides:",len(CS))
INDIA_ROLES=dict(ROLES); INDIA_ROLES.update(OVERRIDES[21])
def roles_for(c): return INDIA_ROLES if c=="India" else ROLES
def near(s,c,role,tol=6):
    x,y=roles_for(c)[role]; m=s.near(x,y,tol=tol); return m[0] if len(m)==1 else None
reqs=[]
def style(el,st): reqs.append({'updateTextStyle':{'objectId':el['objectId'],'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
BAND=['stat_label','stat_sub','mau_label','mau_sub','l1_label','l1_sub','tot_label','tot_sub']
def knum(t):
    m=re.search(r'~?([\d.]+)K',t); 
    if m: return float(m.group(1))*1000
    m=re.search(r'~?(\d{2,4})\b',t); return float(m.group(1)) if m else None
for c,s in CS.items():
    # fonts + sizes on the blue band
    for role in BAND:
        el=near(s,c,role)
        if el: style(el,{'fontFamily':'Titillium Web','fontSize':{'magnitude':11,'unit':'PT'}})
    # role column, base-case values, SO WHAT: upright; source line italic
    for role in ('r1r','r2r','r3r','sowhat'):
        el=near(s,c,role)
        if el: style(el,{'italic':False})
    for role in ('b1v','b2v','b3v','b4v'):
        el=near(s,c,role)
        if el: style(el,{'italic':False,'bold':True})
    el=near(s,c,'src')
    if el:
        style(el,{'italic':True}); tr=next(t for e,t in s.els if e['objectId']==el['objectId'])
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':46*EMU,'translateY':519*EMU,'unit':'EMU'}}})
    # tile 4 = displayed L1 + displayed L2
    if c not in ("Russia",):
        h1,h2,t4=near(s,c,'L1h'),near(s,c,'L2h'),near(s,c,'tot')
        if h1 and h2 and t4:
            a,b=knum(text_of(h1)),knum(text_of(h2))
            if a is not None and b is not None:
                tot=a+b; txt=f"~{tot/1000:.1f}K" if tot>=1000 else f"~{int(round(tot,-2))}"
                reqs+=replace_requests(t4,txt)
    # flags: stronger outline
    for el,tr in s.els:
        if 'image' in el and pos(el,tr)[1]<70 and pos(el,tr)[0]<130:
            reqs.append({'updateImageProperties':{'objectId':el['objectId'],'imageProperties':{'outline':{'outlineFill':{'solidFill':{'color':{'rgbColor':{'red':0.55,'green':0.58,'blue':0.68}},'alpha':1}},'weight':{'magnitude':1*EMU,'unit':'EMU'},'dashStyle':'SOLID'}},'fields':'outline'}})
# India: show 30.1K so 30.1 + 1.4 = 31.5
s=CS["India"]; reqs+=replace_requests(near(s,"India",'L1h'),"+~30.1K new paid subscribers"); reqs+=replace_requests(near(s,"India",'tot'),"~31.5K")
# US: box label + Russia source
s=CS["United States"]
for el,tr in s.els:
    if text_of(el).strip()=='BASE-CASE MODEL': reqs+=replace_requests(el,"UPSIDE MODEL (not in base case)")
s=CS["Russia"]; el=near(s,"Russia",'src')
if el: reqs+=replace_requests(el,"Source: The Moscow Times (Mar 6 2022); US Treasury designation of NSPK (Feb 23 2024) via Wikipedia; SimilarWeb  ·  TO VALIDATE: revisit only if sanctions change")
# EXTRA from agents 2 and 3 (objectId, text) and style tweaks
EXTRA=json.load(open(f"{OUT}/build/extra11.json")) if __import__('os').path.exists(f"{OUT}/build/extra11.json") else {}
IDX={el['objectId']:el for s in SL for el,tr in s.els}
for oid,new in EXTRA.get('text',{}).items():
    if oid in IDX: reqs+=replace_requests(IDX[oid],new)
for oid,st in EXTRA.get('style',{}).items():
    if oid in IDX: style(IDX[oid],st)
# ---- S43 rows 19-20: shift, background, MAU total ----
RANK=next(s for s in SL if s.id=='g3db258e17b2_3_268')
from extras import shape
rowboxes=[(el,tr) for el,tr in RANK.els if el['objectId'].startswith('hf_row')]
for el,tr in rowboxes:
    reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY']+3*EMU,'unit':'EMU'}}})
ys=sorted(set(round(tr['translateY']/EMU)+3 for el,tr in rowboxes))
bg_ids=[]
for y in ys[:2]:
    r=shape(RANK.id,'RECTANGLE',52,y+1,648,14,fill={'red':0.93,'green':0.94,'blue':0.98},outline='none'); bg_ids.append(r[0]['createShape']['objectId']); reqs+=r
reqs.append({'updatePageElementsZOrder':{'pageElementObjectIds':[el['objectId'] for el,tr in rowboxes],'operation':'BRING_TO_FRONT'}})
tot17=[el for el,tr in RANK.els if text_of(el).strip()=='~1.7%']
if tot17:
    st={}
    for te in tot17[0]['shape']['text'].get('textElements',[]):
        if 'textRun' in te and te['textRun'].get('content','').strip(): st={k:v for k,v in te['textRun'].get('style',{}).items() if k in TEXT_FIELDS}; break
    ttr=next(t for e,t in RANK.els if e['objectId']==tot17[0]['objectId'])
    oid='hf_mau_total'; reqs.append({'createShape':{'objectId':oid,'shapeType':'TEXT_BOX','elementProperties':{'pageObjectId':RANK.id,'size':{'width':{'magnitude':70*EMU,'unit':'EMU'},'height':{'magnitude':14*EMU,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'translateX':188*EMU,'translateY':ttr['translateY'],'unit':'EMU'}}}})
    reqs.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':'6.06M'}})
    if st: reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
    reqs.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'autofit':{'autofitType':'NONE'},'contentAlignment':'MIDDLE'},'fields':'autofit.autofitType,contentAlignment'}})
# ---- S45/S47 divider stat boxes: align with S49's original ----
for s in SL:
    for el,tr in s.els:
        if el['objectId'].startswith('hf_divstat'):
            reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX']-6*EMU,'translateY':tr['translateY']-7*EMU,'unit':'EMU'}}})
print("requests:",len(reqs))
if len(sys.argv)>2 and sys.argv[2]=='apply':
    run(svc,COPY,reqs,label='fixes11'); print("applied")
