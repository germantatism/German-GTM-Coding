# Hostinger + Yuno | Demo — Call Transcript (2026-09-24)

**Recorded:** Sep 24, 2026, 06:00 COT / 14:00 Vilnius, Google Meet, 43 min (Fireflies.ai)
**Yuno:** German Tatis (BDM NA), Dirk Van Der Meulen (Sales Engineer), Piotr Sierpinski, Tautvydas "TJ" Paukštė
**Hostinger:** Paulius Lapenas (Head of Payments)
**Did not join:** Justo Benetti, Antoine Cathelin

## Summary (written Sep 24, 2026)

- **NDA:** Paulius overruled his legal team's one-way NDA; Hostinger will send its **mutual NDA** (the one they use with other providers) "today or tomorrow". Route C.
- **He asked to steer the session to two things:** India as a use case, and vaulting as a service.
- **TJ introduced himself** as VP of Engineering on the rails side (integrations, orchestration, transaction core), joined ~1.5 months ago; offered to meet Paulius in Vilnius; Piotr offered to drive over.
- **Dirk demo:** connections (set up a BillDesk UPI connection live), routing by currency INR / amount, fallback to dLocal, decline-code grouping (sandbox bug when selecting codes), metadata-based routing (Paulius asked; yes, text and number), traffic split, smart routing (conversion+latency or conversion+cost; cost uses merchant data, conversion/latency uses platform data), Monitors (window, threshold, email/Opsgenie, auto-reroute with control group).
- **Network token vs PAN priority:** merchant-controlled in routing today; optimization model planned.
- **Volume split (Paulius):** ~70% recurring MIT, ~30% one-time / card-on-file (to verify). Plans mainly yearly, then monthly, then 2 to 4 years. "Bread and butter is subscription payments... convert as much as possible during the auto-renewal flow without the customer in session."
- **Subscription engine:** Dirk showed plan creation, phases, trials, meters; German showed Hostinger-branded plans with AI builder credits. Chargebee today only issues invoices and signals when to charge; dunning cycles configured there. **Paulius: migrating the catalog and billing to Yuno "I don't see that happening, to be honest."** What he wants is "smart subscription management": when they initiate a charge, Yuno decides a better moment within their window (e.g. delay 20 hours). German: a bridge between their billing (Chargebee / in-house) and Yuno subscriptions is possible; Yuno as the party that executes the charge. Piotr: ML retry timing engine (6 months of merchant data) live, "happy to give it a try"; routing by stored-credential reason (first vs subsequent MIT).
  - ⚠️ Piotr answered "Exactly" when Paulius asked whether smart routing would delay an MIT charge created on their side. Needs written verification (Dirk).
  - ⚠️ German said the engine runs cards, Pix Automático, Apple Pay, Google Pay, PayPal and is "finishing off UPI Autopay"; docs.y.uno list CARD, PAYPAL_ENROLLMENT, PIX_AUTOMATIC. Do not repeat in writing until Product confirms.
- **Token migration (his central question):** what happens to network tokens and scheme (network) transaction IDs when moving between orchestrators; he has seen declines when an orchestrator sends the wrong scheme ID. Tokens today live in the current orchestrator's vault, under Hostinger's name (own TRID). **Volume: "a couple of million tokens"**, not all would migrate (inactive customers). Dirk: Yuno runs the transfer with the current provider, delivers a mapping report; network tokens under their name should be reusable, **to verify**; will send a step-by-step migration overview (data taken, what is requested, how auth rates are protected).
- **India:** tokens and UPI Autopay mandates are held **directly with Razorpay and BillDesk**, not with the orchestrator. Paulius: as far as he knows RBI does not allow token sharing between providers; regulation is being pushed; asks whether Yuno has a **production example** of migrating from Razorpay/BillDesk. Piotr: Yuno is local in India; one option is taking raw card data and re-tokenizing (brainstorm, not a plan). **TJ: will check with the vault owner and come back.**
- **Paulius's close:** "If we can focus on India, that would be a very straightforward case for us. Now we handle it separately at the PSP level. It can move to the orchestration platform with proper routing, proper token storage, adhering to local requirements. That could be a strong case for us. This is our second market in terms of size. Good starting point. And then vaulting as a service also as a separate track."
- **Next steps agreed:** Hostinger sends mutual NDA; TJ returns with the India answer ("quite important"); Dirk sends the token-migration overview; German proposes a live migration demo / working session with Paulius's team after the NDA.

