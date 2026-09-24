# -*- coding: utf-8 -*-
"""Review fixes for the live deck "Business Case Yango + Yuno" (proposal section, slides 34 to 37) via the Slides API.

Auth: service account key ~/.config/gsuite/sa.json (gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com).
The deck must be shared with that account as Editor first (Slides > Share; the claude.ai Drive connector cannot do it).

Dry run by default: prints the inventory (stray "$ 75.56" boxes, every text match) and changes nothing.

  python3 apply_review_fixes_2026-09-24.py                       # inventory only
  python3 apply_review_fixes_2026-09-24.py --thumbs out_dir      # + PNG thumbnails of slides 2, 31, 34 to 37 for visual QA
  python3 apply_review_fixes_2026-09-24.py --apply --delete-stray            # delete the hidden "$ 75.56" boxes
  python3 apply_review_fixes_2026-09-24.py --apply --min keep                # "Minimum monthly invoice: $25,000, platform fee included."
  python3 apply_review_fixes_2026-09-24.py --apply --min drop                # remove the minimum line entirely
  python3 apply_review_fixes_2026-09-24.py --apply --ramp                    # slide 37 intro: Colombia alone / Colombia + Peru figures
  python3 apply_review_fixes_2026-09-24.py --apply --source                  # slide 31 source line: July -> shared August 2026
  python3 apply_review_fixes_2026-09-24.py --apply --recon pending           # reconciliation back to "Pending review"

Numbers: build/yango_pricing_model.py (LIVE section). Review: ../yango-proposal-review-2026-09-24.md
"""
import argparse, os, sys, urllib.request
from google.oauth2 import service_account
from googleapiclient.discovery import build

PID = '1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw'
SA_KEY = os.path.expanduser('~/.config/gsuite/sa.json')
STRAY = '75.56'

ap = argparse.ArgumentParser()
ap.add_argument('--pid', default=PID)
ap.add_argument('--apply', action='store_true', help='execute the requests (default: dry run)')
ap.add_argument('--delete-stray', action='store_true', help='delete every element whose whole text is the stray "$ 75.56"')
ap.add_argument('--min', choices=['keep', 'drop'], help='keep = reword the $25,000 minimum clearly; drop = remove the line')
ap.add_argument('--ramp', action='store_true', help='slide 37 intro: add Colombia-alone and Colombia+Peru monthly figures')
ap.add_argument('--source', action='store_true', help='slide 31 source line: "July 2026" -> "July 2026, shared August 2026"')
ap.add_argument('--recon', choices=['pending'], help='reconciliation add-on back to "Pending review"')
ap.add_argument('--thumbs', help='directory: save LARGE PNG thumbnails of slides 2, 31, 34, 35, 36, 37')
args = ap.parse_args()

creds = service_account.Credentials.from_service_account_file(SA_KEY, scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
pres = svc.presentations().get(presentationId=args.pid).execute()
slides = pres['slides']
print('deck:', pres.get('title'), '| slides:', len(slides))

def el_text(el):
    out = []
    for holder in ([el.get('shape', {})] + [c for r in el.get('table', {}).get('tableRows', []) for c in r.get('tableCells', [])]):
        for te in holder.get('text', {}).get('textElements', []):
            out.append(te.get('textRun', {}).get('content', ''))
    for ch in el.get('elementGroup', {}).get('children', []):
        out.append(el_text(ch))
    return ''.join(out)

texts, ids, stray = {}, {}, []
for i, s in enumerate(slides, 1):
    ids[i] = s['objectId']; texts[i] = ''.join(el_text(el) for el in s.get('pageElements', []))
    for el in s.get('pageElements', []):
        t = el_text(el).strip()
        if STRAY in t and len(t) <= 12:
            tr = el.get('transform', {}); sz = el.get('size', {})
            stray.append((i, el['objectId'], t, round(tr.get('translateX', 0) / 12700), round(tr.get('translateY', 0) / 12700),
                          round(sz.get('width', {}).get('magnitude', 0) / 12700), round(sz.get('height', {}).get('magnitude', 0) / 12700)))
print('stray "%s" boxes (slide, id, text, x pt, y pt, w, h):' % STRAY)
for row in stray: print('  ', row)
print('other slides mentioning %s:' % STRAY, [i for i, t in texts.items() if STRAY in t])

# (search, replace, slide number)
FIXES = []
if args.min == 'keep':
    FIXES.append(('Monthly minimum billing: $25,000.', 'Minimum monthly invoice: $25,000, platform fee included.', 36))
elif args.min == 'drop':
    FIXES.append((' Monthly minimum billing: $25,000.', '', 36))
if args.ramp:
    tail = ', billed at the $25,000 minimum' if args.min != 'drop' else ''
    FIXES.append(('Sequence shown as Yango proposed it: Colombia and Peru first, then Bolivia and Venezuela.',
                  'Sequence as Yango proposed it: Colombia first ($22,526 a month on its own%s), then Peru ($33,414 for both), then Bolivia and Venezuela.' % tail, 37))
if args.source:
    FIXES.append(("Source: Yango's own recharge data, July 2026.", "Source: Yango's own recharge data for July 2026, shared August 2026.", 31))
if args.recon == 'pending':
    FIXES.append(('$2,000 / month for the first 500K reconciled trx, then $0.0003 per trx', 'Pending review', 36))

ok = True
for search, repl, n in FIXES:
    hits = {i: t.count(search) for i, t in texts.items() if search in t}
    print(f'"{search[:70]}" -> slides {hits or "NONE"}')
    if not hits or set(hits) != {n}: ok = False
if not ok:
    print('Text mismatch: fix the search strings before applying.'); sys.exit(1)

reqs = [{'replaceAllText': {'containsText': {'text': s, 'matchCase': True}, 'replaceText': r, 'pageObjectIds': [ids[n]]}} for s, r, n in FIXES]
if args.delete_stray:
    reqs += [{'deleteObject': {'objectId': oid}} for _, oid, *_ in stray]

if args.thumbs:
    os.makedirs(args.thumbs, exist_ok=True)
    for n in [2, 31, 34, 35, 36, 37]:
        if n > len(slides): continue
        th = svc.presentations().pages().getThumbnail(presentationId=args.pid, pageObjectId=ids[n], thumbnailProperties_thumbnailSize='LARGE').execute()
        path = os.path.join(args.thumbs, f'slide{n:02d}.png'); urllib.request.urlretrieve(th['contentUrl'], path); print('thumbnail', path)

if not reqs:
    print('nothing selected (use --delete-stray / --min / --ramp / --source / --recon)'); sys.exit(0)
if not args.apply:
    print(f'dry run: {len(reqs)} request(s) prepared, nothing changed'); sys.exit(0)
res = svc.presentations().batchUpdate(presentationId=args.pid, body={'requests': reqs}).execute()
for req, rep in zip(reqs, res.get('replies', [])):
    if 'replaceAllText' in req: print('replaced', rep.get('replaceAllText', {}).get('occurrencesChanged', 0), 'x ->', req['replaceAllText']['replaceText'][:70])
    else: print('deleted', req['deleteObject']['objectId'])
print('done. Re-export the PDF and re-upload it to Papermark (slug yangobclatam); replaceAllText does not resize boxes, check slide 37 intro visually.')
