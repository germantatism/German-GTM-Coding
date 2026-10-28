#!/usr/bin/env python3
"""
cut_to_12.py: apply the 12-slide cut to the Google Slides COPY of Magdalena's
"The New York Times - Subscriptions Deck" (original 1eFQx1WE..., 19 slides, 18 Sep 2026).

Copy (owned by German, folder "The New York Times"):
  https://docs.google.com/presentation/d/1I_MuFh9-jjQ0bfiNHXQFoj6-x_HCp6UFSHp6ngtMrms/edit

What it does (same decisions as Deals/NYT/Yuno_x_NYT_Subscriptions_Sep2026.pptx):
  1. Deletes 7 slides: agenda, the three section dividers, "The renewal falls between two systems"
     (slide 5 + 7 carry the point), and the retries detail slide (its content is folded into the cycle slide).
  2. Text edits: retries line on the cycle slide; "What is live" proof replaced by Control Center figures
     (16 merchants, 135K subs, 83% -> 86%, 69K reactivated) instead of the Reface stats and the unsourced
     "about 1 week"; next step runs one billing cycle instead of "about a week"; German added to the close.

Usage:
  python3 cut_to_12.py            # dry run: prints the plan, checks the token
  python3 cut_to_12.py --apply    # applies it
  python3 cut_to_12.py --pid <id> # target another copy

Needs a live Slides API token (~/.config/yuno-slides/token.json). Since 18 Sep 2026 the old one is dead
(GCP project deleted): create a new GCP project with the Slides API enabled and a Desktop OAuth client,
then run  python3 Deals/Appmaking/build/auth_slides.py <client_secret.json>  and retry.
"""
import sys, argparse
REPO = '/Users/germantatis/Desktop/GTMCoding'
sys.path.insert(0, f'{REPO}/Industry/AI/Higgsfield/build')
from engine import service, run

COPY_ID = '1I_MuFh9-jjQ0bfiNHXQFoj6-x_HCp6UFSHp6ngtMrms'
ORIGINAL_ID = '1eFQx1WE-Ql2PtpFUDGkubTOHLOgTronho2dV9ibbkPA'

# 1-based indexes in the ORIGINAL 19-slide order
DELETE = {2: 'Agenda', 3: 'Divider 01', 6: 'The renewal falls between two systems', 8: 'Divider 02',
          12: 'Retries detail (folded into the cycle slide)', 14: 'Divider 03', 16: 'Divider 04'}
KEEP_TITLES = ['Cover', 'The renewal happens 12.8 million times', 'Your stack today, layer by layer',
               'What that split costs at renewal', 'A subscription engine inside the payments layer',
               "NYT's plans, configured in the Yuno dashboard", 'Every cycle: charge, and if it declines',
               'The step up from promotional to full price', 'The engine comes with its orchestration underneath',
               'Live in production today', 'A first cycle together', 'Close']

REPLACE = [
    # cycle slide: fold the retries slide into the bottom line
    ("The structural difference: the retry is a routed charge too. It can go through a different provider than the one that declined, and when it clears, the cycle is simply renewed.",
     "The structural difference: the retry is a routed charge too, with a strategy per plan (default, custom schedule, Smart ML, A/B in the dashboard) that stops on hard declines. It can go through a different provider than the one that declined, and when it clears, the cycle is simply renewed."),
    # what is live: Control Center figures instead of Reface stats and the unsourced migration time
    ("350,000+", "135K"),
    ("recurring payments a month from one subscription merchant, across roughly 88,000 active subscriptions",
     "active subscriptions across 16 merchants live on the engine"),
    ("88.29%", "83% → 86%"),
    ("approval on their best performing method and market combination",
     "renewal approval per cycle, first attempt and after retries"),
    ("YUNO PORTFOLIO DATA, ANONYMIZED", "YUNO CONTROL CENTER, 31 AUG 2026"),
    ("About 1 week", "69K"),
    ("typical migration time onto the engine", "past-due subscriptions reactivated in 30 days"),
    # next step: a billing cycle, not a week
    ("about a week, second provider as fallback", "one billing cycle, second provider as fallback"),
    # close: add German
    ("Magdalena Torrealba | Sales Strategy Associate",
     "German Tatis | Business Development Manager   ·   Magdalena Torrealba | Sales Strategy Associate"),
    ("magdalena.torrealba@y.uno", "german.tatis@y.uno   ·   magdalena.torrealba@y.uno"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--pid', default=COPY_ID)
    a = ap.parse_args()
    if a.pid == ORIGINAL_ID:
        sys.exit("Refusing to edit Magdalena's original. Target the copy (default) or pass --pid <your copy>.")
    print(f"Target: https://docs.google.com/presentation/d/{a.pid}/edit")
    try:
        svc = service()
        p = svc.presentations().get(presentationId=a.pid, fields='title,slides.objectId').execute()
    except Exception as e:
        msg = str(e)
        if 'CONSUMER_INVALID' in msg or 'has been deleted' in msg or '403' in msg:
            sys.exit("Slides API token is dead (403). Re-auth first:\n  python3 Deals/Appmaking/build/auth_slides.py <new client_secret.json>\n" + msg[:200])
        raise
    slides = p['slides']
    print(f"'{p['title']}': {len(slides)} slides")
    if len(slides) != 19:
        sys.exit(f"Expected the untouched 19-slide copy, found {len(slides)}. Already cut? Nothing done.")
    reqs = []
    for idx, why in sorted(DELETE.items()):
        reqs.append({'deleteObject': {'objectId': slides[idx - 1]['objectId']}})
        print(f"  delete slide {idx:2d}: {why}")
    for old, new in REPLACE:
        reqs.append({'replaceAllText': {'containsText': {'text': old, 'matchCase': True}, 'replaceText': new}})
        print(f"  replace: {old[:60]!r} -> {new[:60]!r}")
    if not a.apply:
        print(f"\nDry run: {len(reqs)} requests prepared. Re-run with --apply.")
        return
    run(svc, a.pid, reqs, label='cut to 12')
    p2 = svc.presentations().get(presentationId=a.pid, fields='slides.objectId').execute()
    n = len(p2['slides'])
    print(f"Done: {n} slides." + ('' if n == 12 else '  WARNING: expected 12'))
    print("Remaining order:", ' | '.join(KEEP_TITLES))

if __name__ == '__main__':
    main()
