import warnings; warnings.filterwarnings('ignore')
import gs_engine as E, re
PID='1D1HwXY1TRczJxtqDKWi_JgJT-cKqSXhuH-6rRn1BIQ4'; deck=E.Deck(PID); P=deck.fetch()
base=[x for x in P['slides'] if x['objectId']=='dproof_slide'][0]
sid='global_slide'
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'duplicateObject':{'objectId':base['objectId'],'objectIds':{base['objectId']:sid}}}]}).execute()
dup=[x for x in deck.fetch()['slides'] if x['objectId']==sid][0]
keep=[];kick=head=None
for el in dup['pageElements']:
    x,y,w,h=E.geom(el,el.get('transform',{})); t=E.text_of(el).strip()
    if t.startswith('WHY YUNO'): kick=el['objectId']; keep.append(kick)
    elif t.startswith('Across about'): head=el['objectId']; keep.append(head)
    elif 'image' in el and x>600 and y<45: keep.append(el['objectId'])
    elif re.fullmatch(r'\d{1,2}',t) and y>=370: keep.append(el['objectId'])
req=[{'deleteObject':{'objectId':el['objectId']}} for el in dup['pageElements'] if el['objectId'] not in keep]
req+=[{'deleteText':{'objectId':kick,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':kick,'insertionIndex':0,'text':'WHY YUNO · BEYOND LATIN AMERICA'}},
      {'deleteText':{'objectId':head,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':head,'insertionIndex':0,'text':'EBANX direct stops at its own 23 countries; the same Yuno integration opens 190+ countries, with redundancy in each.'}}]
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':req}).execute()
sb=E.SB(deck,sid,'glob')
y0=E.ZONE_Y+2
# left: blue stat panel
sb.rect(36,y0,236,248,fill=E.BLUE)
sb.text(50,y0+12,210,10,'ONE YUNO INTEGRATION OPENS',size=7.5,bold=True,color=E.PALE,ls=100)
stats=[('190+','countries supported'),('1,000+','payment methods, PSPs and fraud solutions'),('180+','currencies covered'),('16','offices, with local teams in São Paulo, Mexico City, Bogotá and Buenos Aires')]
yy=y0+30
for v,l in stats:
    sb.text(50,yy,210,26,v,size=22,bold=True,color=E.WHITE,ls=90)
    lh=E.text_h(l,7.5,210,110); sb.text(50,yy+26,210,lh,l,size=7.5,color=E.ONDARK,ls=110); yy+=26+lh+10
# right: comparison table
rows=[['Coverage','23 pay-in countries, one provider','190+ countries, through every provider Carry1st connects'],
      ['Providers per market','One: EBANX','EBANX plus other MoRs, local acquirers and methods'],
      ['Redundancy','None: a decline or an outage is a lost sale','Two or more routes per rail, with retries and failover'],
      ['Next markets','A new contract, onboarding and build each time','A connection on the same integration, live in days'],
      ['Where the Shop sells today','Africa, the Middle East and the US need other providers and other builds','The same checkout and dashboard for every storefront']]
sb.table(290,y0,[94,150,150],rows,header=['','EBANX direct','Through Yuno'],header_style='dark',font_size=7.5,bold_first_col=True,zebra=True,max_h=250)
txt='**Latin America is the first launch, not the last.** The integration Carry1st builds now is the one it keeps for every market that follows.'
h=E.bar_h(txt); E._bar(sb,363-h,txt)
sb.source_line('y.uno and y.uno/about (1,000+ payment methods, PSPs and fraud solutions; 190+ countries; 180+ currencies; 16 offices); EBANX docs, pay-in countries, read 15 Oct 2026.')
sb.flush('global')
deck.set_notes(sid,'EBANX is a strong Latin America provider, and it stays at the center of the launch. But it is one provider, in its own 23 countries. The Yuno integration Carry1st builds for Latin America is the same one that reaches 190+ countries and more than 1,000 payment methods, PSPs and fraud solutions, with redundancy in each market, so every next market, in Latin America or wherever the Shop sells, is a connection rather than a new project.')
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'updateSlidesPosition':{'slideObjectIds':[sid],'insertionIndex':5}}]}).execute()
P=deck.fetch(); reqs=[]
for i,sl in enumerate(P['slides'],1):
    for el,tr in E.elements(sl):
        t=E.text_of(el).strip()
        if re.fullmatch(r'\d{1,2}',t) and E.geom(el,tr)[1]>=370 and t!=str(i):
            reqs+=[{'deleteText':{'objectId':el['objectId'],'textRange':{'type':'ALL'}}},{'insertText':{'objectId':el['objectId'],'insertionIndex':0,'text':str(i)}}]
if reqs: deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':reqs}).execute()
print('slides',len(P['slides']))
