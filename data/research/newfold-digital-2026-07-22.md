# SDR Research Brief — Newfold Digital
**Prepared:** 2026-07-22 · **Analyst:** Yuno payments intelligence · **Framework:** v8.0

---

## EXECUTIVE SUMMARY

Newfold Digital is the web-presence group formed in Feb 2021 from Endurance International (ex-NASDAQ: EIGI) and Web.com, billing **nearly 7 million customers** on recurring hosting and domain subscriptions through Bluehost, HostGator, Network Solutions, BigRock, ResellerClub and Crazy Domains. Newfold names **no processor in any legal or help document**, but its own production checkout bundle exposes the rails directly: **Worldpay, BillDesk and PayU on a single shared checkout serving nine brands**, with Network Solutions on a separate stack, Brazil on a WHMCS/Bradesco boleto rail, and three different fraud vendors split by brand. **No orchestration layer exists.** This is a multi-PSP, multi-fraud-vendor estate stitched per market, not a single-processor shop.

The standout finding is that **Newfold publicly documents its own involuntary-churn mechanism**. Bluehost's help centre states that some issuers now require the CVV on recurring requests, that "it is illegal for Bluehost to store this number," and therefore **"some cards will work the first time but fail every subsequent time"** — with the only remedies offered being "using a different credit card or logging in every month to... pay your invoice manually." Separately, **"customers cannot store Indian payment methods on file or set up auto-renewals in India."**

