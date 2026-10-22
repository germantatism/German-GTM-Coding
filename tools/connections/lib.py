"""Yuno connections by country, for the "connections and payment methods" Google Slides decks (adidas format).
Master source: y.uno/en/integrations directory export (Deals/Adidas/build/csv/integrations_directory.json, 14 Oct 2026).
Method sources per provider: docs.y.uno Payment Type list (scratchpad/docs/ptl.md, 22 Oct 2026), Caio Freitas's code scan
(code_pm_pairs.json, high+medium), and the Payments Concierge matrix for the 25 adidas countries. Codes are mapped to a label and the
countries where that method exists; unknown codes are logged, never guessed. Exclusions: adidas exclusions.json (official coverage)."""
import json, csv, re, os, collections, importlib.util
ROOT = '/Users/germantatis/Desktop/GTMCoding'
AD = os.path.join(ROOT, 'Deals/Adidas/build')
PTL_PATH = os.path.join(ROOT, 'tools/connections/ptl_2026-10-22.md')
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())

# ---------------- countries
LATAM = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador',
         'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Venezuela']
LATAM_MATRIX = LATAM[:17]   # countries covered by the Payments Concierge matrix
EURO = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
        'Luxembourg', 'Malta', 'Netherlands', 'Portugal', 'Slovakia', 'Slovenia', 'Spain']
NORM_C = {'Brasil': 'Brazil', 'Republica Dominicana': 'Dominican Republic', 'Netherlands 64bff': 'Netherlands', 'China C4bc9': 'China', 'Czechia': 'Czech Republic',
          'Hkg': 'Hong Kong', 'Mac': 'Macau', 'Macao': 'Macau', 'Türkiye': 'Turkey', 'Turkiye': 'Turkey', 'Timor Leste': 'Timor-Leste', 'Pri': 'Puerto Rico'}
DISPLAY_COUNTRY = {'Turkey': 'Türkiye'}

# ---------------- directory
def load_directory():
    D = json.load(open(os.path.join(AD, 'csv/integrations_directory.json')))
    for d in D: d['countries'] = sorted({NORM_C.get(c, c) for c in (d['countries'] or [])})
    cs = [d for d in D if nk(d['name']) in ('cybersource', 'cybersourcegtw')]
    if len(cs) == 2:
        keep, dup = sorted(cs, key=lambda d: 0 if d['description'] else 1)
        keep['name'] = 'Cybersource'; keep['countries'] = sorted(set(keep['countries']) | set(dup['countries'])); keep['features'] = sorted(set(keep['features']) | set(dup['features']))
        if not keep.get('logo'): keep['logo'] = dup.get('logo'); D.remove(dup)
    ul = [d for d in D if nk(d['name']) in ('unlimit', 'unlimint')]
    if len(ul) == 2:
        keep = next(d for d in ul if nk(d['name']) == 'unlimit'); dup = next(d for d in ul if d is not keep)
        keep['countries'] = sorted(set(keep['countries']) | set(dup['countries'])); D.remove(dup)
    return D
PTYPE = {'clearsale': 'Fraud prevention', 'kount': 'Fraud prevention', 'striperadar': 'Fraud prevention', 'netcetera': '3DS authentication', 'cybersource3ds': '3DS authentication',
         'terrapay': 'Payouts and remittances', 'uniteller': 'Payouts and remittances', 'vtex': 'Commerce platform', 'skrill': 'Digital wallet', 'neteller': 'Digital wallet',
         'riskified': 'Fraud prevention', 'konduto': 'Fraud prevention', 'au10tix': 'Identity', 'forter': 'Fraud prevention', 'signifyd': 'Fraud prevention', 'sift': 'Fraud prevention'}
def ptype(d):
    k = nk(d['name']); desc = (d['description'] or '').lower()
    if k in PTYPE: return PTYPE[k]
    if 'fraud' in desc and 'gateway' not in desc and 'payment' not in desc[:40]: return 'Fraud prevention'
    if 'remittance' in desc: return 'Payouts and remittances'
    return 'Payment processing'
EXCL = json.load(open(os.path.join(AD, 'sheet/exclusions.json')))
# Official coverage overrides (same rule as the adidas sheet: a directory pair is dropped when the method's own coverage excludes the country).
# Apple Pay: support.apple.com/102775, read 22 Oct 2026. STC Pay: Saudi wallet. Visa Checkout: retired (Click to Pay replaced it).
APPLE_PAY_OK = set('''Egypt Mauritius Morocco South Africa Australia China Hong Kong Japan Macau Malaysia Mongolia New Zealand Philippines Singapore South Korea Taiwan Vietnam
Albania Andorra Armenia Austria Azerbaijan Belarus Belgium Bosnia and Herzegovina Bulgaria Croatia Cyprus Czech Republic Denmark Estonia Faroe Islands Finland France Georgia Germany Greece Greenland Guernsey Hungary Iceland Ireland Isle of Man Italy Kazakhstan Kosovo Kyrgyzstan Jersey Latvia Liechtenstein Lithuania Luxembourg Malta Moldova Monaco Montenegro Netherlands North Macedonia Norway Poland Portugal Romania Serbia Slovakia Slovenia Spain Sweden Switzerland Tajikistan Ukraine United Kingdom Vatican City
Argentina Brazil Chile Colombia Costa Rica Dominican Republic Ecuador El Salvador Guatemala Honduras Mexico Panama Paraguay Peru Bahamas Uruguay Bahrain India Israel Jordan Kuwait Oman Palestine Qatar Saudi Arabia United Arab Emirates Canada United States Puerto Rico'''.split('\n')[0].split() ) if False else {
 'Egypt','Mauritius','Morocco','South Africa','Australia','China','Hong Kong','Japan','Macau','Malaysia','Mongolia','New Zealand','Philippines','Singapore','South Korea','Taiwan','Vietnam',
 'Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia And Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Faroe Islands','Finland','France','Georgia','Germany','Greece','Greenland','Guernsey','Hungary','Iceland','Ireland','Isle Of Man','Italy','Kazakhstan','Kosovo','Kyrgyzstan','Jersey','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','North Macedonia','Norway','Poland','Portugal','Romania','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Tajikistan','Ukraine','United Kingdom','Vatican City',
 'Argentina','Brazil','Chile','Colombia','Costa Rica','Dominican Republic','Ecuador','El Salvador','Guatemala','Honduras','Mexico','Panama','Paraguay','Peru','Bahamas','Uruguay','Bahrain','India','Israel','Jordan','Kuwait','Oman','Palestine','Qatar','Saudi Arabia','United Arab Emirates','Canada','United States','Puerto Rico'}
