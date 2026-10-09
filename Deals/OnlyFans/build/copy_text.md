
=== SLIDE 1 (n01_g3f77215683c_1_445) ===
The vault under creator banking
Your credentials, your connections, your rules.
For discussion. October 2026 · Strictly confidential
W W W . Y . U N O
1,000+ PAYMENT OPTIONS   |   180+ CURRENCIES   |   194+ COUNTRIES

=== SLIDE 2 (n02_g3f769a0f446_0_0) ===
Agenda
1
Executive summary
p. 4-8
2
Our proposal: the OF-Yuno Vault
p. 10-20
3
Why Yuno
p. 22-26
4
Timeline and next steps
p. 28

=== SLIDE 3 (n03_g3f769a0f446_0_988) ===
PART 1
Executive summary
The answer in five pages: the need, our proposal, why Yuno and the timeline
CONTENTS
1
Executive summary
The answer in five pages: the need, our proposal, why Yuno and the timeline
p. 4-8
2
Our proposal: the OF-Yuno Vault
Vault, Proxy, and your way of using them
p. 10-20
3
Why Yuno
The Yuno story, clients, platform and the team behind it
p. 22-26
4
Timeline and next steps
From inclusion in the RFP to a live vault
p. 28

=== SLIDE 4 (of_exec_understanding_v2) ===
EXECUTIVE SUMMARY  ›  OUR UNDERSTANDING OF THE CONTEXT
OnlyFans needs to manage creator payouts and expand into creator BaaS
What OnlyFans aims to deliver
Reliable payments to creators, with a broader ambition to offer one account for BaaS, cards and transfers.
What makes this challenging
Delivering this through multiple banks, issuers and transfer providers means coordinating sensitive data, connections and payment decisions. OnlyFans needs control over that setup and flexibility when partners change.
The decision now
OnlyFans is selecting a token-vault provider through the current RFP. That choice should support how credentials will be used across providers, for both creator payouts and future financial services.
What the solution needs to cover / Secure storage, connections to providers and rules OnlyFans controls—so the data can be used to deliver services to creators.
4

=== SLIDE 5 (m5_mock) ===
EXECUTIVE SUMMARY  ›  COMPREHENSIVE VERSUS STANDALONE
Yuno´s vault solution provides comprehensive functionality with far less build resources than standalone option
5
What OnlyFans needs
Standalone vault / Stores the data. The rest is yours to build or buy.
Yuno integrated vault / Stores the data, connects it to providers and runs payments on it.
Basic vault function
PCI DSS Level 1 storage   ·   Tokenisation   ·   Proxy to providers   ·   Portable tokens and contractual exit
Other connections and capabilities
Data in one vault
PARTIAL
Cards and tokens; other data varies by vendor
INCLUDED
Cards, network tokens, bank, identity and tax data in one vault
Provider connections
Additional Build
Each processor and bank connection, built and run in-house
460+ processors and banks already connected
Payment capabilities
Routing, retries, failover and payouts, built in-house
Routing, retries, failover and payouts on rules you set
Additional services
A new vendor and integration for each service
3DS, account updater, payouts and BaaS on the same tokens
Same independence, far less to build.   OnlyFans keeps portable tokens and exit terms, and decides how much of the stack Yuno runs.
Additional Build
Additional Purchase

=== SLIDE 6 (of_vault_proxy_flow_v3) ===
EXECUTIVE SUMMARY  ›  VAULT AND PROXY
Your systems use tokens. The proxy delivers the data providers need.
Credential flow, not funds movement. Card proxy is in beta; broader data and destination coverage to confirm.
6
OPTIONAL
Yuno services
Same tokens, on per use case
Authentication
Optimisation
Payouts
BaaS
Orchestration
Agentic commerce
YOUR SYSTEMS
OnlyFans systems
Store and send tokens only. / No raw card or bank data.
SECURE STORAGE
Yuno Vault
Cards and network tokens / Creator bank, identity / and tax data
SECURE FORWARDING
Yuno Proxy
Swaps tokens for stored / values, then forwards.
APPROVED DESTINATION
Your chosen provider
Receives the data it needs / to process the request.
PCI DSS Level 1
tokens
data
ONLYFANS' CONTROL     You decide who accesses data and which destinations receive it   ·   Allowlisted destinations   ·   Secure transport   ·   Audit trail

