# -*- coding: utf-8 -*-
"""Write Gaps + Full ranking tabs into an existing Google Sheet (shared with the SA) and apply German's house format."""
import json,os,sys,warnings; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
SC=os.path.dirname(os.path.abspath(__file__))
SID=sys.argv[1]
ORDER=json.load(open('/Users/germantatis/Desktop/GTMCoding/Deals/HBO Max/build/config.json'))
REGION={}; CORDER=[]
for r in ORDER['regions']:
    for c in r['countries']: REGION[c]=r['name']; CORDER.append(c)
rows=json.load(open(f'{SC}/ranking.json'))
def cidx(c): return CORDER.index(c) if c in CORDER else 99
rows.sort(key=lambda r:(cidx(r['country']), -r['rating'], r['type'], r['name']))
GAP_ST=('MISSING','Homologating','Integrated (code)','Elsewhere')
gaps=[r for r in rows if r['yuno_status'] in GAP_ST]
def status_label(r):
    return {'MISSING':'Not available','Homologating':'Homologating (not live)','Integrated (code)':'Integrated in code, not listed','Elsewhere':'Connection exists in other markets, not listed here','Partial':'Partial (see Yuno match)','N/A':'Not applicable','Generic':'Category, not a connection'}.get(r['yuno_status'],r['yuno_status'])
H1=['Country','Region','Connection','Type','Rating (1-10)','Yuno status','Why it matters','Source']
V1=[H1]+[[r['country'],REGION.get(r['country'],''),r['name'],r['type'],r['rating'],status_label(r),r['why'],r['source'] if r['source']!='knowledge' else ''] for r in gaps]
H2=['Country','Region','Connection','Type','Rating (1-10)','Recurring-capable','Yuno status','Yuno match','Why it matters','Source']
V2=[H2]+[[r['country'],REGION.get(r['country'],''),r['name'],r['type'],r['rating'],'' if r.get('recurring') is None else ('Yes' if r['recurring'] else 'No'),
          ('Live' if r['yuno_status']=='Live' else status_label(r)),r['yuno_match'],r['why'],r['source'] if r['source']!='knowledge' else ''] for r in rows]
# summary tab: per country, count of gaps rated >=8, top gaps
summ=[['Country','Region','Items ranked','Live through Yuno','Gaps (not available or not listed)','Gaps rated 8+','Top gaps (rating)']]
for c in CORDER:
    rc=[r for r in rows if r['country']==c]; g=[r for r in rc if r['yuno_status'] in GAP_ST]
    top=', '.join(f"{r['name']} ({r['rating']})" for r in sorted(g,key=lambda r:-r['rating'])[:5])
    summ.append([c,REGION[c],len(rc),sum(1 for r in rc if r['yuno_status']=='Live'),len(g),sum(1 for r in g if r['rating']>=8),top])
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/spreadsheets'])
svc=build('sheets','v4',credentials=creds,cache_discovery=False)
meta=svc.spreadsheets().get(spreadsheetId=SID).execute()
existing={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
first_id=meta['sheets'][0]['properties']['sheetId']
reqs=[{'updateSheetProperties':{'properties':{'sheetId':first_id,'title':'Gaps'},'fields':'title'}}]
for t in ('Full ranking','Summary by country'):
    if t not in existing: reqs.append({'addSheet':{'properties':{'title':t}}})
svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':reqs}).execute()
meta=svc.spreadsheets().get(spreadsheetId=SID).execute()
ids={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
svc.spreadsheets().values().batchClear(spreadsheetId=SID,body={'ranges':['Gaps!A:Z','Full ranking!A:Z','Summary by country!A:Z']}).execute()
svc.spreadsheets().values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'RAW','data':[
    {'range':'Gaps!A1','values':V1},{'range':'Full ranking!A1','values':V2},{'range':'Summary by country!A1','values':summ}]}).execute()
