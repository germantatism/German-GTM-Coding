# Hostinger + Yuno — Call Transcript

**Date:** September 3, 2026 · 45 min · Google Meet
**Yuno:** German Tatis (AE), Justo Benetti (CRO), Antoine Cathelin (Head of Product), Dirk Van Der Meulen (Sales Engineer)
**Hostinger:** Paulius Lapenas (Head of Payments)

**Key outcomes:**
- Paulius's real interest: **vault as a standalone service** for business continuity (60-70% of revenue is subscriptions; wants to survive an orchestrator outage). Decision targeted **this year**, execution plan for next year.
- Stack confirmed by Paulius: Stripe, Adyen, Checkout.com, local providers for APAC/LatAm, **direct integrations in India (Razorpay + BillDesk, cross-border, ~70% UPI / 30% cards)**. They already use a third-party orchestration layer for card subscriptions with PSP fallbacks.
- Billing: **Chargebee** (limitations: only controls gap between retries, no time-of-day / day-of-month logic, batch renewals flagged as fraud by PSPs). Dunning: up to 5 retries in 21 days. **Migrating billing in-house gradually.**
- Agentic payments: prioritizing **stablecoin-based protocols (x402, Cloudflare wallet, MPP)** over card-based agentic; early stage, already talking to Stripe about specs; open question on micro-payment billing/invoicing.
- **NDA: Hostinger's paper.** Paulius needs Yuno entity name + signatory by email to kick off.
- **Next call: Thursday, September 17, 2026, same time** (deep dive: vault standalone, subscription engine, India).
- Commitments: Justo → vaulting material, India UPI token-portability status from local team, Revolut Pay / Mastercard funded-card notification info. Dirk → confirm retry-timing intelligence can operate inside their dunning schedule.

---

## Transcript

0:00 | German
great. Thanks for asking. How have these past months been? It's been a while since we met.

0:07 | Paulius
Yeah, it was some time. It was quite intense summer, but all good here.

0:15 | German
So, I understand you guys had a really tough backlog for qo… three. Didn't you. Yeah.

0:26 | Paulius
It is kind of intense from the product perspective. Overall organization is kind of a bit shifting priorities for the way we position ourselves in the market. So everyone needs to kind of prepare for that, and work towards that new approach including payments. So, it is quite interesting period.

0:51 | German
Okay, amazing. Okay. So palos, let me introduce the rest of the team here with us today. So you already met usto who might be joining anytime soon and myself back in San Francisco. So here with us, we have Antoine, who is our head of product and dirk, who is our senior sales solutions engineer. So getting straight into what I want to cover today.

1:21 | Justo
So,

1:22 | German
you send us, the questionnaire, we already prepared it. We sent it back to you a couple weeks ago. So the idea is for us to go over what has happened since we met in San Francisco, understand your priorities and go over, the questionnaire, and we would love, we'd love to show you a demo on our dashboard as well. So if we have time for that, you'll be amazing. Do you have anything you'd like to cover yourself? I.

1:50 | Paulius
Think that's a good agenda. And thank you for sending over the questionnaire with the detailed answers. I went through it and some of the links you shared. So I appreciate it of.

2:02 | German
Course. Amazing.

2:03 | Justo
You got it only like nine months later than when you requested.

2:10 | Paulius
It happens, it happens.

2:13 | German
We promised, we promised this time would be different.

2:16 | Justo
Yes. Anyways, how was your time off? Good?

2:20 | Paulius
Yeah, it was good. It was good.

2:23 | Justo
Okay, perfect. Great. So, yes, no.

2:30 | German
No, I was just gonna start saying polio if you have any questions regarding the questionnaire before we get into anything happy, to answer?

2:43 | Paulius
Maybe just in general one, right? Because I went through the responses… I'm looking into you as an orchestration service provider, right? But when it comes to pci proxy service, I think you mentioned that it can be used, right? So is my understanding correct that you as a yuno is kind of developing or already developed? Let's put it this way, kind of different blocks of services which a merchant can use separately? Let's say, okay, I don't want the orchestration but I want your proxy part or only vaulting part, right? Can I use only that or it's it always comes as a bundle. So, you know, orchestration vaulting and so on and support needs to be used as a cloud service. I think that one thing I would like to clarify. Yeah.

