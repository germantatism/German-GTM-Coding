import os, sys, json
sys.argv=[sys.argv[0]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0])
team7 = [s for s in D if s['objectId'].startswith('n06_')][0]; team6 = S[4]
def runs(e): return [(te['textRun']['content'], te['textRun'].get('style', {})) for te in e['shape']['text']['textElements'] if 'textRun' in te]
def by_text(slide):
    out = {}
    for e in slide['pageElements']:
        if e.get('shape', {}).get('text'): out[text_of(e).strip()] = e
    return out
b6, b7 = by_text(team6), by_text(team7)
for t in ['Juan Pablo Ortega', 'CRO · US']:
    r6, r7 = runs(b6[t]), runs(b7[t])
    for (c6, s6), (c7, s7) in zip(r6, r7):
        diff = {k: (s6.get(k), s7.get(k)) for k in set(s6) | set(s7) if s6.get(k) != s7.get(k)}
        print(t, repr(c6[:15]), 'style diff:', diff)
    p6 = b6[t]['shape'].get('shapeProperties', {}); p7 = b7[t]['shape'].get('shapeProperties', {})
    print('  props diff:', {k: (p6.get(k), p7.get(k)) for k in set(p6) | set(p7) if p6.get(k) != p7.get(k)})
# widen every text box except the title by 22% around its centre
reqs = []
for e in team7['pageElements']:
    if not e.get('shape', {}).get('text') or text_of(e).startswith('Run by builders'): continue
    tf = dict(e['transform']); w = e['size']['width']['magnitude'] * tf.get('scaleX', 1)
    tf['scaleX'] = tf.get('scaleX', 1) * 1.22; tf['translateX'] = tf.get('translateX', 0) - 0.11 * w
    reqs.append({'updatePageElementTransform': {'objectId': e['objectId'], 'transform': tf, 'applyMode': 'ABSOLUTE'}})
run(reqs, 'widen team boxes')