For a leveraged subscription business (~$3.5B debt, Moody's CFR **Caa1** citing "lower than expected revenue growth") where renewals are the lender-watched metric, recovered involuntary churn drops straight to the number that matters. Yuno's opening: network tokenization plus issuer-aware retries to replace a blunt 4-card cascade, routing across the three acquirers they already run, and UPI AutoPay to restore recurring billing in India. Note Brazil already has Pix Automático live, so the India gap is the sharp one.

---

## SECTION 1 — Traffic by Country

**Method:** SimilarWeb per-domain visits and country shares (retrieved 2026-07-22), weighted across the 13 brand domains below to produce a portfolio view. SimilarWeb's free tier labels the headline figure "Total Visits Last 3 Months"; reported as retrieved.

### 1A. Portfolio domains

| Domain | Brand / Region | Visits | Category rank | MoM |
|---|---|---|---|---|
| bluehost.com | Bluehost US/global | 4.8M | #13 Web Hosting (US) | +0.07% |
| hostgator.com.br | HostGator Brazil | 4.2M | **#4 Web Hosting (Brazil)** | +1.76% |
| hostgator.com | HostGator US/global | 2.7M | #24 (US) | −3.81% |
| networksolutions.com | Network Solutions | 2.0M | n/a | n/a |
| ipage.com | iPage | 980.4K | n/a | n/a |
| bigrock.in | BigRock India | 719.6K | #18 (India) | n/a |
| domain.com | Domain.com | 598.6K | n/a | n/a |
| hostgator.mx | HostGator Mexico | 561.4K | **#7 (Mexico)** | +13.38% |
| crazydomains.com.au | Crazy Domains AU | 419.2K | **#9 (Australia)** | −9.79% |
| resellerclub.com | ResellerClub | 347K | n/a | n/a |
| my.bluehost.com | Bluehost portal | 206.5K | n/a | +2.87% |
| web.com | Web.com | 198.5K | n/a | n/a |
| bluehost.in | Bluehost India | 188.2K | #76 (India) | +7.71% |

Source: `https://www.similarweb.com/website/{domain}/` for each domain above.

### 1B. Portfolio-weighted country mix

| Rank | Country | Weighted Share | Trend | Source |
|---|---|---|---|---|
| 1 | United States | **39.1%** | Flat | SimilarWeb (weighted) |
| 2 | **Brazil** | **22.9%** | Growing (+1.76% MoM on BR domain) | SimilarWeb (weighted) |
| 3 | **India** | **5.8%** | Growing (bluehost.in +7.71%) | SimilarWeb (weighted) |
| 4 | Mexico | 3.3% | **Growing (+13.38% MoM)** | SimilarWeb (weighted) |
| 5 | Canada | 3.0% | Flat | SimilarWeb (weighted) |
| 6 | Australia | 2.8% | **Declining (−9.79% MoM)** | SimilarWeb (weighted) |
| 7 | United Kingdom | 2.5% | Flat | SimilarWeb (weighted) |
| 8 | Philippines | 0.9% | n/a | SimilarWeb (weighted) |
| 9 | UAE | 0.9% | **+36.09% on hostgator.com** | SimilarWeb (weighted) |
| 10 | Saudi Arabia | 0.4% | **+51.45% on hostgator.com** | SimilarWeb (weighted) |

**Flags:**
- 🔴 **Brazil is 22.9% of portfolio traffic**, second only to the US, and larger than India, Mexico, Canada, Australia and the UK combined. HostGator BR is #4 in its category nationally.
- 🔴 **India is fragmented across three front doors** (bigrock.in 719.6K + resellerclub.com 347K + bluehost.in 188.2K ≈ 1.25M) and is a top-5 country for domain.com, networksolutions.com and web.com.
- 🟡 **Gulf is the fastest-growing surface**: UAE +36.09% and Saudi Arabia +51.45% MoM on hostgator.com.
- 🟡 LATAM extends beyond Mexico: Chile, Argentina and Peru all feed hostgator.mx.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Local Entity? | Cross-Border Risk? | Source |
|---|---|---|---|---|
| United States | Yes (39.1%) | **Yes** — Newfold Digital, Inc. (Jacksonville FL); Bluehost Inc. (UT); HostGator.com LLC (FL); Network Solutions, LLC | No | [S2a] [S2b] |
| Brazil | Yes (22.9%) | **Yes** — HostGator Brasil Ltda., CNPJ 15.754.475/0001-40, Florianópolis SC (branch 0003-02 São Paulo) | No | [S2c] |
| India | Yes (5.8%) | **Was yes, now shifting** — Endurance International Group (India) Pvt Ltd (Mumbai) for purchases **before 18 Sep 2025**; **Bluehost Inc. (Utah, US)** for purchases **after 18 Sep 2025** | ⚠️ **Yes, newly introduced** | [S2b] |
| Mexico | Yes (3.3%) | **No entity found** | ⚠️ Potential cross-border operation | — |
| Canada | Yes (3.0%) | **No entity found** | ⚠️ Potential cross-border operation | — |
| Australia | Yes (2.8%) | **Indirect** — Dreamscape Networks International Pte. Ltd. (**Singapore**, UEN 201814004Z) provides Crazy Domains merchant facilities | ⚠️ AU customers contract with a SG entity | [S2d] |
| United Kingdom | Yes (2.5%) | **Only legacy** — JDI Backup Limited (England & Wales, per 2014 SEC Ex-21.1). UK Companies House returns **no Newfold group entity** | ⚠️ Potential cross-border operation | [S2e] [S2f] |
| Singapore | No | **Yes** — Vodien Internet Solutions Pte. Ltd.; Dreamscape Networks International Pte. Ltd. | No | [S2d] |
| Netherlands | No | **Operations confirmed, entity name not public** (EIGI FY2019 10-K names NL as a primary operating country) | ⚠️ Unnamed | [S2e] |

> ⚠️ **The India entity switch is the single most payment-relevant legal finding.** Bluehost's user agreement states purchases on or after 18 Sep 2025 contract with **Bluehost Inc. (Utah)**, not the Indian entity. Combined with the documented inability to store Indian payment methods or run auto-renewals, this points to a US-entity, cross-border acquiring posture in India, which is exactly the configuration RBI card-storage and e-mandate rules penalise.

> ⚠️ MANUAL: Verify contracting entity on each regional T&C before quoting in a live call.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

**Breakthrough method.** Every live checkout is Cloudflare-403. The stack was recovered from Bluehost's **archived production checkout bundle** (`reg3-bundle.js` on `static.registration.bluehost.com`), retrieved via the Wayback Machine and gzip-decompressed to 2.05 MB. All strings below were **verified firsthand** by the analyst, not taken from a summary. Snapshot date **2024-05-25** unless noted.

| Country/Region | PSP / Acquirer | Evidence (verbatim) | Type | Source |
|---|---|---|---|---|
| **Global / US (9-brand shared checkout)** | **Worldpay** | `worldpayFollowup:function(...){var s="".concat(eX(),"/cart/order/worldpay/")...}` and `"/cart/order/worldpayRedirect?capReturnURL="`. 14 occurrences | **[Source Code]** own order route | [S3g] |
| **India (shared checkout)** | **BillDesk** | `billdeskOrder:function(...){var o="".concat(eX(),"/cart/order/billdesk")...}`; UI `htmlFor:"pay-with-billdesk"`. 73 occurrences | **[Source Code]** own order route | [S3g] |
| **India (Bluehost, INR)** | **PayU / PayUbiz** | `function l8(){var e;return 66===$U()&&(e=JU("paymentProcessor")\|\|"payubiz"),e}` (brand 66 = `bluehostindia`) plus `PayUbiz_logo.png`. Independently confirmed on the **live** help page: "the payment gateway used is **PayU**" | **[Source Code]** + **[Help Page]** | [S3a] [S3g] |
| **All 9 brands** | **PCI Pal** + in-house vault | `title:"PaaS - Credit Card (PCI Pal)"`; iframe `https://securepay.svcs.endurance.com/payment/cc-pcip_2.html?...tokenType=MULTI`; `paymentProcessor:"paas"` | **[Source Code]** card descoping, not an acquirer | [S3g] |
| **Brazil (HostGator BR)** | **Banco Bradesco S.A. (237)** via **GatorPay / WHMCS** | Live boleto: `Banco Bradesco S.A. 237-2` · `Beneficiário HostGator Brasil LTDA` · `CNPJ 15.754.475/0001-40`; served from `/modules/gateways/gatorpay/` | **[Primary doc]** collection bank | [S3h] |
| **Philippines / selected markets (Crazy Domains)** | **Dragonpay** | "you can also choose from several alternative payment options: PayPal, Maestro Debit Card, ZipPay, WebMoney, Alipay, UnionPay, Neteller and **Dragonpay** (selected countries only)" | **[Help Page]** live | [S4f] |
| **AU / APAC (Crazy Domains, Vodien)** | **Dreamscape Networks International Pte Ltd** (SG) | "**5.1 Merchant Facilities** Our merchant facilities are provided/serviced via Dreamscape Networks International Pte Ltd" | **[T&C]** acquiring entity, not a gateway | [S3i] |
| **ResellerClub (global)** | **Pay.pw** | "Debit/Credit Card payments via **Pay.pw**... Charge will be displayed as: **EIG\*ResellerClub**" | **[Official page]** archived | [S3j] |
| **ResellerClub (Brazil)** | **EBANX** | "Transferência via **Ebanx** 2.75%" | **[Official page]** archived | [S3k] |
| **Network Solutions / Web.com / Register.com** | **Not identified** | **Absent from the 9-brand map**, so they run a separate checkout stack entirely | Structural finding | [S3g] |
| All markets (predecessor) | **Plural, unnamed** — "our credit card processors", "merchant banks and payment processors" | | **[SEC 10-K]** Endurance FY2019 | [S3c] |

**The shared-checkout brand map (verbatim):**
`{40:"ipage",45:"netfirms",46:"dotster",47:"domaincom",48:"mydomain",50:"hostgator",52:"bluehost",61:"justhost",66:"bluehostindia"}`
One checkout, nine brands, three processors, no routing layer between them.

**Fraud stack is also fragmented (all [Source Code], verified):** **Sift** (`if("hostgator"===n||"bluehost"===n)... faas-sift.js`), **iovation / TransUnion** (`iovation/loader.js`, `aci-transunion.js`), and **MaxMind** (`device.maxmind.com` on HostGator US checkout). Three vendors, split by brand.

**Timeline:** Worldpay was **added between Oct 2021 and Mar 2024** (zero "worldpay" occurrences in the 2021-10-04 bundle; 14 by 2024-05). Newfold has changed acquirers recently, which means the stack is actively in play.

**Newfold discloses none of this.** Its subprocessor list (updated 6 Jan 2026) names 38 vendors including WHMCS but **not one payment processor**, hiding them behind "Fraud detection and deterrence services." [S3l]

**Do NOT conflate (verified merchant-side, not Newfold's own rail):**
- **Razorpay** — 2021 partnership for *Bluehost customers'* online stores, not Bluehost's billing. [S3d]
- **Asaas** — "Gerenciador de Cobranças Asaas" bundled with HostGator BR hosting for *customers'* invoicing (found in page JSON). [S3e]
- **PagSeguro** — rates for HostGator's *store-builder* product. [S3f]

### 3B. Orchestrator

**No public evidence found.** Searched Spreedly, Primer, Gr4vy, CellPoint, APEXX against Newfold and every brand: zero company-specific hits. Also searched Cybersource, Worldpay, Chase Paymentech, Recurly, Zuora, Chargebee, Adyen, Stripe, Braintree, Checkout.com with no confirmed hit for Newfold's own processing outside India.

**Checkout source code was ultimately recovered** (see §3A) via the archived `reg3-bundle.js`, despite every live checkout returning Cloudflare 403. Note: apparent PSP keyword matches *inside the 403 challenge bodies themselves* are false positives from random base64 and were discarded. The bundle confirms three processors and **no orchestration vendor**: no Spreedly, Primer, Gr4vy, CellPoint or APEXX string appears anywhere in it.

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123

### 3C. Contractual currencies

**Six:** USD, GBP, CAD, EUR, AUD, INR. Refunds issued in original currency, except Bluehost US where "all refunds are processed in U.S. dollars and will reflect the exchange rate in effect on the date of the refund" (customer absorbs FX movement on refunds). [S2b]

### 3D. SEC risk language (predecessor, verbatim)

From Endurance International Group FY2019 10-K [S3c]:

> "**A majority of our revenue is processed through credit card transactions.**"

> "our credit card processors **have in the past** and could in the future **impose fines on us as a result of increased refunds and chargebacks**... could require us to **maintain or increase reserves, increase our processing fees, terminate their contracts with us**"

> "we offer our products and services through **numerous brands that operate from different websites, control panels, billing systems**... **differences across our multiple billing systems have at times made it challenging for us to accurately and consistently determine certain enterprise-wide operational metrics, such as total subscribers**"

> "**In the past, we have identified control gaps in our adherence to PCI DSS in certain of our brands**"

Restricted cash held by merchant banks and processors as chargeback collateral: **$1.932M (Dec 2018) → $1.732M (Dec 2019)**.

*Attribution note: these are Endurance International filings, Newfold's largest predecessor. Newfold is private and files nothing with the SEC.*

---

## SECTION 4 — APMs

### 4A. Confirmed APMs (pages fetched)

| Market | APMs Confirmed | Verification Source | Source |
|---|---|---|---|
| **US — Bluehost** | PayPal, **Google Pay**. Renewals only: checks, money orders, wire | Official KB, fetched | [S3a] |
| **US — Network Solutions** | **Apple Pay**, **Google Pay**, PayPal (legacy wallet only). Checks by post, renewals only | Official KB | [S4a] |
| **US — HostGator** | PayPal (instant only; requires linked bank or card) | Official KB | [S4b] |
| **India — Bluehost (INR)** | **UPI** (cart ≤ ₹1,00,000), **Net Banking**. Via **PayU**. Cart capped ₹2,50,000 | Official KB, verified firsthand | [S3a] |
| **Brazil — HostGator** | **Pix**, **Pix Automático / Pix Recorrente (LIVE)**, **Boleto Bancário**, PayPal, cards (Visa, Mastercard, **Hipercard**, **Elo**). **Parcelamento to 12x** on annual/biennial/triennial, min R$100 | Official KB + pricing page | [S3b] [S4c] [S4g] |
| **Mexico — HostGator** | **OXXO**, **7-Eleven** cash, **Bancomer** transfer, PayPal | Official KB | [S4d] |
| **Colombia — HostGator** | **PSE**, **Efecty** | Official KB | [S4e] |
| **Chile — HostGator** | **Webpay**, **Khipu**, **ServiPag** | Official KB | [S4e] |
| **Argentina — HostGator** | **RapiPago**, **Pago Fácil**, bank transfer, local cards (Cabal, Naranja, Nativa, CMR Falabella, Cencosud, Argencard) | Official KB | [S4e] |
| **Peru — HostGator** | **PagoEfectivo**, BCP, **Payvalida**, QR | Official KB | [S4e] |
| **AU/NZ/IN — Crazy Domains** | PayPal, debit & prepaid cards. **POLi and bank transfer discontinued** | Official KB | [S4f] |

### 4B. Unverified Markets

| Market | Attempted? | Reason Not Verified | Popular Local APMs *(market context only, NOT a claim about Newfold)* |
|---|---|---|---|
| India — BigRock | Yes | **HTTP 403** bot-block on bigrock.in/support/payment-options.php | UPI, RuPay, net banking, Paytm/PhonePe, card EMI |
| Crazy Domains AU/UK | Partial | 403 on several regional help articles | BPAY, PayID/Osko, Apple/Google Pay, BNPL |
| Web.com, Domain.com, Register.com | No | Not reached within budget | — |
| UAE / Saudi Arabia | No | No regional help page located | mada (SA), Apple Pay, local debit |
| Netherlands / Germany / Spain | No | No regional help page located | iDEAL, SEPA DD, Bizum |

> **"Not verified" ≠ "not available."** Aggregator sites (whoacceptsit, knoji) claimed Afterpay/Zip/Klarna/Alipay on Crazy Domains and UPI/RuPay/Paytm on BigRock; **none traced to an official page**, so none are carried forward. MANUAL: VPN checkout walk-through before any APM claim.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| **Billing issues** | BBB — Newfold Digital | **584 complaints / 3 yrs; 124 closed in 12 mo; 84 tagged Billing**. **BBB "Pattern of Complaints" alert active** | to Jun 2026 | [S5a] |
| **Billing issues** | BBB — Network Solutions | **192 / 3 yrs; 86 closed in 12 mo; 36 Billing.** D− rating, not accredited | to Jun 2026 | [S5b] |
| Unrecognised auto-renewal, high ticket | BBB | "a charge of $550... for 3/year hosting under 'auto-renew'"; "$451.83 USD" | May 2026 | [S5a] |
| Renewal price mismatch | BBB | "renewal pricing... $28.99 per month... advertise a renewal rate of $18.99" | May 2026 | [S5a] |
| **Charge to a cancelled card** | BBB | "charged $94.92 to my BMO credit card... which had been officially CANCELLED on May 2, 2026" | Jun 2026 | [S5b] |
| Unauthorised add-on + refund refusal | BBB | "charged me for privacy protection... They refused to issue a refund" | Jun 2026 | [S5b] |
| **Cobrança indevida / renovação automática** | Reclame Aqui (BR) | Distinct recurring cluster; amounts R$274 to >R$500 | ongoing | [S5c] |
| Duplicate charges | Bluehost KB | Dedicated article *"I have been charged twice"* (indexed; 404 on fetch). Bluehost's own top-5 chargeback causes include "billing errors or duplicate charges" | current | [S5d] |
| AVS declines | HostGator KB | Billing-address mismatch called "one of the most common errors" | current | [S5e] |
| FX loss on refund | Bluehost T&C | US refunds in USD at refund-date rate | current | [S2b] |

**Analysis → Yuno mapping.** Every dominant theme is a *payments-infrastructure* problem, not a customer-service one:
- Unrecognised high-ticket renewals ($450–$590 single charges) are exactly the profile issuers decline for suspected fraud and customers dispute. → **NOVA** false-decline reduction + clearer descriptors.
- Charges to cancelled cards and cards failing after the first charge → **network tokenization** and **Account Updater across all schemes**, not just Visa/Mastercard.
- Chargebacks are frequent enough that Bluehost publishes a punitive policy ("Submitting a chargeback will result in your Bluehost account being suspended"). → **Failover + Recovery** converts disputes into recovered renewals.

### 5A. ⭐ Self-documented involuntary churn (verified firsthand)

Bluehost's KB, verbatim [S5f]:
> "There is an increasing trend in issuing companies requiring that the customer's security code on the back of the card be submitted along with the recurring payment requests." · "It is illegal for Bluehost to store this number." · **"Some cards will work the first time but fail every subsequent time."**
>
> Remedies offered: **"The only options we can suggest are using a different credit card or logging in every month to manage your account and pay your invoice manually."**

### 5B. Retry logic is a cascade, not intelligence

Bluehost KB [S5g]:
> "If your primary payment method fails, our system will immediately attempt to charge your next available saved payment method. The system will cycle through **up to 4 different cards on file** before returning to re-attempt the first card."

No retry timing, no soft-vs-hard decline logic, no issuer-aware scheduling, and it depends on a consumer/SMB having up to four cards saved. Mitigation is limited to **Visa Account Updater and Mastercard Automatic Billing Updater** (verified firsthand) — leaving Amex, Discover and every non-US scheme uncovered.

### 5C. The term structure amplifies it

Bluehost user agreement [S2b]: terms ≥3 months charge **15 days before** term end; monthly terms charge **24 hours before expiry "without any prior notice"**; opt-out requires **16 days**; disputes allowed for **90 days**. On a 1-to-3-year term, **a single stored card must survive 12 to 36 months** before it is charged again, against natural card churn from expiry, reissue and loss.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | 2025-02-14 | **Moody's downgrades CFR to Caa1 from B3**, outlook negative. Cites $380M revolver refi risk (Feb 2026, $223M drawn) and "lower than expected revenue growth". ~$89M cash | Credit | [S6a] |
| 2 | 2025-04 → 06 | **Web.com brand retired**; accounts migrated into Network Solutions | Restructuring | [S6b] |
| 3 | 2025-05-14 | **Sachin Puri appointed CEO, Bluehost Group** (ex-StubHub, McAfee, WP Engine, Liquid Web) | Leadership | [S6c] |
| 4 | 2025-06-03 | Christina Clohecy appointed CEO, Network Solutions Group | Leadership | [S6d] |
| 5 | 2025-09-18 | **Wesley Pua appointed CFO, Bluehost Group** (ex-Fabric, Udemy through IPO) | Leadership | [S6e] |
| 6 | 2025-09-25 | Agreement to sell **MarkMonitor to Com Laude** | M&A | [S6f] |
| 7 | 2025-10-17 | Seeking creditor support for debt deal via side pacts (PIMCO, GoldenTree in group) | Credit | [S6g] |
| 8 | 2025-12-09 | **$100M financing** from Clearlake + Siris; maturities extended to 2029, some obligations discounted | Credit | [S6h] |
| 9 | 2025-12-18 | **Antonis Papatsaras appointed CTO, Bluehost Group** (ex-Hootsuite, DocuSign CLM) | Leadership | [S6i] |
| 10 | 2025-12-31 | **MarkMonitor sale completed.** "Simplify our portfolio and strengthen our focus on Bluehost and Network Solutions" (Rowlands). Price undisclosed by Newfold | M&A | [S6j] |
| 11 | 2024-11 | Tony Murphy appointed CIO, Newfold Digital | Leadership | [S6k] |
| 12 | ongoing | **Open role: "Senior Manager, Payment Systems and Processing"** — "leads and oversees the end-to-end operations of the organization's payment systems", "optimizing payment processing systems and workflows" | **Payments hiring** | [S6l] |
| 13 | ongoing | Senior Java Developer, **Billing team** (req R14611; R12772 Brazil-Remote) | Payments hiring | [S6m] |
| 14 | ongoing | Billing and Risk Mitigation Associate, Mumbai | Payments hiring | [S6n] |

**Structural read.** Bluehost Group replaced its **entire C-suite inside eight months** (CEO May, CFO Sep, CTO Dec 2025, plus group CIO Nov 2024), all from SaaS/eCommerce/marketplace backgrounds, while running a P&L split from Network Solutions. That is a stack-decision window, and there is an open payments-systems leadership role to own it.

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | — | **No new PSP partnership, PSP removal, or billing replatform announced in the last 24 months** | 🟡 Neutral. No incumbent orchestrator to displace, no recent lock-in event | multiple |
| 2 | 2021-07-22 | Bluehost × Razorpay for **customers'** online stores in India | 🟢 Shows India payments partnership appetite, merchant-side only | [S3d] |
| 3 | 2023-02-01 | Acquired **DLoja Virtual** (Brazil store builder) "integrated with the most relevant payment gateways... in Brazil" | 🟢 Deepens Brazil commerce surface | [S7a] |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Hosted, account-first, on-site | 🟡 | 10 documented steps from landing to portal [S8a] |
| Guest checkout | **None.** "To proceed, create your Bluehost account with your email address and password" | 🔴 | Account creation mandatory before payment |
| Steps to purchase | 10, including a **data-centre choice from 10 locations** inserted mid-funnel | 🔴 | Technical decision inside a purchase flow |
| 3DS | Not mentioned on any US page. India (PayU) implies OTP/3DS | 🟡 | Unverified outside India |
| Mobile experience | No mobile-specific guidance published | 🟡 | Not verified |
| APM display logic | **Geo-varying and fragmented.** US = cards/PayPal/Google Pay; India = UPI/NetBanking via PayU, no PayPal; Brazil = Pix/Boleto/parcelamento, **domestic-issued cards only**; Mexico = OXXO/7-Eleven/Bancomer | 🔴 | Sibling brands differ **within the same country**: Network Solutions US has Apple Pay, Bluehost US does not |
| Auto-renew disclosure | Not present in the signup KB; terms live only in the User Agreement | 🔴 | Correlates with the BBB unrecognised-renewal cluster |
| Stored credentials | US: cards on file + PayPal Billing Agreements (changeable **only at PayPal**, not in-portal). **India: cannot store methods, no auto-renewal** | 🔴 | Newfold has no in-portal control over a material share of its mandates |

> ⚠️ MANUAL: Walk checkout in US, Brazil and India before the call.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| **Not published.** Policy asserts "compliance with the Payment Card Industry – Data Security Standard" with "regular security reviews", but names no level, QSA, AoC, ISO 27001 or SOC 2 | Cards stored on file for recurring billing; **CVV explicitly not stored** ("illegal for Bluehost to store this number"); Visa AU / Mastercard ABU in production | **Yuno Vault + network tokenization.** Removes PAN from Newfold's scope, restores CVV-less recurring success via network tokens, and extends card-lifecycle updates beyond Visa/Mastercard | [S9a] [S5f] |

Predecessor filing admits: "**In the past, we have identified control gaps in our adherence to PCI DSS in certain of our brands**" and "we are required to reimburse our processor for penalties imposed by credit card associations." [S3c]

Bluehost's own customer-facing posture: "**Bluehost does not guarantee PCI compliance on all accounts**", framing PCI as the hosting customer's responsibility. [S9b]

**Explicit non-finding:** no public AoC, Level 1 Service Provider listing, or trust portal for Newfold or any brand. Absence of evidence, not evidence of non-compliance.

---

## SECTION 10 — Strategic Insights

### Insight #1: They published their own involuntary-churn confession
**Evidence:** §5A — "Some cards will work the first time but fail every subsequent time"; remedy is to pay manually every month. §5B — a 4-card cascade with no issuer-aware retry. Account Updater covers Visa/Mastercard only.
**Pain Point:** A ~7M-subscriber recurring business is telling customers its stored-card rail cannot bill them reliably, then asking them to do it by hand. Every manual step is a churn event.
**Yuno Value Prop:** Network tokenization removes the CVV dependency entirely; issuer-aware smart retries plus multi-PSP failover replace the cascade; recovery of up to 50% of failed transactions.
**Best Case:** **Livelo** recovered +5% approvals within 3 months.
**Outreach Angle:** Lead with their own sentence. Nothing lands harder than quoting a merchant's help centre back to them and asking what that costs at seven million subscribers.

### Insight #2: India accepts UPI but cannot renew on it
**Evidence:** §4A and §2 — UPI and Net Banking live via PayU, but "customers cannot store Indian payment methods on file or set up auto-renewals in India", cart capped at ₹2,50,000, and purchases moved to the **US Bluehost Inc. entity** on 18 Sep 2025.
**Pain Point:** India is ~5.8% of portfolio traffic across three brands and structurally the highest-churn cohort, because every renewal is a manual, customer-initiated repurchase.
**Yuno Value Prop:** **UPI AutoPay** e-mandates plus RBI-compliant tokenization restore true recurring billing in India, with local acquiring to avoid cross-border decline penalties on a US entity.
**Best Case:** **InDrive** stood up 10 LATAM markets in under 8 months at 90% approval.
**Outreach Angle:** "You accept UPI in India but can't auto-renew on it. That makes your fastest-growing region your leakiest." Pair with the entity switch.

### Insight #3: Three processors on one checkout, and a second checkout no one routes with
**Evidence:** §3A — Newfold's own checkout bundle runs **Worldpay, BillDesk and PayU** across a single map of nine brands, while **Network Solutions, Web.com and Register.com are absent from that map entirely** and run a separate stack. Brazil sits on a WHMCS/Bradesco boleto rail, Crazy Domains on Dragonpay via a Singapore merchant entity, ResellerClub on Pay.pw and EBANX. Fraud is split across Sift, iovation and MaxMind. No orchestrator found, and Worldpay was only added between late 2021 and early 2024.
**Pain Point:** Multiple acquirers already exist, but nothing routes between them. There is no cross-PSP failover, no single approval-rate owner, and (per the 10-K) billing-system fragmentation severe enough to blur the subscriber count.
**Yuno Value Prop:** One API over 1,000+ methods and 30+ PSPs, with per-transaction routing by BIN, issuer and market, and unified reconciliation across all brands.
**Best Case:** **Rappi** removed implementation time entirely and cut analyst resolution effort by 80%.
**Outreach Angle:** Ask who owns approval rate across Bluehost, HostGator, Network Solutions and BigRock. The answer is usually nobody, because each brand inherited its own rail.

### Insight #4: Retention is the lender-watched metric
**Evidence:** §6 — Moody's **Caa1**, negative outlook, explicitly citing "lower than expected revenue growth"; ~$3.5B debt; $100M sponsor financing Dec 2025; MarkMonitor divested to focus on Bluehost and Network Solutions.
**Pain Point:** With growth capital constrained and the portfolio simplified to two core brands, recovered revenue from existing subscribers is the cheapest available growth. Involuntary churn is pure margin leakage.
**Yuno Value Prop:** Recovery is booked revenue, not new acquisition spend. Every saved renewal flows straight to the metric the sponsors and rating agencies are watching.
**Best Case:** **Livelo** +5% approvals in 3 months; up to 50% recovery on failed transactions.
**Outreach Angle:** Frame in CFO language for **Wesley Pua**: no new CAC, no new markets, just the renewals already earned and currently lost at the issuer.

### Insight #5: A brand-new C-suite and an open payments role
**Evidence:** §6 — Bluehost Group CEO (May 2025), CFO (Sep 2025), CTO (Dec 2025), group CIO (Nov 2024), plus an open **Senior Manager, Payment Systems and Processing** owning "end-to-end operations of the organization's payment systems."
**Pain Point:** No publicly identifiable Head/VP of Payments exists today, and four new executives are re-evaluating inherited infrastructure simultaneously.
**Yuno Value Prop:** Orchestration is the standard answer to "we inherited nine rails and one named processor", and it can be evidenced before the new payments hire even lands.
**Best Case:** **Rappi**, zero implementation time.
**Outreach Angle:** Time it to the hiring window. Offer the audit the new payments manager will be asked to produce in their first 90 days.

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| GoDaddy | godaddy.com | Tempe, AZ | FY25 rev **$4.95B**, 20.4M customers | US, EU, LATAM, APAC | [S11a] |
| Hostinger | hostinger.com | Kaunas, LT | 2025 rev **€275.4M (+51%)**, 4.6M customers, 150+ countries | BR, MX, AR, CO, EU, APAC | [S11b] |
| IONOS Group | ionos.com | Montabaur, DE | FY25 rev **€1.317B**, 6.63M customers | DACH, EU, US, MX | [S11c] |
| Namecheap | namecheap.com | Phoenix, AZ | 2024 rev **$398M**; CVC majority at ~$1.5B EV | US, EU, APAC | [S11d] |
| Tucows | tucows.com | Toronto, CA | FY25 rev **$390.3M** | Global wholesale | [S11e] |
| OVHcloud | ovhcloud.com | Roubaix, FR | FY25 rev **€1.085B** | EU, APAC | [S11f] |
| SiteGround | siteground.com | Sofia, BG | Private, margin >50% | EU, US, APAC | [S11f] |
| Liquid Web | liquidweb.com | Lansing, MI | ~$105M rev | US | [S11g] |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Wix | wix.com | Website builder SaaS | 190+ countries | Same SMB web-presence subscriber, global LPM need | [S11h] |
| Squarespace | squarespace.com | Website builder SaaS | US, EU | **Permira take-private $7.2B**; 5.2M+ subscriptions, ARPUS $225 | [S11i] |
| Automattic | automattic.com | WordPress / hosting | Global | 2024 rev $710M; WooPayments rail | [S11j] |
| WP Engine | wpengine.com | Managed WordPress | US, EU, APAC | ~$236M rev, Silver Lake-backed | [S11k] |
| **Locaweb** | locaweb.com.br | BR hosting + payments | **Brazil** | FY25 **TPV BRL 8.9B (+17.7%)**; direct BR rival running its own rail | [S11l] |
| KingHost | kinghost.com.br | BR hosting | Brazil | Locaweb-owned, Pix/Boleto native | [S11l] |
| DigitalOcean | digitalocean.com | Cloud infra | Global | Developer subscription billing | [S11f] |
| Shopify | shopify.com | Commerce platform | Global | 4.1% hosting share; 100+ gateways | [S11m] |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| **Wix** | **Multi-PSP: Adyen + Stripe + PayPal**, plus a **PSP Service Plugin** framework for third-party processors | current | Website builder | [S11h] |
| Hostinger | Region-specific multi-rail (PIX, Boleto, OXXO, SPEI, installments, wallets, crypto); "available payment methods differ depending on where services were purchased" | current | Hosting | [S11b] |
| Automattic | WooPayments (Stripe) + gateway marketplace | current | WordPress | [S11j] |

*No orchestration **vendor** is publicly named for Newfold or any direct hosting competitor. Wix and Hostinger are the closest analogues and both run deliberate multi-rail strategies.*

### 11D. Scoring — Newfold Digital

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ US, BR, IN, MX, AU, SG, UK, CO, CL, AR, PE |
| Multiple PSPs | +3 | ✅ **Verified in Newfold's own checkout code:** Worldpay + BillDesk + PayU on one shared 9-brand checkout, plus Bradesco/WHMCS (BR), Dragonpay (Crazy Domains), Pay.pw + EBANX (ResellerClub) |
| Recent expansion (24 mo.) | +2 | ✅ Divestiture, brand consolidation, group split, 4 exec hires |
| Public payment issues | +2 | ✅ BBB Pattern-of-Complaints alert, 84 billing complaints, self-documented recurring failure |
| Funding >$10M | +2 | ✅ $100M financing Dec 2025 |
| LATAM/APAC/MENA traffic | +2 | ✅ BR 22.9%, MX 3.3%, IN 5.8%, AU 2.8%, Gulf growing 36–51% |
| No orchestrator | +2 | ✅ Zero evidence found |
| Payment job postings | +1 | ✅ Senior Manager, Payment Systems and Processing |
| Public RFP | +3 | ❌ None found |

**Score: 17 → 🔴 HIGH PRIORITY**

### Top 10 Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | **Newfold Digital** | Target | US, BR, IN, MX, AU | **17** | 🔴 High | 3+ acquirers on one checkout with no routing layer, plus self-documented recurring-billing failure at ~7M subs |
| 2 | Hostinger | Competitor | BR, MX, AR, CO, EU, APAC | 13 | 🔴 High | 150+ countries, deep LPM matrix, +51% growth, no orchestrator named |
| 3 | GoDaddy | Competitor | Global | 12 | 🔴 High | 20.4M customers, own acquiring plus third-party gateways |
| 4 | Locaweb | Peer | Brazil | 12 | 🔴 High | BRL 8.9B TPV, runs its own rail, LATAM native |
| 5 | Namecheap | Competitor | US, EU, APAC | 11 | 🟡 Medium | New CVC ownership at $1.5B, stack review window |
| 6 | IONOS Group | Competitor | DACH, EU, MX | 11 | 🟡 Medium | 6.63M customers, EU multi-country billing |
| 7 | Squarespace | Peer | US, EU | 10 | 🟡 Medium | Permira take-private, 5.2M+ subscriptions |
| 8 | WP Engine | Peer | US, EU, APAC | 9 | 🟡 Medium | Silver Lake-backed, subscription billing |
| 9 | Tucows | Competitor | Global wholesale | 9 | 🟡 Medium | Multi-currency reseller settlement |
| 10 | OVHcloud | Competitor | EU, APAC | 8 | 🟡 Medium | €1.08B revenue, EU-centric expansion |

**Pipeline Summary:** 16 companies mapped, **4 high-priority**. Strongest vertical: **SMB web-presence and hosting subscriptions**, concentrated in **Brazil, India and Mexico** where local rails already dominate and every player is stitching them per-region. Locaweb and Hostinger are the two best adjacent entries.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| **Not verifiable.** Aggregator estimates diverge wildly ($926M RocketReach / $1.1B ZoomInfo / $1.4B CompWorth / $5B LeadIQ). No filing, no company disclosure. Predecessor Endurance reported **$1,113.28M in FY2019** (US $812.87M / Intl $300.41M, 27% international) | **Not disclosed.** Observed renewal charges in BBB complaints: **$94.92, $451.83, $550, $587.88**. Brazil parcelamento minimum **R$100** | **Not disclosed.** Anchor: "nearly 7 million customers" on recurring terms of 1 month to 3 years | **USD**, plus GBP, CAD, EUR, AUD, INR (6 contractual) | **United States (39.1%), Brazil (22.9%), India (5.8%)** |

**Do not quote a revenue figure.** Use "nearly 7 million customers" (company-stated) and the 6-currency footprint instead. Directional sizing should be built from subscriber count × observed renewal tickets, flagged as an estimate.

---

## SECTION 13 — Outreach

```
--- LINKEDIN MESSAGE ---

Hi Sachin, congrats on the first year leading Bluehost Group.

I was reading Bluehost's own billing help pages and one line stopped me:
"Some cards will work the first time but fail every subsequent time."
The article's suggested fix is that customers log in every month and pay
the invoice manually.

At nearly 7 million subscribers on 1 to 3 year terms, that is a lot of
renewals resting on a stored card surviving 12 to 36 months, with a
4-card cascade and Visa/Mastercard Account Updater as the only safety
net. India looks even tighter, since methods there cannot be stored for
auto-renewal at all.

You already run Worldpay, BillDesk and PayU across one shared checkout,
with Network Solutions on a separate stack. Nothing routes between them.
Yuno is that layer: network tokenization removes the CVV dependency,
issuer-aware retries replace the cascade, and UPI AutoPay restores true
recurring billing in India. Livelo recovered +5% approvals in 3 months
and InDrive runs 10 LATAM markets at 90% approval.

Worth 20 minutes to show you where the renewals are leaking? I have
Tuesday or Thursday afternoon next week.

--- COLD EMAIL ---
Subject: The line in Bluehost's help centre about recurring charges

Hi Wesley,

Bluehost's billing KB tells customers that "some cards will work the
first time but fail every subsequent time," and recommends they log in
each month to pay manually. That is involuntary churn, documented by
you, at nearly 7 million subscribers.

The structure makes it worse. Terms run 1 to 3 years, so a stored card
has to survive up to 36 months before it is charged again. Recovery
today is a cascade through up to 4 saved cards, backed by Visa and
Mastercard Account Updater, which leaves Amex, Discover and every
non-US scheme uncovered. In India, methods cannot be stored for
auto-renewal at all, so every renewal is a manual repurchase in a
market that is roughly 6% of your traffic across three brands.

You already run Worldpay, BillDesk and PayU on one shared checkout, and
Network Solutions sits on a separate stack entirely. The acquirers exist,
the routing between them does not. Yuno is one API over 1,000+ payment
methods and 30+ PSPs: network tokenization removes the CVV dependency,
issuer-aware retries and cross-PSP failover recover up to 50% of failed
transactions, and UPI AutoPay restores true recurring billing in India.

Livelo recovered +5% approvals within 3 months. InDrive runs 10 LATAM
markets at 90% approval. No new CAC, just the renewals you already
earned.

Open to 20 minutes next week to walk through where it is leaking?

German
```

---

## APPENDIX — Source URLs

```
[S2a] https://newfold.com/privacy-center/privacy
[S2b] https://www.bluehost.com/terms/user-agreement
[S2c] https://cnpj.biz/15754475000140
[S2d] https://www.sgpbusiness.com/company/Dreamscape-Networks-International-Pte-Ltd
[S2e] https://www.sec.gov/Archives/edgar/data/0001237746/000162828020001590/eigi1231201910-k.htm
[S2f] https://find-and-update.company-information.service.gov.uk/search/companies?q=newfold
[S3a] https://www.bluehost.com/help/article/payment-types-accepted
[S3b] https://www.hostgator.com.br/formas-de-pagamento
[S3c] https://www.sec.gov/Archives/edgar/data/0001237746/000162828020001590/eigi1231201910-k.htm
[S3d] https://bfsi.eletsonline.com/bluehost-razorpay-partner-to-expand-online-store-solution-with-integrated-payments-for-india/
[S3e] https://www.hostgator.com.br/hospedagem-de-sites
[S3f] https://suporte-loja.hostgator.com.br/hc/pt-br/articles/27101719088403
[S4a] https://www.networksolutions.com/help/article/make-payment-to-renew
[S4b] https://www.hostgator.com/help/article/what-forms-of-payment-do-you-accept
[S4c] https://suporte.hostgator.com.br/hc/pt-br/articles/30823530972819
[S4d] https://soporte.hostgator.mx/hc/es-419/articles/28446271360275
[S4e] https://soporte-latam.hostgator.com/hc/es-419/articles/217286347
[S4f] https://www.crazydomains.com.au/help/article/what-credit-cards-are-accepted
[S4g] https://suporte.hostgator.com.br/hc/pt-br/articles/42481864736787
[S3g] http://web.archive.org/web/20240525020918id_/https://static.registration.bluehost.com/1274/static/reggie/js/reg3-bundle.js
[S3h] http://web.archive.org/web/20240906222146/https://financeiro.hostgator.com.br/gatorpay/1af1689a-6862-448c-8451-997638788328
[S3i] https://www.crazydomains.com.au/privacy/terms-of-service/
[S3j] http://web.archive.org/web/20260306040933/https://www.resellerclub.com/domain-reseller/payment-methods
[S3k] http://web.archive.org/web/20251006140347/https://br.resellerclub.com/domain-reseller/payment-methods
[S3l] https://www.newfold.com/privacy-center/third-party-data
[S5a] https://www.bbb.org/us/fl/jacksonville/profile/web-hosting/newfold-digital-inc-0403-236012022/complaints
[S5b] https://www.bbb.org/us/fl/jacksonville/profile/internet-service/network-solutions-0403-235968175/complaints
[S5c] https://www.reclameaqui.com.br/hostgator/cobranca-indevida-renovacao-automatica-de-dominio_-M7fk1BN4XCPiZ__/
[S5d] https://www.bluehost.com/blog/what-is-a-charge-back/
[S5e] https://www.hostgator.com/help/article/unable-to-make-a-payment-payment-errors
[S5f] https://www.bluehost.com/help/article/recurring-charges-why-contact
[S5g] https://www.bluehost.com/help/article/bh-invoicing-and-automatic-billing
[S6a] https://in.investing.com/news/stock-market-news/newfold-digitals-ratings-downgraded-by-moodys-due-to-refinancing-risk-93CH-4668171
[S6b] https://www.prnewswire.com/news-releases/network-solutions-and-webcom-consolidate-to-deliver-an-even-stronger-all-in-one-digital-experience-302484560.html
[S6c] https://www.newfold.com/newsroom/bluehost-group-appoints-sachin-puri-as-chief-executive-officer-t
[S6d] https://www.newfold.com/newsroom/christina-clohecy-appointed-chief-executive-officer-of-network-s
[S6e] https://www.prnewswire.com/news-releases/bluehost-appoints-new-cmo-and-cfo-to-accelerate-ai-powered-saas-platform-for-smbs-302559819.html
[S6f] https://www.prnewswire.com/news-releases/newfold-digital-to-sell-markmonitor-to-com-laude-302565131.html
[S6g] https://www.bloomberg.com/news/articles/2025-10-17/clearlake-s-newfold-seeks-support-for-debt-deal-via-side-pacts
[S6h] https://www.prnewswire.com/news-releases/newfold-digital-secures-100-million-investment-to-accelerate-growth-302635827.html
[S6i] https://www.prnewswire.com/news-releases/bluehost-appoints-antonis-papatsaras-as-chief-technology-officer-to-lead-ai-driven-innovation-for-smbs-302646186.html
[S6j] https://www.prnewswire.com/news-releases/newfold-digital-completes-sale-of-markmonitor-to-com-laude-302651398.html
[S6k] https://www.prnewswire.com/news-releases/newfold-digital-appoints-tony-murphy-as-new-cio-302297876.html
[S6l] https://www.ziprecruiter.com/co/newfold-digital/Jobs
[S6m] https://web.wd1.myworkdayjobs.com/en-US/ExternalCareerSite/job/Senior-Java-Developer_R14611
[S6n] https://foundthejob.com/newfold-digital-jobs-2024-freshers-billing-and-risk-mitigation-associate/
[S7a] https://www.prnewswire.com/news-releases/newfold-digital-expands-global-commerce-offerings-with-acquisition-of-dloja-virtual-301735684.html
[S8a] https://www.bluehost.com/help/article/how-to-sign-up-for-an-account
[S9a] https://www.newfold.com/privacy-center/information-security-policy
[S9b] https://www.bluehost.com/help/article/pci-compliance
[S11a] https://www.sec.gov/Archives/edgar/data/1609711/000160971126000008/gddyex991x20251231xq4earni.htm
[S11b] https://www.hostinger.com/blog/financial-results-2025
[S11c] https://www.ionos-group.com/fileadmin/Publications/Berichte/FY_2025/IONOS_Annual_Report_2025.pdf
[S11d] https://domainnamewire.com/2025/09/12/private-equity-firm-is-buying-namecheap-in-deal-that-values-company-at-1-5-billion/
[S11e] https://www.sec.gov/Archives/edgar/data/909494/000143774926008009/tcx20251231_10k.htm
[S11f] https://webhosting.today/2026/07/13/the-balance-sheet-behind-your-renewal-invoice-who-owns-the-hosting-industry-and-what-it-owes/
[S11g] https://www.oneequity.com/news/one-equity-partners-acquires-cloud-services-provider-liquid-web-and-forms-new-holding-company-cloudone-digital/
[S11h] https://www.wix.com/about/terms-of-payments
[S11i] https://www.permira.com/news-and-insights/announcements/squarespace-to-go-private-in-69bn-all-cash-transaction-with-permira
[S11j] https://getlatka.com/companies/automattic
[S11k] https://growjo.com/company/WP_Engine
[S11l] https://locaweb.company/en/negocios/king-host/
[S11m] https://www.wpbeginner.com/research/ultimate-web-hosting-statistics-and-market-share-report/
```

---

## RESEARCH GAPS

1. **Newfold never *discloses* a processor**, but the stack was recovered from its own archived checkout code (§3A): Worldpay, BillDesk, PayU. Evidence is dated **May 2024**; the live bundle is Cloudflare-blocked, so current-state should be re-confirmed in a DevTools walk.
2. **Brazil acquirer still unnamed.** Bradesco is confirmed as the boleto *collection bank* via GatorPay/WHMCS, but the card acquirer for HostGator BR is not public. Asaas and PagSeguro are merchant-side products for HostGator's *customers*; do not conflate.
3. **No orchestration vendor**, now a stronger negative: the checkout bundle contains no orchestrator string at all.
3b. **Pix Automático is LIVE in Brazil** (verified). Do not pitch it as a gap. India, by contrast, has no auto-renewal at all.
4. **No audited revenue exists publicly.** All estimates are aggregator-grade and mutually inconsistent.
5. **BigRock and Crazy Domains APMs unverified** (HTTP 403). Do not claim gaps there.
6. **No PCI AoC or level published.**
7. **No named payments executive.** The open Senior Manager role suggests the seat is being created now.
8. S&P subscriber-loss figure (reportedly >1M lost since 2023, ~17%) comes from a secondary summary; spglobal.com and hostingadvice.com both 403'd. Re-verify before use.
