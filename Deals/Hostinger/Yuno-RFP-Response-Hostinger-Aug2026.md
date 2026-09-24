# PAYMENT ORCHESTRATOR

## Answers to Request for Proposal

**Hostinger**
**August 2026**

---

# Answers to Questions

## 1. Company & Experience

### 1.1. Company overview

Yuno was founded in 2022 by Juan Pablo Ortega, co-founder of Rappi, and Julian Nunez, after experiencing first hand the complexity of scaling payments across fragmented global markets. Today Yuno is the AI-native operating system of global commerce: a unified platform that enables companies to orchestrate their entire payment stack, including payment methods, processors, antifraud tools, KYC/KYB providers, reconciliation and stablecoins, through a single integration.

We operate in more than 190 countries, with over 1,000 payment methods, PSPs and fraud solutions integrated and support for 180+ currencies. Yuno processes over US$1 billion in monthly transaction volume across more than 50 million monthly transactions. The company is backed by globally recognized investors including Andreessen Horowitz (a16z), DST Global, Tiger Global, Kaszek and Monashees; all funding has been raised through equity and Yuno carries no debt.

Our platform powers the payment operations of some of the world's leading companies, including Uber, McDonald's, Rappi, NetEase, Ant Group, inDrive, Garena, Moon Active, Hotmart, Whop, GoFundMe, Despegar, Copa Airlines, Viva Aerobus, Kavak and Carrefour.

By connecting everything in one place, Yuno enables businesses to accelerate global expansion, increase authorization rates, reduce payment costs and operate more efficiently.

### 1.2. Track record & client experience

For a global, subscription driven digital business like Hostinger, the most directly comparable Yuno clients are digital merchants running high volumes of card on file and recurring payments across many markets:

- **Hotmart**: global platform for digital creators, processing subscription and one time payments for content businesses across Latin America and beyond.
- **Whop**: marketplace for digital products and memberships, recurring billing at scale.
- **Open English**: subscription based online education; unified fragmented payment systems on Yuno, increasing approval rates and accelerating time to market for new geographies.
- **Moon Active, NetEase and Garena**: global gaming and digital entertainment companies with high frequency, card on file purchase flows across dozens of countries.
- **GoFundMe**: leading online giving platform, running payments on Yuno globally.

Selected results across our client base, with direct relevance to a prepaid renewal business:

- **inDrive**: reached a 90% approval rate while expanding into 10 new markets in 8 months on Yuno's orchestration layer.
- **Viva Aerobus**: recovered 75% of failed payments, generating more than US$300 per recovered transaction with zero integration cost.
- **Livelo**: recovered 50% of previously failed transactions and improved approval rates by 5 percentage points.
- **McDonald's (Arcos Dorados)**: unified payment operations across 21 Latin American markets on a single platform.
- **Rappi**: integrated hundreds of local payment methods and cut payment issue response time from minutes to seconds.
- **Reserva**: increased approval rates by 4 percentage points in under three months using Smart Routing.

Video case studies:
- Livelo (Brazil): https://www.youtube.com/watch?v=9mPAdwrD77Q
- Rappi (LatAm): https://www.youtube.com/watch?v=fQngxBkUjic
- inDrive (Global): https://www.youtube.com/watch?v=S6BwagGGEtE

Written success stories: https://y.uno/en/success-stories

---

## 2. Network Transaction ID (Scheme Transaction ID)

### 2.1. List of supported PSPs

*Not all PSPs have APIs to respond or accept network tx ID, for recurring business it's important to know if PSPs is capable of doing it.*

Yuno stores network transaction IDs (Visa network tx ID, Mastercard trace ID) via the stored_credentials model at payment_method.detail.card.stored_credentials.network_transaction_id. The API Changelog confirms this field is available for stored credentials. Yuno integrates with 1,000+ payment methods across 190+ countries, including 300+ PSPs. PSP-by-PSP support for network tx ID acceptance can be provided on request.

ADYEN · AIRWALLEX · ANTOM · AZUL · BAC_CREDOMATIC · BAMBOO · BANCARD · BANCO_DO_BRASIL · BANORTE · BARTE · BOKU · BRADESCO · BRAINTREE · CHECKOUT · CIBC · CIELO · CREDIBANCO · CYBERSOURCE · DLOCAL · EBANX · ECOMMPAY · E_MERCHANT_PAY · EVO · FAC · FINTOC · FISERV · GETNET · INOVIO · INSWITCH · ITAU · IZIPAY · KHIPU · KLAP_2 · KUSHKI · MERCADO_PAGO · MONNET · NIUBIZ · NMI · NOMUPAY · NTT_DATA · NUVEI · OKTO · OPENPAY · PAGARME · PAGO_EFECTIVO · PAGSEGURO · PAGSMILE · PAYMENTEZ · PAYPAL · PAYPLUG · PAYU · PAYVALIDA · PINBANK · PRISMA · PROSA_ISO · QNB_MPGS · REDE · REDEBAN_DIRECT · REDSYS · SAFETYPAY · SANTANDER · SPINPAY · STARKBANK · STONE · STP · STRIPE · TAP_PAYMENTS · TRANSBANK · TRANSFEERA · UNLIMINT · WOMPI · WORLDLINE · WORLDPAY · XACBANK · XENDIT · ZOOP

