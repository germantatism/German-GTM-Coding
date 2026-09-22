# FlightHub · questions for Jarrett after the Sep 22 in-person (Will's notes)

Two things Will flagged as "validate": scheduled retries and chargeback / dispute orchestration. Everything else in the notes (A/B testing of routes, payment links) we already know.

## 1. Scheduled (delayed) retries
1. Can we configure a delayed retry on a route, i.e. wait X seconds or minutes before retrying on the same or the next provider, instead of an instant retry? Is that native in routing today, or only in the subscriptions engine (scheduled smart retries)?
2. If it exists, where is it set (route, decline group, condition set) and what are the limits (delay range, max attempts)?
3. If it does not exist, is it on the roadmap and when? What can we commit to FlightHub?
4. How do instant retries work exactly today: retry on the same provider vs cascade to the next one, on which decline codes or decline groups, with what cap on attempts? And on a retry after a timeout, how do we avoid a double authorization or double charge (idempotency, auto-void)?

## 2. Chargeback and dispute management
5. Do we have chargeback and dispute management in the dashboard? Visibility and alerts only, or also case handling: evidence upload, representment, accept or contest?
6. Can we orchestrate chargebacks across their 7 providers (Chase Paymentech, Stripe, Nuvei, Airwallex, Adyen, Braintree, ConnexPay)? From which of them do we ingest chargebacks via webhook and normalize them in one place?
7. Is there a chargebacks API (list disputes, upload evidence, respond)? Which providers are supported through it?
8. They already have a chargeback provider. Can we feed it (webhooks or export) or coexist with it without duplicating alerts?
9. Chargeback alerts (Ethoca + Verifi), now priced in the proposal at $15 per matched alert: how do we enroll MIDs and descriptors across 7 providers, who holds the Ethoca and Verifi contract, what match rate should we expect, what happens with unmatched alerts, and does Verifi RDR go through the PSP as with Appmaking?
