# Poshmark (Naver) payments fact file

Research date: 23 Oct 2026. Scope: public facts only, for a token-vault deck aimed at Poshmark. Every claim carries a URL, a quote or data point, and a date. Items that could not be verified from a primary or reputable source are marked UNVERIFIED. Nothing about Yuno's product is included here.

Budget log: 30/30 WebSearch calls used (all "standard" mode, two of them domain-restricted to poshmark.com / support.poshmark.com / support.poshmark.ca). Primary sources fetched directly: poshmark.com live HTML (home, category feed, one listing page, posh_guide pages, offers_help, posh_protect, posh_authenticate, engineering), the Poshmark Legal Center (Ironclad-hosted, poshmark.com/privacy and the vault.pactsafe.io copy: Terms v4.6, Privacy Policy v8.2, Fee Policy v1.7, Canada Fee Policy v1.0, Buyer Policy v1.5, Posh Show Policy v1.4, Return Policy v1.2), support.poshmark.com raw HTML (Salesforce shell, CSP only), Naver IR (navercorp.com earnings-release page, 1Q26 and 2Q26 release PDFs, 2Q26 factsheet xlsx), PR Newswire (five Poshmark releases Aug 2025 to May 2026), blog.poshmark.com, Trustpilot, BBB, Have I Been Pwned, TechCrunch, Retail Dive, Value Added Resource, Edaily, Korea JoongAng Daily, Dealroom, Digital Commerce 360, PYMNTS. Prior internal note reused for leads only: /Users/germantatis/Desktop/GTMCoding/Events/Research/Poshmark/poshmark-stripe-sessions-research.md (21 Apr 2026); every number in it was re-verified or replaced below.

Legend: [PRIMARY] company filing, company site, legal center or official doc. [PRESS] reputable trade press. [SNIPPET] only seen in a search-result snippet, page not fetched (support.poshmark.com articles do not render outside a browser: Salesforce Experience Cloud plus a TLS chain that the fetch tool rejects). [UNVERIFIED] could not confirm.

---

## 1. Buyer payment stack today (Oct 2026)

### 1.1 Accepted methods by market (live feature flags, poshmark.com HTML fetched 23 Oct 2026) [PRIMARY]

Source: https://poshmark.com/ (3.49 MB HTML, server-rendered config JSON). The flags name the gateway per method: `bt` = Braintree, `ad` = Adyen, `af` = Affirm.

