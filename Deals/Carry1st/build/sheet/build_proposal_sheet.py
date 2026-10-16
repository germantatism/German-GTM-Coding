# Builds the "Carry1st + Yuno · Proposal breakdown" Google Sheet (formula-linked, house format). 16 Oct 2026.
import warnings, os, json; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
SID='1oIq55KHyjLA4R73_WtDLYLB5bG93rkh3WGcA6A3Mtmw'
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/spreadsheets'])
sh=build('sheets','v4',credentials=creds,cache_discovery=False).spreadsheets()
M=json.load(open(os.path.join(os.path.dirname(__file__),'..','model','model_numbers.json')))
TABS=['Summary','What the $7,500 covers','Cost by volume','Value by scenario','Fixed fee vs share of sales','Assumptions']
meta=sh.get(spreadsheetId=SID).execute()
existing={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
reqs=[]
first=meta['sheets'][0]['properties']['sheetId']
for i,t in enumerate(TABS):
    if t in existing: continue
    if i==0: reqs.append({'updateSheetProperties':{'properties':{'sheetId':first,'title':t},'fields':'title'}})
    else: reqs.append({'addSheet':{'properties':{'title':t,'index':i}}})
if reqs: sh.batchUpdate(spreadsheetId=SID,body={'requests':reqs}).execute()
meta=sh.get(spreadsheetId=SID).execute(); ids={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
def q(t): return "'"+t+"'"
V={}
# ---------- Assumptions
A=[['Assumption','Value','Notes'],
   ['Platform fee, a month (USD)',7500,'Flat, billed annually'],
   ['Monthly sales included in the platform fee (USD)',500000,'Each month, no rollover'],
   ['Band 1: $500K to $2M of monthly sales, rate',0.004,'40 bps'],
   ['Band 2: $2M to $5M, rate',0.003,'30 bps'],
   ['Band 3: $5M to $10M, rate',0.002,'20 bps'],
   ['Band 4: above $10M, rate',0.001,'10 bps'],
   ['Average ticket (USD)',10,'Carry1st estimate, Oct 2026'],
   ['Median ticket (USD)',5,'Carry1st estimate, Oct 2026'],
   ['Run rate, monthly sales (USD)',4500000,'Carry1st estimate, end 2027'],
   ['Senior payments engineer, loaded cost a year (USD)',130000,'Yuno estimate ($2,500 a week)'],
   ['Payments consultant, rate per hour (USD)',200,'Yuno estimate, fractional senior payments consultant'],
   ['Payments solutions engineer, rate per hour (USD)',175,'Yuno estimate, fractional technical consultant'],
   ['Only approved sales are billed','Yes','Declines and card verification attempts cost nothing']]
V['Assumptions']=A
AS=q('Assumptions')
PF=f"{AS}!$B$2"; INC=f"{AS}!$B$3"; R1=f"{AS}!$B$4"; R2=f"{AS}!$B$5"; R3=f"{AS}!$B$6"; R4=f"{AS}!$B$7"; TK=f"{AS}!$B$8"; MD=f"{AS}!$B$9"; RR=f"{AS}!$B$10"; ENG=f"{AS}!$B$11"; KAMR=f"{AS}!$B$12"; TAMR=f"{AS}!$B$13"
def usage(c): return f"(MAX(0,MIN({c},2000000)-{INC})*{R1}+MAX(0,MIN({c},5000000)-2000000)*{R2}+MAX(0,MIN({c},10000000)-5000000)*{R3}+MAX(0,{c}-10000000)*{R4})"
# ---------- What the $7,500 covers
C=[['What the platform fee covers','What Carry1st gets','How we value it','Quantity','Unit','Unit cost (USD)','Value a month (USD)','Value a year (USD)']]
items=[
 ['First $500K of monthly sales','No usage fee on the first $500K of approved sales, every month','The usage it would carry at the first band (40 bps)',f'={INC}','USD of sales',f'={R1}'],
 ['Dedicated Key Account Manager (KAM)','Payments strategy, provider negotiation including EBANX, quarterly reviews','Fractional senior payments consultant',20,'hours a month',f'={KAMR}'],
 ['Dedicated Technical Account Manager (TAM)','Integration support, routing setup, incident escalation','Fractional payments solutions engineer',20,'hours a month',f'={TAMR}'],
 ['Orchestration and rules engine','Rules by country, card BIN, amount and method across every provider','Built and maintained in house',0.5,'senior engineer (FTE)',f'={ENG}/12'],
 ['Smart routing and retries','Each payment to the route most likely to approve; soft declines retried on another provider','Built and maintained in house',0.25,'senior engineer (FTE)',f'={ENG}/12'],
 ['Monitors and auto-failover','Detects approval drops and outages, shifts traffic, returns it on recovery','Observability tooling plus on-call',1,'month',1500],
 ['Connector maintenance','EBANX and every provider added later kept current by Yuno','In-house upkeep per provider',2,'providers (0.15 FTE each)',f'=0.15*{ENG}/12'],
 ['Checkout and SDKs','Localized web and mobile checkout with local methods per market','Build amortized over two years plus upkeep',1,'month',1500],
 ['Dashboard and insights','Approval, cost and provider performance in one view','BI tooling and analyst time',1,'month',1000],
 ['PCI token vault','Cards stored once and usable with any provider','Standalone vault service',1,'month',1000]]
for i,it in enumerate(items):
    r=i+2; C.append(it+[f'=D{r}*F{r}',f'=G{r}*12'])
n=len(items)+1
C.append(['Total value covered','','','','','',f'=SUM(G2:G{n})',f'=SUM(H2:H{n})'])
C.append(['Platform fee Carry1st pays','','','','','',f'={PF}',f'={PF}*12'])
C.append(['Value for every $1 of platform fee','','','','','',f'=G{n+1}/G{n+2}',''])
C.append(['What Carry1st keeps, value minus fee','','','','','',f'=G{n+1}-G{n+2}',f'=H{n+1}-H{n+2}'])
V['What the $7,500 covers']=C
CV=q('What the $7,500 covers'); TOTV=f"{CV}!$G${n+1}"; MULT=f"{CV}!$G${n+3}"
# ---------- Cost by volume
B=[['Monthly sales (USD)','Transactions at average ticket','Included in platform fee (USD)','Band 1, 40 bps (USD)','Band 2, 30 bps (USD)','Band 3, 20 bps (USD)','Band 4, 10 bps (USD)','Usage total (USD)','Platform fee (USD)','Total a month (USD)','Total a year (USD)','All-in, bps of sales','Per transaction at $10','Per transaction at $5']]
vols=[250000,500000,1000000,2000000,3000000,4500000,5000000,7500000,10000000,15000000,20000000]
for i,v in enumerate(vols):
    r=i+2
    B.append([v,f'=A{r}/{TK}',f'=MIN(A{r},{INC})',f'=MAX(0,MIN(A{r},2000000)-{INC})*{R1}',f'=MAX(0,MIN(A{r},5000000)-2000000)*{R2}',f'=MAX(0,MIN(A{r},10000000)-5000000)*{R3}',f'=MAX(0,A{r}-10000000)*{R4}',f'=SUM(D{r}:G{r})',f'={PF}',f'=H{r}+I{r}',f'=J{r}*12',f'=J{r}/A{r}*10000',f'=J{r}/B{r}',f'=J{r}/(A{r}/{MD})'])
V['Cost by volume']=B
# ---------- Value by scenario
S=M['model']; T=M['ttm']
def ann(sc,k): return round(S[sc]['450000'][k]*12)
D=[['Annual value at the $4.5M run rate (USD)','Conservative','Base','Optimistic','What it is'],
   ['Approval uplift',ann('Conservative','l2c'),ann('Base','l2c'),ann('Optimistic','l2c'),'Routing and retries recover sales a single provider declines'],
   ['Local methods',ann('Conservative','l3c'),ann('Base','l3c'),ann('Optimistic','l3c'),'Methods one provider does not carry (MODO, QR, Bre-B, Nequi, Bolivia cards)'],
   ['Processing cost',ann('Conservative','l1'),ann('Base','l1'),ann('Optimistic','l1'),'Volume moves to the cheaper route; every rate has a real alternative'],
   ['Integrations avoided',ann('Conservative','l4'),ann('Base','l4'),ann('Optimistic','l4'),'Market-by-market EBANX work, later builds and upkeep Carry1st does not carry'],
   ['Recurring value a year','=SUM(B2:B5)','=SUM(C2:C5)','=SUM(D2:D5)','Every year at run rate'],
   ['Yuno cost a year',f"={q('Cost by volume')}!$K$7",f"={q('Cost by volume')}!$K$7",f"={q('Cost by volume')}!$K$7",'$21,000 a month at $4.5M of monthly sales'],
   ['Net value a year','=B6-B7','=C6-C7','=D6-D7','What Carry1st keeps after paying Yuno'],
   ['Value for every $1 paid to Yuno','=B6/B7','=C6/C7','=D6/D7',''],
   ['Time to market, 2027 only',round(T['Conservative']['l5']),round(T['Base']['l5']),round(T['Optimistic']['l5']),'Run rate reached in Nov, Sep or Aug 2027 instead of Dec 2027'],
   ['2027 total value','=B6+B10','=C6+C10','=D6+D10','Recurring value plus time to market'],
   ['2027 value for every $1 paid to Yuno','=B11/B7','=C11/C7','=D11/D7','']]
V['Value by scenario']=D
# ---------- Fixed fee vs share of sales
F=[['At 450,000 transactions a month','Ticket $5 (median)','Ticket $10 (average)','Ticket $15'],
   ['Monthly sales (USD)','=450000*5','=450000*10','=450000*15'],
   ['Yuno, share of sales (USD a month)']+[f'={usage(c+"2")}+{PF}' for c in 'BCD'],
   ['Yuno, bps of sales']+[f'={c}3/{c}2*10000' for c in 'BCD'],
   ['A fixed $0.05 per transaction (USD a month)']+['=450000*0.05']*3,
   ['Fixed $0.05, bps of sales']+[f'={c}5/{c}2*10000' for c in 'BCD'],
   ['A fixed $0.10 per transaction (USD a month)']+['=450000*0.10']*3,
   ['Fixed $0.10, bps of sales']+[f'={c}7/{c}2*10000' for c in 'BCD'],
   ['Reading','A fixed fee doubles as a share of sales when the ticket halves; a share of sales does not.','','']]
V['Fixed fee vs share of sales']=F
# ---------- Summary
CB=q('Cost by volume'); VS=q('Value by scenario')
Sm=[['Carry1st + Yuno: the proposal at a glance','',''],
    ['The price','',''],
    ['Platform fee a month',f'={PF}','Covers the first $500K of monthly sales, the KAM and TAM, orchestration, routing, monitors, failover, vault, checkout and dashboard'],
    ['Usage above $500K a month','40 / 30 / 20 / 10 bps','Bands at $2M, $5M and $10M; each band charged only on the sales inside it'],
    ['Yuno at launch ($500K a month)',f'={CB}!$J$3','Platform fee only, nothing per transaction'],
    ['Yuno at $2M a month',f'={CB}!$J$5',f'={CB}!$L$5'],
    ['Yuno at the $4.5M run rate',f'={CB}!$J$7',f'={CB}!$L$7'],
    ['What the platform fee is worth','',''],
    ['Value covered by the platform fee, a month',f'={TOTV}','If Carry1st bought or built it separately'],
    ['Value for every $1 of platform fee',f'={MULT}',''],
    ['What the business case returns (base case)','',''],
    ['Recurring value a year',f'={VS}!$C$6','Approval, local methods, processing cost, integrations'],
    ['Yuno cost a year',f'={VS}!$C$7',''],
    ['Net value a year',f'={VS}!$C$8',''],
    ['Value for every $1 paid to Yuno',f'={VS}!$C$9',''],
    ['Plus 2027 time to market',f'={VS}!$C$10','Reaching the run rate in Sep instead of Dec 2027']]
V['Summary']=Sm
data=[{'range':f"{q(t)}!A1",'values':V[t]} for t in TABS]
for t in TABS: sh.values().clear(spreadsheetId=SID,range=f"{q(t)}!A1:Z200").execute()
sh.values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':data}).execute()
# ---------- formatting
NAVY={'red':16/255,'green':40/255,'blue':74/255}; WHITE={'red':1,'green':1,'blue':1}; BLUE={'red':0,'green':0,'blue':1}; LIGHT={'red':232/255,'green':234/255,'blue':245/255}
R=[]
def rng(t,r0,r1,c0,c1): return {'sheetId':ids[t],'startRowIndex':r0,'endRowIndex':r1,'startColumnIndex':c0,'endColumnIndex':c1}
def fmt(t,r0,r1,c0,c1,f,fields): R.append({'repeatCell':{'range':rng(t,r0,r1,c0,c1),'cell':{'userEnteredFormat':f},'fields':'userEnteredFormat('+fields+')'}})
USD={'type':'CURRENCY','pattern':'"$"#,##0'}; USD3={'type':'CURRENCY','pattern':'"$"#,##0.000'}; NUM={'type':'NUMBER','pattern':'#,##0'}; X={'type':'NUMBER','pattern':'0.0"x"'}; BPS={'type':'NUMBER','pattern':'0" bps"'}; PCT={'type':'PERCENT','pattern':'0.00%'}
widths={'Summary':[330,170,560],'What the $7,500 covers':[260,380,260,90,180,120,140,140],'Cost by volume':[150,150,160,140,140,140,140,130,130,140,140,130,150,150],'Value by scenario':[300,130,130,130,480],'Fixed fee vs share of sales':[330,170,170,170],'Assumptions':[380,140,420]}
for t in TABS:
    nrows=len(V[t]); ncols=len(V[t][0])
    R.append({'updateSheetProperties':{'properties':{'sheetId':ids[t],'gridProperties':{'frozenRowCount':1,'frozenColumnCount':1,'hideGridlines':True}},'fields':'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}})
    fmt(t,0,nrows,0,ncols,{'textFormat':{'fontFamily':'Roboto','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE'},'textFormat,wrapStrategy,verticalAlignment')
    fmt(t,0,1,0,ncols,{'backgroundColor':NAVY,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':WHITE},'horizontalAlignment':'LEFT','verticalAlignment':'MIDDLE','wrapStrategy':'WRAP'},'backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy')
    fmt(t,1,nrows,0,1,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'textFormat')
    R.append({'updateBorders':{'range':rng(t,0,nrows,0,ncols),'top':{'style':'SOLID'},'bottom':{'style':'SOLID'},'left':{'style':'SOLID'},'right':{'style':'SOLID'},'innerHorizontal':{'style':'SOLID'},'innerVertical':{'style':'SOLID'}}})
    R.append({'updateDimensionProperties':{'range':{'sheetId':ids[t],'dimension':'ROWS','startIndex':0,'endIndex':1},'properties':{'pixelSize':34},'fields':'pixelSize'}})
    for j,w in enumerate(widths[t]): R.append({'updateDimensionProperties':{'range':{'sheetId':ids[t],'dimension':'COLUMNS','startIndex':j,'endIndex':j+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
# number formats
t='What the $7,500 covers'; n=len(items)+1
fmt(t,1,n,3,4,{'numberFormat':{'type':'NUMBER','pattern':'#,##0.##'}},'numberFormat'); fmt(t,1,2,3,4,{'numberFormat':USD},'numberFormat')
fmt(t,1,n,5,6,{'numberFormat':{'type':'CURRENCY','pattern':'"$"#,##0.###'}},'numberFormat'); fmt(t,1,2,5,6,{'numberFormat':PCT},'numberFormat')
fmt(t,1,n+4,6,8,{'numberFormat':USD},'numberFormat'); fmt(t,n+2,n+3,6,7,{'numberFormat':X},'numberFormat')
fmt(t,n,n+4,0,8,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
t='Cost by volume'
fmt(t,1,12,0,1,{'numberFormat':USD,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'numberFormat,textFormat'); fmt(t,1,12,1,2,{'numberFormat':NUM},'numberFormat'); fmt(t,1,12,2,11,{'numberFormat':USD},'numberFormat'); fmt(t,1,12,11,12,{'numberFormat':BPS},'numberFormat'); fmt(t,1,12,12,14,{'numberFormat':USD3},'numberFormat')
fmt(t,6,7,0,14,{'backgroundColor':LIGHT},'backgroundColor')
t='Value by scenario'
fmt(t,1,12,1,4,{'numberFormat':USD},'numberFormat'); fmt(t,8,9,1,4,{'numberFormat':X},'numberFormat'); fmt(t,11,12,1,4,{'numberFormat':X},'numberFormat')
for r in (5,7,10): fmt(t,r,r+1,0,5,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
t='Fixed fee vs share of sales'
for r in (1,2,4,6): fmt(t,r,r+1,1,4,{'numberFormat':USD},'numberFormat')
for r in (3,5,7): fmt(t,r,r+1,1,4,{'numberFormat':BPS},'numberFormat')
fmt(t,2,4,0,4,{'backgroundColor':LIGHT},'backgroundColor')
R.append({'mergeCells':{'range':rng(t,8,9,1,4),'mergeType':'MERGE_ALL'}})
t='Summary'
for r in (1,7,10): fmt(t,r,r+1,0,3,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
fmt(t,2,7,1,2,{'numberFormat':USD},'numberFormat'); fmt(t,3,4,1,2,{'numberFormat':{'type':'TEXT'}},'numberFormat'); fmt(t,5,7,2,3,{'numberFormat':{'type':'NUMBER','pattern':'0" bps of sales"'},'horizontalAlignment':'LEFT'},'numberFormat,horizontalAlignment')
fmt(t,8,9,1,2,{'numberFormat':USD},'numberFormat'); fmt(t,9,10,1,2,{'numberFormat':X},'numberFormat')
fmt(t,11,14,1,2,{'numberFormat':USD},'numberFormat'); fmt(t,14,15,1,2,{'numberFormat':X},'numberFormat'); fmt(t,15,16,1,2,{'numberFormat':USD},'numberFormat')
t='Assumptions'
fmt(t,1,3,1,2,{'numberFormat':USD},'numberFormat'); fmt(t,3,7,1,2,{'numberFormat':PCT},'numberFormat'); fmt(t,7,9,1,2,{'numberFormat':USD},'numberFormat'); fmt(t,9,13,1,2,{'numberFormat':USD},'numberFormat')
fmt(t,1,13,1,2,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUE}},'textFormat')
sh.batchUpdate(spreadsheetId=SID,body={'requests':R}).execute()
out=sh.values().batchGet(spreadsheetId=SID,ranges=[f"{q('Summary')}!A1:C16",f"{q('What the $7,500 covers')}!A12:H15",f"{q('Value by scenario')}!A1:D12"]).execute()
for vr in out['valueRanges']:
    for row in vr.get('values',[]): print(row)
    print('--')
