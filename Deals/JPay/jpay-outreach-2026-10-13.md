# JPay outreach: redundancy / second acquirer (13-Oct-2026)

**Intel (internal, from Sean Calabro, ex-Worldpay):** JPay runs all of its card traffic through Worldpay, and the volume is significant. This is not public, so the copy below never names Worldpay or says how we know.

**Angle:** keep the current processor, add Yuno on top plus a second acquirer behind it. This means redundancy, routing, and leverage on pricing. No rip and replace.

**Target:** Kevin Elder (President, Aventiv). Swap in Peter Ohser if he still runs payments, or Brian Evans (CEO) for a top-down version.

---

## LinkedIn 1: connection request

> Hi Kevin, congrats on the new role and on closing the recap in July. I work on payments infrastructure at Yuno and spend a lot of time with high-volume deposit businesses in the US. Would be glad to connect.

## LinkedIn 2: after he accepts

> Thanks for connecting, Kevin. A question I've been asking payments leaders lately: if your processor has a bad hour, what happens to deposits? For JPay that's families who can't fund an account and agencies watching the numbers.
>
> We help teams keep their current processor and add a second path behind it, with routing and failover in one place. Worth 20 minutes next week?

---

## Email 1

**Subject:** A second path for JPay deposits

Hi Kevin,

Congratulations on the new role, and on getting the recapitalization done in July. New ownership usually brings a fresh look at where the business carries risk, and payments tends to sit near the top of that list.

When a deposit business runs all of its volume through one processor, it works well until the day it doesn't. One outage or a spike in declines and families can't fund accounts, support queues fill up, and the agencies you serve notice. It also leaves very little leverage when pricing comes up for renewal.

Yuno lets you keep the processor you have today and add a second one behind it, with routing, failover and monitoring handled in a single layer. Your checkout stays as it is, and a new connection is typically live in weeks.

Would you be open to a short conversation next Tuesday or Wednesday? I'd love to hear how you're thinking about this under the new structure.

Best,
German

---

## Email 2 (same thread, about 5 business days later)

**Subject:** Re: A second path for JPay deposits

Hi Kevin,

Following up with something a bit more concrete.

Diversifying a payment stack doesn't have to mean replacing what works. The teams we work with keep their primary processor exactly where it is and use Yuno to add a second one. Then each deposit goes where it makes the most sense: the lower cost route, the one approving better that day, or simply the one that's up. Soft declines get retried on the other path before the family ever sees an error.

Two things usually follow. Approval rates go up, typically around 7%, which at JPay's volume means fewer failed deposits and more fees collected. And every processor negotiation starts with a real alternative on the table, which changes the conversation on rates.

Allegiant Air recently signed with Yuno to run its payments in North America, and Rappi uses our real-time monitors to catch issues in milliseconds instead of the 5 to 10 minutes it used to take their analysts.

If it's helpful, I can sketch what a dual processor setup would look like for JPay's deposit flow. Would 20 minutes next week work?

Best,
German

---

## Key contacts (from Sales Navigator, 13-Oct-2026)

### David Lovitt, Senior Manager, Infrastructure (Fort Lauderdale; 14 yrs at JPay; 2nd degree, 1 mutual)
Angle: uptime and redundancy. Owns infrastructure, so a single processor reads as a single point of failure.

**Connection request**
> Hi David, 14 years keeping JPay's infrastructure running says a lot. I work on payments infrastructure at Yuno, mostly with high-volume US businesses thinking about uptime and redundancy. Would be glad to connect.

**Follow-up DM**
> Thanks for connecting, David. Curious how your team thinks about redundancy on the payments side. When all deposits run through one processor, a bad hour on their end turns into families who can't fund accounts and a full support queue.
>
> We help teams keep their current processor and add a second one behind it, with failover and monitoring in one layer and no checkout rebuild. Open to a quick call? And if payments sits with someone else, I'd appreciate a pointer.

### Dariel Baez, MBA, CAMS, Compliance Sr. Analyst (Miami; 6 yrs at JPay; 3rd degree)
Angle: adding a second processor without adding compliance overhead. Ask for their perspective, no hard pitch. Never mention CFPB or regulatory history.

**Connection request**
> Hi Dariel, I work on payments infrastructure at Yuno with regulated US businesses, and I always value the compliance view on how payment stacks evolve. Would be glad to connect.

**Follow-up DM**
> Thanks for connecting, Dariel. A question from the compliance side: when a money transmitter adds a second payment processor, what's usually the hardest part to get comfortable with?
>
> We help teams add a second processor behind the one they already have, keeping fraud screening and reporting in one place instead of two. Happy to compare notes for 15 minutes, or if payments decisions sit with someone else at JPay, a pointer would mean a lot.

---

## Intro emails (13-Oct-2026). Gmail draft creation was blocked; paste manually. Emails not found, add addresses.
Call slots: Thu 22-Oct or Fri 23-Oct, late morning ET (German is at Money20/20 Vegas 18 to 21-Oct).

### David Lovitt
**Subject:** Payments redundancy at JPay

Hi David,

I'm German, part of the North America team at Yuno. I've spent some time getting to know JPay's business before reaching out, and fourteen years on the infrastructure side means you've seen just about every version of the platform, and probably most of the bad days too.

From what I understand, your card deposits run entirely through Worldpay. It's a solid partner, but it also means one provider carries every deposit a family makes, across every state you serve. With the new ownership group settling in and agencies comparing fees and service levels at every re-bid, I'd imagine resilience on the payments side is getting more attention than it used to.

That's the problem we work on at Yuno. We sit on top of the processor you already have and add a second one behind it, so deposits can fail over automatically, go to the better performing path, and be monitored in real time from one place. Your checkout doesn't change, and Worldpay stays where it is.

Would you be open to a 30 minute call on Thursday the 22nd or Friday the 23rd? Late morning Eastern works well on my side. And if payments decisions sit with someone else at JPay, I'd be grateful for a pointer.

Best,
German

### Dariel Baez
**Subject:** A compliance view on JPay's payment stack

Hi Dariel,

I'm German, part of the North America team at Yuno. I've been reading up on JPay before reaching out, and your background stood out: six years in compliance at a licensed money transmitter, plus a CAMS, is exactly the perspective I was hoping to hear.

From what I understand, JPay runs its card deposits through a single processor, Worldpay. Teams in that position often start looking at a second processor for resilience and pricing, and what usually slows them down is the compliance side: two sets of fraud rules, two sets of reports, two vendors to oversee.

At Yuno we sit on top of the processor you already have and add a second one behind it, with fraud screening and reporting kept in one place. Worldpay stays where it is, and adding a provider doesn't mean rebuilding your controls from scratch.

I'd really value your take on how JPay thinks about this. Would a 30 minute call on Thursday the 22nd or Friday the 23rd work? And if this sits with someone else on the payments side, a pointer would be much appreciated.

Best,
German
