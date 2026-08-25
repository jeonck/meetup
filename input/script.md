<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

 So the analogy here would be this, okay?
 So let's say you're in the kitchen, and kitchen, as in the commercial kitchen, and kitchen order tickets on a rail, right? And cook, pulls the ticket, and then, you know, when free, you know, when the rush is come, rush order comes in, the rush is absorbed by this ticketing system.
 Okay?
 And a drop ticket leads to a remake of the pile, right?


Microphone

 So, so what that is, is, if, if the, you know, maybe in our scene, we'll probably do this.
 She cooked for a long time, the spaghetti sauce, and she spilled it at the end, right?
 So when something like that happens, okay?
 Um, uh, in the cue, when something fails, you have this thing called the letter cue.
 So the letter Q is a function, or feature, of the simple Q service.
 So that if a worker is not able to actually complete the work, and they'll try several times, but if it completely fails, because of whatever reason, okay?


Microphone

 It goes into a separate queue called the letter cue.
 So the linocue are all these events that were supposed to been handled, but it wasn't because it failed.
 So you just don't say, well, hey, that's a lost cause, forget it.
 Let's move forward.
 No?
 Right?
 You have to come back and say, okay, so what failed?
 And what can we do about this?
 So that's basically what the letter Q is.
 Okay?
 Um, so, um, so drop ticket leads to a remake pile, okay?
 Now, for, if you wanna use something like a step function, you could do this, right?


Microphone

 But, you know, you could do this with, let's say, a, you know, repetitive, well running, fairly fixed flow.
 Um, you know, where you may have some human approvals, you know, uh, multi day weights.
 You know, something that happens in a fixed order.
 Yeah, you could definitely use step function.
 But for event driven orchestration, this is the pattern.
 So let's go over one more time.
 So you have the event sources, goes into the event bridge, which will buffer and also to route those action based on rules.


Microphone

 And you may put those things in a cube, as it's here, with a cube.
 Now you can tie the Asian workers into, you know, picking up the message in the cube at the speed that it needs to.
 So in this case, it's a lambda function, lambda function itself scales.
 So if a message or the queue starts to pile up with a bunch of messages, so there's their back pressure, lamb that can increase the number of instances that can handle these orders.


Microphone

 slash work, okay? And, but each land agent is one per vestige, because remember, it's, you know, doing small things, you know, one at a time.
 And lamb of function can store state information in diamond would be not inside itself, but inside external, like, persistent storage.
 Then, it could also kickstart, lamb the function can actually kickstart, step function, right?
 So long running application, approvals, et cetera, V tries, that could be offloaded to step function if you want, okay?


Microphone

 Then the cloud watch can be observing all these things.
 Re ready?
 So, the last part here, at the bottom, you know, why even driven for agents? Let's take a look, Agent Sipsaslo, first D, that's fine, right?
 And you want to decouple these sense, so that the whole system doesn't get, you know, kind of swung around every time they're supposed to be, everybody, you know, both in the hectic mode, and whatever is slow, and nobody's doing anything, right?
 So we want to separate those actions from and back.


Microphone

 So there you go.
 So that is one of the patterns in the orchestration.
 The Germanistic version versus Asian driven.
 So this is where deterministic is, you have a fixed flow of things that we don't have to make any decisions over.
 Um, you know, like a model decision, but if you need some judgment, uh, then you have an agent driven control system.
 right?
 So, you know, some decision, you don't always need a large language model or comedy, right?


Microphone

 There is a known, repeatable, you know, maybe compliance critical flows.
 That's usually deterministic.
 So, in case of deterministic, you use the function.
 That's a normal choice.
 Right? And you can actually, step functions are cheaper in that you could do testing of the flow.
 You can order it.
 Those things are, I think, it's still free.
 But we have open ended, you know, judgment heavy steps.


Microphone

 Well, let the agents decide, right?
 So that's when we use the agents.
 The mature design is a hybrid, right?
 So it mix those things together. So a state machine that calls an agent for the one step that needs that judgment.
 But for everything else, use a deterministic flow.
 So, for example, an analogy here is a trick, or rail, right, for the route that you know, and use taxi for the last mile that you don't know.
 Again, so there you go.


Microphone

 So that's basically how you would use it.
 Hybrid model.
 The sweet spot, okay?
 All right.
 The last part here is a summary, okay?
 Choosing which part did you choose?
 Is the pattern fixed, or does it have a known flow? Then you step function.
 It's different.
 Okay? Does it need a human like judgment to route, use a supervisor agent?
 If you have something that is spiky and you can separate out the front and the back, where they can communicate asynchronously, that is, they are decoupled, use event driven.


Microphone

 So use even bridge plus SQS power.
 And if you have an independent subclass that can be DV'd out for work, use the fan out, fan in.
 Found out, give a brick that has down into small pieces, or independent specialized pieces, and then send them off to different ages, and then at the end, synthesize the output.
 That would be the femine part of it.
 Okay, so that's it for this pillar?


Microphone

 And next, we'll be talking about the production, which is pillar number three.
 All right, so the next pillar, clue number three, is the production killer, right?
 So I have reliability, observability, governance, operational resilience.
 I think I've covered everything except for reliability, but, you know, I didn't say reliability, but, you know, we were talking about that, but let's let's take a look at it, okay?
 So, remember at the beginning, you know, how do we use these systems, or how do we use the systems?


