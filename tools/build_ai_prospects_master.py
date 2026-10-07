import json,re,csv,sys
M='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/49f121e3-1b42-499d-826d-45d993ea05ac/scratchpad/master'
g=json.load(open(M+'/german.json')); s=json.load(open(M+'/sam.json'))
GH=g[0]; G=g[1:]; SH=s['Top 100 by ARR'][0]; S=s['Top 100 by ARR'][1:]; NR=s['Not ranked'][1:]
def norm(n):
    n=n.lower(); n=re.sub(r'\(.*?\)','',n); n=n.replace('formerly','').replace('.ai','').replace('.com','').replace('.new','').replace(' ai','').replace('&','and')
    return re.sub(r'[^a-z0-9]','',n)
ALIAS={'falai':'fal','arena':'lmarena','chairesearch':'chai','anysphere':'cursor','thinkingmachineslab':'thinkingmachines'}
def key(n): k=norm(n); return ALIAS.get(k,k)
gi={key(r[0]):r for r in G}; si={key(r[1]):r for r in S}
# ---- classification for German-only rows: segment, revenue model, fit, payments angle
C={
'Anysphere (Cursor)':('AI coding / IDE','Self-serve subscriptions + usage + enterprise','B','Global self-serve developer base; now a SpaceX subsidiary (Samuel: sits in the SpaceX account)'),
'Vercel (v0)':('Frontend cloud / AI app builder','Self-serve subscriptions + usage + enterprise','A','Self-serve global developers; confirmed Stripe customer'),
'Factory':('AI coding agents','Self-serve subscriptions + enterprise','B','Self-serve tiers plus enterprise; small base'),
'Descript':('AI video / audio editing','Freemium self-serve subscriptions','A','Global creator subscriptions'),
'Krea':('AI creative suite','Freemium self-serve subscriptions','A','30M+ users, self-serve credits worldwide'),
'Hedra':('AI video (avatars)','Self-serve credit subscriptions','A','Self-serve creators'),
'Hex':('AI analytics workspace','Per-seat self-serve + enterprise','B','Mixed self-serve seats and enterprise'),
'Exa':('AI search API','Usage API (prepaid credits) + enterprise','B','Developer usage billing'),
'Browserbase':('Browser infrastructure for agents','Self-serve plans + usage + enterprise','B','Developer self-serve tiers with overages'),
'Abacus.AI':('AI assistant / enterprise AI platform','Low-cost per-user subscriptions + enterprise','A','Cheap global prosumer subscriptions (ChatLLM $10/mo)'),
'Bolt.new (StackBlitz)':('AI app builder','Self-serve subscriptions + usage','A','Fully self-serve global builders'),
'CodeRabbit':('AI code review','Per-developer subscriptions + enterprise','B','Self-serve seats; 17K customers worldwide'),
'Augment Code':('AI coding agent','Self-serve subscriptions + usage top-ups + enterprise','B','Self-serve plus enterprise'),
'Pika':('Consumer AI video','Consumer subscriptions (web + app)','A','Global consumer subscriptions'),
'Character.AI':('AI companion / entertainment','Freemium consumer subscription (web + app stores)','A','20M MAU, app-store heavy; web checkout is the opening'),
'Notion':('Productivity workspace (AI-heavy)','Freemium seats + usage-based AI credits','A','100M+ users, self-serve global seats (Samuel: AI-adjacent, worth targeting)'),
'You.com':('AI search API','Usage API (prepaid) + enterprise','B','API credits by card; consumer plans sold in-app'),
'Fathom':('AI meeting notes','Freemium self-serve + team plans','A','Self-serve SMB subscriptions'),
'Mintlify':('Developer documentation','Self-serve subscriptions + enterprise','B','Self-serve business plans'),
'Firecrawl':('Web data API','Self-serve subscriptions + credit top-ups + enterprise','A','150K+ organizations, self-serve global developers'),
'Anyscale':('Managed Ray / AI compute','Usage-based + committed contracts','B','Self-serve usage (Stripe Billing); being acquired by Nscale'),
'Opus Clip':('AI video clipping','Freemium creator subscriptions','A','16M users, global creator subscriptions'),
'Fireflies.ai':('AI meeting assistant','Freemium self-serve seats + enterprise','A','20M users, 500K orgs; India/UK heavy, Stripe only per 2024 call'),
'Vapi':('Voice AI agents API','Usage-based self-serve + plans + enterprise','A','1M+ developers paying usage by card'),
'Amp (Sourcegraph spinout)':('AI coding agent','Self-serve subscription + usage','B','Self-serve developers; small'),
'Poe (Quora)':('Multi-model AI subscription app','Consumer subscriptions (web + app stores)','A','Consumer tiers $5 to $250/mo; payouts to bot creators'),
'Cartesia':('Voice AI models','Self-serve plans + usage + enterprise','B','Developer self-serve tiers'),
'Bland AI':('Voice AI calling platform','Usage per minute + plans + enterprise','B','Usage billing; enterprise share rising'),
'Krisp':('Voice AI (noise cancellation, meetings)','Freemium prosumer subscriptions + call-center enterprise','A','Global consumer and SMB subscriptions'),
'Inworld AI':('Voice AI APIs','Self-serve tiers + enterprise','B','Developer self-serve tiers'),
'Writesonic':('AI search visibility / SEO','Self-serve subscriptions + enterprise','A','Self-serve marketing teams worldwide'),
'Tavus':('Conversational video AI','Developer self-serve tiers + consumer app + enterprise','B','Developer and consumer self-serve'),
'Julius AI':('AI data analyst','Freemium self-serve subscriptions','A','Self-serve prosumer subscriptions'),
'Elicit':('AI research assistant','Freemium self-serve subscriptions + enterprise','A','Self-serve researcher subscriptions worldwide'),
'Greptile':('AI code review','Per-seat self-serve + enterprise','B','Self-serve seats; small'),
'Lindy':('AI agent builder','Credit-based self-serve subscriptions + enterprise','B','Self-serve prosumer; small'),
'Delphi':('Creator AI clones','Creator subscriptions + custom','B','Creator subscriptions; clone monetization is a payouts angle'),
'Cline':('Open-source coding agent','Pay-as-you-go inference credits + enterprise','B','Credit top-ups by card; small'),
'Browser Use':('Browser agents infrastructure','Pay-as-you-go top-ups + enterprise','B','Developer top-ups; very small'),
'E2B':('Agent sandboxes','Self-serve plan + usage + enterprise','B','Developer usage; small'),
'Writer':('Enterprise generative AI','Enterprise contracts + small self-serve Starter','C','Invoiced enterprise; Starter card checkout is marginal'),
'Observe.AI':('Contact-center AI','Enterprise subscriptions by interaction volume','C','Invoiced enterprise'),
'Intercom (Fin)':('AI customer service','Self-serve seats + per-resolution usage + enterprise','B','30K customers on self-serve card plus usage billing; now a Salesforce unit'),
'Gorgias':('Ecommerce helpdesk AI','Self-serve tiered subscriptions + per-resolution AI','A','17K Shopify brands on self-serve card plans with usage overages'),
'Pylon':('B2B support platform','Per-seat subscriptions + AI add-ons','B','Self-serve seats; 1,500 customers'),
'Labelbox (Alignerr)':('AI training data','Enterprise contracts; contractor payouts','B','Payouts angle: Alignerr pays contributors weekly via PayPal and Stripe'),
'Snorkel AI':('AI training data','Enterprise contracts; contractor payouts','B','Payouts angle; enterprise pay-ins invoiced'),
'xAI (Grok)':('Foundation models','Consumer subscriptions (SuperGrok) + usage API','A','Global consumer subscriptions plus prepaid API; SpaceX subsidiary (Samuel: part of the SpaceX account)'),
'Thinking Machines Lab (Tinker)':('AI research lab / fine-tuning API','Usage API (Tinker)','B','Self-serve usage billing; early'),
'Cerebras (Cerebras Inference)':('AI chips + inference cloud','Systems sales + pay-per-token inference','B','Self-serve inference top-ups; public company since May 2026 (Samuel excluded as public)'),
'LangChain (LangSmith)':('Agent framework / LLMOps','Per-seat self-serve + usage + enterprise','B','7K+ self-serve customers plus enterprise'),
'Arize AI':('AI observability','Self-serve Pro + enterprise','B','Mostly enterprise; small self-serve tier'),
'AssemblyAI':('Speech API','Usage-based API (pay-as-you-go + enterprise)','B','Developer self-serve usage; billing runs on Metronome'),
'LiveKit':('Real-time voice / video infrastructure','Self-serve plans + usage + enterprise','B','300K developers; self-serve usage'),
'Replika (Luka, Inc.)':('AI companion app','Consumer subscriptions (app stores + web)','A','42M users; app-store heavy, web Pro on Stripe + PayPal, cards only'),
'Plaud':('AI notetaker hardware + software','Hardware sales + prosumer subscriptions','A','Global web store and subscriptions; #16 on a16z consumer spend list'),
'Tolan (Portola)':('AI companion app','Consumer subscriptions (app-store IAP)','B','App-store led; web checkout is the opening'),
'Beautiful.ai':('AI presentations','Self-serve subscriptions + enterprise','A','100K businesses on self-serve card checkout'),
'Invideo (invideo AI)':('AI video generator','Self-serve per-seat subscriptions with credits','A','50M users in 190 countries, self-serve card'),
'ELSA Speak':('AI language learning','Consumer subscriptions (app stores + web) + B2B seats','A','90M learners, Vietnam, SEA and LatAm heavy; web annual plans'),
'Freed':('AI medical scribe','Self-serve per-clinician subscriptions','A','26K clinicians on self-serve card; US-centric'),
'Anything':('AI app builder','Self-serve subscriptions + credits','A','Self-serve global builders; embeds Stripe payments in shipped apps'),
'Zapier':('Workflow automation (AI-heavy)','Freemium self-serve subscriptions + enterprise','A','3M+ businesses, self-serve global (Samuel: AI-adjacent, worth targeting)'),
'11x':('AI SDR agents','Enterprise annual contracts','C','Invoiced'),
'Artisan (Ava)':('AI BDR agents','Enterprise contracts (credit tiers)','C','Sales-led; piloting pay-per-response'),
'Nooks':('AI sales dialer','Enterprise subscriptions','C','Invoiced'),
'Listen Labs':('AI customer research','Enterprise contracts; respondent payouts','B','Payouts angle (pays interview respondents); enterprise pay-ins'),
'Hippocratic AI':('Healthcare voice agents','Usage-priced enterprise contracts','C','Invoiced enterprise'),
'Ambience Healthcare':('Healthcare AI scribe','Per-clinician enterprise contracts','C','Invoiced enterprise'),
'Delve':('AI compliance','Sales-led subscriptions','C','Invoiced'),
'humans&':('Frontier AI lab','Pre-revenue','C','No product yet; watch for a consumer launch'),
'Inferact':('Inference platform (vLLM)','Pre-revenue (paid serverless planned)','B','Usage billing once launched'),
'Mirendil':('Frontier AI lab','Pre-revenue','C','No product yet'),
'Flapping Airplanes':('Frontier AI lab','Pre-revenue','C','No product yet'),
'Instinct':('Personal AI agent','Free beta; merchant transaction fees planned','B','Agentic commerce: ~$1B annualized GTV on users own cards; merchant-fee model coming'),
'Poke (The Interaction Company)':('Personal AI agent','Self-serve subscriptions','A','Self-serve consumer subscriptions; now part of Cognition'),
'Photon':('Agent platform for messaging apps','Self-serve subscriptions + enterprise','B','Self-serve developer plans; very small'),
'Hark':('Personal AI / multimodal lab','Consumer subscriptions (app stores + web)','A','Consumer tiers $20 and $100 just launched'),
'Goodfire':('AI interpretability','Enterprise (sales-led)','C','Invoiced'),
'Simile':('AI simulation / digital twins','Enterprise contracts','C','Invoiced'),
'World Labs (Marble)':('World models / 3D generation','Self-serve subscriptions + API credits','A','Self-serve creators; being acquired by AMD'),
'Parallel Web Systems':('Web APIs for agents','Usage API (prepaid credits) + enterprise','B','100K developers paying usage'),
'Reducto':('Document parsing API','Usage API (prepaid credits) + enterprise','B','Self-serve credits plus enterprise'),
'Braintrust':('AI evals / observability','Self-serve Pro + enterprise','B','Self-serve Pro; mostly enterprise logos'),
}
STRIPE={'Vercel (v0)':'Confirmed - Stripe case study (Samuel: 2.6% auth-rate lift)','Anysphere (Cursor)':'Confirmed - Stripe customer (Samuel)','Replika (Luka, Inc.)':'Likely - web Pro checkout on Stripe + PayPal (German research)','Anyscale':'Likely - Stripe Billing per search snippet','Labelbox (Alignerr)':'Payouts via PayPal and Stripe (Alignerr), pay-ins not verified','Fireflies.ai':'Confirmed - Stripe only (Yuno call, Jul 2024)','AssemblyAI':'Not verified (billing and invoicing run on Metronome)','OpenArt':'Confirmed - Stripe named in terms of service'}
YSTAT={'Fireflies.ai':'Prior call Jul 2024 (Samuel V. + Jonathan) with Shreya Saraf, stalled; German new-thread draft to Shreya 7-Oct-2026','Anthropic':'German met Shaa in Apr 2026; subscriptions deck sent by Magdalena 15-Sep; German follow-up by WhatsApp + email 6-Oct','Genspark':'Winnie Wei (Head of Finance) replied 5-Oct-2026 (NetSuite rollout, later); German reply drafted for an in-person week of 26-Oct','Higgsfield':'ACTIVE DEAL (German), proposal from Sep Stripe country report','Gamma':'IN PLAY, business case sent by Magdalena; web deck /m/gamma-ai','Replika (Luka, Inc.)':'Research brief only (Jun 2026 AI-apps batch)','Chai Research (Chai AI)':'Research brief only (Jun 2026 AI-apps batch)','Perplexity':'Research brief only (Jun 2026 AI-apps batch)','xAI (Grok)':'Outside-in business case deck built by German','Replit':"Yuno 'Replit + Yuno at Stripe Sessions' deck exists (May 2026)"}
BELOW={'invideo','factory','descript','coderabbit','characterai','youcom','character'}; NOFIG={'pika','krea','hippocratic','vapi','assemblyai','cartesia','bolt'}
# ---- helpers
def parse_arr(t):
    if not t or t.lower().startswith('not disclosed'): return ('','','','No figure')
    m=re.search(r'\$\s?([\d.,]+)\s*([BMK])',t)
    if not m: return ('','','', '')
    v=float(m.group(1).replace(',','')); v= v*1000 if m.group(2)=='B' else (v/1000 if m.group(2)=='K' else v)
    d=re.search(r'\(([^)]*?(?:20\d\d)[^)]*)\)',t); asof=''
    if d:
        dd=re.search(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* 20\d\d|Q[1-4] 20\d\d|H[12] 20\d\d|end of 20\d\d|20\d\d)',d.group(1)); asof=dd.group(1) if dd else ''
    tl=t.lower()
    basis='Gross run-rate' if 'gross' in tl else ('Reported revenue' if 'gaap' in tl else ('Run-rate' if ('run-rate' in tl or 'run rate' in tl or 'annualized' in tl or 'arr' in tl) else 'Annual revenue'))
    conf='Estimate' if ('est.' in tl or '~' in t or 'sacra' in tl or 'aggregator' in tl or 'latka' in tl) else ('Company-confirmed' if ('company' in tl or 'site' in tl or 'ceo' in tl) else ('Press-reported' if ('press' in tl or 'techcrunch' in tl or 'bloomberg' in tl or 'reported' in tl) else 'Press-reported'))
    return (f"{v:.0f}" if v>=10 else f"{v:.1f}", asof, basis, conf)
