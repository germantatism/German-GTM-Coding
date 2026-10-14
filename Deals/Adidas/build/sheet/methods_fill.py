"""Per (country, provider) payment-method lists for the adidas sheet, from three sources:
 1. Yuno integration matrix (Payments Concierge CSV): processed through Yuno.
 2. docs.y.uno Payment Type list (official provider -> method catalog): ptl.md.
 3. Caio's code scan (Provider PM gaps, 14 Oct 2026): code_pm_pairs.json, high + medium confidence.
Every code is mapped to a label and to the countries where that method exists; anything else is dropped and logged."""
import re, json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
LATAM = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay']
SEA = ['Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar']
ALL = LATAM + SEA + ['Israel']
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())

# code -> (label, countries). 'ALL' = every market in scope.
M = {
 'CARD': ('Cards', ALL), 'CARD_REDIRECT': ('Cards', ALL), 'CHECKOUT_API': ('Cards', ALL), 'TARJETA_CLAVE': ('Clave', ['Panama']),
 'APPLE_PAY': ('Apple Pay', [c for c in ALL if c not in ('Bolivia', 'Nicaragua', 'Indonesia', 'Thailand', 'Myanmar')]),
 'GOOGLE_PAY': ('Google Pay', [c for c in ALL if c != 'Indonesia']), 'GOOGLE_PAY_PIX': ('Google Pay PIX', ['Brazil']), 'SAMSUNG_PAY': ('Samsung Pay', ['Brazil']),
 'PAYPAL': ('PayPal', [c for c in ALL if c != 'Myanmar']), 'PAYPAL_ENROLLMENT': ('PayPal', [c for c in ALL if c != 'Myanmar']), 'PAYPAL_BRAINTREE': ('PayPal', [c for c in ALL if c != 'Myanmar']),
 # Argentina
 'PAGO_FACIL': ('Pago Fácil', ['Argentina']), 'RAPI_PAGO': ('Rapipago', ['Argentina']), 'RAPIPAGO': ('Rapipago', ['Argentina']), 'MODO': ('MODO', ['Argentina']),
 'TRANSFERENCIA_30': ('Transferencias 3.0', ['Argentina']), 'TRANSFERENCIA_3.0': ('Transferencias 3.0', ['Argentina']), 'BANK_TRANSFER_AR': ('Bank transfer', ['Argentina']),
 # Brazil
 'PIX': ('PIX', ['Brazil']), 'SMART_PIX': ('Smart PIX', ['Brazil']), 'PIX_AUTOMATIC': ('PIX Automático', ['Brazil']), 'PIX_AUTOMATIC_ENROLLMENT': ('PIX Automático', ['Brazil']),
 'PIX_BIOMETRICO': ('PIX biométrico', ['Brazil']), 'PIX_BIOMETRIC': ('PIX biométrico', ['Brazil']), 'PIX_PARCELADO': ('PIX Parcelado', ['Brazil']), 'BOLETO': ('Boleto', ['Brazil']),
 'NU_PAY': ('NuPay', ['Brazil']), 'NUPAY': ('NuPay', ['Brazil']), 'NU_PAY_ENROLLMENT': ('NuPay', ['Brazil']), 'PICPAY': ('PicPay', ['Brazil']), 'ALELO': ('Alelo', ['Brazil']), 'BB_PAY': ('BB Pay', ['Brazil']),
 'PIX_SAFETYPAY': ('PIX', ['Brazil']),
 # Chile
 'KHIPU': ('Khipu', ['Chile']), 'WEBPAY': ('Webpay', ['Chile']), 'MACH_PAY': ('MACH', ['Chile']), 'MACH_SAFETYPAY': ('MACH', ['Chile']), 'BCI_MACH_QR': ('MACH QR', ['Chile']), 'SERVIPAG': ('Servipag', ['Chile']),
 'PLUXEE_CL': ('Pluxee', ['Chile']),
 # Colombia
 'PSE': ('PSE', ['Colombia']), 'NEQUI': ('Nequi', ['Colombia', 'Panama']), 'NEQUI_QR': ('Nequi QR', ['Colombia']), 'NEQUI_ENROLLMENT': ('Nequi', ['Colombia']), 'NEQUI_SAFETYPAY': ('Nequi', ['Colombia']),
 'DAVIPLATA': ('Daviplata', ['Colombia']), 'DAVIPLATA_ENROLLMENT': ('Daviplata', ['Colombia']), 'EFECTY': ('Efecty', ['Colombia']), 'BREB': ('Bre-B', ['Colombia']), 'BREB_QR': ('Bre-B', ['Colombia']), 'BREB_LLAVES': ('Bre-B', ['Colombia']),
 'BANCOLOMBIA': ('Botón Bancolombia', ['Colombia']), 'BANCOLOMBIA_QR': ('Bancolombia QR', ['Colombia']), 'BANCOLOMBIA_TRANSFER': ('Bancolombia transfer', ['Colombia']), 'BOTON_BANCOLOMBIA': ('Botón Bancolombia', ['Colombia']),
 'BANCOLOMBIA_BNPL': ('Bancolombia BNPL', ['Colombia']), 'BANCOLOMBIA_TOKEN_BOX': ('Bancolombia Tokenbox', ['Colombia']), 'TOKENBOX': ('Bancolombia Tokenbox', ['Colombia']), 'SU_PLUS_PAY': ('SU+ Pay', ['Colombia']),
 'ADDI': ('ADDI', ['Colombia']), 'TRANSFIYA': ('Transfiya', ['Colombia']), 'ACCIONES_Y_VALORES': ('Acciones y Valores (cash)', ['Colombia']), 'SISTECREDITO': ('Sistecrédito', ['Colombia']),
 # Mexico
 'SPEI': ('SPEI', ['Mexico']), 'SPEI_SAFETYPAY': ('SPEI', ['Mexico']), 'CODI': ('CoDi', ['Mexico']), 'OXXO': ('OXXO', ['Mexico']), 'OXXO_PAY': ('OXXO Pay', ['Mexico']), 'PAYNET': ('Paynet', ['Mexico']),
 'PAYCASH': ('PayCash', ['Mexico']), 'PUNTOSHEY': ('Puntos Hey', ['Mexico']), 'APLAZO': ('Aplazo', ['Mexico']), 'KUESKI_PAY': ('Kueski Pay', ['Mexico']), 'DIRECT_DEBIT_ENROLLMENT': ('Direct debit', ['Mexico']),
 'FARMACIAS_AHORRO': ('Farmacias Benavides and Del Ahorro (cash)', ['Mexico']), '7ELEVEN': ('7-Eleven', ['Mexico', 'Malaysia', 'Philippines']), 'BENAVIDES': ('Farmacias Benavides (cash)', ['Mexico']),
 'CALIMAX': ('Calimax (cash)', ['Mexico']), 'SAMSCLUB': ("Sam's Club (cash)", ['Mexico']), 'T1PAGOS': ('T1 Pagos', ['Mexico']), 'TELECOMM': ('Telecomm (cash)', ['Mexico']),
 # Peru / Ecuador / Bolivia / Central America / DR
 'PAGO_EFECTIVO': ('PagoEfectivo', ['Peru', 'Ecuador']), 'YAPE': ('Yape', ['Peru']), 'YAPE_ENROLLABLE': ('Yape', ['Peru']), 'YAPE_ENROLLMENT': ('Yape', ['Peru']), 'YAPE_ONESHOT': ('Yape', ['Peru']),
 'PLIN': ('Plin', ['Peru']), 'NIUBIZ_QR': ('Niubiz QR', ['Peru']), 'CUOTEALO_BCP': ('Cuotéalo BCP', ['Peru']), 'ACUOTAZ': ('aCuotaz', ['Peru']), 'POWERPAY': ('Powerpay', ['Peru']),
 'MONNET_QR': ('Monnet QR', ['Peru', 'Guatemala']), 'MONNET_WALLET': ('Monnet wallet', ['Peru', 'Guatemala']),
 'DE_UNA': ('Deuna', ['Ecuador']), 'DE_UNA_(APP)': ('Deuna', ['Ecuador']), 'DEUNA_SAFETYPAY': ('Deuna', ['Ecuador']),
 'PAGOSNET': ('PagosNet', ['Bolivia']), 'PAGO_AL_PASO': ('Pago al Paso', ['Bolivia']), 'MULTIPAGO': ('Multipago', ['Bolivia']),
 'BANCO_NACIONAL_CASH': ('Banco Nacional cash', ['Costa Rica']), 'BANCO_NACIONAL_TRANSFER': ('Banco Nacional transfer', ['Costa Rica']), 'BANCO_NACIONAL_BANK_TRANSFER': ('Banco Nacional transfer', ['Costa Rica']),
 'PUNTO_XPRESS': ('PuntoXpress', ['Costa Rica', 'El Salvador', 'Nicaragua']), 'PUNTOXPRESS': ('PuntoXpress', ['Costa Rica', 'El Salvador', 'Nicaragua']), 'BAM': ('BAM (Banco Agromercantil)', ['Guatemala']),
 'BANCO_POPULAR': ('Banco Popular', ['Dominican Republic']), 'BANCO_POPULAR_DOMINICANA': ('Banco Popular', ['Dominican Republic']), 'BANRESERVAS': ('Banreservas', ['Dominican Republic']),
 'PAGA_TODO': ('Pagatodo', ['Dominican Republic']),
 'YAPPY': ('Yappy', ['Panama']), 'PUNTO_PAGO': ('Punto Pago', ['Panama']), 'PLUXEE_PA': ('Pluxee', ['Panama']),
 # SEA
 'QRIS': ('QRIS', ['Indonesia']), 'ALFAMART': ('Alfamart', ['Indonesia']), 'INDOMARET': ('Indomaret', ['Indonesia']), 'OVO_WALLET': ('OVO', ['Indonesia']), 'DANA': ('DANA', ['Indonesia']), 'DANA_ENROLLMENT': ('DANA', ['Indonesia']),
 'VIRTUAL_ACCOUNT_IDN': ('Virtual Account', ['Indonesia']), 'GOPAY': ('GoPay', ['Indonesia']), 'GOPAY_ENROLLMENT': ('GoPay', ['Indonesia']),
 'FPX': ('FPX', ['Malaysia']), 'BOOST': ('Boost', ['Malaysia']), 'TOUCH_AND_GO': ("Touch 'n Go", ['Malaysia']), 'TOUCH_N_GO': ("Touch 'n Go", ['Malaysia']), 'TOUCH_AND_GO_ENROLLMENT': ("Touch 'n Go", ['Malaysia']),
 'GRABPAY_MY': ('GrabPay', ['Malaysia']), 'GRABPAY_PH': ('GrabPay', ['Philippines']), 'GRABPAY_SG': ('GrabPay', ['Singapore']), 'GRABPAY': ('GrabPay', ['Malaysia', 'Philippines', 'Singapore']),
 'GCASH': ('GCash', ['Philippines']), 'GCASH_ENROLLMENT': ('GCash', ['Philippines']), 'GCASH_RECURRING': ('GCash', ['Philippines']), 'MAYA_WALLET': ('Maya', ['Philippines']), 'MAYA_CHECKOUT': ('Maya', ['Philippines']),
 'QRPH': ('QR Ph', ['Philippines']), 'DIRECT_DEBIT': ('Direct debit', ['Philippines']),
 'SHOPEEPAY': ('ShopeePay', ['Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Vietnam']), 'SHOPEEPAY_ENROLLMENT': ('ShopeePay', ['Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Vietnam']),
 'PAYNOW': ('PayNow', ['Singapore']), 'THAI_QR': ('Thai QR (PromptPay)', ['Thailand']), 'TRUEMONEY': ('TrueMoney', ['Thailand']), 'BIG_C': ('Big C', ['Thailand']), 'MOMO': ('MoMo', ['Vietnam']),
 'ALIPAY': ('Alipay', ALL), 'WECHAT_PAY': ('WeChat Pay', ALL), 'WECHAT': ('WeChat Pay', ALL), 'UNIONPAY': ('UnionPay', ALL),
 # regional wallets / cash aggregators
 'MERCADO_PAGO_WALLET': ('Mercado Pago Wallet', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']), 'MERCADO_PAGO_QR': ('Mercado Pago QR', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']),
 'MERCADO_PAGO_CHECKOUT_PRO': ('Checkout Pro', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']), 'CHECKOUT_PRO': ('Checkout Pro', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']),
 'MERCADO_PAGO_SUPERTOKEN': ('Mercado Pago Fast Payments', ['Argentina', 'Brazil']), 'MERCADO_PAGO_SAFETYPAY': ('Mercado Pago', ['Peru']), 'WALLET_CONNECT': ('Mercado Pago Wallet Connect', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']),
 'SAFETYPAY': ('SafetyPay', LATAM), 'SAFETYPAY_CASH': ('SafetyPay (cash)', LATAM), 'SAFETYPAY_BANK': ('SafetyPay (bank transfer)', LATAM), 'SAFETYPAY_BANK_TRANSFER': ('SafetyPay (bank transfer)', LATAM),
 'ASTROPAY': ('AstroPay', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Indonesia']), 'ASTROPAY_ENROLLABLE': ('AstroPay', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Indonesia']),
 'DOLARAPP': ('DolarApp', ['Argentina', 'Brazil', 'Colombia', 'Mexico']), 'PAYVALIDA': ('Payvalida', ['Colombia', 'Peru', 'Ecuador', 'El Salvador', 'Guatemala']), 'NETELLER': ('Neteller', ALL), 'SKRILL': ('Skrill', ALL),
 'BANK_TRANSFER': ('Bank transfer', LATAM), 'CASH': ('Cash', LATAM), 'BANCO_NACIONAL': ('Banco Nacional', ['Costa Rica']),
 'PAGOEFECTIVO': ('PagoEfectivo', ['Peru', 'Ecuador']), 'MACH': ('MACH', ['Chile']), 'ATOME': ('Atome', ['Malaysia', 'Singapore']), 'QR': ('Mercado Pago QR', ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico']),
 'MONNET_CASH': ('Cash', ['Peru']), 'MONNET_BANK_TRANSFER': ('Bank transfer', ['Peru']), 'BANCO_CONTINENTAL': ('Banco Continental (cash)', ['Paraguay']),
 'ALSUPER': ('Alsuper (cash)', ['Mexico']), 'FARMATODO': ('Farmatodo (cash)', ['Mexico']), 'SFDEASIS': ('San Francisco de Asís (cash)', ['Mexico']), 'DELAHORRO': ('Farmacias del Ahorro (cash)', ['Mexico']),
 'BANORTE': ('Banorte (cash deposit)', ['Mexico']), 'BANCOMER': ('BBVA (cash deposit)', ['Mexico']), 'KIOSKO': ('Kiosko (cash)', ['Mexico']), 'EXTRA': ('Extra (cash)', ['Mexico']), 'STAMARIA': ('Farmacias Santa María (cash)', ['Mexico']),
 'CIRCULOK': ('Círculo K (cash)', ['Mexico']), 'WALMART': ('Walmart (cash)', ['Mexico']), 'FARMROMA': ('Farmacias Roma (cash)', ['Mexico']), 'CASH_CASHMX': ('Cash', ['Mexico']), 'FARMUNION': ('Farmacias Unión (cash)', ['Mexico']),
 'LAMASBARATA': ('La Más Barata (cash)', ['Mexico']), 'SORIANA': ('Soriana (cash)', ['Mexico']), 'BODEGA': ('Bodega Aurrera (cash)', ['Mexico']), 'ELASTURIANO': ('El Asturiano (cash)', ['Mexico']), 'WALDOS': ("Waldo's (cash)", ['Mexico']),
}
# codes that are real but outside these markets or not pay-in: dropped silently
SKIP = set('''TAMARA_BNPL PAGAR_COM_PAGBANK BHD_LEON BANK TRANSFER (VIA KCP) PAYCO (VIA KCP) CREDIT CARD (VIA KCP) PAY BY BANK (EUROPE) ACH ACH_ENROLLMENT ACH_PLAID SEPA SEPA_ENROLLMENT BACS BACS_ENROLLMENT IDEAL IDEAL_ENROLLMENT BLIK EPS PRZELEWY24 MULTIBANCO MB_WAY MB_WAY_BANK_TRANSFER TRUSTLY VIPPS MOBILEPAY SWISH SWISH_WALLET TWINT TWINT_ENROLLMENT
KLARNA KLARNA_PAY_LATER KLARNA_PAY_NOW KLARNA_PAY_OVER_TIME KLARNA_PAY_LATER_ENROLLMENT KLARNA_PAY_NOW_ENROLLMENT KLARNA_PAY_OVER_TIME_ENROLLMENT AFTERPAY AFTERPAY_ENROLLMENT CLEARPAY ZIP TAMARA TABBY UPI UPI_AUTOPAY UPI_AUTOPAY_INTENT UPI_AUTOPAY_QR
KAKAO_PAY NAVER_PAY PAYPAY PAYPAY_WALLET TOSS_PAY KCP KCP_BANKTRANSFER KCP_CREDITCARD KCP_PAYCO HECTO KR_LOCAL_CARD FAMILY_MART LAWSON MINI_STOP SEICOMART PAY_EASY MPESA MTN_MOMO AIRTEL_MONEY CASHAPP CASHAPP_ENROLLMENT VENMO PADS PAYPAL_CREDIT PAYPAL_BA_ENROLLMENT PAYPALCP_CARD
CRYPTO HONG_KONG_FPS_QR OPEN_BANKING_AT OPEN_BANKING_BE OPEN_BANKING_DE OPEN_BANKING_EE OPEN_BANKING_FI OPEN_BANKING_FR OPEN_BANKING_HU OPEN_BANKING_LT OPEN_BANKING_LV OPEN_BANKING_NL OPEN_BANKING_PT EU_BANK_TRANSFER EU_BANK_TRANSFER_ENROLLMENT PAYBYBANK PAYBYBANK_ENROLLMENT
PIX_PAYOUT PAYPAL_PAYOUT ASTROPAY_PAYOUT STP_PAYOUT AFIRME_PAYOUT TRANSFIYA_PAYOUT NEQUI_PAYOUT QI_PAYOUT CARD_PAYOUT ECOMMPAY_PAYOUT UNLIMINT_PAYOUT WALLET PAGSEGURO_CHECKOUT DLOCAL_CHECKOUT CHECKOUT_REDIRECT UNLIMINT_CHECKOUT PANDABLUE_CHECKOUT
AMPM JUMBOMARKET PAYSER SMELPUEBLO WUNION ACERTEMOS GANA GANA_GANA SURED SUCHANCE APUESTAS_CUCUTA_75 APUESTAS_UNIDAS JER LA_PERLA DINOMEX PAGA_TODO_PARA_TODO FRAUD 3DS YUNO_TEST_PAYMENT_GW CLICK_TO_PAY ALIPAY_HK UNION_BANK SBP SBERPAY ZAINCASH
REVOLUT REVOLUT_PAY REVOLUT_PAY_ENROLLMENT AMAZON_PAY PAZE PAYSAFECARD AUTOGIRO AUTOGIRO_ENROLLMENT BETALINGSSERVICE BETALINGSSERVICE_ENROLLMENT BECS_DIRECT_DEBIT BECS_DIRECT_DEBIT_ENROLLMENT BECS_NZ PAD_ENROLLMENT BANCONTACT BANCONTACT_ENROLLMENT
SUPERAMA COMERCIAL_MEXICANA PAYOUT_CARD AFTER_PAY AFTER_PAY_ENROLLMENT KLARNA_ENROLLMENT CASH_APP DIRECT CHECKOUT_EXPRESS KAKAOPAY BANK_TRANSFER_ENROLLMENT EDENRED_WALLET PIX_RECORRENTE SAFETY_BANK SAFETY_CASH PAYMENT_LINK_CASH NAPS ITAU_PAY STC_PAY LINE_PAY BIZUM SATISPAY MEGAFON MTS TELE2 BEEPING OCBC PAGA_CON_RAPPI PAYPAL_WALLET KLAP_CASH WEBPAY_MALL WEBPAY_PLUS WEBPAY_PLUS_MALL'''.split())
# Dominican Republic bank list via Inswitch
DR_BANKS = {'ASOCIACION_BONAO', 'ASOCIACION_CIBAO', 'ASOCIACION_LA_NACIONAL', 'BANCO_ADOPEM', 'BANCO_ATLANTICO', 'BANCO_BANESCO', 'BANCO_JMMB', 'BANCO_LAFISE', 'BANCO_SANTA_CRUZ', 'BANCO_VIMENCA', 'COOPERATIVA_LA_ALTAGRACIA', 'BANRESERVAS'}