| Market | Flag (verbatim) | Reading |
|---|---|---|
| US | `"payment_methods__us":{"default":{"payment_methods":{"bt":{"venmo":{"enabled":true},"credit_card":{"enabled":true,"form_type":"std_cc"},"paypal":{"enabled":true},"apple_pay":{"enabled":true},"google_pay":{"enabled":true}},"ad":{"credit_card":{"enabled":false,"form_type":"std_cc"}},"af":{"affirm":{"enabled":true}}},"fvv_id":"payment_methods__us.base.002"}}` | US cards, PayPal, Venmo, Apple Pay, Google Pay all run through Braintree; Adyen card form exists but is disabled for US; Affirm enabled |
| Canada | `"payment_methods__ca":{"default":{"payment_methods":{"bt":{"paypal":{"enabled":true},"venmo":{"enabled":false}},"ad":{"credit_card":{"enabled":true,"form_type":"std_cc"},"apple_pay":{"enabled":true},"google_pay":{"enabled":true}},"af":{"affirm":{"enabled":false}}},"fvv_id":"payment_methods__ca.new.002"}}` | Canada cards, Apple Pay, Google Pay run through Adyen; PayPal through Braintree; no Venmo, no Affirm |
| Canada token switch | `"adyen_switch_new_payment_tokens__ca":{"default":{"enabled":true,"enabled_at":"2022-03-09T21:00:00","fvv_id":"adyen_switch_new_payment_tokens__ca.enabled.003"}}` | New Canadian payment tokens have been created on Adyen since 9 Mar 2022; a sibling flag `migration_payment_methods__ca` carries the same method map |
| PayPal Pay Later (US) | flag id `braintree_paypal_pay_later_visitor__us.enabled.003`; listing JSON: `"npb":[{"content_type":"paypal_pay_later","pay_later_options":{"message":"Pay in 4 interest-free payments of $12.50","info_tooltip_url":"https://www.paypal.com/credit-presentment/lander/modal?payer_id=FDJJJ2Y4U4EMY&offer=PAY_LATER_SHORT_TERM&amount=50"}}]` | PayPal Pay in 4 messaging is served through the Braintree/PayPal integration on a $50 listing (https://poshmark.com/listing/Lilly-Pulitzer-Inca-resort-dress-size-medium-6adb6011c5c2ed0e5f0f7b2e) |
| Gift cards (US) | `"app_account_settings_gift_cards__us":{"default":{"ios":{"enabled":true,"display_string":"Gift Cards","payment_provider":"tt","buy_url":"https://poshmark.cashstar.com/store/recipient?locale=en-us","bulk_buy_url":"https://totuscards.com/giftcards/poshmark"` | Gift cards are sold through CashStar (Blackhawk) storefronts; Canada uses `https://poshmarkca.cashstar.com` |
| Redeemable balance and credits | Posh Guide: "We require a payment method to complete an order" ... "if your order total is covered by your redeemable balance and credits, then your payment method will not be charged." https://poshmark.com/posh_guide/how_to_buy | Seller balance and Posh Credits can fully cover an order; a stored method is still mandatory |
| Stored methods page | "To view, add, or delete a stored payment method, head over to the Account Tab > My Payment Methods. Poshmark accepts all major credit cards, Apple Pay, Android Pay, PayPal, and Venmo." https://poshmark.com/posh_guide/how_to_change_payment_info | Guide text is stale ("Android Pay") but confirms card-on-file model |

Official support article "What payment methods does Poshmark accept?" (https://support.poshmark.com/s/article/284791087?language=en_US) could not be rendered. The April 2026 internal note listed US: cards, Apple Pay, Google Pay, PayPal, PayPal Pay Later, Venmo, Affirm, gift cards; Canada: cards, Apple Pay, Google Pay. That list is consistent with the flags above; the flags add PayPal for Canada and exclude Venmo and Affirm there. [SNIPPET] for the article, [PRIMARY] for the flags.

### 1.2 Processor evidence: script hosts and merchant IDs (poshmark.com HTML, 23 Oct 2026) [PRIMARY]

Content-Security-Policy served in the page (identical on home, category and listing pages):
- script-src includes: `*.adyen.com *.braintreegateway.com *.paypal.com *.affirm.com` plus `www.paypalobjects.com appleid.cdn-apple.com cdn.siftscience.com mpsnare.iesnare.com ci-mpsnare.iovation.com checkout.razorpay.com cdn.seel.com *.openai.com`
- connect-src includes: `*.braintreegateway.com *.braintree-api.com *.razorpay.com *.paypal.com *.affirm.com *.adyen.com ... *.paylution.com ... *.browser-intake-datadoghq.com *.logs.datadoghq.com *.naver.com *.navercorp.com ... log.seel.com api.seel.com ... api.greenhouse.io ... bulk-post-action-input-poshmark-prod.s3.us-west-2.amazonaws.com` and websocket origins `wss://*.agora.io wss://*.sd-rtn.com wss://*.naver.com`
- frame-ancestors: `https://poshmark.lightning.force.com` (Salesforce)

Hosts that do NOT appear anywhere in the three pages: `js.stripe.com`, `checkout.com`, `forter`, `riskified`, `signifyd`, `kount`, `cybersource`, `arkose`, `datadome`. (The only "forter" substring is the category "Comforters"; "Stripe" appears only in product titles and CSS.)

Merchant-ID flags (verbatim):
- `"braintree_mid__us":{"default":{"bt_mid":"poshmark_BT","bt_mid_promoted_posts":"Poshmark_USD7311","payment_processing_country_code":"us","apple_pay_merchant_id":"merchant.com.poshmark.poshmark",...,"google_pay_merchant_id_web":"17987362452414474640","fvv_id":"braintree_mid__us.braintree.003"}}`
- `"braintree_mid__ca":{"default":{"bt_mid":"Poshmark_CADUSD5931","bt_mid_promoted_posts":"Poshmark_USD5931","payment_processing_country_code":"us",...,"fvv_id":"braintree_mid__ca.braintree.004"}}` (note: the Canadian Braintree MID is flagged with processing country "us")
- `"adyen_mid__us":{"default":{"merchant_id":"APM_USDUSD5931","google_pay_merchant_id":"APM_USDUSD5931",...,"payment_processing_country_code":"us","threeds2_enabled":false,"ad_mid_promoted_posts":"APM_USDUSD7311","fvv_id":"adyen_mid__us.production.004"}}` with `"apple_pay_merchant_id":"merchant.com.adyen.poshmark"`
- `"adyen_mid__ca":{"default":{"merchant_id":"APM_CADCAD5931",...,"payment_processing_country_code":"ca","threeds2_enabled":false,"ad_mid_promoted_posts":"APM_CADCAD7311","fvv_id":"adyen_mid__ca.production.010"}}`
- `"web_braintree_version_upgrade":{"default":{"enabled":false,...},"T32":{"enabled":true,...}}` (an A/B test of a newer Braintree JS version is running for one cohort)
- Separate MIDs exist for "promoted posts" (seller advertising spend) on both gateways.

Reading (ours, not a company statement): two card acquirers are integrated and live in production, Braintree (PayPal) for the US and Adyen for Canada, with both MIDs present for each country; 3DS2 is switched off on both Adyen MIDs; Razorpay hosts remain in the CSP from the closed India marketplace. No orchestration vendor host is present.

Support site (https://support.poshmark.com, Salesforce Experience Cloud, raw HTML 419 KB): its CSP whitelists `https://www.paypal.com/sdk/js`, `https://checkoutshopper-live.adyen.com/`, `https://checkoutshopper-test.adyen.com/`, `https://pal-test.adyen.com`, `https://www.google.com/recaptcha/`, and `https://poshmark.my.salesforce-scrt.com` [PRIMARY]. Interpretation: the help site embeds Adyen Checkout and PayPal SDK components (likely for agent-assisted or form-based payment updates); not a company statement.

### 1.3 Stored-credential charges: offers, Buy Now, Bundles, Posh Shows (official wording)

| Flow | Verbatim | Source |
|---|---|---|
| Make an Offer | "Offers are Binding. To submit an offer, you must have a valid payment method and shipping address. If an offer is accepted, payment will be processed immediately." ... "If no action is taken 24 hours after an offer is submitted, it will expire." ... "If Buy Now is selected at any time, all offers will be cancelled." ... "Offer Sales Tax is Estimated. If applicable, sales tax is estimated based on the offer and may vary based on the final order price." | [PRIMARY] https://poshmark.com/offers_help (fetched 23 Oct 2026) |
| Terms 10(h) Payments | "Buyers may pay for Items only by using payment methods approved by Poshmark, and Poshmark will receive such payment from the Buyer on behalf of the Seller. By submitting payment information through Poshmark, you authorize Poshmark to securely store that information and charge you for any Items purchased along with all associated taxes, shipping, and other fees. Poshmark reserves the right to request additional information from Users for the purposes of completing any transactions, identity verification, fraud prevention, and any other regulatory and compliance purposes." | [PRIMARY] Terms of Service v4.6, "Effective June 3rd 2025", https://poshmark.com/terms |
| Terms 10(g) Purchases | "Poshmark may delay or cancel any purchase for purposes of fraud detection or to protect Users from other illegal or wrongful activities. All purchases are final with no returns, refunds, cancellations, or retractions allowed, except where (i) the Buyer cancels an order within three (3) hours of purchase; (ii) Poshmark cancels the purchase..." | [PRIMARY] same |
| Buyer Policy | "Once a Buyer selects the Buy Now option for a listing or a Buyer makes an offer to purchase items that is accepted by the Seller, it will be considered a purchase and a binding contract between the Buyer and Seller. Upon purchasing an item, a Buyer must remit payment to Poshmark for the Item, including any listed shipping or additional fees and applicable taxes" | [PRIMARY] Buyer Policy v1.5, "Effective November 25th 2024", Legal Center |
| Posh Shows (live auctions) | "All bids are final and binding. If you are the highest bidder when an auction concludes, your payment method will be charged for the winning bid amount, plus any shipping, taxes, or additional fees listed." ... "Bids entered and accepted prior to a loss of connection will be considered binding." ... "All Buy Now purchases in a Posh Show are final and binding." | [PRIMARY] Posh Show Policy v1.4, "Effective March 25th 2026", Legal Center |
| Posh Shows, failed charge | "In the event of payment failure, you can update your payment details from the Order Details page." Tip: "The seller can reauction this listing to another shopper, so be sure to update this information as soon as possible." ... "Posh Shows is currently available in the U.S. and Canada." | [PRIMARY] Poshmark blog, "Your Guide to Posh Shows", 5 Dec 2022, https://blog.poshmark.com/2022/12/05/posh-shows-shopper-hub/ |
| Bundles | Listing page UI strings "Buy Now", "Make an Offer", "Add To Bundle" present; support article "What is a Posh Bundle?" https://support.poshmark.com/s/article/124959465 not renderable | [PRIMARY] listing HTML for the buttons; [SNIPPET] for the article |

Note on fees to buyers: the listing JSON still carries the strings `"label":"Estimated Tax & Buyer Protection Fee"` and `"disclaimer":"Poshmark is required or may be otherwise obligated to collect sales tax in certain states. The Buyer Protection Fee includes Posh Protect, Posh Authenticate (if applicable), 24/7 customer support, and ongoing product improvements."` [PRIMARY, listing HTML]. The Fee Policy notice says the US Buyer Protection Fee was removed effective 24 Oct 2024 (see 2.3), so this looks like a legacy string or a Canada-specific line. Whether any buyer fee is charged today: UNVERIFIED.

### 1.4 Posh Protect, Posh Authenticate, Posh Remit (sales tax)

- Posh Protect [PRIMARY] https://poshmark.com/posh_protect : "We will give you a full refund if your item never ships or does not match the listing description. Otherwise, all sales are final and no refunds will be provided under Posh Protect." ... "If you've received your order as described, accept the order to release payment to the seller." ... "you have 72 hours after delivery (as determined by the tracking information on the shipping label) to open a return case" ... "If no return case is opened within 3 days of delivery, payment will be automatically released to the seller." ... "Posh Protect does not cover trades or transactions completed off of the Poshmark platform."
- Terms 11(a) [PRIMARY]: "RECEIVING A REFUND UNDER THE POSH PROTECT POLICY IS A BUYER'S SOLE REMEDY". The Terms do not use the word "chargeback".
- Return Policy v1.2, "Effective May 1st 2025" [PRIMARY]: return case "within seventy-two (72) hours from delivery" for "Undisclosed damage; Incorrect or missing item; Item not as described within the listing; or Item is not authentic."
- Posh Authenticate [PRIMARY] https://poshmark.com/posh_authenticate : "When you purchase an item from select luxury brands and categories priced at $500 or higher, your order will be sent to Poshmark and undergo our expert authentication process." ... "If authenticity cannot be confirmed, you will receive a full refund."
- Sales tax: Terms 10(i) [PRIMARY]: "Transactions conducted through the Service may be subject to taxes in your jurisdiction, which Poshmark will collect from Buyers on behalf of Sellers where legally obligated to do so." The program name "Posh Remit" and "no additional charge to sellers" appear only in third-party tax guides (zamp.com, keepertax.com, 2026) [SNIPPET].
- Seel: `cdn.seel.com`, `log.seel.com`, `api.seel.com` are whitelisted in the CSP [PRIMARY] and a support article titled "Seel Return Policy & FAQs" exists (https://support.poshmark.com/s/article/Seel-Return-Policy) [SNIPPET]. Whether Seel return assurance is sold at checkout today: UNVERIFIED.

### 1.5 Affirm (BNPL)

| Fact | Source |
|---|---|
| "Of Poshmark's 80 million users, eligible shoppers can now tap Affirm and choose between monthly payments or four interest-free payments every other week for merchandise exceeding $50." | [PRESS] PYMNTS, 13 Apr 2022, https://www.pymnts.com/?p=1282157 |
| John McDonald, Chief Operating Officer, Poshmark: "More than half of our available inventory is now eligible for Affirm's payment solutions, and we're seeing strong uptake of these options" | [PRESS] same |
| Two-year extension and expansion announced 12 Apr 2022 | [SNIPPET] Business Wire, https://www.businesswire.com/news/home/20220412005375/en/ (403 on fetch) |
| Affirm case study (13 Jul 2023): Adaptive Checkout delivers Pay in 4 and monthly in one flow; Poshmark lowered the floor to $50 | [SNIPPET] https://investors.affirm.com/node/11706/pdf (403 on fetch) |
| Affirm is enabled in the US flag and disabled in the Canada flag (see 1.1); listing page shows "Buy now, pay later" strings and `*.affirm.com` in the CSP | [PRIMARY] |

---

## 2. Seller payout stack

### 2.1 Redemption options and timing

| Item | Verbatim / value | Source |
|---|---|---|
| Hyperwallet | "Poshmark uses Hyperwallet payment services to deliver Instant Transfer, PayPal, and Venmo." | [PRIMARY] https://poshmark.com/posh_guide/how_to_get_paid (fetched 23 Oct 2026, footer "© 2026 Poshmark, Inc.") |
| Direct Deposit | "Enter your bank information and we will deposit your money directly in your account, typically within 2-3 business days." | [PRIMARY] same |
| Check | "Enter your address and we will mail you a check." | [PRIMARY] same |
| Instant Transfer | "Add a participating debit card and for a transfer fee, send your money directly to your account, typically within 30 minutes." ... "Eligible with most Visa and Mastercard debit cards. Prepaid and expired debit cards are not accepted." | [PRIMARY] same |
| PayPal / Venmo | "Log in and for a transfer fee, send money to your PayPal account." ... "Upon withdrawal from Venmo, funds are deposited into your bank in 1-3 business days." | [PRIMARY] same |
| Hyperwallet host | `*.paylution.com` (Hyperwallet's pay portal domain) is whitelisted in the poshmark.com CSP connect-src | [PRIMARY] poshmark.com HTML |
| Seller Policy wording | "Get paid Fast and flexible payout options like Direct Deposit, ACH, Instant Transfer, Paypal, and Venmo." | [PRIMARY] Seller Policy, Legal Center |
| US fee table | Instant Transfer $2 ("The $2 fee is deducted from your total redemption amount for each transfer"), PayPal and Venmo $0.35 each, Direct Deposit no fee 2-3 business days, check no fee about 2 weeks; "You must use your own PayPal account"; "only one Venmo account can be connected to your Poshmark account" | [SNIPPET] https://support.poshmark.com/s/article/redemption-options?language=en_US and https://support.poshmark.com/s/article/redeem-earnings-via-Venmo-and-PayPal?language=en_US |
| Canada fee table | "Visa Instant Transfer · Send money to your Visa debit card for C$2.00 · 30 mins or less"; PayPal "C$0.50 transfer fee will be deducted from your total redemption amount for each PayPal transfer"; direct deposit no fee, "normally take 1-3 business days"; no Venmo | [SNIPPET] https://support.poshmark.ca/s/article/redemption-options-CA and https://support.poshmark.ca/s/article/redeem-earnings-via-PayPal-CA |
| Funds release | Payment released to seller when buyer accepts or automatically 3 days after delivery (see 1.4) | [PRIMARY] posh_protect page |
| Unclaimed funds | Terms 10(m): "It is the User's sole responsibility to update payment Account Information to receive any redeemable funds." ... "Poshmark will escheat any unclaimed funds to the relevant government authorities as necessary" and "may charge a dormancy fee when such a fee is allowed by applicable rules and regulations." | [PRIMARY] Terms v4.6 |

### 2.2 How bank details are stored and protected

- Multi-factor flag in the live config [PRIMARY]: `"multi_factor_token":{"default":{...,"sms_enabled":true,"android":{"create_ach_details":true,"create_check_details":true,"invalid_ach_details":true,"remove_phone_number":true,"update_ach_details":true,"update_address_book":true,"update_check_details":true,"update_paypal_redemption_details":true,...` (same for ios and web). Reading: creating or updating ACH, check and PayPal redemption details is gated behind a second factor, and Poshmark holds ACH details itself ("create_ach_details"). Flag ids `paypal_redemption_details` and `venmo_redemption_details` also appear.
- Plaid: no `plaid` string in any fetched page or CSP. Bank verification method: UNVERIFIED (support snippet only says "The payout information must be valid and verifiable" and that the account name must match the legal name on the Poshmark account) [SNIPPET].
- Privacy Policy v8.2 [PRIMARY]: "When you buy and sell on Poshmark, we will need to collect payment and billing information, such as credit card and bank account information to complete the transaction." (see 6.1)

### 2.3 Seller fees and fee history

| Market | Verbatim | Source |
|---|---|---|
| US (current) | "It's always free to list an item for sale on Poshmark. For Sellers, after your item sells, we deduct a small fee from the final order price. For sales under $15, the fee is a flat rate of $2.95. For sales $15 and above, the fee is 20% and you keep 80%." | [PRIMARY] Fee Policy v1.7, "Effective November 25th 2024" (current as of 23 Oct 2026), Legal Center |
| US notice | "Our U.S. marketplace Fee Policy has changed, effective October 24, 2024, to revert to our original fee structure of 20% seller fee for sales over $15 and $2.95 for sales $15 and under, and remove the Buyer Protection Fee." | [PRIMARY] Fee Policy version "Effective October 24th 2024 to November 25th 2024" |
| US config | `"app_listing_fee__us":{"default":{"minimum_listing_price":0,"minimum_selling_price":3,"fee":{"minimum_fee":2.95,"commission":20}` | [PRIMARY] poshmark.com HTML |
| Canada (current) | "For all sales under C$20, Poshmark takes a flat commission of C$3.95. For sales of C$20 or more, you keep 80% of your sale and Poshmark's commission is 20%. All orders include a GST/HST on the Poshmark fee that is deducted from the seller's earnings. The GST/HST rate is dependent on the seller's Province." | [PRIMARY] Canada Fee Policy v1.0, "Effective December 18th 2023", Legal Center |
| Canada config | `"app_listing_fee__ca":{"default":{"minimum_listing_price":0,"minimum_selling_price":5,"fee":{"minimum_fee":3.95,"commission":20}` | [PRIMARY] poshmark.com HTML |
| Oct 2024 experiment | Sellers were "charged 5.99% of an order total, plus $1 for orders under $15" and "$2 for orders between $15 and $50; and $3 for orders $50 and over" from "Oct. 3"; "As of Oct. 24, however, the company will revert to its original policies." The new rules "were to be implemented in Canada at a future date." Manish Chandra: "The outcome of the change did not meet our expectations and I sincerely apologize" | [PRESS] Retail Dive, 22 Oct 2024, https://www.retaildive.com/news/poshmark-scraps-new-fees-after-seller-outcry-sales-hit/730484 |
| 2025 to 2026 fee changes | None: Fee Policy v1.7 (Nov 2024) is still the current version; Canada v1.0 (Dec 2023) unchanged. Shipping-fee changes only (flat-rate label $8.27 to $6.49 in Sep 2025; Purolator option in Canada from 15 Apr 2025) | [PRIMARY] Legal Center version list; [SNIPPET] third-party shipping guides for the 2025 shipping changes |

---

## 3. Scale and markets

### 3.1 Naver reporting (Poshmark sits in Naver's "Global Opportunities > C2C" line; latest reported quarter = 2Q26; 3Q26 not reported as of 23 Oct 2026)

| Metric | Value | Source |
|---|---|---|
| Segment definition | "C2C Kream/Soda, Poshmark, Wallapop" | [PRIMARY] Naver 1Q26 Earnings Release PDF, https://www.navercorp.com/api/article/download/896dc2b0-33ea-4dbf-a354-c9608c6d989b |
| C2C revenue, quarterly (bn KRW) | 1Q23 146.2, 2Q23 152.4, 3Q23 155.8, 4Q23 163.6, 1Q24 213.7, 2Q24 203.8, 3Q24 194.4, 4Q24 214.0, 1Q25 222.7, 2Q25 227.5, 3Q25 250.6, 4Q25 285.7, 1Q26 351.1, 2Q26 397.9 | [PRIMARY] Naver 2Q26 factsheet xlsx, sheet "Consolidated IS", https://www.navercorp.com/api/article/download/b82b086d-2b0f-4f5b-932f-c41fb93433e1 |
| C2C 2Q26 | 397.9 bn KRW, "Y/Y 74.9%, Q/Q 13.3%"; "Excluding effects of Wallapop, c2c grew YoY 52.1%, QoQ 9.8%" | [PRIMARY] Naver 2Q26 Earnings Release PDF, https://www.navercorp.com/api/article/download/07b3b329-bbbe-481c-ac47-b3d0d7fea855 |
| Poshmark commentary 2Q26 | "[C2C] Poshmark growth accelerated helped by service and organization revamp; Soda growth led by trading cards" | [PRIMARY] same |
| C2C 1Q26 | 351.1 bn KRW, "57.7%" YoY, "22.9%" QoQ; "Excl. consolidation of Wallapop, C2C YoY 41.6%, QoQ 10.3%" | [PRIMARY] 1Q26 release |
| Poshmark commentary 1Q26 | "[C2C] Wallapop consolidated in 1Q26. GMV and revenue acceleration at Poshmark going through rebuilding as well as robust growth at Soda led to strong growth" | [PRIMARY] same |
| Global Opportunities 2Q26 | 1,015.9 bn KRW, +24.4% YoY, +7.9% QoQ | [PRIMARY] 2Q26 release |
| Naver group 2Q26 | Revenue 3,388.8 bn KRW (+16.2%), operating profit 520.3 bn KRW (-0.2%), net profit 704.3 bn KRW | [PRIMARY] 2Q26 release; [PRESS] Edaily, 7 Aug 2026, https://en.edaily.co.kr/news/eda202608075217/ |
| Poshmark revenue growth 2Q26 (call) | "Poshmark recorded revenue growth of over 40% year-over-year in the second quarter" ... "Poshmark saw the benefits of improvements in the quality of its AI-based search and recommendations." | [PRESS] Edaily, 7 Aug 2026 (conference-call coverage) |
| Alternate press figure | "Its global commerce platforms, such as Poshmark and Wallapop, saw sales rise 24.4 percent to 1.16 trillion won." (growth rate matches the release; the 1.16 tn figure does not match the 1,015.9 bn in the release) | [PRESS] Korea JoongAng Daily, 7 Aug 2026, https://www.koreajoongangdaily.com/business/navers-net-profit-leaps-nearly-42-in-q2-to-495-million/12813879 |
| Q1 2026 press | Naver's C2C business "grew Q1 2026 revenue 57.7% year-over-year on the consolidation of Wallapop" and "growth at Poshmark, Kream, and Japanese subsidiary SODA" | [PRESS] Dealroom, 4 Aug 2026, https://dealroom.co/news/142869-naver-adds-109-5m-to-kream-as-resale-platform-diversifies-beyond-sneaker/ |
| Poshmark standalone GMV / revenue | Not disclosed by Naver in the 1Q26 or 2Q26 releases or factsheet. ECDB estimate "approximately $1.9 billion in GMV in 2025" is a third-party estimate quoted by Seoulz (27 May 2026) | [UNVERIFIED] https://www.seoulz.com/naver-recommerce-empire-2026/ |
| 3Q26 results | Not published: the Naver IR earnings page lists only "1Q 2026" and "2Q 2026" releases as of 23 Oct 2026 | [PRIMARY] https://www.navercorp.com/en/investment/earningsRelease |

### 3.2 Poshmark's own public numbers

| Metric | Value | Source |
|---|---|---|
| Members | "Powered by a vibrant community of 165 million members" | [PRIMARY] PR Newswire, 27 May 2026, https://www.prnewswire.com/news-releases/poshmark-partners-with-loren-to-release-new-song-during-exclusive-closet-drop-and-interactive-live-shopping-experience-302783822.html ; same "165 million members" in the 25 Mar 2026 release |
| Members (prior boilerplate) | "over 150 million users" and "over $10 billion in GMV" since founding in 2011 | [PRIMARY] PR Newswire, 11 Aug 2025, 27 Oct 2025 and 15 Dec 2025 releases (URLs in section 4) |
| Lifetime GMV | "over $10 billion in GMV" (cumulative, not annual) | [PRIMARY] same |
| Live listings | "over 200 million live listings" | [UNVERIFIED] Seoulz, unattributed |
| Active buyers | Not disclosed since the 2023 take-private | [UNVERIFIED] |
| Acquisition | Naver acquired Poshmark for $1.2 billion in cash; closed January 2023 | [PRESS] TechCrunch, 3 Oct 2022, https://techcrunch.com/2022/10/03/naver-agrees-to-acquire-fashion-marketplace-poshmark-for-1-2b/ ; PR Newswire completion release https://www.prnewswire.com/news-releases/naver-completes-acquisition-of-poshmark-301714299.html (from prior note, not re-fetched) |

### 3.3 Markets live today

- US and Canada only. "rolling out to all users in the U.S. and Canada starting March 25, 2026" [PRIMARY] PR Newswire, 25 Mar 2026, https://www.prnewswire.com/news-releases/poshmark-unveils-redesigned-app-ushering-in-new-chapter-of-style-discovery-302724193.html ; "Posh Shows is currently available in the U.S. and Canada." [PRIMARY] blog, Dec 2022. Live config carries only `__us` and `__ca` payment flags [PRIMARY].
- UK, Australia, India closed: "The closures take effect October 26, 2023"; Chandra: "I'm sad to share that we've made the tough decision to close three of our expansion marketplaces"; FAQ: "to focus on and increase our investments in our core markets of the U.S. and Canada"; "Beginning November 2, 2023, buyers and sellers for India, Australia, and the UK will no longer have access"; "We hope to be back at some point in the future." [PRESS] Value Added Resource, 19 Oct 2023, https://www.valueaddedresource.net/poshmark-closes-uk-australia-india-marketplaces/
- Residue: the current Terms still name "Poshmark PTY LTD" (Australia) and "Poshmark India Marketplace Online Limited" as contracting entities, and Razorpay hosts remain in the CSP [PRIMARY].
- Japan, Korea, cross-border with Kream or Naver Shopping, "Poshmark Japan": no launch found. Naver, 4 Aug 2026: 130 bn KRW injection into Kream; "Kream plans to further strengthen service integration with these overseas platforms" (Wallapop, Poshmark, SODA named) [PRESS] Edaily, https://en.edaily.co.kr/news/eda202608045949/ . Seoulz claims Naver stated "Carousell, Wallapop, and Poshmark will eventually plug into a shared cross-listing infrastructure" [UNVERIFIED]. Status of any Poshmark launch outside US/CA: UNVERIFIED (none found).

### 3.4 2025 to 2026 news

| Date | Item | Source |
|---|---|---|
| 11 Aug 2025 | CEO transition: Namsun Kim (Executive Chairman since April 2025; Naver "President of Investments"; "previously served three years as Naver's CFO") becomes CEO effective 1 Oct 2025; Manish Chandra moves "to a strategic role on the company's Board of Directors" | [PRIMARY] https://www.prnewswire.com/news-releases/poshmark-inc-announces-chief-executive-officer-transition-302525526.html |
| 27 Oct 2025 | First Chief Product Officer, Heather Friedland; Kim: "We're entering an exciting new chapter as AI redefines how people shop, sell, and connect." | [PRIMARY] https://www.prnewswire.com/news-releases/poshmark-inc-appoints-first-chief-product-officer-302594726.html |
| 10 Nov 2025 | Deb Liu appointed to the Board | [PRIMARY] https://www.prnewswire.com/news-releases/poshmark-inc-appoints-deb-liu-to-board-of-directors-302609593.html (title only) |
| 15 Dec 2025 | First Chief Revenue Officer, Elizabeth von der Goltz (ex-Farfetch, Browns, Matches), starts January 2026 | [PRIMARY] https://www.prnewswire.com/news-releases/poshmark-inc-appoints-first-chief-revenue-officer-302637317.html |
| 25 Mar 2026 | Redesigned app (Guided Discovery, For You page, centralized Seller Tools, 3:4 imagery); Privacy Policy v8.2 and Posh Show Policy v1.4 both effective the same day | [PRIMARY] PR Newswire release above; Legal Center |
| 27 May 2026 | LØREN closet drop with "two exclusive Posh LIVE shopping events" hosted from Poshmark HQ | [PRIMARY] PR Newswire release above |
| Jun to Sep 2026 | Seller tools: Smart List AI upgrade (reads photos and tags to identify "brand, category, material, size, condition and color", writes title and description, suggests price), Sourcing Insights (rolled out June), Show Analytics Dashboard and bulk upload for Posh Shows, "Seller Hub" previewed July | [PRESS] Value Added Resource, 4 Sep 2026 (updated 17 Sep 2026), https://www.valueaddedresource.net/poshmark-seller-tools-updates/ |
| 2025 | Posh Lens visual search "leverages visual search technology from Poshmark owner Naver" | [SNIPPET] Adweek / Retail TouchPoints, 2025 |
| 2026 | Layoffs or restructuring: none found in press; Naver's own wording is "service and organization revamp" (2Q26) and "going through rebuilding" (1Q26) [PRIMARY]. Last reported layoff: about 2% of staff in Feb 2023 [PRESS] https://www.retaildive.com/news/poshmark-layoffs-two-percent-workforce/643617 | |
| 2026 tax | Federal 1099-K threshold for 2026 reported as more than $20,000 and more than 200 transactions (state thresholds lower) | [SNIPPET] third-party tax guides; Poshmark's own 1099-K page not fetched. UNVERIFIED on Poshmark's page |

---

## 4. Leadership and payments owners

| Name | Title | Evidence | Status |
|---|---|---|---|
| Namsun Kim | Chief Executive Officer (since 1 Oct 2025); ex Naver President of Investments and Naver CFO | [PRIMARY] PR Newswire 11 Aug 2025; quoted as CEO in Oct and Dec 2025 releases | Confirmed |
| Manish Chandra | Co-founder, Board member (ex-CEO) | [PRIMARY] same | Confirmed |
| Heather Friedland | Chief Product Officer (ex-CPO Ancestry, VP Product eBay) | [PRIMARY] PR Newswire 27 Oct 2025; quoted 25 Mar and 27 May 2026 | Confirmed |
| Elizabeth von der Goltz | Chief Revenue Officer (since Jan 2026) | [PRIMARY] PR Newswire 15 Dec 2025; quoted 25 Mar 2026 | Confirmed |
| Gautam Golwala | CTO, co-founder | [PRIMARY] https://poshmark.com/engineering (live page, fetched 23 Oct 2026): "By Gautam Golwala, CTO of Poshmark" | Listed on live site; tenure not re-confirmed elsewhere |
| Chetan Pungaliya | VP of Engineering | [PRIMARY] same page: "By Chetan Pungaliya, VP of Engineering at Poshmark" | Listed on live site |
| "Kalpak" (surname not shown) | VP, Platform Engineering | [PRIMARY] same page: "I just launched a social negotiation system where I incorporated complex payment authorization into peer-to-peer communication flow. This gave me the opportunity to dig deeper into how payments work in social and mobile commerce." | Surname UNVERIFIED |
| Rodrigo Brumana | CFO Dec 2021 to May 2025; appointed CFO of Joby Aviation 7 May 2025 (start 29 May 2025) | [SNIPPET] Joby 8-K coverage (tipranks), marketscreener profile "Chief Financial Officer from 2021 to 2025" | Departed |
| CFO today | No appointment release or profile found in three searches | [UNVERIFIED] | Vacant or unannounced |
| John McDonald | Chief Operating Officer (quoted Apr 2022) | [PRESS] PYMNTS 13 Apr 2022 | Current status UNVERIFIED |
| Robbie Fritts | "Senior Director Operations, Fraud and Payments"; profile text: leads an organization of about 40 covering fraud, payments, payments compliance (PCI mentioned) | [SNIPPET] anymailfinder.com directory (page returned HTTP 410 on fetch) | UNVERIFIED |
| Risk team (role) | "Staff Risk Strategy Analyst", Redwood City, "137K-194K Annually", removed 8 Sep 2026: "buyer fraud, seller abuse, account integrity, payment fraud, refund and return abuse, spam, and trust & safety domains"; "This role will leverage internal and external risk platforms, data tools, and orchestration capabilities"; partners with "Product, Engineering, Trust & Safety Operations, Payments, Customer Experience, and Analytics teams" | [PRIMARY job post] https://www.builtinsf.com/job/staff-risk-strategy-analyst/10248353 | Confirms a Payments team and a risk-orchestration layer exist |
| Security roles | "Software Engineer, SOC" (Redwood City): "automated security detection, incident response playbooks, and SOC tooling"; Application Security Engineer and Senior Security Engineer, Infrastructure Security (Chennai) | [SNIPPET] startup.jobs, teamlease.com | Chennai engineering hub indicated |
| Payments-titled leaders on LinkedIn | Searches for "Poshmark" with head of payments / payments lead / fraud / risk returned no additional named profiles | [UNVERIFIED] | |

Greenhouse board: poshmark.com CSP whitelists `api.greenhouse.io`, but `boards-api.greenhouse.io/v1/boards/poshmark/jobs` returned zero jobs (board slug differs or board is private) [PRIMARY, negative result].

---

## 5. Payment pain signals

### 5.1 Review platforms (fetched 23 Oct 2026)

| Source | Metric | Quotes (verbatim, dated) |
|---|---|---|
| Trustpilot https://www.trustpilot.com/review/poshmark.com | TrustScore 1.2 of 5 ("Bad"), 5,175 reviews, 86% one-star | 11 Oct 2026: "my card information and verification codes were used to initiate an unauthorized $2,000 transaction." ; 1 Oct 2026: "taking money out of your account without your approval in the name of promoting your listing" ; 28 Sep 2026: "I have a $50 balance and it showing zero. I want my money now." ; 11 Sep 2026: "i withdrawed a total of $120 and STILL HAVENT RECEIVED IT!" ; 15 Oct 2026: "Despite providing this evidence, Poshmark refused to refund me." [PRESS, consumer reviews] |
| BBB https://www.bbb.org/us/ca/redwood-city/profile/consignment-clothes/poshmarkcom-1116-442251/complaints | Rating B, not accredited; 3,548 complaints filed in last 3 years, 1,500 in last 12 months (3,089 "Answered", 459 "Resolved") | 11 Oct 2026: "poshmark charged me multiple times for both items." (duplicate charges on a debit card) ; 10 Oct 2026: "I now have a charge of 1305 on my Apple Pay." (pending after a failed order) ; 9 Oct 2026: "the $1,960 is STILL not in my bank account." (direct deposit) ; 9 Oct 2026: "I was promised a payout of money I earned before the end of September." ; 12 Oct 2026: "wrongfully withholding my seller earnings." [PRESS, consumer complaints] |
| Older note (Apr 2026) | Trustpilot 1.3 stars / 2,800+ reviews; PissedConsumer 9,400+ reviews | Superseded by the numbers above; PissedConsumer not re-fetched [UNVERIFIED] |

Themes observable in the Oct 2026 samples: duplicate card charges, pending Apple Pay authorizations after failed orders, account takeover with stored-card misuse, delayed or missing payouts, withheld seller earnings during return disputes, promoted-closet (ad) charges contested. App-store review themes for 2026 were not fetched (budget): UNVERIFIED.

### 5.2 Data breach (2018, disclosed 2019)

| Fact | Source |
|---|---|
| "Clothing marketplace Poshmark confirms data breach", 1 Aug 2019: "user profile information, including names and usernames, gender and city data was taken by an 'unauthorized third party.'" Email addresses, size preferences, scrambled passwords and notification settings also taken; "Poshmark said it used the bcrypt hashing algorithm to scramble the passwords"; "retained outside forensics firm Kroll"; "Financial data and physical address information was not compromised, the company said." | [PRESS] TechCrunch, https://techcrunch.com/2019/08/01/poshmark-confirms-data-breach |
| Breach date "May 2018"; added to HIBP "2 Sep 2019"; "36.4M" accounts; data: email addresses, genders, geographic locations, names, passwords, usernames; "In mid-2018, social commerce marketplace Poshmark suffered a data breach that exposed 36M user accounts." | [PRIMARY] https://haveibeenpwned.com/breach/Poshmark |
| US users affected, not Canadian (per Retail Dive coverage) | [SNIPPET] https://retaildive.com/news/poshmark-hit-by-data-breach/560220 |
| Any later PCI or card-data incident | None found | [UNVERIFIED] |

### 5.3 Policy anchors behind disputes
- Buyer cancel window: 3 hours after purchase (Terms 10(g)); return case: 72 hours after delivery; payment auto-released to seller after 3 days (posh_protect page); Posh Protect refund is "A BUYER'S SOLE REMEDY" (Terms 11(a)); Posh Show bids and Buy Now purchases "final and binding" (Posh Show Policy v1.4). All [PRIMARY].

---

## 6. Compliance and tech

### 6.1 Privacy Policy and Terms on payment data [PRIMARY] (Legal Center, https://poshmark.com/privacy ; Ironclad-hosted, mirror at https://vault.pactsafe.io/s/c4be733d-0a0a-4da6-9352-575559a32728/legal.html)

- Version: "Privacy Policy Version 8.2 (Current)" ... "Effective March 25th 2026" ... "Last Updated: March 24, 2026". Scope: "personal data Poshmark, Inc. and our subsidiaries and affiliates (collectively 'Poshmark', 'we', 'us', and 'our') obtain". The word "Naver" does not appear in any current policy (0 hits across the legal center).
- Collection: "When you buy and sell on Poshmark, we will need to collect payment and billing information, such as credit card and bank account information to complete the transaction."
- Sharing: "Provide the Services: We will share your information with companies that provide a service to us or our users, such as shipping or delivery, returns, identity verification, fraud monitoring, payment processing, storage, database maintenance, analytics, and hosting. For example, we may use Google Maps API to help autocomplete and validate your address."
- Security: safeguards "may include facilities access restrictions, system access controls, firewalls, data encryption, and other security best practices. No internet, email, or other electronic transmission is ever fully secure or error free" ... "Your information may be stored with third-party cloud service infrastructure providers." ... "We are headquartered in the United States and may share your information with service providers and other recipients in the United States and worldwide."
- No processor is named anywhere in the Privacy Policy, Terms, Seller Policy or Fee Policies (0 hits for Braintree, PayPal, Adyen, Stripe, Hyperwallet, Affirm, Venmo, Plaid, Sift in the policy text; the words "PayPal" and "Venmo" appear only in the Seller Policy payout list quoted in 2.1). The Terms refer to "Poshmark's permitted third-party payment provider(s)".
- Legal center platform: flag `web_ironclad_legal_contracts.enabled.001` and pactsafe.io assets [PRIMARY].

### 6.2 PCI, SOC, tokenization statements
- No public PCI DSS or SOC 2 statement by Poshmark was found (search across job posts and site). The only PCI mention is in the unverified Fritts profile (payments compliance). [UNVERIFIED]
- Tokenization evidence is indirect: Canada "new payment tokens" switched to Adyen in Mar 2022 (flag in 1.1); Terms authorize Poshmark to "securely store" payment information; `threeds2_enabled:false` on both Adyen MIDs [PRIMARY]. No network-token or account-updater statement found [UNVERIFIED].
- Engineering blog (https://poshmark.com/engineering, live): links two 2014/2016 posts by the CTO and VP Engineering on real-time commerce and back-end techniques, plus an AWS case study link (https://aws.amazon.com/solutions/case-studies/poshmark/ , which now resolves to a generic AWS page; content UNVERIFIED). No post on payments, tokenization or microservices.

### 6.3 Observed technology vendors (poshmark.com CSP and config, 23 Oct 2026) [PRIMARY]
| Function | Hosts / flags |
|---|---|
| Card acquiring and wallets | `*.braintreegateway.com`, `*.braintree-api.com`, `*.paypal.com`, `www.paypalobjects.com`, `*.adyen.com`; Apple Pay merchant ids `merchant.com.poshmark.poshmark` (Braintree) and `merchant.com.adyen.poshmark` (Adyen); Google Pay merchant id `17987362452414474640` |
| BNPL | `*.affirm.com`; PayPal Pay Later via Braintree |
| Payouts | `*.paylution.com` (Hyperwallet) |
| Fraud and bot defense | `cdn.siftscience.com` (Sift; flag `sift_decisions_for_chat_block`), `mpsnare.iesnare.com` and `ci-mpsnare.iovation.com` (TransUnion iovation device intelligence), `app_recaptcha_v2_enterprise` enabled on iOS, Android and web |
| Legacy India | `*.razorpay.com`, `checkout.razorpay.com` |
| Live shopping | `*.agora.io`, `*.sd-rtn.com` (Agora real-time video) |
| AI | `*.openai.com` |
| Naver | `*.naver.com`, `*.navercorp.com`, `*.naver.net` (websocket and connect origins) |
| Cloud and observability | S3 buckets `bulk-post-action-*-poshmark-prod.s3.us-west-2.amazonaws.com` (AWS us-west-2), `*.browser-intake-datadoghq.com`, `*.logs.datadoghq.com`, `*.fullstory.com`, `*.clarity.ms` |
| CRM, support, marketing | `poshmark.lightning.force.com` and `poshmark.my.salesforce-scrt.com` (Salesforce), `*.moengage.com`, `api.greenhouse.io`, `cdn.seel.com` (Seel) |

---

## 7. Competitive context in resale (one line each, context only)

| Company | Payment provider (public) | Source |
|---|---|---|
| Depop (Etsy) | "Depop Payments" is "powered by Stripe Connect"; buyers can use Apple Pay, Google Pay, cards and PayPal | [SNIPPET] Depop blog, https://blog.depop.com/articles/depop-payments-more-ways-to-get-paid (JS page, not renderable) |
| Mercari US | Still operating: US GMV "$602 million, up 10.0% year over year" for the nine months to 31 Mar 2026; a separate "standalone Mercari Japan app in the U.S." launched June 2026 ("supports U.S. dollar payments through domestic payment services"); US processor not named | [PRESS] Digital Commerce 360, 19 Jun 2026, https://www.digitalcommerce360.com/2026/06/19/mercari-launches-us-app/ ; processor UNVERIFIED |
| Vinted | Extended Mangopay as PSP across Europe (announced 21 May 2026) "working closely with Vinted's own in-house payment service provider, Vinted Pay" | [PRESS] https://mangopay.com/press-and-media/mangopay-extends-long-standing-payments-partnership-with-vinted |
| eBay | Signed Adyen "to become its primary payments processing partner" (announced 31 Jan 2018); PayPal kept as a checkout option | [SNIPPET] eBay Inc. news, https://www.ebayinc.com/stories/news/13118 ; Retail TouchPoints 1 Feb 2018 |
| ThredUp | 10-K says card data goes to "third-party payment processors" (unnamed); payment processing fees $8.1M in 2021 | [SNIPPET] SEC 10-K FY2022 / FY2021 (EDGAR blocked non-browser fetch) |
| The RealReal | Processor not named in 10-K snippets (FY2019 to FY2025) | [UNVERIFIED] |

---

## Takeaways for a vault pitch (facts only)

- Cards are stored first and charged later: an offer requires "a valid payment method" and "If an offer is accepted, payment will be processed immediately"; in Posh Shows "your payment method will be charged for the winning bid amount"; the Terms authorize Poshmark "to securely store that information and charge you for any Items purchased". (Sections 1.3)
- Two acquirers hold those stored credentials by market: Braintree for US cards, PayPal, Venmo and wallets; Adyen for Canadian cards and wallets, with Canadian "new payment tokens" on Adyen since 9 Mar 2022. Both MIDs exist in both countries; the Adyen US card form is disabled. No orchestration vendor host is present. (1.1, 1.2)
- Payouts run on a third rail: Hyperwallet (PayPal) for Instant Transfer, PayPal and Venmo, plus Poshmark-held ACH and check details gated by a second factor; fees $2 / $0.35 (US) and C$2 / C$0.50 (Canada). (2.1, 2.2)
- Fraud tooling observed: Sift, iovation device intelligence, reCAPTCHA Enterprise; 3DS2 is off on both Adyen MIDs; a 2026 risk role cites "internal and external risk platforms, data tools, and orchestration capabilities". (1.2, 4, 6.3)
- Scale is reported only inside Naver's C2C line: 397.9 bn KRW in 2Q26 (+74.9% YoY, +52.1% excluding Wallapop); Naver's call attributed "over 40%" YoY revenue growth to Poshmark; Poshmark cites 165 million members; markets are US and Canada only. (3.1, 3.2, 3.3)
- Live complaint themes in Oct 2026 include duplicate card charges, a $1,305 Apple Pay authorization left pending after a failed order, stored-card misuse after account takeover, and missing payouts; BBB logged 1,500 complaints in 12 months. (5.1)
- Privacy Policy v8.2 (25 Mar 2026) discloses sharing payment data with unnamed "payment processing" providers and storage with "third-party cloud service infrastructure providers"; the 2018 breach excluded financial data; no PCI or SOC statement is public. (5.2, 6.1, 6.2)
- Leadership is new and Naver-appointed: CEO since Oct 2025 (ex Naver CFO), first CPO and CRO in late 2025, CFO seat unconfirmed since May 2025; Naver describes Poshmark as "going through rebuilding" and a "service and organization revamp". (3.1, 4)

Budget log: 30/30 WebSearch calls used; 0 remaining.