---

## Transcript

0:00 | German
last week full… of work. Hey, Dj. Hello? Hey, it.

0:09 | Paulius
Was quite interesting, quite sudden conference. I needed that then, but all good.

0:15 | German
Now, great. Great. Good to hear that dirk. How are you? I'm.

0:22 | Dirk
curious. How are you? Good morning. Good.

0:26 | German
Morning. Yeah, good.

0:28 | Tautvydas
Morning.

0:33 | Piotr
Good afternoon.

0:36 | German
Amazing. So, Paul, if it's okay, let's get started. The idea for this call is for us to take a deep dive into the dashboard. We've talked internally and based on all the questions you asked, on the questionnaire, the idea is to go over the things that matter for hostinger the most. So let's say things around the token vault, the account updater, all regarding network tokens, network, transaction ids, our subscriptions engine and routing, and of course, anything you want to add or you want to learn a bit more, we're open to taking a deeper dive, on them. So… before I keep them, yeah, yeah.

1:28 | Paulius
Two things for the NDA part, right? So I'm choosing my legal team because they send you an NDA and not a mutual NDA, which is kind of more friendly. Let's put it this way, right? So we'll send out the mutual NDA. That should be fine because we're using it with other service providers. I hope to be able to send it like today or tomorrow. So that should be covered. And for the kind of dashboard review, not sure if changed anything. But last time we spoke about, you know, India as a use case, right? So in case it has some different approaches when it comes to India specific. And then we're talking about like vaulting as a service, right? So if we can somehow tweak the presentation towards these two, I think it would be better for me to understand, you know, the head here… hey.

2:26 | Piotr
Pau, it's my pleasure to see you, man. Hope all is well.

2:31 | Paulius
Yeah. All good looking.

2:34 | Piotr
Forward to work together again, man. This is an amazing time to join Uno.

2:40 | Paulius
Yeah, cool.

2:41 | Piotr
All right. Tj. Happy to have you on board.

2:45 | Tautvydas
Hey, thank you. Thank you. So maybe a little intro from my side. So I'm totidas recently joined Yuna, like one and a half month ago as a VP of engineering at the braille side. So, my main responsibility is with the integrations, payment orchestration and the transaction core. So if Paulus, you have any questions, you can also approach me directly and we even can meet in witness if that's too soon.

3:20 | Piotr
Please invite me. It's like just a few hours drive, right? So, happy to join.

3:25 | Tautvydas
You couple of hours, couple of hours?

3:27 | Paulius
Exactly. We.

3:28 | German
Can do it again together there.

3:31 | Dirk
It's a bit further for you.

3:36 | German
Yeah, but we need to make it happen sometime for sure. True, true Paul regarding the NDA amazing aligned on that. And thank you very much as soon as we get it, we'll get things moving on our end. Now regarding the India case, we can like do specific things around India whenever we're going through the dashboard. But basically what we have is for India is what we have for the world. We have like a huge presence in India now, and the idea is to keep expanding. So we for sure have all the capabilities ready for you guys in India. So, dirk, if okay with you, let's get started and make the most out of the call. Yeah.

4:29 | Dirk
Sure, like guys like interrupt me at any point or let me know what exactly you would want to see… but you've seen this before, right? Paulus?

4:42 | Paulius
Some sort of aversion, yes, I did see, but I think it is already advanced. So.

4:47 | Dirk
Perfect. I'll just give you like a very quick run through of our connections and routing. And like I said, this is all applicable globally. So what we have here is a list of all our providers. And basically what you will do is you build one integration with, you know, if you want to use our orchestration service. And from there, if you want to enable a new provider… you… guys are seeing something else than what I am seeing, which is funny.

5:28 | Paulius
Yeah, transaction lists.

5:33 | German
That's weird because.

5:34 | Dirk
That is not what I'm seeing.

5:38 | German
Maybe what you're going to do dirk is share your full screen.

5:46 | Tautvydas
There we go. That's better.