def parse_ptl(path):
    """docs.y.uno Payment Type list (markdown) -> provider code -> set(method codes)"""
    out = collections.defaultdict(set)
    for l in open(path):
        if not l.strip().startswith('|') or '**' in l or ':--' in l: continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 3: continue
        code = re.findall(r'`([^`]+)`', c[0]); pms = re.findall(r'`([^`]+)`', c[1])
        if code: out[code[0]] |= set(pms)
    return out

GENERIC_OK = {'bamboo', 'dlocal', 'unlimit', 'unlimint', 'monnet', 'paymentez', 'ebanx', 'fintoc', 'inswitch', 'kushki', 'arcus', 'payu', 'openpay', 'safetypay', 'pagsmile', 'payretailers', 'directa24', 'localpayment', 'prontopaga', 'pandablue'}
def labels(codes, country, provider_key=''):
    out = []; unknown = []
    for m in codes:
        if m in ('BANK_TRANSFER', 'CASH', 'CASH_CASHMX') and provider_key not in GENERIC_OK: continue
        if m in DR_BANKS:
            if country == 'Dominican Republic': out.append('Local bank transfers and cash')
            continue
        if m in M:
            lab, cs = M[m]
            if country in cs: out.append(lab)
        elif m in SKIP: pass
        else: unknown.append(m)
    seen = []; [seen.append(x) for x in out if x not in seen]
    seen.sort(key=lambda x: (x != 'Cards', x.lower()))
    return seen, unknown