3:32 | Justo
No, I can take it and you can add Antoine if you want or dick on your ad, but yes, basically, you know, about, I'd say like nine, 12 months ago, we decided to start also offering the pieces as a standalone, right? So now we have our token both standalone. You can use our three DS orchestration as a standard on basis as well. So we basically parsing out everything that before we used to sell, you know, kind of in a nutshell in different pieces. So that's exactly, right? So today, what are the products that you can use like that basically is, you know, three DS and everything around optimization, account updater, network tokens, etc, the vault inside of the house, right? Our subscription engine. And basically our orchestration includes many different things. It could be orchestration from paying to payouts to banking as a service, taxes and other elements. Sorry, one more which I don't know if it comes to the case, but it's reconciliation. So before you could only reconcile everything that was coming through the platform right through the yuno platform. Today, we basically made reconciliation a standalone feature so you can get everything that's coming through a yuno platform or upload any type of sources that are out happening outside of the yuno platform as well.

4:58 | Paulius
Okay. So basically, we can connect our other providers, right? Some sort of a part of the reporting and you can consolidate everything. Okay?

5:08 | Justo
Exactly. Yes.

5:15 | Antoine
Yeah. So, so indeed, the idea is that we believe that if you have the best product across the food chain, you should be also modular, right? I think it's like if you're a merchant that is completely stuck in a single ecosystem and that you cannot really allow for testing for a new iteration upon your product, then it's a bit like you're taking a too big of a commitment. So, the idea here is that effectively, you can pick and choose the right product that you want for your own stack at your own pace. Obviously, everything is better engineered when everything is used together. But the idea right now is really that if you want for instance, to use the standard on threeds that we have, we connect to downstream threeds server, the best one in the region in order to reduce the latency, reduce the cost and things like this. Then the idea is that you can just use this one as a first building block. And then obviously, we hope you're happy with it. And then you say, okay, let's move to our network token connections where we connect to BTS and to the scoff API for instance. And you can use your own trade or you can use our own trade, we can generate a trade for you if you want. So the idea is like to make it as modular as any merchant could want. And this is also what we, what you want to do is really like how can each building block still be the best processing experience and user experience while you're not using the full flow? And I think the next one where we will iterate quite a bit on, it is also the voting area where we believe that especially in the agentic age. How can you store securely yet with agility, the information in order to make sure that effectively your information especially if you do kyc for instance, are stored in an encrypted fashion. And that you can have also anything that is linked to user management and user permission because you might not want to have for instance, dirk to be able to read the pan data, but he might be able to read for instance, let's say anything that is linked to passport because he might be more on the customer support wall rather than the payment support form.

7:21 | Paulius
Yeah. Nice.

7:28 | Justo
Curious. It'd be great to hear from you. Yeah. Like any, his change or there's other stuff top of mind for you that you want to solve for.

7:39 | Antoine
Not.

7:40 | Paulius
much actually changing on our side, but we still continue to look into the, some sort of business redundancy business continuity problem, right? And how we can the owners of all the tokens we have. So we could continue our subscription business in case let's say orchestrator goes down and that could be, you know, some sort of a solution which would allow us to seamlessly switch in case of, you know, unlikely even. But in case it goes down for longer then, you know, we want to have a,

8:14 | Justo
checkbox.

8:15 | Paulius
That we are safe and cover the thing that's, the highest priority when it comes to overall business and the side of that, I think we're shifting a bit from looking to the future and how the agentic payments will look like in the coming in the coming future and how it will incorporate in overall our customer journey and payments both. So how much it is linked to the orchestration, as a service overall. But, but yeah, we're we started to pay more attention to the agentic payments, and getting ready for that.

