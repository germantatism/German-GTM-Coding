# -*- coding: utf-8 -*-
import sys, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests
COPY='1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
S_AGENDA='g3caca0138e4_0_0'; S_BC='g3fb7d86b358_4_73'
svc=service()
def batch(reqs,label):
    if not reqs: return
    r=svc.presentations().batchUpdate(presentationId=COPY,body={'requests':reqs}).execute(); print(f"  {label}: {len(reqs)} requests ok"); return r
def get(): return svc.presentations().get(presentationId=COPY).execute()
EMU=12700; BASE=3000000
BLUE=(0.231,0.294,0.976); DARK=(0.09,0.094,0.11); GREY=(0.357,0.369,0.42); LILAC=(0.933,0.941,0.984); LIGHT=(0.973,0.976,0.988); LINE=(0.89,0.898,0.941); WHITE=(1,1,1); SOFT=(0.85,0.87,1.0)
def rgb(c): return {'red':c[0],'green':c[1],'blue':c[2]}
def st(size,bold=False,color=DARK):
    return {'fontFamily':'Titillium Web','weightedFontFamily':{'fontFamily':'Titillium Web','weight':700 if bold else 400},'bold':bold,'fontSize':{'magnitude':size,'unit':'PT'},'foregroundColor':{'opaqueColor':{'rgbColor':rgb(color)}}}
