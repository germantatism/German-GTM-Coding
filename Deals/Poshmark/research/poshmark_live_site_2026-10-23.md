# Poshmark live site evidence (poshmark.com web bundle)

Read 23 Oct 2026 by fetching https://poshmark.com/ and https://poshmark.com/category/Women with curl (desktop Chrome user agent). The homepage HTML embeds a feature-flag configuration (214 flags, keys ending in `__us` / `__ca`, each with `fvv_id` variant ids) plus Content Security Policy allowlists. Everything below is quoted from that HTML. Public, so it can be cited on a slide as "poshmark.com web bundle, read 23 Oct 2026". Nothing here comes from Yuno's calls with Poshmark.

## 1. Processors and merchant accounts

| Key | Value (verbatim) | Reading |
|---|---|---|
| `braintree_mid__us` | `"bt_mid":"poshmark_BT","bt_mid_promoted_posts":"Poshmark_USD7311","payment_processing_country_code":"us","apple_pay_merchant_id":"merchant.com.poshmark.poshmark","google_pay_merchant_id":"17987362452414474640"` | Braintree (PayPal) merchant account for the US, a second MID for Promoted Posts (seller ads), Apple Pay and Google Pay through Braintree |
| `braintree_mid__ca` | `"bt_mid":"Poshmark_CADUSD5931","bt_mid_promoted_posts":"Poshmark_USD5931","payment_processing_country_code":"us"` | Braintree account for Canada, processed as a US entity |
| `adyen_mid__us` | `"merchant_id":"APM_USDUSD5931","apple_pay_merchant_id":"merchant.com.adyen.poshmark","apple_pay_merchant_id_web":"000000000295332","payment_processing_country_code":"us","threeds2_enabled":false,"ad_mid_promoted_posts":"APM_USDUSD7311"` | Adyen merchant account for the US; Apple Pay also registered through Adyen; 3DS2 switched off; separate Promoted Posts MID |
| `adyen_mid__ca` | `"merchant_id":"APM_CADCAD5931","apple_pay_merchant_id_web":"000000000204762","payment_processing_country_code":"ca","threeds2_enabled":false,"ad_mid_promoted_posts":"APM_CADCAD7311"` | Adyen merchant account for Canada |
| `adyen_switch_new_payment_tokens__ca` | `{"enabled":true,"enabled_at":"2022-03-09T21:00:00"}` | New Canadian payment tokens have been created on Adyen since 9 Mar 2022. No `__us` counterpart appears in the web bundle |
| `migration_payment_methods__ca` | `bt: paypal enabled, venmo disabled; ad: credit_card (std_cc), apple_pay, google_pay enabled; af: affirm disabled` | Canada migration map: cards and wallets on Adyen, PayPal on Braintree |
| `payment_methods__us` | `bt: venmo, credit_card (std_cc), paypal, apple_pay, google_pay enabled; ad: credit_card enabled:false; af: affirm enabled` | US web checkout: cards, wallets, PayPal and Venmo on Braintree; Affirm direct; Adyen cards off on web (the apps may differ) |
| `payment_methods__ca` | `bt: paypal enabled, venmo disabled; ad: credit_card, apple_pay, google_pay enabled; af: affirm disabled` | Canada web checkout: cards and wallets on Adyen, PayPal on Braintree |
| `web_braintree_version_upgrade` | `default enabled:false; T23 enabled:true` | Braintree SDK upgrade under test |
| `multi_factor_token` | present | MFA settings, not payments |

Conclusion for the deck: Poshmark runs two card processors with their own vaults, Braintree and Adyen, with merchant accounts for both in the US and Canada. Which processor stores a given buyer's card depends on country, channel and when the card was saved.

## 2. Third-party hosts in the Content Security Policy (`web_auth_csp__us`, `web_order_and_offers_csp__us`, `web_csp__ca`)

