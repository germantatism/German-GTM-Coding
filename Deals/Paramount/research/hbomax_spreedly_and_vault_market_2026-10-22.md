# HBO Max payment stack, Spreedly vault model, Recurly, and the standalone vault market

Fact file for the Skydance group (Paramount+ and HBO Max) sales deck. Compiled 2026-10-22.
Method: live fetch of HBO Max web properties (curl, JS bundle inspection), vendor documentation fetched directly, 11 of 20 web searches used.
Rules: every claim carries a URL and a quote or data point with the date it was observed. Items that could not be confirmed from a primary source are marked UNVERIFIED. Nothing here is guessed.
Not included on purpose: anything about Yuno's product.

Legend: VERIFIED = fetched from the primary source on the date shown. SNIPPET = quote obtained through a search-engine snippet because the page blocks automated fetchers (Cloudflare 403); treat as near-certain but re-read manually before quoting on a slide. UNVERIFIED = not confirmed.

---

## Part A. HBO Max current payment stack (public evidence)

### A1. What the live HBO Max web sign-up loads today (observed 2026-10-22)

Source: `https://auth.hbomax.com/` returns a single-page app shell that loads `/auth/max.a66d1ab4276c605aa108.sha.js` (450,564 bytes). `https://www.hbomax.com/signup` redirects to `https://auth.hbomax.com/link?flow=signup`. The bundle's environment config and webpack chunk map were inspected.

| Vendor / component | Evidence in the production bundle | Status |
|---|---|---|
| Spreedly (iFrame tokenization, vault) | Config key `"SPREEDLY_IFRAME_SCRIPT_URL":"https://core.spreedly.com/iframe/iframe-stable.min.js"` in the `prd` block; dev/int/stg environments point to `https://core.spreedly.com/iframe/iframe-candidate.min.js`. Chunk names `chunk-spreedly-mapper` and `chunk-spreedly-alternate-payment-method-option-from-cj`. Host `core.spreedly.com` appears 4 times. | VERIFIED |
| Adyen | Chunk name `chunk-adyen-cj-mapper` (chunk id 19244) | VERIFIED (chunk name only, SDK host not observed, see note) |
| Checkout.com | Chunk name `chunk-checkout-cj-mapper` (chunk id 87583) | VERIFIED (chunk name only) |
| iyzico (Türkiye) | Chunk name `chunk-iyzico-cj-mapper` (chunk id 9316) | VERIFIED (chunk name only) |
| PayPal | Chunk name `chunk-paypal-cj-mapper` (chunk id 8294); `www.hbomax.com` `_app` chunk defines a `PAYPAL` button variant | VERIFIED |
| Antom (new vs. Aug 2026 internal notes) | Chunk name `chunk-antom-cj-mapper` (chunk id 79466). Antom is Ant International's merchant payments brand; the vendor identity behind the chunk name is an inference. | VERIFIED chunk name; vendor mapping UNVERIFIED |
| Arkose Labs (bot defense) | Chunk name `gi-sdk-core-arkose-utils` (chunk id 55754) | VERIFIED (chunk name only) |
| Kount (fraud) | No string matching `kount` or `ka.js` in the main bundle or in the two `www.hbomax.com` chunks fetched | UNVERIFIED today |
| SAP BRIM (billing) | Back-end system, not observable from the browser bundle. No public job posting or press found naming it (see A6). | UNVERIFIED |
| Braintree, Recurly, Stripe, Zuora | No matching strings in the auth bundle | Not observed |

Notes on method: the lazy-loaded vendor chunks resolve in the webpack hash map (for example `8371.0aae08aaa9f42d1787e2.sha.js`) but return HTTP 404 at `https://auth.hbomax.com/auth/<id>.<hash>.sha.js`, so the vendor SDK hosts (checkoutshopper, cdn.checkout.com, iyzico) were not observed today; the evidence is the chunk naming in the production bundle. "cj" in the chunk names appears to be an internal module naming convention; its meaning is UNVERIFIED.

