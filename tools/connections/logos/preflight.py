"""Download every logo URL in the y.uno directory export, keep PNG/JPEG only, record aspect (w/h). Output usable.json + aspect.json + bad.json"""
import json, re, io, sys, os, urllib.request, concurrent.futures as cf
from PIL import Image
D = json.load(open(sys.argv[1])); OUT = sys.argv[2]
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
def fetch(e):
    url = e.get('logo') or ''
    if not url: return (nk(e['name']), None, 'no url')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        b = urllib.request.urlopen(req, timeout=25).read()
        im = Image.open(io.BytesIO(b)); fmt = im.format; w, h = im.size
        if fmt not in ('PNG', 'JPEG'): return (nk(e['name']), None, f'format {fmt}')
        # trim transparent/white margins for a truer aspect
        try:
            rgba = im.convert('RGBA'); bbox = rgba.getbbox()
            if bbox: w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        except Exception: pass
        return (nk(e['name']), {'url': url, 'aspect': round(w / h, 3), 'w': w, 'h': h, 'fmt': fmt}, None)
    except Exception as ex: return (nk(e['name']), None, str(ex)[:120])
usable, aspect, bad = {}, {}, {}
with cf.ThreadPoolExecutor(12) as ex:
    for k, ok, err in ex.map(fetch, D):
        if ok: usable[k] = ok['url']; aspect[k] = ok['aspect']
        else: bad[k] = err
json.dump(usable, open(os.path.join(OUT, 'usable.json'), 'w')); json.dump(aspect, open(os.path.join(OUT, 'aspect.json'), 'w')); json.dump(bad, open(os.path.join(OUT, 'bad.json'), 'w'), indent=0)
print('usable', len(usable), 'bad', len(bad)); print({k: v for k, v in list(bad.items())[:40]})