8:49 | Justo
Okay, perfect. Yeah, I think that the difference broadly between what I was talking to starting right? Because starting was they take our agnostic token board, but then they take our orchestration is that the good thing about the product is that you can have the token vault per SE, right? But then all the connectors are already plugged in. They have volume, right? And if tomorrow you need to enable any of those connections or anything, you can do it really quickly, right? So it's just literally a few clicks away which I think it's also the value of having it interconnected in the back, right? For you. As far as authentic payments. We have a product for that across all the different protocols. To be honest, we haven't seen a lot, right? I think probably the us, we've seen a few traffic there. I think everybody's kind of on the same page as you of starting to look at it, but we do have a solution that would allow you to be great to understand, yeah, what information you have so far. And then we can prepare some data for you on our product, what it does and everything. But I don't think yet. We've seen a huge, you know, consumption of that. If we've seen it. It's mostly been across some retail, I would say particularly in the us I.

10:12 | Antoine
Think potentially for you guys. What can be interesting is the MPP protocol where effectively like because I saw that you were selling like I'm not selling but renting like nvidia graphic card for instance. And that can be quite a good use case especially if you want to offer and lower down the payment cost by offering alternative payment method while still being energetic because I think right now the problem is like most of the agentic transactions they are on visa, intelligent commerce or mass card agent pay. But you cannot really optimize up to the interchange level right at one point in the interchange. You cannot really compress it. And what we see now is like potentially, for more like technical use cases of billing, MPP MPP or similar type of protocol might be very interesting to enable it and to do the billing automatically? Yeah.

11:06 | Paulius
Correct. I think we are kind of, I already understood that, you know, part payments will not be soon there in the agentic flow at least for the service businesses, right? It is in retail, it is in physical goods and, yes only. But like rest of the agentic payments like the X core zero two or cloudflare launched wallet quite recently. So these type of payments which are based on stablecoins volumes are quite interesting how they evolve over time. And I think it's something we are kind of would prioritize instead of card payments which has a lot of uncertainties especially in Europe. But it's stablecoin based payments where it's kind of agents buying tokens or buying services based on customer created commands. I think this is what we are looking into especially now and just to understand how we can benefit from that.

12:05 | Antoine
Yeah. So on this, we are having discussion with the MPP team. We didn't integrate it yet because we need to understand how to plug it elegantly. I would frame it this way because indeed, it's like MPP is not really aimed at the same target… at the same customer. If we can frame it this way, vac and mass card agent pay effectively, it's pretty much at the moment customer initiated transaction with at best a delay of four to eight hours if I remember correctly, the specs. So obviously, when your agent is going to say, okay, I would like to for instance, buy X amount or X minutes, and then you have an leeway, it might be too small those four to eight hours to actually have this. And then you need to bring back the customer into session. So it breaks a bit. The whole, the agent is doing its own stuff. And I think on MPP right now, the discussion that we have is how can we integrate it directly into the API without the merchant needing to do any form of additional integration? And the good thing also about MPP is that it's not locked to stablecoins, stablecoin. Sorry, because you can also accept via MPP a non stablecoin payment method. So you can still, because, you know, that most of the consumer, the large scale consumer face, right? They might not have a stablecoin wallet. But what you can do is that effectively you allow for instance, I'm based in Netherlands, I know it's sunny. So it might be weird, but yes, I am based in Netherlands to allow myself to pay with ideal and then for yourself to also lower down the overall payment costs to have a payout in stablecoin. And that this is also one of the flexibility that you would have with MPP that at the moment is not really present into the vac and map protocols.

14:00 | Paulius
Yeah, that's an interesting topic to go into details. I.

14:08 | Antoine
Think on this one, we are looking for feedback. So if you have any feedback about how from merchant perspective, you would integrate it or you would want to use it, that would be we're more than happy to hear it because we're designing the MPP integration and solution on our side. And obviously the idea is to have it tightly linked to the reconciliation engine and also to the billing engine. But I think it was Patton that was saying that a good plan never resists the contact with the enemy. So we can extend this to the contact of reality. And I think here that's always interesting from an early stage on to actually have the perspective of a merchant like yourself into how would you want to have it not only from payment acceptance perspective but also reconciliation? Do you want to have the flexibility when it comes to the payouts? So those kinds of topics, I would be more than happy to collaborate.