Also observed on `https://www.hbomax.com/` (2.9 MB HTML): hosts `graphql.prd.api.discomax.com`, `prd.api.discomax.com`, `events.prd.api.hbomax.com`, `lightning.hbomax.com` (CDP script), `browser.sentry-cdn.com`, Akamai mPulse. Footer copyright on help pages: "© 2026 WarnerMedia Direct, LLC."

### A2. Spreedly's own public references to HBO Max (VERIFIED)

* Spreedly blog, 2025-06-24, "Spreedly Announces Just-In-Time Card Updates for Visa": "customers include BMW, Clear, HBOMax, Hopper, Lemonade, The New York Times, Priceline, SeatGeek, TravelPerk, and others". Same post: Spreedly processes "more than $50 billion in gross merchandise value (GMV) annually in over 100 countries". https://www.spreedly.com/blog/spreedly-announces-just-in-time-card-updates-for-visa
* Spreedly homepage, fetched 2026-10-22: logo wall under the heading "Payment Orchestration for the Agentic Era" shows Lemonade, Priceline, Il Makiage, HBO Max, Busbud, Cabify, Bandcamp, Chargebee, Hopper, Hotel Engine, Transit, Change.org. https://www.spreedly.com/
* Spreedly blog, 2022-02-21, "Spreedly: 2021 In Review": "Digital Goods: PAYMENTSfn Fireside Chat with streaming media provider, HBO". https://www.spreedly.com/blog/spreedly-2021-in-review
* Spreedly blog, 2022-07-15: unnamed "Spreedly customer that's a major streaming service" that "were launching in multiple new markets in Latin America and Europe"; the customer is not named, so attribution to HBO Max is UNVERIFIED. Same post: "pre-built connections to over 120 services". https://spreedly.com/blog/spreedly-solutions-stack-connect-payment-methods
* No Spreedly case study naming HBO Max, Warner Bros. Discovery or WarnerMedia was found (casestudies.com lists Chargebee, Equiant, Funraise, HealPay, PedidosYa, Pin Payments, Pushpay, SeatGeek). https://www.casestudies.com/company/spreedly

### A3. Subscribers and streaming financials (VERIFIED, SEC filings)

* WBD Q4 2025 shareholder letter, dated 2026-02-26 (Form 8-K exhibit): Streaming "ended the year with nearly 132 million subscribers"; "added nearly 15 million subscribers in 2025"; "the fourth quarter of 2025 will be the last quarter we report subscribers and ARPU"; "the Streaming segment generated $1.37 billion in Adjusted EBITDA" for FY2025. Launches: Germany and Italy (early January 2026), United Kingdom and Ireland (March 26, 2026). https://www.sec.gov/Archives/edgar/data/1437107/000143710726000011/wbd4q25earningssharehold.htm
* WBD Q2 2026 shareholder letter, dated 2026-08-06: Streaming "delivered over $3 billion in quarterly revenues for the first time ever"; "Streaming generated $512 million of Adjusted EBITDA during the quarter"; "approximately 40% of global HBO Max subscribers were on the ad-supported tier"; subscriber-related revenue growth "accelerated by 200 bps sequentially". No subscriber count disclosed (consistent with the Q4 2025 decision). https://www.sec.gov/Archives/edgar/data/0001437107/000143710726000072/wbd2q26shareholderletter.htm
* Latest hard subscriber number usable on a slide: "nearly 132 million" at 31 Dec 2025. Q1, Q2 and Q3 2026 counts: not disclosed by the company. A "125.7 million" figure circulating in trade press (Broadcast) refers to an earlier quarter; do not use. https://www.broadcastnow.co.uk/broadcast-international/hbo-maxs-international-growth-fuels-wbd-results/5207695.article
* Paramount+ (group context): "81.6 million globally" as of Q2 2026, "added 2 million subscribers" in the quarter; DTC revenue "rose 9% to $2.47 billion", Paramount+ revenue $2.1 billion (+16%); DTC profit $366 million (+44%). TheWrap, 2026-08-04. https://www.thewrap.com/industry-news/business/paramount-earnings-q2-2026/

### A4. Countries (VERIFIED, fetched 2026-10-22)

