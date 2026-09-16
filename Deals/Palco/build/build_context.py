# -*- coding: utf-8 -*-
import sys, json, urllib.request, time
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests
COPY='1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
S_AGENDA='g3caca0138e4_0_0'; S_WHYDIV='g3caca0138e4_0_2129'; S_BCDIV='g3caca0138e4_0_2759'; S_BC='g3fb7d86b358_4_73'; S_PRICE='g3fb7d86b358_4_331'; S11='g3c99cf7678e_0_28713'
svc=service()
def batch(reqs,label):
    r=svc.presentations().batchUpdate(presentationId=COPY,body={'requests':reqs}).execute(); print(f"  {label}: {len(reqs)} requests ok"); return r
def get(): return svc.presentations().get(presentationId=COPY).execute()
EMU=12700
BLUE=(0.231,0.294,0.976); TBLUE=(0.243,0.310,0.878); DARK=(0.09,0.094,0.11); GREY=(0.357,0.369,0.42)
LILAC=(0.933,0.941,0.984); LIGHT=(0.973,0.976,0.988); LINE=(0.89,0.898,0.941); WHITE=(1,1,1); SOFT=(0.85,0.87,1.0)
def rgb(c): return {'red':c[0],'green':c[1],'blue':c[2]}
def st(size,bold=False,color=DARK):
    return {'fontFamily':'Titillium Web','weightedFontFamily':{'fontFamily':'Titillium Web','weight':700 if bold else 400},'bold':bold,'fontSize':{'magnitude':size,'unit':'PT'},'foregroundColor':{'opaqueColor':{'rgbColor':rgb(color)}}}
def props(page,x,y,w,h):
    return {'pageObjectId':page,'size':{'width':{'magnitude':w*EMU,'unit':'EMU'},'height':{'magnitude':h*EMU,'unit':'EMU'}},'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'}}
def rect(R,oid,page,x,y,w,h,fill,kind='RECTANGLE',alpha=1.0,outline=None):
    R.append({'createShape':{'objectId':oid,'shapeType':kind,'elementProperties':props(page,x,y,w,h)}})
    sp={'shapeBackgroundFill':{'solidFill':{'color':{'rgbColor':rgb(fill)},'alpha':alpha}}}; fields='shapeBackgroundFill.solidFill.color,shapeBackgroundFill.solidFill.alpha'
    if outline: sp['outline']={'outlineFill':{'solidFill':{'color':{'rgbColor':rgb(outline)},'alpha':1}},'weight':{'magnitude':0.75,'unit':'PT'},'propertyState':'RENDERED'}; fields+=',outline.outlineFill.solidFill.color,outline.weight,outline.propertyState'
    else: sp['outline']={'propertyState':'NOT_RENDERED'}; fields+=',outline.propertyState'
    R.append({'updateShapeProperties':{'objectId':oid,'shapeProperties':sp,'fields':fields}})
def tbox(R,oid,page,x,y,w,h,paras,align='START',line=90,valign='TOP'):
    """paras: list of paragraphs; paragraph = list of (text, style) runs"""
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
def cell(R,tid,r,c,text,style,align='START'):
    R.append({'insertText':{'objectId':tid,'cellLocation':{'rowIndex':r,'columnIndex':c},'insertionIndex':0,'text':text}})
    R.append({'updateTextStyle':{'objectId':tid,'cellLocation':{'rowIndex':r,'columnIndex':c},'textRange':{'type':'ALL'},'style':style,'fields':'fontFamily,weightedFontFamily,bold,fontSize,foregroundColor'}})
    R.append({'updateParagraphStyle':{'objectId':tid,'cellLocation':{'rowIndex':r,'columnIndex':c},'textRange':{'type':'ALL'},'style':{'alignment':align,'lineSpacing':90,'spaceAbove':{'magnitude':0,'unit':'PT'},'spaceBelow':{'magnitude':0,'unit':'PT'}},'fields':'alignment,lineSpacing,spaceAbove,spaceBelow'}})

# ---------- 1) duplicate slides ----------
P=get()
if 'ctx_a' not in [x['objectId'] for x in P['slides']]:
  batch([{'duplicateObject':{'objectId':S_WHYDIV,'objectIds':{S_WHYDIV:'ctx_div'}}},
       {'duplicateObject':{'objectId':S_BC,'objectIds':{S_BC:'ctx_a'}}},
       {'duplicateObject':{'objectId':S_BC,'objectIds':{S_BC:'ctx_b'}}},
       {'duplicateObject':{'objectId':S_BCDIV,'objectIds':{S_BCDIV:'prop_div'}}}],'duplicates')
