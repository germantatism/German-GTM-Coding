"""Engine: replace text in a copied Google Slides deck while preserving per-paragraph styles."""
import json, re, sys, time
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN='/Users/germantatis/.config/yuno-slides/token.json'
def service():
    creds=Credentials.from_authorized_user_file(TOKEN)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request()); open(TOKEN,'w').write(creds.to_json())
    return build('slides','v1',credentials=creds,cache_discovery=False)

def compose(a,b):
    sx=a.get('scaleX',1)*b.get('scaleX',1)+a.get('shearX',0)*b.get('shearY',0)
    sy=a.get('shearY',0)*b.get('shearX',0)+a.get('scaleY',1)*b.get('scaleY',1)
    tx=a.get('scaleX',1)*b.get('translateX',0)+a.get('shearX',0)*b.get('translateY',0)+a.get('translateX',0)
    ty=a.get('shearY',0)*b.get('translateX',0)+a.get('scaleY',1)*b.get('translateY',0)+a.get('translateY',0)
    return {'scaleX':sx,'scaleY':sy,'translateX':tx,'translateY':ty}

def elements(slide):
    """flat list of (element, absolute transform) incl. group children"""
    out=[]
    def walk(el,par=None):
        tr=el.get('transform',{})
        if par: tr=compose(par,tr)
        if 'elementGroup' in el:
            for ch in el['elementGroup']['children']: walk(ch,tr)
        else: out.append((el,tr))
    for el in slide.get('pageElements',[]): walk(el)
    return out

def text_of(el):
    if 'shape' in el and 'text' in el['shape']:
        return ''.join(te.get('textRun',{}).get('content','') for te in el['shape']['text'].get('textElements',[]))
    return ''

def pos(el,tr):
    return (round(tr.get('translateX',0)/12700), round(tr.get('translateY',0)/12700))

def paragraphs(el):
    """[{'text','style','pstyle','bullet'}] per paragraph from original textElements"""
    paras=[]; cur=None
    for te in el['shape']['text'].get('textElements',[]):
        if 'paragraphMarker' in te:
            cur={'text':'','style':None,'pstyle':te['paragraphMarker'].get('style',{}),'bullet':te['paragraphMarker'].get('bullet')}
            paras.append(cur)
        elif 'textRun' in te and cur is not None:
            cur['text']+=te['textRun'].get('content','')
            if cur['style'] is None and te['textRun'].get('content','').strip():
                cur['style']=te['textRun'].get('style',{})
    for p in paras:
        if p['style'] is None: p['style']={}
    return paras

TEXT_FIELDS=['bold','italic','underline','fontSize','foregroundColor','fontFamily','weightedFontFamily','baselineOffset','smallCaps','strikethrough']
PARA_FIELDS=['alignment','lineSpacing','spaceAbove','spaceBelow','indentStart','indentEnd','indentFirstLine','direction','spacingMode']

def runs_of(el):
    r=[]
    for te in el['shape']['text'].get('textElements',[]):
        if 'textRun' in te and te['textRun'].get('content','').strip('\n\x0b'):
            st=te['textRun'].get('style',{}); r.append((te['textRun']['content'],st))
    return r

def _style_reqs(oid,start,end,st,ps=None,bullet=False):
    out=[]
    s={k:v for k,v in st.items() if k in TEXT_FIELDS}
    if s and end>start: out.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'style':s,'fields':','.join(s.keys())}})
    if ps:
        p={k:v for k,v in ps.items() if k in PARA_FIELDS}
        if p and end>start: out.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'style':p,'fields':','.join(p.keys())}})
    if bullet and end>start: out.append({'createParagraphBullets':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'bulletPreset':'BULLET_DISC_CIRCLE_SQUARE'}})
    return out

def replace_requests(el,new_text):
    """delete all, insert new, re-apply styles: per paragraph, and two-run split (number + label) when the original had it"""
    oid=el['objectId']; new_text=new_text.rstrip('\n')
    paras=paragraphs(el); rr=runs_of(el)
    def sig(st): return (st.get('fontSize',{}).get('magnitude'),st.get('bold'))
    two=len([p for p in paras if p['text'].strip()])==1 and len(rr)>=2 and sig(rr[0][1])!=sig(rr[-1][1])
    if two and ('\n' in new_text or '\x0b' in new_text or '  ' in new_text):
        reqs=[{'deleteText':{'objectId':oid,'textRange':{'type':'ALL'}}},{'insertText':{'objectId':oid,'insertionIndex':0,'text':new_text}}]
        sep='\n' if '\n' in new_text else ('\x0b' if '\x0b' in new_text else '  ')
        head,tail=new_text.split(sep,1); ps=paras[0]['pstyle'] if paras else {}
        reqs+=_style_reqs(oid,0,len(head),rr[0][1],ps)
        reqs+=_style_reqs(oid,len(head)+len(sep),len(new_text),rr[-1][1],ps)
        return reqs
    reqs=[{'deleteText':{'objectId':oid,'textRange':{'type':'ALL'}}},
          {'insertText':{'objectId':oid,'insertionIndex':0,'text':new_text}}]
    lines=new_text.split('\n'); start=0
    nonempty=[p for p in paras if p['text'].strip()] or paras
    for i,line in enumerate(lines):
        src=nonempty[min(i,len(nonempty)-1)] if nonempty else None
        end=start+len(line)
        if src and len(line)>0:
            st={k:v for k,v in src['style'].items() if k in TEXT_FIELDS}
            if st:
                reqs.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'style':st,'fields':','.join(st.keys())}})
            ps={k:v for k,v in src['pstyle'].items() if k in PARA_FIELDS}
            if ps:
                reqs.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'style':ps,'fields':','.join(ps.keys())}})
            if src.get('bullet'):
                reqs.append({'createParagraphBullets':{'objectId':oid,'textRange':{'type':'FIXED_RANGE','startIndex':start,'endIndex':end},'bulletPreset':'BULLET_DISC_CIRCLE_SQUARE'}})
        start=end+1
    return reqs

def run(svc,pid,reqs,chunk=400,label=''):
    done=0
    for i in range(0,len(reqs),chunk):
        part=reqs[i:i+chunk]
        for attempt in range(3):
            try:
                svc.presentations().batchUpdate(presentationId=pid,body={'requests':part}).execute(); break
            except Exception as e:
                if attempt==2: raise
                print(f"  retry {attempt+1} on chunk {i} ({label}): {str(e)[:120]}"); time.sleep(3)
        done+=len(part)
    print(f"  applied {done} requests {label}")

class Slide:
    def __init__(self,slide):
        self.slide=slide; self.id=slide['objectId']; self.els=elements(slide)
    def by_suffix(self,suf):
        m=[el for el,tr in self.els if el['objectId'].endswith('_'+str(suf))]
        if len(m)!=1: raise KeyError(f"suffix {suf} matched {len(m)} in {self.id}")
        return m[0]
    def by_text(self,prefix):
        m=[el for el,tr in self.els if text_of(el).strip().startswith(prefix)]
        if not m: raise KeyError(f"text '{prefix[:40]}' not found in {self.id}")
        return m
    def near(self,x,y,tol=7):
        m=[el for el,tr in self.els if text_of(el).strip() and abs(pos(el,tr)[0]-x)<=tol and abs(pos(el,tr)[1]-y)<=tol]
        return m
    def texts(self):
        return [(el['objectId'].split('_')[-1],pos(el,tr),text_of(el).strip()) for el,tr in self.els if text_of(el).strip()]