* `https://help.hbomax.com/available` lists 124 countries and territories across five regional lists (Asia Pacific 38, Europe and Central Asia 46, Latin America 20, Caribbean 19, United States 1), plus five US territories named under the US entry (American Samoa, Guam, Northern Mariana Islands, Puerto Rico, US Virgin Islands) for 129 named entries in total. The page does not state a total; it says "We anticipate that HBO Max will be available in additional countries and regions in 2026 and beyond." Türkiye is listed under Europe and Central Asia.

### A5. Accepted payment methods on HBOMax.com direct billing (VERIFIED, fetched 2026-10-22)

* help.hbomax.com article "Change a WarnerMedia-billed subscription": payment method must "Be one of these: American Express, Apple Pay, Discover, JCB, MasterCard, PayPal, or Visa"; must be issued by a US-based bank; must support recurring online payments; "Some prepaid cards don't support recurring payments." https://help.hbomax.com/us/Answer/Detail/000002528
* Billing category index: https://help.hbomax.com/us/Category/Detail/Billing_Subscription/Billing_Payment

### A6. Job postings (UNVERIFIED for vendor names)

* No current WBD or HBO Max posting mentioning Spreedly, Adyen or SAP BRIM was found on careers.wbd.com, Built In or The Muse. The only payments-specific role found, "Senior Software Engineer - Direct Payments" (Stockholm), was removed 2024-09-19 per Built In and describes the DTC platform as "container-based micro-services operated on AWS" covering "payments, to global subscriptions". https://builtin.com/job/senior-software-engineer-direct-payments/2713694
* Caution: at least one careers.wbd.com listing surfaced by search still carries stale 2025 language about a Netflix acquisition and a Discovery Global spin-off. Do not cite that language; the closed transaction is the Paramount Skydance one (A7).

### A7. Group context: Skydance closing (VERIFIED)

* AP via Live 5 News, 2026-10-06: "Skydance-owned Paramount closed its $81 billion takeover of Warner Bros. Discovery on Tuesday"; nearly $111 billion including debt; combined company called Skydance, "under the helm of billionaire David Ellison and his new co-CEO Ynon Kreiz"; HBO Max "now also find themselves under the same roof as Paramount+". https://www.live5news.com/2026/10/06/paramount-warner-bros-are-now-one-hollywood-giant-skydance-heres-how-we-got-here/
* For contrast, the 2026-08-06 WBD letter still described the closing as "on hold until the earlier of five days after legal proceedings are complete or June 1, 2027" and said "We remain highly confident that the Paramount merger will be completed." (same SEC URL as A3)

---

## Part B. Spreedly as a vault and token portability (docs.spreedly.com now redirects 301 to developer.spreedly.com; all pages fetched 2026-10-22)

### B1. Positioning on ownership and portability

* Homepage: "Store every payment method in a vault you own. Take it to any provider, and we keep it current."; "Hold every credential in your own vault, use it with any provider"; heading "Free your tokens from vendor lock-in"; solution named "Payment Token Ownership & Portability"; "Reach any gateway, provider, or processor through one integration." https://www.spreedly.com/
* "The Ultimate Guide to Vaulting" (dated 2026-05-20): "your stored payment credentials belong to your business, not to any single gateway or processor."; "Gateway-issued tokens are the property of that gateway's ecosystem. Portable tokens are yours."; "Your tokens don't go where you go, they stay where they were created" (about gateway vaults); "A standalone vault separates data storage from payment processing."; "Reducing PCI scope doesn't eliminate responsibility, it shifts it." https://www.spreedly.com/guides/vaulting

### B2. Tokenization and PCI scope

* Tokenization overview: "Tokenization is the process of safely capturing this sensitive cardholder data, including card number and CVV, and exchanging it for a secure, non-sensitive payment method token. Spreedly manages the details of securely storing this data in our vault..."; two recommended UI paths "to minimize payment page PCI scope: Headless (Hosted Fields) Checkout & Drop-in Components (Express) Checkout". Direct API: "this method accepts the greatest amount of PCI scope." https://developer.spreedly.com/docs/tokenization
* Import template references "Spreedly's Level-1 PCI compliant payment vault" and compliance documentation at https://spreedly.com/pci. https://developer.spreedly.com/docs/importing-payment-methods

