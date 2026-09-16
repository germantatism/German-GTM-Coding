# -*- coding: utf-8 -*-
import sys, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests, run, TEXT_FIELDS
COPY='1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
LOGO=open('logo_url.txt').read().strip()
svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
SRC=json.load(open('src_deck.json'))
idx={}; 
for s in P['slides']:
    for el,tr in elements(s): idx[el['objectId']]=el
sidx={}
for s in SRC['slides']:
    for el,tr in elements(s): sidx[el['objectId']]=el
reqs=[]
# 1) S9: reapply the first run style of the ORIGINAL element to the whole text (emoji flags are 2 UTF-16 units each)
for suf in (6,9,17,20,26,29,36,41,46,49):
    oid=f'g3f8b4c413fe_1_{suf}'; el=sidx[oid]
    st=None
    for te in el['shape']['text'].get('textElements',[]):
        if 'textRun' in te and te['textRun'].get('content','').strip():
            st={k:v for k,v in te['textRun'].get('style',{}).items() if k in TEXT_FIELDS}; break
    if st: reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':st,'fields':','.join(st.keys())}})
# 2) shorter texts
FIX={'g3fa1128e0cb_1_134':'80%+ de los equipos de TI prefieren orquestación; ~80% menos costo de desarrollo',
     'g3f8b4c413fe_1_2627':'Costos, FX y aprobaciones.',
     'g3caca0138e4_0_2194':'Analítica de pagos'}
for oid,new in FIX.items(): reqs+=replace_requests(idx[oid],new)
# 3) S7 payouts description: anchor to top so two lines grow downward
reqs.append({'updateShapeProperties':{'objectId':'g3caca0138e4_0_2199','shapeProperties':{'contentAlignment':'TOP'},'fields':'contentAlignment'}})
# 4) cover: AppMaking logo -> Palco wordmark
s1=P['slides'][0]['objectId']
if 'g3fa9c656f54_1_0' in idx: reqs.append({'deleteObject':{'objectId':'g3fa9c656f54_1_0'}})
W,H=98,12.5
reqs.append({'createImage':{'objectId':'palco_cover_logo','url':LOGO,'elementProperties':{'pageObjectId':s1,
  'size':{'width':{'magnitude':W*12700,'unit':'EMU'},'height':{'magnitude':H*12700,'unit':'EMU'}},
  'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':122*12700,'translateY':26.5*12700,'unit':'EMU'}}}})
print("requests:",len(reqs))
run(svc,COPY,reqs,label='palco fixes')
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open('copy_deck_after2.json','w'))
for n in (1,6,7,9,16):
    r=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=Q['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f"fix_{n:02d}.png")
print("thumbs done")
