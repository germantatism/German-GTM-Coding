import json, time
import gs_lib as g
import content as C
from build_vault_deck import DECK, S, SKY_LOGO, draw_problem
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_skydance_prefix1_' + time.strftime('%H%M%S') + '.json', 'w'))
R = []
# cover: report images, remove the OnlyFans wordmark if still there, add Skydance if missing
cov = g.slide(P, S['cover'])
imgs = [e for e in cov['pageElements'] if 'image' in e]
for e in imgs:
    tr = e['transform']; print('cover img', e['objectId'], round(tr['translateX']/g.PT), round(tr['translateY']/g.PT), round(e['size']['width']['magnitude']*tr.get('scaleX',1)/g.PT), round(e['size']['height']['magnitude']*tr.get('scaleY',1)/g.PT))
have_sky = any(e['objectId'] == 'sky_cover_logo' for e in imgs)
old = [e for e in imgs if e['objectId'] != 'sky_cover_logo' and 120 < e['transform']['translateX']/g.PT < 200 and e['transform']['translateY']/g.PT < 80]
for e in old: R.append({'deleteObject': {'objectId': e['objectId']}})
if not have_sky:
    x, y, bw, bh = 157, 53, 131, 23
    asp = 640/109; w = min(bw, bh*asp); h = w/asp
    R.append({'createImage': {'objectId': 'sky_cover_logo', 'url': SKY_LOGO, 'elementProperties': {'pageObjectId': S['cover'],
        'size': {'width': {'magnitude': w*g.PT, 'unit': 'EMU'}, 'height': {'magnitude': h*g.PT, 'unit': 'EMU'}},
        'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x*g.PT, 'translateY': (y + (bh-h)/2)*g.PT, 'unit': 'EMU'}}}})
# exec proposal
g.set_text_id(P, S['exec'], 'of_es1_v2_026', C.EXEC['of_es1_v2_026'], R)
# network tokens title + band
for oid in ('h7c266de662ba1cf0_9_210', 'h7c266de662ba1cf0_9_235'): g.set_text_id(P, S['nt'], oid, C.NT[oid], R)
# design slide by id (correct this time)
for oid in ('h7c266de662ba1cf0_9_251', 'h7c266de662ba1cf0_9_265', 'h7c266de662ba1cf0_9_278', 'h7c266de662ba1cf0_9_284'):
    g.set_text_id(P, S['design'], oid, C.DESIGN[oid], R)
# recurring title (chrome title element)
roles = g.chrome_ids(P, S['personal']); tid = next(k for k, v in roles.items() if v == 'title')
R += [{'deleteText': {'objectId': tid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': tid, 'insertionIndex': 0, 'text': C.RECUR['title']}}]
g.run(s, pid, R, 'fix1 text')
# problem slide: redraw body with the shortened copy
P = s.presentations().get(presentationId=pid).execute()
p = g.clear_body(s, pid, P, S['problem'], kicker=C.PROBLEM['kicker'], title=C.PROBLEM['title'])
draw_problem(p); g.run(s, pid, p.R, 'problem redraw')
print('fix1 done')
