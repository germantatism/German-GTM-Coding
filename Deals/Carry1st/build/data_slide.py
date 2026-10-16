import warnings; warnings.filterwarnings('ignore')
import gs_engine as E, re
PID='1D1HwXY1TRczJxtqDKWi_JgJT-cKqSXhuH-6rRn1BIQ4'
deck=E.Deck(PID); P=deck.fetch()
s={'id':'data-proof','kicker':'BUSINESS CASE · WHAT THE DATA SHOWS',
   'headline':'Across about $17B a year from 50 merchants, approval rises with each provider added on a rail, up to three.'}
base=P['slides'][6]; assert 'WHY YUNO AGAINST' in ''.join(E.text_of(el) for el,_ in E.elements(base))
sid='dproof_slide'
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'duplicateObject':{'objectId':base['objectId'],'objectIds':{base['objectId']:sid}}}]}).execute()
dup=[x for x in deck.fetch()['slides'] if x['objectId']==sid][0]
keep=[]; req=[]
for el in dup['pageElements']:
    tr=el.get('transform',{}); x,y,w,h=E.geom(el,tr); t=E.text_of(el).strip()
    if t.startswith('BUSINESS CASE'): kick=el['objectId']; keep.append(kick)
    elif t.startswith('Against going direct'): head=el['objectId']; keep.append(head)
    elif 'image' in el and x>600 and y<45: keep.append(el['objectId'])
    elif re.fullmatch(r'\d{1,2}',t) and y>=370: keep.append(el['objectId'])
req=[{'deleteObject':{'objectId':el['objectId']}} for el in dup['pageElements'] if el['objectId'] not in keep]
req+=[{'deleteText':{'objectId':kick,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':kick,'insertionIndex':0,'text':s['kicker']}},
      {'deleteText':{'objectId':head,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':head,'insertionIndex':0,'text':s['headline']}}]
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':req}).execute()
sb=E.SB(deck,sid,'dproof')
y0=sb.zy+2
# left: approval by providers
sb.text(36,y0,270,10,'APPROVAL BY PROVIDERS ON THE SAME RAIL',size=7,bold=True,color=E.BLUE,ls=100)
rows=[('1 provider','75%','Baseline: one route, a decline is a lost sale',90,'#B0B7F2'),
      ('2 providers','77%','+2 pts: soft declines retried on a second route',126,E.BLUE),
      ('3 providers','78%','+1 pt more; beyond three, the gain flattens',144,E.DEEP)]
y=y0+18
for lab,val,cap,w,col in rows:
    sb.text(36,y+3,62,12,lab,size=8,bold=True,color=E.INK,ls=100)
    sb.rect(100,y,w,18,fill=col)
    sb.text(100+w+6,y+2,40,14,val,size=11,bold=True,color=E.INK,ls=100)
    sb.text(100,y+21,200,10,cap,size=7,color=E.GREY,ls=100)
    y+=46
sb.text(36,y+2,270,30,'Illustrative for Carry1st on a 75% single-route baseline; the business case counts +3 pts in the base case.',size=6.5,color=E.GREY,italic=True,ls=110)
# right: decline codes
sb.text(330,y0,354,10,'WHY A SECOND ROUTE APPROVES WHAT THE FIRST DECLINED',size=7,bold=True,color=E.BLUE,ls=100)
rows=[['Do not honor (05)','Generic issuer refusal, often risk-scored on the acquirer','Retry on another provider in the same session'],
      ['Issuer or switch unavailable (91)','Timeout or outage on one route','Reroute instantly; Monitors shift traffic'],
      ['Insufficient funds (51)','The card cannot pay this amount now','No blind retry; offer Pix or another local method'],
      ['Invalid card or stolen (14, 43)','Hard decline','Never retried, protecting standing with issuers']]
sb.table(330,y0+16,[104,120,130],rows,header=['Decline code','What it means','What Yuno does'],header_style='dark',font_size=7,bold_first_col=True,zebra=True,max_h=200)
txt='**A decline on one provider is often an approval on the next.** That is the approval lever in this business case, and it grows with every provider Carry1st adds.'
h=E.bar_h(txt); E._bar(sb,363-h,txt)
sb.source_line('Yuno merchant data, about $17B annual volume across 50 merchants (internal); decline-code handling per docs.y.uno routing and retries. Carry1st uplift per provider is a Yuno estimate.')
sb.flush('data proof')
deck.set_notes(sid,'This is what we see across our own merchants: adding a second provider on the same payment rail recovers a meaningful share of soft declines, a third adds a little more, and beyond three the gain flattens. The mechanism is the decline code: a do-not-honor or a timeout on one route is often approved on another, while insufficient funds is better solved with a local method than a retry.')
# PCI row on proposal
prop=[x for x in P['slides'] if x['objectId'].startswith('n22r1')][0]
els={el['objectId']:(el,tr) for el,tr in E.elements(prop)}
req=[]
for src,new in (('n22r1_e046','pci_lab'),('n22r1_e047','pci_val')):
    req.append({'duplicateObject':{'objectId':src,'objectIds':{src:new}}})
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':req}).execute()
req=[]
for src,new,text in (('n22r1_e046','pci_lab','PCI token vault'),('n22r1_e047','pci_val','Included')):
    el,tr=els[src]; t=dict(tr); t['translateY']=tr['translateY']+11.55*E.PT; t['unit']='EMU'
    for k in ('scaleX','scaleY'): t.setdefault(k,1)
    for k in ('shearX','shearY'): t.setdefault(k,0)
    req+=[{'updatePageElementTransform':{'objectId':new,'transform':t,'applyMode':'ABSOLUTE'}},
          {'deleteText':{'objectId':new,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':new,'insertionIndex':0,'text':text}}]
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':req}).execute()
# position new slide after slide 7 and renumber
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'updateSlidesPosition':{'slideObjectIds':[sid],'insertionIndex':7}}]}).execute()
P=deck.fetch(); reqs=[]
for i,sl in enumerate(P['slides'],1):
    for el,tr in E.elements(sl):
        t=E.text_of(el).strip()
        if re.fullmatch(r'\d{1,2}',t) and E.geom(el,tr)[1]>=370 and t!=str(i):
            reqs+=[{'deleteText':{'objectId':el['objectId'],'textRange':{'type':'ALL'}}},{'insertText':{'objectId':el['objectId'],'insertionIndex':0,'text':str(i)}}]
if reqs: deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':reqs}).execute()
print('done, slides',len(P['slides']))
