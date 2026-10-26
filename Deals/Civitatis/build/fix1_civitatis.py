# -*- coding: utf-8 -*-
"""Second pass on the copy: L4 metric on one line ('7 → 1') and a one-line title on slide 13."""
import sys, os, json, urllib.request, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run
from google.oauth2 import service_account
from googleapiclient.discovery import build
HERE = os.path.dirname(os.path.abspath(__file__)); PID = sys.argv[1]
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
idx = {el['objectId']: el for s in P['slides'] for el, tr in elements(s)}
reqs = []
reqs += replace_requests(idx['p14_i5669'], '7 → 1')
reqs += replace_requests(idx['p14_i5618'], 'Cinco palancas: aprobación y métodos locales son las dos más grandes')
run(svc, PID, reqs, label='fix1')
r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId='p14', thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{HERE}/thumbs/bc_13.png'); print('thumb 13 refreshed')
