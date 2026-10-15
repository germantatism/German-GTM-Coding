# -*- coding: utf-8 -*-
"""One-off live update for the reframe pass (15 Oct 2026): the deck is finalized (no template slides), and slides were removed
from the spec, so `--only --replace` (which matches old slides by spec index) cannot be used for slides after the removal point.
This script maps the 42 live slides to the pre-reframe spec by position, deletes the removed slides, rebuilds every changed content
slide in place with its new index (page numbers follow), edits the agenda and dividers in place (template types cannot be re-created
after --final), refreshes notes, and deletes every leftover "For: Carry1st" footer.  Usage: python3 apply_reframe_live.py [dry]"""
import sys, json, re, warnings; warnings.filterwarnings('ignore')
import gs_engine as g
DRY = 'dry' in sys.argv
OLD = [s['id'] for s in json.load(open('backup/deck_spec.pre_reframe.json'))['slides']]
SPEC = json.load(open('deck_spec.json')); NEW = SPEC['slides']; footer = SPEC.get('footer', '')
REMOVED = ['launch', 'd08', 'next']
RENAMED = {'bc-levers': 'bc-tiers', 'bc-impact': 'bc-scenarios'}
KEEP_AS_IS = {'cover', 'platform', 'trusted', 'proof', 'closing'}          # untouched slides (cover: notes only)
TEMPLATE_TYPES = {'agenda', 'divider'}

deck = g.Deck(); deck.fetch()
live = deck.slide_ids()
assert len(live) == len(OLD) == 42, (len(live), len(OLD))
old_sid = dict(zip(OLD, live))
for i, sid in zip(OLD, live): assert re.match(r'^n\d\d', sid), sid
print('removing:', [old_sid[i] for i in REMOVED])
plan = [(n, s) for n, s in enumerate(NEW, 1) if s['id'] not in KEEP_AS_IS and s['type'] not in TEMPLATE_TYPES]
print('rebuild in place:', [f"{n}:{s['id']}" for n, s in plan])
if DRY:
    dd = g.DryDeck()
    for n, s in plan: g.render_one(dd, s, f'n{n:02d}', n, footer)
    print('dry ok'); sys.exit(0)

# 1. removed slides
deck.run([{'deleteObject': {'objectId': old_sid[i]}} for i in REMOVED], 'delete launch, d08, next')

# 2. content slides rebuilt in place
for n, s in plan:
    target = old_sid[RENAMED.get(s['id'], s['id'])]
    live_now = deck.slide_ids(); k = 1
    while any(i.startswith(f"n{n:02d}r{k}_") for i in live_now): k += 1
    tag = f"n{n:02d}r{k}"
    print(f"[{n:02d}] {s['type']:16s} {s['id']} -> {tag} (replaces {target})")
    g.render_one(g.DryDeck(), s, tag, n, footer)
    sid = g.render_one(deck, s, tag, n, footer)
    live_now = deck.slide_ids(); idx = live_now.index(target)
    deck.run([{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': idx}}, {'deleteObject': {'objectId': target}}], f'place {sid}')

# 3. agenda and dividers in place
P = deck.fetch(); pages = {sl['objectId']: sl for sl in P['slides']}
def own_elements(sid):
    pre = sid.split('_')[0]
    return [e['objectId'] for e, _ in g.elements(pages[sid]) if re.match(rf'^{pre}(x\d+)?_e\d+$', e['objectId'])]
def idmap_for(sid, base):
    pre = sid.split('_')[0]; src = deck.tpl_slides[base - 1]
    return {i: f"{pre}_{i}" for i in [src['objectId']] + g.all_ids(src)}
def fresh_tag(sid):
    pre = sid.split('_')[0]; ids = {e['objectId'] for e, _ in g.elements(pages[sid])}; k = 1
    while any(i.startswith(f"{pre}x{k}_") for i in ids): k += 1
    return f"{pre}x{k}"
for n, s in enumerate(NEW, 1):
    if s['type'] not in TEMPLATE_TYPES: continue
    sid = old_sid[s['id']]
    if s['type'] == 'divider':
        sb = g.SB(deck, sid, fresh_tag(sid), idmap_for(sid, 3), dark=True)
        sb.R += [{'deleteObject': {'objectId': o}} for o in own_elements(sid)]
        sb.R += g.replace_text_requests(sb._tpl_el(3, g.ROLE[3]['num']), str(s.get('num', '')))
        title = s.get('title') or ''
        sb.R += g.replace_text_requests(sb._tpl_el(3, g.ROLE[3]['title']), title, size=29 if g.wrap_count(title, 29, 579, True) <= 2 else 24)
        if s.get('sub'): sb.text(g.X0, 352, 579, 14, s['sub'], size=10, color=g.ONDARK, ls=110)
        y = 78
        for item in s.get('section_list') or []:
            cur = (str(s.get('num', '')).strip() and item.strip().startswith(str(s.get('num')).strip())) or (title and title.lower() in item.lower())
            sb.text(g.X0, y, 400, 10, item.upper(), size=7, bold=bool(cur), color=g.WHITE if cur else '#B9BFE8', ls=100); y += 13
        sb.flush(f"divider {s['id']}"); deck.set_notes(sid, s.get('notes'))
    else:
        sb = g.SB(deck, sid, fresh_tag(sid), idmap_for(sid, 2))
        sb.R += [{'deleteObject': {'objectId': o}} for o in own_elements(sid)]
        items = s.get('items', []); N = max(len(items), 1); y0 = 118; pitch = min(47.6, (362 - y0) / N); size = 15 if pitch >= 36 else (13 if pitch >= 28 else 11)
        for i, it in enumerate(items):
            y = y0 + i * pitch
            sb.text(g.X0, y + 4, 40, 14, str(it.get('num', f"{i + 1:02d}")), size=10, color=g.LBLUE, font=g.MONO, ls=100)
            sb.text(73.8, y, 549, size * 1.5, (it.get('title') or '').upper(), size=size, color=g.INK, ls=110)
            if i < N - 1: sb.hairline(g.X0, y + pitch - 13, g.W0)
        sb.flush('agenda'); deck.set_notes(sid, s.get('notes'))
    print('in place:', s['id'], sid)

# 4. cover notes (subtitle untouched)
cov = next(s for s in NEW if s['id'] == 'cover'); deck.set_notes(old_sid['cover'], cov.get('notes'))

# 5. leftover footers
P = deck.fetch(); dels = [e['objectId'] for sl in P['slides'] for e, _ in g.elements(sl) if g.text_of(e).strip() == 'For: Carry1st']
if dels: deck.run([{'deleteObject': {'objectId': o}} for o in dels], f'delete {len(dels)} footers')
P = deck.fetch()
left = sum(1 for sl in P['slides'] for e, _ in g.elements(sl) if 'For: Carry1st' in g.text_of(e))
print('slides now:', len(P['slides']), '| "For: Carry1st" left:', left)