15:04 | Paulius
Yeah, I think we are in very early stages and very basic, right? So we can outreach our payment service providers which we use just to understand what they offer. So I think we're in contact with stripe as they have their already specs available for MPP and X. So our very early stage is basic understanding of overall and I think it's really hard to tell how it will look like in the future. But like standing from merchant perspective, ideally, it should be the same as orchestrating part payments and the same should be orchestrating the agentic payments, whether this is existing protocols or as soon as Google launch something, you know, it would be there. So ideally it would be like that, but I think it's better to understand how to build from the orchestrator perspective, how to build a solution? You know, would be seamless for merchant and we could, you know, just have integration, let's say with juno and whatever protocol customer decides to use. The customer agent decides to use. We're going to accept because you have the layer to accept. So ideally it's like that but not sure how it will look like in the future. I think the biggest problem for us as a merchant is genetic payments for now looks like very micro payments, right? They are allowed to kind of transfer part of the cent for the token. So for us, it is interesting how we would build the billing system around it, right? Could we issue invoice for each micro payment, or we should, you know, aggregate those and issue at the end of the session for these type of questions, we still need to understand how to solve it, right? So again early stages or at least for us, yeah.

16:52 | Antoine
And, and I'll be transparent. It's no one has really, I think a straight answer to how it will go, right? I think we're still very much into the protocol wars even though it dialed down a little bit because for instance, like the openai, acp protocol kind of not disappeared but… was not very successful at least in the test. Like there was an article from walmart that said that it basically did not work as expected. And effectively, I think when it comes to the protocol world, the good thing is like it seems that everyone for more the retail use case will move towards ucp, which is the protocol from Google and then they have the ap to bricks into it. But the big part because those protocols are mainly still custom initiated transaction and they are very well attached to vac and map. But for more B to B or machine to machine then those protocols that don't really answer because you don't really need to do let's say a full ucp product discovery if actually it's an agent coming straight to you with what they want to know. And I think here indeed. Therefore, and the X for two and MPP looks to be a better answer at the moment. From our perspective, we are finishing and wrapping up the integration with like the more the custom initiated transaction angle in order to have the orchestration layer on top of it. But we all, as I said, we're also starting to deep dive into how can we with the same layer allow a merchant to not only accept the IC or map via an ap to break or directly ucp? And then ap to, or acp, if they have a connection with open AI, but also, how can we in the same break have the possibility to connect yourself to the machine payments type of protocol? Because I think those two will be separate until design mascot potentially say, okay, now, we also want to chip in. And we also saw that design mascot bought also their own stablecoin infrastructure. So it's just a matter of time before they update visa, intelligent commerce and mascot agent pay into something that can work. And you already see it because they are doing like the whole trusted agent framework with the agent registry type of system. So yeah, I would say within six months, there will be a visa and mascot competitor, of this MPP and X for two in order to make sure that they can keep the full ecosystem on their own rails regardless if it is the traditional rails where we have the interchange model or where it is like something with the stablecoin approach. Yeah.

19:39 | Paulius
Interesting plans, right? Paul earlier?

19:44 | German
You mentioned you guys having a pain around keeping subscriptions going and redundancy. Can you walk us through please over how your subscriptions are looking today and how you try to keep them live whenever something happens?

20:02 | Paulius
So, yeah, basically, we have separate tracks, right? The majority of subscription are card based payments for which we use orchestration layer to execute the payments. But we do have a billing engine outsourced to the chargebee, which is our billing system which indicates when we need to initiate a charge, for a subscription. And basically, we follow, those instructions, right? In case of some issues… or incidents, we do have retry mechanisms both the real time when we do fallbacks between different PSPS and set rules at the orchestration layer. And then we have so called burning cycle which allows us to extend our retries into a certain period of time. So we retry, I think up to five times now in the period of 21 days. So in case someone goes down, we still have a few windows where we retry the payment. And then until now we didn't have a situation where us, when one of the providers would be down for let's say 20 days or so, right? It, it's usually kind of fixed and quite quickly. So we do have ability to retry those payments during the learning cycle. If learning cycle does not help us to capture the payment, then we move to manual renewal flow, but that is more of a communication based flow where we try to interact with the customer to get them back to their panel. And, and the new manual, this is very basic thing. What we do, similar approaches for alternative payments which support recurring capabilities. But then we don't use orchestration layer because majority of alternative payments, we are integrated directly like paytel and some payment methods in latin. In India, we do have direct integration with providers. So not much flexibility of retrying during the session as we don't have fallbacks, let's say adding for fixed payments, but those we can rely on the selling cycle. Perfect. Thank you.

