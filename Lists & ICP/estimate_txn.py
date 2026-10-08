import json,re,csv,math,warnings; warnings.filterwarnings("ignore")
M='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/49f121e3-1b42-499d-826d-45d993ea05ac/scratchpad/master'
out=json.load(open(M+'/master_final.json')); H=out[0]
NEW=['ICP check','Est. monthly transactions','Est. monthly online payment volume ($M)','Transaction estimate method']
for c in NEW:
    if c not in H: H.append(c)
I={h:i for i,h in enumerate(H)}
for r in out[1:]:
    while len(r)<len(H): r.append('')
def num(x):
    try: return float(str(x).replace(',',''))
    except: return None
ACQ={'Anysphere (Cursor)':'SpaceX','xAI (Grok)':'SpaceX','Intercom (Fin)':'Salesforce','Poke (The Interaction Company)':'Cognition','World Labs (Marble)':'AMD (pending)','Anyscale':'Nscale (pending)','Fathom':'Superhuman','Airtable':'Bending Spoons','Base44':'Wix','Cal AI':'MyFitnessPal','OpenRouter':'Stripe (pending)'}
DEF=re.compile(r'defen|robot|humanoid|drone|hardware|storage',re.I)
# ---- ICP check
def icp(r):
    name=r[1]; fit=r[I['Yuno fit']]; arr=num(r[I['ARR ($M)']]); seg=r[I['Segment']]; angle=r[I['Payments angle']]; model=r[I['Revenue model']]; hq=r[I['HQ']]; notes=(r[I['Notes']]+' '+r[I['Merge notes']])
    txt=(seg+' '+angle+' '+model).lower()
    if name.startswith('AIOS'): return 'No: bundled unverified tracker entries'
    if 'china' in hq.lower() or 'china-based' in notes.lower() or name in ('DeepSeek','Moonshot AI','MiniMax / Talkie, Zhipu','PictureThis (Glority)'): return 'No: China-based, not addressable'
    if DEF.search(seg): return 'No: defense, robotics or hardware; no online payers'
    if name=='OpenRouter': return 'No: captive to Stripe (acquisition pending)'
    if arr is not None and arr<=2 and ('pre-revenue' in txt or 'no product' in txt or 'free beta' in txt or 'pre-product' in txt or 'pre-launch' in txt or name in ('Hark','Physical Intelligence','humans&','Mirendil','Flapping Airplanes','Inferact')):
        if name=='Instinct': return 'Borderline: agentic commerce, merchant-fee model not live (watch)'
        return 'No: pre-revenue'
    if fit=='C' or not fit: return 'No: invoiced enterprise, no card or payout volume'
    if name in ACQ: return f'Borderline: acquired by {ACQ[name]}, route via parent'
    if 'app-store led' in txt or 'app stores' in model.lower() and 'web' not in model.lower(): return 'Borderline: app-store led, web checkout is the opening'
    if arr is not None and arr<3: return 'Borderline: under $3M ARR today'
    if 'payout' in txt: return 'Yes: payouts angle (contractor or creator payouts)'
    return 'Yes: online card volume (self-serve subscriptions or usage)'
# ---- ATV / card share
INFRA=re.compile(r'gpu|compute|cloud|data center|infrastructure|serverless|inference',re.I)
ENT=re.compile(r'enterprise|healthcare|legal|security|contact|clinical|compliance|customer-service|support automation',re.I)
CONS=re.compile(r'consumer|companion|creator|image|video|music|language|notetaker|presentation|photo|art|entertainment|dictation|meeting|education|learning|personal',re.I)
def atv(r):
    seg=r[I['Segment']]+' '+r[I['Revenue model']]
    if INFRA.search(seg): return 400,'usage invoices ~$400'
    if ENT.search(seg) and r[I['Yuno fit']]!='A': return 4000,'enterprise invoices ~$4,000'
    if CONS.search(seg): return 20,'consumer subscriptions ~$20'
    return 60,'prosumer or developer charges ~$60'
