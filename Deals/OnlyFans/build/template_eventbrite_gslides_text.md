-----

  

# Powering Seamless Global  
Money Movement for Eventbrite

  

-----

-----

  
AGENDA  
  
01  
A GLOBAL PAYMENT INFRASTRUCTURE FOR BENDING SPOON’S ECOSYSTEM  
  
02  
HOW EVENTBRITE RUNS PAYMENTS TODAY  
  
03  
THE PROPOSED MODEL  
  
04  
WHY YUNO?  
05  
THE MARKETPLACE CASE  

-----

-----

  
  
A Global Payment Infrastructure for Bending Spoons’ Ecosystem  
01  

-----

-----

  
A GLOBAL PAYMENT INFRASTRUCTURE FOR BENDING SPOON’S ECOSYSTEM  
Bending Spoons operates at global scale, centralizing technology and operations on a single platform  
  
THE SCALE TODAY  
400M+  
Monthly active users  
7M+  
Subscriptions customers,  
accounting for 84% of total revenues  
  
48% of subscription revenue comes from customers acquired 5+ years ago. Your payment stack and acceptance rate play a key role in CAC  
  
WHERE BENDING SPOONS IS HEADING  
Become a permanent home for digital businesses, with a stated ambition of up to 1,000 further acquisitions.  
Expanding beyond consumer subscriptions into marketplaces (Eventbrite), media (AOL), and B2B SaaS (Airtable), with products used in 180+ countries  
Converge onto a single centralized technology and operations platform run from Milan  
GLOBAL FOOTPRINT  
B2B SaaS  
  
Media  
  
Data  
  
Entertainment  
  
Consumer  
  
3 out of every 4 revenue dollars at Bending Spoons move through electronic payments. However, the rails behind them were built by 50 different companies  
  
With over $1.3B in total revenues and being present in +180 countries, payments remains the one layer not yet centralized.  
Source: Bending Spoons F-1 (SEC, Jun 2026); Q2 2026 earnings release (Aug 2026); management statements at IPO (Jul 2026)  

-----

-----

A GLOBAL PAYMENT INFRASTRUCTURE FOR BENDING SPOON’S ECOSYSTEM  
Payments remains the last fragmented layer,  
each acquisition kept its own rails and methods  
\+50  
companies  
SOME ALTERNATIVE PAYMENT METHODS BSP IS NOT OFFERING  
Fragmented Billing Across 50+ Acquired Brands Blocks Unified Reconciliation  
Static PSP rules can’t react to BIN, issuer health, or time-of-day, leaving auth uplift on the table.  
  
CHALLENGES IDENTIFIED  
A Third of Card Revenue Pays 15-30% App-Store Fees With No Routing Layer  
Static PSP rules can’t react to BIN, issuer health, or time-of-day, leaving auth uplift on the table.  
Failed Renewals Across Evernote and WeTransfer Inflate Involuntary Churn  
Failed recurring charges and soft declines silently erode lifetime value month after month.  
Top Markets Japan, Brazil and India Sit on Card-Only Web Checkout  
Missing local methods at checkout push shoppers to competitors who localized first.  
A Portfolio Spanning US, EU and Asia Multiplies Cross-Border Currency Friction  
Foreign-issuer declines spike on international BINs without smart failover to a local acquirer.  

-----

-----

  
\+50  
companies  
One integration  
owned by BSP  
  
API  
RISK CONDITIONS  
  
RECONCILIATIONS  
  
INSIGHTS  
  
SMART ROUTING  
  
CHECKOUT BUILDER  
  
PAYOUTS  
  
FRAUD & RISK  
  
TOKENIZATION  
  
CONNECTORS  
  
\+460 Global Payment Partners & Methods  
Expected Impact  
\+12%  
Avg. auth-rate  
uplift  
20-30%  
Decline recovery  
  
Smart Routing Engine  
Route every renewal across the portfolio’s Stripe, PayPal, etc. rails by BIN, issuer and market to lift auth on 7M subscribers.  
  
Failover + Recovery  
Automatic cascade and dunning recovers up to 50% of failed renewals across Evernote, WeTransfer and Remini.  
  
1,000 Local Methods  
Add Pix in Brazil, UPI in India, Konbini in Japan and GCash in the Philippines through one API, beyond card-only web checkout.  
  
Nova Fraud Intelligence  
AI scoring on 5,000+ data points reduces false declines up to 75% and cuts the chargebacks behind unrecognized-charge complaints.  
A GLOBAL PAYMENT INFRASTRUCTURE FOR BENDING SPOON’S ECOSYSTEM  
From a processor mesh to one scalable  
Global Financial Infrastructure  

-----

-----

One single platform to manage your whole portfolio’s payment stack  
One dashboard, every PSP, one click  
Plug and Play any PSP  
460+ providers in our portfolio.  
Smart Routing per condition  
Route by card brand, BIN, currency, country, amount.  
Choose the volume split  
50/50, 70/30, custom weights. Distribute traffic to test, ramp, or load-balance.  
Cascade through declines  
Auto-failover on retryables and errors.   
A GLOBAL PAYMENT INFRASTRUCTURE FOR BENDING SPOON’S ECOSYSTEM  
Connect any provider in our portfolio,  
route every transaction your way in one single dashboard  

-----

-----

  
  
How Eventbrite Runs Payments Today  
02  

-----

-----

  
INDUSTRY CONTEXT  
Ticketing at a glance: one company owns the top of the market, nobody owns the payments layer under it  
$56.6B  
TAM  
Online event ticketing market, 2026,  
growing at \~6.7% CAGR  
Ticketing itself is a $56.6B slice of a $1.46T global events industry (2026). Ticket sales are only the front door: what happens after, paying organizers, vendors and venues, moves through a separate and disconnected set of payout rails. The market's growth gets counted in ticket volume; its margin gets decided by what happens to that money next.  
  