Microphone

 So how do we want to use these systems?
 Well, a lot of us kind of end up with just creating the demos, who are proof of concept, okay?
 So, it works great.
 It's quick.
 You can impress others, right?
 On the happy path, for one user, or, you know, just a couple users, okay?
 But that is very different from making it work at the production level.
 Right?
 And it's something that's consistently works every time.


Microphone

 On the load, right?
 Um, across, you know, context, different contexts.
 I have here across tenants.
 And if it fails, that the surrounding systems, you know, dependencies fail, you know, you were able to be resilient and recover from that, with making sure that you have all the trails.
 So the difference between demo and production is night and day, okay?


Microphone

 And, you know, what we need is something that goes beyond the prototype.
 Right?
 Okay.
 But I gotta tell you, you know, devils are really fun.
 POCs are really fun.
 The tools are, you know, there's so many tools available that you can very quickly create the systems, but it's not something that is a production grade, right?
 Most of these.
 If they come to a point where, you know, creating these production rating systems will become very easily like how we create demos, but I don't think we're there yet.


Microphone

 Famous last words, okay?
 Um, but let's talk about reliability.
 So, remember the stochastic nature of this system? Sarcastic means that every time you ask the same question, sometimes, most of the time, you get a different answer, okay?
 That's the nature, right?
 of this.
 Now, all the generative AI in general, but I did say that you can actually put things before and after to make it so that it's not as stochastic, right?


Microphone

 But that's outside of the the power of the large language models.
 So, the nature is sarcastic, autonomous, if you remember.
 Okay?
 Distributed.
 means that things may fail in between things.
 Like mid flight, okay?
 So, that means when a thing, when the work is traveling from one Asian to the next agent, or from the front end to the agent, or what have you.


Microphone

 And things can fail.
 Remember, that's a distributed nature of the system that we're creating.
 Okay?
 So that means we have to design for it.
 Yeah.
 Okay.
 How do you get item potency?
 So, remember, at the potency, is you could be running multiple instances of a thing, like multiple instances of a Lambda function, and they don't step on each other.
 Right?
 You could do that, let's say, by using dino EV key, right?


Microphone

 So, um, making sure that some data is only accessible to a particular instance, and the other instances will override it, uh, or, you know, corrupt it in some way.
 Right?
 So, the retry, safe to run twice, right, down with EV keys, can be used, right?
 Just one example.
 Now, fullback keeps the system useful under partial failure.
 So maybe some answers can be cashed.


Microphone

 Now, cashing, as soon as you cash something, it's going to start to become stale.
 Right? But it's better than saying, sorry, I don't have any answers, right?
 So this will be failing gracefully part of the answer, okay?
 And maybe, sometimes, you hand it off to a human.
 Yeah, like, you know, we're not completely out of the picture.
 Okay?
 So maybe humans can be in the escalation path when something fails.


Microphone

 And so that means degrade, degrade, and do not collapse all at once.
 Timeouts and circuit breakers on every 2 calls, right?
 It says partial functionality, right? B is the failure, right? So that goes back to failures and time loss, crashing all of a sudden.
 So there you go.
 So this is how one tries to increase reliability of a service like this.
 Okay.
 So, let's take a look at this.


Microphone

 Observability and evaluation.
 The heart of operating agents, right?
 There are two ideas, okay?
 Tracy.
 So, the 1st one is tracing, and the 2nd one is evaluation.
 Okay?
 So observe and evaluate.
 Tracing is, by the way, one type of observation.
 Okay?
 So the one request, for example, let's say fans up, as you see, right?


Microphone

 One week plus fans out into multiple, into mini model calls and tool invocations.
 So that means you need to have tracing feature that follows each of the path.
 You need to distribute the tracing.
 And that's basically what ate of this x ray will do for you.
 Okay?
 So that you can reconstruct exactly what happened in this very complex distributed setup.


Microphone

 Then you have an evaluation, so the evaluation is where you have a unit test, assume determinism, so that means, you know, whenever you do unit testing, you know that, you know, what actions you're looking for.
 Now, agents are not deterministic though, right?
 So you cannot do a traditional unit testing for agents.
 So you need some evaluation sets that score, like, quality, and catch, uh, regression.


Microphone

 So the regression means something breaking.
 Okay?
 All right?
 So catch regression before you ship the product.
 Okay?
 And, you know, put all arms on it, you know, when something changes.
 So, for example, analogy would be a flight recorder, right?
 So, uh, flight reporter, uh, would be, you know, a failure once, in 50 runs is only flexible if every decision and tokens was recorded, right?


Microphone

 So, um, you record everything.
 Get you record everything, right?
 So there, at the bottom, let's go and take a look at the flight reporter.
 You cannot debug what you cannot see.
 Right?
 And stochastic Asian, that answers differently every time, that fails once in 50 runs, okay?
 But the thing is, the 50 runs may have different output, even though the question may have been the same.
 Right?
 is only flexible if every decision, 2 calls and tokens, was reported, right?