=== SLIDE 7 (h7c266de662ba1cf0_35_0) ===
EXECUTIVE SUMMARY  ›  BEYOND THE VAULT
The same platform that holds your credentials can also route your fans' payments, when you want it to
7
FAN PAYMENTS IN · AN OPTION FOR LATER
Orchestration
Routing across several processors by your rules / Automatic failover when a processor degrades / Network tokens and authentication tuned per issuer
No single processor can stop fans paying: the 2021 lesson on the pay-in side.
Live today
CREATOR PAYOUTS OUT · THE RFP DESIGN
BaaS (Banking-as-a-Service) layer
Bank and rail choice by your rules / Payouts by ACH, same-day ACH, wire and RTP / Balances across banks in one view
No single bank can stop creators being paid.
API and rails live
Bank rules proposed
The vault sits under both. Start with the vault; adding orchestration later is configuration, not a new project.

=== SLIDE 8 (es_time) ===
EXECUTIVE SUMMARY  ›  TIMELINE AND NEXT STEPS
From inclusion in the RFP to a live vault: five steps and three decisions, each on your calendar
8
Week of 12 Oct
Get included
Deck to the Payments Manager / Intro call
Late October
Deep dive
Session with your payments team / PCI scope review / Sandbox access
November
Sandbox proof
3 to 4 weeks / Card renews on two processors / Creator on two banks / Export test
[RFP deadline]
RFP response
Written answers to open items / Commercial offer
From Q1 2027
Phase 1 live
Contract / Card migration without re-entry / US vault live
Included in the RFP
Proof criteria met
Vendor selected
Our ask this week: include Yuno in the RFP evaluation. After Phase 1: creator banking across banks, pluggable issuers, then yield, at OnlyFans' pace.
Indicative dates, to align with OnlyFans' RFP calendar.

=== SLIDE 9 (tdiv3) ===
PART 2
Our proposal: the OF-Yuno Vault
Vault, Proxy, and your way of using them
CONTENTS
1
Executive summary
The answer in five pages: the need, our proposal, why Yuno and the timeline
p. 4-8
2
Our proposal: the OF-Yuno Vault
p. 10-20
3
Why Yuno
The Yuno story, clients, platform and the team behind it
p. 22-26
4
Timeline and next steps
From inclusion in the RFP to a live vault
p. 28
2.1  Vault  cards, network tokens and personal data in one store you control
p. 13-17
2.2  Proxy  real values go only where they are needed
p. 18
2.3  Your way  vault on its own, or with Yuno services; and your exit, in the contract
p. 19-20

=== SLIDE 10 (h7c266de662ba1cf0_9_0) ===
2 · OUR PROPOSAL  ›  OF-YUNO VAULT
A secure, scalable vault that you design, for every sensitive recordOnlyFans holds
STEP 1 · CARDS
We built a PCI DSS Level 1 vault for cards.
PAN
network tokens
PAR
STEP 2 · PROXY
Allow merchants to use our vault as a proxy.
detokenisation
STEP 3 · YOUR DESIGN
A unique vault matching you andonly you.
Tokenisation
Encryption
Masked
Clear storage
Compliant out of the box
PCI DSS Level 1
SOC 2 Type 2
ISO 27001
ISO 27701
10

=== SLIDE 11 (h7c266de662ba1cf0_9_33) ===
2 · OUR PROPOSAL  ›  WHAT IT DOES
One vault that stores, connects and controls every sensitive record, forpay-in and for payouts
STORE
Yuno Vault
PCI DSS LEVEL 1
Fan cards, network tokens and PAR
Creator bank accounts
Identity Documents
Any other data points you define
CONNECT
Proxy to your processors and acquirers
Proxy to banks, card issuers and transferproviders
Proxy to KYC and tax services
Yuno routing, payouts and banking when you wantthem
CONTROL
Schema andencryption chosenper column
Access per table,for people and forservices
Retention anderasure, recordby record
An audit record onevery call
Import in, exportout, networktokens inyour name
Deployed in theAWS or GCP regionyou choose
11

=== SLIDE 12 (h7c266de662ba1cf0_9_563) ===
2 · OUR PROPOSAL  ›  WHERE IT RUNS
A local vault at global scale: data staysin the region you choose, paymentmethods stay local
WHAT YOU GET
AWS · India
One schema · one API · one set of access rules
Data residency set by your policy and by each regulator
The same vault design in every region
Local payment methods for fans and creators, next to the data
190+
COUNTRIES
1,000+
PAYMENT METHODS
12

