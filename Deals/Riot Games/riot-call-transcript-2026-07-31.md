# Riot Games + Yuno — Call Transcript

**Fecha:** 2026-07-31 (Google Meet, 23 min)
**Yuno:** German Tatis, Samuel Vieira Tamayo
**Riot:** Andreas Borngraeber (basado en Dubai; construyó todo el stack de payments de Riot; hoy lidera un proyecto confidencial en el espacio "commercial")

---

## Transcript

0:00 | German: Andreas, all good. And you great to meet you.

0:03 | Andreas: So far? So good. Great to meet you too.

0:06 | German: Where are you based?

0:10 | Andreas: I'm based in Dubai, but I've been like based in any other office at riot before. So this is where I'm currently at.

0:18 | German: Amazing, never been to Dubai, but it's definitely on my list.

0:22 | Andreas: It's warm go in the winter and the weather is better.

0:27 | German: Actually about four months ago, I was this close to moving to Qatar which is right beside, but with the bombing and everything plans went down, yeah, happens.

0:42 | Andreas: That's very unfortunate.

0:44 | German: Yes, definitely.

0:49 | Andreas: Can very quickly introduce myself. So my name is Andres. I've been working at riot since I've built like all the payments stuff there. Currently, I'm leading a project in the commercial space. Can't talk more about that before that? I've worked at trading games and was more on a financial role, basically also doing payments but also management accounting, treasury… and all that stuff. So it was more a role of a CFO. And before that, I studied economics. And as you may see from my name or hear from my accent, I'm not American. I'm German. So ended… by accident by right? But loved it. So I stayed.

1:38 | German: Amazing. Great to meet you. So German here, I've been for a year and a half in yuno, not as much experience as you do hopefully one day, but I've been in payments for that time. I've been in yuno.

1:56 | Andreas: Okay, nice. Cool.

1:58 | Samuel: Andreas, great to meet you, Sam. I joined Uno almost three years ago when we were a very small company right before the series a, and I've seen the whole thing grow and it's been an exciting journey. So, great to meet you. If you don't mind just jump right in because I know we only have 30 minutes. I know hideman wanted to set up this call to talk about payments at riot. Obviously, we don't have an NDA so there's a limited amount of things that we can talk about. But essentially, you probably know, we're a payment orchestration platform. We work with moonactive. We work with netease games out of southeast Asia. We work with some of the largest gaming companies that have not been announced yet… particularly in the orchestration business case. I'm sure you're familiar with it. I would just love to have an open discussion about what you guys have implemented so far. And if you're looking at all into orchestration, have looked in the past or will look in the future.

2:56 | Andreas: Yeah. I mean, obviously we're an online service. So there's not much to orchestrate it's like mobile is also like online. So we're like mainly doing CP business or cardinal present… business. Our setup works in a way that we build our own middle tier after having bad experiences with a third party platform that was like back in 2015. So about like I think five or six years before you guys were founded and migrated like all of our payments to that old platform. And since then we pretty much kind of use that as the central integration hub for all PSP vendor relationships that we're having and basically going through the feature list having fallback PSPS doing dynamic routing. All of that stuff is already built in. So we're fairly good on that end. So honestly, I don't think that there's like an overlap however in the future we might go like into also like physical stuff, there's like ideas floating around but not really concrete plans. So it's like a maybe. And so for that purpose, I thought it's good to just know you guys. The other thing that caught my attention is your recent utilization of AI, which is also a hot topic at riot. So I actually went through the documentation, read a little bit about it. And so I would just be curious, are you just kind of replacing basically rule engines now with AI agents and calling it all AI? What are your use cases for AI? Yeah, cool. Just.

4:53 | Samuel: So I can do like a side by side between what you guys have and what we have. So you guys own the tokens today, and you do the dynamic routing based on your own logic that you've built, correct?

5:03 | Andreas: Okay.

5:04 | Samuel: So your pci, you own the tokens. They're not on the PSP side.

