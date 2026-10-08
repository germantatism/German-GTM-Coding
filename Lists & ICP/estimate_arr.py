import json,re,csv
M='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/49f121e3-1b42-499d-826d-45d993ea05ac/scratchpad/master'
out=json.load(open(M+'/master_final.json')); H=out[0]; I={h:i for i,h in enumerate(H)}
# company: (estimate $M, low, high, method)
E={
'Figure':(5,0,10,'robots-as-a-service at ~$1,000 per robot per month with only pilot fleets deployed; revenue immaterial versus the $39B valuation'),
'Thinking Machines Lab (Tinker)':(20,10,40,'Tinker usage API live since Oct 2025; a single tracker claims $200M (unverified), Sacra called it pre-revenue mid-2025; low tens of millions assumed'),
'Instinct':(0,0,2,'free invite-only beta; ~$1B gross transaction volume runs on users own cards and the merchant-fee model is not live'),
'World Labs (Marble)':(10,5,15,'Marble self-serve tiers $20 to $95/mo launched Nov 2025; AMD acquisition is strategic, not revenue based'),
'Hark':(1,0,3,'Sacra pre-revenue as of Sep 2026; $20 and $100 consumer tiers only just launched'),
'Physical Intelligence':(2,0,5,'pre-sales robotics lab; Sacra cites a $300 per robot per month subscription with few deployments'),
'humans&':(0,0,0,'pre-launch research lab; no product billed'),
'Moonshot AI':(500,300,1000,'trackers disagree 3x ($300M to $1B); midpoint of the reported range, China based'),
'Hippocratic AI':(40,20,60,'$3.5B valuation (Nov 2025), 50+ health system and payer contracts priced per agent hour; healthcare agent peers at this stage run $20M to $60M'),
'DeepL':(200,150,250,'200,000+ business customers at roughly $1,000 per year average plus consumer plans; $2B valuation (2024)'),
'Parallel Web Systems':(20,10,40,'$2B valuation five months after $740M (Apr 2026), 100K developers on usage pricing; hot API infra trades at 50x to 100x forward ARR'),
'Simile':(20,10,40,'$2B post-money (Jul 2026) with revenue up 5x in five months; enterprise contracts with CVS, Deloitte, Gallup; 50x to 100x multiple assumed'),
'Anyscale':(40,25,60,'$1.65B acquisition price by Nscale (Jul 2026) with revenue up 70% QoQ; 30x to 40x implied'),
'Flapping Airplanes':(0,0,0,'stealth research lab, no product'),
'Granola':(30,20,45,'$1.5B Series C (Mar 2026) on $14 to $35 per user per month plans; 40x to 60x growth-stage multiple'),
'AI21 Labs':(60,40,100,'$1.4B valuation with enterprise Jamba API deals; Samuel judged the $350M tracker figure too high'),
'Goodfire':(10,5,15,'$1.25B valuation (Feb 2026) for an interpretability lab with a handful of enterprise deployments'),
'LiveKit':(20,12,30,'aggregators put 2025 revenue near $10M; $1B Series C (Jan 2026), powers ChatGPT voice; roughly doubled assumed'),
'Mirendil':(0,0,0,'pre-product research lab'),
'Picsart':(150,120,200,'150M MAU and Pro/Ultra plans; company said revenue passed $100M in 2021, modest growth since'),
'Braintrust':(15,8,25,'$800M valuation (Feb 2026) on a $249/mo self-serve plan plus enterprise logos; ~50x multiple'),
'Inferact':(0,0,1,'paid serverless vLLM announced but not priced or launched'),
'Pinecone':(40,25,60,'10,000+ customers on usage pricing; $750M valuation (2023); mid-market vector DB peers'),
'Pika':(10,5,20,'consumer subscriptions $10 to $95/mo on a 500K+ community (2024); $470M valuation (Jun 2024)'),
'11x':(10,6,15,'~$10M ARR claimed for 2024 (disputed); flat to modest growth assumed after the 2025 leadership change'),
'Delve':(25,15,35,'1,500+ customers (Oct 2026) at a $15K to $25K compliance ACV'),
'Greptile':(5,3,8,'22,000 teams mostly on the free tier; $30 per seat Pro; $180M valuation'),
'Poke (The Interaction Company)':(5,2,10,'hundreds of thousands of users with a $19/mo Pro tier and low single-digit conversion; low nine-figure exit'),
'ELSA Speak':(20,10,33,'aggregator estimates range $9M to $32.5M; 90M learners on $90 to $100 per year web plans and IAP'),
'Aidoc':(60,50,70,'Samuel placed it just below the cut at about $60M'),
'Applied Compute':(50,40,60,'Samuel placed it just below the cut at about $50M'),
'Artlist':(300,250,350,'Samuel noted ~$300M latest revenue (subscription stock media); not independently verified'),
'AssemblyAI':(50,30,80,'aggregators cite $10M to $50M; usage API serving Zoom, Krisp, Fireflies and Granola suggests the upper end'),
'Bland AI':(15,8,25,'$50M Series C (Jun 2026), 250+ enterprise customers on per-minute pricing'),
'Candid Health':(57,50,65,'Samuel placed it just below the cut at about $57M'),
'Cartesia':(15,8,25,'$100M round (Oct 2025), 50K+ companies on self-serve tiers from $5 to $299/mo plus enterprise'),
'Delphi':(3,2,6,'2,000+ creators (Jun 2025) on $79 to $299/mo plans'),
'Elicit':(8,4,15,'5M registered researchers with a $49/mo Pro plan and low conversion'),
'Fireflies.ai':(60,40,90,'20M users and 500K+ organizations, profitable, $1B secondary valuation (Jun 2025); 15x to 25x multiple'),
'Hedra':(8,4,15,'2.5M users (May 2025) on $20 to $100/mo credit plans; $32M Series A'),
'Hex':(40,25,60,'1,500+ customer organizations at $36 to $75 per editor plus enterprise; $70M Series C (May 2025)'),
'Ideogram':(20,10,40,'consumer image subscriptions $20 to $60/mo; $80M Series A (Feb 2024)'),
'Inworld AI':(10,5,20,'developer tiers $25 to $1,500/mo plus enterprise; post-pivot to voice APIs'),
'Julius AI':(8,4,12,'2M+ users (May 2025) on $20 to $450/mo plans; $10M seed'),
'Krisp':(20,12,30,'200M devices deployed, consumer plans $8 to $30/mo plus call-center contracts'),
'Lovart':(15,8,30,'30M claimed users on credit subscriptions; $30M raised (2025)'),
'Motion':(25,12,50,'40,000 paying users at $19 to $29 per seat implies ~$12M; Samuel placed it near $50M (identity of the tracker figure is ambiguous)'),
'Nooks':(45,35,60,'~275 employees and 1,800+ teams after 4x ARR growth in 2024; sales-led ACVs'),
'Observe.AI':(60,40,90,'$213M raised, contact-center contracts such as 19,000 DoorDash agents; last priced in 2022'),
'Opus Clip':(40,20,60,'company stated eight-figure ARR in Aug 2024 and users grew to 16M by 2026'),
'Photon':(1,0.5,2,'$4.5M seed (Oct 2026), revenue up 10x in four months from a very small base'),
'Poe (Quora)':(30,15,60,'consumer tiers $5 to $250/mo across many models; Quora raised $75M in 2024 to grow it; no disclosure'),
'PolyAI':(50,40,60,'Samuel placed it just below the cut at about $50M'),
'Pylon':(18,12,25,'1,500+ customers at roughly $10K to $15K per year in seats and AI add-ons'),
'Reducto':(10,6,15,'crossed $1M ARR before Apr 2025 and cites 8x year-over-year growth; $75M Series B (Oct 2025)'),
'SeaArt':(50,40,60,'Samuel placed it just below the cut at about $50M'),
'Tavus':(10,5,18,'$40M Series B (Nov 2025), 100K+ developers on $59 to $397/mo tiers plus consumer app'),
'Warp':(15,8,25,'1M+ active developers with $20 to $200/mo plans; $73M raised'),
'Veed':(50,40,60,'Samuel placed it just below the cut at about $50M'),
}
n=0; missing=[]
for r in out[1:]:
    if r[I['ARR ($M)']]: continue
    e=E.get(r[1])
    if not e:
        missing.append(r[1]); continue
    est,lo,hi,method=e
    r[I['ARR ($M)']]=str(est); r[I['ARR as of']]='Oct 2026 (est.)'; r[I['Figure basis']]='Claude estimate, not disclosed'; r[I['Confidence']]='Derived estimate (low)'
    txt=f"Estimate ~${est}M (range ${lo}M to ${hi}M), Claude, Oct 2026: {method}"
    a=r[I['ARR (German research)']]
    r[I['ARR (German research)']]=(a+' | ' if a and not a.lower().startswith('not disclosed') else '')+txt if not a.lower().startswith('not disclosed') else a+' | '+txt
    mn=r[I['Merge notes']]; r[I['Merge notes']]=(mn+' | ' if mn else '')+'ARR ($M) is a Claude estimate, see ARR (German research)'
    n+=1