### B3. Advanced Vault (page updated 2026-03-03)

* "Advanced Vault is the evolution of our vault and lifecycle services to a managed vault that combines core vaulting, lifecycle functionality, and data enrichment of payment methods with rules and best practices."
* Includes "Lifecycle management solutions for vaulted payment methods that include coverage for Visa, Mastercard, and Discover brands. Real time Mastercard updates will be enabled or same-day notifications (push) when updates occur with the network. Visa JIT offers real time pull updates via the `inquiry` API."; "Network Tokenization for eligible payment methods to improve security and authorization rates."
* Enablement table: Batch Lifecycle Management (Visa, MC, Discover) "Available for use immediately after AV enrollment"; Mastercard Real Time Updater "~3 Weeks"; Visa Just In Time "~3 Weeks"; Mastercard Network Tokenization "~1-2 Weeks"; Visa Network Tokenization "~1-2 Weeks".
* Enrollment: "A payment method is only enrolled when the Organization and Environment it resides in are enabled, and the payment method itself is enabled (`managed:true`) for Advanced Vault." `update_gratis` lets customers change AV flags "while not incurring a billable API call."
* Un-enrollment: "If you choose to unenroll a payment method from Advanced Vault, and that payment method has a provisioned network token, we will not remove the provisioned network token. However, requests to use the network token while the payment method is unenrolled will result in a fall back to PAN."
https://developer.spreedly.com/docs/advanced-vault

### B4. Network tokenization (page updated 2026-10-13)

* "Spreedly offers Network Tokenization as part of Spreedly's Advanced Vault Product."; "As a Token Requestor Token Service Provider (TR-TSP), Spreedly has completed integrations with Visa and Mastercard allowing merchants to request network tokens using their merchant-specific TRID."
* Portability across gateways: "by pairing the network token to the FPAN in a single Spreedly PCI Token, merchants have the flexibility to take advantage of network tokens on multiple gateways while also being able to use PAN for gateways that have not yet adopted network token transactions."
* Gateways enabled for network token transactions (26 listed): CyberSource, Nuvei (formerly SafeCharge), Adyen, Orbital, Checkout.com, Credorax, dLocal, Braintree*, Stripe Payment Intents*, Decidir, Worldpay, CyberSource Rest, Plexo, Vantiv eCommerce, Authorize.net, Ebanx, Redsys Rest, CommerceHub, Vantiv Express, Nuvei REST, Kushki, NMI, IPG, Adyen checkout, Worldpay New, 2C2P. (* require gateway-side activation.)
* TRID timing: Mastercard TRID "available and ready to use immediately after Spreedly processes the request, and within 72 hours after processing the request for VISA."
https://developer.spreedly.com/docs/network-tokenization

### B5. Lifecycle Management / Account Updater (page updated 2026-09-04)

* "Lifecycle Management is a feature under Advanced Vault."
* "When you opt-in, Spreedly defaults to submitting all retained, non-test, Visa, MasterCard, and Discover cards in your Spreedly vault for automatic updating twice monthly in batch on the 1st and 15th of every month, with results coming back approximately 5-6 days after they were sent. Additionally, Spreedly supports real time updates for Mastercard Cards."
* Billing: "all eligible cards will be sent for update, but you will only be charged for those cards that are identified to be updated."
* Brand swap (Visa to Mastercard and back) supported "via the batch service and Visa Just in Time API."
* Per-card exclusion via `eligible_for_card_updater: false`.
https://developer.spreedly.com/docs/account-updater

### B6. Exporting payment methods / leaving Spreedly (page updated 2025-09-15)