5:08 | Andreas: So what we're doing is… we basically do not want to expose us to pci saqd level. So we work with hosted payment pages or hosted payment fields. The cards are being saved on the PSP end. And also the cards are being entered directly on the PSP side. However for like safe cards, we receive the hashed and salted tokens, that means the tokens are like bound to a PSP. So like basically our approaches, we have multiple games. So we have like multiple playgrounds, we test on like small games, what works best, and then give like a certain region, the business to the PSP that works best. And then when this PSP has a problem, like it doesn't happen often because we work with our partners but let's say a node goes down or like a service center or something goes down, then our system automatically observes that through increased declines. And in that case, we automatically move the traffic to the fallback vendor until like the primary vendor comes back on again… that brings us in a position where we cannot utilize like safe cards. But usually we talk about events of like five minutes, 10 minutes, half an hour that happen like once a year or once every two years. So like it's not a big concern for us.

6:44 | Samuel: Perfect. But per game, you do have traffic that's set to a particular PSP. And then only in the event that it goes down that's when you shift traffic, it's not.

6:53 | Andreas: I mean we can go on into the platform like changes manually anytime we want. But this is like how we decided to kind of configure it.

7:00 | Samuel: Okay, perfect. So there's a couple of places where we use AI the first place and I think it's the easier one to understand is all the logic of issuing, you know, issuing banks or bins or IP or, you know, over 20 parameters, metadata all that there is an option in yuno called smart routing. There is an AI model behind that basically allows you guys, if you want, to manually choose the routing, but you can put that against our own AI engine. And the idea is that there is as little complexity as possible and that you can route transactions based on our AI models which are obviously trained on millions and millions of data points that's like the easiest place to understand. It's just a machine learning model and you literally click a button and you select the number of PSPS upon which you would choose to, you know, the AI model to send the traffic and it'll automatically send the traffic, you know, per transaction, it'll analyze per each one of the transactions and send it to the PSP that's more likely to approve that particular transaction. You can set parameters to optimize for latency cost and auth rates. So it'll try to optimize between those three parameters. And if at any point latency goes up, auth rate goes down or cost is up because you have a particular cost with amex that you don't have with visa or whatever that may be. Then it'll dynamically route. The second thing that we have which is probably what you went through is payments concierge, the payments concierge is an interface. We basically integrated all of yuno to a centralized brain. We can give you a demo of this in a separate call. And the whole idea is that in natural language, you can tell that thing to shift traffic or to do something without any developers interfering with anything. Or you can have it pull reports or you can have it shift traffic. You can have it call the PSP. You can have it do anything. So the whole idea is that you can have an orchestrator that's very, you know, technically intense and needs a bunch of developers to maintain or you can have an orchestrator that only needs a few PMS and non technical people can administrate that orchestrator that's where we're leaning towards and that's where AI is within yuno today.

9:17 | Andreas: Makes sense. So basically, like the concierge is like replacing the admin panel. So, instead of like someone going in and changing it by themselves, you just tell the concierge. Hey, I need a report about this or I need like to change traffic. And for like this reason or whatever that's right? Okay. I see the concierge also.

9:37 | Samuel: Helps use setting rules. So again, you might say, hey, if my auth rate in this country drops below 85 percent, I would like you to automatically shift traffic to whatever you consider best, and you set the rule. Once in the concierge, it'll just memorize it and implement it across your stack. Okay. Yeah. So.

9:58 | Andreas: Basically, it's a layer that abstracts like, to like making the decision by yourself. Like how do you keep like track of all the changes that happened?

10:09 | Samuel: In the dashboard, there is a, you can track the logs and you can see whenever you talk to the concierge, what happened in the logs, and you can also do rollbacks immediately. So if something, if it changed something that you didn't want to change, you can roll back the thing automatically and it doesn't take. Yeah.

10:30 | Andreas: Okay. So it makes it easier to basically manage the payment stuff.

10:34 | Samuel: Yeah. I guess, look, from my experience, I've implemented orchestration at companies where there are teams of 40 people just to manage the orchestration layer. And the whole goal is that you don't need 40 to 50 people. You need a few that's what we're heading towards, because I have customers that have 50, you know, 100 person payments team. I have customers that only have a two person payments team. I think that's where we're headed. Yeah.

10:58 | Andreas: Okay. Excellent. Cool. When I look at your solution, that sounded to me, you're only doing the technical layer, but you're like not involved into the funds flow. Is that correct? Or are you also implementing a merchant of record model? No, that's correct, or only technical gateway?

11:17 | Samuel: Yep. We don't intend for now to touch funds of any kind. Yeah.

11:24 | Andreas: So, no desire for banking lessons?

