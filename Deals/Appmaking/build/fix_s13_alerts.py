# -*- coding: utf-8 -*-
"""Appmaking deck, slide 13: name Ethoca on the $14/alert line and add the Verifi RDR line.
Requires a valid Slides token at ~/.config/yuno-slides/token.json (see auth_slides.py).
Run:  python3 Deals/Appmaking/build/fix_s13_alerts.py [--dry]
"""
import sys, json, urllib.request, os
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of, replace_requests
PID='1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc'
S13='g3f6c0558646_0_35'
DRY='--dry' in sys.argv
OUT=os.path.dirname(os.path.abspath(__file__))

NEW_TITLE='SUBSCRIPTIONS ENGINE & PRE-CHARGEBACK ALERTS'
NEW_BODY=('First $50,000 processed free, then $0.05 per transaction through the engine\n'
          'Ethoca alerts, Mastercard network: $14 for every alert\n'
          'Verifi RDR: enrolled through your PSP; cases surface in Yuno flagged as pre-dispute')

svc=service(); P=svc.presentations().get(presentationId=PID).execute()
s=[x for x in P['slides'] if x['objectId']==S13][0]
els=elements(s)
def find(pred):
    m=[el for el,tr in els if pred(text_of(el).strip())]
    if len(m)!=1: raise SystemExit(f"expected 1 match, got {len(m)}: {[text_of(e)[:50] for e in m]}")
    return m[0]
title=find(lambda t:t.upper().startswith('SUBSCRIPTIONS ENGINE'))
body=find(lambda t:t.startswith('First $50,000') or '$14 for every alert' in t)
print('title el:',title['objectId'],repr(text_of(title).strip()))
print('body el :',body['objectId'],repr(text_of(body).strip()))
# if the two bullets live in separate shapes, edit only the $14 one and append RDR as a new paragraph there
if 'First $50,000' not in text_of(body):
    NEW_BODY='\n'.join(NEW_BODY.split('\n')[1:])
R=replace_requests(title,NEW_TITLE)+replace_requests(body,NEW_BODY)
if DRY:
    print(json.dumps(R,indent=1)[:3000]); raise SystemExit('dry run, nothing applied')
svc.presentations().batchUpdate(presentationId=PID,body={'requests':R}).execute()
print('applied',len(R),'requests')
Q=svc.presentations().get(presentationId=PID).execute()
n=[i for i,x in enumerate(Q['slides'],1) if x['objectId']==S13][0]
r=svc.presentations().pages().getThumbnail(presentationId=PID,pageObjectId=S13,thumbnailProperties_thumbnailSize='LARGE').execute()
png=os.path.join(OUT,f'appmaking-s{n:02d}-alerts-fixed.png'); urllib.request.urlretrieve(r['contentUrl'],png)
print('thumbnail:',png,'  -> check the box does not overflow; if it does, shrink the body font one step or grow the box')