def parse_val(notes):
    m=re.search(r'(?:at|valuing \w+ at|valuation)\s*(?:~|about |around |a reported |a )?\$([\d.]+)\s*B',notes)
    return m.group(1) if m else ''
def numclean(x):
    x=(x or '').strip().replace(',','')
    if re.fullmatch(r'-?\d+\.0+',x): return x.split('.')[0]
    return x
def hq(loc): return loc.replace(', CA',', US') if loc else ''
HEAD=SH+['List status','In German SF list','Company description','Location (German)','Plans / pricing','ARR (German research)','Users','Website','LinkedIn (company)',"German's notes",'Leads','Contacted','Payments lead: title','Payments lead: name','Payments lead: LinkedIn','Backup contact','Merge notes']
def gcols(r):
    r=r+['']*(15-len(r)); return [r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14]]
rows=[]; used=set()
# 1) Sam's 100
for sr in S:
    k=key(sr[1]); sr=sr+['']*(17-len(sr)); gr=gi.get(k); merge=[]
    row=list(sr); row[0]=numclean(row[0]); row[2]=numclean(row[2]); row[14]=numclean(row[14])
    if gr:
        used.add(k); gr=gr+['']*(15-len(gr))
        ga=gr[4]
        # merge notes on conflicts (keep Sam's numbers; note German's where newer or different)
        garr,gasof,_,_=parse_arr(ga)
        try: sv=float(sr[2].replace(',',''))
        except: sv=None
        if garr and sv is not None and abs(float(garr.replace(',',''))-sv)/max(sv,1)>0.15 and sr[1] not in ('Chai','Apollo.io','Higgsfield','Together AI'): merge.append(f"German ARR differs: {ga}")
        if gr[2] and hq(gr[2]).split(',')[0]!=sr[6].split(',')[0]: merge.append(f"German HQ: {gr[2]}")
        if sr[1]=='Chai': row[2]='100'; row[3]='Jul 2026'; row[5]='Company-confirmed'; merge.append('ARR updated to $100M (company site, Jul 2026); Samuel had $80M (Mar 2026)')
        if sr[1]=='Apollo.io': row[2]='200'; row[3]='Feb 2026'; row[4]='Run-rate (approaching)'; row[5]='Company-confirmed'; merge.append('ARR updated: approaching $200M (company statement, Feb 2026); Samuel had $150M (May 2025)')
        if sr[1]=='Together AI': row[2]='1150'; row[3]='Jul 2026'; merge.append('ARR updated to $1.15B annualized (Jul 2026); Samuel had ~$1B mid-2026')
        if sr[1]=='Meshy': row[6]='Sunnyvale, US'; row[7]='Yes'; merge.append('HQ set to Sunnyvale (LinkedIn)')
        if sr[1]=='Retell AI': row[6]='Palo Alto, US'
        if sr[1]=='Scale AI': merge.append('German: Sacra estimates ~$2B revenue for 2025; Samuel uses the $1B FY2026 projection')
        if sr[1]=='Higgsfield': merge.append('German: ~$700M annualized at the Aug 2026 raise; $1B is the CEO claim (Sep 2026)')
        if not row[13] and YSTAT.get(gr[0]): row[13]=YSTAT[gr[0]]
        elif YSTAT.get(gr[0]) and YSTAT[gr[0]] not in row[13]: row[13]=row[13]+' | '+YSTAT[gr[0]]
        if gr[7] and gr[7] not in ('',): pass
        row+= [f"Samuel top 100 #{row[0]}",'Yes']+gcols(gr)+['; '.join(merge)]
    else:
        row+= [f"Samuel top 100 #{row[0]}",'No']+['']*14+['']
    rows.append(row)