11:27 | Samuel: Yeah, we like to keep our exposure limited there. Okay?

11:33 | Andreas: Makes sense. Cool. From your data center perspective. Like where is your stuff hosted?

11:43 | Samuel: Aws, three availability zones in the us. We also do Hyderabad and Mumbai in India for upi as you're aware, we have Saudi Arabia because we needed to get it licensed by the central bank in Saudi. And we're looking into not yet because it's not enforced yet, but we're looking into Brazil locally and Indonesia locally, and then frankfurt or Berlin. I forget which one in Germany, I think frankfurt.

12:18 | Andreas: Is the main internet hub?

12:19 | Samuel: Yeah. The simple one, the short answer is us for most merchants, whenever you have really great data requirements, we go and put the fancy stuff up. Yeah. Okay.

12:29 | Andreas: Cool. Makes sense. Why do is like saving headcount, the only motivation why people give up their own environment and move to yuno or like what would you see like the biggest motivation for customers doing that?

12:46 | Samuel: Not necessarily. I think that's one of the motivations but some of the recent projects that I've implemented like spacex and gofundme, spacex has a very small and mighty team. It's just seven people. Gofundme has like 100 plus people on their payments engineering team. They implemented, you know, but they didn't caught any heads. It was because they needed a ledger. So yuno becomes the system of record, their source of truth for absolutely everything that's what I just the head of payments at gofundme. And then building and maintaining that ledger is super tough. So yuno becomes that system of record for gfm. First, it was speed, you know, they have to launch in 200 countries locally instead of them doing an integration that takes a couple of weeks to certify et cetera. They can just call us and we can just spin up the integration in a few days and they're done. So, I think it's different case by case, but I think time to market is very big. Data is also very big. And then we're pci compliant. You can also offload your pci scope over to us tokens, can not, you know, they could not be on the PSP side. It could be on our side. And that way you can just send transactions to whichever PSP, you want to send.

14:00 | Andreas: So you're then basically meeting the saqd so that you're touching cards and processing them.

14:08 | Samuel: Pci level one, stock, two, GDPR, iso, everything instead.

14:13 | Andreas: Of pci level one is like about the number of transactions, but the question is like to which level are you exposed to data? So… the question really is, are you processing card data on your own systems and storing them on your own system that you have direct access to the pan? Or are you also just utilizing hosted payment fields from the PSPS? No. Okay. So you go like that.

14:40 | Samuel: We touch the card data, we touch the pan, we touch the cvv, we touch eii data, these kind of drivers. We touch all that. And there's particular requirements. So some companies require us to delete PII data within 24 hours of our servers. Like that is something we can do, but we taught, we see everything. We just don't process the payment. Technically, we just, the data goes to our pipelines and that's pretty much it.

15:06 | Andreas: How do you deal with fraud prevention? Like are you utilizing external services or also building internal ML, AI models for that?

15:15 | Samuel: Quick question. So, there's two things. One, you can set fraud rules on the orchestration level that trickle down to the PSP level. So like, you know, if you log into your audient account, that kind of stuff is also on a yuno level which will trickle down to the PSPS, but you can also implement a third party solution like fortr, like sardine, like signified all that via yuno, those are all created today. And so, with three DS as well. So we have our own three DS. We have our own fraud rules, and then we have a third party solution and you can just create a combination of whichever you want.

15:53 | Andreas: Okay. Makes sense. Cool… for the front end. How do you provide the checkout window? Is it customizable look and feel in the feeling of the merchants? Is it adaptable? So multi platform, how does that work?

16:17 | Samuel: Great. So we have sdks for web, iOS, android, react everything. So you can embed our sdks if you're pci, you want to do a server to server integration that's fair, you're not. So you're going to go with an SDK, you can have a full SDK that's a.

16:32 | Andreas: Deliberate choice why we're not, yeah.

16:35 | Samuel: So, you could have an SDK where you basically call an API and we give you back a response with the available payment methods that you can paint on your checkout. So you have full control of the way your checkout looks and feels there is just the specific fields for the credit card that are, you know, that we touch and you guys don't see doesn't go into your servers, but the sdks allow you to not get exposed to any of that data. Okay?

17:03 | Andreas: Cool. That's all the questions I had immediately. Anything I can help you answer?