5:50 | Dirk
Perfect. I was sharing the wrong. I had the dashboard open twice and I was sharing the wrong one. So there we go. That happens live demos. So what you do is you build one integration with yuno, and if you don't want to start processing with another provider, you basically just enable that provider through the dashboard. So we were talking about India… got an Indian provider… give me one.

6:22 | Paulius
This razor blade build desk should be, I think you.

6:26 | Dirk
Mentioned that, but it's… but we for sure integrated with them buildesk. So what you basically do here, you just set up the account, you give it a name, the connection, you select what payment method. So in this case upi, you want to process and you just get your details from buildesk. In this case, once you fill that all in, you basically save the integration, you can fill in the cost. So I'm just going to fill in some dummy data here now.

7:16 | Dirk
I should be able to click through… and what you can do here, you can set up the cost. So based on the contract that you have for them, you just fill in the percentage and a fixed fee you.

7:44 | Dirk
Are you safe… save, your connection, then you add it to a brand. So… we're… gonna add it to the upi right now.

8:08 | Dirk
And this is basically where you build, how your payments will flow. So this is all based on different conditions so that you can decide to which provider which transaction is going. So in this case, we're going to say currency is equal to… Indian rupee and amount is oops. That was a bit too much amount is greater than 200. And what we're then going to say, we're going to add a step here. So this one is going to be processed through buildesk. Of course, a payment might get declined. So in case it gets declined, what we're gonna do, we're gonna add a step and we're gonna be processing it through the local. Of… course, we don't want to retry all the clients basically. So what we have also done here, we give you the option to group the declines by the client type. So for example, you can select them based on response code or mac code. So for example, if we say, oh,

9:42 | Dirk
not getting… them all here. Okay. That's weird.

9:55 | Dirk
Right. Browser doesn't unclick this. So that's weird. But in principle, this is always the, sandbox bug, that we run into during a demo, you should be able to in life select them, by the client code. And then you can say, okay, the one we're gonna retry, and the other one, for example, we're gonna not retry, so we're gonna say here… these declines, we're gonna retry on the local and I see that all the other declines, they just end. There. Are there any questions about that part?

10:38 | Paulius
Do you have a data based routing capability?

10:46 | Dirk
Sorry, I didn't did it fully get it. Did we have a writing capability on based on what?

10:51 | Paulius
On metadata? So now it's kind of some sort of fixed values like currency amount, etc, but let's say we do have certain situations where we need to pass certain metadata. Okay. Yes. So.

11:03 | Dirk
We have that metadata based on text and a number. You can at as much as you would like that. So yes, we do have that. I'll see you. One thing you might also want to do. So we're just gonna delete these. Of course, you always want to optimize for as much as possible for authorization rate. So we do give you the ability to split your traffic over multiple connections. And you can fill in yourself how you would like to split this traffic. So, say, in this case, we're going to split 50 percent over build desk and then 25 percent over the different D, local connections that we have. And we automatically then but randomly split the traffic. And then you can also define the retries per provider in there as we just did. Alternatively… you can let us decide using the smart writing. So let's quickly show what that looks like. So without smart writing, you can optimize your writing or actually you won't optimize it. You let us optimize your writing based, on two things. So we can either optimize for conversion and latency, or alternatively we can optimize for conversion and cost. One thing is there of course, that you have to have the cost set up in the connection that we set up that we just showed? And.

13:02 | Paulius
Transaction processing logic based on let's say if I want to prioritize network token versus pan or vice versa? Is it in control of merchant? Or do you just use some sort of default logic which tries first network token, then flow back to pan, how you handle this?

13:19 | Dirk
So that is set up by you year. So that is something you can define in your route, whether you want to try to process on network token or not for the future. We would be looking at something that lets us optimize for that as well because we know that you can know that some transactions have a better chance, to succeed on pan instead of network token. But there are optimization models that we're working towards for the future… so that you could leave it completely to us. And.

13:59 | Paulius
Your smart routing engine, is it trained on single merchant data or how you build the one behind the smart routing?

14:08 | Dirk
So when it comes to cost, it's of course based, on single merchant data because it's purely on the cost that you have. That when it comes to optimizing for conversion, and latency, it's based on platform data, okay.

14:28 | Paulius
You can take a look at how ESP performs across the platform, right? To make that routing decision. Yeah.

