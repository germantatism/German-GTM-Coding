import json,csv,sys,warnings; warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
M='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/49f121e3-1b42-499d-826d-45d993ea05ac/scratchpad/master'
SID='1aevNJ2Ukpgieopu81YGCzqOAUe5s-nu397jQnvf3u8w'
out=json.load(open(M+'/master_final.json')); H=out[0]; I={h:i for i,h in enumerate(H)}
def num(x):
    try: return float(str(x).replace(',',''))
    except: return None
# blank estimates for non-ICP rows
for r in out[1:]:
    if r[I['ICP check']].startswith('No'):
        r[I['Est. monthly transactions']]=''; r[I['Est. monthly online payment volume ($M)']]=''; r[I['Transaction estimate method']]='Not estimated: outside ICP ('+r[I['ICP check']].split(': ',1)[1]+')'
icp=[r for r in out[1:] if not r[I['ICP check']].startswith('No')]; non=[r for r in out[1:] if r[I['ICP check']].startswith('No')]
def rerank(rows):
    k=0
    for r in rows:
        if num(r[I['ARR ($M)']]) is not None and not r[1].startswith('AIOS'): k+=1; r[I['Rank']]=str(k)
        else: r[I['Rank']]=''
rerank(icp); rerank(non)
json.dump([H]+icp+non,open(M+'/master_final.json','w'),ensure_ascii=False)
csv.writer(open('/Users/germantatis/Desktop/GTMCoding/Lists & ICP/ai-prospects-master-german-samuel-2026-10.csv','w',newline='')).writerows([H]+icp+non)
creds=service_account.Credentials.from_service_account_file('/Users/germantatis/.config/gsuite/sa.json',scopes=['https://www.googleapis.com/auth/spreadsheets'])
svc=build('sheets','v4',credentials=creds,cache_discovery=False)
meta=svc.spreadsheets().get(spreadsheetId=SID,fields='sheets.properties').execute()['sheets']; ids={s['properties']['title']:s['properties']['sheetId'] for s in meta}
reqs=[]
if 'Not ICP' not in ids: reqs.append({'addSheet':{'properties':{'title':'Not ICP','index':1}}})
if reqs: svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':reqs}).execute(); meta=svc.spreadsheets().get(spreadsheetId=SID,fields='sheets.properties').execute()['sheets']; ids={s['properties']['title']:s['properties']['sheetId'] for s in meta}
navy={'red':0.0627451,'green':0.15686275,'blue':0.2901961}
widths={0:55,1:200,2:80,3:95,4:120,5:120,6:150,7:70,8:170,9:230,10:60,11:300,12:220,13:300,14:85,15:300,16:220,17:230,18:70,19:320,20:130,21:340,22:230,23:240,24:200,25:260,26:400,27:120,28:90,29:260,30:180,31:280,32:300,33:300,34:260,35:110,36:110,37:360}
def cell(v,ci):
    if ci in (0,2,14,35,36) and v not in ('',None):
        try: return float(v) if '.' in str(v) else int(v)
        except: return v
    return v