Script and connect allowlists include: `*.adyen.com`, `*.braintreegateway.com`, `*.braintree-api.com`, `*.paypal.com`, `www.paypalobjects.com`, `*.affirm.com`, `*.razorpay.com`, `checkout.razorpay.com`, `cdn.siftscience.com`, `*.paylution.com` (Hyperwallet's platform domain), `*.naver.net`, `*.naver.com`, `*.navercorp.com`, `*.browser-intake-datadoghq.com`, `*.fullstory.com`, `appleid.cdn-apple.com`. Frame ancestors include `poshmark.lightning.force.com` (Salesforce).

Reading: Razorpay remains allowlisted from the Indian marketplace closed in 2023. Sift is the fraud engine (also referenced by the order-chat flag below). Paylution is Hyperwallet, the seller payout provider.

## 3. Fraud and risk

| Key | Value (verbatim) |
|---|---|
| `order_chat__ca` | `"sift_decisions_for_chat_block":["high_risky_payment_abuse"]`, `"order_cancellation_reasons_for_chat_block":["FRAUD_ATO","FRAUD_CCF","ACCIDENTAL_PURCHASE"]` |

Reading: Sift decisions drive chat blocking; cancellation reasons distinguish account takeover (ATO) and credit-card fraud (CCF).

## 4. Fees, tax and buyer protection

| Key | Value (verbatim) |
|---|---|
| `app_listing_fee__us` | `"minimum_selling_price":3,"fee":{"minimum_fee":2.95,"commission":20}` |
| `app_listing_fee__ca` | `"minimum_selling_price":5,"fee":{"minimum_fee":3.95,"commission":20}` |
| `processing_fee__us` / `__ca` | `"enabled":false` (web default) |
| `buyer_protection_fee_display_info` | labels "Tax & Buyer Protection Fee", list items "Tax" (`buyer_sales_tax_amount`) and "Buyer Protection Fee" (`processing_fee_amount`); disclaimer: "The Buyer Protection Fee includes Posh Protect, Posh Authenticate (if applicable), 24/7 customer support, and ongoing product improvements."; an `offer_checkout` variant reads "Estimated Tax & Buyer Protection Fee" |
| `web_sales_tax_rebate_label` | "Seller 50/50 Tax Discount" |
| `seller_tax_discount__us` | disabled, 17 states listed |

## 5. Seller payouts and tax

| Key | Value (verbatim) |
|---|---|
| permissions block | `"create_instant_transfer_redemption_details":true,"update_instant_transfer_redemption_details":true`, alongside `update_venmo_redemption_details` and PayPal redemption details |
| `redemptions_bank_validation__us` | `"enabled":true` |
| `check_redemption_switch__us` | `"check_redemption_enabled":true`; `__ca` false |
| `app_seller_tax_info__us` | web and app enabled |
| `download_tax_documents__us` | variant G enabled |
| `redeemable_activity_page` | enabled, thresholds 60 / 30 / 10 |

Reading: sellers redeem balances by direct deposit (bank validation on), Instant Transfer, PayPal, Venmo and, in the US, check; tax identity is collected in-app.

## 6. Markets and legacy flags

`web_pre_uk_banner` disabled, `australia_post_package_configuration` present, Razorpay allowlisted: remnants of the UK, Australia and India marketplaces closed in October 2023. Live country switches in the bundle are `__us` and `__ca` only.

## 7. Posh Shows and offers

Flags present: `app_shows_search` (enabled on iOS, Android, web), `app_bundle_seller_offers`, `app_buyer_offer_suggestions_v2`, `offer_to_likers__us`, `app_offer_to_likers_seller_shipping_discounts`, `offer_conversion_reporting_value_multiplier`. These confirm the offer flows exist; the charging rule (saved payment method charged when the seller accepts) is documented on support.poshmark.com, see the payments fact file.

## 8. Not found in the web bundle

No `js.stripe.com`, `checkout.com`, `cybersource`, `forter.com` or `riskified` host. "forter" appears only inside unrelated strings. No `hyperwallet` string (the domain used is paylution.com). No `network_token` or `account_updater` string: those run server-side at the processors.