17:12 | Samuel: No, I guess on my end, that's pretty much it, I could give you a sandbox account to play with. It's. Super simple so you can map.

17:21 | Andreas: Yeah, I mean, just to be open and honest, I don't see your solution replacing an entire solution. We have too much bad experiences with third parties basically doing the layer. So that is something we want to control even if it costs us a little bit more money. What I'm potentially interested on the road is like when it comes to orchestration, since we're not doing physical goods, that might be like something, you know, we could like explore when the time is right, but that is like not tomorrow. That will probably like take like a couple months or like maybe even like a year or two. So depending on like how those projects go. But I think it's like to just kind of keep contact and once in a while have a ping when we engage new partners, we pretty much do what you advised doing with the PSPS. We always run people through an RFP. It's never going to be like a straight sale into one merchant. It's like basically we compare like 10, 12 vendors on that space, and then have a list of criterias that are our current and future requirements as we believe. And then it goes like into like service offering pricing like last round of three negotiations. And then one of the lucky winners will be drawn. Yeah.

18:43 | Samuel: Understood. Perfect. And then just so you're when you said physical goods, do you mean like POS?

18:51 | Andreas: No, it's like right now, we're only selling digital goods meaning like skins or champions will appear on the account of the gamer. So for that, we don't need like address, right? But when it comes to let's say we want to send, I don't know some let's take a stupid example like leek branded chocolate to like a game. Then we need to kind of get their address. We need to verify that address is correct. And we need to kind of check with the warehouse. If we still have enough chocolate, then we need to kind of accept the payments. And then once the chocolate is ready to be sent, then kind of the capture request goes out because that's us regulation then chips. And then for whatever reason, you know, like the gamer decides he doesn't want to have like a leek brand of chocolate. So he sends it back. And then we also need to kind of recognize the return at the warehouse, tie it all back to the underlying payment and refund the money.

19:50 | Samuel: So like,

19:52 | Andreas: full use case, right? So like right now, it's like only digital. So we don't have this like whole shipping address, blah, blah piece. We have like only like this account wants this amount of money, give me a payment information. You got the stuff. And then there's still like cases of like refund, you know, we have that flexibility when they want a refund then, you know, like basically, we reverse like that chain. So it's fairly easy, but shipping physical goods basically mail order that's a bit more complicated.

20:23 | Samuel: Understood. Okay?

20:24 | Andreas: Super clear.

20:25 | German: I do have one question, Andres you mentioned having bad experiences with third?

20:30 | Samuel: Party vendors in the past. Could you?

20:33 | German: Walk us through what those bad experiences have been?

20:38 | Andreas: Yes, number one, that was before I joined riot. I think in 2008 and 2009. So riot developed league of legends. It was like a lot of money. I thought, OK, we're just going to engage a third party company called fat fugu doesn't exist anymore. The moment riot turned on payment, that system collapsed… and we were like out of money. So basically all the gaming engineers were getting into the war room and like building our own shop and own payments API in like six weeks and then did that. And that worked… then for basically international rollout, you know, like that was then migrated to another solution. I'm not saying the name because they still exist out of Korea… that was kind of our middle layer and that we used to kind of bring league internationally but it was like a solution only built for the market and was very difficult to scale globally let alone operate multiple products on it. But the thing that kind of really made us flip the switch was that their engineering environment was not as secure as they should have been. So they were getting attacked by a war which by only some stupid accidents and mistyping almost created… like a ddos complete ddos riot events. So only because the hacker mistyped some of our stuff that did not happen, otherwise, they would have been successful. So basically ransomware attack coming through payments. And so security and healthy level of paranoia is really big at riot and especially payments. We want to control our Destiny. And that's why we want to own the middle layer.

22:48 | Samuel: Perfect. Makes sense.

22:51 | Andreas: By the way, the current CEO was a CFO at that time and he was deeply involved into that thing. So as long as our CEO is CEO, there won't be a way in, but what I believe could work in a complementary way once you go into mail order. So that's why I basically offered to talk. Yeah.

23:13 | Samuel: That's perfect. Every few months, we can just send you something whatever and we'll see when there is an opening. Okay? Sounds good. Thank you for the time, Andreas. It was great meeting.

23:24 | Andreas: You, thank you so much.

23:26 | Samuel: Great meeting. You have a good one. Bye bye.