APPLE_PAY_EXTRA = set()   # filled after checking the Thai page (Thailand launched Nov 2024)
def excluded(name, c):
    k = nk(name)
    if EXCL.get(k, {}).get(c): return True
    if k == 'applepay' and c not in (APPLE_PAY_OK | APPLE_PAY_EXTRA): return 'Apple Pay not available (Apple)'
    if k == 'stcpay' and c != 'Saudi Arabia': return 'STC Pay is a Saudi wallet'
    if k == 'visacheckout': return 'Visa Checkout retired'
    return None

# ---------------- display names (adidas sheet QA)
DISPLAY = {'Dlocal': 'dLocal', 'Astropay': 'AstroPay', 'Ebanx': 'EBANX', 'Fac': 'FAC (First Atlantic Commerce)', 'Ppro': 'PPRO', 'Paypal': 'PayPal', 'Pag Smile': 'Pagsmile',
           'MercadoPago': 'Mercado Pago', '2c2p': '2C2P', 'Safetypay': 'SafetyPay', 'PlaceToPay': 'PlacetoPay', 'Antom/Alipay': 'Antom', 'More Payments/uniteller': 'More Payments',
           'ELAVON': 'Elavon', 'PAYNET': 'Paynet', 'Btg Pactual': 'BTG Pactual', 'Banbajio': 'BanBajío', 'Bci Mach': 'BCI MACH', 'Evo Payments': 'EVO Payments', 'Pagarme': 'Pagar.me',
           'ALFAMART': 'Alfamart', 'BOOST': 'Boost', 'THAI QR': 'Thai QR (PromptPay)', 'TRUEMONEY': 'TrueMoney', 'BIG C': 'Big C', 'SHOPEEPAY': 'ShopeePay', '7ELEVEN': '7-Eleven',
           'OVO WALLET': 'OVO', 'CODI': 'CoDi', 'PAGO AL PASO': 'Pago al Paso', 'PUNTO PAGO': 'Punto Pago', 'YAPE': 'Yape', 'PIX': 'PIX', 'Nupay': 'NuPay', 'RapiPago': 'Rapipago',
           'Pago Facil': 'Pago Fácil', 'SAMSclub': "Sam's Club", 'Mach': 'MACH', 'SPEI': 'SPEI', 'QRIS': 'QRIS', 'FPX': 'FPX', 'Click-to-Pay': 'Click to Pay', 'De Una': 'Deuna',
           'PuntosHey': 'Puntos Hey', 'T1Pagos': 'T1 Pagos', 'Pagbank': 'PagBank', 'Paycash': 'PayCash', 'Dana': 'DANA', 'GCASH': 'GCash', 'GRABPAY': 'GrabPay',
           'BANCO NACIONAL DE COSTA RICA': 'Banco Nacional de Costa Rica', 'BANCO CONTINENTAL': 'Banco Continental', 'OpenPay': 'Openpay', 'IziPay': 'Izipay', 'Epayco': 'ePayco',
           'Unlimint': 'Unlimit', 'CyberSource': 'Cybersource', 'Pay-pay': 'PayPay', 'Mada': 'mada', 'Payabl': 'payabl.', 'Paysera': 'Paysera', 'PaySera': 'Paysera', 'SIBS': 'SIBS',
           'Myfatoorah': 'MyFatoorah', 'Hyperpay': 'HyperPay', 'Paytabs': 'PayTabs', 'Nuvei': 'Nuvei', 'Worldpay': 'Worldpay', 'Checkout.com': 'Checkout.com', 'Ntt Data': 'NTT DATA',
           'NTT Data': 'NTT DATA', 'Gmo': 'GMO', 'Komoju': 'KOMOJU', 'Sb Payment Service': 'SB Payment Service', 'Paidy': 'Paidy', 'Eximbay': 'Eximbay', 'Kcp': 'KCP', 'Nhn Kcp': 'NHN KCP',
           'Ipsp': 'IPSP', 'Moneris': 'Moneris', 'Tap': 'Tap Payments', 'Iyzico': 'iyzico', 'Paytr': 'PayTR', 'Param': 'Param', 'Pockyt': 'Pockyt', 'Opn': 'Opn', 'Omise': 'Omise',
           'Payoneer': 'Payoneer', 'Jkopay': 'JKOPAY', 'Linepay': 'LINE Pay', 'Ecpay': 'ECPay', 'Newebpay': 'NewebPay', 'Tappay': 'TapPay'}
def disp(name): return DISPLAY.get(name, name)

# Caio Freitas, payment-method-coverage-gaps (14 Oct 2026): directory providers with no Yuno integration repo yet. German: keep them, Status "Homologating".
HOMOLOGATING = {'Alignet', 'AsiaPay', 'BTG Pactual', 'BanBajío', 'Banco Azteca', 'Banco Estado de Chile', 'Banco Rendimento', 'Banco de Bogota', 'Bancolombia', 'Cardnet', 'Cobre', 'Commerce Gate', 'Coppel',
                'Davivienda', 'Directa 24', 'Doku', 'Etpay', 'Facilitapay', 'Ibex', 'Local Payment', 'Midtrans', 'More Payments', 'Netpay', 'Nium', 'Openco', 'PPRO', 'Pag Brasil', 'PagosNet', 'PayCash',
                'Payments Way', 'Paynet', 'Paysafe', 'Primefy', 'Pronto Paga', 'Sistecredito', 'Totalnet', 'Trace Finance', 'Transfero', 'Unico', 'Venti', 'We Payments'}
CATALOG_CARD = {'Datafast', 'Medianet'}
NO_DATA_NOTE = 'Methods confirmed on activation'