22:22 | Justo
Is the subscription engine today something you build in house or are you using no?

22:30 | Paulius
We don't use stripe. Basically, it is based on our billing system which is chargev. And then on top, we build a rule on the orchestrator, how to route the transaction, how to retry it, so on and so forth. So basically the engine, the logic behind how we initiate the charges sits with the chargebee. We do have some customization availability there, which is not much but still there. But most likely we will migrate internally, the full billing logic as, you know, chargebee has some limitations which we think is not in favor for our business. So we will move that in house and have full control in terms of how and when we initiate charges. Okay?

23:22 | Justo
So at that point, I guess you would drop chargebee per SE, right? Because then you're moving it pretty much in house or are you still going to use some functionality from them?

23:32 | Paulius
It will be gradually, right? So we will not drop it fully at a certain period of time, but we will migrate in certain phases. I need to have the details from the billing team, how it will be done, but it will not be full stop using chargebee, because we still have some maybe legacy customers who will need to migrate, whether this is new customer, existing customers, so on and so forth. So it will be gradual rollout or move to our internal system.

24:04 | Justo
Okay. And when you say some limitations, can you expand a bit more on those? Which are they?

24:12 | Paulius
Yes. So basically, what we see as a subscription business, right? We only can control the time… period, the time gap between the dining charges. So for example, if we initiate the first charge attempt today, then we can control the second attempt will be after two days or five days. So it's very limited, right? And when we take a look into the subscription payment performance, we do see that even time in the day matters when we charge a day in the month also gives a success rate, right? So we don't have this possibility with the chargebee. So we have only the time when the invoice was created and the day when it was created. And we cannot move, right? So if you purchase something from us in the middle of the night, we will try to charge your subscription in the middle of the night even though it's like not bank operational hours in your country. We're still going to do it because we don't have flexibility to tweak… those hours. So this limitation, I think main limitation that we don't have any control or very limited control in terms of how we built our subscription charge logic and timelines, right? So even like the same approach that there is a certain time in the day, then when they submit a batch of subscription renewals, and then it increased load to our system to the payment service provider, and they start to flag it as some sort of, you know, maybe fraud attack because in the short period of time, there is like tens of thousands requests coming from hostinger and it looked like a bit suspicious and too intense for their system, right? So we needed to kind of go to hpsp and tell the day, this is our dining window. We will make a lot of requests. So don't put any risk rules on that. But again, we cannot outreach banks and tell same to them saying that, hey, this is subscription payments. So there's a lot of these small nuances which I think are not good at least during a successful subscription business… okay?

26:28 | Justo
Perfect. That's super helpful insight. And also that ends up creating like a higher cost for you, right? Because you get charged when you retry those transactions or not… let's say you were driving at a time of the day where it doesn't have a lot of intelligence per SE, right? Yeah.

26:49 | Paulius
No intelligence. I'm not even talking about intelligence. It's just a basic thing that we can manually configure some items saying that, okay, if a customer is from the us, don't charge it during the european daytime, right? Wait for working day to start the JS, and then start charging and banks are operational and maybe are applying less risk rules on their side, right? So we don't even have that flexibility. So, I'm not even talking about intelligence which could tell that they hold on charged and then we retry or do something else. So it's not even in scope for now. Okay?

27:28 | Justo
Yeah. There's there's a couple there of stuff that might be interesting like revolut for example, now, in Europe, I'm not sure if you use them. Sorry, do you use revolut or? No? We do.