14:39 | Dirk
And also especially when it comes to latency, of course, we see that we could look at that platform wide… quickly. One thing to add here as well. We do have monitors available here where you can… easily like money or traffic. So say here we want to look at like a 30 minute window and your approval rate drops below 50 percent and the number of payments is above equal. Let's say like a normal number, 200 payments in 30 minutes, you can opt in to receive alerts either through email, obscene or both. Of course. And if this happens, we can also read your traffic for you. And what we will then do is, for example, if we see that one provider is severely underperforming, so say you're processing on Adyen, and stripe is severely underperforming. We will route all the traffic to Adyen, and like leave a small control group on stripe to see when it's back up. And, and we can route the traffic back to both providers, in the normal way.

16:06 | Dirk
Delta, go ahead. Yes. I.

16:07 | Piotr
Have a quick question if I may. So Pau, first of all, I wanted to say I'm still a loyal customer of hostinger. I have a couple of domains. I mean, daugas just sold me a hosting, right? So I know how kind of your payments work by the way, all my cards and paypal are basically tokenized. So, you just charge me yearly, right? But I wanted to ask, in sake for this. Let's say workshop. Can you tell us what is the split between let's say card on file and subscriptions per SE versus one time payment? Because I wanted to also touch with dirk's topic of donning and some more sophisticated engine we have for recurring payments. You know, not only those we trust, so can you tell us the split? You know, what is, for the plans for the yearly plans? Is it like 50 percent 70?

16:57 | Paulius
Mainly, we have yearly plans then it goes monthly and then remaining like two years, three years, four years. Around 70 percent of our dealings come from recurring payments like your Mit transactions and remaining like 30 are manual one time payments or card and file payments. I need to kind of check this. Let them those 30 percent. But, and our bread and butter, is subscription payments, right? So this is our focus, how we can convert as much as possible during the auto renewal flow without the customer being in the session without disturbing customers. So this is kind of our almost all the time.

17:39 | Piotr
Amazing. So, Derek, I don't want to interrupt you man. Just a few cents from my end, like if you can connect the, you know, idea of for dunning and three tries through the subscription engine. On top of this with our routing, this is super powerful combo and parties that's quite unique on market. I don't think anybody else has this coverage plus those products, you know? Yeah… yeah.

18:04 | Dirk
So, and I think this is also something, we touched upon last time, right? Where currently with your retries, you're basically… stuck to the time where the initial transaction was tried and that doesn't really give optimal conversion. So what we have on, you know, is we do have a subscription engine. It's it's one of our newer products where, you can handle subscriptions in multiple ways. So one of the ways is you just create subscription plans. So just… an example, here, we create a program here which is built, on a monthly basis through cards. In this case, it's usd. And I don't know what a pro plan costs for you, but, I guess it's we're just gonna say it's gonna be 50 usd.

19:08 | German
Gonna jump here really quickly. Yeah, there's four payment methods on our subscriptions engine. Right now. We're doing cards pics, automatico, apple pay, Google pay, and paypal. And we're finishing off the integration with upi out of a, yeah.

19:26 | Paulius
And how this sets your subscription, this mechanism, how it sits with the merchants billing system. So is it kind of separate or can it be somehow connected because, you know, we do everything in house, partly in house. And then this would look like a third part or like third pillar when it comes to managing subscription or plans, right? So it becomes?

20:00 | Dirk
So what is charge me currently doing for you, pavlis?

20:04 | Paulius
Currently, charge me is just issuing invoices. They are sending a request when the charge needs to happen based on the planned date. They would do configure dunning cycles in the charge B, meaning that, the retries until the, we exhaust it. So basically this information and then based on that signal, we initiate attainment through our tsps. So they just very basic billing engine for us. Nothing, nothing in smart or the engine features. Yeah. So.

20:42 | Dirk
Basically, what this does is it takes over all, the functionalities from chargebee except for the invoice creation at the moment. So starting a new Mit, is done by, would be done by, you know, subscriptions at that point. And also the dunning would be taken over, by, you know, subscriptions. So if a new shopper comes in and they sign up, you sign them up through, to the subscription using, you know, subscriptions. And then, when the next day first of the month comes, we automatically initiate a transaction, with one of your, one of the providers that you have. If the transaction fails, we retry them… either through a standard dunning schedule. We can use smart retries, which basically optimizes, for conversion or you can set your own custom schedule.