Microphone

 Because you can't, because it's not deterministic, you can't say, well, you ask this question A, so it's gonna go to 8 floor A.
 No, uh, the question A can go to, you know, 50 different, uh, you know, paths, right?
 So you can replay the exact run that was wrong at that moment.
 Okay?
 So, you see, it's very dynamic, right?
 Okay.
 So trump shooting, I think, is gonna be a bear.
 But that's the way you would do that.


Microphone

 So what are some tools?
 Okay?
 So you have traces, full step by step, metric, latency, logs, what was the information that triggered the stent, right?
 And the observability is card watch, x ray, and cost.
 So, what's interesting about observing using cost?
 And tokens, how much token it was used, okay?
 Is that, uh, let's say you have certain ideas, balance, as to, uh, what what it should cost in general.


Microphone

 Both the under cost and over cost are both troubles.
 Okay?
 Because under me, okay, so why is it cheaper, like, way cheaper than what I expect?
 Maybe it's because hackers have shut down some systems.
 How about Uber spending?
 We tend to concentrate on, wow, this is more expensive than, you know, what I expect.
 And cheaper is okay.
 But over is also, you know, that's a red flag, right?


Microphone

 Because, yeah, you know, something is just going out of whack, right?
 Going berserk.
 But I just wanna stress to you that the underspending, wow, it's so cheap, it's so nice.
 is not always the case.
 Well, it's so cheap, maybe there's something wrong.
 Okay?
 So kind of keep an eye on that.
 And then, we have the evaluate, right?
 So offline evaluation, um, bedrock model evaluation here, so, you know, you could put scores on quality, um, and, you know, you could do before releasing these, uh, you could do a sarcastic system.


Microphone

 Is regression test, too, as well, just like regular testing.
 Okay?
 And then have an alarm with the model starts to drip.
 So when we talk about model drift, drift is, wait a minute, you know, this model, this system, used to give me, like, great answers, like, a month ago, but now, oh my gosh, you know, all these answers are, like, off.
 Like, what happened?
 At the drift.
 Okay?
 So maybe it's time for some of these models to be retrained, or maybe a situation has changed.


Microphone

 The world is a new place, and the model hasn't caught up to it.
 It could be mini, mini things.
 So it's a very common thing for us to, when we're operating on these agendic systems and involving models, then we have to always be sensitive to drifts that is going off of the expectation.
 The model will answer degrading.
 All right, so let's take a look at the security and bounded autonomy.
 Yes, you want agents to be autonomous, you know, making decisions, but within limits, right, within limits.


Microphone

 So, because autonomy, a good thing is also the attack surface.
 A tax surface is where attackers, hackers, whoever, with malicious intent, can actually touch the system, do something bad to it.
 Okay?
 So, each layer, see, I have them in, like, a little, like, um, layers, right?
 You have the agent, the guardians, the identity, the balance of economy, all the transability, right?
 All those things.


Microphone

 We call this insecurity, a layered security, or defend in depth, because one layer can fail, and you don't want that to be the only security feature, right?
 You want multiple security features, and we're not looking for same type of, you know, security feature.
 And, you know, if you have, you know, physical building that you have to protect, we're not talking about putting, you know, three fences around, you know, one after another, the auto fence, the inner fence, the middle fence, and the inner fence, right?


Microphone

 Okay?
 Because if people know how to go over fences, they could probably go over all the fences.
 So we want to have different types of security controls in layers.
 That's basically what you see here, right?
 So, with agents, with, you know, models inside, you may want to filter what comes in, what's being asked, and what goes out, the output, so that's the guardrails, right?
 So that's the input and output filtering, and bedrock has that, right?
 Bedrock has those bedrock guard rails, okay?


Microphone

 Then the identity, remember, each agent is a, you know, it does one thing, it does one thing, well, and it's small.
 And we assign identity separately to each tool, each agent, each application.
 So you don't, you know, group multiple things that does different things into one identity.
 That's a bad, bad design.
 So there, identity, I am, least privileged, per agent, per tool, okay?
 Then you have bounded autonomy.


Microphone

 So you limit their actions, you know?
 You have some list of things that they can do, right, in the loop, right, for the high risk type of stuff, right?
 So that, you know, you yeah, you let them do certain things, you know, autonomously within limits.
 Then, if something does go wrong, you have the audit and traceability.
 Now, all the trustability isn't always after the fact.
 Because these days, these auditing and traceability data can be monitored in real time.


Microphone

 Right?
 So security operation centers or socks usually do that, right?
 They're looking at these logs, and then receiving signals in real time.
 But traditional sense, you know, we're looking for after the fact as well.
 So that's for forensics.
 So we can use the all of the entraceability in real time, as well as for forensics use.
 Okay.
 So, see those things at the bottom, prompt the injection, prove it just escalation, data extrotation, rogue actions.
 Those are all attacks.


Microphone

 Prompt injections, I'm not sure if you know what a social engineering is.
 So social engineering is hacking the human, right?
 We lie to people to make them do things that they're not supposed to do, or reveal information that they're not supposed to reveal.
 Well, guess what?
 You could do something similar to large language models, right, into models in general, but large language models are usually the focus of these attacks.
 Um, so you, let's say they're not supposed to give you any sense of information, but you socially engineer, right?


Microphone

 In quotations, the large language model, by prompting, that is to telling it to do something, that will circumvent the filters that they have.
 Okay?
 So, you know, once again, this is not a security class, but this is a very, very interesting feel for me.
 So, you know, socially engineering, the large language model is one of my interests.
 Right?
 No, I don't do illegal activities, right?
 Okay.
 But anyway, so prompt injection.


