# -*- coding: utf-8 -*-
"""v2 fix 10 (German, 27-oct-2026): middle panel reorganized: today hero on top, full-tranche costs below. Pricing and 'What's included' slides redrawn, pricing headline renamed."""
import sys, urllib.request
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
import v2
svc = service(); P = svc.presentations().get(presentationId=v2.PID).execute()
for marker, fn, name in [('RATE PER SUCCESSFUL TRANSACTION', v2.price, 'f12_price'), ('INCLUDED AT NO EXTRA COST', v2.terms, 'f12_terms')]:
    sl = next(x for x in P['slides'] if any(v2.txt(e) == marker for e in x['pageElements']))
    reqs = [{'deleteObject': {'objectId': e['objectId']}} for e in sl['pageElements'] if e['objectId'][:2] in ('r_', 't_', 'l_')]
    s = Slide(sl['objectId']); fn(s); reqs += s.reqs
    if fn is v2.price:
        reqs.append({'replaceAllText': {'containsText': {'text': 'Platform fee plus usage', 'matchCase': True},
                                        'replaceText': 'Usage only, no platform fee', 'pageObjectIds': [sl['objectId']]}})
    svc.presentations().batchUpdate(presentationId=v2.PID, body={'requests': reqs}).execute()
    r = svc.presentations().pages().getThumbnail(presentationId=v2.PID, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f'{v2.WORK}/{name}.png'); print('ok', name, len(reqs))