\~80%  
Of primary ticketing at major concert venues sits with one company: Ticketmaster  
Ticketmaster built that share around marquee venues and arena tours. Eventbrite plays a different game: self-service signup, open to anyone running an event. That long tail produced 78.9M paid tickets and $3.0B+ in sales in FY2025.  
  
\~41%  
Of Eventbrite's paid tickets are international, but they generate only 28.4% of revenue (FY2025)  
International processing already runs cheaper on local rails, per Eventbrite's own filings. Yet international revenue lags ticket volume by 13 points. The demand is already there. What is missing is acceptance and routing built for it.  
6  
PAYMENT VENDORS, ZERO ORCHESTRATION LAYER  
Cybersource, Adyen, Braintree, Mercado Pago, Wells Fargo, and Stripe all sit on Eventbrite's own sub-processor list. Routing between them is self-built, described in their 10-K only as multiple integrations in place at one time.  
Ticketing is concentrated at the top and fragmented everywhere else, including inside Eventbrite’s own stack. Processing fees are already named as the largest component of Eventbrite’s cost of net revenue. That is the conversation this deck is about.  

-----

-----

  
KEY CHALLENGES  
Executive Summary  
EVENTBRITE  
$3.0B gross ticket sales and $291.8M net revenue in 2025.  
258M tickets, 4.6M events.  
Part of Bending Spoons since March 2026.  
  
SIX PROCESSORS, ZERO ORCHESTRATION  
All run in parallel, with no failover, no smart routing and no ledger between them.  
  
KEY CHALLENGES  
01  
Six Rails, No Routing or Failover Between Them  
02  
One Reporting Portal per Provider, No Unified Reconciliation  
03  
Creators Tied to One Rail, Double FX on Cross-Currency Events  
04  
Own Entities Keep LatAm Compliance and Funds Flow In-House  
05  
Multi-PSP Direction Set, No Orchestration Layer Running Yet  
  
WHAT WILL YOU GET BY WORKING WITH YUNO  
PAY-IN & PAYOUT ROUTING IN ONE LAYER  
Both sides of the marketplace orchestrated, with the ledger that links every pay-in to its payout.  
MODULAR BY DESIGN  
Activate only what you need, and every provider you run today stays. Smart routing with fallbacks and retries, network tokenization, KYC and KYB, split payments, fraud and 3DS, and reconciliation all arrive as modules on the same integration.  
ONE DASHBOARD  
One ledger across every PSP, with payment ops, chargebacks and refunds in one place instead of one portal per provider. Analytics on fees, FX and approvals that are decision-ready, plus Payments Concierge, a natural-language copilot for payment ops.  

-----

-----

  
HOW EVENTBRITE RUNS PAYMENTS TODAY  
Where Eventbrite’s demand actually sits  
% OF WEB TRAFFIC BY COUNTRY  
  
United States  
49.58%  
  
United Kingdom  
14.97%  
  
Canada  
8.66%  
  
Australia  
4.88%  
  
Germany  
3.04%  
  
Brazil  
2.45%  
  
Spain  
1.68%  
  
Mexico  
1.55%  
  
India  
1.36%  
  
France  
1.22%  
  
Netherlands  
0.95%  
  
Argentina  
0.69%  
  
Ireland  
0.59%  
Colombia  
0.36%  
Source Similarweb, 2026  

-----

-----

  
HOW EVENTBRITE RUNS PAYMENTS TODAY  
Eventbrite’s current setup runs six rails with zero orchestration between them  
THE CURRENT SETUP HAS MANY CONSTRAINTS  
  
MISSING LOCAL METHODS IN TOP MARKETS  
None of the six rails currently offer Pix, Boleto, OXXO, SEPA Direct Debit, Bizum or Klarna, the local methods that convert best in Brazil, Mexico, Germany, Spain and Europe, markets already inside Eventbrite’s own top 10 by tickets sold.  
PAY-IN AND PAYOUT, NEVER TIED TOGETHER  
No orchestrator evaluated connects pay-in and payout end to end. Pay-ins collected under one PayPal MID pay out to 12,000 individual creators with nothing tracing one to the other.  
  
LATAM ENTITIES, AND ONE MORE PORTAL TO LOG INTO  
Brazil, Argentina, Mexico and Colombia run through entities Eventbrite wants to exit. EBANX is reachable only through Braintree today, with no unified reporting, their own payments operations leader’s reaction: another EBANX login means “another portal” on top of the ones they already have.  
  
STRIPE CONNECT’S COUNTRY-AND-CURRENCY LOCK-IN  
A Canadian organizer running a US event gets charged FX twice, once converting to CAD to sit in the Connect account, again converting back to USD to pay the creator. When Stripe cannot support a corridor, the creator has to re-onboard elsewhere.  
DIAGNOSTIC  
Today’s topology  
CAPABILITY STACK  
  
LIVE  
  
MISSING  
Payouts  
Subscriptions  
Tokenization  
Fraud  
KYC/KYB  
SOME ALTERNATIVE PAYMENT METHODS YOU ARE NOT OFFERING  
  
Pix · ð§ð· Brazil  
  
Boleto · ð§ð· Brazil  
  
OXXO · ð²ð½ Mexico  
  
SEPA Direct Debit · ð©ðª Germany  
  
Bizum · ðªð¸ Spain  
  
Satispay · ð®ð¹ Italy  
  
Interac · ð¨ð¦ Canada  
  
PayTo · ð¦ðº Australia  
  
Open Banking · ð¬ð§ United Kingdom  
  
Klarna · ðªðº Europe  

-----

-----