def write_tab(title,rows):
    sid=ids[title]; n=len(rows)+1; ncol=len(H)
    svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':[{'updateSheetProperties':{'properties':{'sheetId':sid,'gridProperties':{'rowCount':max(n+20,120),'columnCount':ncol,'frozenRowCount':1,'frozenColumnCount':2,'hideGridlines':True}},'fields':'gridProperties(rowCount,columnCount,frozenRowCount,frozenColumnCount,hideGridlines)'}}]}).execute()
    svc.spreadsheets().values().clear(spreadsheetId=SID,range=f"'{title}'!A1:ZZ").execute()
    vals=[H]+[[cell(v,i) for i,v in enumerate(r)] for r in rows]
    svc.spreadsheets().values().update(spreadsheetId=SID,range=f"'{title}'!A1",valueInputOption='USER_ENTERED',body={'values':vals}).execute()
    fmt=[{'repeatCell':{'range':{'sheetId':sid,'startRowIndex':0,'endRowIndex':1,'startColumnIndex':0,'endColumnIndex':ncol},'cell':{'userEnteredFormat':{'backgroundColor':navy,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':{'red':1,'green':1,'blue':1}},'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE','horizontalAlignment':'LEFT'}},'fields':'userEnteredFormat(backgroundColor,textFormat,wrapStrategy,verticalAlignment,horizontalAlignment)'}},
         {'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':0,'endColumnIndex':ncol},'cell':{'userEnteredFormat':{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':False},'wrapStrategy':'WRAP','verticalAlignment':'TOP','backgroundColor':{'red':1,'green':1,'blue':1}}},'fields':'userEnteredFormat(textFormat,wrapStrategy,verticalAlignment,backgroundColor)'}},
         {'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':1,'endColumnIndex':2},'cell':{'userEnteredFormat':{'textFormat':{'bold':True}}},'fields':'userEnteredFormat.textFormat.bold'}},
         {'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':2,'endColumnIndex':3},'cell':{'userEnteredFormat':{'numberFormat':{'type':'NUMBER','pattern':'#,##0'},'horizontalAlignment':'RIGHT'}},'fields':'userEnteredFormat(numberFormat,horizontalAlignment)'}},
         {'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':35,'endColumnIndex':36},'cell':{'userEnteredFormat':{'numberFormat':{'type':'NUMBER','pattern':'#,##0'},'horizontalAlignment':'RIGHT'}},'fields':'userEnteredFormat(numberFormat,horizontalAlignment)'}},
         {'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':36,'endColumnIndex':37},'cell':{'userEnteredFormat':{'numberFormat':{'type':'NUMBER','pattern':'#,##0.0'},'horizontalAlignment':'RIGHT'}},'fields':'userEnteredFormat(numberFormat,horizontalAlignment)'}},
         {'updateBorders':{'range':{'sheetId':sid,'startRowIndex':0,'endRowIndex':n,'startColumnIndex':0,'endColumnIndex':ncol},'top':{'style':'SOLID','width':1},'bottom':{'style':'SOLID','width':1},'left':{'style':'SOLID','width':1},'right':{'style':'SOLID','width':1},'innerHorizontal':{'style':'SOLID','width':1},'innerVertical':{'style':'SOLID','width':1}}},
         {'updateDimensionProperties':{'range':{'sheetId':sid,'dimension':'ROWS','startIndex':0,'endIndex':1},'properties':{'pixelSize':34},'fields':'pixelSize'}}]
    for ci,w in widths.items(): fmt.append({'updateDimensionProperties':{'range':{'sheetId':sid,'dimension':'COLUMNS','startIndex':ci,'endIndex':ci+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
    # light tint on the ICP check column
    fmt.append({'repeatCell':{'range':{'sheetId':sid,'startRowIndex':1,'endRowIndex':n,'startColumnIndex':34,'endColumnIndex':35},'cell':{'userEnteredFormat':{'backgroundColor':{'red':0.93,'green':0.96,'blue':1}}},'fields':'userEnteredFormat.backgroundColor'}})
    svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':fmt}).execute()
write_tab('Master',icp); write_tab('Not ICP',non)
# Read me additions
rid=ids['Read me']
cur=svc.spreadsheets().values().get(spreadsheetId=SID,range="'Read me'!A1:B60").execute().get('values',[])
cur=[r for r in cur if r and r[0] not in ('ICP check and tabs','Transaction estimates')]
add=[['ICP check and tabs','Oct 7 2026: column AI "ICP check" classifies every company for Yuno. Yes = online card volume (self-serve subscriptions or usage) or a payouts angle; Borderline = acquired (route via the parent), app-store led (web checkout is the opening), under $3M ARR, or agentic commerce not yet live; No = invoiced enterprise with no card or payout volume, defense/robotics/hardware, pre-revenue, China-based, or captive. The Master tab holds only Yes and Borderline rows (ranked 1..N by ARR); the Not ICP tab holds the No rows with the reason, so nothing is lost.'],
     ['Transaction estimates','Columns AJ to AL: estimated monthly transactions and monthly online payment volume ($M), with the method in AL. Default method: ARR/12 x online share by Yuno fit (A 90%, B 45%) divided by an average charge by segment (consumer ~$20, prosumer/developer ~$60, infrastructure usage ~$400). Named companies use specific overrides (paying-customer counts, payout cadences, IAP share). Marketplaces include contractor payouts in both count and volume. Not ICP rows are not estimated. All are Claude estimates (Oct 2026), order-of-magnitude only, for prioritization, never for external use.']]
svc.spreadsheets().values().clear(spreadsheetId=SID,range="'Read me'!A1:B60").execute()
vals=cur[:-1]+add+cur[-1:] if cur and cur[-1][0]=='Sources' else cur+add
svc.spreadsheets().values().update(spreadsheetId=SID,range="'Read me'!A1",valueInputOption='RAW',body={'values':vals}).execute()
svc.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':[{'repeatCell':{'range':{'sheetId':rid,'startRowIndex':0,'endRowIndex':len(vals),'startColumnIndex':0,'endColumnIndex':2},'cell':{'userEnteredFormat':{'textFormat':{'fontFamily':'Roboto','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'TOP'}},'fields':'userEnteredFormat(textFormat,wrapStrategy,verticalAlignment)'}},{'repeatCell':{'range':{'sheetId':rid,'startRowIndex':1,'endRowIndex':len(vals),'startColumnIndex':0,'endColumnIndex':1},'cell':{'userEnteredFormat':{'textFormat':{'bold':True}}},'fields':'userEnteredFormat.textFormat.bold'}}]}).execute()
print('Master rows',len(icp),'| Not ICP rows',len(non),'| cols',len(H))
print('Master top 10:',[(r[I['Rank']],r[1],r[I['Est. monthly transactions']]) for r in icp[:10]])
