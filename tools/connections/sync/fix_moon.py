import os, sys, json
sys.argv=[sys.argv[0]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0])
logos = [s for s in D if s['objectId'].startswith('n05_')][0]
kr = [e for e in logos['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_0')][0]
neg = [e for e in logos['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_2')][0]
moon = [e for e in S[5]['pageElements'] if e.get('image') and 'moonactive' in e['image'].get('sourceUrl', '')][0]
print('donor props', json.dumps(neg['image'].get('imageProperties', {}).get('recolor', {}).get('name')), neg['image'].get('imageProperties', {}).get('brightness'))
run([{'duplicateObject': {'objectId': neg['objectId'], 'objectIds': {neg['objectId']: 'moon_logo'}}},
     {'replaceImage': {'imageObjectId': 'moon_logo', 'url': moon['image']['sourceUrl'], 'imageReplaceMethod': 'CENTER_INSIDE'}},
     {'updatePageElementTransform': {'objectId': 'moon_logo', 'transform': moon['transform'], 'applyMode': 'ABSOLUTE'}},
     {'deleteObject': {'objectId': kr['objectId']}}], 'moonactive via negative donor')