21:56 | Paulius
Okay. That. So basically, it's kind of as a standalone system almost and then just in which would we need exactly yeah, of.

22:05 | Dirk
Course, like if you wanna like, if you, we also do have merchants, who was working with say stripe billing, or charge B. However we do believe that our especially our dunning strategy and really outperforms them. And we also see, with mergers that we have on, you know, subscriptions that we can significantly lift our odds rates, on those Mit transactions due to a smarter dunning strategy. Okay. Subscriptions, we do have several features in there such as adding different phases, where for example, here, we can add a free trial to the package. We can add like different phases to it. So if you have plans where the costs are slowly ramped up, you can do that as well. Additionally, we do have something called meters where we could use some sort of subscription that is usage based. And you would just send the usage to yuno via API call. And we would keep track of how much one of your users has used and at the end of the month or the end of the quarter or whatever you set, we would bill them for their usage instead of just a standard subscription fee.

23:50 | Dirk
Anything to add Piotr on subscriptions here or any questions from your side, paulius,

23:59 | Paulius
I do want to add.

24:00 | German
Something before we get into questions, I'm actually going to steal your screen really quick. Sure… I created some of your subscriptions plans values here, in our dashboard and just to give you a sense on how things can look for you guys. So we can like jump into the unlimited for the eight month prepaid. And here you're gonna see a, what's the price in the subscription? How many, how many people you have subscribed to the plan? How many are in trial? In which countries you're moving that subscription and tying things up to what dirk was mentioning about meters. So I know you guys have like builder credits for with AI. I estimated you can charge you 40 cents per credit. And then this subscription will include only 15 credits. And then ever since credit number 16, the subscriptions engine is going to add everything up, giving you all the information on how much Herman in this case is using AI builder credits over what my subscription covered. And now regarding analytics in here, you can see basically everything you're going to have information about everything regarding your subscription. So how many have been canceled, how many are paused? How many have been upgraded and even downgraded? And you're going to basically have everything that we have on top on insights and everything on reporting. But here regarding everything around subscriptions.

25:53 | Paulius
Just trying to imagine how we would do this in our context because we already have a pricing and plan schedule. We have a running billing engine whereas I think like to be honest, it would be too much of a effort to migrate everything to outsourced party to manage everything from there because you kind of build a catalog which allows us to manage pricing plans, so on and so forth which interacts with our communication systems with the front end with customer panels, so on and so forth. I think like I don't see much of a synergy here for the subscription plan unless you have some sort of a smart subscription management which would work together… without any gaming that's not if we initiated that charge, you know, that it's not the perfect day to charge the customer. Then you say, hey, let's delay for 20 hours. And then you charge maybe some sort of this type of smart subscription management exactly but not like moving everything we have already built in house to, you know, to yuno's environment. I don't see that happening to be honest.

27:07 | German
No, no, makes total sense. Like replying your two different questions. For the first one, we can build a bridge between chargebee and how you're managing things in house and the yuno subscriptions platform without issues like that's. Something we've already been doing with some merchants that want to stay with their subscription billing engine. But then again, I want to try a bit on how we're doing things. So basically what it will do is that your billing system would stay the same and then like it will just give you the information to go and make the subscription, let's say active with your customer. So, you know, we'll be just like, the party in charge of going and charging for the subscription. And now, regarding your other question, of course, this has like what the subscriptions engine has behind is all of the routing section we just saw with dirk. So at the end of the day, we have all the smart routing and fallback strategies and whatever you want to whatever condition you want to add behind of the subscriptions engine. And of course, as dirk was showing also before, when creating the subscription, you can decide how the retries are going to work.

28:48 | Paulius
So basically, through routing rules, right? All the Mit routing plus retries is on the routing rules, right? And on top of that, if we put your smart routing for subscription payments, even if it's created on our side, if you see that this is the Mit charge, your smart routing engine would help us to let's say delay a charge or do something else with the charge production?

29:15 | Piotr
Exactly. Okay. Awesome.

