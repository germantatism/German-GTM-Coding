"""Pre-flight every image URL of one or more deck specs through the Slides API (createImage on a scratch slide), in batches, bisecting to
single URLs on failure. Writes logos/slides_bad.json {url: error}. Usage: python3 preflight_slides.py <presentation_id> <spec.json> [<spec.json> ...]"""
import json, sys, os, time, warnings; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'logos', 'slides_bad.json')
pid = sys.argv[1]; specs = sys.argv[2:]
urls = []
for sp in specs:
    S = json.load(open(sp))
    if S.get('logo_url'): urls.append(S['logo_url'])
    for s in S['slides']:
        for sec in s.get('sections', []):
            for ch in sec.get('chips', []):
                if ch.get('logo'): urls.append(ch['logo'])
urls = sorted(set(urls)); print(len(urls), 'distinct image urls')
known = json.load(open(OUT)) if os.path.exists(OUT) else {}
todo = [u for u in urls if u not in known]; print(len(todo), 'to test')
cr = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=cr, cache_discovery=False)
EMU = 12700
first = svc.presentations().get(presentationId=pid, fields='slides.objectId').execute()['slides'][0]['objectId']
sid = 'preflight_scratch_1'
svc.presentations().batchUpdate(presentationId=pid, body={'requests': [{'duplicateObject': {'objectId': first, 'objectIds': {first: sid}}}]}).execute()
def req(u, i):
    return {'createImage': {'url': u, 'elementProperties': {'pageObjectId': sid, 'size': {'width': {'magnitude': 20 * EMU, 'unit': 'EMU'}, 'height': {'magnitude': 20 * EMU, 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': (i % 30) * 22 * EMU, 'translateY': (i // 30) * 22 * EMU, 'unit': 'EMU'}}}}
def try_batch(batch):
    for attempt in range(3):
        try:
            svc.presentations().batchUpdate(presentationId=pid, body={'requests': [req(u, i) for i, u in enumerate(batch)]}).execute(); return None
        except HttpError as e:
            msg = str(e)
            if 'not found' in msg or 'Invalid requests' in msg or 'could not be fetched' in msg.lower() or 'image' in msg.lower():
                if attempt == 2: return msg
                time.sleep(2)
            else: raise
    return 'unknown'
bad = dict(known); ok = 0
for k in range(0, len(todo), 15):
    batch = todo[k:k + 15]; err = try_batch(batch)
    if err is None: ok += len(batch); continue
    for u in batch:
        e1 = try_batch([u])
        if e1: bad[u] = e1[:160]; print('BAD', u[:110], '|', e1[:90])
        else: ok += 1
    time.sleep(1)
svc.presentations().batchUpdate(presentationId=pid, body={'requests': [{'deleteObject': {'objectId': sid}}]}).execute()
json.dump(bad, open(OUT, 'w'), indent=1); print('ok', ok, 'bad', len(bad), '->', OUT)
