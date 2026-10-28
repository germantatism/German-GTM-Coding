# -*- coding: utf-8 -*-
"""v2 fix 14 (German, 27-oct-2026): plain headline on the pricing slide."""
import sys, urllib.request
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
import v2
svc = service(); P = svc.presentations().get(presentationId=v2.PID).execute()
sl = next(x for x in P['slides'] if any(v2.txt(e) == 'RATE PER SUCCESSFUL TRANSACTION' for e in x['pageElements']))
svc.presentations().batchUpdate(presentationId=v2.PID, body={'requests': [{'replaceAllText': {
    'containsText': {'text': "Usage only, no platform fee", 'matchCase': True}, 'replaceText': "Pricing", 'pageObjectIds': [sl['objectId']]}}]}).execute()
r = svc.presentations().pages().getThumbnail(presentationId=v2.PID, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{v2.WORK}/f16_price.png'); print('ok')