Documentation: https://docs.y.uno/docs/payment-features/stored-credentials https://docs.y.uno/changelog/api

### 2.2. Logic

*Particular customer can have many network tx IDs thougut the lifecycle. What is the logic you use to pick the network tx for recurring transaction?*

Yuno uses the card.stored_credentials.network_transaction_id field. For recurring transactions, the most recent network tx ID from the initial customer-initiated transaction (CIT) is referenced for subsequent merchant-initiated transactions (MITs). The stored_credentials model supports both reason (CARD_ON_FILE, RECURRING) and usage (USED, FIRST) fields following scheme rules.

Documentation: Stored Credentials - Yuno API Documentation

### 2.3. Backfill

*Do you have an API where merchant can backfill network tx id if it's missing? If not, how it can be done?*

Yes, through several paths. If Hostinger already holds a network transaction ID from prior processing history, it can be supplied directly in the payment request in payment_method.detail.card.stored_credentials.network_transaction_id and Yuno will use the merchant-provided value for the MIT. During card migrations, network transaction IDs are imported together with card data as part of Yuno's token migration process, which backfills the vault at scale. For PCI proxy use cases the stored value is injected with the {{vaulted_token.<TOKEN>.network_transaction_id}} placeholder. Bulk backfills outside a migration are handled with the Yuno team rather than a self-service endpoint

Documentation: Stored Credentials - Yuno API Documentation

### 2.4. Token database health

*Is it possible to easily check what % of your token database has at least 1 network transaction id?*

Yes. Transaction reports expose network_transaction_id, network_token and merchant_order_id per transaction, so the share of traffic carrying a network transaction ID can be measured directly from report data. For a point-in-time view of the vault itself (percentage of stored tokens holding at least one network transaction ID), Yuno's team runs this analysis on request, typically during migration planning and then periodically as part of account reviews

Documentation: https://docs.y.uno/docs/direct-integration-use-cases/build-reports https://docs.y.uno/reference/reports/create-a-report https://docs.y.uno/reference/reports/reports-fields

## 3. Network Tokenization

### 3.1. What card schemes are supported?

Visa, Mastercard, and American Express. Yuno's documentation states: 'A network token is a digitized representation of a card's Primary Account Number (PAN), issued directly by card networks such as Visa, Mastercard, or American Express.' Network token enrollment is automatic for all enrolled cards when enabled.

Documentation: https://docs.y.uno/docs/security-and-compliance/network-tokens

### 3.2. Can you enroll new merchant TRID?

Yes. Yuno can enroll a new merchant Token Requestor ID (TRID) through its network tokenization service as part of the onboarding process. Yuno's documentation describes the network token migration process including importing network tokens from gateway accounts.

Documentation: https://docs.y.uno/docs/security-and-compliance/network-tokens https://docs.y.uno/docs/security-and-compliance/data-migration-processes/network-token-migration-process

### 3.3. Can merchant use existing TRID?

Yes. Merchants can bring their own existing TRID and configure it within Yuno's platform. Yuno supports importing existing network tokens from other providers via its token migration process.

Documentation: https://docs.y.uno/docs/security-and-compliance/data-migration-processes/network-token-migration-process https://docs.y.uno/docs/security-and-compliance/network-tokens

### 3.4. Once successfully enrolled in NT, do you keep raw PAN as well?

Yes. Yuno's token vault stores both the network token and the raw PAN for enrolled cards. Yuno is PCI DSS Level 1 certified and also holds ISO 27001, ISO 27701, SOC 2 Type 2, GDPR, and Visa Service Provider certifications. For non-PCI-certified merchants, Yuno's SDKs keep raw card data off merchant servers entirely (SAQ A scope).

Documentation: https://docs.y.uno/docs/basic-concepts/tokens https://docs.y.uno/docs/security-and-compliance/pci-compliance

### 3.5. List of supported PSPs

*Not all PSPs have APIs to accept NT transactions. Do you have a list of supported integrations?*

Yes. Network token acceptance varies by PSP and acquirer, so Yuno maintains a capability matrix of which integrations accept network token payments (token plus cryptogram) and shares it scoped to the merchant's provider mix during solution design. Where a provider cannot accept a network token, the payment is processed with the vaulted card credential instead, so tokenization never blocks authorization

Documentation: https://docs.y.uno/docs/security-and-compliance/network-tokens https://docs.y.uno/docs/payment-features/network-token-authentication

### 3.6. Network token usage logic

*Token enrollment is far from 100%, what logic do you use to decide which type of token to use?*

When network tokenization is enabled, Yuno provisions a network token for every card enrolled in the vault. At payment time the decision is per provider: if the target provider accepts network token payments, Yuno sends the network token with its cryptogram; if it does not, or the token is not yet active for that card, Yuno processes with the vaulted card credential. Enrollment coverage below 100% is therefore not a blocker, every vaulted card always has a processable credential. Network Token Authentication can additionally be scoped with standard routing rules (per country, amount, payment method or BIN) where enabled

Documentation: https://docs.y.uno/docs/security-and-compliance/network-tokens https://docs.y.uno/docs/using-yuno/dashboard-overview/routing