# ---------------- method codes -> (label, countries). 'ALL' = every country in scope; 'DIR:<name>' = the directory entry's own country list
AP = 'DIR:Apple Pay'; GP = 'DIR:Google Pay'; PP = 'DIR:Paypal'; KL = 'DIR:Klarna'; TR = 'DIR:Trustly'; WC = 'DIR:WeChat Pay'; SP_ = 'DIR:SHOPEEPAY'
SEA_SHOPEE = ['Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Vietnam', 'Singapore', 'Taiwan']
MX_CASH = lambda lab: (lab, ['Mexico'])
M = {
 'CARD': ('Cards', 'ALL'), 'CARD_REDIRECT': ('Cards', 'ALL'), 'CHECKOUT_API': ('Cards', 'ALL'), 'CREDIT CARD (VIA KCP)': ('Cards', ['South Korea']), 'KR_LOCAL_CARD': ('Cards', ['South Korea']),
 'APPLE_PAY': ('Apple Pay', AP), 'GOOGLE_PAY': ('Google Pay', GP), 'GOOGLE_PAY_PIX': ('Google Pay PIX', ['Brazil']), 'SAMSUNG_PAY': ('Samsung Pay', 'DIR:Samsung Pay'),
 'PAYPAL': ('PayPal', PP), 'PAYPAL_ENROLLMENT': ('PayPal', PP), 'PAYPAL_BRAINTREE': ('PayPal', PP), 'PAYPAL_ACDC': ('PayPal', PP), 'PAYPAL_BA_ENROLLMENT': ('PayPal', PP),
 # Argentina
 'PAGO_FACIL': ('Pago Fácil', ['Argentina']), 'RAPI_PAGO': ('Rapipago', ['Argentina']), 'RAPIPAGO': ('Rapipago', ['Argentina']), 'MODO': ('MODO', ['Argentina']),
 'TRANSFERENCIA_30': ('Transferencias 3.0', ['Argentina']), 'TRANSFERENCIA_3.0': ('Transferencias 3.0', ['Argentina']), 'BANK_TRANSFER_AR': ('Bank transfer', ['Argentina']),
 # Brazil
 'PIX': ('PIX', ['Brazil']), 'SMART_PIX': ('Smart PIX', ['Brazil']), 'PIX_AUTOMATIC': ('PIX Automático', ['Brazil']), 'PIX_AUTOMATIC_ENROLLMENT': ('PIX Automático', ['Brazil']), 'PIX_RECORRENTE': ('PIX Automático', ['Brazil']),
 'PIX_BIOMETRICO': ('PIX biométrico', ['Brazil']), 'PIX_BIOMETRIC': ('PIX biométrico', ['Brazil']), 'PIX_PARCELADO': ('PIX Parcelado', ['Brazil']), 'BOLETO': ('Boleto', ['Brazil']),
 'NU_PAY': ('NuPay', ['Brazil']), 'NUPAY': ('NuPay', ['Brazil']), 'NU_PAY_ENROLLMENT': ('NuPay', ['Brazil']), 'PICPAY': ('PicPay', ['Brazil']), 'ALELO': ('Alelo', ['Brazil']), 'BB_PAY': ('BB Pay', ['Brazil']),
 'PIX_SAFETYPAY': ('PIX', ['Brazil']), 'PAGAR COM PAGBANK': ('Pagar com PagBank', ['Brazil']),
 # Chile
 'KHIPU': ('Khipu', ['Chile']), 'WEBPAY': ('Webpay', ['Chile']), 'WEBPAY_PLUS_MALL': ('Webpay', ['Chile']), 'MACH_PAY': ('MACH', ['Chile']), 'MACH': ('MACH', ['Chile']), 'MACH_SAFETYPAY': ('MACH', ['Chile']),
 'BCI_MACH_QR': ('MACH QR', ['Chile']), 'SERVIPAG': ('Servipag', ['Chile']), 'PLUXEE_CL': ('Pluxee', ['Chile']), 'PLUXEE': ('Pluxee', ['Chile', 'Panama']), 'SENCILLITO': ('Sencillito', ['Chile']), 'KLAP_CASH': ('Klap (cash)', ['Chile']),
 # Colombia
 'PSE': ('PSE', ['Colombia']), 'NEQUI': ('Nequi', ['Colombia', 'Panama']), 'NEQUI_QR': ('Nequi QR', ['Colombia']), 'NEQUI_ENROLLMENT': ('Nequi', ['Colombia']), 'NEQUI_SAFETYPAY': ('Nequi', ['Colombia']),
 'DAVIPLATA': ('Daviplata', ['Colombia']), 'DAVIPLATA_ENROLLMENT': ('Daviplata', ['Colombia']), 'EFECTY': ('Efecty', ['Colombia']), 'BREB': ('Bre-B', ['Colombia']), 'BREB_QR': ('Bre-B', ['Colombia']), 'BREB_LLAVES': ('Bre-B', ['Colombia']),
 'BANCOLOMBIA': ('Botón Bancolombia', ['Colombia']), 'BANCOLOMBIA_QR': ('Bancolombia QR', ['Colombia']), 'BANCOLOMBIA_TRANSFER': ('Bancolombia transfer', ['Colombia']), 'BOTON_BANCOLOMBIA': ('Botón Bancolombia', ['Colombia']),
 'BANCOLOMBIA_BNPL': ('Bancolombia BNPL', ['Colombia']), 'BANCOLOMBIA_TOKEN_BOX': ('Bancolombia Tokenbox', ['Colombia']), 'TOKENBOX': ('Bancolombia Tokenbox', ['Colombia']), 'SU_PLUS_PAY': ('SU+ Pay', ['Colombia']),
 'ADDI': ('ADDI', ['Colombia']), 'TRANSFIYA': ('Transfiya', ['Colombia']), 'ACCIONES_Y_VALORES': ('Acciones y Valores (cash)', ['Colombia']), 'SISTECREDITO': ('Sistecrédito', ['Colombia']),
 # Mexico
 'SPEI': ('SPEI', ['Mexico']), 'SPEI_SAFETYPAY': ('SPEI', ['Mexico']), 'CODI': ('CoDi', ['Mexico']), 'OXXO': ('OXXO', ['Mexico']), 'OXXO_PAY': ('OXXO Pay', ['Mexico']), 'PAYNET': ('Paynet', ['Mexico']),
 'PAYCASH': ('PayCash', ['Mexico']), 'PUNTOSHEY': ('Puntos Hey', ['Mexico']), 'APLAZO': ('Aplazo', ['Mexico']), 'KUESKI_PAY': ('Kueski Pay', ['Mexico']), 'DIRECT_DEBIT_ENROLLMENT': ('Direct debit', ['Mexico', 'Colombia', 'Brazil']),
 'FARMACIAS_AHORRO': ('Farmacias Benavides and Del Ahorro (cash)', ['Mexico']), '7ELEVEN': ('7-Eleven', ['Mexico', 'Malaysia', 'Philippines', 'Japan']), 'BENAVIDES': ('Farmacias Benavides (cash)', ['Mexico']),
 'CALIMAX': ('Calimax (cash)', ['Mexico']), 'SAMSCLUB': ("Sam's Club (cash)", ['Mexico']), 'T1PAGOS': ('T1 Pagos', ['Mexico']), 'TELECOMM': ('Telecomm (cash)', ['Mexico']),
 'ALSUPER': MX_CASH('Alsuper (cash)'), 'FARMATODO': MX_CASH('Farmatodo (cash)'), 'SFDEASIS': MX_CASH('San Francisco de Asís (cash)'), 'DELAHORRO': MX_CASH('Farmacias del Ahorro (cash)'),
 'BANORTE': MX_CASH('Banorte (cash deposit)'), 'BANCOMER': MX_CASH('BBVA (cash deposit)'), 'KIOSKO': MX_CASH('Kiosko (cash)'), 'EXTRA': MX_CASH('Extra (cash)'), 'STAMARIA': MX_CASH('Farmacias Santa María (cash)'),
 'CIRCULOK': MX_CASH('Círculo K (cash)'), 'WALMART': MX_CASH('Walmart (cash)'), 'FARMROMA': MX_CASH('Farmacias Roma (cash)'), 'CASH_CASHMX': MX_CASH('Cash'), 'FARMUNION': MX_CASH('Farmacias Unión (cash)'),
 'LAMASBARATA': MX_CASH('La Más Barata (cash)'), 'SORIANA': MX_CASH('Soriana (cash)'), 'BODEGA': MX_CASH('Bodega Aurrera (cash)'), 'ELASTURIANO': MX_CASH('El Asturiano (cash)'), 'WALDOS': MX_CASH("Waldo's (cash)"),
 'SUPERAMA': MX_CASH('Superama (cash)'), 'COMERCIAL_MEXICANA': MX_CASH('Comercial Mexicana (cash)'),
 # Peru / Ecuador / Bolivia / Central America / DR / Venezuela
 'PAGO_EFECTIVO': ('PagoEfectivo', ['Peru', 'Ecuador']), 'PAGOEFECTIVO': ('PagoEfectivo', ['Peru', 'Ecuador']), 'YAPE': ('Yape', ['Peru']), 'YAPE_ENROLLABLE': ('Yape', ['Peru']), 'YAPE_ENROLLMENT': ('Yape', ['Peru']), 'YAPE_ONESHOT': ('Yape', ['Peru']),
 'PLIN': ('Plin', ['Peru']), 'NIUBIZ_QR': ('Niubiz QR', ['Peru']), 'CUOTEALO_BCP': ('Cuotéalo BCP', ['Peru']), 'ACUOTAZ': ('aCuotaz', ['Peru']), 'POWERPAY': ('Powerpay', ['Peru']),
 'MONNET_QR': ('Monnet QR', ['Peru', 'Guatemala']), 'MONNET_WALLET': ('Monnet wallet', ['Peru', 'Guatemala']), 'MONNET_CASH': ('Cash', ['Peru']), 'MONNET_BANK_TRANSFER': ('Bank transfer', ['Peru']),
 'DE_UNA': ('Deuna', ['Ecuador']), 'DE_UNA_(APP)': ('Deuna', ['Ecuador']), 'DE_UNA_(WEB)': ('Deuna', ['Ecuador']), 'DEUNA_SAFETYPAY': ('Deuna', ['Ecuador']),
 'PAGOSNET': ('PagosNet', ['Bolivia']), 'PAGO_AL_PASO': ('Pago al Paso', ['Bolivia']), 'MULTIPAGO': ('Multipago', ['Bolivia']),
 'BANCO_NACIONAL_CASH': ('Banco Nacional cash', ['Costa Rica']), 'BANCO_NACIONAL_TRANSFER': ('Banco Nacional transfer', ['Costa Rica']), 'BANCO_NACIONAL_BANK_TRANSFER': ('Banco Nacional transfer', ['Costa Rica']), 'BANCO_NACIONAL': ('Banco Nacional', ['Costa Rica']),
 'PUNTO_XPRESS': ('PuntoXpress', ['Costa Rica', 'El Salvador', 'Nicaragua']), 'PUNTOXPRESS': ('PuntoXpress', ['Costa Rica', 'El Salvador', 'Nicaragua']), 'BAM': ('BAM (Banco Agromercantil)', ['Guatemala']),
 'BANCO_POPULAR': ('Banco Popular', ['Dominican Republic']), 'BANCO_POPULAR_DOMINICANA': ('Banco Popular', ['Dominican Republic']), 'BANRESERVAS': ('Banreservas', ['Dominican Republic']), 'PAGA_TODO': ('Pagatodo', ['Dominican Republic']),
 'YAPPY': ('Yappy', ['Panama']), 'PUNTO_PAGO': ('Punto Pago', ['Panama']), 'PLUXEE_PA': ('Pluxee', ['Panama']), 'PLUXEE_PANAMA': ('Pluxee', ['Panama']), 'TARJETA_CLAVE': ('Clave', ['Panama']), 'BANCO_CONTINENTAL': ('Banco Continental (cash)', ['Paraguay']),
 # Southeast Asia
 'QRIS': ('QRIS', ['Indonesia']), 'ALFAMART': ('Alfamart', ['Indonesia']), 'INDOMARET': ('Indomaret', ['Indonesia']), 'OVO_WALLET': ('OVO', ['Indonesia']), 'DANA': ('DANA', 'DIR:Dana'), 'DANA_ENROLLMENT': ('DANA', ['Indonesia']),
 'VIRTUAL_ACCOUNT_IDN': ('Virtual Account', ['Indonesia']), 'GOPAY': ('GoPay', ['Indonesia']), 'GOPAY_ENROLLMENT': ('GoPay', ['Indonesia']), 'DIRECT_DEBIT': ('Direct debit', ['Indonesia', 'Philippines']),
 'FPX': ('FPX', ['Malaysia']), 'BOOST': ('Boost', ['Malaysia']), 'TOUCH_AND_GO': ("Touch 'n Go", ['Malaysia']), 'TOUCH_N_GO': ("Touch 'n Go", ['Malaysia']), 'TOUCH_AND_GO_ENROLLMENT': ("Touch 'n Go", ['Malaysia']),
 'GRABPAY_MY': ('GrabPay', ['Malaysia']), 'GRABPAY_PH': ('GrabPay', ['Philippines']), 'GRABPAY_SG': ('GrabPay', ['Singapore']), 'GRABPAY': ('GrabPay', ['Malaysia', 'Philippines', 'Singapore']),
 'GCASH': ('GCash', ['Philippines']), 'GCASH_ENROLLMENT': ('GCash', ['Philippines']), 'GCASH_RECURRING': ('GCash', ['Philippines']), 'MAYA_WALLET': ('Maya', ['Philippines']), 'MAYA_CHECKOUT': ('Maya', ['Philippines']), 'QRPH': ('QR Ph', ['Philippines']),
 'SHOPEEPAY': ('ShopeePay', SEA_SHOPEE), 'SHOPEEPAY_ENROLLMENT': ('ShopeePay', SEA_SHOPEE), 'PAYNOW': ('PayNow', ['Singapore']), 'ATOME': ('Atome', ['Singapore', 'Malaysia']),
 'THAI_QR': ('Thai QR (PromptPay)', ['Thailand']), 'TRUEMONEY': ('TrueMoney', ['Thailand']), 'BIG_C': ('Big C', ['Thailand']), 'MOMO': ('MoMo', ['Vietnam']),
 'ALIPAY': ('Alipay', 'ALL'), 'WECHAT_PAY': ('WeChat Pay', WC), 'WECHAT': ('WeChat Pay', WC), 'UNIONPAY': ('UnionPay', 'DIR:UnionPay'), 'ALIPAY_HK': ('AlipayHK', ['Hong Kong']), 'HONG_KONG_FPS_QR': ('FPS QR', ['Hong Kong']),
 # Japan / Korea / Oceania / Canada
 'PAYPAY': ('PayPay', ['Japan']), 'PAYPAY_WALLET': ('PayPay', ['Japan']), 'LAWSON': ('Konbini (Lawson)', ['Japan']), 'FAMILY_MART': ('Konbini (FamilyMart)', ['Japan']), 'SEICOMART': ('Konbini (Seicomart)', ['Japan']),
 'MINI_STOP': ('Konbini (Ministop)', ['Japan']), 'PAY_EASY': ('Pay-easy', ['Japan']), 'KONBINI': ('Konbini', ['Japan']), 'LINE_PAY': ('LINE Pay', ['Japan', 'Taiwan', 'Thailand']), 'RAKUTEN_PAY': ('Rakuten Pay', ['Japan']),
 'KAKAO_PAY': ('Kakao Pay', ['South Korea']), 'KAKAOPAY': ('Kakao Pay', ['South Korea']), 'NAVER_PAY': ('Naver Pay', ['South Korea']), 'TOSS_PAY': ('Toss Pay', ['South Korea']), 'PAYCO (VIA KCP)': ('Payco', ['South Korea']),
 'BANK TRANSFER (VIA KCP)': ('Bank transfer (KCP)', ['South Korea']), 'AFTER_PAY': ('Afterpay', ['Australia', 'New Zealand', 'Canada']), 'AFTERPAY': ('Afterpay', ['Australia', 'New Zealand', 'Canada']),
 'AFTER_PAY_ENROLLMENT': ('Afterpay', ['Australia', 'New Zealand', 'Canada']), 'AFTERPAY_ENROLLMENT': ('Afterpay', ['Australia', 'New Zealand', 'Canada']), 'CLEARPAY': ('Clearpay', ['United Kingdom']), 'ZIP': ('Zip', ['Australia', 'New Zealand']),
 'BECS_DIRECT_DEBIT': ('BECS direct debit', ['Australia']), 'BECS_DIRECT_DEBIT_ENROLLMENT': ('BECS direct debit', ['Australia']), 'BECS_NZ': ('BECS direct debit', ['New Zealand']), 'PAD_ENROLLMENT': ('PAD direct debit', ['Canada']), 'PADS': ('PAD direct debit', ['Canada']),
 'INTERAC': ('Interac', ['Canada']),
 # Europe
 'IDEAL': ('iDEAL', ['Netherlands']), 'IDEAL_ENROLLMENT': ('iDEAL', ['Netherlands']), 'BANCONTACT': ('Bancontact', ['Belgium']), 'BANCONTACT_ENROLLMENT': ('Bancontact', ['Belgium']),
 'SEPA': ('SEPA Direct Debit', EURO), 'SEPA_ENROLLMENT': ('SEPA Direct Debit', EURO), 'EU_BANK_TRANSFER': ('EU bank transfer', EURO), 'EU_BANK_TRANSFER_ENROLLMENT': ('EU bank transfer', EURO),
 'BLIK': ('BLIK', ['Poland']), 'PRZELEWY24': ('Przelewy24', ['Poland']), 'TWINT': ('TWINT', ['Switzerland']), 'TWINT_ENROLLMENT': ('TWINT', ['Switzerland']), 'MOBILEPAY': ('MobilePay', ['Denmark', 'Finland']), 'VIPPS': ('Vipps', ['Norway']), 'SWISH': ('Swish', ['Sweden']), 'SWISH_WALLET': ('Swish', ['Sweden']),
 'KLARNA': ('Klarna', KL), 'KLARNA_PAY_NOW': ('Klarna', KL), 'KLARNA_PAY_LATER': ('Klarna', KL), 'KLARNA_PAY_OVER_TIME': ('Klarna', KL), 'KLARNA_ENROLLMENT': ('Klarna', KL), 'KLARNA_PAY_NOW_ENROLLMENT': ('Klarna', KL),
 'KLARNA_PAY_LATER_ENROLLMENT': ('Klarna', KL), 'KLARNA_PAY_OVER_TIME_ENROLLMENT': ('Klarna', KL), 'EPS': ('EPS', ['Austria']), 'SATISPAY': ('Satispay', ['Italy']), 'TRUSTLY': ('Trustly', TR),
 'MULTIBANCO': ('Multibanco', ['Portugal']), 'MB_WAY': ('MB WAY', ['Portugal']), 'MB_WAY_BANK_TRANSFER': ('MB WAY', ['Portugal']), 'BIZUM': ('Bizum', ['Spain']), 'GIROPAY': ('giropay', ['Germany']), 'SOFORT': ('Sofort', ['Germany', 'Austria', 'Switzerland', 'Belgium', 'Netherlands', 'Italy', 'Spain']),
 'BACS': ('Bacs direct debit', ['United Kingdom']), 'BACS_ENROLLMENT': ('Bacs direct debit', ['United Kingdom']), 'REVOLUT_PAY': ('Revolut Pay', 'DIR:Revolut'), 'REVOLUT_PAY_ENROLLMENT': ('Revolut Pay', 'DIR:Revolut'), 'REVOLUT': ('Revolut Pay', 'DIR:Revolut'),
 'AUTOGIRO': ('Autogiro', ['Sweden']), 'AUTOGIRO_ENROLLMENT': ('Autogiro', ['Sweden']), 'BETALINGSSERVICE': ('Betalingsservice', ['Denmark']), 'BETALINGSSERVICE_ENROLLMENT': ('Betalingsservice', ['Denmark']),
 'OPEN_BANKING_AT': ('Open banking', ['Austria']), 'OPEN_BANKING_BE': ('Open banking', ['Belgium']), 'OPEN_BANKING_DE': ('Open banking', ['Germany']), 'OPEN_BANKING_EE': ('Open banking', ['Estonia']), 'OPEN_BANKING_FI': ('Open banking', ['Finland']),
 'OPEN_BANKING_FR': ('Open banking', ['France']), 'OPEN_BANKING_HU': ('Open banking', ['Hungary']), 'OPEN_BANKING_LT': ('Open banking', ['Lithuania']), 'OPEN_BANKING_LV': ('Open banking', ['Latvia']), 'OPEN_BANKING_NL': ('Open banking', ['Netherlands']), 'OPEN_BANKING_PT': ('Open banking', ['Portugal']),
 # regional wallets / cash aggregators
 'MERCADO_PAGO_WALLET': ('Mercado Pago Wallet', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']), 'MERCADO_PAGO_QR': ('Mercado Pago QR', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']), 'QR': ('Mercado Pago QR', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']),
 'MERCADO_PAGO_CHECKOUT_PRO': ('Checkout Pro', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']), 'CHECKOUT_PRO': ('Checkout Pro', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']),
 'MERCADO_PAGO_SUPERTOKEN': ('Mercado Pago Fast Payments', ['Argentina', 'Brazil']), 'MERCADO_PAGO_SAFETYPAY': ('Mercado Pago', ['Peru']), 'WALLET_CONNECT': ('Mercado Pago Wallet', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']),
 'SAFETYPAY': ('SafetyPay', LATAM), 'SAFETYPAY_CASH': ('SafetyPay (cash)', LATAM), 'SAFETYPAY_BANK': ('SafetyPay (bank transfer)', LATAM), 'SAFETYPAY_BANK_TRANSFER': ('SafetyPay (bank transfer)', LATAM),
 'ASTROPAY': ('AstroPay', 'DIR:Astropay'), 'ASTROPAY_ENROLLABLE': ('AstroPay', 'DIR:Astropay'), 'DOLARAPP': ('DolarApp', ['Argentina', 'Brazil', 'Colombia', 'Mexico']), 'PAYVALIDA': ('Payvalida', ['Colombia', 'Peru', 'Ecuador', 'El Salvador', 'Guatemala']),
 'NETELLER': ('Neteller', 'DIR:Neteller'), 'SKRILL': ('Skrill', 'DIR:Skrill'), 'BANK_TRANSFER': ('Bank transfer', LATAM), 'CASH': ('Cash', LATAM), 'VOUCHER': ('Voucher', LATAM),
 # MENA / other (kept for completeness, out of scope markets just never match)
 'TABBY': ('Tabby', 'DIR:Tabby'), 'TAMARA': ('Tamara', 'DIR:Tamara'), 'TAMARA BNPL': ('Tamara', 'DIR:Tamara'), 'TAMARA_BNPL': ('Tamara', 'DIR:Tamara'), 'STC_PAY': ('STC Pay', ['Saudi Arabia']), 'MADA': ('mada', ['Saudi Arabia']),
 'UPI': ('UPI', ['India']), 'UPI_AUTOPAY': ('UPI Autopay', ['India']), 'ACH': ('ACH', ['United States']), 'ACH_ENROLLMENT': ('ACH', ['United States']), 'ACH_PLAID': ('ACH (Plaid)', ['United States']), 'CASHAPP': ('Cash App Pay', ['United States']), 'CASH_APP': ('Cash App Pay', ['United States']), 'CASHAPP_ENROLLMENT': ('Cash App Pay', ['United States']), 'VENMO': ('Venmo', ['United States']),
 'MPESA': ('M-Pesa', ['Kenya', 'Tanzania']), 'MTN_MOMO': ('MTN MoMo', ['Ghana', 'Uganda', 'Cameroon', 'Rwanda', 'Zambia']), 'AIRTEL_MONEY': ('Airtel Money', ['Kenya', 'Uganda', 'Tanzania', 'Zambia']),
}
SKIP = set('''PIX_PAYOUT PAYPAL_PAYOUT ASTROPAY_PAYOUT STP_PAYOUT AFIRME_PAYOUT TRANSFIYA_PAYOUT NEQUI_PAYOUT QI_PAYOUT CARD_PAYOUT ECOMMPAY_PAYOUT UNLIMINT_PAYOUT PAYOUT_CARD NEQUI_DISPERSION WALLET PAGSEGURO_CHECKOUT DLOCAL_CHECKOUT CHECKOUT_REDIRECT UNLIMINT_CHECKOUT PANDABLUE_CHECKOUT CHECKOUT_EXPRESS
AMPM JUMBOMARKET PAYSER SMELPUEBLO WUNION ACERTEMOS GANA GANA_GANA SURED SUCHANCE APUESTAS_CUCUTA_75 APUESTAS_UNIDAS JER LA_PERLA DINOMEX PAGA_TODO_PARA_TODO FRAUD 3DS YUNO_TEST_PAYMENT_GW CLICK_TO_PAY CLICTOPAY UNION_BANK SBP SBERPAY ZAINCASH ZainCash MEGAFON MTS TELE2 BEEPING OCBC PAGA_CON_RAPPI PAYPAL_WALLET PAYPAL_CREDIT CRYPTO
PAYSAFECARD AMAZON_PAY PAZE DIRECT LINK_TO_PAY SMART_BUTTON SAFETY_BANK SAFETY_CASH PAYMENT_LINK_CASH NAPS ITAU_PAY EDENRED_WALLET BANK_TRANSFER_ENROLLMENT BHD_LEON HECTO KCP PAY BY BANK (EUROPE) PAYBYBANK PAYBYBANK_ENROLLMENT ASOCIACION_BONAO ASOCIACION_CIBAO ASOCIACION_LA_NACIONAL BANCO_ADOPEM BANCO_ATLANTICO BANCO_BANESCO BANCO_JMMB BANCO_LAFISE BANCO_SANTA_CRUZ BANCO_VIMENCA COOPERATIVA_LA_ALTAGRACIA
WEBPAY_MALL WEBPAY_PLUS PAGAR_COM_PAGBANK ALIPAY_PLUS'''.split()) | {'PAY BY BANK (EUROPE)', 'BANK TRANSFER (VIA KCP)'}
DR_BANKS = {'ASOCIACION_BONAO', 'ASOCIACION_CIBAO', 'ASOCIACION_LA_NACIONAL', 'BANCO_ADOPEM', 'BANCO_ATLANTICO', 'BANCO_BANESCO', 'BANCO_JMMB', 'BANCO_LAFISE', 'BANCO_SANTA_CRUZ', 'BANCO_VIMENCA', 'COOPERATIVA_LA_ALTAGRACIA', 'BANRESERVAS'}
GENERIC_OK = {'bamboo', 'dlocal', 'unlimit', 'unlimint', 'monnet', 'paymentez', 'ebanx', 'fintoc', 'inswitch', 'kushki', 'arcus', 'payu', 'openpay', 'safetypay', 'pagsmile', 'payretailers', 'directa24', 'localpayment', 'prontopaga', 'pandablue'}

