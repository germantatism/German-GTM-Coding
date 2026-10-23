import os, sys, json
sys.argv=[sys.argv[0]]
src_code = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
src_code = src_code.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", "SRC = '1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw'; DST = '1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo'")
exec(src_code)
# white Skydance asset = the right-hand image on the v1 closing slide (no recolor there)
cl_imgs = [e for e in S[89]['pageElements'] if e.get('image')]
cl_imgs.sort(key=lambda e: e['transform'].get('translateX', 0)); sky_cl = cl_imgs[-1]
print('closing skydance props recolor:', (sky_cl['image'].get('imageProperties') or {}).get('recolor'), 'size', sky_cl['size'])
cov1_sky = [e for e in S[0]['pageElements'] if e['objectId'].endswith('_0_1255')][0]
box_w = cov1_sky['size']['width']['magnitude'] * cov1_sky['transform']['scaleX']; box_h = cov1_sky['size']['height']['magnitude'] * cov1_sky['transform']['scaleY']
sw, sh = sky_cl['size']['width']['magnitude'], sky_cl['size']['height']['magnitude']
scale = min(box_w / sw, box_h / sh)
tf = {'scaleX': scale, 'scaleY': scale, 'translateX': cov1_sky['transform']['translateX'], 'translateY': cov1_sky['transform']['translateY'] + (box_h - sh * scale) / 2, 'unit': 'EMU'}
old = [e for e in D[0]['pageElements'] if e['objectId'] == 'im_15902_12']
run([{'deleteObject': {'objectId': e['objectId']}} for e in old] + [{'createImage': {'objectId': 'sky_cover_white', 'url': sky_cl['image']['contentUrl'], 'elementProperties': {'pageObjectId': D[0]['objectId'], 'size': sky_cl['size'], 'transform': tf}}}], 'cover skydance from closing asset')