### 3.7. Raw network token in the response

*Do you provide raw network token in the payment response?*

Yes. Network token data, including network (VISA/MASTERCARD/AMEX), status (ACTIVE/INACTIVE/SUSPENDED), PAR (Payment Account Reference), iin (8-digit), lfd (last four digits), expiration_month, expiration_year, holder_name, and response code, is returned in API responses. For PCI-certified merchants, full token details are available. For non-PCI merchants, masked representations are returned.

Documentation: https://docs.y.uno/reference/payments/the-payment-object https://docs.y.uno/docs/security-and-compliance/network-tokens https://docs.y.uno/reference/network-tokens/generate-network-token-cryptogram

### 3.8. Network token usage flag

*Do you provide a clear identification in the API and UI if transaction was processed with NT?*

Yes. Yuno exposes a clear network_token object in the API response (payment_method.detail.card.network_token) with fields including network, status, and par. The Dashboard UI also indicates whether a transaction was processed with a network token vs. a gateway token or raw PAN.

Documentation: https://docs.y.uno/reference/payments/the-payment-object https://docs.y.uno/docs/using-yuno/dashboard-overview/payments https://docs.y.uno/docs/security-and-compliance/network-tokens

### 3.9. Network token usage metrics

*Do you have dashboards to see how many transactions are going though NT rails?*

Yuno's Insights dashboard supports segmenting volume, approval rate and conversion by network tokens, alongside card brand, currency, country and issuer country, so NT and non-NT traffic can be compared directly in the UI. Transaction reports additionally carry per-transaction network token fields (network_token, network_token_type, network_token_iin, network_token_last4) for analysis in the merchant's own BI stack. Deeper adoption reviews, such as enrollment coverage and NT approval-rate uplift by issuer, are provided by Yuno's team as part of ongoing optimization

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/insights https://docs.y.uno/docs/security-and-compliance/network-tokens

## 4. Data & Reporting

### 4.1. What dashboards do you have?

*How customizable are they?*

Yuno provides four core report types: Payment Reports, Transaction Reports, Transaction Reconciliation Reports, and Settlement Reports. The Reports API supports programmatic report generation and download. Smart Routing analytics includes provider health monitoring, decline analysis, and recovery optimization. Dashboards support role-based access controls and are customizable per merchant needs. The Yuno Dashboard also includes performance and latency charts (P99 provider response times), today's performance review, and conversion rate tracking.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/insights https://docs.y.uno/docs/using-yuno/dashboard-overview/your-payment-operative-system https://docs.y.uno/docs/direct-integration-use-cases/build-reports https://docs.y.uno/reference/reports/create-a-report

### 4.2. Is there a specific dashboards for subscription businesses?

Subscription performance is tracked through three complementary surfaces rather than a separate subscription-only dashboard: (1) Insights segmentation over recurring traffic; (2) transaction reports carrying subscription_id and billing-cycle fields (billing_cycles_current, billing_cycles_next_at, billing_cycles_total) plus merchant_order_id, which lets renewal and retry performance be measured per billing cycle in the merchant's BI; (3) real-time subscription lifecycle webhooks for every state transition. Yuno's team also runs recurring-performance reviews with subscription merchants as part of account management

Documentation: https://docs.y.uno/docs/payment-features/subscriptions https://docs.y.uno/reference/subscriptions/status-subscriptions https://docs.y.uno/docs/webhooks

### 4.3. Do you have any aggregation based on order id?

*E.g. recurring charges retries often drags down the auth rate if you look from transaction perspective, but from order perspective it's more informative.*

Yes. Every payment carries merchant_order_id, exposed both in the API (payments are retrievable by merchant order id) and as a column in transaction reports. Retries of the same order share the order id, so order-level approval rate (whether the order eventually succeeded) can be computed directly from report data, separating true conversion from attempt-level noise introduced by dunning retries

Documentation: https://docs.y.uno/reference/payments/retrieve-payment-by-merchant-order-id https://docs.y.uno/docs/payment-features/subscriptions/retries https://docs.y.uno/reference/reports/reports-fields

### 4.4. Export to data warehouse.

*Do you support data export to dwh? If so, which providers do you support?*

Yes. Yuno supports data export via the Reporting API, which enables programmatic report generation and download. The platform provides payment, transaction, and settlement reports that can be exported for ingestion into data warehouses. Specific DWH connector availability (e.g., Snowflake, BigQuery, Redshift) should be confirmed with your Yuno account team based on your infrastructure.

Documentation: https://docs.y.uno/docs/direct-integration-use-cases/build-reports https://docs.y.uno/reference/reports/create-a-report https://docs.y.uno/reference/reports/download-a-report

### 4.5. 8 digit BIN

*Do you support 8 digit BIN exposure?*

Yes. Yuno supports 8-digit BIN exposure via API responses and token data. The token_data object includes iin at 8-digit granularity (e.g., '45079900'). The card_data object also includes iin, lfd, number_length, brand, issuer_name, issuer_code, country_code, category, type, and fingerprint. Card fingerprinting provides a stable, cryptographic identifier for deduplication without exposing raw PAN.