def props(page,x,y,w,h):
    return {'pageObjectId':page,'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':h*EMU,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'}}
def xform(oid,x,y,w,h,size):
    return {'updatePageElementTransform':{'objectId':oid,'transform':{'scaleX':w*EMU/size['width']['magnitude'],'scaleY':h*EMU/size['height']['magnitude'],'shearX':0,'shearY':0,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'},'applyMode':'ABSOLUTE'}}
def fillreq(oid,fill,alpha=1.0):
    return {'updateShapeProperties':{'objectId':oid,'shapeProperties':{'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':rgb(fill)},'alpha':alpha}},'outline':{'propertyState':'NOT_RENDERED'}},'fields':'shapeBackgroundFill.solidFill.color,shapeBackgroundFill.solidFill.alpha,outline.propertyState'}}
def rect(R,oid,page,x,y,w,h,fill,alpha=1.0):
    R.append({'createShape':{'objectId':oid,'shapeType':'RECTANGLE','elementProperties':props(page,x,y,w,h)}}); R.append(fillreq(oid,fill,alpha))
def tbox(R,oid,page,x,y,w,h,paras,align='START',line=90,valign='TOP'):
    R.append({'createShape':{'objectId':oid,'shapeType':'TEXT_BOX','elementProperties':props(page,x,y,w,h)}})
    full='\n'.join(''.join(t for t,s in p) for p in paras)
    R.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':full}})
    i=0
    for p in paras:
        for t,s in p:
            if t: R.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':i,'endIndex':i+len(t)},'style':s,'fields':'fontFamily,weightedFontFamily,bold,fontSize,foregroundColor'}}); i+=len(t)
        i+=1
    R.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':{'lineSpacing':line,'alignment':align,'spaceAbove':{'magnitude':0,'unit':'PT'},'spaceBelow':{'magnitude':0,'unit':'PT'}},'fields':'lineSpacing,alignment,spaceAbove,spaceBelow'}})
    R.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':{'contentAlignment':valign},'fields':'contentAlignment'}})

P=get(); order=[s['objectId'] for s in P['slides']]
# ---- 0) agenda scales ----
R=[]
S={s['objectId']:s for s in P['slides']}
for el,tr in elements(S[S_AGENDA]):
    t=text_of(el).strip(); oid=el['objectId']
    rows={'NUESTRO ENTENDIMIENTO DEL CONTEXTO':(415,262,263),'01.':(373,262,23),'¿POR QUÉ YUNO?':(415,284,263),'02.':(373,284,23),'BUSINESS CASE':(415,306,263),'03.':(373,306,23),'PROPUESTA':(415,328,263),'04.':(373,328,23)}
    if t in rows:
        x,y,w=rows[t]; R.append(xform(oid,x,y,w,13,el['size']))
batch(R,'agenda scales')
# ---- 1) delete old slides first (frees element ids), then fresh duplicates ----
batch([{'deleteObject':{'objectId':sid}} for sid in ('ctx_a','ctx_b') if sid in order],'delete old ctx slides')
P=get(); order=[s['objectId'] for s in P['slides']]
if 'ctx_a2' not in order:
    batch([{'duplicateObject':{'objectId':S_BC,'objectIds':{S_BC:'ctx_a2','g3fb7d86b358_4_75':'ctxa_eyebrow','g3fb7d86b358_4_74':'ctxa_title','g3fb7d86b358_4_197':'ctxa_panel'}}},
           {'duplicateObject':{'objectId':S_BC,'objectIds':{S_BC:'ctx_b2','g3fb7d86b358_4_75':'ctxb_eyebrow','g3fb7d86b358_4_74':'ctxb_title','g3fb7d86b358_4_189':'ctxb_bg0','g3fb7d86b358_4_191':'ctxb_bg2'}}}],'duplicate S13 x2')
P=get(); S={s['objectId']:s for s in P['slides']}
R=[]
keepA={'ctxa_eyebrow','ctxa_title','ctxa_panel'}; keepB={'ctxb_eyebrow','ctxb_title','ctxb_bg0','ctxb_bg2'}
sizes={}
for sid,keep in (('ctx_a2',keepA),('ctx_b2',keepB)):
    for el,tr in elements(S[sid]):
        if el['objectId'] in keep: sizes[el['objectId']]=el['size']
        else: R.append({'deleteObject':{'objectId':el['objectId']}})
eyeA=[el for el,tr in elements(S['ctx_a2']) if el['objectId']=='ctxa_eyebrow'][0]; titA=[el for el,tr in elements(S['ctx_a2']) if el['objectId']=='ctxa_title'][0]
eyeB=[el for el,tr in elements(S['ctx_b2']) if el['objectId']=='ctxb_eyebrow'][0]; titB=[el for el,tr in elements(S['ctx_b2']) if el['objectId']=='ctxb_title'][0]
R+=replace_requests(eyeA,'NUESTRO ENTENDIMIENTO DEL CONTEXTO')+replace_requests(titA,'Resumen ejecutivo')
R+=replace_requests(eyeB,'NUESTRO ENTENDIMIENTO DEL CONTEXTO')+replace_requests(titB,'La capa de pagos de Palco hoy')
# panel + row backgrounds: recolor + place
R.append(fillreq('ctxa_panel',BLUE)); R.append(xform('ctxa_panel',358,64,332,326,sizes['ctxa_panel']))
R.append(fillreq('ctxb_bg0',LILAC)); R.append(xform('ctxb_bg0',315,90,375,66,sizes['ctxb_bg0']))
R.append(fillreq('ctxb_bg2',LILAC)); R.append(xform('ctxb_bg2',315,230,375,66,sizes['ctxb_bg2']))
batch(R,'strip + titles + backgrounds')
# ---- 2) slide A content ----
R=[]; pg='ctx_a2'
tbox(R,'ctxa_l1',pg,45,70,140,12,[[('Palco',st(9,True,BLUE))]])
tbox(R,'ctxa_b1',pg,45,84,138,70,[[('Plataforma white-label de ticketing con sede en Madrid: más de 500 recintos y promotores en 30 países venden bajo su propia marca sobre la tecnología de Palco. Desde finales de 2025 pertenece a Bocel Private Equity junto a Patricio Villalobos y Miguel Ramírez, con un plan de expansión en LatAm.',st(7.5,False,GREY))]])
rect(R,'ctxa_vl',pg,190,72,1,84,LINE)
tbox(R,'ctxa_l2',pg,198,70,145,24,[[('50+ integraciones propias, sin capa de decisión',st(9,True,BLUE))]])
tbox(R,'ctxa_b2',pg,198,94,145,66,[[('Palco construyó y mantiene más de 50 conexiones con pasarelas en 18 mercados. Cada tenant es merchant of record: recauda con su propia cuenta, liquida a Palco y gestiona fraude y contracargos con su procesador, sin visibilidad consolidada.',st(7.5,False,GREY))]])
tbox(R,'ctxa_kc',pg,45,168,200,16,[[('RETOS CLAVE',st(11,True,BLUE))]])
items=['Aprobación en tarjeta entre 56% y 68% en los procesadores de México, la mitad de su volumen','Cada mercado nuevo exige construir y mantener otra integración','Sin reintento sobre otra ruta cuando un procesador declina o cae','Split de comisión, 3DS, tokenización y ruteo por BIN resueltos tenant por tenant','Septiembre define el camino: construir la orquestación en casa o integrarla']
for i,t in enumerate(items):
    y=190+i*24
    tbox(R,f'ctxa_ar{i}',pg,40,y,20,22,[[('↗',st(11,True,BLUE))]],align='CENTER',valign='MIDDLE')
    tbox(R,f'ctxa_it{i}',pg,58,y,287,22,[[(t,st(8.5,False,DARK))]],valign='MIDDLE')
tbox(R,'ctxa_ph',pg,372,76,305,16,[[('QUÉ OBTIENE PALCO AL TRABAJAR CON YUNO',st(10.5,True,WHITE))]])
blocks=[('UNA SOLA INTEGRACIÓN PARA TODAS SUS PASARELAS','450+ proveedores y 1,000+ métodos de pago con una integración. Sus clientes cargan sus propias credenciales por API y cada uno opera en su subcuenta.'),
        ('SMART ROUTING, REINTENTOS Y MONITORES','Reglas por BIN, país, monto y metadata. Reintento automático sobre otra ruta cuando un procesador declina o cae, y redistribución de tráfico durante los on-sales.'),
        ('SEGURIDAD Y VISIBILIDAD CONSOLIDADA','3DS dinámico, motor antifraude y reglas de riesgo sobre todos los tenants, con reportes por cuenta, condición e issuer en un solo dashboard.')]
for i,(h,b) in enumerate(blocks):
    y=104+i*94
    tbox(R,f'ctxa_bh{i}',pg,372,y,305,14,[[(h,st(9,True,WHITE))]])
    tbox(R,f'ctxa_bb{i}',pg,372,y+16,305,44,[[(b,st(8,False,SOFT))]])
    if i<2: rect(R,f'ctxa_sep{i}',pg,372,y+76,305,0.75,WHITE,alpha=0.3)
batch(R,'slide A content')
# ---- 3) slide B content (shape table) ----
R=[]; pg='ctx_b2'
tbox(R,'ctxb_l1',pg,45,68,250,12,[[('APROBACIÓN POR PROCESADOR',st(9,True,DARK))]])
tbox(R,'ctxb_l2',pg,45,80,250,11,[[('Su data, últimos 12 meses, ordenada por intentos',st(7.5,False,GREY))]])
rows=[('Mercado Pago v2 (AR/MX)','754,700','67.9%'),('Openpay (MX)','506,700','58.0%'),('Redsys (ES)','500,300','88.1%'),('Banorte (MX)','420,400','59.6%'),
 ('Authorize.net (US)','210,400','90.3%'),('UepaPay (RD)','153,100','98.0%'),('Cybersource','109,800','63.7%'),('Santander (MX)','74,800','56.1%'),
 ('Mercado Pago Wallet','72,900','92.1%'),('Stripe','55,900','57.4%'),('Fiserv','48,100','43.7%'),('Line (VE)','29,100','8.7%'),('Total (16 procesadores)','3,087,600','70.8%')]
MX={'Openpay (MX)','Banorte (MX)','Santander (MX)'}
X0,W=45,250; cols=[(0,128),(128,62),(190,60)]; RH=13; y=95
rect(R,'ctxb_hdr',pg,X0,y,W,14,BLUE)
for ci,(cx,cw) in enumerate(cols):
    tbox(R,f'ctxb_h{ci}',pg,X0+cx,y,cw,14,[[(('Procesador','Intentos','Aprobación')[ci],st(7,True,WHITE))]],align='START' if ci==0 else 'END',valign='MIDDLE')
y+=14
for ri,(a,b,c) in enumerate(rows):
    tot=ri==len(rows)-1; mx=a in MX
    if mx or tot: rect(R,f'ctxb_rb{ri}',pg,X0,y,W,RH,LILAC if mx else LIGHT)
    color=BLUE if mx else DARK; bold=mx or tot
    for ci,(cx,cw) in enumerate(cols):
        tbox(R,f'ctxb_c{ri}_{ci}',pg,X0+cx,y,cw,RH,[[((a,b,c)[ci],st(7,bold,color))]],align='START' if ci==0 else 'END',valign='MIDDLE')
    rect(R,f'ctxb_ln{ri}',pg,X0,y+RH-0.5,W,0.5,LINE)
    y+=RH
tbox(R,'ctxb_fn',pg,45,y+3,250,20,[[('Se muestran 12 de los 16 procesadores; el total incluye los 16. Fuente: cifras compartidas por Palco el 2 de septiembre de 2026.',st(6,False,GREY))]])
tbox(R,'ctxb_rh',pg,315,68,375,16,[[('EL SETUP ACTUAL TIENE RESTRICCIONES',st(11,True,DARK))]])
cons=[('Aprobación de tarjeta por debajo de su propio mercado','Openpay 58.0%, Banorte 59.6% y Santander 56.1% en México, donde el mercado ronda entre 69% y 72%. Con el mismo checkout, Redsys aprueba 88.1% y UepaPay 98.0%: la variable es la ruta, no la plataforma.'),
      ('Sin fallback entre rutas','Un rechazo en un procesador no se reintenta automáticamente por otra ruta, y una caída durante un on-sale no redistribuye el tráfico. La venta se pierde en el primer intento.'),
      ('Cada integración es un proyecto','Más de 50 conexiones construidas y mantenidas en casa. Cada mercado nuevo y cada cambio de API de un procesador cae sobre el equipo de Palco; ustedes lo describieron como el principal cuello de botella.'),
      ('Fraude y riesgo sin visión consolidada','Cada tenant gestiona fraude y contracargos con su procesador. No hay dato consolidado ni reglas comunes de 3DS, riesgo o split de comisión con el tenant como merchant of record.')]
for i,(h,b) in enumerate(cons):
    yy=90+i*70
    tbox(R,f'ctxb_ch{i}',pg,325,yy+6,355,13,[[(h,st(9,True,BLUE))]])
    tbox(R,f'ctxb_cb{i}',pg,325,yy+20,355,44,[[(b,st(8,False,DARK))]])
batch(R,'slide B content')
# ---- 4) remove old slides, reposition ----
P=get(); order=[s['objectId'] for s in P['slides']]
R=[{'deleteObject':{'objectId':sid}} for sid in ('ctx_a','ctx_b') if sid in order]
batch(R,'delete old ctx slides')
for sid,target in (('ctx_a2',3),('ctx_b2',4)):
    order=[s['objectId'] for s in get()['slides']]
    if order.index(sid)!=target: batch([{'updateSlidesPosition':{'slideObjectIds':[sid],'insertionIndex':target}}],f'move {sid}')
Q=get(); json.dump(Q,open('cur_deck_v5.json','w')); o=[s['objectId'] for s in Q['slides']]; print("order head:",o[:6],"total",len(o))
for sid,name in ((S_AGENDA,'agenda3'),('ctx_a2','A3'),('ctx_b2','B3')):
    r=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=sid,thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f"ctx_{name}.png"); print("thumb",name,"slide #",o.index(sid)+1)