HOW EVENTBRITE RUNS PAYMENTS TODAY  
Eventbrite’s payment stack is scattered across six processors,  
and card-only checkout leaves local volume on the table  
GLOBAL CARDS AS THE CORE RAIL  
Visa, Mastercard and Amex carry most online volume across all ten core markets, split across six processors. None of them routes to another when one declines.  
DEPENDENT ON PROCESSOR COVERAGE  
Local method availability is whatever each processor supports, so the catalogue is set by six vendor roadmaps rather than by what a market checks out with.  
APM INTEGRATION OPPORTUNITY  
Ten dominant rails are unavailable: Pix, SPEI, OXXO, Interac, Bizum, Satispay, PayTo, SEPA Direct Debit, Open Banking and Cartes Bancaires.  
RESERVE AND PAYOUT TIMING  
A 20% reserve is held until after the event, then the creator waits three to five business days. Onboarding is tied to the processor that served the market.  
Source Provider topology from the shared payments review. Reserve, payout timing and cost statements from Eventbrite FY2025 Form 10-K, filed 12 March 2026. Method availability compiled from public market data, August 2026.  
  
The lever — connect the dominant rail in each market and route across the six processors on live performance. On the modeled split that is $74.6M of incremental gross ticket sales and $7.2M of net revenue, before any change to pricing or to the existing provider mix.  
6  
Processors live,  
zero routing between them  
  
20%  
Of net sales reserved  
until after the event  
  
10  
Dominant local  
rails not offered  
˜8%  
Net revenue year  
over year, 2025  
PAYMENTS TODAY, IN FOUR NUMBERS  
  

-----

-----

  
  
The Proposed Model  
03  

-----

-----

THE PROPOSED MODEL  
Six rails already exist. A pay-in-only orchestrator still leaves payouts exactly where they are.  
“Eventbrite already runs six rails in parallel. What’s missing isn’t another processor, it’s orchestration that spans pay-in and payout together.”  
Gap stays open  
Partly closed  
Closed  
THE GAP  
Where the current setup breaks  
TODAY  
Six rails, self-built  
OPTION A  
\+ a pay-in orchestrator  
OPTION B · RECOMMENDED  
\+ Yuno orchestration  
  
Local methods missing  
Pix, Boleto, OXXO, SEPA Direct Debit, Bizum, Klarna  
  
Limited to what each of the six rails supports natively. A new market means a new integration.  
  
Adds method coverage, but only on the pay-in side. Payout for those methods still runs separately.  
  
Full local method depth per market, pay-in and payout together, through one API.  
  
Six rails, no routing or failover  
Stripe, Braintree, Authorize.net, Adyen, Wells Fargo, Mercado Pago run in parallel  
  
Self-built failover only. No routing conditions and no smart retries.  
  
Adds routing and failover across the rails it connects to. Payout stays a separate system.  
  
Smart routing, cascading failover and retries across all six rails, one control plane.  
  
Pay-in ↔ payout ledger  
Collusion fraud tracing, LatAm entity payouts, 12,000+ creators  
  
No system links pay-in data to payout data. Collusion gets caught manually, after the fact.  
  
Out of scope  
  
One ledger ties every pay-in to its payout, across every rail, including the LatAm entities being exited.  
  
Creator onboarding & FX  
Creator verification for payouts, and currency conversion on cross-border events  
  
KYC owned by the processor; double FX on cross-currency events  
  
Onboarding stays with the processor  
  
Portable KYC/KYB owned by Eventbrite; one conversion per payout.  
  
LatAm entities, one more portal  
Brazil, Argentina, Mexico, Colombia via EBANX (potentially) and Braintree  
  
EBANX reachable only through Braintree, no unified reporting, its own portal to manage.  
  
Adds another integration, and likely another portal. No path out of the funds flow.  
  
One dashboard across every rail and every MoR partner, with a path to exit the LatAm entities.  
Gaps closed  
0 of 5  
1 of 5 narrowed  
5 of 5  
Option A adds a second integration and narrows the pay-in gaps.  
Option B adds one integration and closes all five, pay-in and payout together, while keeping every rail Eventbrite runs today live.  
Source: Eventbrite call, August 4, 2026 (Paul Pasion); Eventbrite FY2025 Form 10-K, filed 2026-03-12 (SEC).  

-----

-----

  
$74.6M  
incremental GTS modeled  
\+12%  
auth. uplift  
20-30%  
decline recovery  
No Migration  
Six rails stay live and direct; Yuno orchestrates on top of them: no re-integration, no cutover window, nothing to rebuild.  
No Downtime at the On-Sale  
No re-integration means no cutover window: on-sales never stop selling.  
Ramp by traffic Split  
Shadow mode → 10% of volume → scale by market. Each step is a dashboard setting, reversible in one click.  
Pay-ins  
Payouts  
  