27:43 | Paulius
We do have some treasury relationship with them when it comes to bank account. And we did launch revolut as a payment method quite recently, but nothing more than that. Okay?

27:55 | Justo
Perfect. Jose. They build some intelligence there across revolute pay, and also revolute acquiring for when funds kick in into the account, right? Or eventually the fact that they could, you know, allow to overthrow a customer, for example, in some cases and make sure like you charge your subscription. So, yeah, I think it'd be worth there. Another talk. I know we built all those things in our integration. It's pretty new, right? Like two months old or so, but that should allow you to have like even more intelligence from their end to consume and understand when to retire or not even have to think about it, right? And then we're having a conversation with mastercard. I think we're trying to understand this, but they develop also a product around. Yeah. When a customer's card, it's actually gets actually funded. We would receive a notification, right? And we could pass that back up to you for example, right? And then, you know, that is exactly the time to retry. So those are two things that come to mind for sure, that I think could help across that process.

29:08 | Paulius
I think revolut is quite small for us comparing to the volumes we process. So I really don't want them to be building some sort of logical flow just for a single issuer, which is not even in the top list for us as a merchant, right? But I think chase has some sort of also product which allows this smart subscription… or how do you call it? There are different products but they are, you know, you need to adjust each and every of them instead of having some sort of a better approach which could cover all the subscriptions instead of managing pay five or even more logics. But, yeah.

29:51 | Justo
No, super helpful. I know we are, yeah, right on time. I think to understand from your, yes, we actually, we have.

30:04 | Paulius
15.

30:04 | Justo
More.

30:04 | Paulius
Minutes. Okay.

30:05 | Justo
Perfect. Then it's my calendar that, I am out of time, but yes, for this, I think, you know, we have 15 minutes then it'd be great to understand from your end, where do you want to dive deep? Would you like to see the platform? I think for us takeaways, just understand what else do you need on your end to kind of make this vaulting decision, right? And I think we have some interesting information on everything that you mentioned around follow ups that we can do, right? And what the platform can do as well.

30:40 | Paulius
Yeah. So I think, you know, just to be kind of fair and honest here, right? Most likely, the interest would be to better understand the vaulting part as a standalone service. And then, you know, as you progress with your development on the agentic payments, I think it would be good to also understand, can we leverage that, right? Instead of us building everything in house as a separate integration with different protocols and getting some approvals because you're a way bigger organization, right? And it's maybe easier for you to integrate all the protocols. And then we can start using, this new program. But I think it's a bit in the early stages first. So I think these two flows with something we could continue to discuss. And for now, maybe wall thing would be interesting to understand whether there is actual need and benefit for us, to kind of explore it as a standalone service. And, you know, what risk it covers for us because, you know, the main concern is our business continuity as we are pushing this business in like 60 percent or 70 percent of our money comes from subscription payments, right? So we don't want to stop operating in the subscription. I think this attracts that most likely candidates.

31:58 | Justo
Perfect. No, I think for the bolting, yeah, we can definitely send you had a lot of questions there, right? But I think we can expand on some of those questions. So we show you all the different features that you can use with bolting. We'll prepare some material there. So you understand the full breadth and depth, of the platform. I think where we stand on is probably different than just bolting solutions, right? Is that okay? Since we have an operation that runs payments, you know, 24 seven, you have our 24 seven noc, we have our servers running hot, two in the us, one in Europe, one in APAC, right? Instance in ksa, an instance in India, right? So I think that's pretty much different than your typical just bolting solution, right? Just because we need another level of infrastructure there, which I think gives our customers a lot of comfort when it comes to that. Yeah. And then the fact that you have all these pre built connections at the end of the day, right? So if tomorrow you decide you need to use one, right? Or whatever, you can use components or parts of the orchestration to get those payments. So, I think that's really the difference between us and how we thought about the product versus just bolting solutions, right? Is that it gives you that flexibility and it's actually paired with more of, a global support 24 seven, follow the sand model, right? Because I think when you see a lot of these bolting companies are maybe like 20 or 30 people, right? And you don't really get a full support like you do in payments typically. And I think that's why we've been winning a lot of details and why customers have pushed us to do it as a standalone as well. So there, yeah, I would say let us follow up with that. Is that a decision that you're still trying to make this year?