29:25 | Piotr
Yeah. Sorry, if I may just say two words on top of this paulius, just to be super clear because those are still two different topics. Right? One is the engine. We understand that you have currently your stack. Let's say, what I wanted to emphasize is that what you saw exactly… there is actually ML and AI engine connected to this engine that it's not just hard retries, like charging one hour, one week. Of course, you can put a custom schedule, but actually you can let our engine to decide based on all the performance of all the merchants, similar accounts, et cetera, when actually is the best hour and time to retry, and how many times. So this is absolutely automatic and you can basically plug in into that logic and engine. And this is a machine learning module that is learning at least last six months behavior of our merchants. We believe this is good data. It's already live and happy to give it a try with you. But since I was not on the last call, I'm not sure, if we had the chance to take a look at also the routing section where we can actually add not only metadata but also a couple of other flags that may be interesting for you. Like for example, stored credential reasons, right? That you can differentiate that. Okay. Let's use this flow with providers, you know, stripe to braintree, to Adyen, if this is, you know, subsequent transaction and Mit. But for the first transaction, you can have definitely different, you know, flow and the plan and the logic of sending to the providers. Like maybe you wanted to have more sophisticated risk management, right? Or maybe you want to just send transactions that are first to specific mid on provider side to not let's say mess with your chargeback ratio, right? So, yeah, this is a question to you if you want, if you want to continue, with the routing or?

31:44 | Paulius
You know, I think it's quite good understanding when you're writing, right? Of course, all the nitty gritty details would need to then be learned by clicking it and going through each and every. So we don't have enough time, right? We have what 10, 15 minutes. But I would also like to understand because, you know, I don't know about switching orchestrators because now we're using orchestrator, right? It comes to migrating tokens right? Between orchestrators, right? You know, exporting our existing cards, existing users from one orchestrator, let's say in this case to yuno. So when this process happens, right? What is your approach when, you know, we kind of either we send or you export from our existing orchestrator the card information, what you do with it, right? What is the flow? Thank?

32:35 | Dirk
You, you know? So what would happen is you are largely out of that flow and we basically takes it on with your existing orchestrator or provider depending you said you're currently already on an orchestrator who have your tokens?

32:51 | Piotr
So they.

32:53 | Dirk
would basically share the card data with us and we would then give you a report after that transfer, which basically allows you to create the customers and attach them the correct token to them on the yuno side. And then you can replace the token that you have on your side currently from your current provider, and replace that with a yuno token. But the like the transfer itself is basically done by us. So you don't really have to have a role in that, and.

33:37 | Paulius
Once you do the transfer, right? So what you do with this schema, these network tokens, do you take it from the existing provider or do you recreate it on your side? How you handle that part?

33:51 | Dirk
So some of it we save from the existing providers. I believe that network tokens, but I would have to verify that we request them ourselves again. But that is also, I think per merchant specific depending… on how it is registered with the schemes.

34:20 | Paulius
Yeah, all the tokens we host with the providers are under our name. So I was just wondering, you know, will it work? Yeah. So if they're under.

34:29 | Dirk
Your name, we should be able to reuse them… but I will verify that to be 100 percent sure about that and follow up on that. Okay? So we don't make any mistakes around that?

34:51 | Paulius
Yes.

34:52 | Dirk
Because what are you basically looking into to switch providers and to use potentially use yuno as an orchestration platform instead of your current provider or just make use of our token services?

35:11 | Paulius
Well, in any of the cases, right? We would need to do the migration, right? Whether this is pre orchestrating or vaulting. So I really want to understand how the token migration works. So let's say once we migrate the tokens to the vault or to the orchestration platform, what happens with the network tokens and schema is because these are two very important aspects for recurring payment processing, especially the schema id. Because we do see when an orchestrator messes up for the schema id and uses not the correct one. We do receive the client's permission saying that they cannot trace back to this schema id. So we really want to understand how that works because it will be quite some number of tokens to be migrated. So just to make sure that we're not making it worse… no.

36:01 | Dirk
For sure. And we do anything we can to not let your alt rates decrease. Can you give me because you said it's quite a lot of tokens. Give me a ballpark estimate of how many we're talking about?

36:22 | Paulius
It will be a couple of 1,000,000 tokens, right? In total. If we migrate all the… customers, right? I think we wouldn't migrate everything, what we have in the existing orchestrator because some of the tokens are not used for some time. Some of the customers already kind of gone, they are not using our services. So it might be, but still a couple of 1,000,000 tokens for sure. They'll work. Okay? That's.