else: print('  duplicates already exist, skipping')
# ---------- 2) reorder, one move per call ----------
def order(): return [s['objectId'] for s in get()['slides']]
def move(sid,target):
    o=order(); cur=o.index(sid)
    if cur==target: print(f'  {sid} already at {target}'); return
    batch([{'updateSlidesPosition':{'slideObjectIds':[sid],'insertionIndex':target}}],f'move {sid} -> {target}')
move('ctx_div',2); move('ctx_a',3); move('ctx_b',4)
o=order(); move('prop_div',o.index(S_PRICE))
o=order(); print("order:",o)
assert o[2:5]==['ctx_div','ctx_a','ctx_b'] and o[o.index(S_PRICE)-1]=='prop_div'

# ---------- 3) strip duplicates, set titles, agenda ----------
P=get(); idx={s['objectId']:s for s in P['slides']}
done3=any(text_of(el).strip()=='Resumen ejecutivo' for el,tr in elements(idx['ctx_a']))
R=[]
keep={}
for sid,(eyebrow,title) in {'ctx_a':('NUESTRO ENTENDIMIENTO DEL CONTEXTO','Resumen ejecutivo'),'ctx_b':('NUESTRO ENTENDIMIENTO DEL CONTEXTO','La capa de pagos de Palco hoy')}.items():
    for el,tr in elements(idx[sid]):
        t=text_of(el).strip()
        if t=='BUSINESS CASE': R+=replace_requests(el,eyebrow)
        elif t.startswith('Cuatro palancas'): R+=replace_requests(el,title)
        else: R.append({'deleteObject':{'objectId':el['objectId']}})
for el,tr in elements(idx['ctx_div']):
    if text_of(el).strip().startswith('¿Por qué'): R+=replace_requests(el,'Nuestro entendimiento del contexto')
for el,tr in elements(idx['prop_div']):
    if text_of(el).strip()=='Business Case': R+=replace_requests(el,'Propuesta')
# agenda: 4 rows
ag={text_of(el).strip():el for el,tr in elements(idx[S_AGENDA])}
def mv(oid,x,y): R.append({'updatePageElementTransform':{'objectId':oid,'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':x*EMU,'translateY':y*EMU,'unit':'EMU'},'applyMode':'ABSOLUTE'}})
e_lbl1=ag['¿POR QUÉ YUNO?']; e_num1=ag['01.']; e_lbl2=ag['BUSINESS CASE']; e_num2=ag['02.']
ys=[262,284,306,328]
R+=replace_requests(e_lbl1,'NUESTRO ENTENDIMIENTO DEL CONTEXTO'); mv(e_lbl1['objectId'],415,ys[0]); mv(e_num1['objectId'],373,ys[0])
R.append({'duplicateObject':{'objectId':e_lbl1['objectId'],'objectIds':{e_lbl1['objectId']:'ag_lbl2'}}}); R.append({'duplicateObject':{'objectId':e_num1['objectId'],'objectIds':{e_num1['objectId']:'ag_num2'}}})
el2=dict(e_lbl1); el2['objectId']='ag_lbl2'; R+=replace_requests(el2,'¿POR QUÉ YUNO?'); en2=dict(e_num1); en2['objectId']='ag_num2'; R+=replace_requests(en2,'02.'); mv('ag_lbl2',415,ys[1]); mv('ag_num2',373,ys[1])
R+=replace_requests(e_num2,'03.'); mv(e_lbl2['objectId'],415,ys[2]); mv(e_num2['objectId'],373,ys[2])
R.append({'duplicateObject':{'objectId':e_lbl2['objectId'],'objectIds':{e_lbl2['objectId']:'ag_lbl4'}}}); R.append({'duplicateObject':{'objectId':e_num2['objectId'],'objectIds':{e_num2['objectId']:'ag_num4'}}})
el4=dict(e_lbl2); el4['objectId']='ag_lbl4'; R+=replace_requests(el4,'PROPUESTA'); en4=dict(e_num2); en4['objectId']='ag_num4'; R+=replace_requests(en4,'04.'); mv('ag_lbl4',415,ys[3]); mv('ag_num4',373,ys[3])
if done3: print('  step 3 already applied, skipping')
else: batch(R,'strip + titles + agenda')

