# -*- coding: utf-8 -*-
"""Apply the three blocker fixes to the live FlightHub proposal deck via the Slides API.

Auth: service account key ~/.config/gsuite/sa.json (gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com).
The deck must be shared with that service account as editor (done via the claude.ai Drive connector).

Usage:
  python3 apply_blocker_fixes_2026-09-22.py --dry            # only count matches, change nothing
  python3 apply_blocker_fixes_2026-09-22.py                  # apply
  python3 apply_blocker_fixes_2026-09-22.py --l2 "Smart routing"   # alternative lever 2 label
"""
import argparse, json, os, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

PID = '1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI'
SA_KEY = os.path.expanduser('~/.config/gsuite/sa.json')

ap = argparse.ArgumentParser()
ap.add_argument('--dry', action='store_true')
ap.add_argument('--l2', default='Routing & retries', help='new label for business-case lever 2 (slide 13)')
ap.add_argument('--pid', default=PID)
args = ap.parse_args()

creds = service_account.Credentials.from_service_account_file(SA_KEY, scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
pres = svc.presentations().get(presentationId=args.pid).execute()
slides = pres['slides']
print('deck:', pres.get('title'), '| slides:', len(slides))

def slide_text(s):
    out = []
    for el in s.get('pageElements', []):
        for holder in ([el.get('shape', {})] + [c for r in el.get('table', {}).get('tableRows', []) for c in r.get('tableCells', [])]):
            for te in holder.get('text', {}).get('textElements', []):
                out.append(te.get('textRun', {}).get('content', ''))
        for ch in el.get('elementGroup', {}).get('children', []):
            for te in ch.get('shape', {}).get('text', {}).get('textElements', []):
                out.append(te.get('textRun', {}).get('content', ''))
    return ''.join(out)

texts = {i + 1: slide_text(s) for i, s in enumerate(slides)}
ids = {i + 1: s['objectId'] for i, s in enumerate(slides)}

# (search, replace, restrict-to-slide-number or None)
FIXES = [
    ('NETWORK AND SECURITY TOKENS & RECONCILIATION', 'NETWORK TOKENS & RECONCILIATION', 16),
    ('Network and security tokens:', 'Network tokens:', 16),
    ('Smart Routing & Retries', args.l2, 13),
    ('in-house squad cost is an estimate of 4 to 5 fully-loaded payments engineers plus ops',
     'in-house cost is an estimate: 4 to 5 payments engineers at $100K fully loaded ($0.4M to $0.5M, the run-ops lever) plus infrastructure, PCI and certification upkeep and tooling', 19),
]

ok = True
for search, repl, n in FIXES:
    hits = {i: t.count(search) for i, t in texts.items() if search in t}
    print(f'"{search[:60]}" -> found on slides {hits or "NONE"}')
    if not hits or (n and set(hits) != {n}):
        ok = False
if not ok:
    print('Text mismatch: fix the search strings before applying.'); sys.exit(1)
if args.dry:
    print('dry run, nothing changed'); sys.exit(0)

reqs = [{'replaceAllText': {'containsText': {'text': s, 'matchCase': True}, 'replaceText': r,
                            'pageObjectIds': [ids[n]]}} for s, r, n in FIXES]
res = svc.presentations().batchUpdate(presentationId=args.pid, body={'requests': reqs}).execute()
for (s, r, n), rep in zip(FIXES, res.get('replies', [])):
    print(f'slide {n}: {rep.get("replaceAllText", {}).get("occurrencesChanged", 0)} occurrence(s) -> "{r[:70]}"')
