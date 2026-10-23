"""post_build_waymo.py : after `gs_engine.py build --final` and `vault_slides.py <pid>`, re-apply German's reviewed customisations to the new Waymo deck.
Reference deck = the v6 copy (intro, team, closing as reviewed). Usage: python3 post_build_waymo.py <new_pid> [<ref_pid>]"""
import os, sys, json, time, copy
HERE = os.path.dirname(os.path.abspath(__file__))
NEW = sys.argv[1]; REF = sys.argv[2] if len(sys.argv) > 2 else '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'
prelude = open(os.path.join(HERE, 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
prelude = prelude.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", f"SRC = '{REF}'; DST = '{NEW}'")
sys.argv = [sys.argv[0]]; exec(prelude)
MOON_URL = 'https://drive.google.com/uc?export=download&id=1DVDaujX4mYhF79wDLsiXmiafHtOdbKuB'
print('ref', len(S), 'slides; new', len(D), 'slides')
# 1. story: kicker off, $30B -> $100B
k = find(D[2], lambda e: text_of(e).strip() == 'THE YUNO STORY')
run(([{'deleteObject': {'objectId': k[0]['objectId']}}] if k else []) + [{'replaceAllText': {'containsText': {'text': '30', 'matchCase': True}, 'replaceText': '100', 'pageObjectIds': [sid(2)]}}], 'story')
# 2. pillars kicker off
k = find(D[3], lambda e: text_of(e).strip() == 'ABOUT YUNO · PLATFORM'); run([{'deleteObject': {'objectId': k[0]['objectId']}}] if k else [], 'pillars')
# 3. trusted: kicker off, page number 6, Kraken -> white Moonactive at the reference position
k = find(D[4], lambda e: text_of(e).strip() == 'WHY YUNO?'); pn = find(D[4], lambda e: text_of(e).strip() == '5')
ref_moon = [e for e in S[5]['pageElements'] if e.get('image') and ('moonactive' in e['image'].get('sourceUrl', '') or '1DVDaujX' in e['image'].get('sourceUrl', ''))]
kraken = [e for e in D[4]['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_0')]
reqs = [{'deleteObject': {'objectId': x['objectId']}} for x in k + kraken]
if pn: reqs += [{'deleteText': {'objectId': pn[0]['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': pn[0]['objectId'], 'insertionIndex': 0, 'text': '6'}}]
if ref_moon: reqs.append({'createImage': {'objectId': 'moon_white', 'url': MOON_URL, 'elementProperties': {'pageObjectId': sid(4), 'size': ref_moon[0]['size'], 'transform': ref_moon[0]['transform']}}})
run(reqs, 'trusted')
# 4. team: wipe, clone from the reference (index 4), widen text boxes 22%, move before the logo wall
n06 = sid(5)
run([{'deleteObject': {'objectId': e['objectId']}} for e in D[5].get('pageElements', [])], 'team wipe')
bg = S[4].get('pageProperties', {}).get('pageBackgroundFill')
reqs = [{'updatePageProperties': {'objectId': n06, 'pageProperties': {'pageBackgroundFill': bg}, 'fields': 'pageBackgroundFill'}}] if bg else []
reqs += clone_elements(S[4]['pageElements'], n06)
for i in range(0, len(reqs), 120): run(reqs[i:i+120], f'team clone {i}')
team = svc.presentations().get(presentationId=DST, fields='slides(objectId,pageElements)').execute()['slides'][5]
reqs = []
for e in team.get('pageElements', []):
    if not e.get('shape', {}).get('text') or text_of(e).startswith('Run by builders'): continue
    tf = dict(e['transform']); w = e['size']['width']['magnitude'] * tf.get('scaleX', 1)
    tf['scaleX'] = tf.get('scaleX', 1) * 1.22; tf['translateX'] = tf.get('translateX', 0) - 0.11 * w
    reqs.append({'updatePageElementTransform': {'objectId': e['objectId'], 'transform': tf, 'applyMode': 'ABSOLUTE'}})
reqs.append({'updateSlidesPosition': {'slideObjectIds': [n06], 'insertionIndex': 4}})
run(reqs, 'team widen + order')
# 5. closing from the reference closing (last slide), then drop the engine next-steps slide
cs = S[len(S) - 1]; lay = {l['objectId']: l for l in src['layouts']}.get(cs['slideProperties'].get('layoutObjectId'), {})
mas = {m['objectId']: m for m in src['masters']}.get(lay.get('layoutProperties', {}).get('masterObjectId'), {})
def ph_style(layout, ptype):
    for e in layout.get('pageElements', []):
        if e.get('shape', {}).get('placeholder', {}).get('type') == ptype:
            for te in e['shape'].get('text', {}).get('textElements', []):
                if 'textRun' in te: return te['textRun'].get('style', {})
    return {}
cl = 'closing_sync'
run([{'createSlide': {'objectId': cl, 'insertionIndex': len(D), 'slideLayoutReference': {'layoutId': 'g3f77215683c_2_1907'}}}], 'closing create')
dark = None
for c in mas.get('masterProperties', {}).get('colorScheme', {}).get('colors', []):
    if c.get('type') == 'DARK1': dark = c.get('color')
reqs = [{'updatePageProperties': {'objectId': cl, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': dark or {}}, 'alpha': 1}}}, 'fields': 'pageBackgroundFill'}}]
reqs += clone_elements([e for e in lay.get('pageElements', []) if not e.get('shape', {}).get('placeholder')], cl)
for e in cs['pageElements']:
    ph = e.get('shape', {}).get('placeholder', {}).get('type')
    if ph in ('TITLE', 'BODY'):
        base = ph_style(lay, ph); e2 = copy.deepcopy(e); e2['shape'].pop('placeholder', None)
        for te in e2['shape']['text']['textElements']:
            if 'textRun' in te:
                st = dict(base); st.update(te['textRun'].get('style', {})); st['foregroundColor'] = {'opaqueColor': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}; te['textRun']['style'] = st
            if 'paragraphMarker' in te and ph == 'BODY':
                st = te['paragraphMarker'].get('style', {}); st['indentStart'] = {'magnitude': 0, 'unit': 'PT'}; st['indentFirstLine'] = {'magnitude': 0, 'unit': 'PT'}
        e2['shape']['shapeProperties']['autofit'] = {'autofitType': 'NONE'}
        if ph == 'BODY': e2['transform']['scaleX'] = max(e2['transform'].get('scaleX', 1), 1.9)
        reqs += clone_shape(e2, cl)[1]
    elif e.get('image'): reqs += clone_image(e, cl, url=e['image'].get('sourceUrl') or None)[1]
    elif e.get('shape'): reqs += clone_shape(e, cl)[1]
    elif e.get('elementGroup'): reqs += clone_elements([e], cl)
run(reqs, 'closing content')
last = D[len(D) - 1]
if any(text_of(e).strip() == 'NEXT STEP' for e in last.get('pageElements', [])): run([{'deleteObject': {'objectId': last['objectId']}}], 'drop next steps')
# 6. dividers and vault wording
d01, d02, d03 = sid(1), sid(6), sid(11)
reqs = [{'replaceAllText': {'containsText': {'text': '03 CONNECTIONS AND PAYMENT METHODS', 'matchCase': True}, 'replaceText': '03 CONNECTIONS AND PAYMENT METHODS IN TARGET MARKETS', 'pageObjectIds': [d01, d02, d03]}},
        {'replaceAllText': {'containsText': {'text': 'The token vault', 'matchCase': True}, 'replaceText': 'The Token Vault', 'pageObjectIds': [d02]}},
        {'replaceAllText': {'containsText': {'text': 'Connections and payment methods', 'matchCase': True}, 'replaceText': 'Connections and payment methods in target markets', 'pageObjectIds': [d03]}}]
for i, start in [(1, 'What we do, the platform'), (6, 'A PCI DSS Level 1 vault you can use'), (11, 'Who is live through Yuno')]:
    for e in find(D[i], lambda e: text_of(e).strip().startswith(start)): reqs.append({'deleteObject': {'objectId': e['objectId']}})
run(reqs, 'dividers')
wv = {s['objectId']: s for s in D}
reqs = [{'replaceAllText': {'containsText': {'text': 'London 2026', 'matchCase': True}, 'replaceText': 'London', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Tokyo, Munich 2027', 'matchCase': True}, 'replaceText': 'Tokyo, Munich', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Singapore, Toronto 2028', 'matchCase': True}, 'replaceText': 'Singapore, Toronto', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Tokenisation', 'matchCase': True}, 'replaceText': 'Tokenization', 'pageObjectIds': ['wv_summary']}},
        {'replaceAllText': {'containsText': {'text': 'One token on both PSPs, with routing', 'matchCase': True}, 'replaceText': 'One token on both PSPs (and future), with routing', 'pageObjectIds': ['wv_summary']}}]
for e in find(wv['wv_summary'], lambda e: text_of(e).strip() == 'INCLUDED'): reqs.append({'deleteObject': {'objectId': e['objectId']}})
for e in find(wv['wv_versus'], lambda e: text_of(e).strip().startswith('Yuno leads on 4')): reqs.append({'deleteObject': {'objectId': e['objectId']}})
run(reqs, 'vault wording')
# 7. cover wordmark sized as the reference
ref_cover = [e for e in S[0]['pageElements'] if e['objectId'] == 'n01_e001']
if ref_cover: run([{'updatePageElementTransform': {'objectId': 'n01_e001', 'transform': ref_cover[0]['transform'], 'applyMode': 'ABSOLUTE'}}], 'cover logo')
final = svc.presentations().get(presentationId=DST, fields='slides.objectId').execute()['slides']
print('final slides', len(final), [s['objectId'][:12] for s in final[:13]], final[-1]['objectId'])
