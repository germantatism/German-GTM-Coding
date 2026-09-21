# -*- coding: utf-8 -*-
"""Appmaking deck: duplicate the pricing slide (s13) and, on the COPY only, turn the "PENDING REVIEW"
box into the add-ons Tatsiana asked for on 2026-09-21: token vault (included), network tokens and a
reconciliation estimate. The original slide is never edited; the copy lands right after it.

Requires a valid Slides token at ~/.config/yuno-slides/token.json (see auth_slides.py).
  python3 Deals/Appmaking/build/dup_s13_addons.py --inspect              # print the box structure, change nothing
  python3 Deals/Appmaking/build/dup_s13_addons.py --nt established --dry  # print the requests, change nothing
  python3 Deals/Appmaking/build/dup_s13_addons.py --nt established        # apply + save a thumbnail for QA

--nt (required, no default on purpose; source: Yuno Products Pricing Policy, Laura Galan, 2026-09-21)
    established  $0.05 per token created / $0.01 per update. BELOW the policy minimum: red zone,
                 needs Global Controller/CFO + CRO sign-off before it is quoted
    floor        $0.20 / $0.04, policy minimum: yellow zone, RevOps / Sales Ops / GM review
    list         $0.35 / $0.07, policy list price: green
    included     bundled into the platform fee (the policy lists Network Tokens as bundleable)
--matched        also change "$14 for every alert" to "$14 per matched alert" on the copy
                 (policy billable unit: one matched alert, unmatched alerts are not billed)

Reconciliation estimate = policy pack "50K reconciled transactions": $1,500 / month, then $0.032 per
additional reconciled transaction. On Appmaking's ramp: $1,500 a month through month 3 (20K, 30K, 45K),
$1,980 at 65K, $2,780 at 90K, $3,740 at 120K, $4,700 at 150K. Above ~160K the 250K pack ($5,000 / month,
then $0.022) is cheaper. Token vault: $0, bundled into core for any merchant processing pay-ins with Yuno.
"""
import sys, os, json, time, argparse, urllib.request
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')

PID = '1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc'
S13 = 'g3f6c0558646_0_35'
OUT = os.path.dirname(os.path.abspath(__file__))
PT = 12700.0  # EMU per point

NT = {'established': ('$0.05', '$0.01'), 'floor': ('$0.20', '$0.04'), 'list': ('$0.35', '$0.07'), 'included': None}
TITLE = 'ADD-ONS'
SUB = 'Estimated pricing. Reconciliation is optional and can be added later.'
TEXT_FIELDS = ['bold', 'italic', 'underline', 'fontSize', 'foregroundColor', 'fontFamily', 'weightedFontFamily']
PARA_FIELDS = ['alignment', 'lineSpacing', 'spaceAbove', 'spaceBelow', 'indentStart', 'indentEnd', 'indentFirstLine']


def lines_for(nt):
    """two lines of (text, 'L' label | 'V' value) segments"""
    l1 = [('Token vault ', 'L'), ('Included', 'V'), ('   ·   ', 'L'), ('Network tokens ', 'L')]
    if NT[nt] is None:
        l1 += [('Included', 'V')]
    else:
        c, u = NT[nt]
        l1 += [(c, 'V'), (' per token, ', 'L'), (u, 'V'), (' per update', 'L')]
    l2 = [('Reconciliation ', 'L'), ('$1,500 / month', 'V'), (' incl. 50,000 reconciled trx, then ', 'L'),
          ('$0.032', 'V'), (' each', 'L')]
    return [l1, l2]


# ---------- geometry / lookup (pure functions, testable offline) ----------
def compose(a, b):
    return {'scaleX': a.get('scaleX', 1) * b.get('scaleX', 1) + a.get('shearX', 0) * b.get('shearY', 0),
            'scaleY': a.get('shearY', 0) * b.get('shearX', 0) + a.get('scaleY', 1) * b.get('scaleY', 1),
            'translateX': a.get('scaleX', 1) * b.get('translateX', 0) + a.get('shearX', 0) * b.get('translateY', 0) + a.get('translateX', 0),
            'translateY': a.get('shearY', 0) * b.get('translateX', 0) + a.get('scaleY', 1) * b.get('translateY', 0) + a.get('translateY', 0)}


def flat(slide):
    out = []
    def walk(el, par=None, grp=None):
        tr = el.get('transform', {})
        if par: tr = compose(par, tr)
        if 'elementGroup' in el:
            for ch in el['elementGroup']['children']: walk(ch, tr, el['objectId'])
        else: out.append((el, tr, grp))
    for el in slide.get('pageElements', []): walk(el)
    return out


def text_of(el):
    return ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', []))


def runs(el):
    return [(te['textRun']['content'], te['textRun'].get('style', {}))
            for te in el.get('shape', {}).get('text', {}).get('textElements', [])
            if 'textRun' in te and te['textRun'].get('content', '').strip('\n\x0b')]