Microphone

 previous escalation, I've already mentioned it, it's where the, let's say, a application is, you know, told that it can only do A, B, and C, but, you say you give, you know, you allow it to do D, and E, and F.
 So, you know, your elevating is privileged.
 And when you have a flawed, I think the next is management, one can do this, right?
 Now, eight of uses I am is pretty, uh, pretty good.
 So, you know, I suggest using IM to limit the capabilities of a particular application.


Microphone

 But religious escalation is a real thing.
 Data, infiltration, another word for the leakage, right?
 So people are taking out data, sensitive data from a system that they're not supposed to release that information, right?
 So, um, you know, so the guardrails exist for that kind of purpose, uh, and order and traceability exists for that kind of purpose.
 So we're trying to prevent people stealing data.
 Okay?
 And by the way, the prompt injection is one way of actually X filtering data, because if the data resides, and it's controlled by the, let's say, large language model, and if you could fool it, to say, that's okay, you can give me that information.


Microphone

 Yeah, no problem, just give it to me.
 And then the sense of data is now outside of the system, that is a data exploration.
 Rogue actions?
 Sure, right?
 So if one can do privileged escalation, you know, you can ask the tool to do something that they weren't meant to do, since those are wrong actions.
 So that's why we need multiple layers of security, right?
 Defend them down.
 Please remember that.


Microphone

 Okay, cost optimization.
 Yes.
 We want to get the best at the lowest cost, right?
 Low cost doesn't always mean inferior, you know, product, right?
 So the Asian cost is a function of how much the Asian thinks.
 Yes, okay?
 Um, kind of think of it, right?
 As they're thinking in words, and words, the tokens, right?
 It's not just about asking how many questions, like, oh, I only ask one question, how can it cost so much?
 Or man.
 I asked 100 questions and yeah, boy, it's so cheap, so it got, you know, it's great, right?


Microphone

 It's not that, right?
 It's not just the request count, okay?
 An agent, stuck in a reasoning loop, doing a do loop, okay?
 Burns tokens very fast, because it's thinking the same thing over and over and over again, using many, many words, right?
 Meaning tokens.
 So, you have to control that.
 Because sometimes, you know, as people may go into doodloop in their brain, the Asians may also do go into loops as well.
 And we're talking about the models, okay?


Microphone

 So we could put an iteration cap.
 How many time can you go through them, right?
 Do you only allow 10 times, or do you allow, like, 100 times?
 Okay.
 Right size models?
 Yeah, so use a, you know, cheaper, more economic models, if that works.
 Prompt cashing?
 so that you cash certain results.
 You know, we use cashing all the time in regular systems, too, and then there's no reason why you can't use that in the system.
 If one is being asked to, you know, ask similar questions every single time.


Microphone

 Short circuiting or high confidence?
 Um, and so, you know, you don't have to go through the entire process if the confidence in the action or the result is, you know, pretty high.
 So make puff visible per agent.
 That is, you can attribute costs to certain agents and, you know, their work.
 And per tenant, right, the people who's using it, so you can see which workflow is expensive, and whether it's worth doing it or not, right?


Microphone

 But that happens over time, right?
 So you have to be monitoring that, and you have to be, you know, trapped in costs.
 Governance and responsible AI, right?
 So this is in the realm of the company, the corporate, and, you know, one cannot say, well, I'm gonna use AI, but AI is black box.
 So, you know, if AI gives back certain reply back, you know, we're not responsible for that.
 Of course you are.
 Okay?
 So, got this, is it design principle?
 And, uh, if you're familiar with AWS is well architect in the framework, uh, you know, from governance is a design principle.


Microphone

 especially from a well objected lens.
 So not a compliance afterthought, right?
 It has to be in a design, right?
 So the oversight should be, you know, tiered to risk, and, you know, can you reverse it?
 So, you know, this also costs, it costs too, right?
 season free.
 Uh, so, you know, make sure that it's prioritized, uh, and then, and here, based on risk, and we call that risk-based, okay?
 And because these systems are continuously operating, continues evaluation, keeps the system, you know, aligned as, you know, as the data and model starts to drift, right?


Microphone

 Because drifting could eventually cause you to break governance, you know, provinces.
 So, um, you know, also, in these AR systems, we're not necessarily talking about 100% AI.
 You know, in some of these, you know, perhaps in many of these systems, especially for governors, you need human in the loop.
 Okay?
 So leverage your people.
 We're not replacing them, okay?
 This also keeps the institutional knowledge alive as well.


Microphone

 So I say, well, I don't know, I don't know anything about our system, but our database knows. Okay.
 No, okay?
 People have to be smart as well.
 on their business.
 All right, so the next one is going to be pillow four, five will be proof of concept, two, production.
 Okay, so let's go ahead and talk about pillars 4 and 5, which is from proof of concept, to production, right? That's what our goal was.
 Uh, so deployment stages, uh, strategies for moving ejectic workload from idea, uh, to production grade.