Documentation: https://docs.y.uno/docs/security-and-compliance/fingerprint https://docs.y.uno/reference/payments/the-payment-object https://docs.y.uno/docs/basic-concepts/tokens

## 5. Fallbacks

### 5.1. What fallback logic do you use?

Yuno provides two layers of fallback protection: (1) Condition-based routing with primary and fallback provider chains, triggered on decline (by decline group/code), timeout, or specific error conditions. (2) Monitors feature: automatically detects provider approval rate drops below configurable thresholds, redirects traffic to fallback providers, and auto-recovers when the primary provider's approval rate returns above the threshold. If all providers are below threshold, traffic routes to the one with the highest recent approval rate. Alerts via email and Opsgenie.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/docs/using-yuno/dashboard-overview/monitors https://docs.y.uno/docs/payment-features/transaction-retries

### 5.2. How customizable it is?

Highly customizable. Yuno's Smart Routing supports condition-based routing with: COUNTRY, ISSUER_COUNTRY, CURRENCY, AMOUNT, CARD_TYPE, CARD_BRAND, CARD_BIN, INSTALLMENTS, TRANSACTION_TYPE, and METADATA. Routing can be configured via the visual Dashboard or REST API. Smart Routing optimizes by approval rate or cost. Post-authorization steps (antifraud, authentication) can be chained. Monitors provide automated fallback with configurable approval rate thresholds and traffic percentage controls.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/reference/organizations/routing/routing-conditions https://docs.y.uno/docs/using-yuno/dashboard-overview/monitors

## 6. Routing

### 6.1. What routing management flow can the merchant use?

Yuno provides both a visual routing dashboard (with Table view and List view) and a full REST API for routing management. The Dashboard supports condition set creation, reordering, provider selection, percentage allocation, Smart Routing toggle, and Publish workflow. The API supports programmatic CRUD operations on routing configurations. Routing can also incorporate Risk Profiles and post-authorization flows (antifraud, 3DS authentication).

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/reference/organizations/connections-routing-overview https://docs.y.uno/reference/organizations/routing/create-routing

### 6.2. Does it have any validation from user error?

Yes. Routing rules are validated on save. The Dashboard requires explicit publishing of routing changes. Monitors feature provides runtime validation: when providers drop below approval thresholds, traffic is automatically redirected. The List view provides a structured table format for reviewing complex route configurations with many condition sets.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/docs/using-yuno/dashboard-overview/monitors

### 6.3. Does it have version control?

Yes. Routing configurations support a Publish workflow in the Dashboard, where changes are explicitly published to take effect. Condition set reordering is supported. For full audit trail and version history details, confirm with your Yuno account team.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/docs/using-yuno/settings/audit-logs

## 7. Webhooks

### 7.1. Webhooks

*Do you show what webhooks transaction received in the payments screen/timeline?*

Webhook endpoints, event selection and payload examples are managed in the Dashboard, and the payment detail view shows the full transaction timeline that the webhooks mirror. Delivery is at-least-once with automatic retries, up to seven attempts on a documented escalating schedule (immediate, 5 min, 50 min, 6 h, 24 h, 48 h, 96 h), so no event is lost to a transient endpoint failure. HMAC signature verification and OAuth2 are supported for endpoint security. Per-payment webhook delivery logs are not currently surfaced in the payments screen; delivery diagnostics are handled with Yuno support

Documentation: https://docs.y.uno/docs/webhooks https://docs.y.uno/docs/webhooks/configure-webhooks https://docs.y.uno/docs/webhooks/verify-webhook-signatures-hmac https://docs.y.uno/docs/using-yuno/dashboard-overview/payments

### 7.2. Webhook unification

*Do you unify certain types of webhooks (e.g. chargebacks)? If so, do you have a list for which PSPs which webhooks are supported?*

Yes. Yuno normalizes webhook events across all integrated PSPs into a unified event model. Standardized event types include: payment events (payment.purchase, payment.refund, payment.capture, payment.cancel, payment.chargeback, payment.fraud_screening), enrollment events (enrollment.create, enrollment.update), and subscription events (subscription.create, subscription.active, subscription.pause, subscription.resume, subscription.cancel, subscription.complete). Yuno maintains documentation showing which webhooks are supported per PSP integration.

Documentation: https://docs.y.uno/docs/webhooks https://docs.y.uno/docs/webhooks/object-and-examples

## 8. Pinless Debit Routing

### 8.1. Do you have support for pinless debit routing?

Yuno supports pinless debit through acquirers that offer it rather than as a Yuno-side debit-network switch. Debit traffic is identified and segmented in routing (CARD_TYPE, CARD_BIN, issuer country) and steered to connections where pinless or least-cost debit processing is enabled on the acquirer side. Whether pinless rails apply to a given transaction is then governed by that acquirer's capabilities and the merchant's configuration with them

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/reference/organizations/routing/routing-conditions

### 8.2. For which providers?

Pinless debit is an acquirer capability, so the relevant list depends on the merchant's markets and acquirer mix. Yuno validates pinless support with the shortlisted acquirers for the target regions during solution design and configures routing so debit BINs reach those connections. We are happy to run this validation against Hostinger's specific provider shortlist as part of the evaluation

### 8.3. How the logic of using it is controlled?