# ---------- 4) content: slide A (Resumen ejecutivo) ----------
P=get(); s11=[s for s in P['slides'] if s['objectId']==S11][0]
icon=[el['image']['contentUrl'] for el,tr in elements(s11) if 'image' in el and el['objectId']=='g3c99cf7678e_0_28724'][0]
R=[]; pg='ctx_a'
tbox(R,'ctxa_l1',pg,45,70,140,12,[[('Palco',st(9,True,BLUE))]])
tbox(R,'ctxa_b1',pg,45,84,138,70,[[('Plataforma white-label de ticketing con sede en Madrid: más de 500 recintos y promotores en 30 países venden bajo su propia marca sobre la tecnología de Palco. Desde finales de 2025 pertenece a Bocel Private Equity junto a Patricio Villalobos y Miguel Ramírez, con un plan de expansión en LatAm.',st(7.5,False,GREY))]])
rect(R,'ctxa_vl',pg,190,72,1,84,LINE)
tbox(R,'ctxa_l2',pg,198,70,145,24,[[('50+ integraciones propias, sin capa de decisión',st(9,True,BLUE))]])
tbox(R,'ctxa_b2',pg,198,94,145,66,[[('Palco construyó y mantiene más de 50 conexiones con pasarelas en 18 mercados. Cada tenant es merchant of record: recauda con su propia cuenta, liquida a Palco y gestiona fraude y contracargos con su procesador, sin visibilidad consolidada.',st(7.5,False,GREY))]])
tbox(R,'ctxa_kc',pg,45,168,200,16,[[('RETOS CLAVE',st(11,True,BLUE))]])
items=['Aprobación en tarjeta entre 56% y 68% en los procesadores de México, la mitad de su volumen',
       'Cada mercado nuevo exige construir y mantener otra integración',
       'Sin reintento sobre otra ruta cuando un procesador declina o cae',
       'Split de comisión, 3DS, tokenización y ruteo por BIN resueltos tenant por tenant',
       'Septiembre define el camino: construir la orquestación en casa o integrarla']
for i,t in enumerate(items):
    y=190+i*24
    R.append({'createImage':{'objectId':f'ctxa_ic{i}','url':icon,'elementProperties':props(pg,45,y+3,10,10)}})
    tbox(R,f'ctxa_it{i}',pg,60,y,285,22,[[(t,st(8.5,False,DARK))]],valign='MIDDLE')
# right blue panel
rect(R,'ctxa_panel',pg,358,64,332,326,BLUE,'ROUND_RECTANGLE')
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

# ---------- 5) content: slide B (La capa de pagos de Palco hoy) ----------
R=[]; pg='ctx_b'
tbox(R,'ctxb_l1',pg,45,68,250,12,[[('APROBACIÓN POR PROCESADOR',st(9,True,DARK))]])
tbox(R,'ctxb_l2',pg,45,80,250,11,[[('Su data, últimos 12 meses, ordenada por intentos',st(7.5,False,GREY))]])
rows=[('Procesador','Intentos','Aprobación'),
 ('Mercado Pago v2 (AR/MX)','754,700','67.9%'),('Openpay (MX)','506,700','58.0%'),('Redsys (ES)','500,300','88.1%'),('Banorte (MX)','420,400','59.6%'),
 ('Authorize.net (US)','210,400','90.3%'),('UepaPay (RD)','153,100','98.0%'),('Cybersource','109,800','63.7%'),('Santander (MX)','74,800','56.1%'),
 ('Mercado Pago Wallet','72,900','92.1%'),('Stripe','55,900','57.4%'),('Fiserv','48,100','43.7%'),('Line (VE)','29,100','8.7%'),
 ('Total (16 procesadores)','3,087,600','70.8%')]