# 2) German-only
for gr in G:
    k=key(gr[0])
    if k in used or k in si: continue
    gr=gr+['']*(15-len(gr)); name=gr[0]
    arr,asof,basis,conf=parse_arr(gr[4]); seg,model,fit,angle=C.get(name,('','','',''))
    status='German SF list only'
    nk=norm(name)
    for nr in NR:
        if key(nr[0])==k: status=f"Samuel: not ranked ({nr[2]}) - {nr[3][:160]}"
    if nk in BELOW or k in BELOW: status='Samuel: not ranked (Below top 100, ~$50-70M)'
    if nk in NOFIG or k in NOFIG: status='Samuel: not ranked (No public ARR figure)'
    row=['',name,arr,asof,basis,conf,hq(gr[2]),'Yes',seg,model,fit,angle,STRIPE.get(name,'Not verified'),YSTAT.get(name,''),parse_val(gr[8]),'',"German's research (sources in German's notes)",status,'Yes']+gcols(gr)+['']
    rows.append(row); used.add(k)
# 3) Sam's not-ranked companies not in German's list
SKIP={'just below the cut','no public arr figure'}
extra_names={'Aidoc':'Just below the cut ($50-70M)','Candid Health':'Just below the cut ($50-70M), SF','Langdock':'Just below the cut ($50-70M)','Rogo':'Just below the cut ($50-70M)','Hebbia':'Just below the cut (~$50M)','Parloa':'Just below the cut (~$50M)','PolyAI':'Just below the cut (~$50M)','Heidi Health':'Just below the cut (~$50M)','Applied Compute':'Just below the cut (~$50M), SF','SeaArt':'Just below the cut (~$50M)','Motion':'Just below the cut (~$50M), Bay Area','Veed':'Just below the cut (~$50M)','Granola':'No public ARR figure','Warp':'No public ARR figure','Ideogram':'No public ARR figure','Lovart':'No public ARR figure','Physical Intelligence':'No public ARR figure','Figure':'No public ARR figure','DeepL':'No public ARR figure','Pinecone':'No public ARR figure','Picsart':'No public ARR figure'}
for nr in NR:
    nk=key(nr[0])
    if nk in used or nk in si: continue
    if nr[0].lower().startswith(('just below','no public')): continue
    rows.append(['',nr[0],'','','','','','','','','','','','','',nr[3],"Samuel's 'Not ranked' tab",f"Samuel: not ranked ({nr[2]})",'No']+['']*14+[f"Latest ARR per Samuel: {nr[1]}"])
for n,why in extra_names.items():
    rows.append(['',n,'','','','','','','','','','','','','','',"Samuel's 'Not ranked' tab",f"Samuel: not ranked ({why})",'No']+['']*14+[''])
# order: ARR desc, no-figure German rows, then Sam's not-ranked extras
def arrv(r):
    try: return float(r[2].replace(',',''))
    except: return -1
ranked=[r for r in rows if arrv(r)>=0]; nofig=[r for r in rows if arrv(r)<0 and r[18]=='Yes']; rest=[r for r in rows if arrv(r)<0 and r[18]!='Yes']
ranked.sort(key=lambda r:-arrv(r)); nofig.sort(key=lambda r:r[1].lower()); rest.sort(key=lambda r:r[1].lower())
out=[HEAD]+ranked+nofig+rest
with open(M+'/master.csv','w',newline='') as f: csv.writer(f).writerows(out)
json.dump(out,open(M+'/master.json','w'),ensure_ascii=False)
print('rows',len(out)-1,'| with ARR',len(ranked),'| german no-figure',len(nofig),'| sam not-ranked extras',len(rest),'| cols',len(HEAD))
miss=[r[1] for r in rows if r[18]=='Yes' and not r[8]]; print('german rows missing classification:',miss)