\`  
  
LEDGER  
RISK CONDITIONS  
  
RECONCILIATIONS  
  
INSIGHTS  
  
SMART ROUTING  
  
CHECKOUT BUILDER  
  
PAYOUTS  
  
FRAUD & RISK  
  
TOKENIZATION  
  
CONNECTORS  
  
LIVE TODAY  
UNLOCKED DAY ONE  
Yuno becomes Eventbrite's payment ledger: pay-ins and payouts orchestrated on one layer   
THE PROPOSED MODEL  
  

-----

-----

  
MODULAR DESIGN  
Every module activates standalone,  
and nothing obliges Eventbrite to take the bundle  
  
↗  
MODULE  
PAY-IN ORCHESTRATION  
Routing and retries across every connected provider.  
  
↗  
MODULE  
PAYMENT METHODS  
More than 1,000 local methods on the same integration.  
  
↗  
MODULE  
PAYOUTS  
Creator disbursement by bank, card or wallet, per market.  
  
↗  
MODULE  
KYC AND KYB  
Portable onboarding, owned by Eventbrite rather than a processor.  
  
↗  
MODULE  
FRAUD  
Screening on both sides of the marketplace loop.  
  
↗  
MODULE  
RECONCILIATION  
One ledger across every rail, matched back to transactions.  
  
↗  
MODULE  
TOKENIZATION  
A PSP-agnostic vault, so cards stay valid when a rail changes.  
  
↗  
MODULE  
MOR NETWORK  
More than 90 local entities on tap, market by market.  
  
PROVIDER   
LAYER  
\+460 &#11;integrations  
  
all under one API, one contract and one dashboard.  

-----

-----

  
Pay-in routing, as deep as Eventbrite wants it  
THE ROUTE DECISION  
Condition-based routes on card type, amount, currency, payment origin and BIN range.  
Smart Routing AI optimizing for conversion and cost, or conversion and latency.  
Cascading by outcome, with chained steps for succeeded, pending, declined and error.  
Percentage splits across connections, for partial manual control.  
Risk profiles as gates inside the route: fraud screening, 3DS, block and allow lists, velocity rules.  
Post-authorization steps for risk review or settlement, plus no-code editing on published routes.  
WHAT IT UNLOCKS  
  
01  
SMART RETRY ECONOMICS  
Retry only when the expected recovery beats the scheme fees, rule based per decline code and market.  
  
02  
INTERCHANGE PLUS VISIBILITY  
Transaction-level data surfaces downgrades and the patterns behind them.  
  
03  
NO-CODE CONTROL  
Routes and cascades are edited from the dashboard, without a deploy. Payment ops owns the logic, not a backlog.  
  
MODULAR DESIGN  
  

-----

-----

  
MODULAR DESIGN  
Payout routing, the same discipline on the creator side  
A payout follows the same three steps every time, then lands on whichever rail the creator prefers in their market.  
THE FLOW, EVERY PAYOUT  
  
01  
PAYOUT REQUEST  
Raised the moment the event settles, or on the creator’s own schedule.  
→  
02  
KYC AND KYB GATE  
Beneficiary verified once, then reused across every payout that follows.  
→  
03  
PROVIDER SELECTION PER PAYOUT  
Routing picks the provider per market and method, with no limit on the records in a request.  
THE EXIT RAILS, CREATOR CHOICE  
↗  
Local bank transfer  
Directly into local bank accounts, in the creator’s preferred currency.  
↗  
Card, via referenced payouts  
Pays out to the card used in the original payment by referencing that transaction. Eventbrite never touches card data.  
↗  
Wallets  
Where creators already hold balances, with states and notifications in real time.  

-----

-----

  
  
Why Yuno?  
04  

-----

-----

  
YOUR 360° PARTNER FROM DAY ONE  
Everything you run today,  
everything you’re missing tomorrow,  
on one platform  
YOUR 6 PSPS / ACQUIRERS ALREADY LIVE IN YUNO  
All six rails are already integrated and carrying volume for other Yuno merchants; nothing needs to be built to start  
EVERY ADDITIONAL PAYMENT PARTNER IN JUST ONE CLICK  
Adding a provider stops being an engineering project: pick it from the catalogue, plug in credentials, and route volume to it the same day  
PAY-INS & PAYOUTS LEDGER IN ONE SINGLE PLATFORM  
Yuno orchestrates both sides of the marketplace on one platform, with a single ledger tracing every pay-in to its payout across every rail  
Pay-ins  
Payouts  
  
\`  
  
LEDGER  
RISK CONDITIONS  
  
RECONCILIATIONS  
  
INSIGHTS  
  
SMART ROUTING  
  
CHECKOUT BUILDER  
  
PAYOUTS  
  
FRAUD & RISK  
  
TOKENIZATION  
  
CONNECTORS  
  
LIVE TODAY  
UNLOCKED DAY ONE  

-----

-----

  
  
THE YUNO STORY  
Today, Yuno is proven global payment infrastructure  
  
$30B+  
ANNUAL TPV  
PROCESSED  
  
150+  
ENTERPRISE  
MERCHANTS  
  
1,000+  
PAYMENT  
CONNECTIONS  
190+  
COUNTRIES WITH  
TRANSACTIONS  
  
BACKED BY THE WORLD’S MOST ESTEEMED INVESTORS  
Happy Easter  

-----

-----

  
01  
Route & recover  
ORCHESTRATION  
02  
Convert everywhere  
CHECKOUT & SDKS  
03  
Protect every card  
SECURITY & RISK  
04  
The brain  
AI & INTELLIGENCE  
  
ABOUT YUNO · PLATFORM  
A complete suite · Four pillars · One brain  
460+  
INTEGRATIONS  
190+  
COUNTRIES  
1,000+  
METHODS  
180+  
CURRENCIES  
Orchestration engine  
Pay-in, payouts, tax, KYC/KYB, fraud and reconciliation on one control plane.  
Smart routing  
Per-transaction decisioning.  
Monitors & auto-failover  
Checkout stays live, always.  
Customizable checkout  
  
Local methods, native feel.  
Subscription management  
  
Recurring, with less engineering.  
Mobile SDKs  
One interface, iOS + Android.  
PCI Vault Tokenization  
  
Stay valid across networks.  
3DS authentication  
  
Reduce fraud, lift auth.  
  
Account updater  
  
Credentials always fresh.  
  
Network tokens  
  
Lower scheme fees, higher approvals.  
  
Analytics  
  
Fees, FX, approvals. Decision-ready.  
Reconciliation  
  
One ledger across every PSP.  
Payments Concierge  
  
Natural-language copilot  
for payments ops.  

-----

-----

  
WHY YUNO?  
Our global presence  
INCLUDES OFFICES IN  
San Francisco  
Madrid  
New York  
Oporto  
Miami  
Paris  
Mexico City  
London  
Bogotá  
Warsaw  
São Paulo  
Dubai  
Buenos Aires  
Doha  
Shanghai  
Singapore  

-----

-----

  
WHY YUNO?  
Yuno is trusted by leading   
companies worldwide  

-----

-----

World-class, merchant-first team built by global payment operators  
  
YUNO  
FOUNDERS  
Juan Pablo Ortega  
CO-FOUNDER & CEO  
ðºð¸ USA  
Co-founder of Rappi  
Julián Nuñez  
CO-FOUNDER  
ð¨ð´ Colombia  
Ex-Rappi (Founding team)  
LEADERSHIP TEAM  
  
Justo Benetti  
CRO  
ð¦ð· Argentina  
Led dLocal’s enterprise integrations&#11;across LATAM  
Edwin Poot  
CTO  
ð³ð± Netherlands  
20+ years of experience in  
tech transformation  
Mauricio Schwartzmann  
CHIEF BANKING & FI  
ð²ð½ Mexico  
Former Country Manager at Mastercard  
Mexico; former CEO of RappiBank  
Walter Campos  
GM LATAM  
ð§ð· Brazil  
20+ years in LATAM payments at  
Mercado Pago and Cielo  
  
Chee Beh  
GM APAC  
ð¸ð¬ Singapore  
20+ years in payments; ex-Director of&#11;Payments APAC at Uber, ex-J.P. Morgan  
Martin Mexia  
SVP, PRODUCT  
ð¦ðª UAE  
12+ years in fintech product &#11;(Revolut, Rappi); founder of Payit  
Bernabe Murata  
HEAD, GTM  
ð¦ð· Argentina  
10+ years in fintech; former Director&#11;of Relationship Management at Worldpay  
Rik Ter Beek  
VP, ENGINEERING  
ð³ð± Netherlands  
20+ years in payments; former  
Head of Integrations Engineering at Adyen  
WHY YUNO?  

-----

-----

WHY YUNO?  
A dedicated team for Eventbrite across every region  
  
MARKETING & PARTNERSHIPS  
APM partnerships  
Drive adoption  
\+ commercial promotions.  
Co-marketing with each APM (Pix, UPI, BLIK, GCash, iDEAL…)  
Priority placement and badge inclusion in APM apps  
Joint campaigns and promotional rates per region  
Direct fee + commercial negotiations with each PSP  
  
Embedded with  
30+ local apms  
  
TECHNICAL ACCOUNT MGMT  
TAM team  
Day-to-day platform health&#11;+ decline analysis  
BIN-level decline analysis and routing optimization  
Issuer escalations on stuck and high-risk transactions  
Continuous tuning of retry logic and fallback paths  
Real-time dashboards and weekly business reviews  
  
Same-timezone coverage across all regions  
  
SALES ENGINEERING  
Solutions engineers  
Implementation&#11;+ integration partner  
Direct integration support (single API, all PSPs)  
Per-market go-live runbook and migration support  
Custom checkout flow tuning per geography  
Sandbox, monitoring, and reconciliation setup  
  
On-call during launches in every market  
  
KEY ACCOUNT MGMT  
Strategic KAM  
Strategic partner&#11;+ commercial QBRs  
Single point of contact across all regions  
QBRs on funnel performance and market expansion  
Net new market entry sequencing and prioritization  
Executive escalation owner for any platform issue  
  
Senior owner aligned to Eventbrite’s roadmap  
  
REGIONAL PRESENCE  
Local teams across the Americas, EMEA and APAC  
São Paulo · Mexico City · San Francisco · New York · Bogotá · Buenos Aires · Madrid · London · Paris · Dubai · Singapore · Mumbai · Manila  
Source: Yuno commercial commitment to Eventbrite; team structures dedicated upon contract signing  

-----

-----

  
  
The Marketplace Case  
05  

-----

-----

MARKETPLACE & PLATFORM PAYMENTS  
  
One recipient model.  
Every acquiring rail.  
Onboard sellers once, route across providers, split or disburse on your terms, and reconcile it all in one layer — with a single answer to whether each seller can actually be paid.  
  
1  
RECIPIENT  
OBJECT  
  
N  
CONNECTIONS  
PER RECIPIENT  
  
2  
MONEY-MOVEMENT  
MODELS  
  
4  
NORMALIZED  
CAPABILITIES  

-----

-----

THE MODEL  
Recipients, connections, capabilities  
The marketplace is the organization. Accounts underneath it carry connections to providers. Sellers are recipients — and each recipient links to one or more connections, with independent onboarding status per provider.  
  
MARKETPLACE ORGANIZATION  
  
RECIPIENTS  
CAPABILITIES  
SPLIT CONFIG  
TRANSFERS  
PAYOUTS  
EVENTS  
ONE RECIPIENT → MANY CONNECTIONS  
STRIPE  
CONNECT  
ADYEN FOR PLATFORMS  
PAYPAL MULTIPARTY  
J.P.  
MORGAN  
01  
Recipient. One record per seller: identity, entity type, documents, legal representatives, withdrawal methods, split configuration.  
02  
Onboarding per connection. The same seller can be onboarded to two providers at once, each with its own status and requirements.  
03  
Capabilities. A normalized answer to “can this seller take payments, and can they be paid out?” with the provider’s own remediation reason attached.  
04  
Money movement. Split at authorization, or disburse from balance independently of any payment.  
05  
Events. One webhook contract for onboarding lifecycle and transfer status, across every rail.  
06  
Reconciliation. Provider settlements matched back to transactions, with discrepancies surfaced in reporting.  

-----

-----

MONEY MOVEMENT  
The route out of the flow of funds  
A platform that collects the full order holds other people’s money — with the licensing, safeguarding and regulatory weight that follows. The marketplace model removes that: the provider funds the event owner directly, into the account established during onboarding, and the platform receives only what it is owed.  
  
MODEL A · PLATFORM COLLECTS  
Collect, hold, disburse  
The platform takes the full order, holds it, and instructs a disbursement to each seller later — a standalone transfer, decoupled from any payment.  
· Fits reserve, hold and post-event release rules  
· Forward and reverse as separate audited transactions  
· But: the platform is holding funds owed to sellers  
  
MODEL B · PROVIDER FUNDS THE SELLER  
Split at authorization  
The payment divides at capture. The provider settles the seller’s share straight into the account created at onboarding, and routes the platform’s commission to the platform. The platform never holds the seller’s money.  
· Platform receives its commission, not the gross  
· Per-leg processing-fee and chargeback liability  
· Requires KYC/KYB at onboarding  
· Provider funds a verified party  
PCI DSS LEVEL 1  
·  
SOC 2 TYPE 2  
·  
ISO 27001  
·  
ISO 27701  
·  
GDPR  
·  
VISA-LISTED SERVICE PROVIDER  
  
Neither of us needs to be in the flow of funds. Yuno holds no balances and moves instructions, not money — and under the marketplace model neither does the platform. Settlement runs provider-to-seller and provider-to-platform, which removes the safeguarding, licensing and regulatory exposure that comes with holding funds on someone else’s behalf.  

-----

-----

NORMALIZATION  
One capability model, five dialects  
Every provider has a different way of saying “this seller can be paid.” Yuno resolves them to four capabilities and four statuses, with the provider’s own remediation detail preserved underneath.  
NORMALIZED BY YUNO  
WHAT EACH PROVIDER CALLS IT  
YUNO  
STRIPE  
ADYEN  
PAYPAL  
BRAINTREE  
J.P. MORGAN  
  
payments  
  
charges\_enabled  
  
receiveFromPlatformPayments  
  
payments\_receivable  
  
Sub-merchant active  
  
Client APPROVED  
  
payouts  
  
payouts\_enabled  
  
sendToTransferInstrument  
  
Bank linked  
  
Disbursement enabled  
  
Payout eligibility  
  
send\_transfers  
  
transfers  
  
sendToBalanceAccount  
  
Platform fee sweep  
  
Escrow release  
  
Account-to-account  
  
receive\_transfers  
  
transfers  
  
receiveFromBalanceAccount  
  
Seller receipt  
  
Sub-merchant credit  
  
Limited account credit  
  
Seller construct  
  
Connected account  
  
Account holder + balance account  
  
Merchant via referral  
  
Sub-merchant  
  
Client with Limited DDA  
  
Split mechanism  
  
application\_fee\_amount  
  
Typed splits\[\]  
  
platform\_fees\[\]  
  
serviceFeeAmount  
  
Ledger allocation  
  
Remediation detail  
  
Error codes + reasons  
  
remediatingActions  
  
Status flags  
  
Limited  
  
Documents + attestations  
Status  
Live  
Live  
In build  
Base connector live  
—  
Normalized statuses: ACTIVE · PENDING · INACTIVE · REJECTED Requirements carry the provider response code, field, message and CURRENTLY\_DUE state per capability.  

-----

-----

  
  
WHAT THAT LOOKS LIKE  
The answer to “can this seller be paid?”  
"capabilities": {  
  "payments": {  
    "status": "ACTIVE",  
    "requirements": \[\]  
  },  
  "payouts": {  
    "status": "PENDING",  
    "requirements": \[{  
      "provider\_response\_code": "2\_8019",  
      "provider\_response\_field":  
        "withdrawal\_methods.bank",  
      "message": "withdrawal\_methods.bank  
        currently required",  
      "status": "CURRENTLY\_DUE"  
    }\]  
  },  
  "send\_transfers": { "status": "ACTIVE" },  
  "receive\_transfers": { "status": "ACTIVE" }  
}  
Identical shape on every rail, including the ones added after  
WHY THIS IS THE HARD PART  
A seller isn’t binary. They can take payments but not receive payouts. They can be live today and blocked tomorrow because an acquirer pulled a capability. They can be verified on one rail and pending on another.  
Without normalization, every one of those states is provider-specific code in your platform — and every new rail multiplies it.  
With it, your product asks one question and gets one answer, and the remediation text you show a seller comes from the provider that actually raised it.  
Existing sellers carry over. A seller already onboarded with a provider is registered as PREVIOUSLY\_ONBOARDED — supply the provider’s recipient ID and they are active immediately. No re-onboarding of an existing base.  

-----

-----

ONBOARDING & KYC  
Three ways in, one lifecycle out  
  
TYPE 1  
Previously onboarded  
Seller already exists with the provider. Supply their ID and status is SUCCEEDED immediately. This is the migration path for an existing base.  
  
TYPE 2  
One-step  
Basic information captured up front, with verification triggered on submission.  
TYPE 3  
Two-step  
Initial creation, then Continue Onboarding for documents, KYC/KYB and bank instrument — including provider-hosted flows.  
STANDALONE KYC / KYB  
One submission, every provider  
Yuno submits a single onboarding request to as many providers as that seller needs, at the same time — a business in one market, an individual in another, two acquirers for redundancy — and normalizes what comes back into one set of statuses and one requirements array, whatever raised it. Yuno is a pass-through, not a store of record: verification data goes to the providers required to hold it and who perform the checks. What we keep is the state — so a provider refusing to share KYC with another stops being your integration problem.  
Hosted flows where the provider offers them, so KYC capture never touches your systems  
Migration via onboarding transfer and reverse-transfer, with traceable history  
Block, unblock and cancel gate a seller at payment time, not just in reporting  
Push events, not polling  
ONE EVENT CONTRACT  
  
ONBOARDING.CREATED  
  
ONBOARDING.BLOCKED  
  
ONBOARDING.PENDING  
  
ONBOARDING.UNBLOCKED  
  
ONBOARDING.SUCCEEDED  
  
ONBOARDING.EXPIRED  
  
ONBOARDING.DECLINED  
  
ONBOARDING.TRANSFERRED  
  
ONBOARDING.CANCELLED  
  
ONBOARDING.INACTIVE  
  
ONBOARDING.ERROR  
  
TRANSFER.TRANSFER  

-----

-----

  
SPLITS, FEES AND LIABILITY  
Distribute funds without distributing risk  
"split\_marketplace": \[  
  { "type": "PURCHASE",  
    "recipient\_id": "…",  
    "amount": { "value": 5400, "currency": "USD" },  
    "liability": {  
      "processing\_fee": "MERCHANT",  
      "chargebacks": true  
    }  
  },  
  { "type": "COMMISSION",  
    "amount": { "value": 600, "currency": "USD" },  
    "liability": {  
      "processing\_fee": "RECIPIENT",  
      "chargebacks": false  
    }  
  }  
\]  
Liability is assigned per leg, not per transaction  
  
THE CONTROL THAT MATTERS  
A zero-value leg can carry chargeback liability. The platform stays responsible for disputes without taking a share of the transaction — running in production today on a live marketplace.  
  
AUTO SPLIT CONFIGURATION  
Commission rules live on the recipient — percentage, fixed or mixed, with bankers’, round-up or round-down modes. Omit the amount on the payment and Yuno calculates it. Per-seller terms configured once.  
  
REFUNDS AND REVERSALS  
Split-aware refunds reverse the original distribution; transfer reversal claws funds back at payment or recipient level. Chargeback debits follow the liability assignment.  

-----

-----

RECONCILIATION & REPORTING  
Settlements matched back  
to transactions  
The reconciliation engine cross-matches what each provider says it settled against what actually went through Yuno — so finance sees one view across every rail rather than one file per provider.  
  
01  
INGESTION  
Every provider  
Settlement files collected by API, SFTP, storage bucket or email — normalized into one schema regardless of source format.  
02  
MATCHING  
Two rules  
Matched by transaction identifier, and by card BIN where identifiers don’t carry through. Discrepancies raise corrective actions.  
03  
DELIVERY  
On demand  
Generated on request and delivered by secure link, with report webhooks when output is ready.  
BOTH DIRECTIONS, NOT JUST PAY-IN  
  
PAY-IN  
Every transaction reconciled against what the provider reported settling, with exceptions flagged rather than absorbed. Fee detail per transaction, per provider.  
  
PAY-OUT  
Every disbursement tracked as its own audited object — forward and reverse separately — queryable per recipient and per onboarding, with status events on change.  
  
Why both matters for a marketplace: a platform’s close depends on tying three things together — what buyers paid, what the provider settled, and what went out to sellers. Reconciling only the pay-in leg leaves the payable to your sellers unreconciled, which is usually the larger number on the balance sheet.  

-----

-----

IN PRODUCTION  
Marketplaces running on this today  
LIVE-ENTERTAINMENT TICKETING   
150+ CITIES · ES · MX · US · GB · AR · QA  
Fever is building on Yuno for its next phase of international growth — purpose-built pipelines in place for its launch markets, certification ramping ahead of go-live. The scope is the whole flow rather than the pay-in alone: corridor-specific acquiring so each market routes to the provider that converts there, smart routing with failover across acquirers, 3DS and fraud screening in the same layer, and pay-out and reconciliation alongside the pay-in instead of in separate provider portals. Same category, same shape of problem — a high-volume ticketing platform going multi-market, where a processor incident during an on-sale is lost revenue rather than a delayed order.  
DONATION PLATFORM · STRIPE + PAYPAL  
Platform collects from donors, splits to non-profit beneficiaries, retains a platform fee. Recipients, onboarding and splits live on Stripe; PayPal Multiparty in build.  
CLASSIFIEDS MARKETPLACE · MULTI-ACQUIRER  
One of Brazil’s largest marketplaces, live in production with marketplace payment orchestration, multi-acquirer redundancy, wallets, local rails and installments.  
CREATOR MARKETPLACE · MULTI-PROVIDER  
Subscription and creator marketplace routing across several providers, with per-seller soft descriptors and recurring credentials handled across rails.  
RETAIL MARKETPLACE · MULTI-LEG SPLITS  
Live multi-leg splits distributing a single order across seller, commission and marketplace legs — including a zero-value leg carrying chargeback responsibility.  

-----

-----

Powering The Future  
of Financial Infrastructure  
World’s Top Fintech Companies  
CNBC and Statista  
\#1 Best Payment API  
The 2025 API Awards  

-----

-----

  
  
Appendix  
06  

-----

-----

Yuno is the global payment partner to scale Eventbrite  
Global payment method coverage and  
leading capabilities for payment routing and orchestration, position Yuno as a best-in-class partner for Eventbrite.  
  
Key Advantages  
1000+ payment methods  
Day-one local coverage  
Higher approvals, lower cost  
Reporting and analytics  
  
APPENDIX  
  

-----

-----

  
APPENDIX  
Selected credentials  
  
↗ WATCH THE VIDEO  
  
Expanded to 11 countries in 8 months, 90% approval rates  
VASILIY EVERSTOV  
Head of FinTech, inDrive  
  
↗ WATCH THE VIDEO  
  
Cuts new provider implementation  
time to zero  
LEONARDO BENANTE  
Global Head of PayIns, Rappi  
  
↗ WATCH THE VIDEO  
  
CAMILO FERREIRA  
Finance Manager, Livelo  
50% transaction recovery, 5% approval uplift  
  
↗ READ THE POST  
JORGE JIMENEZ LEON  
Vice President of Commercial  
and Planning, Wingo  
14% increase in approval rates  

-----

-----

  
APPENDIX  
Payments have become a strategic bottleneck  
that impact the entire organization  
  
“We invest heavily in growth of our customer base, but even a few percentage points of failed payments at checkout erase that growth”  
– Chief Commercial Officer,  
online marketplace  
  
“Whenever a provider goes down, our teams have to be called in the middle of the night to manually resolve the issue and reroute the payments”  
– Chief Operations Officer, equipment manufacturer  
  
“Two acquirers can deliver the same volume with a meaningful gap in a cost, yet we lack the flexibility to optimize routing to take advantage of this”  
– Chief Financial Officer,  
delivery platform  
  
“We apply conservative rules to prevent fraud, which also causes a significant number of legitimate transactions to not go through”  
– Head of Risk,  
retailer  
  
“Every new market adds another payment integration, another failure point, and more operational drag. It slows us down exactly when we want to scale”  
– VP of Engineering,  
global ecommerce company  
  
“We know there’s revenue on the table, but without visibility into routing, costs, and failures, we’re making decisions blind”  
– Head of Payments,  
digital marketplace  
  
“Payments should just work. Instead, our teams spend time firefighting providers instead of improving conversion and customer experience”  
– COO,  
international SaaS platform  

-----

-----

What Yuno unlocks 1/2  
DIMENSION  
YUNO VS A SINGLE PSP/MOR  
WHAT IT IS WORTH  
CAPABILITY/ DIMENSION  
YUNO ORCHESTRATION APPROACH  
SINGLE PSP/MOR APPROACH  
BUSINESS BENEFIT FROM USING YUNO  
SUPPORTING STATS  
  
APPROVAL RATES  
  
Smart routing across multiple acquirers and PSPs with fallback and retries  
  
Single acquirer; limited fallback options  
  
Higher approval rates = more revenue  
  
Multi-acquirer setup boosts approvals by 4–16%  
  
LATENCY & CONVERSION IMPACT  
  
Optimized transaction routing for minimal latency  
  
Latency from fixed routing or distant endpoints  
  
Faster checkout = fewer cart abandonments  
  
100ms delay = 7% drop in conversion (Amazon)  
  
LOCAL PAYMENT COVERAGE  
  
Access to 300+ local/global methods via one integration  
  
Limited methods tied to PSP roadmap  
  
Better conversion via locally relevant methods  
  
8–12% uplift when offering local APMs  
  
GO-TO-MARKET SPEED  
  
Rapid market entry via pre-integrated methods; weeks not months  
  
Slow rollout; new markets require new integrations  
  
Accelerated time to revenue in new markets  
  
Yuno does 20–40 Integrations Monthly  
  
COST OPTIMIZATION  
  
Routes to lowest-cost provider; avoids cross-border fees  
  
Fixed fees; limited cost optimization  
  
Lower transaction costs; higher margins  
  
Domestic routing reduces FX & fees  
  
REDUNDANCY / FAILOVER  
  
Built-in redundancy with auto-failover between PSPs  
  
Single point of failure if PSP is down  
  
Avoid downtime revenue losses  
  
Downtime costs $100K+/hour (Amazon)  
  

-----

-----

DIMENSION  
YUNO VS A SINGLE PSP/MOR  
WHAT IT IS WORTH  
CAPABILITY/ DIMENSION  
YUNO ORCHESTRATION APPROACH  
SINGLE PSP/MOR APPROACH  
BUSINESS BENEFIT FROM USING YUNO  
SUPPORTING STATS  
  
FRAUD MANAGEMENT  
  
Multiple fraud tools + dynamic rules across regions  
  
Single fraud engine; harder to customize  
  
Lower fraud + fewer false declines  
  
False declines cost $443B  
globally (2021)  
  
REPORTING & VISIBILITY  
  
Unified dashboard with real-time global reporting  
  
Fragmented reports; limited real-time data  
  
Faster decisions; less manual work  
  
Reconciliation reduced  
from weeks to hours  
  
ENGINEERING EFFORT  
  
One API for global access; minimal dev overhead  
  
Multiple custom integrations required per PSP  
  
Dev team focused on core product  
  
80%+ of IT teams prefer orchestration, saves c. 80% on development costs  
  
FLEXIBILITY TO TEST/SCALE NEW PSPS  
  
Instantly test/scale PSPs via dashboard; no dev work needed  
  
New PSPs require full integration projects  
  
Continuous optimization and agility  
  
45%+ of merchants cite  
agility as top benefit  
  
NEGOTIATION LEVERAGE  
  
Volume control across PSPs increases fee negotiation power  
  
Locked-in pricing and terms  
  
More favorable processing terms  
  
Orchestration increases leverage  
for fee negotiations  
  
CUSTOMER EXPERIENCE METRICS  
  
Localized, fast, and reliable checkout with preferred methods  
  
Generic experience; more errors and abandoned cart  
  
Higher satisfaction and loyalty  
  
76% abandon carts without  
preferred payment method  
What Yuno unlocks 2/2  
  

-----

-----

Yuno meets or exceeds the compliance requirements  
of the regulated financial institutions globally  
Yuno is certified across security and privacy standards required by Tier 1 global banks, incl. PCI DSS v4.0, SOC 2 Type 2, ISO 27001, ISO 27701, and GDPR  
WHAT THE BANK ASKS  
HOW YUNO ANSWERS IT  
RISK DIMENSION  
PARTNER CONCERN  
HOW YUNO ADDRESSES  
CERTIFICATIONS  
  
DATA SECURITY  
  
Protection of cardholder data across processors  
  
End-to-end encryption for data in transit and at rest. Tokenization of sensitive cardholder data. No PAN storage — tokens replace card numbers across the platform  
  
PCI DSS v4.0 (highest standard in payments) + SOC 2 Type 2 (independently audited controls)  
  
INFORMATION SECURITY MANAGEMENT  
  
Vendor security maturity; ability to pass bank’s vendor audit  
  
Formal Information Security Management System (ISMS) with continuous risk assessment, incident response procedures, and annual external audits  
  
ISO 27001 certified  
  
DATA PRIVACY AND SOVEREIGNTY  
  
Data residency; cross-border data transfer; access controls over merchant data  
  
Data residency configurable per jurisdiction. All analytics use anonymized, aggregated data — no PII leaves the bank's domain. Privacy-by-design architecture aligned with GDPR principles  
  
ISO 27701 certified (privacy management) + GDPR compliant . Data processing agreements customized per bank's regulatory requirements  
  
OPERATIONAL RESILIENCE  
  
Platform availability and failover mechanisms  
  
Infrastructure built on AWS scalable framework. Multi-region failover. 99.99% uptime SLA  
  
AWS-hosted infrastructure with redundancy. Monitoring and alerting with defined RTO/RPO. Detailed incident response and disaster recovery plan  
  
REGULATORY AND LICENSING  
  
Acquiring license ownership; regulatory classification; settlement control  
  
Yuno operates as a technology provider. The bank retains its acquiring license, BIN sponsorship, and regulatory obligations. Yuno does not control settlement or hold funds  
  
Bank remains the regulated entity. Yuno is classified as a technology vendor / service provider. Recognized Visa Service Provider  
  
VENDOR LOCK-IN  
  
Portability of data and contracts  
  
All processor connections remain bank's property. Standard APIs to allow migration. Bank retains all merchant contracts, data, and relationships  
  
No proprietary data formats. Bank owns all merchant data  
  

-----

-----