Microphone

 Okay, let's take a look at that.
 Okay, so let's take a look, okay?
 So, you want to have a production protest, go into production.
 Okay.
 All right.
 So you give teams a staged path.
 A stage path.
 Small steps at a time, so the production ready is not as one terrifying, terrifying leap.
 Okay?
 So, phase one is one agent, one job, prove its value.


Microphone

 Remember, agent is supposed to add value.
 Or be it small, but still a complete value.
 Okay?
 Phase two is tracing.
 Remember, we have to trace, do the evaluation.
 Remember observe, and then evaluate, right?
 And then maybe retries, but for failures, guardrails, for limiting is behavior.
 These privilege for security, right?
 So now we start to wrap this agent around all the scaffolding that will, you know, productionize it, making it reliable, right?


Microphone

 Which we just covered.
 And phase three,
 Now we can start to put in multi agent.
 Right?
 And then multi agent, make sure to have cost attribution per agent per tenant.
 Do the load failures, you use the failure testing, right?
 So scaling.
 Mostly horizontal scaling, but, you know, can it handle the production globe?


Microphone

 And phase four, the, um, agent operation, human oversight, um, match to the risk and to the business.
 Right?
 So, um, from a, well, octic perspective, so it does the best practice, um, perspective.
 You want to start to crawl, they'll walk, then run.
?
 Take baby steps.
 A, you know, and so first, initially shift a narrow agent to production early, and then learn from that, right?


Microphone

 Gain experience from that.
 I mean, this is still a new thing for a lot of companies, and, you know, in the industry as a whole.
 So then, you know, start to get into the game and to mature, you know, as the industry matures, and the sector matures.
 Rather than, you know, chumpy right in, uh, and, you know, uh, uh, not learning anything in fit, making horrible failures, right?
 So, yeah, small steps in steps as I have here.


Microphone

 Asian thoughts.
 Okay?
 So, Asian thoughts is related to devots.
 If you're familiar with Delox, right?
 So with dev offs, it's a, when you create a new application, you want to put that out to production as quickly as reasonable as possible.
 And the way to do that is to reduce friction in the process, right?


Microphone

 So, and this is also related to, you know, the time to market.
 So how quickly can you put reliable service and value out into the marketplace?
 And that's how you win in business, right?
 So it's very similar to that.
 So, we're gonna bring DevOp's discipline to agents.
 Okay?
 And so that means prompts that we use for the agents and tools and definitions, right?


Microphone

 Our code.
 They all code, right?
 So that means if they're code, you can keep versions of the code.
 You can review the code, you could test the code, right?
 Just like any other important business applications that we have.
 Then, we'll have gates to release these codes, you know, from development to quality assurance, to stages, you know, staging, and then to production, right?


Microphone

 And others.
 And then, based on the evaluation scores that we maintain,
 and roll out gradually, right?
 Not a big bang, and watch the dashboard for the metric.
 That's what we do in Devos, right?
 And if something goes wrong, roll back instantly, right?
 If the quality or the cost regresses, that is, if they break, okay?
 So that means you have to be able to roll back to the previous state, the previous known good state.


Microphone

 So that needs to be in place.
 So, for example, in regular application building, you would not deploy a microservice straight to 100% with no test and no rollback.
 No, right?
 Because something can go wrong.
 So, the agent deserves the same type of handling, plus evaluation gate, because, because it's sarcastic, right?
 So it makes things a little bit more dynamic in a, you know, a bit more challenging, but that's the nature of this system.


Microphone

 Okay, so you may be familiar with well architected framework.
 A Davis's best practice for club, okay?
 And it does have six pillars, okay?
 So this is not a, this thing.
 The walk, the AILS.
 It's not a brand new set of pillars.
 This is a, as well, architected framework, not a new pillar.
 The same six that you already know if you already use it and reference it, it just re-examine for systems that reason, act autonomously, and behave sarcastically.


Microphone

 So that's the agentic system.
 It is downloadable.
 Um, and you could, you could definitely import it into, well, arctic and tool, if you're familiar with the tool, is a free tool that's available on AWS, uh, to measure how well you align with these best practices currently, and you could keep track as you improve and mature in the process.
 So the, uh, you know, it does recommend it as a checklist for reviewing anything, um, you know, uh, you build, um, after today, and hopefully you just download it and use that.


Microphone

 And it does actually neatly kind of encapsulate this webinar, because each pillar echoes the suction that we've, you know, we just covered, okay?
 So take a look at it.
 Now, here is a kind of biffle, just to kind of, you know, we can see, because we don't fall in your face, right?
 It's a never will wait to remember, do not do this list, okay?
 So let's take a look.
 Over agent time.


Microphone

 Okay, for Asian time.
 That means if the Asians are not what you need, don't use it, okay?
 And use it reasonably.
 So if the workflow, just like it determines the workflow does it, then do that, okay?
 Now, we're talking about agentic architecture.
 not talking about the, you know, machine learning in general, but, uh, you know, same, same thought actually goes in.
 So if a company is trying to decide, should we use a, you know, artificial intelligence, a machine learning, to solve this problem?


Microphone

 Or should we just go and use a regular program?
 And if you could think of a way to write the regular program, you use that.
 It's simpler.
 more deterministic, okay?
 But if the problem that you try to solve is not going to be easily done in the program, then, yeah, machine learning is a great thing to consider.
 Same thing here, right?
 Asians aren't the only thing.
 Okay.
 Anyway, the next one is unbounded memory and reasoning loops.
 Yes, right?
 It got to blow out the cost.
 You know, infinite amounts of memory, infinite number of loops, if you have infinite amount of money to, you know, handle that.


