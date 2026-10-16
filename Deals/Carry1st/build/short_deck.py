# Builds the short Carry1st deck on a copy of the full deck (16 Oct 2026).
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E, json, re, copy
PID='1D1HwXY1TRczJxtqDKWi_JgJT-cKqSXhuH-6rRn1BIQ4'
deck=E.Deck(PID); P=deck.fetch(); S=P['slides']
def title(s): return ''.join(E.text_of(el) for el,_ in E.elements(s))
ids={k:None for k in ('cover','agenda','exec','needs','cmp','model','along','dash','story','six','pillars','team','logos','levers','impact','proposal')}
for s in S:
    t=title(s); o=s['objectId']
    if 'Carry1st in Latin America' in t and 'Yuno · 16' in t: ids['cover']=o
    elif 'AGENDA' in t: ids['agenda']=o
    elif 'EXECUTIVE SUMMARY' in t: ids['exec']=o
    elif 'WHAT CARRY1ST NEEDS' in t: ids['needs']=o
    elif 'THE COMPARISON' in t: ids['cmp']=o
    elif 'THE PROPOSED MODEL' in t: ids['model']=o
    elif 'ALONGSIDE EBANX' in t: ids['along']=o
    elif 'ONE DASHBOARD' in t: ids['dash']=o
    elif 'THE YUNO STORY' in t: ids['story']=o
    elif 'Six things' in t: ids['six']=o
    elif 'Four pillars' in t: ids['pillars']=o
    elif 'Run by builders' in t: ids['team']=o
    elif 'trusted by' in t: ids['logos']=o
    elif 'FIVE LEVERS' in t: ids['levers']=o
    elif 'TOTAL IMPACT' in t: ids['impact']=o
    elif 'PROPOSAL' in t and 'platform fee' in t: ids['proposal']=o
ids['cover']=S[0]['objectId']
print({k:bool(v) for k,v in ids.items()})
assert all(ids.values())
# assumptions text from the levers slide
lev=[s for s in S if s['objectId']==ids['levers']][0]
assump=[E.text_of(el).strip() for el,_ in E.elements(lev) if E.text_of(el).strip().startswith('Assumptions')][0]
d=json.load(open('deck_spec.json'))
W=copy.deepcopy([x for x in d['slides'] if x['id']=='bc-why'][-1])
C=copy.deepcopy([x for x in d['slides'] if x['id']=='options'][-1])
C.pop('tag',None)
C['options']=[C['options'][0],C['options'][2]]
for r in C['rows']: r['cells']=[r['cells'][0],r['cells'][2]]
last=C['rows'][-1]; last['label']='Time to launch, and later'; last['sub']='local presence later'
last['cells'][0]['text']='EBANX onboarding sets the pace; local presence later is a new build.'
last['cells'][1]['text']='Same onboarding; Yuno setup in days; local presence later is a connection.'
C['rows'][1]['cells'][0]['text']='All five once EBANX enables each; Bolivia cash only.'
C['footer']=[{'label':'Rows closed'},{'value':'0 of 6'},{'value':'6 of 6'}]
C['source']='EBANX docs (api-operability, pay-in guide, Bolivia and Argentina overviews) and status.ebanx.com, read 15 Oct 2026; docs.y.uno connections, routing, monitors, tokens. Yuno setup time is a Yuno estimate.'
C['notes']='One EBANX integration and one agreement can switch on all five countries, and we say so. What going direct cannot give is a second rail: retries and failover when EBANX declines or drops, a real alternative to negotiate price against, the methods EBANX does not carry, and new providers or local presence without a new build.'
for s in (C,W): E.render_one(E.DryDeck(),s,'dry',4,'')
newC=E.render_one(deck,C,'sdcmp',4,''); newW=E.render_one(deck,W,'sdwhy',6,'')
# exec title, no numbers
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'replaceAllText':{'containsText':{'text':'Through Yuno, EBANX plus local rails per market costs less than EBANX direct at run rate, and pays back in month one.','matchCase':True},'replaceText':'Through Yuno, Carry1st launches on EBANX plus every rail each market needs: more sales approved, leverage on price, one integration.'}}]}).execute()
# total impact: replace takeaways with the assumptions box
imp=[s for s in deck.fetch()['slides'] if s['objectId']==ids['impact']][0]
els=E.elements(imp); dele=[]; 
for el,tr in els:
    x,y,w,h=E.geom(el,tr); t=E.text_of(el).strip()
    if 300<=y<=360 and t and not t.startswith('Yuno cost') and not re.fullmatch(r'\d+',t): dele.append(el['objectId'])
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'deleteObject':{'objectId':o}} for o in dele]}).execute()
sb=E.SB(deck,ids['impact'],'sdassump')
body=assump.replace('Assumptions ','',1)
th=E.text_h('**Assumptions** '+body,7,W0-24 if False else 624,112)
y=362-th-12; sb.rect(36,y,648,th+12,fill=E.PANEL2); sb.text(48,y+6,624,th,'**Assumptions** '+body,size=7,color=E.BODY3,ls=112); sb.flush('assumptions')
print('deleted takeaway elements',len(dele),'assumptions box at y',round(y))
# delete and reorder
for k in ('agenda','model','six','pillars','levers','cmp'): pass
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'deleteObject':{'objectId':ids[k]}} for k in ('agenda','model','six','pillars','levers','cmp')]}).execute()
order=[ids['cover'],ids['exec'],ids['needs'],newC,ids['along'],newW,ids['impact'],ids['proposal'],ids['story'],ids['dash'],ids['team'],ids['logos']]
deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':[{'updateSlidesPosition':{'slideObjectIds':order,'insertionIndex':0}}]}).execute()
P=deck.fetch(); reqs=[]
for i,sl in enumerate(P['slides'],1):
    for el,tr in E.elements(sl):
        t=E.text_of(el).strip()
        if re.fullmatch(r'\d{1,2}',t) and E.geom(el,tr)[1]>=370 and t!=str(i):
            reqs+=[{'deleteText':{'objectId':el['objectId'],'textRange':{'type':'ALL'}}},{'insertText':{'objectId':el['objectId'],'insertionIndex':0,'text':str(i)}}]
if reqs: deck.svc.presentations().batchUpdate(presentationId=PID, body={'requests':reqs}).execute()
print('slides',len(P['slides']))