SHARE={'A':(0.9,'90%'),'B':(0.45,'45%'),'C':(0.08,'8%'),'':(0.1,'10%')}
# ---- overrides: (transactions per month, volume $M per month, method)
O={
'OpenAI':(50_000_000,1500,'~50M paid consumer and self-serve subscriptions billed monthly plus API prepaid top-ups; ~25% of the $70B run-rate assumed card-paid'),
'Anthropic':(6_000_000,270,'~5M consumer Claude subscriptions plus API top-ups; ~5% of run-rate card-paid, the rest invoiced API and enterprise'),
'Anysphere (Cursor)':(3_000_000,150,'~2.5M individual subscriptions at $20 to $200 plus team seats; ~45% of ARR self-serve'),
'Perplexity':(2_500_000,50,'~2.5M Pro and Max subscribers at ~$20 average; enterprise and API invoiced'),
'Midjourney':(1_400_000,42,'all revenue is web card subscriptions; $500M ARR at ~$30 average'),
'Replit':(1_500_000,35,'~80% of ARR self-serve at ~$23 average including credit top-ups'),
'Lovable':(2_000_000,45,'fully self-serve builders at ~$22 average incl. credits'),
'Higgsfield':(1_500_000,75,'credit subscriptions $19 to $129, ~90% of revenue self-serve, 75% outside the US'),
'Superhuman (formerly Grammarly)':(3_000_000,50,'consumer Pro at $12 to $15 plus business seats; ~85% card-paid'),
'Gamma':(500_000,7.5,'freemium self-serve, ~90% card-paid at ~$15 average'),
'Genspark':(900_000,19,'~100K paying seats on $20 to $250 tiers plus consumer Plus; ~90% card'),
'Emergent':(400_000,9,'200K paying customers billed monthly plus credit top-ups'),
'Apollo.io':(150_000,12,'~100K paying customers, mostly monthly cards; ~75% of ARR self-serve'),
'Gorgias':(25_000,5,'17K brands on monthly plans plus per-resolution overages'),
'Fireflies.ai':(150_000,4.5,'paying seats across 500K+ organizations, mostly monthly card'),
'Freed':(26_000,2.4,'26K clinicians at ~$92 average, monthly card'),
'Otter.ai':(300_000,7,'self-serve Pro and Business seats at ~$24; ~85% card'),
'Chai Research (Chai AI)':(700_000,7.5,'weekly $9.99 and monthly plans, mostly app-store IAP; web checkout a minority'),
'Chai':(700_000,7.5,'weekly $9.99 and monthly plans, mostly app-store IAP; web checkout a minority'),
'Character.AI':(250_000,2.5,'c.ai+ at $9.99, app stores plus web'),
'Replika (Luka, Inc.)':(80_000,1.2,'Pro and Ultra plans, mostly IAP; web on Stripe and PayPal'),
'Tolan (Portola)':(100_000,1,'100K+ subscribers, weekly and monthly IAP'),
'Meshy':(330_000,7.5,'credit subscriptions $20 to $100 plus API; self-serve card'),
'OpenArt':(350_000,7.5,'credit subscriptions $14 to $240 on Stripe'),
'Plaud':(250_000,7.5,'software subscriptions plus device sales on its web store'),
'Suno':(2_000_000,22,'~2M paid subscribers at ~$10 average, web and app stores'),
'ElevenLabs':(800_000,22,'self-serve creator plans plus API top-ups; ~45% of ARR card-paid, the rest enterprise'),
'HeyGen':(400_000,12,'self-serve creator and team plans at ~$30; ~70% card'),
'Runway':(300_000,7.5,'self-serve credits and plans; enterprise growing'),
'Canva':(15_000_000,300,'~90% self-serve Pro and Teams at ~$20; global card volume'),
'Notion':(4_000_000,65,'Plus and Business seats billed monthly, ~90% card'),
'Zapier':(400_000,25,'self-serve plans $20 to $100+, ~75% card'),
'Vercel (v0)':(300_000,20,'Pro seats plus usage, v0 plans; ~70% card'),
'Supabase':(200_000,10,'Pro plans plus usage overages on Stripe'),
'n8n':(100_000,6,'cloud plans billed in EUR via Paddle'),
'Webflow':(300_000,15,'site plans and seats, self-serve card'),
'Quizlet':(1_000_000,10,'consumer Plus subscriptions at ~$10'),
'DeepL':(600_000,14,'Pro individual and team plans at ~$24; ~85% card'),
'Picsart':(1_200_000,11,'Pro and Ultra plans at ~$9, web and app stores'),
'Mercor':(150_000,75,'~130K weekly contractor payouts (30K weekly actives) worth ~$60M/mo plus invoiced lab contracts; pay-ins invoiced'),
'Handshake (Handshake AI)':(200_000,45,'hourly payouts to ~50K active fellows paid weekly; ~50% of gross marketplace volume paid out'),
'Handshake':(200_000,45,'hourly payouts to ~50K active fellows paid weekly; ~50% of gross marketplace volume paid out'),
'Surge AI':(100_000,60,'annotator payouts, ~60% of $1.2B gross; pay-ins invoiced'),
'Scale AI':(400_000,40,'weekly payouts to Outlier and Remotasks contributors; pay-ins invoiced'),
'Micro1':(120_000,35,'contractor payouts ~60% of $700M gross run-rate'),
'Turing':(25_000,15,'monthly payouts to engaged developers and experts; pay-ins invoiced'),
'Snorkel AI':(10_000,4,'specialist payouts; enterprise pay-ins invoiced'),
'Labelbox (Alignerr)':(80_000,4,'weekly Alignerr payouts via PayPal and Stripe to ~20K active contributors'),
'Invisible Technologies':(20_000,5,'agent payouts; enterprise pay-ins invoiced'),
'AfterQuery':(20_000,5,'contractor payouts ~60% of gross'),
'Paraform':(2_000,4,'recruiter payouts on placement fees'),
'Listen Labs':(80_000,1,'incentive payouts to interview respondents; enterprise pay-ins invoiced'),
'Together AI':(60_000,40,'monthly usage invoices and prepaid credits; ~45% of ARR self-serve'),
'Fireworks AI':(50_000,37,'prepaid usage credits; ~45% self-serve'),
'Baseten':(10_000,20,'usage invoices, mostly larger customers'),
'Lambda':(40_000,55,'on-demand GPU usage by card for 200K+ developers; clusters invoiced'),
'Groq':(30_000,4,'developer pay-per-token top-ups; enterprise invoiced'),
'Deepgram':(20_000,4,'pay-as-you-go top-ups; Growth and enterprise invoiced'),
'AssemblyAI':(15_000,2,'pay-as-you-go top-ups; billing on Metronome'),
'Cerebras (Cerebras Inference)':(10_000,3,'inference top-ups from $10; systems invoiced'),
'Prime Intellect':(15_000,4,'GPU marketplace usage billed via dashboard'),
'Modal':(30_000,12,'usage-based self-serve compute'),
'Runpod':(150_000,18,'prepaid credits from a global developer long tail; ~90% card'),
'fal':(120_000,25,'prepaid usage credits; ~75% self-serve at ~$200 average'),
'Hugging Face':(150_000,6,'Pro subscriptions and compute usage; enterprise invoiced'),
'Cognition (Devin + Windsurf)':(800_000,34,'Windsurf and Devin self-serve plans; ~45% of ARR self-serve'),
'Cognition (Devin / Windsurf)':(800_000,34,'Windsurf and Devin self-serve plans; ~45% of ARR self-serve'),
'Instinct':(300_000,83,'agent-initiated purchases on users own cards (~$1B annualized GTV, half travel); Instinct is not the merchant of record yet'),
'Intercom (Fin)':(60_000,15,'30K customers on seat plans plus per-resolution usage; ~45% card'),
'Codeway':(1_200_000,22,'consumer app subscriptions, app-store IAP; web checkout is the opening'),
'HubX':(500_000,7.5,'consumer app subscriptions, app-store IAP'),
'Glam AI':(400_000,5,'consumer app subscriptions, app-store IAP'),
'Photoroom':(400_000,6,'consumer and SMB plans, mostly app stores plus API'),
'Speak':(500_000,7.5,'Premium at $18/mo or $84/yr, app stores and web; ~90% consumer'),
'ELSA Speak':(250_000,1.5,'annual web plans and IAP across 90M learners'),
'Poe (Quora)':(300_000,2.5,'subscription tiers $5 to $250, app stores and web'),
'Wispr Flow':(400_000,7.5,'Pro and Growth seats at $12 to $23, monthly card'),
'Luma AI':(250_000,6,'credit subscriptions $30 to $300; API'),
'Retell AI':(20_000,6,'usage-based self-serve at ~$300 average plus enterprise'),
'Vapi':(60_000,0.9,'usage billing by card for 1M+ developers; small ARR today'),
'Krea':(300_000,0.9,'credit plans $21 to $105; ARR still small'),
'Bolt.new (StackBlitz)':(150_000,3,'self-serve plans $25 to $30 plus tokens'),
'Anything':(80_000,0.15,'launch-period figure; subscriptions $19 to $199 plus credits'),
}
def fmt_txn(x):
    if x is None: return ''
    if x>=1_000_000: return str(int(round(x/1_000_000.0,1)*1_000_000)) if x<10_000_000 else str(int(round(x/1_000_000)*1_000_000))
    if x>=100_000: return str(int(round(x/10_000)*10_000))
    if x>=10_000: return str(int(round(x/1_000)*1_000))
    return str(int(round(x/100)*100)) if x>=1000 else str(int(round(x/10)*10))
