# -*- coding: utf-8 -*-
import sys, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests
COPY='1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
S13='g3fb7d86b358_4_73'; S14='g3f6c0558646_0_35'; S15='g3fb7d86b358_4_331'; S11='g3c99cf7678e_0_28713'
T=37.09
# ---- recompute ----
L1_att=1952600; L2_att=88000; L2_appr=41888
l1c=round(L1_att*0.05)*T; l1o=round(L1_att*0.10)*T
l2c=(round(L2_att*0.60)-L2_appr)*T; l2o=(round(L2_att*0.68)-L2_appr)*T
l3c,l3o=346e6*0.00075,346e6*0.00125; l4c,l4o=230000,360000
tc=l1c+l2c+l3c+l4c; to=l1o+l2o+l3o+l4o
M=lambda v:f"${v/1e6:.1f}M"; M2=lambda v:f"${v/1e6:.2f}M"
print("L1",l1c,l1o,"L2",l2c,l2o,"Tc",tc,"To",to,"avg",(tc+to)/2,"L1avg",(l1c+l1o)/2,"L2avg",(l2c+l2o)/2,"GTV",(l1c+l1o+l2c+l2o)/2,l1c+l2c,l1o+l2o)
def rep(old,new,pages):
    return {'replaceAllText':{'containsText':{'text':old,'matchCase':True},'replaceText':new,'pageObjectIds':pages}}
R=[]
both=[S13,S14]
# numbers (bold runs preserved)
for old,new in [("$15.9M",M(l1c)),("$31.8M",M(l1o)),("$0.47M",M2(l2c)),("$0.77M",M2(l2o)),
                ("$23.9M",M((l1c+l1o)/2)),("$0.62M",M2((l2c+l2o)/2)),("$16.9M",M(tc)),("$33.4M",M(to)),("$25.1M",M((tc+to)/2)),
                ("$24.5M",M((l1c+l1o+l2c+l2o)/2)),("$16.4M a $32.6M",f"{M(l1c+l2c)} a {M(l1o+l2o)}")]:
    R.append(rep(old,new,both))
# S13 texts
R+=[rep("con un ticket de $163 por transacción de tarjeta, derivado de sus propias cifras: $346 M de TPV en tarjeta entre 2.12 M de transacciones de tarjeta aprobadas al año.","con el ticket promedio de $37.09 que ustedes reportaron.",[S13]),
    rep("Hoy el 3DS es obligatorio en todos los flujos de tarjeta:","Si el 3DS aplica a todos los flujos de tarjeta, como plantearon,",[S13]),
    rep("Requiere el MDR por procesador, que aún no tenemos.","Se calibra con el MDR por procesador que nos compartan.",[S13]),
    rep("el mantenimiento de 16 conexiones en 18 mercados","el mantenimiento de sus 50+ integraciones (16 procesadores concentran el volumen)",[S13]),
    rep("3.09 M de intentos de tarjeta al año","3.09 M de intentos en sus procesadores al año",[S13]),
    rep("declinadas al año , unas","declinadas al año, unas",[S13]),
    rep("concentradas en los procesadores","concentradas principalmente en los procesadores",[S13])]
# S14 texts
R+=[rep("a un ticket de $163. Ese ticket sale de sus propias cifras, $346 M de TPV en tarjeta entre 2.12 M de transacciones de tarjeta aprobadas, y no del ticket de $37.09 que corresponde al boleto individual, no a la transacción.","al ticket promedio de $37.09 que ustedes reportaron.",[S14]),
    rep("a un ticket de $43.10 derivado del volumen de Honduras","al mismo ticket de $37.09",[S14]),
    rep("benchmark de Yuno por ruteo de menor costo","supuesto de modelación de Yuno por ruteo de menor costo",[S14]),
    rep("3 a 4 FTE de ingeniería de pagos, benchmark de Yuno.","3 a 4 FTE de ingeniería de pagos, supuesto de modelación de Yuno.",[S14]),
    rep("Propuesta","BUSINESS CASE",[S14])]
svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
idx={}
for s in P['slides']:
    for el,tr in elements(s): idx[el['objectId']]=el
# S15 eyebrow (dash + tab) via full replace
R+=replace_requests(idx['g3fb7d86b358_4_333'],'PROPUESTA · PRICING')
# S11 speaker notes: wipe
s11=[s for s in P['slides'] if s['objectId']==S11][0]
for el in s11['slideProperties']['notesPage'].get('pageElements',[]):
    if 'shape' in el and text_of(el).strip():
        print('notes element with text:',el['objectId'],repr(text_of(el)[:60]))
        R.append({'deleteText':{'objectId':el['objectId'],'textRange':{'type':'ALL'}}})
resp=svc.presentations().batchUpdate(presentationId=COPY,body={'requests':R}).execute()
for q,r in zip(R,resp.get('replies',[])):
    if 'replaceAllText' in q:
        n=r.get('replaceAllText',{}).get('occurrencesChanged',0)
        flag='' if n else '   <-- NO MATCH'
        print(f"{n:2d}x  {q['replaceAllText']['containsText']['text'][:70]!r} -> {q['replaceAllText']['replaceText'][:50]!r}{flag}")
Q=svc.presentations().get(presentationId=COPY).execute(); json.dump(Q,open('cur_deck_v3.json','w'))
for n in (11,13,14,15):
    r=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=Q['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f"v3_{n:02d}.png")
print("thumbs done")