# Recurring-capable through Yuno (docs.y.uno, 22 Oct 2026): subscriptions engine = CARD, PAYPAL_ENROLLMENT, PIX_AUTOMATIC; stored credentials = cards + Apple Pay / Google Pay
# wallet tokens; enrollable methods (vaulted_token) = the *_ENROLLMENT / enrollable codes in the Payment Type list and API enums. Belvo = direct-debit enrollment (code scan, high).
RECURRING_CODES = {'CARD', 'CARD_REDIRECT', 'CHECKOUT_API', 'CREDIT CARD (VIA KCP)', 'KR_LOCAL_CARD', 'APPLE_PAY', 'GOOGLE_PAY', 'PAYPAL_ENROLLMENT', 'PAYPAL_BA_ENROLLMENT', 'PIX_AUTOMATIC', 'PIX_AUTOMATIC_ENROLLMENT', 'PIX_RECORRENTE',
                   'PIX_BIOMETRICO', 'SMART_PIX', 'NU_PAY_ENROLLMENT', 'DAVIPLATA_ENROLLMENT', 'WALLET_CONNECT', 'YAPE_ENROLLMENT', 'ASTROPAY_ENROLLABLE', 'SEPA_ENROLLMENT', 'IDEAL_ENROLLMENT', 'BANCONTACT_ENROLLMENT',
                   'EU_BANK_TRANSFER_ENROLLMENT', 'KLARNA_ENROLLMENT', 'KLARNA_PAY_NOW_ENROLLMENT', 'KLARNA_PAY_OVER_TIME_ENROLLMENT', 'AFTER_PAY_ENROLLMENT', 'ACH_ENROLLMENT', 'CASHAPP_ENROLLMENT', 'DIRECT_DEBIT', 'DIRECT_DEBIT_ENROLLMENT'}