print('estimated',n,'| not estimated:',missing)
# re-sort and re-rank (same rules as organize.py)
def num(x):
    try: return float(str(x).replace(',',''))
    except: return None
def arr(r): return num(r[I['ARR ($M)']])
def val(r): return num(r[I['Valuation ($B)']])
rows=out[1:]
bundle=[r for r in rows if r[1].startswith('AIOS')]; rows=[r for r in rows if not r[1].startswith('AIOS')]
withv=[r for r in rows if arr(r) is not None]; without=[r for r in rows if arr(r) is None]
withv.sort(key=lambda r:(-arr(r), -(val(r) or -1), r[1].lower())); without.sort(key=lambda r:(-(val(r) or -1), r[1].lower()))
for i,r in enumerate(withv,1): r[I['Rank']]=str(i)
for r in without+bundle: r[I['Rank']]=''
out=[H]+withv+without+bundle
json.dump(out,open(M+'/master_final.json','w'),ensure_ascii=False)
csv.writer(open('/Users/germantatis/Desktop/GTMCoding/Lists & ICP/ai-prospects-master-german-samuel-2026-10.csv','w',newline='')).writerows(out)
print('ranked',len(withv),'| unranked',len(without)+len(bundle))
print('estimated rows now at ranks:',[(r[I['Rank']],r[1]) for r in withv if 'Claude estimate' in r[I['Figure basis']]][:12])