n=0
for r in out[1:]:
    r[I['ICP check']]=icp(r)
    arr=num(r[I['ARR ($M)']]); name=r[1]
    if name in O:
        t,v,m=O[name]; r[I['Est. monthly transactions']]=fmt_txn(t); r[I['Est. monthly online payment volume ($M)']]=('%.1f'%v).rstrip('0').rstrip('.'); r[I['Transaction estimate method']]='Claude estimate, Oct 2026: '+m
    elif arr is None or arr<=0:
        r[I['Est. monthly transactions']]='0'; r[I['Est. monthly online payment volume ($M)']]='0'; r[I['Transaction estimate method']]='No revenue yet'
    else:
        a,alabel=atv(r); s,slabel=SHARE.get(r[I['Yuno fit']],SHARE[''])
        vol=arr/12.0*s; txn=vol*1e6/a
        r[I['Est. monthly transactions']]=fmt_txn(txn); r[I['Est. monthly online payment volume ($M)']]=('%.2f'%vol).rstrip('0').rstrip('.')
        r[I['Transaction estimate method']]=f"Claude estimate, Oct 2026: ARR/12 x {slabel} online share (Yuno fit {r[I['Yuno fit']] or 'n/a'}) = ${vol:,.1f}M/mo; divided by {alabel} average charge"
    n+=1
json.dump(out,open(M+'/master_final.json','w'),ensure_ascii=False)
csv.writer(open('/Users/germantatis/Desktop/GTMCoding/Lists & ICP/ai-prospects-master-german-samuel-2026-10.csv','w',newline='')).writerows(out)
import collections
c=collections.Counter(r[I['ICP check']].split(':')[0] for r in out[1:]); print('rows',n,dict(c))
print('ICP No reasons:',collections.Counter(r[I['ICP check']] for r in out[1:] if r[I['ICP check']].startswith('No')))
print('sample:')
for r in out[1:12]: print(f"  {r[1][:24]:24} | {r[I['ICP check']][:38]:38} | txn {r[I['Est. monthly transactions']]:>10} | vol ${r[I['Est. monthly online payment volume ($M)']]}M")