=== SLIDE 13 (h7c266de662ba1cf0_9_85) ===
2 · OUR PROPOSAL  ›  VAULT  ›  THE PROBLEM
As we understand it, fan cards live with your processor and creator datalives in your own systems
BEFORE
Data in two places
Processor
holds the fan's card
OnlyFans systems
hold the creator's data
Fan cards are locked to the processor that stores them
Two systems to secure and audit
A new bank or issuer means collecting creator details again
OnlyFans Privacy Policy: “We do not receive your full payment cardnumber.” Read 8 Oct 2026.
Fan cards
Bank accounts
ID documents
Tax records
AFTER
One vault
Cards work on any processor you connect
One vault to secure and audit
Creator details collected once and reused
Processors
SWAPPABLE
Banks
SWAPPABLE
Card issuers
SWAPPABLE
Yuno Vault
Cards
Bank accounts
ID documents
Tax records
…
13

=== SLIDE 14 (h7c266de662ba1cf0_9_140) ===
2 · OUR PROPOSAL  ›  VAULT  ›  WHAT IT IS
One PCI DSS Level 1 vault with three stores: cards, network tokens andpersonal data
/
Vault
/
Schema
Production
Tables
Search columns
Filter
+ New table
Protection is set per column. In this live demo, legal_name can be changed by clicking its badge.
cards
PCI
id
uuid
fan_id
→ fans
pan
•••• 0193
Tokenized
expiry
••/27
Masked
holder_name
•••• ••••
Encrypted
network_tokens
PCI
card_id
→ cards
network
VISA
token
•••• 7740
Tokenized
par
V001••••••••8F2
network_transaction_id
Encrypted
creator_records
PII
creator_id
cr_8812
legal_name
•••• ••••
Encrypted
date_of_birth
••/••/••••
Encrypted
tax_id
•••• 6789
Tokenized
id_document
tok_71c0••••
Tokenized
14

=== SLIDE 15 (h7c266de662ba1cf0_9_207) ===
2 · OUR PROPOSAL  ›  VAULT  ›  NETWORK TOKENS
Network tokens and PAR sit next to the card, so one fan stays one fanacross every credential
PAN
•••• 0193
PAR
Payment AccountReference
Network token · card on file
•••• 7740 · network transaction ID 3812•••••••2210
Network token · Apple Pay
•••• 2215
Reissued card
PAN •••• 5521 · same PAR
One fan across card, wallet and reissue: for chargebacks, bansand subscriptions.
Token requestor ID registered under OnlyFans where the schemeallows it. Yuno acts as TS-TRP.
15

=== SLIDE 16 (h7c266de662ba1cf0_9_241) ===
2 · OUR PROPOSAL  ›  VAULT  ›  SCHEMA
You define the tables, the columns, how each one is protected and howlong it lives
TABLES
cards
PCI
network_tokens
PCI
creator_records
PII
+ New table
COLUMN
TYPE
CLASS
PROTECTION
RETENTION
payout_methods
PCI
PII
payout_methods
PCI
PII
one table, two classifications
method_type
enum
—
Clear
7 years
account_number
string
PII
Tokenized
7 years
routing_number
string
PII
Encrypted
7 years
card_pan
string
PCI
Tokenized
7 years
card_expiry
string
PCI
Masked
7 years
account_holder
string
PII
Encrypted
7 years
mandate_id
string
—
Clear
Life of account
+ Add column
16

=== SLIDE 17 (h7c266de662ba1cf0_9_316) ===
2 · OUR PROPOSAL  ›  VAULT  ›  ACCESS
Access is set per table and per role, for people and for services
ROLE
cards
network_tokens
creator_records
PEOPLE
Creator support
Masked
None
Masked
Compliance
None
None
Read
Engineer
None
None
None
Auditor
Export
Export
Read
SERVICES
Checkout andrebills
Detokenize
Detokenize
None
Payouts
None
None
Detokenize
Onboarding
None
None
Write
ACCESS LOG
Today
Checkout · service
Allowed
detokenize cards.pan
09:41
Creator support · person
Allowed
read creator_records.legal_name · masked
09:38
Engineer · person
Denied
read cards.pan
09:35
Payouts · service
Allowed
detokenize payout_methods.account_number
09:30
Compliance · person
Denied
export cards
09:27
Auditor · person
Allowed
export network_tokens
09:21
Onboarding · service
Allowed
write creator_records
09:12
17

