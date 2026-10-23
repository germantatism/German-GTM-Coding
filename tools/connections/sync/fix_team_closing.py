import os, sys, json, copy
sys.argv=[sys.argv[0]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0])
# team: wipe clone and redo with transparent backgrounds
team = [s for s in D if s['objectId'].startswith('n06_')][0]
run([{'deleteObject': {'objectId': e['objectId']}} for e in team['pageElements']], 'team wipe')
reqs = clone_elements(S[4]['pageElements'], team['objectId'])
for i in range(0, len(reqs), 120): run(reqs[i:i+120], f'team clone {i}')
# closing body: recreate wider, flush left
cl = [s for s in D if s['objectId'] == 'closing_v7'][0]
body = [e for e in cl['pageElements'] if e.get('shape', {}).get('text') and text_of(e).startswith('German Tatis')][0]
src_body = [e for e in S[79]['pageElements'] if e.get('shape', {}).get('placeholder', {}).get('type') == 'BODY'][0]
e2 = copy.deepcopy(src_body); e2['shape'].pop('placeholder', None); e2['transform']['scaleX'] = 1.9
for te in e2['shape']['text']['textElements']:
    if 'paragraphMarker' in te:
        st = te['paragraphMarker'].get('style', {}); st['indentStart'] = {'magnitude': 0, 'unit': 'PT'}; st['indentFirstLine'] = {'magnitude': 0, 'unit': 'PT'}
    if 'textRun' in te:
        st = te['textRun'].get('style', {}); st['foregroundColor'] = {'opaqueColor': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}
e2['shape']['shapeProperties']['autofit'] = {'autofitType': 'NONE'}
oid, reqs = clone_shape(e2, 'closing_v7')
run([{'deleteObject': {'objectId': body['objectId']}}] + reqs, 'closing body')
# moonactive white
logos = [s for s in D if s['objectId'].startswith('n05_')][0]
kr = [e for e in logos['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_0')][0]
run([{'updateImageProperties': {'objectId': kr['objectId'], 'imageProperties': {'brightness': 1.0}, 'fields': 'brightness'}}], 'moonactive brightness')
print('done')