34:00 | Paulius
Decision wise? Yes, I think it would be good to finalize this year and then just have already a plan at least for next year, how it is better for us as an organization to proceed with this.

34:15 | Justo
Okay. And remind me today, you use just stripe or you're using stripe Adn and a few more. We.

34:23 | Paulius
Use multiple stripe Adn, check out the local events for afac region and latam, and some more direct integrations with other providers for India.

34:39 | Justo
Okay. Perfect. India. Are you doing it cross border or are you doing it locally?

34:44 | Paulius
Yeah, we do cross border.

34:47 | Justo
Okay. Perfect. Well, all the ones that you mentioned at least in the top of your list is pretty easy. I would say token migrations and business as usual for us in India. Are you using raise or pay buildesk? Any of those guys? Both? Perfect. We got a tight relationship with both of them.

35:08 | Paulius
So maybe India would be also interesting to kind of understand as a separate market, right? And is there a possibility of orchestrated payments there between let's say buildask and razorpay especially for subscription? Because as far as I know… central bank is not allowed to kind of exchange tokens between providers there. But I'm not fully sure I'm fully accurate here. So it would be good also to understand India as a kind of standalone region country.

35:42 | Justo
Is the majority of your payments there like upi or no? Yeah.

35:47 | Paulius
I think 70 percent upi, 30 percent card payments, something around that or 60 40, but still upi is the dominant one.

35:56 | Justo
Okay, perfect. So the central bank, they already push for what you would call a network token at the upi level, right? So you can actually have that redundancy and kind of move it around. It's. Actually been a mandate. It's just a lot of these companies are behind in the application of it, right? But it should happen last time we spoke to razorpay, which I think was, or I spoke to razorpay like two months ago, they still had it for this year, right? So I do believe it's something that by the end of this year, most of the players should be abiding by the mandate. Okay? And I can share that with you. But yes, that's something that definitely you'll be able to do at the most by the end of this year, right? Which is make sure you have redundancy and you are not stuck with tokens that are just related to one financial institution per SE.

36:51 | Paulius
Yeah. I think that's kind of also crucial for us to understand because now we maintain two separate integrations. They are a bit different. Customer journey is also a bit different, which is not good from our customer perspective. So if we can aggregate that part in front end and then subscription charging and all those token questions. I think that would be a good solution.

37:17 | Justo
No, perfect. We'll share that information, everything we had. I'll get an updated status also for some of the players there in India because we have a local team, a local general manager to understand like where are the rest of the players as well in terms of that functionality? Nice. Thank you. No, fantastic. Sorry, I need to drop, but, yeah, polios, thank you again for your time. At least for me. I'll leave the team here but really appreciate you jumping on this call and having this combo with us.

37:49 | Paulius
Yeah, thank you. Likewise. Husto, appreciate it. Bye, husto… polios.

37:55 | German
So we don't have much time for us to go over a deep dive into our platform. So I would like to propose if you have time next week or maybe the week after, we can hop 30 minutes and go into the details. So tell me how's your agenda and we can set something up.

38:17 | Paulius
Yeah, we can plan something maybe not next week, but the following week… Wednesday or Thursday… we can do it to Thursday same time as now.

38:37 | German
Okay. Amazing. Paul, something also I feel really important to mention is that we also have our standalone subscription engine. And unlike what you guys have right now, our standalone subscription handles, orchestration handles, smart routing. We have integrated already apms such as apple pay, Google, pay, paypal, pix, automatiko, upi autopay, and many others. It's basically let's say you'll migrate away from chargebee and start using our engine on top of all of your orchestration. So it'll be great also to show you all regarding our product. So… maybe also.

39:38 | Dirk
Like one thing to add there because I've heard you just say that like one of the frustrations you're currently facing is that retries are basically always at the same time. It's not that with us, you can determine like what time you are going to retry, but we do have a model behind it that chooses a more optimal time for retries. So it's not like it's every time going to be at the exact same time, which could be the middle of the night. Like you said, so we do have some logic there.