* "Performing an export from Spreedly to a supported endpoint/gateway, whether for the purpose of migrating one of your merchants to a new provider or for leaving the Spreedly platform completely, is a self-service process that lets you control the export timing and specifics of the process."
* Self-service path: "For any gateways that support the store transaction type, you can perform an automated export." The `store` call copies the card to the gateway vault and returns a `third_party_token`, "the unique ID of the payment method at the gateway which you can then use to transact directly against the target gateway."
* Unsupported destinations: "A manual export involves the secure exchange of encrypted files between Spreedly and the PCI compliant third party location. Spreedly generally processes exports within 2 weeks once Spreedly has all required details, assuming the third party location you're exporting to is responsive." Exports go as PGP-encrypted JSON or CSV over SFTP.
* Fees: "Spreedly does one free export per merchant for each third party storage service receiving data. Should you or your customer request multiple exports to the same third party storage service, Spreedly will charge for each additional export."
* After export: "the Spreedly tokens will still remain in your vault. It is your responsibility to redact any payment data you no longer wish to retain in the Spreedly vault."
https://developer.spreedly.com/docs/exporting-payment-methods

### B7. Third-party vaulting (page updated 2026-04-01)

* Use cases: "store cards in multiple vaults for extra redundancy"; "export credit cards when you or one of your customers is leaving for another payments provider"; "Perform a Gradual Migration".
* About 64 gateways listed as supporting `store`, including Adyen, Braintree, Checkout.com, CyberSource, Cybersource REST, EBANX, Stripe, Stripe Payment Intents, WorldPay, Rapyd, Shift4, Datatrans.
* "Since tokens are gateway specific, ThirdPartyToken payment methods are locked to the gateway type they were created against."
https://developer.spreedly.com/docs/third-party-vaulting

### B8. Payment Method Distribution (page updated 2026-10-22)

* "Spreedly supports the ability to distribute vaulted credit card data to third parties, referred to as 'receivers'."; "Payment method distribution (PMD) allows you to transact against another service's API while still controlling your customer's card data by vaulting with Spreedly."
* Two modes: "single card PMD or batch export PMD" (HTTPS endpoint per card, or SFTP file with multiple cards). Receivers must be "confirmed and implemented by Spreedly"; "allow several weeks for Spreedly to approve and configure a receiver for production use."
https://developer.spreedly.com/docs/payment-method-distribution

### B9. Importing into Spreedly (page updated 2026-06-26)

* "Spreedly will complete one import per merchant account, per third party vault at no charge. Should the merchant require any additional transfers from the same third party vault, a fee will apply."
* "Alternative payment methods have different technical restrictions that may make them ineligible for migrations between service providers" (Apple Pay, Google Pay tokens).
https://developer.spreedly.com/docs/importing-payment-methods

### B10. Gateway count and pricing

* Supported Gateways page (updated 2026-10-13): 160 unique direct gateway guides plus 7 offsite gateways linked; the page itself states no number. https://developer.spreedly.com/docs/supported-gateways
* Integrations Ecosystem page: "Showing 200 results" across gateways, payment methods and fraud tools combined; no gateway-only count. https://www.spreedly.com/connections
* Marketing count: "pre-built connections to over 120 services" (2022 post, see A2).
* Pricing page: "Independent Vault, Starting at $750 per month"; "Performance Optimization" has no published price (Contact Sales). https://www.spreedly.com/pricing
* Scale: "Annual Gross Merchant Volume (GMV) processed is expected to exceed $60 billion in 2025, up from $50 billion in 2024" (2026-01-27). https://www.spreedly.com/blog/spreedly-announces-record-growth

---

## Part C. Recurly token and vault model (short)