def first_pstyle(el):
    for te in el.get('shape', {}).get('text', {}).get('textElements', []):
        if 'paragraphMarker' in te: return te['paragraphMarker'].get('style', {})
    return {}


def bbox(el, tr):
    w = el.get('size', {}).get('width', {}).get('magnitude', 0) * tr.get('scaleX', 1)
    h = el.get('size', {}).get('height', {}).get('magnitude', 0) * tr.get('scaleY', 1)
    x, y = tr.get('translateX', 0), tr.get('translateY', 0)
    return x, y, x + w, y + h


def locate(slide):
    """find the PENDING REVIEW box pieces on the pricing slide"""
    els = flat(slide)
    tt = [(e, t, g) for e, t, g in els if text_of(e).strip().upper().startswith('PENDING REVIEW')]
    if len(tt) != 1: raise SystemExit(f"expected 1 'PENDING REVIEW' element, got {len(tt)}")
    title = tt[0]; tx0, ty0, _, _ = bbox(title[0], title[1])
    region = [(e, t, g) for e, t, g in els if text_of(e).strip()
              and bbox(e, t)[0] >= tx0 - 2 * PT and ty0 - 2 * PT <= bbox(e, t)[1] <= ty0 + 40 * PT]
    sub = None
    if 'scope and pricing' not in text_of(title[0]).lower():
        ss = [x for x in region if text_of(x[0]).strip().lower().startswith('scope and pricing')]
        if len(ss) != 1: raise SystemExit(f"expected 1 subtitle element, got {len(ss)}")
        sub = ss[0]
    rows = [x for x in region if x[0] is not title[0] and (sub is None or x[0] is not sub[0])]
    if not rows: raise SystemExit('no row elements (Reconciliation / Token vault) found in the box')
    rows.sort(key=lambda x: (round(bbox(x[0], x[1])[1] / PT), bbox(x[0], x[1])[0]))
    keep = [x for x in rows if text_of(x[0]).strip().lower().startswith('reconciliation')] or rows[:1]
    subs = [x for x in els if 'processed free' in text_of(x[0])]
    return {'title': title, 'sub': sub, 'rows': rows, 'keep': keep[0], 'region': region, 'subs_body': subs[0] if subs else None}


def styles(found):
    """label style from the kept row's first run; value style = label + bold + the accent colour of the left box"""
    kr = runs(found['keep'][0])
    label = {k: v for k, v in (kr[0][1] if kr else {}).items() if k in TEXT_FIELDS}
    label['italic'] = False; label.setdefault('bold', False)
    value = dict(label); value['bold'] = True
    if found['subs_body']:
        for _, st in runs(found['subs_body'][0]):
            if st.get('bold') and st.get('foregroundColor'):
                value['foregroundColor'] = st['foregroundColor']
                for k in ('fontFamily', 'weightedFontFamily'):
                    if k in st: value[k] = st[k]
                break
    return label, value


