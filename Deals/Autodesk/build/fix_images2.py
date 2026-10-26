# -*- coding: utf-8 -*-
"""Second pass of the image fixes (26 Oct 2026): the first uploads of the Moonactive card and of logo wall column 2
arrived corrupted (Drive showed no image metadata). Re-uploaded smaller files, verified by md5 here, then placed:
  moon_card_s.png        -> overlay on the Kraken cell of the trusted-by row
  subs_wall_col1_top.png -> rows 1 to 3 of logo wall column 2
  subs_wall_col1_bot.png -> rows 4 and 5 of logo wall column 2
Google's fetcher accepts https://lh3.googleusercontent.com/d/<id> once Drive has generated the image thumbnail.
  python3 fix_images2.py"""
import sys, os, time, hashlib, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs_lib as g
import fix_images as F

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
NEW = {'moon': ('1u-36dSrcqkCkFDVM_Xsh-_O2__Kn1BKp', 'moon_card_s.png'),
       'top': ('1XoYcE1PWK2WqPV3QQHDqzGvN7m83oTaQ', 'wall_col1_top.png'),
       'bot': ('1arI8iqYWiQd50vOP19bqAlYO7JsLgFM1', 'wall_col1_bot.png')}
s, d = F.s, F.d


def ready(fid):
    """True once Drive has image metadata and a thumbnail for the file (then the lh3 URL resolves)."""
    m = d.files().get(fileId=fid, fields='md5Checksum,hasThumbnail,imageMediaMetadata').execute()
    return m.get('hasThumbnail') and m.get('imageMediaMetadata'), m.get('md5Checksum')


if __name__ == '__main__':
    for k, (fid, local) in NEW.items():
        print(k, F.public(fid))
        ok, md5 = ready(fid)
        local_md5 = hashlib.md5(open(os.path.join(A, local), 'rb').read()).hexdigest()
        print(k, 'md5 match' if md5 == local_md5 else f'MD5 MISMATCH drive={md5} local={local_md5}', '| thumbnail ready' if ok else '| thumbnail pending')
    for a in range(20):
        if all(ready(fid)[0] for fid, _ in NEW.values()): break
        print('waiting for Drive thumbnails', a); time.sleep(30)
    P = s.presentations().get(presentationId=F.PID).execute()
    stale = [e['objectId'] for e in g.slide(P, F.TRUSTED)['pageElements'] if e['objectId'] == 'moon_card_overlay']
    stale += [e['objectId'] for e in g.slide(P, F.SUBS)['pageElements'] if e['objectId'] in ('ad_subs_wall_1', 'ad_subs_wall_1t', 'ad_subs_wall_1b')]
    if stale: g.run(s, F.PID, [{'deleteObject': {'objectId': o}} for o in stale], 'stale images removed')
    x = 36 + 971 / 1600 * 648; w = 305 / 1600 * 648
    print('moon ->', F.place('moon overlay', NEW['moon'][0], lambda u: F.img('moon_card_overlay', F.TRUSTED, u, x, 301, w, 66)))
    print('top ->', F.place('wall col 2 top', NEW['top'][0], lambda u: F.img('ad_subs_wall_1t', F.SUBS, u, 480, 104, 98, 114)))
    print('bot ->', F.place('wall col 2 bottom', NEW['bot'][0], lambda u: F.img('ad_subs_wall_1b', F.SUBS, u, 480, 224, 98, 74)))
    F.thumb(F.SUBS, 'thumbs_v5/s07.png'); F.thumb(F.TRUSTED, 'thumbs_v5/s13.png'); print('thumbs refreshed')