* PCI: "Recurly is PCI-DSS Level 1 compliant, and recognized on the Visa Global Registry of Service Providers."; "Cardholder data is sent directly to Recurly to minimize risk to your business."; "Sensitive information is stored using several layers of encryption in a segmented network with no public internet access." VERIFIED. https://recurly.com/security/
* Does Recurly vault cards itself: yes for cards and imported cards. Storage table on "Gateways and token support" (updated 2026-07-15) lists network tokens for "Cards", gateway "Any", stored in "Recurly and Visa". Network token defined as "A card token issued by a card network (e.g., Visa) that can be used across multiple gateways" and "is not bound to a single provider". Benefits: "Enable failover across gateways when using multiple providers."; "Support migrating existing subscriptions to a different gateway that supports network tokens." Gateway tokens: "Gateway tokens are not transferable between gateways." VERIFIED. https://docs.recurly.com/recurly-subscriptions/docs/gateway-token-support
* Exporting card data to another provider: "Recurly can only export credit card data in a tokenized format when a merchant is looking to migrate from Recurly to another system. The system you are migrating the data to must also be PCI compliant." SNIPPET (page returns 403 to fetchers). https://support.recurly.com/hc/en-us/articles/360026949031-Can-I-Export-Customer-Credit-Card-Data-or-Billing-Information
* Migration mechanics: "Migrating full PCI cardholder data has no self-managed path and is handled by Recurly's Professional Services team."; "On supported gateways, a merchant can use gateway tokens to keep billing subscribers without moving raw card data at all." (Stripe, Braintree, Adyen named); "Recurly's Professional Services team migrates NTIDs directly as part of its managed service." VERIFIED. https://recurly.com/glossary/data-migration/
* Gateway-to-gateway inside Recurly: "Token migration requires cooperation from both gateways. Not all processors support cross-vault migrations."; "Keep your current gateway active until all recurring billing and token migrations are fully tested and validated." SNIPPET (403). https://support.recurly.com/hc/en-us/articles/42976406636052-How-to-Migrate-to-a-New-Payment-Gateway-in-Recurly
* Importing into Recurly: "We provide PCI-compliant processes to ensure a secure migration of highly sensitive billing data." VERIFIED. https://docs.recurly.com/docs/customer-imports
* Account Updater: "monitors your customers' Mastercard®, Visa®, Discover®, and American Express® credit cards for changes"; runs pre-renewal about one week before renewal; "This feature requires an additional cost."; not included in Starter or Pro plans; Adyen RTAU "returns card update responses in real time, inline with transaction processing" but needs Adyen as the only gateway; "Recurly recommends keeping both Adyen RTAU and Recurly Account Updater enabled to cover all cases." VERIFIED. https://docs.recurly.com/docs/account-updater
* Network tokens via gateways: Adyen page, "If Adyen is enabled to create network tokens for your merchant account (cards only), Recurly surfaces whether a network token was used on each transaction."; "Token usage is determined by Adyen, not Recurly". SNIPPET. https://docs.recurly.com/recurly-subscriptions/docs/adyen

---

## Part D. Standalone vault market (speaker notes only; each line from the vendor's own pages, fetched 2026-10-22)

| Vendor | Positioning (own words) | Network tokens | Account updater | PCI proxy / forwarding | Gateway count (own claim) | Published pricing |
|---|---|---|---|---|---|---|
| VGS | "The World's Leader in Payment Tokenization"; "Collect, protect, and transmit sensitive data from a processor-agnostic, PCI-compliant vault." | Yes: "VGS issues and manages network tokens that replace primary account numbers (PANs) with secure, network-approved aliases." | Yes: "refreshes stored tokens, including network tokens, through VGS's secure network connections" | Yes: "VGS re-inserts the original data instead of the tokenized data in real-time" on outbound; "securely detokenize and forward the original data to authorized third parties" | Not stated ("any number of processors") | "Plans start at $1,000/month." (Starter); Growth: contact |
| Basis Theory | "Built to keep customers transacting"; "More than a token vault"; "An agnostic payment vault can slide into any payment stack" | Yes: "Basis Theory provides the rails to connect directly to Visa, Mastercard, or AmEx"; "Basis Theory will facilitate creating your TRID" | Yes: "Batch Account Updater supports Visa, Mastercard, American Express and Discover."; "Real-Time Account Updater supports Visa and Mastercard." | Yes: Proxy and Reactors ("our Proxy and Reactors enable your team to keep your credit cards up to date with your vendor of choice") | Not stated ("Route to any PSP") | "$995 per month, Includes 20,000 tokens*"; enterprise: "Get in touch" |
| TokenEx / IXOPAY | "TokenEx is now IXOPAY: #1 Payment Tokenization for simple PCI compliance"; "Enterprise-Grade Payment Orchestration, Tokenization, & Payments Intelligence"; Universal Tokens "reduce PCI scope by up to 90%" | Yes: "network token provisioning for major card brands, including Visa, Mastercard, and American Express"; "IXOPAY provides a TRID to each customer"; "Improve authorization rates by 4% or more" | Yes: automatic monthly updates plus "on-demand through batch file and API options" | Yes: Transparent Gateway, "Outbound replacement of token with card details keeps you out of PCI scope." | "500+" pre-built payment adapters; "200+ acquirers and 300+ payment methods"; "$171B In Payments Orchestrated in 2025"; "500+ merchants & fintechs" | None (ROI calculator only) |
| Spreedly | "Store every payment method in a vault you own. Take it to any provider, and we keep it current." | Yes (Advanced Vault, Visa + Mastercard TR-TSP, 26 gateways enabled) | Yes (Visa, MC, Discover batch 1st/15th; MC real-time; Visa JIT) | Yes: Payment Method Distribution to approved receivers; third-party vaulting via `store` | 160 direct gateway guides + 7 offsite (docs); "over 120 services" (marketing) | "Independent Vault, Starting at $750 per month" |
| Evervault | "Separate card collection and payment capabilities from your processors so you can send transactions to any downstream partner, with minimal PCI scope."; "Each product is PSP-agnostic" | Yes: "Process cards with network tokens." | Yes: "Automate card updates" (Card Account Updater) | Yes: Relay, "Send encrypted data to any API."; Functions, "Transform data before forwarding." | Not stated | Platform "$995/mo, plus usage" (under 25K tx/mo); Network Tokens "$0.03 per token", "$0.03 per cryptogram", "$0.03 per update"; Card Account Updater "$0.25 per card update" |
| Skyflow | "Protect sensitive financial data with a data privacy vault specifically designed for PCI compliance."; "reduces compliance scope by 90%" | Listed as a payments feature ("network tokenization"), no detail page found | Not mentioned on payments pages | Yes: "prebuilt connections to third-party payment processor APIs" | Not stated ("multiple leading payment processors"; Visa, Plaid, Stripe named) | None published |