Microphone

 So, you know, bound up, okay?
 Keep them in certain limits, put caps on them.
 The third one is admin scope agents.
 Yeah, right.
 No.
 So, the, you know, security incidents will follow, don't do that.
 Uh, I know it's easy, uh, to say, oh, you know, all the security limitations is, like, really hampering me from doing stuff.
 Just give me all the power that I can use.
 No, because you can make mistakes.
 You could be hacked, right?


Microphone

 And then hackers will have all the power.
 So, yes, right, no admin scoped agents.
 Okay?
 No agents that have administrative privileges, right?
 Just enough privilege, this privilege, to do their work.
 That's it.
 No tracing, uh, right.
 Then when something goes wrong, you won't be able to identify them quickly enough in the efficient manner.
 So trace, right?
 And remember the stocastic nature, right?
 Because the path may be different for a same question that's asked different times, you know, different, you know, days, right?


Microphone

 So the agents may take different take different paths.
 Um, because of the stochastic nature.
 Shipping without evaluation gates, yeah, right.
 No, right?
 Okay.
 Silent quality regression, so regressions do happen.
 Drifts do happen.
 The models will start to give you wrong answers, wrong end, you know, or inappropriate answers, because the context change, right?
 So, yeah, we have to make sure that we evaluate, make sure that everything's okay before we ship.


Microphone

 And then, um, continue monitoring, uh, for drifts as well.
 Okay, so recapping the fiber objectives here?
 So, um, check it, let's, you know, check it, make sure that we cover these things, uh, in the, um, the webinar.
 So design scalable architectures, right?
 So that's because production ready also means it is scalable.
 Okay, straight, if you have a multiple agents workflow, then yes, orchestration is needed, and we talked about certain orchestration patterns as well.


Microphone

 Build reliable, memory tools, secure data?
 Yes, right?
 So we just finished talking about that.
 Operate, observe, govern, and resilience?
 Yes.
 Right?
 It constantly needs to be observed, because things, you know, things do great, things do regress, and things do drill.
 And then deploy the POC for production, so we went through the stages, okay?
 Don't do a big bang.
 What you can, but it's very risky.
 and very stressful, I'm sure, right?
 To your team and also to the customers, too.


Microphone

 Now, for those of you that are thinking about going to the next step, and I hope you are, here are some resources and next steps.
 Eight of us well architected framework with the agentic AI list.
 And don't... Or import it into your... or, um... Well, Arctic II, to evaluate where you're at, so that event with your readiness, to move into, um, to the...


Microphone

 Eight of this agentic framework.
 And there was prospective guidance.
 So, you know, they offer the patterns, uh, and, you know, how do you put into production the agentic AI?
 So, uh, guidances, okay?
 Very, very helpful, because, you know, we're not starting from 0 here, right?
 We have experiences, we have lessons learned, so let's learn from those past mistakes and past successes.


Microphone

 As a bedrock, Asian core step functions, so these are the core services that are available, so check out the documentation and perhaps learn about more about these tools.
 Nepcom continues the adds to the most, you know, the latest and greatest, you know, technology trends.
 So, related agentic AI and AI of his courses are available.
 So please come back and check us out.
 Slides and diagrams, right?
 So these will be shared, because some of these, you know, diagrams that I created for you are little, you know, detailed, a little bit busy, right?


Microphone

 So take a look at it.
 Uh, you know, and try to digest as much as you uh, you need to live, literally, later on.
 So check those things out.
 Okay, so what I want to do is, this is appendix, but, um, let me, uh, go ahead and walk through, just one scenario, uh, that, uh, that shows you what an ejectic, um, system, um, can do.


Microphone

 Okay, so I've created for you a simple walkthrough of a fictitious system. Okay, just to kind of demonstrate all the pieces that are usually found in the agentic AI system.
 So it's just one slide, so let's take a look at it.
 So we're gonna put it together.
 Customer support triage agent.
 Customer support triage agents, and that usually means, you know, when customer for customer support, when somebody asks a question, you have to decide, okay, how do I answer that?


Microphone

 Is there a simple answer?
 Is there a complex answer, or do I have to send this thing to a human, right?
 That's usually what happens.
 And of course, not just the output, but you have to also maintain the stability reliability of the system itself, the infrastructure, and the components.
 Okay.
 So here, let's take a look.
 The customer, number one, asked, A, where's my order?
 Okay, maybe for e commerce systems, okay?
 Then, that request goes through the front end. So, it's gonna go to the tree as the agent, but it's gonna go through the API gateway.


Microphone

 APA gateway usually is a gateway into the internal systems.
 Okay? And put in the system here, the filter for the input that is coming in.
 So I have a plus guard wheels in, okay?
 So instead of asking, where's my order, you know, maybe I could ask, where is somebody else's order? Or ask something completely different?
 Okay?
 Right?
 Give me your credit card information, whatever, okay?