NAVY={'red':0x10/255,'green':0x28/255,'blue':0x4A/255}; BLACK={'red':0,'green':0,'blue':0}
def fmt(sheet_id,nrows,ncols,widths):
    R=[]
    R.append({'updateSheetProperties':{'properties':{'sheetId':sheet_id,'gridProperties':{'frozenRowCount':1,'frozenColumnCount':1,'hideGridlines':True}},'fields':'gridProperties.frozenRowCount,gridProperties.frozenColumnCount,gridProperties.hideGridlines'}})
    R.append({'repeatCell':{'range':{'sheetId':sheet_id,'startRowIndex':0,'endRowIndex':1,'startColumnIndex':0,'endColumnIndex':ncols},
        'cell':{'userEnteredFormat':{'backgroundColor':NAVY,'horizontalAlignment':'LEFT','verticalAlignment':'MIDDLE','wrapStrategy':'WRAP','textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':{'red':1,'green':1,'blue':1}}}},
        'fields':'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,wrapStrategy,textFormat)'}})
    R.append({'repeatCell':{'range':{'sheetId':sheet_id,'startRowIndex':1,'endRowIndex':nrows,'startColumnIndex':0,'endColumnIndex':ncols},
        'cell':{'userEnteredFormat':{'wrapStrategy':'WRAP','verticalAlignment':'TOP','textFormat':{'fontFamily':'Roboto','fontSize':10}}},'fields':'userEnteredFormat(wrapStrategy,verticalAlignment,textFormat)'}})
    R.append({'repeatCell':{'range':{'sheetId':sheet_id,'startRowIndex':1,'endRowIndex':nrows,'startColumnIndex':0,'endColumnIndex':1},'cell':{'userEnteredFormat':{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}}},'fields':'userEnteredFormat.textFormat'}})
    b={'style':'SOLID','width':1,'color':BLACK}
    R.append({'updateBorders':{'range':{'sheetId':sheet_id,'startRowIndex':0,'endRowIndex':nrows,'startColumnIndex':0,'endColumnIndex':ncols},'top':b,'bottom':b,'left':b,'right':b,'innerHorizontal':b,'innerVertical':b}})
    R.append({'updateDimensionProperties':{'range':{'sheetId':sheet_id,'dimension':'ROWS','startIndex':0,'endIndex':1},'properties':{'pixelSize':30},'fields':'pixelSize'}})
    for i,w in enumerate(widths):
        R.append({'updateDimensionProperties':{'range':{'sheetId':sheet_id,'dimension':'COLUMNS','startIndex':i,'endIndex':i+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
    return R
reqs=fmt(ids['Gaps'],len(V1),len(H1),[140,110,200,90,80,170,360,220])
reqs+=fmt(ids['Full ranking'],len(V2),len(H2),[140,110,200,90,80,90,170,220,360,220])
reqs+=fmt(ids['Summary by country'],len(summ),7,[140,110,90,110,100,90,430])
# blue URLs in Source columns
for t,col,n in (('Gaps',7,len(V1)),('Full ranking',9,len(V2))):
    reqs.append({'repeatCell':{'range':{'sheetId':ids[t],'startRowIndex':1,'endRowIndex':n,'startColumnIndex':col,'endColumnIndex':col+1},'cell':{'userEnteredFormat':{'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':{'red':0,'green':0,'blue':1}}}},'fields':'userEnteredFormat.textFormat'}})
# rating colour scale (10 = navy-ish strong, 1 = light)
for t,n in (('Gaps',len(V1)),('Full ranking',len(V2))):
    reqs.append({'addConditionalFormatRule':{'rule':{'ranges':[{'sheetId':ids[t],'startRowIndex':1,'endRowIndex':n,'startColumnIndex':4,'endColumnIndex':5}],
        'gradientRule':{'minpoint':{'color':{'red':1,'green':1,'blue':1},'type':'NUMBER','value':'1'},'maxpoint':{'color':{'red':0.55,'green':0.65,'blue':0.95},'type':'NUMBER','value':'10'}}},'index':0}})
svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':reqs}).execute()
print('gaps rows',len(V1)-1,'| full rows',len(V2)-1,'| countries',len(summ)-1)
