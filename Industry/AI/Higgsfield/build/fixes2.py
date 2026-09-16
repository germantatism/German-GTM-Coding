import json, sys, urllib.request
from engine import *
from content import WAVE2, grid_rows
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'; OUT=sys.argv[1]; svc=service()
O=json.load(open(f"{OUT}/copy_deck.json")); P=svc.presentations().get(presentationId=COPY).execute()
w2o=Slide(next(s for s in O['slides'] if s['objectId']=='g3dbb3d0b7de_0_4441')); w2=Slide(next(s for s in P['slides'] if s['objectId']=='g3dbb3d0b7de_0_4441'))
orows=[r for r in grid_rows(w2o,55,760,160,470) if len(r)>=7]
reqs=[]
def fill_of(el): return el['shape'].get('shapeProperties',{}).get('shapeBackgroundFill',{}).get('solidFill',{}).get('color',{}).get('rgbColor')
# chips: non-text shapes at x 385..415 per row in ORIGINAL geometry -> fill by original priority
chipfill={}; chip_by_y={}
for r in orows:
    y=r[0][0]; pr=[text_of(c[2]).strip().replace('Medum','Medium') for c in r if text_of(c[2]).strip() in ('Very high','High','Medium','Medum')]
    bg=[(el,tr) for el,tr in w2o.els if not text_of(el).strip() and 'shape' in el and 385<=pos(el,tr)[0]<=420 and abs(pos(el,tr)[1]-y)<=8]
    if pr and bg:
        chipfill.setdefault(pr[0],fill_of(bg[0][0])); chip_by_y[y]=bg[0][0]['objectId']
print("chip fills by priority:",chipfill)
for r,d in zip(orows,WAVE2):
    oid=chip_by_y.get(r[0][0]); f=chipfill.get(d[5])
    if oid and f: reqs.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':f},'alpha':1}}},'fields':'shapeBackgroundFill.solidFill.color'}})
# penetration bars: per row two rects at x 255..300; wider (original) = track -> restore; narrower = bar -> scale
for r,d in zip(orows,WAVE2):
    y=r[0][0]; opct=float(text_of(r[3][2]).strip().rstrip('%')); npct=float(d[3].rstrip('%'))
    bars=[(el,tr) for el,tr in w2o.els if not text_of(el).strip() and 'shape' in el and 255<=pos(el,tr)[0]<=300 and abs(pos(el,tr)[1]-y)<=8]
    bars.sort(key=lambda b:-b[0]['size']['width']['magnitude']*b[1].get('scaleX',1))
    for k,(el,tr) in enumerate(bars):
        sx=tr.get('scaleX',1) if k==0 else tr.get('scaleX',1)*npct/opct
        reqs.append({'updatePageElementTransform':{'objectId':el['objectId'],'applyMode':'ABSOLUTE','transform':{'scaleX':sx,'scaleY':tr.get('scaleY',1),'shearX':0,'shearY':0,'translateX':tr['translateX'],'translateY':tr['translateY'],'unit':'EMU'}}})
print("requests:",len(reqs)); run(svc,COPY,reqs,label='chips+bars')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open(f"{OUT}/final_deck.json","w"))
for n in [1,2,3,4,9,10,11,12,14,20,23,24]:
    pid=Q['slides'][n-1]['objectId']
    t=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=pid,thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(t['contentUrl'],f"{OUT}/thumbs/S{n:02d}.png")
print("thumbs refreshed")