Controlled through routing conditions: rules combining CARD_TYPE, CARD_BIN, country, currency and amount steer eligible debit traffic to the connections where pinless processing is enabled, while everything else follows the standard card routes. Rules are managed in the Dashboard or via the routing API and can be changed without code

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/reference/organizations/routing/routing-conditions

## 9. PCI Proxy

### 9.1. PCI Proxy support

*Does your platform support PCI proxy capabilities?*

Yes. Yuno provides a PCI Proxy feature that allows merchants to send raw card data to any third-party API through Yuno's PCI DSS Level 1 environment. The proxy supports GET, POST, PUT, PATCH, and DELETE methods. Card data is referenced via placeholders like {{vaulted_token.<TOKEN>.number}}, {{vaulted_token.<TOKEN>.expiration_month}}, {{vaulted_token.<TOKEN>.expiration_year}}, and {{vaulted_token.<TOKEN>.holder_name}}. Yuno also supports redacting card data from responses via the yuno-proxy-response-redactions header. Limits: 1 MB request/response body, 20 distinct vaulted tokens per request, configurable timeout up to 120 seconds.

Documentation: https://docs.y.uno/docs/security-and-compliance/pci-proxy/overview https://docs.y.uno/docs/security-and-compliance/pci-proxy/forward-proxy https://docs.y.uno/docs/security-and-compliance/pci-proxy/allowlist https://docs.y.uno/reference/pci-proxy/invoke-forward-proxy

### 9.2. Payments list

*Do proxied transactions are showed in payments list? If so, what data is showed?*