RECURRING_DIRECT = {'Visa', 'Mastercard', 'Discover', 'UnionPay', 'Apple Pay', 'Google Pay', 'Paypal', 'Klarna', 'Nupay', 'Daviplata', 'YAPE', 'Belvo'}   # directory "Payment Method" entries that are recurring-capable
RECURRING_DIRECT_NOTE = {'Belvo': 'Direct debit enrollment'}

def parse_ptl(path):
    out = collections.defaultdict(set)
    for l in open(path):
        if not l.strip().startswith('|') or '**' in l: continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 3: continue
        code = re.findall(r'`([^`]+)`', c[0]); pms = re.findall(r'`([^`]+)`', c[1])
        if code: out[code[0]] |= set(pms)
    return out

CODE_ALIAS = {'2c2p': '2c2p', 'checkoutcom': 'checkout', 'cybersource': 'cybersourcegtw', 'qnb': 'qnbmpgs', 'redeban': 'redebandirect', 'prosa': 'prosaiso', 'firstatlanticcommerce': 'fac', 'unlimit': 'unlimint',
              'antomalipay': 'antom', 'evopayments': 'evo', 'bbvabancomer': 'bbva', 'webpay': 'transbank', 'machpay': 'bcimach', 'paypal': 'paypal', 'mercadopago': 'mercadopago', 'nttdata': 'nttdata'}
