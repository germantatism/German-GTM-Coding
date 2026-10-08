# -*- coding: utf-8 -*-
"""
qa_thumbs.py · export slide thumbnails + contact sheets and run a geometry / overflow check on the live deck.

  python3 qa_thumbs.py                      # all slides -> thumbs_build/, report for every slide
  python3 qa_thumbs.py --out thumbs_smoke   # different folder
  python3 qa_thumbs.py --from 47            # only slides 47.. (1-based position), e.g. the appended ones
  python3 qa_thumbs.py --no-thumbs          # geometry report only

Checks per slide (from presentations.get, absolute geometry, group transforms composed):
  OUT      element outside the page (tolerance 0.6 pt; full-bleed images allowed)
  OVERLAP  two text-bearing shapes whose boxes intersect by more than 3 pt in both axes
  OVERFLOW estimated text overflow: chars per line from the box width (minus insets) at the run's font size,
           average glyph 0.5 em (0.53 for lowercase mixed text), lines * size * 1.21 * lineSpacing vs box height
  FONT     any run below 6.5 pt (engine floor) on engine-built slides
"""
import os, sys, json, math, re, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs_engine as E
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))

def thumbs(deck, slides, out, start=1):
    os.makedirs(out, exist_ok=True); paths = []
    for n, s in enumerate(slides, 1):
        if n < start: continue
        for attempt in range(4):
            try:
                r = deck.svc.presentations().pages().getThumbnail(presentationId=deck.pid, pageObjectId=s['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
                p = os.path.join(out, f"b_{n:02d}.png"); urllib.request.urlretrieve(r['contentUrl'], p); paths.append((n, p)); break
            except Exception as e:
                if attempt == 3: raise
                print('  thumb retry', n, str(e)[:100]); time.sleep(3)
    # contact sheets, 4 x 4 per sheet
    per = 16; cols = 4
    for k in range(0, len(paths), per):
        chunk = paths[k:k + per]; tw, th = 400, 225
        rows = math.ceil(len(chunk) / cols); sheet = Image.new('RGB', (cols * tw + 10 * (cols + 1), rows * (th + 18) + 10), 'white'); d = ImageDraw.Draw(sheet)
        for i, (n, p) in enumerate(chunk):
            im = Image.open(p).convert('RGB').resize((tw, th)); x = 10 + (i % cols) * (tw + 10); y = 10 + (i // cols) * (th + 18)
            sheet.paste(im, (x, y)); d.text((x, y + th + 2), f"{n:02d}", fill='black')
        sheet.save(os.path.join(out, f"contact_{k // per + 1}.png"))
    return paths

def runs_of(el):
    out = []
    if 'shape' in el and 'text' in el['shape']:
        for te in el['shape']['text'].get('textElements', []):
            if 'textRun' in te and te['textRun'].get('content', '').strip():
                st = te['textRun'].get('style', {}); out.append((te['textRun']['content'], st.get('fontSize', {}).get('magnitude'), bool(st.get('bold'))))
    return out

def para_spacing(el):
    ls = []
    for te in el['shape']['text'].get('textElements', []):
        if 'paragraphMarker' in te: ls.append(te['paragraphMarker'].get('style', {}).get('lineSpacing', 100))
    return (sum(ls) / len(ls)) if ls else 100

def est_overflow(el, w, h, engine_built):
    """returns (needed_h, lines) or None"""
    rr = runs_of(el)
    if not rr: return None
    txt = E.text_of(el).rstrip('\n'); size = max([r[1] for r in rr if r[1]] or [0])
    if not size: return None
    inset_x = 2 * E.INSET_X if engine_built else 0; inset_y = 2 * E.INSET_Y if engine_built else 0
    width = max(w - inset_x, 10); ls = para_spacing(el)
    lines = 0
    for para in txt.split('\n'):
        cpl = max(int(width / (size * 0.5)), 1)
        lines += max(1, math.ceil(E.text_width(para, size, any(b for _, _, b in rr)) / width)) if para else 1
    need = lines * size * 1.21 * ls / 100.0
    return need, lines, h - inset_y

def report(deck, slides, start=1, engine_prefix=('n', 'c')):
    issues = {}
    for n, s in enumerate(slides, 1):
        if n < start: continue
        sid = s['objectId']; slide_built = bool(re.match(r'^n\d\d_', sid))
        probs = []; texts = []
        for el, tr in E.elements(s):
            x, y, w, h = E.geom(el, tr)
            built = bool(re.search(r'_e\d{3}$', el['objectId']))   # engine-created text box: visual box = shape minus insets
            if built and 'shape' in el and E.text_of(el).strip():
                x, y, w, h = x + E.INSET_X, y + E.INSET_Y, w - 2 * E.INSET_X, h - 2 * E.INSET_Y
            if 'image' in el and w >= 719 and abs(h) >= 404: continue   # full bleed
            if x < -0.6 or y < -0.6 or x + w > E.PAGE_W + 0.6 or y + h > E.PAGE_H + 0.6:
                probs.append(f"OUT {el['objectId']} ({x:.0f},{y:.0f},{w:.0f}x{h:.0f}) '{E.text_of(el).strip()[:30]}'")
            t = E.text_of(el).strip()
            if t:
                texts.append((el, x, y, w, h))
                r = est_overflow(el, w, h, False)
                if r and r[0] > r[2] + 2.5 and h > 2:
                    probs.append(f"OVERFLOW {el['objectId']} needs {r[0]:.0f} pt ({r[1]} lines) in {r[2]:.0f} pt: '{t[:40]}'")
                if slide_built:
                    small = [sz for _, sz, _ in runs_of(el) if sz and sz < E.MIN_FONT - 0.01]
                    if small: probs.append(f"FONT {el['objectId']} {min(small)} pt '{t[:30]}'")
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                a, b = texts[i], texts[j]
                ox = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]); oy = min(a[2] + a[4], b[2] + b[4]) - max(a[2], b[2])
                header_row = a[2] < 40 and b[2] < 40                       # kicker / tag pills / wordmark row
                stacked = oy <= 6 and ox > 3                                 # title over body inside one card (estimate tolerance)
                if ox > 3 and oy > 3 and not header_row and not stacked:
                    probs.append(f"OVERLAP '{E.text_of(a[0]).strip()[:24]}' x '{E.text_of(b[0]).strip()[:24]}' ({ox:.0f}x{oy:.0f} pt)")
        issues[n] = probs
        tag = 'OK ' if not probs else f"{len(probs):2d} "
        print(f"[{n:02d}] {tag} {sid}")
        for p in probs: print('      ', p)
    return issues

if __name__ == '__main__':
    a = sys.argv[1:]
    out = os.path.join(HERE, a[a.index('--out') + 1] if '--out' in a else 'thumbs_build')
    start = int(a[a.index('--from') + 1]) if '--from' in a else 1
    deck = E.Deck(); pres = deck.fetch(); slides = pres['slides']
    print(f"{len(slides)} slides in the deck")
    if '--no-thumbs' not in a:
        paths = thumbs(deck, slides, out, start); print(f"{len(paths)} thumbnails -> {out}")
    issues = report(deck, slides, start)
    json.dump({str(k): v for k, v in issues.items()}, open(os.path.join(out if os.path.isdir(out) else HERE, 'qa_report.json'), 'w'), indent=1)
    bad = sum(1 for v in issues.values() if v); print(f"{len(issues) - bad} clean, {bad} with findings")