MX={'Openpay (MX)','Banorte (MX)','Santander (MX)'}
tid='ctxb_table'
R.append({'createTable':{'objectId':tid,'elementProperties':props(pg,45,95,250,200),'rows':len(rows),'columns':3}})
for ci,w in enumerate((128,62,60)): R.append({'updateTableColumnProperties':{'objectId':tid,'columnIndices':[ci],'tableColumnProperties':{'columnWidth':{'magnitude':w*EMU,'unit':'EMU'}},'fields':'columnWidth'}})
R.append({'updateTableRowProperties':{'objectId':tid,'rowIndices':list(range(len(rows))),'tableRowProperties':{'minRowHeight':{'magnitude':12*EMU,'unit':'EMU'}},'fields':'minRowHeight'}})
for ri,(a,b,c) in enumerate(rows):
    hdr=ri==0; tot=ri==len(rows)-1; mx=a in MX
    color=WHITE if hdr else (BLUE if mx else DARK); bold=hdr or tot or mx
    cell(R,tid,ri,0,a,st(7,bold,color)); cell(R,tid,ri,1,b,st(7,bold,color),'END'); cell(R,tid,ri,2,c,st(7,bold,color),'END')
    fill=BLUE if hdr else (LILAC if mx else (LIGHT if tot else WHITE))
    R.append({'updateTableCellProperties':{'objectId':tid,'tableRange':{'location':{'rowIndex':ri,'columnIndex':0},'rowSpan':1,'columnSpan':3},'tableCellProperties':{'tableCellBackgroundFill':{'solidFill':{'color':{'rgbColor':rgb(fill)},'alpha':1}},'contentAlignment':'MIDDLE'},'fields':'tableCellBackgroundFill.solidFill.color,tableCellBackgroundFill.solidFill.alpha,contentAlignment'}})
for posn in ('INNER_HORIZONTAL','INNER_VERTICAL','OUTER'):
    R.append({'updateTableBorderProperties':{'objectId':tid,'borderPosition':posn,'tableBorderProperties':{'tableBorderFill':{'solidFill':{'color':{'rgbColor':rgb(LINE)},'alpha':1}},'weight':{'magnitude':0.5,'unit':'PT'}},'fields':'tableBorderFill.solidFill.color,tableBorderFill.solidFill.alpha,weight'}})
tbox(R,'ctxb_fn',pg,45,300,250,20,[[('Se muestran 12 de los 16 procesadores; el total incluye los 16. Fuente: cifras compartidas por Palco el 2 de septiembre de 2026.',st(6,False,GREY))]])
# right constraints
tbox(R,'ctxb_rh',pg,315,68,375,16,[[('EL SETUP ACTUAL TIENE RESTRICCIONES',st(11,True,DARK))]])
cons=[('Aprobación de tarjeta por debajo de su propio mercado','Openpay 58.0%, Banorte 59.6% y Santander 56.1% en México, donde el mercado ronda entre 69% y 72%. Con el mismo checkout, Redsys aprueba 88.1% y UepaPay 98.0%: la variable es la ruta, no la plataforma.'),
      ('Sin fallback entre rutas','Un rechazo en un procesador no se reintenta automáticamente por otra ruta, y una caída durante un on-sale no redistribuye el tráfico. La venta se pierde en el primer intento.'),
      ('Cada integración es un proyecto','Más de 50 conexiones construidas y mantenidas en casa. Cada mercado nuevo y cada cambio de API de un procesador cae sobre el equipo de Palco; ustedes lo describieron como el principal cuello de botella.'),
      ('Fraude y riesgo sin visión consolidada','Cada tenant gestiona fraude y contracargos con su procesador. No hay dato consolidado ni reglas comunes de 3DS, riesgo o split de comisión con el tenant como merchant of record.')]
for i,(h,b) in enumerate(cons):
    y=90+i*70
    if i%2==0: rect(R,f'ctxb_bg{i}',pg,315,y,375,66,LILAC,'ROUND_RECTANGLE')
    tbox(R,f'ctxb_ch{i}',pg,325,y+6,355,13,[[(h,st(9,True,BLUE))]])
    tbox(R,f'ctxb_cb{i}',pg,325,y+20,355,44,[[(b,st(8,False,DARK))]])
batch(R,'slide B content')

# ---------- thumbnails ----------
Q=get(); json.dump(Q,open('cur_deck_v4.json','w'))
o=[s['objectId'] for s in Q['slides']]
for sid,name in (('ctx_div','div'),('ctx_a','A'),('ctx_b','B'),('prop_div','pdiv'),(S_AGENDA,'agenda')):
    r=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=sid,thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f"ctx_{name}.png"); print("thumb",name,"slide #",o.index(sid)+1)
print("total slides:",len(o))