def write_segments(oid, lines, label, value, pstyle):
    text = '\n'.join(''.join(s for s, _ in ln) for ln in lines)
    reqs = [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}},
            {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': text}}]
    i = 0
    for ln in lines:
        for s, kind in ln:
            st = value if kind == 'V' else label
            reqs.append({'updateTextStyle': {'objectId': oid, 'style': st, 'fields': ','.join(st.keys()),
                                             'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(s)}}})
            i += len(s)
        i += 1
    ps = {k: v for k, v in pstyle.items() if k in PARA_FIELDS}
    if ps:
        reqs.append({'updateParagraphStyle': {'objectId': oid, 'style': ps, 'fields': ','.join(ps.keys()),
                                              'textRange': {'type': 'ALL'}}})
    return reqs, text


def write_segments_raw(oid, parts, pstyle):
    """parts: [(text, style)] written back to back, one style per part"""
    text = ''.join(s for s, _ in parts)
    reqs = [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}},
            {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': text}}]
    i = 0
    for s, st in parts:
        st = {k: v for k, v in st.items() if k in TEXT_FIELDS}
        if st and s.strip():
            reqs.append({'updateTextStyle': {'objectId': oid, 'style': st, 'fields': ','.join(st.keys()),
                                             'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(s)}}})
        i += len(s)
    ps = {k: v for k, v in pstyle.items() if k in PARA_FIELDS}
    if ps:
        reqs.append({'updateParagraphStyle': {'objectId': oid, 'style': ps, 'fields': ','.join(ps.keys()),
                                              'textRange': {'type': 'ALL'}}})
    return reqs


def build_requests(slide, nt, matched=False, stamp=None):
    f = locate(slide); stamp = stamp or time.strftime('%m%d%H%M%S')
    new_slide = f'am_s13_addons_{stamp}'
    touched = [f['title'][0], f['keep'][0]] + ([f['sub'][0]] if f['sub'] else []) + [x[0] for x in f['rows']]
    ids = {S13: new_slide}
    for k, el in enumerate({e['objectId']: e for e in touched}.values()):
        ids[el['objectId']] = f'{new_slide}_e{k}'
    reqs = [{'duplicateObject': {'objectId': S13, 'objectIds': ids}}]

    # title (+ subtitle, same shape or its own)
    t_el = f['title'][0]; t_runs = runs(t_el); t_txt = text_of(t_el)
    if f['sub'] is None:
        a = t_txt.upper().find('PENDING REVIEW') + len('PENDING REVIEW'); b = t_txt.lower().find('scope and pricing')
        sep = t_txt[a:b] or '   '
        sub_style = next((st for s, st in t_runs if 'scope' in s.lower()), t_runs[-1][1])
        reqs += write_segments_raw(ids[t_el['objectId']], [(TITLE, t_runs[0][1]), (sep, sub_style), (SUB, sub_style)], first_pstyle(t_el))
    else:
        reqs += write_segments_raw(ids[t_el['objectId']], [(TITLE, t_runs[0][1])], first_pstyle(t_el))
        s_el = f['sub'][0]
        reqs += write_segments_raw(ids[s_el['objectId']], [(SUB, runs(s_el)[0][1])], first_pstyle(s_el))

    # rows: keep the "Reconciliation" shape (its insets and font survive), stretch it, drop the rest
    k_el, k_tr, _ = f['keep']
    for e, _, _ in f['rows']:
        if e is not k_el: reqs.append({'deleteObject': {'objectId': ids[e['objectId']]}})
    x0, y0, x1, y1 = bbox(k_el, k_tr)
    right = max(bbox(e, t)[2] for e, t, _ in f['region'])
    fx = max(1.0, (right - x0) / max(x1 - x0, 1)); fy = 2.15
    own = dict(k_el.get('transform', {}))
    new_tr = {'scaleX': own.get('scaleX', 1) * fx, 'scaleY': own.get('scaleY', 1) * fy,
              'shearX': own.get('shearX', 0), 'shearY': own.get('shearY', 0),
              'translateX': own.get('translateX', 0), 'translateY': own.get('translateY', 0), 'unit': own.get('unit', 'EMU')}
    reqs.append({'updatePageElementTransform': {'objectId': ids[k_el['objectId']], 'applyMode': 'ABSOLUTE', 'transform': new_tr}})
    reqs.append({'updateShapeProperties': {'objectId': ids[k_el['objectId']], 'fields': 'contentAlignment',
                                           'shapeProperties': {'contentAlignment': 'TOP'}}})
    label, value = styles(f)
    seg_reqs, row_text = write_segments(ids[k_el['objectId']], lines_for(nt), label, value, first_pstyle(k_el))
    reqs += seg_reqs
    if matched:
        reqs.append({'replaceAllText': {'containsText': {'text': 'for every alert', 'matchCase': True},
                                        'replaceText': 'per matched alert', 'pageObjectIds': [new_slide]}})
    return reqs, new_slide, row_text


def inspect(slide):
    f = locate(slide)
    for e, t, g in f['region'] + ([f['subs_body']] if f['subs_body'] else []):
        x0, y0, x1, y1 = [round(v / PT, 1) for v in bbox(e, t)]
        role = 'TITLE' if e is f['title'][0] else 'SUB' if f['sub'] and e is f['sub'][0] else 'KEEP' if e is f['keep'][0] else 'row/other'
        print(f"\n[{role}] {e['objectId']} group={g} box=({x0},{y0})-({x1},{y1})pt own_tr={e.get('transform')}")
        print('  autofit:', e.get('shape', {}).get('shapeProperties', {}).get('autofit'))
        for s, st in runs(e):
            print('  run', repr(s), {k: st.get(k) for k in ('fontSize', 'bold', 'italic', 'fontFamily', 'foregroundColor') if k in st})


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--nt', choices=list(NT)); ap.add_argument('--matched', action='store_true')
    ap.add_argument('--dry', action='store_true'); ap.add_argument('--inspect', action='store_true'); a = ap.parse_args()
    if not a.inspect and not a.nt: raise SystemExit('--nt is required: established | floor | list | included (see the docstring)')
    from engine import service
    svc = service(); P = svc.presentations().get(presentationId=PID).execute()
    s = [x for x in P['slides'] if x['objectId'] == S13][0]
    if a.inspect: inspect(s); raise SystemExit(0)
    R, new_slide, row_text = build_requests(s, a.nt, a.matched)
    print('box title :', TITLE, '|', SUB); print('box rows  :', row_text.replace('\n', ' / '))
    if a.dry: print(json.dumps(R, indent=1)[:6000]); raise SystemExit('dry run, nothing applied')
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': R}).execute()
    print('applied', len(R), 'requests; new slide', new_slide)
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=new_slide, thumbnailProperties_thumbnailSize='LARGE').execute()
    png = os.path.join(OUT, f'appmaking-s13-addons-{a.nt}.png'); urllib.request.urlretrieve(r['contentUrl'], png)
    print('thumbnail:', png, ' -> check the box: nothing overflows or overlaps; original slide 13 untouched')
    print(f'link: https://docs.google.com/presentation/d/{PID}/edit#slide=id.{new_slide}')