Source URLs for Part D:
* VGS: https://www.verygoodsecurity.com/ , https://www.verygoodsecurity.com/vault , https://www.verygoodsecurity.com/pricing (homepage also claims "10 Billion Tokens Held Globally" and "VGS is PCI DSS Level 1 compliant")
* Basis Theory: https://basistheory.com/ , https://basistheory.com/pricing , https://developers.basistheory.com/docs/features/network-tokens , https://developers.basistheory.com/docs/features/account-updater
* TokenEx / IXOPAY: https://www.tokenex.com/ , https://www.ixopay.com/ , https://www.ixopay.com/products/payment-modules/universal-tokens , https://www.ixopay.com/products/payment-modules/network-tokens , https://www.ixopay.com/products/payment-modules/account-updater
* Spreedly: see Part B
* Evervault: https://evervault.com/ , https://evervault.com/pricing (customers named on homepage: Ramp, Overwolf, FlightHub)
* Skyflow: https://www.skyflow.com/ , https://www.skyflow.com/product/skyflow-for-payments , https://www.skyflow.com/solutions/by-use-case/solutions-card-acceptance (customer logos: Flipkart, Visa, ServiceNow, Scalapay, JULO, Apaya)

---

## UNVERIFIED or not found (do not put on slides)

1. Kount on HBO Max web checkout: not observed in the production bundle fetched 2026-10-22.
2. SAP BRIM as HBO Max billing system: no public evidence found (back-end, no postings or press).
3. Vendor behind `chunk-antom-cj-mapper` (presumed Antom by Ant International) and the meaning of "cj" in chunk names.
4. Checkout.com, Adyen and iyzico SDK hosts: chunk names observed, SDK URLs not observed (lazy chunks 404 at the guessed path).
5. HBO Max subscriber count for any 2026 quarter: not disclosed by the company after Q4 2025.
6. Whether the unnamed "major streaming service" in Spreedly's 2022 post is HBO Max.
7. Recurly support-center quotes marked SNIPPET: pages block automated fetch (Cloudflare); re-read manually before quoting.
8. Spreedly support-center articles (What is Advanced Vault, Which of my cards will be updated) returned 403; the developer docs above cover the same content.
9. Gateway counts for VGS, Basis Theory, Evervault and Skyflow: none published on their sites.
