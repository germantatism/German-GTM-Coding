# -*- coding: utf-8 -*-
import sys, json, urllib.request, re
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests, run, pos
from content_palco import T, DELETE, MOVE, RESTYLE, NEW, FORBID
COPY='1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
DRY = len(sys.argv)>1 and sys.argv[1]=='dry'
svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
json.dump(P,open('copy_deck_before.json','w'))
idx={}
for s in P['slides']:
    for el,tr in elements(s): idx[el['objectId']]=(el,tr,s['objectId'])
missing=[k for k in T if k not in idx]
print("MISSING ids:",missing)
reqs=[]; sim={}
for oid,new in T.items():
    if oid in idx:
        reqs+=replace_requests(idx[oid][0],new); sim[oid]=new
# duplicates for new rows
for src,new_id,text,box in NEW:
    reqs.append({'duplicateObject':{'objectId':src,'objectIds':{src:new_id}}})
    if text:
        el2=dict(idx[src][0]); el2['objectId']=new_id
        reqs+=replace_requests(el2,text); sim[new_id]=text
for oid in DELETE:
    if oid in idx: reqs.append({'deleteObject':{'objectId':oid}}); sim[oid]=''
def box_req(oid,x,y,w,h,size):
    sx=w*12700/size['width']['magnitude']; sy=h*12700/size['height']['magnitude']
    return {'updatePageElementTransform':{'objectId':oid,'transform':{'scaleX':sx,'scaleY':sy,'shearX':0,'shearY':0,'translateX':x*12700,'translateY':y*12700,'unit':'EMU'},'applyMode':'ABSOLUTE'}}
for oid,(x,y,w,h) in MOVE.items():
    reqs.append(box_req(oid,x,y,w,h,idx[oid][0]['size']))
for src,new_id,text,box in NEW:
    reqs.append(box_req(new_id,*box,idx[src][0]['size']))
for oid,st in RESTYLE.items():
    reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
# scan: untouched text elements and leftover tokens
untouched=[]; bad=[]
for n,s in enumerate(P['slides'],1):
    for el,tr in elements(s):
        t=text_of(el).strip()
        if not t: continue
        new=sim.get(el['objectId'],None)
        if new is None and not re.fullmatch(r'[\d\.,+%$ ]*',t): untouched.append((n,el['objectId'],t[:70]))
        chk=new if new is not None else t
        for f in FORBID:
            if f in chk: bad.append((n,el['objectId'],f,chk[:60]))
print("UNTOUCHED text elements:"); [print("  S%d %s | %s"%u) for u in untouched]
print("FORBIDDEN tokens:"); [print("  S%d %s [%s] %s"%b) for b in bad]
print("requests:",len(reqs))
if not DRY:
    run(svc,COPY,reqs,label='palco build')
    Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open('copy_deck_after.json','w'))
    for n,sl in enumerate(Q['slides'],1):
        r=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=sl['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(r['contentUrl'],f"new_{n:02d}.png")
    print("thumbs done")