=== SLIDE 18 (h7c266de662ba1cf0_9_391) ===
2 · OUR PROPOSAL  ›  PROXY  ›  HOW IT WORKS
You build the request your provider expects and mark the tokens. Theproxy fills in the real values
OnlyFans system
builds the request
Yuno Proxy
swaps tokens for vault values
Your provider
receives the real values
As OnlyFans sends it
ILLUSTRATIVE
POST /v1/pci-proxy/forwardyuno-proxy-destination-url:  https://provider.example/v1/charges{  "amount": 1499,  "currency": "USD",  "card": {    "number": "{{vaulted_token.9f2a….network_token}}",    "expiry": "{{vaulted_token.9f2a….expiration}}"  },  "initial_transaction_id":    "{{vaulted_token.9f2a….network_transaction_id}}"}
As the provider receives it
ILLUSTRATIVE
POST https://provider.example/v1/charges{  "amount": 1499,  "currency": "USD",  "card": {    "number": "4895 •••• •••• 7740",    "expiry": "09/29"  },  "initial_transaction_id": "3812•••••••2210"}
18

=== SLIDE 19 (h7c266de662ba1cf0_9_421) ===
2 · OUR PROPOSAL  ›  YOUR WAY  ›  OPTIONS
Use the vault on its own, or add Yuno services on the same tokens
OPTION A
Vault only
Vault and Proxy
Yuno stores and forwards. You keep everything else.
Your processors
Reached through the proxy, in the request format each oneexpects
Your banks
Payout rails you already hold: ACH, wire, RTP
Your logic
Routing, retries and failover stay in your stack
Add a service.No token moves.
OPTION B
Same vault, same tokens
Vault and Yuno services
Everything in A, plus the services below, switched on per usecase.
+ Add a service
Routing and failover
across 460+ integrations
Payouts
to creators, by API
Banking connectivity
entities, accounts, ACH,wire, RTP
Network tokens and accountupdater
Authentication
3DS, passkeys
Yuno Vault
The same tokens under both options
PCI DSS LEVEL 1
19

=== SLIDE 20 (h7c266de662ba1cf0_9_469) ===
2 · OUR PROPOSAL  ›  YOUR WAY  ›  PORTABILITY
Your tokens and your exit, written into the contract
PROCESSORS
Switch processor, keep the cards
Cards and network tokens are stored once and forwarded to any of460+ processors through the proxy. A migration is a routing change,not a re-collection.
Yuno Vault
Stripe
Adyen
dLocal
PayPal
Checkout.com
Worldpay
Nuvei
Airwallex
+450 more
VAULT
Leave Yuno, keep the tokens
VAULT EXPORT
Exit terms are part of the contract, so the price of leaving is knownbefore you sign.
Network tokens
Registered under OnlyFans' token requestor IDwhere the scheme allows it, so they survive achange of processor or of vault. Nore-tokenization on exit.
01
A written request from OnlyFans
02
The recipient's PCI DSS attestation
03
A PGP-encrypted file delivered over SFTP
20

=== SLIDE 21 (tdiv4) ===
PART 3
Why Yuno
The Yuno story, clients, platform and the team behind it
CONTENTS
1
Executive summary
The answer in five pages: the need, our proposal, why Yuno and the timeline
p. 4-8
2
Our proposal: the OF-Yuno Vault
Vault, Proxy, and your way of using them
p. 10-20
3
Why Yuno
The Yuno story, clients, platform and the team behind it
p. 22-26
4
Timeline and next steps
From inclusion in the RFP to a live vault
p. 28

=== SLIDE 22 (h7c266de662ba1cf0_9_588) ===
3 · WHY YUNO  ›  THE YUNO STORY
Today, Yuno is proven global payment infrastructure
$100B+
ANNUAL TPV PROCESSED
150+
ENTERPRISEMERCHANTS
1,000+
PAYMENT CONNECTIONS
190+
COUNTRIES WITHTRANSACTIONS
BACKED BY THE WORLD'S MOST ESTEEMED INVESTORS
22

=== SLIDE 23 (h7c266de662ba1cf0_9_611) ===
3 · WHY YUNO  ›  CLIENTS
Yuno is trusted by leading companies worldwide
23

=== SLIDE 24 (n28_g3f769a0f446_0_7028) ===
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
3 · WHY YUNO  ›  ABOUT YUNO  ›  PLATFORM
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
Natural-language copilot / for payments ops.
24

