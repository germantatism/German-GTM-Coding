# Yuno coverage gaps, 25 countries (LATAM, SEA, Israel)

Basis: 220 sourced rows in `gaps.json` (108 No, 17 Partial, 95 Yes). "On Yuno" = present for that country in `Deals/Adidas/build/sheet/rows.json` or the directory export, including methods carried through a provider (processed-methods column). Share figures come from PPRO country pages, 2C2P/IDC InfoBriefs, PCMI, central banks (BCRP, BCB, BCCR, BCN, BCU, BCR El Salvador), FNE Chile, UBS BB/ABECS, OECD and Bank of Israel. Where no share was published the row says "widely used" and cites the page.

## LATAM: biggest gaps

- **Israel-grade blind spot in the Southern Cone cards layer: local schemes.** Elo/Hipercard are 13% of Brazilian card volume, Chile's local schemes are 44% (more than Visa or Mastercard), Naranja/Cabal 5% in Argentina, Carnet ~2% in Mexico, OCA/Lider in Uruguay. None exist as scheme-level entries; Chile's domestic cards reach Yuno only through Transbank/Webpay.
- **American Express is absent everywhere.** Not listed in rows.json or the directory for any country, while PPRO puts it at 6% of card volume in Argentina and Israel, 3% in Mexico and Singapore.
- **Real-time rails in Central America are not connected:** SINPE Movil in Costa Rica (648.6M transactions, 4.2M users in 2024), Transfer365 in El Salvador (93% of interbank transfers, 5M+ ops/month), Clave/Telered in Panama (264M debit transactions), ACH Xpress, Bolivia's QR BCB (38% of all electronic operations in 2024).
- **Colombia's Bre-B is only Partial (dLocal).** 370M transactions and COP 59T settled in its first four months, 2.8M active merchants; Transfiya (Redeban) is not covered at all.
- **Peru: Plin is missing** while Yape is live. Wallets are 68.5% of retail payments by number and Yape+Plin exceed half of cashless transactions. Culqi (BCP-ecosystem gateway) and direct BCP transfers are also absent.
- **Argentina acquiring: Payway (Prisma) is not on Yuno** despite being one of the three leading acquirers with Fiserv and Mercado Pago; MODO and interoperable QR are Partial only; Uala and Cuenta DNI are absent.
- **Mexico PSP layer: Clip (2M+ merchants, 4M daily transactions) and Conekta are missing**, even though aggregators run 78% of the country's 6.3M terminals. Carnet and DiDi Paga Despues also absent.
- **Uruguay cash and transfer layer is empty:** Abitab and Redpagos (the two national collection networks), OCA cards and instant transfers/Toke are all No; only Mercado Pago covers the 11% wallet share.
- **Mobile money across Central America, Bolivia and Paraguay is absent:** Tigo Money (Paraguay "widely used", Honduras 1M+ customers, also GT/SV/BO), Banpro Billetera Movil (83% of Nicaraguan wallet users), Personal Pay, Zimple, Wally, Payphone (Ecuador), tPago (DR), Zinli (Panama). The regional gateway Tilopay (65K+ merchants, 47 banks, SINPE Movil and Yappy) is also missing.
- **Bolivia acquiring is uncovered:** neither ATC Red Enlace nor Linkser (the two Visa/Mastercard processors) is connected; Guatemala's NeoNet (ex-VisaNet, "la red mas grande de aceptacion") likewise.

## Southeast Asia: biggest gaps

- **Vietnam is effectively uncovered locally.** MoMo (69% of wallet users), ZaloPay (44%), VietQR/NAPAS 247 (29% of e-commerce), Napas domestic debit (87% of card volume), VNPay-QR, ViettelPay and the domestic gateways (OnePay, Payoo, Ngan Luong) are all No; only ShopeePay and international PSPs are live.
- **Singapore lacks PayNow**, used by 80% of consumers and businesses and 99% of bank transfers, plus DBS PayLah! (26% of online wallet use), NETS, Atome and HitPay.
- **Indonesia: GoPay is missing** (21-32% of wallet use depending on survey) alongside LinkAja, BI-FAST, Kredivo/Akulaku BNPL (6% of e-commerce); Virtual Accounts (part of the 34% domestic-payments share) are Partial only via Xendit/dLocal.
- **Malaysia: DuitNow QR (870M transactions in 2024) is absent**, Touch 'n Go eWallet (23M+ users) is Partial only, and the domestic gateways iPay88 and Fiuu, plus Atome/SPayLater, MAE, are No.
- **Philippines: the domestic rails QR Ph and InstaPay/PESONet (24% of e-commerce) are missing**, as are Dragonpay and Billease; GCash and Maya are live.
- **Thailand: Rabbit LINE Pay (24.7% of wallets), bank apps K PLUS and SCB Easy, Opn Payments and bank acquiring (KBank, SCB) are absent**; PromptPay and TrueMoney are live.
- **Myanmar has only 2C2P cards.** KBZPay (19M users, 43% of adults), Wave Pay (~80% of mobile financial services), AYA Pay, CB Pay, MMQR and the MPU domestic card network (39K POS, 600+ e-commerce merchants) are all No.

## Israel

- **Only Nuvei, PPRO, Pockyt and global wallets are live.** The three card companies that administer every bank-issued card (Isracard ~42% of active cards, Cal, Max), the local schemes (16% of card volume), Bit and Paybox (e-wallets are 26% of e-commerce), Amex (6%) and every domestic gateway (Tranzila, Cardcom, PayPlus, Pelecard) are missing.