PTL_ALIAS = {'cybersourcegtw': 'cybersource', 'redebandirect': 'redeban', 'prosaiso': 'prosa', 'klap2': 'klap', 'transbank2': 'transbank', 'unlimint': 'unlimint'}
def code_for(name):
    k = nk(name); return CODE_ALIAS.get(k, k)

class Data:
    def __init__(self, countries):
        self.T = list(countries); self.D = load_directory()
        self.dir_countries = {nk(d['name']): set(d['countries']) for d in self.D}
        self.PTL = {nk(k): v for k, v in parse_ptl(PTL_PATH).items()}
        cp = json.load(open(os.path.join(AD, 'csv/code_pm_pairs.json')))
        self.CODEPAIRS = {nk(k): {pm for pm, conf in v} for k, v in cp.items() if not k.startswith('_')}
        self.matrix = collections.defaultdict(lambda: collections.defaultdict(set))
        shape_src = open(os.path.join(AD, 'csv/shape.py')).read().split('rows = list')[0]
        g = {}; import sys; a = sys.argv; sys.argv = ['x', os.path.join(ROOT, 'Deals/Adidas/adidas_payment_connections_live.csv'), '/dev/null']; exec(shape_src, g); sys.argv = a
        WALLET_PROV = g['WALLET_PROV']
        for r in csv.DictReader(open(os.path.join(ROOT, 'Deals/Adidas/adidas_payment_connections_live.csv'))):
            if r['Country'] in self.T and r['Provider'] not in WALLET_PROV: self.matrix[r['Country']][nk(r['Provider'])] |= set(r['Payment Methods (via Yuno)'].split('; '))
        self.UNKNOWN = collections.Counter()
        self.prov_by_c = collections.defaultdict(list); self.meth_by_c = collections.defaultdict(list)
        for d in self.D:
            for c in d['countries']:
                if c not in self.T or excluded(d['name'], c): continue
                if d['category'] == 'Provider' and ptype(d) != 'Payment processing': continue
                (self.prov_by_c if d['category'] == 'Provider' else self.meth_by_c)[c].append(d)
    def countries_of(self, spec):
        if spec == 'ALL': return set(self.T)
        if spec == 'DIR:Apple Pay': return self.dir_countries.get('applepay', set()) & (APPLE_PAY_OK | APPLE_PAY_EXTRA)
        if isinstance(spec, str) and spec.startswith('DIR:'): return self.dir_countries.get(nk(spec[4:]), set())
        return set(spec)
    def all_codes(self, dirname):
        code = code_for(dirname); dk = nk(disp(dirname)); out = set()
        for cc in self.matrix.values(): out |= cc.get(code, set())
        for k in {code, PTL_ALIAS.get(code, code), nk(dirname), dk}: out |= self.PTL.get(k, set())
        for k in {dk, nk(dirname), code}: out |= self.CODEPAIRS.get(k, set())
        return out
    def codes_for(self, c, dirname):
        code = code_for(dirname); dk = nk(disp(dirname))
        codes = set(self.matrix.get(c, {}).get(code, set()))
        for k in {code, PTL_ALIAS.get(code, code), nk(dirname), dk}: codes |= self.PTL.get(k, set())
        for k in {dk, nk(dirname), code}: codes |= self.CODEPAIRS.get(k, set())
        if 'CARD' in self.all_codes(dirname) or disp(dirname) in CATALOG_CARD: codes.add('CARD')   # card processing is not country-specific
        if dk == 'baccredomatic' and c == 'Panama': codes.add('TARJETA_CLAVE')
        return codes
    def labels(self, codes, c, provider_key='', recurring_only=False):
        out = []
        for m in sorted(codes):
            if recurring_only and m not in RECURRING_CODES: continue
            if m in ('BANK_TRANSFER', 'CASH', 'CASH_CASHMX', 'VOUCHER') and provider_key not in GENERIC_OK: continue
            if m in DR_BANKS:
                if c == 'Dominican Republic': out.append('Local bank transfers and cash')
                continue
            if m in M:
                lab, cs = M[m]
                if c in self.countries_of(cs): out.append(lab)
            elif m in SKIP: pass
            else: self.UNKNOWN[m] += 1
        konb = sorted({x[9:-1] for x in out if x.startswith('Konbini (')})
        out = [x for x in out if not x.startswith('Konbini (')] + (['Konbini (' + ', '.join(konb) + ')'] if konb else [])
        seen = []; [seen.append(x) for x in out if x not in seen]
        seen.sort(key=lambda x: (x != 'Cards', x.lower())); return seen
    def rows(self, recurring_only=False):
        """[Country, Type, Name, methods(list), Status, logo_key]"""
        R = []; seen_code = collections.defaultdict(set)
        for c in self.T:
            for d in sorted(self.prov_by_c[c], key=lambda d: disp(d['name']).lower()):
                name = disp(d['name']); ck = code_for(d['name'])
                if ck in seen_code[c]: continue
                seen_code[c].add(ck)
                if name in HOMOLOGATING: R.append([c, 'Provider', name, [], 'Homologating', nk(d['name'])]); continue
                labs = self.labels(self.codes_for(c, d['name']), c, nk(name), recurring_only)
                R.append([c, 'Provider', name, labs, 'Live', nk(d['name'])])
            seen_m = set()
            for d in sorted(self.meth_by_c[c], key=lambda d: disp(d['name']).lower()):
                if recurring_only and d['name'] not in RECURRING_DIRECT: continue
                if nk(disp(d['name'])) in seen_m: continue
                seen_m.add(nk(disp(d['name'])))
                R.append([c, 'Direct payment method', disp(d['name']), [RECURRING_DIRECT_NOTE[d['name']]] if d['name'] in RECURRING_DIRECT_NOTE else [], 'Live', nk(d['name'])])
        return R
