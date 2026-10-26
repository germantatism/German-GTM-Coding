# -*- coding: utf-8 -*-
"""One-off image fixes for the Autodesk deck (26 Oct 2026):
  1. restore the trusted-by row 4 strip from the OnlyFans source deck (it was replaced by a broken PNG),
  2. overlay the Moonactive card on the Kraken cell of that row,
  3. place the subscriptions logo wall as three column images on the subs slide.
Small PNGs were uploaded through German's Drive and shared with the service account; this script makes them
anyone-reader and waits for Google's image CDN before creating the images.
  python3 fix_images.py"""
import sys, time, os, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs_lib as g

PID = '1H0NFvyWIPy6tGDQi7E_910v08y2Sokf_vkvvrF9o6-s'
SRC = '1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8'      # OnlyFans source deck (same slide ids)
TRUSTED, ROW4, SUBS = 'h7c266de662ba1cf0_9_611', 'h7c266de662ba1cf0_9_620', 'ad_subs'
FILES = {'moon': '1igm2QZCSlb8GAnfaDXT1ABKzt-fUXH1N', 'c0': '1a3yWPjBzpbrGpx_W0aFC_7Wp-zjGCRqV',
         'c1': '1Twewgp9WMwD9LTmmyGhvw5K8T2XOIZqR', 'c2': '1WKTH09drP1FsvtGYpWXQ7LhYARwJi6jw'}
PT = g.PT
s = g.svc(); d = g.drive()


def public(fid):
    try:
        d.permissions().create(fileId=fid, body={'type': 'anyone', 'role': 'reader'}).execute(); return 'anyone-reader'
    except Exception as e:
        return 'perm: ' + str(e)[:50]


def img(oid, page, url, x, y, w, h):
    return {'createImage': {'objectId': oid, 'url': url, 'elementProperties': {'pageObjectId': page,
            'size': {'width': {'magnitude': w * PT, 'unit': 'EMU'}, 'height': {'magnitude': h * PT, 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x * PT, 'translateY': y * PT, 'unit': 'EMU'}}}}


def place(label, fid, make):
    """Try the two public URL forms until Google's fetcher accepts one (CDN propagation takes minutes)."""
    err = ''
    for a in range(12):
        for form in ('https://lh3.googleusercontent.com/d/{}', 'https://drive.google.com/uc?export=download&id={}'):
            try:
                g.run(s, PID, [make(form.format(fid))], label); return form.format(fid)
            except Exception as e:
                err = str(e)[-60:]
        print('  ', label, 'waiting', a, err); time.sleep(30)
    return None


def thumb(page, path):
    t = s.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=page, thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(t['contentUrl'], path)


if __name__ == '__main__':
    for k, fid in FILES.items(): print(k, public(fid))
    # 1. restore row 4 from the source deck (a slides-images URL is accepted by the API)
    src = s.presentations().get(presentationId=SRC, fields='slides(objectId,pageElements(objectId,image(contentUrl)))').execute()
    orig = next(e['image']['contentUrl'] for sl in src['slides'] if sl['objectId'] == TRUSTED for e in sl['pageElements'] if e['objectId'] == ROW4)
    g.run(s, PID, [{'replaceImage': {'imageObjectId': ROW4, 'url': orig, 'imageReplaceMethod': 'CENTER_INSIDE'}}], 'row 4 restored')
    # 2. Moonactive card over the Kraken cell: card 4 spans px 971..1275 of the 1600 px strip (648 pt wide)
    P = s.presentations().get(presentationId=PID).execute()
    stale = [e['objectId'] for e in g.slide(P, TRUSTED)['pageElements'] if e['objectId'] == 'moon_card_overlay']
    stale += [e['objectId'] for e in g.slide(P, SUBS)['pageElements'] if e['objectId'].startswith('ad_subs_wall')]
    if stale: g.run(s, PID, [{'deleteObject': {'objectId': o}} for o in stale], 'stale images removed')
    x = 36 + 971 / 1600 * 648; w = 305 / 1600 * 648
    print('moon overlay ->', place('moon overlay', FILES['moon'], lambda u: img('moon_card_overlay', TRUSTED, u, x, 301, w, 66)))
    # 3. logo wall: three columns of 98 x 194 pt with 6 pt gaps, at x 376, y 104
    for i, k in enumerate(('c0', 'c1', 'c2')):
        print('wall col', i, '->', place(f'wall col {i}', FILES[k], lambda u, i=i: img(f'ad_subs_wall_{i}', SUBS, u, 376 + i * 104, 104, 98, 194)))
    os.makedirs('thumbs_v5', exist_ok=True)
    thumb(SUBS, 'thumbs_v5/s07.png'); thumb(TRUSTED, 'thumbs_v5/s13.png'); print('thumbs refreshed')