40:10 | Paulius
Yeah, it would be good to understand how, you know, because actually we will build the billing engine in house, right? So part of the functionalities will sit with us. But then on top bringing that, okay, we will send a request to charge through yuno to stripe checkout or whatsoever. Yeah. And then you apply your logic but it needs to kind of adhere to our billing schedule. So, you know, we kind of know, you know, it cannot be delayed for five days.

40:38 | German
If so, right? No.

40:40 | Dirk
But when you say like you're building an engine in house, but do you still rely on a third party to take care of the retrying or is that something you would build in house as well?

40:53 | Paulius
Yes. And no, the retries are more from the managing the learning cycle itself. Yeah. And then the fallback retries is going to still sit on the third party which is orchestration layer, right? Yeah. Okay. Yeah. Well, that's all intelligence when it comes to subscription, right? So, for example, now we run and running charges each today. So if I send you a request today, which is Thursday, my next request will come on. Let's say Saturday. So if you, if your intelligence tells that, okay, don't charge on Thursday, but you can attempt to charge on Friday so that's okay with me because it will not impact my dunning. I still will receive a response from your site till Saturday, which is my decision whether I continue to charge the person or not, right? So if that intelligence can be built on top, that's totally fine with us. But if your intelligence will say that, hey delay for one week, then for us, it's no use because it will break our everything cycle. Yeah. Well.

41:58 | Dirk
Let's look into that and see what we can do there. I might come back to that. Yeah. Thanks also.

42:06 | German
Before, we go, I did wanted to show you maybe, a glimpse on how, the subscription stack standalone is looking right now. So basically, here you're going to be able to create different plans. I understand you guys operate a model in which you like offer your client to buy a 48 month plan at a way cheaper price, and then that's going to renew once the four years are done. So you can do this in here and you're going to have complete visibility on how it works and it will do automatically. Like we will handle the retries, we all handle like we're going to be the ones initiating every single transaction. And you can also create different meters like for example, you want to include 15… credits per subscription to like for AI building. But then after the credit number 16, you're going to charge you 40 cents per credit and you're going to have complete visibility on that in the dashboard… you can see it's like subscription.

43:24 | Paulius
Management. And then like doing pricing offers one and support through the through your engine, right? Yes, that's right? You.

43:36 | German
Will have access to everything. Like you can manage, you can know a who's handling which subscription if anything's changed, like 16 upgraded 11 downgraded, and you can track everything like what percentage of people are linked to your premier plan, to your pro plan, to your unlimited 48 month, and you can have visibility on everything basically.

44:06 | German
So, yeah, that was kind of like a glimpse, on the product, more than happy, to take a deeper dive on Thursday the following week.

44:19 | Paulius
Okay. Sounds like a plan. Amazing.

44:22 | German
Paul, we don't yet have an NDA signed and so, is it okay if we send you our NDA and we can get that done? Or do you guys want to move forward with you? Okay, perfect. It's always.

44:39 | Paulius
Kind of better to use our mda, but, you know, we're quite flexible there. I think our mda will be faster just from our legal perspective review. So it depends, right? I can keep up in the process, and I'll teach you or if there is kind of a hard request from your site to use your NDA, we can review it and provide our comments. If you.

45:02 | German
Say your NDA will move faster, then let's go forward with your NDA at the end of the day, let's make it more efficient. Like we don't have any preference regarding that?

45:11 | Paulius
Okay. Nice. Just send me over the email, the kind of exact entity name of yuno and who would be signing the NDA from your side? If I could throw it so they could kick off the process?

45:26 | German
Amazing will do. Okay. Oh, thank you very much for your time. Have a great rest of the week.

45:35 | Paulius
Appreciate it. Thank.

45:36 | Dirk
You for your time and speak to you later.

45:38 | Paulius
Yeah, thank you. Pleasure. Meeting. You. Take care. Bye.

45:42 | Dirk
Likewise. Bye bye.
