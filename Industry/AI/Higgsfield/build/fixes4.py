import json, sys, urllib.request
from engine import *
from content import grid_rows, TOP20, WAVE2
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
O=json.load(open(f"{OUT}/copy_deck.json")); SO={s['objectId']:Slide(s) for s in O['slides']}
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
def restore(el,tr): return {'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}}
def setfill(oid,rgb): return {'updateShapeProperties':{'objectId':oid,'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':rgb},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}}
reqs=[]
P=svc.presentations().get(presentationId=COPY).execute(); EXIST=set()
def _walk(el):
    EXIST.add(el['objectId'])
    for ch in el.get('elementGroup',{}).get('children',[]): _walk(ch)
for _s in P['slides']:
    for _e in _s.get('pageElements',[]): _walk(_e)
# ---- S7 ----
t=SO['g3db0b697a2f_0_11825']; rows=[r for r in grid_rows(t,30,680,160,470) if len(r)>=6]
arch_fill={}
for r in rows:
    y=r[0][0]; arch=text_of(r[5][2]).strip()
    chips=[(el,tr) for el,tr in t.els if not text_of(el).strip() and 'shape' in el and 575<=pos(el,tr)[0]<=590 and abs(pos(el,tr)[1]-y)<=6]
    if chips: arch_fill.setdefault(arch,fill_of(chips[0][0]))
print("archetype fills:",arch_fill)
bars_all=[(el,tr) for el,tr in t.els if not text_of(el).strip() and 'shape' in el and 300<=pos(el,tr)[0]<=372 and 160<=pos(el,tr)[1]<=470]
print("MRR bar candidates:",len(bars_all),[(round(el['size']['width']['magnitude']*tr.get('scaleX',1)/12700,1),pos(el,tr)) for el,tr in bars_all[:4]])
GREY={'red':0.82,'green':0.83,'blue':0.88}
for r,d in zip(rows,TOP20):
    y=r[0][0]; arch=d[5]
    for el,tr in t.els:
        if not text_of(el).strip() and 'shape' in el and abs(pos(el,tr)[1]-y)<=6:
            x=pos(el,tr)[0]
            if 575<=x<=590:   # chip background: restore + recolor (recreate if deleted earlier)
                col=arch_fill.get(arch, GREY if arch in ('Excluded','Home market') else arch_fill['Mature'])
                if el['objectId'] in EXIST:
                    reqs.append(restore(el,tr)); reqs.append(setfill(el['objectId'],col))
                else:
                    nid='hf_chip_'+el['objectId'][-5:]
                    reqs.append({'createShape':{'objectId':nid,'shapeType':'RECTANGLE','elementProperties':{'pageObjectId':t.id,'size':el['size'],'transform':{'scaleX':tr.get('scaleX',1),'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}}})
                    reqs.append(setfill(nid,col)); reqs.append({'updateShapeProperties':{'objectId':nid,'shapeProperties':{'outline':{'propertyState':'NOT_RENDERED'}},'fields':'outline'}})
                    txt=[c[2]['objectId'] for c in r if 578<=c[1]<=590]
                    if txt: reqs.append({'updatePageElementsZOrder':{'pageElementObjectIds':txt,'operation':'BRING_TO_FRONT'}})
            elif 300<=x<=372 and el['objectId'] in EXIST:  # MRR bar
                m=d[3]
                if m in ('Baseline','n/a'): reqs.append({'deleteObject':{'objectId':el['objectId']}})
                else:
                    v=float(m.strip('$M')); base_w=el['size']['width']['magnitude']
                    reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':(45*12700*v/0.67)/base_w,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
# ---- S8 ----
w=SO['g3dbb3d0b7de_0_4441']; wrows=[r for r in grid_rows(w,55,760,160,470) if len(r)>=7]
pfill={}
for r in wrows:
    y=r[0][0]; pr=[text_of(c[2]).strip().replace('Medum','Medium') for c in r if text_of(c[2]).strip() in ('Very high','High','Medium','Medum')]
    pill=[(el,tr) for el,tr in w.els if not text_of(el).strip() and el.get('shape',{}).get('shapeType')=='ROUND_RECTANGLE' and 390<=pos(el,tr)[0]<=400 and abs(pos(el,tr)[1]-y)<=6]
    if pr and pill: pfill.setdefault(pr[0],fill_of(pill[0][0]))
print("priority fills:",pfill)
for r,d in zip(wrows,WAVE2):
    y=r[0][0]
    for el,tr in w.els:
        if text_of(el).strip() or 'shape' not in el or abs(pos(el,tr)[1]-y)>6: continue
        x=pos(el,tr)[0]
        if el['shape'].get('shapeType')=='ROUND_RECTANGLE' and 390<=x<=400 and pfill.get(d[5]): reqs.append(setfill(el['objectId'],pfill[d[5]]))
        elif 385<=x<=392 and fill_of(el): reqs.append(setfill(el['objectId'],fill_of(el)))   # restore cell bg
print("requests:",len(reqs)); run(svc,COPY,reqs,label='fixes4')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w"))
for n in [1,4,6,8,9,10,16,17,19,20,22,24,42,44,46]:
    pid=Q['slides'][n-1]['objectId']
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=pid,thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(th['contentUrl'],f"{OUT}/thumbs/S{n:02d}.png")
print("thumbs refreshed")