Microphone

 So we need to have the guardwheels to filter inappropriate type of prompts that may come in.
 So that's number two.
 Then, the request via the AKA gateway reaches the triage agent.
 So this will be in the Amazon bedrock system.
 So here, the actual agents themselves are limited to looking up the order, right?
 So here, we have to kind of look up the order, perhaps use a Lambda function, and use the orders API. That is connected to the enterprise system that has the list of all the orders.


Microphone

 Or perhaps reach into a knowledge base using rag, and, by the way, rag stands for... for the, um, request augmented generation, okay?
 So that's reaching into the data source.
 So, these are the things that may happen with the triage.
 And then, route that output from those individual tools, look up order and search KB, knowledge base, to a routing to the decision point.


Microphone

 Now, so decision point could be,
 Hey, is this a, like, a simple answer?
 Did I just get the answer already?
 Will I search for it?
 So answer directly, right?
 Simple question, reply back directly, okay?
 Um, however, if they ask for, who is my order and it needs to be refunded, maybe the, there, there must be another workflow, let's say, for refunding.
 So, if it's refund, um, refund workflow, maybe deterministic workflow based on sub function.


Microphone

 Even with the human approval, perhaps, right, before the money is released, maybe a human has to be in a loop.
 Okay?
 Or, perhaps, it's something that the agent is not able to handle, or it's been flagged as something that must be escalated to human.
 So, uh, perhaps put these requests into, you know, queue them in the SQS, and the SQS, maybe an Asian inbox, right?
 that can notify humans using something like SNS, simple notification service, so that a person, a real human, can handle it.


Microphone

 And before the money can be refunded, if this is, indeed, a refunding situation, we have approver, and then the actual payments made, external, right?
 Using external payment systems and such.
 And so notice how this actually, you know, connects the agents as far as the large language models are concerned out into the real world.
 And literally real money, right?
 In this case.


Microphone

 So underneath each step, we'll use other infrastructure components.
 So, dynamo DV for states and memory, called watch for traces, uh, latency, uh, of the, uh, system itself.
 Guardrails.
 Now, this one here is the Alka rail.
 So when the reply is sent back to the customer, making sure that inappropriate information is not returned.
 So this is a, um, you know, TII, so privacy related data is redacted, um, you know, based on your company policy and also compliance.


Microphone

 And then even bridge will emit events when certain events happen, right?
 So if it's event driven, event bridge is often used.
 So how does this all fit together, as I have it here?
 Right?
 Is that one support triage agent uses every service that you can see here.
 Bedrock, lambda, step function, event bridge, SQS, animal TV, codwatch board, right?
 So there you go.
 Because ADVS is the premier service of infrastructure components, and now, they are, you know, giving you a very powerful AI and agent based system infrastructure and components as well.


Microphone

 Okay, so I hope that gives you a good overview.
 And next one, thank you very much for all the questions that you've been sending in, so we'll be covering the questions later next year.
 Thank you to ruin me.
 That was most informative.
 Now I'd like to give the presentation rights over to Remy, our vendor manager, to introduce our promotions and webinar related courses.
 Uh, thank you, Trish.
 I believe everyone must have learned something new today, or would have been able to brush up their skills around the fundamentals of AWS Cloud.


Microphone

 I would quickly like to take you through some of our hand-picked resources, which we think will immensely help in accelerating your AWS Cloud scaling journey.
 Well, this document here, I'm sharing on my screen, this has been shared with you all in the handout section of go to webinar panel.
 You can download this document and access all the resources and browse all the offerings we have to wait for.
 So, 1st off here is the list of our recommended courses, which we feel will best suit your learning journey after attending our master class.


Microphone

 All these courses are hyperlinked.
 Feel free to go through them post-event and check out the course descriptions, pre-requisites, and the value.
 It can add to you and your team skill sets.
 Additionally, we have created a blend of resources, including our upcoming and on demand events, as well as informative and educational blog.
 You can make the most of these resources to gain extensive knowledge on the AWS topics they cover.
 Our free AWS E-Learning courses follow a self-paced training model wherein you get the liberty of accessing extensive course related videos that are delivered by the AWS Subject Matter experts on the go.


Microphone

 So these videos cover the availability on the device of your choice.
 So you can access them from your laptop, your tablet, or from your phone as well.
 There are more than 280 videos covering various AWS topics explained in a very easy to comprehend language.
 You can simply sign up for free, watch these videos, and make the most out of them.
 Also, here, I would like to inform you that this session is being recorded, so in case you want to refer back to any of the topics that the trainer might have covered in today's session, we will be sharing the recording link with you, through emails, and also, you can access it here by taking on this button.


Microphone

 So you have to download this handout for that. And then if you want to revisit any topic, you can just simply click on the access recording and you can revisit the session and learn at your own pace.
 Now, apart from our virtual sessions, you can also catch the relevant updates related to IT and business trainings on our social media handles, so please feel free to follow us on LinkedIn, Twitter, Instagram, and subscribe to our YouTube channel for all the latest updates.


Microphone

 Our official pages and channels are linked here on the icons.
 Finally, if you have any suggestions regarding the topics you would like us to cover in our upcoming webinars and masterclasses, please don't hesitate to send us a direct message, or you can leave a comment on our social media posts, or you can just simply email us at info at theratenetcomlearning.com.
 We would definitely try to come up with the sessions on your suggested topics.
 Thank you once again for joining us today.


