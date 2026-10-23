# -*- coding: utf-8 -*-
"""Fix pass 1 after the first build (23 Oct 2026):
  cover: delete the OnlyFans wordmark that survived (it sits inside the cover's element tree);
  slide 7: shorter title so it stays on one line;
  slide 8: tax_id row gets proper PII and Tokenized pills (duplicates of the account_holder / card_pan pills)."""
import json, time
import gs_lib as g
import content as C
from build_vault_deck import DECK, S
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_poshmark_prefix1_' + time.strftime('%H%M%S') + '.json', 'w'))
R = []
# ---- cover
cov = g.slide(P, S['cover'])
for e in g.walk(cov['pageElements']):
    if 'image' not in e: continue
    tr = e['transform']; x = tr['translateX'] / g.PT; y = tr['translateY'] / g.PT
    w = e['size']['width']['magnitude'] * tr.get('scaleX', 1) / g.PT; h = e['size']['height']['magnitude'] * tr.get('scaleY', 1) / g.PT
    print('cover img', e['objectId'], round(x), round(y), round(w), round(h))
    if e['objectId'] != 'posh_cover_logo' and 130 < x < 300 and y < 80 and w > 60:
        print('  -> delete', e['objectId']); R.append({'deleteObject': {'objectId': e['objectId']}})
# ---- slide 7 title (chrome element)
roles = g.chrome_ids(P, S['personal']); tid = next(k for k, v in roles.items() if v == 'title')
R += [{'deleteText': {'objectId': tid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': tid, 'insertionIndex': 0, 'text': C.OFFER['title']}}]
# ---- slide 8 tax_id pills: duplicate the account_holder PII pill (9_302) and the card_pan Tokenized pill (9_291) onto the tax_id row
des = S['design']; sl = g.slide(P, des)
def el(oid): return next(e for e in g.walk(sl['pageElements']) if e['objectId'] == oid)
row_y = el('h7c266de662ba1cf0_9_306')['transform']['translateY']          # tax_id label row
for src, new, ref in (('h7c266de662ba1cf0_9_302', 'posh_taxid_pii', 'h7c266de662ba1cf0_9_308'), ('h7c266de662ba1cf0_9_291', 'posh_taxid_tok', 'h7c266de662ba1cf0_9_309')):
    e = el(src); tr = dict(e['transform'])
    ref_tr = el(ref)['transform']
    R.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}})
    R.append({'updatePageElementTransform': {'objectId': new, 'applyMode': 'ABSOLUTE', 'transform': {
        'scaleX': tr.get('scaleX', 1), 'scaleY': tr.get('scaleY', 1), 'shearX': 0, 'shearY': 0,
        'translateX': tr['translateX'], 'translateY': ref_tr['translateY'], 'unit': 'EMU'}}})
    R.append({'deleteObject': {'objectId': ref}})
g.run(s, pid, R, 'fix1')
print('fix1 done')