No, by design. Requests sent through the PCI proxy are API forwards to third parties, not Yuno payments, so they do not appear in the payments list (only payments created through Yuno's payment APIs do). Every proxy invocation produces an audit record capturing who called it, when, the destination and the outcome; card data is never logged and request and response bodies are excluded from logs. Where the merchant wants proxied operations visible as payments, the equivalent flow through Yuno's payment API is the recommended pattern

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/payments https://docs.y.uno/docs/security-and-compliance/pci-proxy/overview

### 9.3. Network transaction ID

*Can you insert network tx ID in the proxied request?*

Yes, natively. The forward proxy supports a {{vaulted_token.<TOKEN>.network_transaction_id}} placeholder that injects the network transaction ID stored for that vaulted card into the outbound request; the docs call this out precisely because many processors require it for merchant-initiated transactions. Network token placeholders (number, expiration month and year) are available as well. If the merchant holds its own network transaction ID from processing history, the literal value can also simply be included in the proxied request body, since the ID itself is not PCI-scoped data

Documentation: https://docs.y.uno/docs/security-and-compliance/pci-proxy/forward-proxy https://docs.y.uno/docs/payment-features/stored-credentials

## 10. Account Updater

### 10.1. Scheme support

*For which card schemes do you support account updater?*

Yuno's Card Account Updater (CAU) is currently available for Visa (Visa Account Updater - VAU) and Mastercard (Automatic Billing Updater - ABU). This is explicitly documented: 'Card Account Updater is currently available for Visa and Mastercard.'

Documentation: https://docs.y.uno/docs/additional-services/card-account-updater

### 10.2. Logic

*How the update logic is handled?*

CAU operates asynchronously, independently of the payment flow. Yuno automatically monitors stored credentials and updates expired, reissued, or upgraded card details. Updates occur when: (1) the card is past its expiration date, or (2) the account is in a closed, disabled, or flagged state. When a card is updated, Yuno sends an enrollment.update webhook with the new expiry, last four digits, IIN, update reason, and replaced card details. Critically, the vaulted_token and fingerprint remain the same, no integration changes are needed. A card_data_history array tracks previous card data.

Documentation: https://docs.y.uno/docs/additional-services/card-account-updater https://docs.y.uno/docs/webhooks/object-and-examples

### 10.3. Manual initiation

*Can you initiate update via API?*

Card enrollment into the Account Updater is available via API: POST /payment-methods/account-updater registers stored cards for monitoring, with registration running asynchronously (a 200 confirms the cards were accepted). The updates themselves originate from the card schemes, so there is no on-demand "refresh this card now" call; once registered, scheme updates are applied automatically and notified through the enrollment.update webhook. Activation is arranged with the Yuno team and scheme registration can take up to 10 working days for new customers

Documentation: https://docs.y.uno/docs/additional-services/card-account-updater https://docs.y.uno/reference/payment-methods-direct-workflow/register-cards-for-account-updater-api

### 10.4. Other ways to initiate update

*Is there any other ways to trigger the update? E.g. as a workflow rule or smth*

No additional trigger mechanism is needed. CAU runs as a continuous background service independent of the payment flow: registered cards are monitored and updates from Visa (VAU) and Mastercard (ABU) are applied automatically as issuers publish them. The merchant-side touchpoints are the registration API for enrolling cards and the enrollment.update webhook for consuming changes. Because the vaulted_token and card fingerprint stay stable across updates, no merchant-side workflow rules are required for the update to take effect on the next billing cycle

Documentation: https://docs.y.uno/docs/additional-services/card-account-updater https://docs.y.uno/docs/webhooks

## 11. Recurring Engine

### 11.1. Do you have recurring engine?

Yes. Yuno provides a full subscription/recurring engine. Subscriptions move through states: CREATED → ACTIVE (on first successful payment) or CANCELLED. Other states: PAUSED and COMPLETED. Key features: configurable billing frequency (daily/weekly/monthly), start_at and finish_at dates, first_successful_payment_only flag, Smart Retries with configurable strategy and count (up to 5 in production), card-on-file storage via token vault, lifecycle management webhooks, and a management_url for customer self-service. Currently, only Cards can be used as payment methods for subscriptions.

Documentation: https://docs.y.uno/docs/payment-features/subscriptions https://docs.y.uno/docs/payment-features/subscriptions/retries https://docs.y.uno/reference/subscriptions/create-subscription https://docs.y.uno/reference/subscriptions/the-subscription-object

### 11.2. How customizable is the logic?

Highly customizable via the subscription creation API. Configurable parameters include: billing frequency (daily/weekly/monthly), start_at and finish_at dates, amount, retry_on_decline flag (bool), number of retries (amount, capped at 5 in production), retry strategy (DEFAULT with fixed schedule: 5h/12h/24h/36h/48h, or CUSTOM_SCHEDULE with per-attempt delay_seconds), stop_on_hard_decline flag (stops retries for current cycle only, subscription stays ACTIVE), first_successful_payment_only flag, and trial periods with $0 cycles. Subscriptions support both CIT and MIT workflows.

Documentation: https://docs.y.uno/docs/payment-features/subscriptions/retries https://docs.y.uno/reference/subscriptions/create-subscription https://docs.y.uno/docs/payment-features/subscriptions/plans

## 12. PayPal

### 12.1. Reference transactions (RT)

*Do you support setting billing agreement IDs, aka reference transactions?*

Yes. Yuno supports PayPal recurring processing on billing agreements: the agreement is established with the customer present and subsequent merchant-initiated charges reference the billing agreement ID. Yuno has also executed migrations of existing PayPal billing agreement portfolios into Yuno for large recurring merchants; billing agreement IDs are scoped to the PayPal merchant account (payee), so they remain valid when moving orchestration to Yuno as long as the same PayPal merchant account is retained. Zero-value verification of vaulted PayPal agreements is available to validate credentials without charging. Detailed flow design, including migration of the existing agreement portfolio, is covered with Yuno's solution team during onboarding

Documentation: https://docs.y.uno/changelog/web

## 13. Apple Pay / Google Pay

### 13.1. Apple pay implementation

*How apple pay is implemented in your platform?*

Yuno's iOS, Android, Web, Flutter, and React Native SDKs support Apple Pay natively. The Apple Pay SDK integration documentation explicitly covers both one-time payments and recurring payments (CIT and MIT). Apple Pay tokens are vaulted in Yuno's token vault. Recurring payments use checkout sessions with billing_agreement, start_at, finish_at, and management_url. Apple Pay is displayed as a direct button (not a radio button) from SDK v1.5+. The cancel flow includes metadata with paymentCreated boolean.

Documentation: https://docs.y.uno/docs/wallets/apple-pay/apple-pay-sdk-integration https://docs.y.uno/docs/wallets/apple-pay/prerequisites-apple-pay https://docs.y.uno/docs/wallets/apple-pay/apple-pay-direct-integration

### 13.2. Google pay implementation

*How google pay is implemented in your platform?*

Yuno's Android, iOS, Web, Flutter, and React Native SDKs support Google Pay natively. Google Pay is displayed as a direct button (not a radio button) from SDK v1.5+. The mountExternalButtons method allows custom placement of Google Pay buttons. Google Pay wallet tokens are vaulted and managed through Yuno's token vault for both one-time and recurring use cases.

Documentation: https://docs.y.uno/docs/wallets/google-pay/google-pay-sdk-integration https://docs.y.uno/docs/wallets/google-pay/google-pay-direct-integration https://docs.y.uno/docs/wallets/google-pay/integration-via-provider-google-pay

### 13.3. Support accross different PSPs

*Do you have a list of PSPs accross which apple pay tokens are working well for MITs?*

Wallet MIT support depends on how each PSP accepts the vaulted wallet credential (DPAN) with stored-credential framing, so it is validated per provider rather than published as a static list. Yuno vaults Apple Pay and Google Pay tokens and supports CIT-then-MIT flows on providers that accept wallet-token MITs; the concrete list scoped to Hostinger's provider mix is confirmed during solution design and certification, including test transactions on each target connection before go-live

Documentation: https://docs.y.uno/docs/wallets/apple-pay/apple-pay-sdk-integration https://docs.y.uno/docs/payment-features/stored-credentials

### 13.4. Support for new format Apple Pay MIT transactions

*https://support.cybersource.com/knowledgebase/knowledgearticle/?code=KA-04318*

The referenced Cybersource note concerns Apple Pay's updated format for merchant-initiated transactions (merchant tokens, MPAN, replacing device-token-based MITs). Yuno's wallet stack is actively maintained against wallet and scheme mandates, and Apple Pay recurring support (recurring payment requests with billing agreement fields) is already in place across the SDKs. MPAN rollout status is processor-dependent; Yuno's product team confirms the current state per acquirer and we are glad to review it against Hostinger's target providers during evaluation

Documentation: https://docs.y.uno/changelog/web https://docs.y.uno/changelog/ios

## 14. Risk Screening

### 14.1. Do you have build in risk-engine?

Yes. Yuno offers Risk Conditions: a built-in, no-code rules engine for fraud prevention. It supports: custom rules, blocklists (to block specific users/cards/emails), and allowlists (to always allow trusted entities). Risk conditions can operate pre-authorization (block) or post-authorization (flag for review). Risk Profiles can be added to routing conditions as part of the payment flow.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/risk-conditions https://docs.y.uno/docs/using-yuno/dashboard-overview/routing

### 14.2. Do you support 3rd party risk engines?

*If yes, which ones?*

Yes. Alongside the built-in Risk Conditions engine, Yuno integrates leading third-party fraud providers, including Riskified, Signifyd, Forter, ClearSale, Konduto, Kount, Sift, SEON, Cybersource Decision Manager, Accertify, Vesta, TrustDecision, Bayonet, Fraudio and PRECISION (Etraveli Group), among others. Fraud screening can run pre-authorization or post-authorization as a routing step, and different providers can be used per segment. The full current connector list for the merchant's regions is shared during solution design

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/changelog/web

## 15. 3D Secure (3DS)

### 15.1. What 3DS engine do you use?

Yuno provides its own 3DS2 engine with support for multiple 3DS providers: Netcetera (default), Cybersource, and Checkout.com. The platform supports both frictionless and challenge flows in compliance with EMV 3DS 2.x specifications (2.1.0, 2.2.0, 2.3.1). Yuno also offers 3DS Standalone: authentication-only flow without payment authorization. Native mobile 3DS is supported via Netcetera's 3DS SDK for Android and iOS.

Documentation: https://docs.y.uno/docs/security-and-compliance/3d-secure https://docs.y.uno/docs/payment-features/3ds-standalone https://docs.y.uno/docs/sdks/external-native-modules/netcetera-3ds-android https://docs.y.uno/docs/sdks/external-native-modules/netcetera-3ds-ios

### 15.2. Do you have dynamic 3DS logic?

Yes. Yuno supports dynamic 3DS logic through routing configuration. 3DS can be added as a step in the routing flow (pre-authorization or post-authorization). The 3DS Standalone feature allows pure authentication without payment. Routing conditions determine when 3DS is applied based on transaction characteristics. The 3DS configuration supports specifying which 3DS provider to use per routing condition.

Documentation: https://docs.y.uno/docs/security-and-compliance/3d-secure https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/docs/payment-features/3ds-standalone https://docs.y.uno/reference/three-d-secure-setups/create-three-d-secure-setup

### 15.3. Do you support force challenge 3ds flow?

Yes. Yuno supports challenge 3DS flows. The 3DS Standalone documentation explicitly supports three modes: FRICTIONLESS, CHALLENGE, and DATA_ONLY. Test cards are provided for each scenario. The webhook response includes a has_challenge boolean indicating whether the authentication went through a challenge. The pares_status field indicates the authentication result (Y=authenticated, N=failed, C=challenge required).

Documentation: https://docs.y.uno/docs/payment-features/3ds-standalone https://docs.y.uno/docs/direct-integration-use-cases/3ds-configuration-and-testing

### 15.4. Do you support processor 3DS?

*E.g. using Stripe, Adyen or other provider 3DS setup*

Yes. Yuno can leverage processor-native 3DS implementations. The documented 3DS providers include Netcetera (default 3DS Server), Cybersource, and Checkout.com. When routing transactions through specific PSPs, Yuno can use their 3DS implementations. The platform abstracts the 3DS flow so merchants get a unified integration regardless of the underlying provider's 3DS mechanism. For PSPs listed as 3DS-enabled in the dashboard, the 3DS setup is configured at the connection level.

Documentation: https://docs.y.uno/docs/security-and-compliance/3d-secure https://docs.y.uno/reference/three-d-secure-setups/create-three-d-secure-setup

## 16. Checkout Builder

### 16.1. Do you support dynamic display of payment methods for each customer?

Yes. Yuno's Checkout Builder and Smart Routing can dynamically display or hide payment methods based on customer attributes such as country, currency, transaction amount, and custom metadata. The routing configuration supports condition sets that determine which payment methods are shown. The SDK supports multiple integration modes (Seamless, Lite, Headless) giving merchants full control over payment method presentation.

Documentation: https://docs.y.uno/docs/using-yuno/dashboard-overview/checkout-builder https://docs.y.uno/docs/using-yuno/dashboard-overview/routing https://docs.y.uno/docs/sdks/overview/choose-integration

### 16.2. How many integration options are there for front-end implementation?

Yuno offers multiple front-end integration options: (1) Seamless SDK (Full), pre-built checkout UI with automatic payment method listing, separate wallet buttons; (2) Lite SDK, semi-customized with merchant-controlled payment method display; (3) Headless SDK, fully custom UI with Yuno handling the secure fields; (4) Payment Links, hosted payment page via URL; (5) Direct REST API, for fully custom front-ends (PCI DSS Level 1 required). All SDKs support enrollment (vaulting) and payment flows. White-label and custom styling (fonts, colors, buttons) are supported across all SDK types.

Documentation: https://docs.y.uno/docs/sdks/overview/choose-integration https://docs.y.uno/docs/sdks/seamless-sdk https://docs.y.uno/docs/sdks/lite-web/payment https://docs.y.uno/docs/sdks/headless-web/payment https://docs.y.uno/docs/using-yuno/dashboard-overview/payment-links https://docs.y.uno/reference/getting-started/api-reference-overview

## 17. Integration & SDKs

### 17.1. What SDKs do you have for back-end?

Yuno's backend surface is a single REST API (JSON over HTTPS) covering all server-side operations: checkout sessions, payments (create, authorize, capture, refund, void), tokenization and vault, subscriptions, routing configuration and reporting. There are deliberately no required server-side SDKs; the API integrates directly from any stack, and a maintained Postman collection is provided for exploration and testing. Idempotency keys, HMAC-signed webhooks and account/secret API credentials are standard. This keeps the backend integration dependency-free and identical across languages

Documentation: https://docs.y.uno/reference/getting-started/api-reference-overview https://docs.y.uno/reference/getting-started/authentication https://docs.y.uno/reference/getting-started/postman-collections

### 17.2. What SDKs do you have for front-end?

Yuno provides a Web SDK (JavaScript) for frontend integration, supporting: Seamless SDK (full checkout UI), Lite SDK (merchant-controlled method display), and Headless SDK (fully custom UI with secure fields). The Web SDK supports cards, digital wallets (Apple Pay, Google Pay, Click to Pay, PayPal), and local payment methods. Features include: customizable styling, white-label hosting, SRI support, enrollment flows, and 3DS handling. The SDK automatically handles co-badged card compliance (EU IFR 2015/751).

Documentation: https://docs.y.uno/docs/sdks/overview/choose-integration https://docs.y.uno/docs/sdks/seamless-sdk/web-payments https://docs.y.uno/docs/sdks/lite-web/payment https://docs.y.uno/docs/sdks/headless-web/payment https://docs.y.uno/docs/sdks/customization/web/styling https://docs.y.uno/docs/sdks/customization/web/white-label

### 17.3. What SDK do you have for mobile?

Yuno provides: Android SDK (Kotlin, available via Maven/Gradle), iOS SDK (Swift, supports Swift 6 concurrency), Flutter SDK (cross-platform), and React Native SDK. All mobile SDKs include: one-time token creation, card enrollment (vaulting), wallet integration (Apple Pay/Google Pay), 3DS challenge handling via native Netcetera 3DS SDK, and antifraud token collection. Headless and Lite modes are available on all platforms. ProGuard/R8 rules are provided for Android.

Documentation: https://docs.y.uno/docs/sdks/seamless-sdk/android-payments https://docs.y.uno/docs/sdks/seamless-sdk/ios-payments https://docs.y.uno/docs/sdks/additional-platforms/flutter https://docs.y.uno/docs/sdks/additional-platforms/react-native https://docs.y.uno/docs/sdks/external-native-modules/netcetera-3ds-android https://docs.y.uno/docs/sdks/external-native-modules/netcetera-3ds-ios

### 17.4. SDK integrations

Native SDKs (first-class, actively versioned):
Web SDK, JavaScript, `@yuno-payments/sdk-web` via npm or CDN
iOS SDK, Swift
Android SDK, Kotlin

Cross-platform wrappers:
Flutter SDK, Dart, wraps native iOS/Android
React Native SDK, wraps native iOS/Android (Full + Lite + Headless variants, plus styling/enrollment)

Integration modes (available across Web, iOS, Android):
Seamless SDK, pre-built UI, full dashboard control (add methods, set conditions, style checkout without code)
Lite SDK, you control payment-method selection UI, Yuno handles secure processing
Headless SDK, fully custom UI, tokenization + 3DS only
Secure Fields, tokenize cards without mounting the full SDK

Each mode supports payment + enrollment flows and 3DS.

External native modules:
Netcetera 3DS SDK (Android), native in-app 3DS challenges
Netcetera 3DS SDK (iOS), native in-app 3DS challenges

Wallet SDK integrations (SDK_CHECKOUT workflow):
Apple Pay
Google Pay
NuPay

Also available: card enrollment flows, white-label hosting (serve the Web SDK from your own domain with no Yuno branding), styling customization, and country/language reference coverage.

## 18. Other: Co-badged Cards

### 18.1. Co-branded cards selection

*Can you specify which rails to use for co-branded cards? E.g. Carte Bancaire in France*

Yes. Yuno provides built-in co-badged card compliance per EU IFR Regulation 2015/751 Article 8. When using Yuno's SDKs, co-badged card network selection is handled automatically: the SDK detects co-badged cards by IIN, displays network selection options (e.g., Cartes Bancaires vs. Visa), stores the customer's choice, and applies it to all recurring payments. Supported SDKs: Web v1.1.0+, iOS v2.0.0+, Android v2.0.0+, React Native v1.0.16+. For Direct API integrations, merchants must implement network selection themselves. Yuno's routing conditions also support BIN-based routing for co-badged cards.

Documentation: https://docs.y.uno/docs/security-and-compliance/co-badged-cards-compliance
