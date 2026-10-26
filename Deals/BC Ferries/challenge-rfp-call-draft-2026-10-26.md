# BC Ferries NRFP 28-2026: challenge-the-RFP reply (draft for Sean), 26 Oct 2026, v2

Context: procurement@bcferries.com replied to Sean on 26 Oct with boilerplate ("we encourage all qualified Proponents to participate... refer to Section 1.1.4 on Proponents, Proponent Teams and Subcontractors"). Amendment #1 (issued 22 Oct) names Phil Miller, Category Manager, as the Procurement Contact, bars contacting the business department directly, and defines the Core Solution as Categories A, B and C (processing, gateway, fraud) with Wallet and Programs as a separately evaluated Category D. Questions close Wed 28 Oct 2026, 2:00 PM PT; addenda deadline 4 Nov; submissions 17 Nov.

v2 (German's feedback): no Section 1.1.4 reference; open with "we're in, we'll answer everything, but we want to raise our hand"; a persuasive middle on all connections in one place, lower cost and higher revenue; then the call ask. Stats are Yuno's published figures only (up to 7% authorization uplift, 30% recovered revenue).

Gmail draft in German's account as a reply-all to Sean's forward (Sean + Magda). Sean sends the reply to Phil / procurement since the thread is his.

---

## Cover note to Sean (and Magda)

Sean, Magda,

Procurement's reply is boilerplate. Amendment 1 (Oct 22) names Phil Miller as the procurement contact and bars us from contacting the business team directly, so any call has to go through him. The NRFP is structured for a processor-led stack (processing, gateway and fraud as the Core Solution, wallets as a separate Category D), so I'd rather raise orchestration now, before questions close Wednesday Oct 28 at 2 PM PT, than find out at shortlisting that we don't fit the boxes.

Suggested reply to Phil below, from you since the thread is yours. We'll take care of the BC Bid registration.

---

## Reply for Sean to send to Phil Miller / procurement@bcferries.com

Hi Phil,

Thanks for the reply. We'll register on BC Bid and respond to the full NRFP.

We do want to raise our hand on one point before questions close on the 28th. Looking at the evaluation ahead of you, we believe orchestration belongs in it, and we'd like to explain why.

The NRFP treats processing, gateway, fraud and wallets as separate categories. Bought that way, each one is its own integration and its own contract, and every provider change becomes a project. An orchestration layer puts all of those connections behind one integration: the processors you choose, 3DS and fraud tools, Apple Pay, Google Pay and stored cards. Adding or replacing any of them becomes configuration rather than a re-platform, which is what the flexibility for future modernization in your scope actually requires.

On cost, sitting above the processors lets BC Ferries route each transaction by cost and keep more than one acquiring relationship, leverage a single provider never gives you. On revenue, smart routing, retries and automatic failover recover transactions a single processor declines or drops, and keep online and app sales running through a processor outage like the fleetwide one in September 2023. Yuno's published figures are up to 7% higher authorization rates and 30% of lost revenue recovered.

We'll respond in full either way. Could we get 30 minutes with you and the team that owns the payment ecosystem, arranged through Procurement, to walk through how this maps to your categories before proposals are locked? If the process doesn't allow it at this stage, we'll put the question in formally before the deadline.

Thanks,
Sean
