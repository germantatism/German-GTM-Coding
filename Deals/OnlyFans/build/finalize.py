# -*- coding: utf-8 -*-
"""
finalize.py · after parallel workers: order the built slides by their nXX prefix, delete the 46 template slides
in one call, verify. Safe to re-run: it only reorders and only deletes slides whose id does not start with "n".

  python3 finalize.py            # reorder + delete templates + verify
  python3 finalize.py --dry      # report only
"""
import re, sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs_engine as E

def main(dry=False):
    deck = E.Deck(); spec = json.load(open(os.path.join(E.HERE, 'deck_spec.json')))
    n_spec = len(spec['slides'])
    live = deck.slide_ids()
    built = {}
    for sid in live:
        m = re.match(r'^n(\d\d)(?:r\d+|p)?_', sid)
        if m: built.setdefault(int(m.group(1)), []).append(sid)
    templates = [s for s in live if not re.match(r'^n\d\d', s)]
    if not templates: print('no template slides left: reorder only')
    missing = [k for k in range(1, n_spec + 1) if k not in built]
    dupes = {k: v for k, v in built.items() if len(v) > 1}
    print(f"live {len(live)} | built positions {len(built)}/{n_spec} | template slides {len(templates)} | missing {missing} | duplicates {dupes}")
    if missing:
        ids = [spec['slides'][k - 1]['id'] for k in missing]
        print("rerun:  python3 gs_engine.py build deck_spec.json --only " + ','.join(ids)); return 1
    if dupes:
        print("resolve duplicates first (a position has both a real slide and a placeholder, or two workers built it)"); return 1
    order = [built[k][0] for k in sorted(built)]
    if dry: print('would order:', order[:5], '...'); return 0
    reqs = [{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': i}} for i, sid in enumerate(order)]
    deck.run(reqs, 'reorder built slides')
    live = deck.slide_ids()
    if live[:len(order)] != order:
        print('ORDER MISMATCH after reorder; not deleting templates'); print(live[:len(order)]); return 1
    if templates:
        if len(templates) != E.N_TEMPLATE: print(f"note: {len(templates)} template slides present (expected {E.N_TEMPLATE})")
        deck.delete_slides(templates)
    live = deck.slide_ids()
    ok = live == order
    print(f"final deck: {len(live)} slides; order verified: {ok}")
    for i, sid in enumerate(live, 1):
        if sid != order[i - 1]: print('  position', i, 'has', sid, 'expected', order[i - 1])
    deck.state['built'] = []; deck.state['finalized'] = True; deck.save_state()
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main('--dry' in sys.argv))