=== SLIDE 25 (h7c266de662ba1cf0_0_3) ===
3 · WHY YUNO  ›  TEAM
Run by builders from top payments companies
Juan Pablo Ortega
Co-Founder & CEO · US
Previously Co-founderof Rappi
YUNO FOUNDER
Antoine Cathelin
Head of Trust & Vault · NL
10 years in card-not-presentpayments; leads Trust &Vault at Yuno
YOUR LEAD
Justo Benetti
CRO · US
Led enterprise integrations atdLocal across LATAM
Mauricio Schwartzmann
Chief Financial Services Officer· MX
Former CM Mexico atMastercard, CEO of RappiBank,MD at Citi
Walter Campos
GM LATAM · BR
20+ years in LATAM paymentsat MercadoPago and Cielo
Chee Beh
SVP & GM APAC · SG
20+ years across JPMorgan,Uber, NTT Data, TSYS
Edwin Poot
CTO · NL
Former VP Product &Technology at Nubank, ChiefArchitect at Booking.com
Martin Mexia
SVP, Product · AE
12+ years in fintech product(Revolut, Rappi); founderof Payit
Bruno Ascencio
VP Data, AI and ML · AE
10+ years in data and AI acrossFIs (FAB, Wio Bank, Bineo, Uber)
Maria José Pineda
GM EMEA · CH
5+ years at Adyen leadingenterprise account teams;previously Head of AccountManagement at Yuno
25

=== SLIDE 26 (h7c266de662ba1cf0_0_54) ===
3 · WHY YUNO  ›  YOUR TEAM
A dedicated OnlyFans team, from sandbox to roadmap
Source: Yuno commercial commitment to OnlyFans; team structures dedicated upon contract signing
TRUST & VAULT PRODUCT
Vault Product Team
Open items and roadmapin writing.
Direct access to Slack
Vault design reviews withyour engineers
Network tokens, export anddata-model decisions
Direct line to the Trust &Vault team
Direct access to the builder
TECHNICAL ACCOUNT MGMT
TAM team
Day-to-day platform health +decline analysis
BIN-level decline analysis androuting optimization
Issuer escalations on stuck andhigh-risk transactions
Continuous tuning of retry logicand fallback paths
Real-time dashboards and weeklybusiness reviews
Same-timezone US coverage
SALES ENGINEERING
Solutions engineers
Implementation +integration partner
Direct integration support (singleAPI, all PSPs)
Card migration without fanre-entry
Sandbox proof against agreedsuccess criteria
Sandbox, monitoring, andreconciliation setup
On-call during launches inevery market
KEY ACCOUNT MGMT
Strategic KAM
Strategic partner +commercial QBRs
Single point of contact acrossall regions
Quarterly reviews against yourcreator-banking roadmap
Coordination with banking andissuing partners
Executive escalation owner for anyplatform issue
Senior owner aligned toOnlyFans’s roadmap
REGIONALPRESENCE
Local teams across the Americas, EMEA and APAC
São Paulo · Mexico City · San Francisco · New York · Bogotá · Buenos Aires · Madrid · London · Paris · Dubai · Singapore · Mumbai · Manila
26

=== SLIDE 27 (tdiv5) ===
PART 4
Timeline and next steps
From inclusion in the RFP to a live vault
CONTENTS
1
Executive summary
The answer in five pages: the need, our proposal, why Yuno and the timeline
p. 4-8
2
Our proposal: the OF-Yuno Vault
Vault, Proxy, and your way of using them
p. 10-20
3
Why Yuno
The Yuno story, clients, platform and the team behind it
p. 22-26
4
Timeline and next steps
From inclusion in the RFP to a live vault
p. 28

=== SLIDE 28 (nv_time) ===
4 · TIMELINE AND NEXT STEPS
From inclusion in the RFP to a live vault: five steps and three decisions, each on your calendar
28
Week of 12 Oct
Get included
Deck to the Payments Manager / Intro call
Late October
Deep dive
Session with your payments team / PCI scope review / Sandbox access
November
Sandbox proof
3 to 4 weeks / Card renews on two processors / Creator on two banks / Export test
[RFP deadline]
RFP response
Written answers to open items / Commercial offer
From Q1 2027
Phase 1 live
Contract / Card migration without re-entry / US vault live
Included in the RFP
Proof criteria met
Vendor selected
Our ask this week: include Yuno in the RFP evaluation. After Phase 1: creator banking across banks, pluggable issuers, then yield, at OnlyFans' pace.
Indicative dates, to align with OnlyFans' RFP calendar.
