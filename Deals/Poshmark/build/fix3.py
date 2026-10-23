# -*- coding: utf-8 -*-
"""Fix pass 3 (23 Oct 2026): on slide 8 the pill backgrounds are baked into each row's background image, so the duplicated
text shapes rendered without a pill. Replace them with real filled pills (ROUND_RECTANGLE) on the tax_id row."""
import json, time
import gs_lib as g
from gs_lib import Page, LAV, BLUE, WHITE
from build_vault_deck import DECK, S
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_poshmark_prefix3_' + time.strftime('%H%M%S') + '.json', 'w'))
sl = g.slide(P, S['design']); ids = {e['objectId'] for e in g.walk(sl['pageElements'])}
R = [{'deleteObject': {'objectId': o}} for o in ('posh_taxid_pii', 'posh_taxid_tok') if o in ids]
lab = next(e for e in g.walk(sl['pageElements']) if e['objectId'] == 'h7c266de662ba1cf0_9_306')
y = lab['transform']['translateY'] / g.PT - 1          # pills sit 1 pt above their row label
p = Page(S['design'], prefix='posh_taxid')
p.pill(406, y, 27, 'PII', fill=LAV, color=BLUE, size=8, h=14)
p.pill(479, y, 53, 'Tokenized', fill=BLUE, color=WHITE, size=8, h=14)
g.run(s, pid, R + p.R, 'fix3')
import urllib.request, os
os.makedirs('thumbs_v3', exist_ok=True)
t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=S['design'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(t['contentUrl'], 'thumbs_v3/s08.png'); print('fix3 done, thumb s08')
