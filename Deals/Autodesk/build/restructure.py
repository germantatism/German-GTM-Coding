# -*- coding: utf-8 -*-
"""26 Oct 2026 pm (German): orchestration first, deck shortened to 12 slides (m5 'vault and orchestration, one platform'
and 'billing depth' cut), slide 3 methods as logo chips, copy on exec / beyond / close reworded orchestration-first.
Targeted: never reruns build_deck.main() (that would wipe the logo wall and Moonactive overlay placed by fix_images*).
  python3 restructure.py"""
import sys, os, time, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
import gs_lib as g
import build_deck as B
import content as C
from googleapiclient.http import MediaFileUpload

CHIPS_FID = '1FQYy8xqCZfl1wWlIdgl9txf-Ty34JR4P'     # placeholder uploaded through German's Drive, SA writer
s, d, pid = g.svc(), g.drive(), B.DECK
get = lambda: s.presentations().get(presentationId=pid).execute()


def host(fid, path):
    """SA overwrites the placeholder with the exact bytes, makes it anyone-reader, waits for Drive's image metadata."""
    local = hashlib.md5(open(path, 'rb').read()).hexdigest()
    m = d.files().get(fileId=fid, fields='md5Checksum').execute()
    if m.get('md5Checksum') != local:
        d.files().update(fileId=fid, media_body=MediaFileUpload(path, mimetype='image/png')).execute(); print('  bytes updated')
    try:
        d.permissions().create(fileId=fid, body={'type': 'anyone', 'role': 'reader'}).execute(); print('  anyone-reader')
    except Exception as e:
        print('  permission:', str(e)[-80:])
    for a in range(30):
        m = d.files().get(fileId=fid, fields='md5Checksum,hasThumbnail,imageMediaMetadata').execute()
        if m.get('hasThumbnail') and m.get('imageMediaMetadata') and m.get('md5Checksum') == local:
            print('  drive ready', m['imageMediaMetadata'].get('width'), 'x', m['imageMediaMetadata'].get('height')); break
        print('  waiting for Drive thumbnail', a); time.sleep(20)
    url = f'https://lh3.googleusercontent.com/d/{fid}'
    open('TODAY_CHIPS_URL.txt', 'w').write(url); B.CHIPS_URL = url
    return url


def run_with_image(reqs, label):
    """Google's fetcher can lag the CDN: draw everything else first, then retry the image alone."""
    imgs = [r for r in reqs if 'createImage' in r]
    g.run(s, pid, [r for r in reqs if 'createImage' not in r], label)
    for a in range(12):
        try:
            g.run(s, pid, imgs, label + ' image'); return True
        except Exception as e:
            print('  image waiting', a, str(e)[-70:]); time.sleep(30)
    return False


def main():
    print('host chips:', host(CHIPS_FID, os.path.join('assets', 'today_chips.png')))
    P = get(); json.dump(P, open('backup_autodesk_prerestructure_' + time.strftime('%H%M%S') + '.json', 'w'))
    R = []
    for oid, t in C.EXEC.items(): g.set_text_id(P, B.S['exec'], oid, t, R)
    g.run(s, pid, R, 'exec text')
    P = get(); p = g.clear_body(s, pid, P, B.S['today'], kicker=C.TODAY['kicker'], title=C.TODAY['title']); B.draw_today(p)
    ok = run_with_image(p.R, 'today body')
    P = get(); p = B.fresh(s, pid, P, 'beyond', C.BEYOND['kicker'], C.BEYOND['title']); B.draw_beyond(p); g.run(s, pid, p.R, 'beyond body')
    P = get(); p = B.fresh(s, pid, P, 'close', C.CLOSE['kicker'], C.CLOSE['title']); B.draw_close(p); g.run(s, pid, p.R, 'close body')
    P = get(); N = []
    for key, text in C.NOTES.items():
        if key in B.ORDER: N += g.set_notes(s, pid, P, B.S[key], text)
    g.run(s, pid, N, 'speaker notes')
    g.finish(s, pid, [B.S[k] for k in B.ORDER])
    print('chips image placed:', ok)


if __name__ == '__main__':
    main()
