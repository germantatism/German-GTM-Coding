# Suno: LinkedIn thread German ↔ Jasper van Rijckevorsel (verbatim)

Jasper van Rijckevorsel (He/Him), Music + Engineering @ Suno. 1st degree connection.
Span: 2026-02-20 to 2026-04-29. Pasted by German on 2026-08-06.

---

**Feb 20, 10:02 AM. German:**
> Hi Jasper,
>
> I'm reaching out over the possibility of having a conversation on how you're managing payments at Suno.
>
> I'd love to tell you how at Yuno we've been helping companies like Open AI, Lovable, Whop, Hotmart, GoFundMe, McDonald's, SpaceX, Uber, and many more reduce payment processing costs, increase approval rates, and enhance customer experience.
>
> Would you be open to a quick call next week?

**Mar 3, 1:04 PM. German:**
> Hey Jasper! Hope all is well.
>
> Just wanted to swing by your inbox again and see if you were able to see my message.
>
> At Yuno we firmly believe there's a great opportunity to explore synergies with Suno!
>
> Would you be open to a quick call?

**Mar 5, 10:24 AM. Jasper:**
> Hi German. We're currently in the early stages of optimizing our mobile payment flows and potentially moving payment vendors. I'm very busy so I'd love an honest assessment of where you could fit in or optimize our flows.

**Mar 6, 10:41 AM. German:**
> Hi Jasper,
>
> Thanks for the honest reply, and it makes total sense to focus on what actually matters without wasting time (love the mentality).
>
> Given that you work with recurring card payments and are reviewing your mobile flow, I can give you a quick and concrete assessment on three areas where we typically see the most opportunity in companies with this profile:
>
> 1. Approval rates on recurring renewals: relying on a single acquirer significantly limits your ability to recover declined transactions. With intelligent routing, clients like Livelo recovered 50% of transactions that would have otherwise been lost, with zero action required from the end user.
>
> 2. Smart retry logic: most mobile flow failures happen due to temporary issues (instability, momentary limit reached). With well-configured retry logic, it's possible to recover revenue that's currently leaking out silently.
>
> 3. Payment method flexibility without integration costs: enabling Pix (all forms), digital wallets, or other methods on mobile still takes months of dev work on almost every traditional stack. With Yuno, it's done in days, with no new integration required.
>
> I even built a business case so you can go over a bit on what we can do for you. Please find it here: https://deck.y.uno/sunobc
>
> So, if it makes sense I would love to have 20-30 minutes with you to take a deeper dive! Free next week on Tuesday?

> Sorry for the kind of long answer but this is my one shot haha. Really looking forward to your thoughts Jasper

**Mar 6, 10:52 AM. Jasper:**
> It's a great answer, let me look at the deck and let you know if it makes sense to connect now or if we should look a little further into the future

**Mar 6, 11:07 AM. German:** Thanks!

**Mar 10, 2:17 PM. German:**
> Hey Jasper!
>
> Hope you're having a great week. Just wanted to follow up on the deck I shared. I put a lot of thought into the numbers, so I'd love to walk you through it together and dig into where we think we can move the needle for you.
>
> I genuinely think there's a compelling story in it and my previous answer, and a quick call would let me give you a much clearer picture than any message can. Would you be up for 20 minutes sometime this or next week?

**Mar 18, 3:40 PM. German:**
> Hi Jasper,
>
> I know you mentioned being pretty busy so I'll be quick - any chance we can get together and explore potential synergies between Suno and Yuno? After working on the business case, I feel like there's a lot we can build together!

**Apr 10, 11:12 AM. German:**
> Hi Jasper,
>
> I'll keep it short.
>
> You mentioned you're optimizing mobile flows and exploring new vendors. That's exactly where the 3 points I shared (approval rates, retries, payment method flexibility) make the biggest difference, and all of it can sit on top (or alongside) of your current Stripe setup without ripping anything out. On top of that, there's real room to rethink how you're billing through App Store and Google Play, which usually unlocks the single biggest saving for apps like Suno.
>
> Integrating new payment partners usually is really expensive and takes a lot of time. With Yuno, you'll have instant access to everything you need with a few clicks.
>
> Really looking forward to having 15 minutes to walk you through what that could look like for Suno specifically and go over the business case?
>
> Best,
> German
>
> PS: Are you heading to Stripe Sessions in San Francisco at the end of the month? Would love to grab a coffee there if you are.

**Apr 29, 11:40 AM. German:** [content missing in the paste, likely an image/GIF or truncated. Per prior session context: Jasper reacted with emojis 😆👏👍 around this date, no text reply.]

---

## Analysis (2026-08-06, day before the Suno & Yuno meeting)

**What Jasper actually committed to (his only two messages):**
1. Mar 5: confirmed an ACTIVE vendor evaluation: "early stages of optimizing our mobile payment flows and potentially moving payment vendors". He asked for an honest assessment, not a pitch.
2. Mar 6: framed the open question as TIMING, not fit: "connect now or look a little further into the future". He never objected to the substance; he called it "a great answer".

**Reality answered the timing question:** Suno hired subscription-payments operators (Madden Titus ex Disney Streaming payments/fraud PM; Gurwinder Gulati, likely ex Uber One membership-payments tech lead) and took a meeting with Justo for Aug 7. The evaluation Jasper described in March is now staffed and running. "The future" arrived; the meeting IS the evaluation.

**Claims already planted with Suno (be consistent tomorrow):**
- Single-acquirer limits decline recovery; Livelo recovered 50% of lost transactions via routing.
- Smart retries recover silent mobile-flow leakage.
- APMs (Pix, wallets) in days, no new integration.
- Yuno sits on top of or alongside "your current Stripe setup", nothing ripped out (German asserted Stripe in Apr; Jasper never corrected it; research later confirmed via Suno's own ToS/help center).
- App Store / Google Play billing rethink = "the single biggest saving" for apps like Suno.
- Business case at deck.y.uno/sunobc, in Jasper's hands since Mar 6 and sent to the exec group (Martin, Jeremy, Georg, Jack) on Jun 3.

**Flags for the Aug 7 call:**
- The Feb 20 opener name-dropped OpenAI, Lovable, Whop, Hotmart, GoFundMe, McDonald's, SpaceX and Uber. Gurwinder likely built Uber One payments and Madden ran Disney Streaming payments: any client claim will be validated by operators who lived those stacks. Only reference what Yuno demonstrably did for each named client.
- These two attendees know base rates for approvals/retries in subscriptions. Quantified claims (50% recovery, +7% approval) should come with the conditions under which they hold.
- The sunobc deck predates the Series D, the $300M ARR announcement, the WMG settlement and Spark. If it resurfaces tomorrow, the numbers read stale; refresh or reframe verbally.
- Jasper is NOT in tomorrow's meeting. He is the origin touchpoint and possible internal ally in engineering, not the payments owner. A short thank-you note to Jasper after the meeting ("your team took the conversation, appreciated the honesty back in March") keeps that bridge alive.
- German's Apr 29 message content is unknown (blank in paste). If it matters for continuity, check LinkedIn before referencing the thread's ending.