Microphone

 Over to you, Tracy.
 Thanks so much for guiding us through that information, Remy.
 And now we're going to go ahead and jump right into our question and answer session.
 All right, so let's go ahead and see if I can answer some of your questions.
 Uh, looks like we have five questions, okay?
 So let me read the first one.
 Um, a person asked, uh, when is a single agent, you know? So, when do I actually need multi agent?


Microphone

 And I did cover that in the webinar.
 So the basic default is the single agent.
 So if single agent does the job, go to the simplest app first.
 You do multi Asian, only when you have really separate domains.
 The domain, what I mean by that, is business domain.
 Oh, so this would be a different business domain of expertise, specialty, that doesn't really fit into one prop, one pool, right?


Microphone

 When, or when a pass can run in parallel, and the coordination overhead is worth it, right?
 So it's a cost benefit analysis.
 Okay?
 So if you can't really, you know, articulate clearly why a specific subtask needs its own agent, then you probably don't need a multi-agent.
 Yeah, you probably, you know, just need a better tool.
 I will prompt, own one agent.


Microphone

 I hope that's that answers that.
 Second question.
 Let's see, how do you test or evaluate something non-deterministic?
 Yeah, right?
 So the sarcastic nature is something that I've been repeating.
 So, um, So when you are testing, you can't test on exact output, like exact prompt coming back or exact text coming back.


Microphone

 You have to grade, um, that that output based on certain properties that you're looking for, right?
 So you're looking for things like expected behavior.
 Uh, such as did the task complete, uh, did you call the right tools?
 No hallucination or facts, right?
 Those kinds of things, right?
 We're not testing for in the exact expected string.
 And here's the new thing.
 You can actually use large language model to do this to the testing.


Microphone

 So it's called, like, LLM, as judge, for fuzzy correctness, right?
 Um, So if you have some hard constraints, uh, like schemas, the safety, the cost, then you could use deterministic assertion.
 But if not, then, you know, because the answer is not going to look exactly the same.
 So use these properties, as I just mentioned them for you.


Microphone

 Question number three.
 How do you stop an agent from burning money in a runaway reasoning room?
 That's right, that do loop that I mentioned, right?
 So put hard with it.
 You know, not soft guidance, you know, put maximum iteration count, maximum token budget, per task, maximum tool calls, you know, clock the time outs, right?
 Um, and put a circuit breaker that kills the loop if Asian calls the same tool with the same argument twice or something, right?


Microphone

 Those hard requirements.
 And log and alert on cost procession too.
 So that's going to be a good, you know, key factor for you.
 so that the runaway is caught in minutes, not, you know, not at the end of the month.
 Okay?
 I hope that helps.
 Uh, question number four.
 How do you secure an agent that can take real actions?
 and guard against prompting injection?


Microphone

 Yeah, good question.
 Yeah.
 Like I said, I like security.
 So, you have to treat every tool call, right?
 Like an authorization decision.
 If that agent can be doing that, allowed to do that, should be doing that, all that stuff, right?
 Not a suggestion from the model.
 You know?
 Uh, it's a hard, uh, you know, authorization.
 Using least privilege, right?
 Using scoped credentials, per tool.
 And perhaps even for human in a loop, for some high value actions.


Microphone

 You know, like, you know, actually paying somebody.
 Okay?
 And never let the, you know, the retrieve content, like web pages, emails, documentation, be treated as a trusted instructions.
 Because those things can also be faked, right?
 Or, um, you know, um, modify.
 So, what we say in the application security world is that whatever the user inputs, right?
 Don't trust it, okay?


Microphone

 So I'll isolate these untrusted inputs from the instructions, right, from the users, or, you know, maybe other, even other tools, sending instructions to other tools.
 where the architecture allows for that kind of things to happen.
 And validate, uh, using, you know, the list of allowed tools output before they feed back into the next reasoning stuff.
 So, yeah, you have to, it's called 0 trust in a very broad sense, that is, you don't trust anybody, not even other tools that, you know, your system has, right?


Microphone

 Every input can be an attack, right?
 There you go.
 And okay, so we have 5th question.
 Should we build it ourselves with AWS services, or use a managed option like bedrock agents or Amazon Quick Suite?
 Yeah, I actually recently tried the Amazon QuickSweet.
 Really, really nice, very easy to create these agentic systems.
 So, yeah, so you've managed when your workflow maps cleanly to, you know, their orchestration model and you want you want the speed.


Microphone

 And the 8 of us native security integration, right?
 Out of the box.
 That's basically what managed the solution world help you do that.
 So, but building custom, when you need separate, separate, unique orchestration logic, um, maybe using multiple models, multimodel flexibility.
 or control over the reasoning rules that the managed service doesn't, you know, expose or give it to you.


Microphone

 Right?
 Because, you see, when you use managed stuff, it abstracts away certain details, and you can't change those, right?
 Not to say that they're very limiting, but it's limiting compared to customized solutions, for sure.
 So, you know, when you create these things, most teams should prototype, uh, you know, managed first and see if that fits.
 Uh, then, uh, graduate to, you know, maybe custom only, where the manage abstraction actually gets in the way of you're doing these custom actions.


Microphone

 Okay, so, hey, thank you very much for those questions.
 Uh, and.
 Thank you very much overall for attending today's all pictures series



```
