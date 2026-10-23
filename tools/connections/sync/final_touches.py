import os, sys, json, time
from google.oauth2 import service_account
from googleapiclient.discovery import build
SP = os.path.dirname(os.path.abspath(__file__)); ROOT = '/Users/germantatis/Desktop/GTMCoding'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive'])
slides = build('slides', 'v1', credentials=creds, cache_discovery=False); drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
MOON_ID = '1DVDaujX4mYhF79wDLsiXmiafHtOdbKuB'
try:
    drive.permissions().create(fileId=MOON_ID, body={'type': 'anyone', 'role': 'reader'}, supportsAllDrives=True).execute(); print('moonactive png: anyone-reader set')
except Exception as e: print('permission:', str(e)[:200])
MOON_URL = f'https://drive.google.com/uc?export=download&id={MOON_ID}'
def run(pid, reqs, label):
    if not reqs: return
    for attempt in range(6):
        try: slides.presentations().batchUpdate(presentationId=pid, body={'requests': reqs}).execute(); print(f'  {label}: {len(reqs)} requests'); return
        except Exception as e:
            if '429' in str(e): time.sleep(65)
            else: raise
def text_of(e):
    sh = e.get('shape', {}); return ''.join(te.get('textRun', {}).get('content', '') for te in sh.get('text', {}).get('textElements', []))
wcfg = json.load(open(f'{ROOT}/Deals/Waymo/build/config.json')); hcfg = json.load(open(f'{ROOT}/Deals/HBO Max/build/config.json'))
WPID, W6PID = wcfg['presentation_id'], wcfg['presentation_id_v6']; HPID, H1PID = hcfg['presentation_id'], hcfg['presentation_id_v1']
print('waymo', WPID, 'from', W6PID, '| hbo', HPID, 'from', H1PID)
# ---- Waymo: white Moonactive, cover logo size as v6
W6 = json.load(open(os.path.join(SP, 'v6_full.json'))); W7 = slides.presentations().get(presentationId=WPID).execute()
moon6 = [e for e in W6['slides'][5]['pageElements'] if e.get('image') and 'moonactive' in e['image'].get('sourceUrl', '')][0]
logos7 = [s for s in W7['slides'] if s['objectId'].startswith('n05_')][0]
reqs = [{'deleteObject': {'objectId': e['objectId']}} for e in logos7['pageElements'] if e['objectId'] in ('moon_plain', 'moon_logo')]
reqs.append({'createImage': {'objectId': 'moon_white', 'url': MOON_URL, 'elementProperties': {'pageObjectId': logos7['objectId'], 'size': moon6['size'], 'transform': moon6['transform']}}})
cover6 = [e for e in W6['slides'][0]['pageElements'] if e['objectId'] == 'n01_e001'][0]
reqs.append({'updatePageElementTransform': {'objectId': 'n01_e001', 'transform': cover6['transform'], 'applyMode': 'ABSOLUTE'}})
run(WPID, reqs, 'waymo moonactive + cover logo')
# ---- HBO: Moonactive, team widen, cover diagnosis
H1 = slides.presentations().get(presentationId=H1PID).execute(); H2 = slides.presentations().get(presentationId=HPID).execute()
json.dump(H1, open(os.path.join(SP, 'hbo_v1_full.json'), 'w'))
moon1 = [e for e in H1['slides'][5]['pageElements'] if e.get('image') and 'moonactive' in e['image'].get('sourceUrl', '')]
mt = (moon1[0] if moon1 else moon6)
logosH = [s for s in H2['slides'] if s['objectId'].startswith('n05_')][0]
kr = [e for e in logosH['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_0')]
reqs = [{'deleteObject': {'objectId': k['objectId']}} for k in kr]
reqs.append({'createImage': {'objectId': 'moon_white_h', 'url': MOON_URL, 'elementProperties': {'pageObjectId': logosH['objectId'], 'size': mt['size'], 'transform': mt['transform']}}})
teamH = [s for s in H2['slides'] if s['objectId'].startswith('n06_')][0]
for e in teamH['pageElements']:
    if not e.get('shape', {}).get('text') or text_of(e).startswith('Run by builders'): continue
    tf = dict(e['transform']); w = e['size']['width']['magnitude'] * tf.get('scaleX', 1)
    tf['scaleX'] = tf.get('scaleX', 1) * 1.22; tf['translateX'] = tf.get('translateX', 0) - 0.11 * w
    reqs.append({'updatePageElementTransform': {'objectId': e['objectId'], 'transform': tf, 'applyMode': 'ABSOLUTE'}})
run(HPID, reqs, 'hbo moonactive + team widen')
print('--- HBO v1 cover elements')
for e in H1['slides'][0]['pageElements']:
    kind = 'img' if e.get('image') else 'group' if e.get('elementGroup') else e.get('shape', {}).get('shapeType')
    print('  v1', kind, e['objectId'], {k: round(v, 2) for k, v in e['transform'].items() if k != 'unit'}, e.get('size', {}).get('width', {}).get('magnitude'), (e.get('image') or {}).get('sourceUrl', '')[:50], repr(text_of(e).strip()[:20]) if e.get('shape') else '', [('img' if c.get('image') else c.get('shape', {}).get('shapeType')) for c in e.get('elementGroup', {}).get('children', [])])
print('--- HBO v2 cover elements now')
for e in H2['slides'][0]['pageElements']:
    kind = 'img' if e.get('image') else 'group' if e.get('elementGroup') else e.get('shape', {}).get('shapeType')
    print('  v2', kind, e['objectId'], {k: round(v, 2) for k, v in e['transform'].items() if k != 'unit'}, e.get('size', {}).get('width', {}).get('magnitude'), (e.get('image') or {}).get('sourceUrl', '')[:50], repr(text_of(e).strip()[:20]) if e.get('shape') else '')