36:50 | Dirk
nothing out of the ordinary. I'll go out of there where.

36:53 | German
Were you storing tokens right now? Polish?

36:58 | Paulius
With the, with the orchestrator, they are also well there's.

37:03 | Piotr
yeah. You just asked the same question everyone I wanted to ask. So they are also to be on the same page, not let's say the network tokens on the visa and mastercard trails? That not so easy to move, right? So this is like vault of your current orchestrator that's it. Okay?

37:24 | Paulius
Okay. Yeah. And another topic for the migrating, the India topic, right? Because it is quite a country with regulations and no other stuff. I don't think it's going to be easy as migrating other cards. So have you ever done the migration of tokens from the indium provider? In this case, I don't build desk razor pay to your ecosystem because for India, we do keep the tokens and autopay mandates with the kcp directly, not with any of the orchestrator. So have you ever done the razor pay build desk migration?

38:10 | Piotr
Well, we are local in India. So we have different powers than other companies and I say yes because this is already a very saturated market for us and, you know, there's a couple of ways how to handle this values. One of them is that actually like, of course, please, don't take it as a plan, right? I'm just brainstorming with you and sharing how we've done this couple of times. So we can actually take the raw card data and re, tokenize with the plans that's one of the ways, right? But of course, dick will be back with the actually plan per, case by case. But yeah, like if I'm just saying if there's one of the options that basically reach out to the company, S local Indian company, yes, as you know, India, let's say and we do basically transfer, the rocker data and we're talking nice in our vault that's one of the options. Yeah.

39:08 | Paulius
Those details as far as I know… yes, please don't allow to share the tokens between each another. Now, it's only kind of pushing the regulation from central bank of India to allow exchange the tokens. But until now, I think it was not possible. So really would be good to understand whether you have the actual example in production which you were able to migrate. And now that work because maybe my knowledge is already, quite old, but I know that we were not able to migrate between providers, yes.

39:44 | Tautvydas
I can double check regarding that so I already could ask the question for the, our owner, of the vault. So I will come back with the answer. Nice.

40:02 | Dirk
Any other questions around tokens? India, migrations? No?

40:08 | Paulius
I think pretty good here saying if we can clarify for the idea part would really help us a lot. Yeah.

40:15 | Dirk
What I will do, I will give you a complete overview like a step by step overview of how we typically handle a token migration and which of the data we take from your old provider also depending on what, they can share, of course, right? That, that, that's also the second dependency we always have there. And then what, we need to request, and how we make sure that we don't see a drop in us rates shortly after, that migration process because like this is a, that a worry every merchant could have. So we do have a raise around that too to make sure that doesn't happen. And, we keep the alt rates up, and the business running as usual. Okay?

41:05 | Paulius
Wait.

41:10 | German
Amazing. So now, a, I mean, regarding how we're planning on advancing about values, we said, a call, I know just said that he's gonna give you information, on everything regarding how the process, of migrating works. But it will be amazing, to do a live demo and show you guys how we can do that. So if we can meet up with your team, it would be great to do that. We'll get the NDA going as soon as it lands. And yeah, it will give you all the information on how.

41:52 | Dirk
the.

41:53 | German
migration will work, and of course, the routing and the subscriptions. Yeah.

41:58 | Paulius
So, I will try to send that NDA shortly if we can focus on India because that would be a very straightforward case for us. Now, we handle it separately on the PSP level. It can move to the orchestration platform with proper workers, proper token storage, adhering to local requirements. I think that could be a strong case for us. This is kind of second market now in terms of size. So that could be a good starting point. And then a whole thing as a service also as a separate… that's good. Amazing.

42:35 | German
Is there anything you want to add? Tj? Maybe? Thank you. Very good meeting a.

42:43 | Paulius
Lot of insights. I.

42:44 | German
appreciate it. Yes.

42:45 | Dirk
Thank you. Yeah.

42:47 | Tautvydas
So, we're going to come back regarding the India case. Yeah.

42:51 | Paulius
We'll do that. That is quite important. Amazing.

42:58 | German
Great. So, Paulus, talk to you later. Thank you very much for your time. Great meeting. I.

43:04 | Paulius
appreciate it. Take care, guys. Thank you. Thank.

43:06 | Dirk
You. Bye.
