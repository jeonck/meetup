<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

 So, we're gonna be talking about an evolution from platform engineering and a report that Pankaj and I published just a few weeks ago talking about some of the changes we're seeing in the platform engineering world.
 And some of the things that we think, apart from engineering community, all of you, really need to be aware of if you're not aware of.
 There are probably things you're feeling yourself already, but maybe haven't been able to articulate into words, and I hope this is super helpful for you.
 First of all, who are we?


Microphone

 Well, me, maybe you recognize from these webinars already.
 I run a lot of the content and community stuff here.
 You probably see me on my face on webinars all the time, but we have a very special guest.
 I'm super excited to welcome here. We've had him before on another bang of webinar, but that is punk age.
 So, Punkash, maybe say a few words about who you are for our old son.
 Oh, no.
 Hello, Sam.
 Thank you for having me here.
 I am senior director of Private Club Solutions, and very passionate about modern applications, whether they are Cubernet is based or AI, or the new stakeholders portrayed from agents, looking forward to exchange two thoughts today with Sam.


Microphone

 Nice.
 My pleasure.
 Took.
 First of all, what's the agenda?
 Well, we're gonna talk about the state of platform engineering today.
 What's going on, basically?
 Why this evolution is necessary?
 The five pillars of what we're gonna be talking about, and then, of course, some strategic recommendations.
 You know, I always like to give you what can you actually do.
 Maybe not tomorrow.
 Maybe you can have tomorrow and the weekend to perfectly, but on Monday, you can start kicking things off immediately.
 So, the state of platform engineering.


Microphone

 What is the data tell us?
 Well, as you probably have experienced or seen, platform engineering is not really optional.
 Okay.
 You know, adoption is basically universal infrastructure, you know, this new substrate we're all very familiar with.
 We're not really in the territory these days, of saying, What is platform engineering, or why platform engineering is just a fact of life.
 You know, 90% of organizations have already adopted from engineering.
 Many of these organizations are building pretty high quality internal platforms.


Microphone

 They also recognize that these platforms are essential for AI success.
 You know, 76% of organizations have a dedicated platform team, 80% see AI integration critical for the success of their IVPs.
 So, you know, we're not in a territory now where we're thinking about, oh, what is this platform thing?
 You know, should we adopt it?
 That conversation is over.
 We're looking at almost universal adoption now.
 We're now in the territory, where most organizations have even built platforms, are building platforms, or who've had platforms for free years.


Microphone

 So it's a different kind of conversation that we need to be having.
 And part of that means we have a much better understanding.
 I think you can almost universally, as an industry, about what platform engineering is, how it's worked, and where it's going.
 Now, originally, if you, you probably are very aware, the goal of platform engineering, Index, bit.


Microphone

 You know, 76% of organizations have a dedicated platform team, 80% see AI integration critical for the success of their IDPs.
 So, you know, we're not in this territory now where we're thinking about, oh, what is this platform thing?
 you know, should we adopt it?
 That conversation is over.
 We're looking at almost universal adoption now.
 We're now in the territory where most organizations have need built platforms, are building platforms, or have had platforms for use.
 So it's a different kind of conversation that we need to be having.


Microphone

 And part of that means we have a much better understanding.
 I think you can almost universally as an industry about what platform engineering is, how it's worked, and where it's going.
 Now, originally, if you, you probably are very aware, the goal of pop engineering when it 1st emerged was around reducing cognitive load on application developers.
 This was a very, very, very fundamental idea.
 That's really where it all came from.
 If you remember Devops's dad develops burnout, these ideas really focused on cognitive load, productive, you know, application developers were the customer, almost universally, 99% of the time, and the objective was to reduce their cognitive load.


Microphone

 That'll probably just for driving productivity game, but the cognitive load was a key part of that.
 So what came with that?
 Well, golden path standardization, you know, we wanted to start creating these opinionated, more templates, more common workloads.
 We've really focused on, you know, how do we improve the developer experience and the productivity that comes with that?
 So what are the types of things you need to build into an internal developer platform for that?
 You know, what can we do to reduce time to deploy?
 You know, how can we reduce the kind of the ticket avalanche that most people are dealing with?


Microphone

 And then how can we fix some of the issues with security?
 You know, shifting left security has huge amounts of incredible benefits.
 We know that, but it also brings with it a huge amount of challenges, and platform engineering was really about kind of keeping the benefits of shifting left, while alleviating some of the challenges and the issues with that.
 Now, when we look at that world of Apple engineering, that platform engineering that we're used to, well, why does it need to evolve?
 All of those things sound fantastic, reducing common in a load for active.


Microphone

 Great.
 Fixing shift like, great.
 Opinionated golden paths, great.
 So, why is that not perfect?
 What more do we need to change?
 Well, there are a lot of ceilings when we talk about that model.
 Because if you notice all the things that I talked about just there, they don't mention AI had nothing to do with AI.
 They also index entirely on the application developer, and I would be surprised if there's even a single application developer in this weaponar.


Microphone

 Three years ago, there was many application developers.
 They're a huge part, not to say application developers have disappeared.
 That is not what I'm saying.
 What I'm saying is platform engineering index, very heavily on how do we resolve issues for application developers?
 And they're not the only persona that is important, especially in an AI 1st world.
 We need to be thinking about, you know, how do you support, first of all, everything related to AI?
 How do you support the data scientist?
 How do you support the AI engineer, the MLAI engineer?


Microphone

 How do you support the AI agent?
 You know, what kind of workload support do we have?
 Do we have GPU TPU workloads?
 Are we serving models?
 we have MPC service?
 You know, are you providing the foundation that AI and the kind of AI teams and the AI personas that come with that need to effectively use the platform?
 More than that, what about other types of personas in the organization?
 Security teams, observability teams, SREs.
 Why would your platform not serve those people?


Microphone

 Why would your platform and all benefit to come with it? Index only on the application developer, where there's so many other roles that I think could be served super well as well.
 We also run into an issue when we talk about many of you having platforms already.
 Well, many of these platforms were built based on a model responding to those things we talked about just before.
 How do we reduce cognitive load and improved FX platforms?
 Well, many of those things end up being very reactive.
 These are not kind of proactive growing things that we talk about platforms of product and the idea of a platform needing to evolve.


Microphone

 Often what that evolution entailed was, this is a new problem that's come up, let me solve that.
 Not a proactive way of thinking about that from engineering.
 And then, of course, many of those golden pads that we talked about often became golden cages.
 We are really racing ahead to think, this is the best way it should be done.
 So let me enforce that to the best way.
 And at the same time, the paradigm that we were operating with in 2022, 2023, many of these core platform engineering principles were spreading throughout the industry.


Microphone

 Well, it was a very different universe.
 We didn't have the same regulatory environment.
 We didn't have the same compliance and sovereignty question mark and environment, and really, we didn't even have the same technical environment.
 You know, we've got a great stat here, that there was 50 CNCF projects in 2018.
 I mean, there's like 200 plus now.
 So the open source environment is completely changed, not to mention everything related to AI.
 And so many platforms that are built on those models from a few years ago, they don't really respond effective super effectively to all of this stuff.


Microphone

 coming against it.
 So what does that mean, then?
 What is the response to that?
 Well, the response is, we need to start thinking about some of the challenges that are pushing down on top of all of these things.
 Because if we think of those as ceilings, you can understand why platform engineering is needed to evolve.
 We're now dealing with an environment where AI has accelerated the amount of code as produced by 10, 20, 30, X, in many cases. Take 90% plus of developers are using AI tools, and they're producing an insane amount of code.


Microphone

 I would be surprised if there's anybody here, even a single person in the chat, who is not dealing with a delusion code. If there is, definitely say, I would love to hear what's going on with you, but it's a universal problem that we're all happening.
 At the same time, none of us really imagined that agents were going to be a persona that we really needed to be thinking about.
 We live in an agentic future.
 You know, open claw, with all its faults and flaws, it's one of the fastest growing open source projects of all time.
 You know, we're talking faster, then it has almost as many stars as a freaking, uh, cupertone, which is insane.


Microphone

 And, well, what does that mean?
 It means that agents are going to be a fundamental part of organizations, and if they are, then platform teams need to be thinking about this.
 They need to be thinking, well, how do we approach this from a security standpoint?
 But also how do we support it?
 You know, how do we make sure that those agents have everything they need?
 They have the guardrails, but they also have the, you know, the gas they need to really bring value.
 And then, at the same time, we are all dealing with a finot reckoning.
 Every single one of us.


Microphone

 I would be surprised if there's anyone here.
 I mean, my dad is a school teacher, and he messaged me about token concerns and tokenomics and token maxing.
 So if it's even reaching the schools, imagine what it's like in many of our big organizations.
 I know I'm struggling with token cost.
 I am sure everyone else here.
 And at the same time, tokens are not the only thing.
 35% of cloud spend is wasted.
 We still are dealing with significant issues related to cloud costs related to the infrastructure that holds up so much of this.
 So, if we're in a world where cloud is still so much of a challenge that we're placing, thrilling AI and token cost on top of this is just an absolute fin off reckoning.


Microphone

 And then like I highlighted before, we're in a new paradigm when it comes to sovereignty and compliance.
 The number of new regulations that are coming out, almost every country on the planet, the EU has huge runs to Cyber Resiliency Act, the EU AI Act.
 You know, these are things that organizations need to really be focusing on.
 And the platform team is powerless.
 I would say, in many of these things, I'm waiting for a sat for opportunity.
 We have some great webinars, and I written an article on exactly that.
 But there's still things that need to be figured out that need to be thought on that.


Microphone

 And at the same time, like I highlighted before, we don't live in a single persona world now.
 Platforms need to be ready for a multi persona experience.
 They need to be thinking about the application developer, of course, but also the ML engineer, the data scientist, Adops.
 They need to be thinking about security teams, infrastructure teams, observability, SRI, maybe.
 I also need to be thinking about well beyond the IT organization.
 What about how many people here have non IT, non software teams, non-developers, spitting up micro apps?


Microphone

 I know I am, I know many of my organization are, oh, those are things that the platform needs to be thinking about.
 needs to be taken care of.
 And then, of course, like I said before, the AI agent.
 Well, your platform needs to be thinking about how does it serve AI agents?
 You need to be able to bring BMs, you need to be able to provide everything that's needed to support all of these things.
 There is a huge convergence, all forces, that are demanding, demanding, demanding, attention, effort, and growth, from platform teams, and talk from engineering organizations.


Microphone

 And there's a big reason why things have needed to evolve in the past.
 If we think about all that amazing stuff that I highlighted before, well, it's not really enough to meet where we're here.
 Now, does that mean the fundamentals change?
 Just platform is a product change.
 Absolutely not.
 That fundamental principle of building an internal platform, treating it like product, treating users of it like it's your customers, with all the trappings of that, user research, cool name, thinking about how it operates at long term lifecycle product managers.


Microphone

 That is the same.
 The fundamentals of platform engineering is exactly the same.
 All the stuff around it, the personas that we think about, the way that we operate, the goals that we have, all of that is changing, and all of that is really being demanded by a lot of these branches, honest.
 So what is really the path that we got here?
 I think that helps to understand kind of the situation that we're in.
 when you think about where we might be going.
 So there was, of course, the Devobs era.
 We will remember that.
 You know, this original sense of what the platform is, Golden Pass, in terms of the dolphin platforms.


Microphone

 Well, where did inflection point?
 And we have been for about a year.
 AI, sovereignty, the threats that come from that.
 That is really requiring us to thinking about what comes next, the way that we build platforms need to change, the way that we think about our platforms need to change, and the people that our platforms serve, and the non-people, the non-human identities that our platforms serve, needs to change as well.
 So, my dear friend, Pankaj, is going to go through some of the core pillars that we think of the things you are thinking about, that we put in our own food report.


Microphone

 Pankaj, over to you.
 Thank you so much for a detailed insight about, uh, Origin of play from injuring, where the platform injuring, as a, at an inflection point, and where it has to go next, and why.
 So very deep inside.
 Thank you.
 An audience, if you have any questions or commands, feel free to put it in chat or in Q and A, Sam and myself will be answering that.


Microphone

 So we heard that we are the platform engineering has to go.
 Let's look at what played from engineering 2.0 looks like for that.
 I'm going to share from my screen, so I need not to ask Mr. Sam every time that next light, please, so...
 Can you see the slides, Sam?
 Yep, I can see them.
 Everybody in the chat, let us know.
 So before we go to the platform engineering, 2 dot, you know.


Microphone

 One thing I'd like to reinforce over here is that platform, Indian, include.0, is not a reset.
 It is the evolution of platform engineering one dot giro.
 The infrastructure which you built, the principles which you have and played from, injuring one, like managing platform is a product, increasing the developer productivity.
 Putting or getting more efficiency into the infrastructure, getting more efficient IT organization.


Microphone

 All those principles and pillars still remain the same for platform, injuring to our chila.
 So it is the evolution, not a revolution for that.
 However, the factors which are driving the evolutions could be revolutionary.
 The five pillars of play from injuring.0 are very, very simple and very, very deep into that.
 First and foremost is the AI native platform.
 AI workloads and agents supported natively on the platform itself for that.


Microphone

 And many platforms are already doing that today in the industry.
 including the VMVCF platform.
 Second one is the expansion of the persona, so we use and benefit from the platform.
 So, evolution from just primary build for developers, to the new personas, and these personas will be human and non human personas will use and benefit from the platform.


Microphone

 Third is the evolution from a bolt on pin of two embedded spin ups into the play form.
 The fourth one is complementing the security left or shift left, the security, with security shift down, into the platform for that.
 And that is not a replacement of ship lab.
 It's a compliment of the shift lab security line.


Microphone

 And last one is composable by design.
 You should be able to mix and match best of the breed platform, uh, component, and you should be able to repave your platform with confidence, but quickly, and also, do that smooth transition when you move to the new building block of the platform injuring for them.
 So, these are the five pillars of platform injuring 2.0.
 We are going to throw deep into each one of them.


Microphone

 But make no mistakes.
 Infrastructure is still remain the underlying substrate behind all the pillars for that.
 Let's start with the first AI native platform, supporting AI workloads natively onto the platform.
 Whether you are building or governing and protecting AI workload, they should be natively supported in the platform.
 There is a lot of distribution of focus right now on building the AI workload, but equally important is the governance and protection for that.


Microphone

 And supporting AI workloads on the platform.
 has a very unique requirement, like the GPU policemen, in near future, TPU policemen, the model survey, the model registry, for security and compliance, or for the guard race, AI gateways, for agents who will require MCP servers and the gateways, the pipelines with the data scientist will require the guardrails, which everybody needs today for the AI for that.


Microphone

 Not just the AI native on the platform, the platform should also be very agile.
 As you have seen in last 12 months alone, that MCP servers and gateways have grown so significantly in the requirement for the agent, pick one.
 So that's what we mean by the AI workload supported natively.
 Second one is the AI agents as platform citizens.


Microphone

 It is... pretty obvious that number of agents who are going to use the platform will outnumber the number of developers who use the test.
 Today in the world, they are somewhere from 30 to 33 million developers.
 Agents will be in hundreds of millions who will be using this platform.
 Agents are basically LLM power agents who are able to reason, plan, use tools, execute trusts in a boundary scope.


Microphone

 And bounded scope is a very heavily loaded word.
 We will talk about a little bit more into that.
 And agents also use the APIs for that. So your platform has to support the agents of the platform citizen.
 We see two kinds of agents evolving or benefiting from the flight.
 First, is the agents with customers or your IT organizations is writing, will write.
 To help, to streamline your process, giving a better experience to your customer, giving a better experience to your employees, giving a better experience to your partners for that.


Microphone

 Second area for the agents, which is the agents which optimize the platform itself for that.
 Ability to do the incidence triage, or maybe develop a ask certain environment just in natural language, and that's the next phase of evolution from the ticket from click off to just asking the environment in the natural language.
 But this also comes with a huge responsibility on the platform for putting the right guard rails for that.


Microphone

 which we will talk about in upcoming philosophy.
 And that's has to happen now, but this also has to happen with life, God, right, into that.
 Recently, you might have heard that the hugging phase agent, uh, hugging phase, uh, had a security incidence because one of the agents crossed the boundaries of, uh... of the sandboxing with open AI helped put together.


Microphone

 The last one over here is the distant future is the autonomous pledge, where all the agents, control loops, policy engine, telemetry, all working together, and multiple agents working together to play from to become an autonomous platform.
 Self feeling, self optimizing, self is telling, just like what Tesla does for the autonomous driving for that.
 But along with, for the AI native platform, is that the platform will evolve to be a single platform for all applications for that.


Microphone

 Current platforms are very much focused on containers.
 Now they are expanding to the AI workloads.
 When you require the AI workloads, stronger security, you have to put the VMs also for the stronger security.
 So a single platform supporting all three kinds of the workloads, the containers, the VMs, and AI workloads.
 And they have very strong benefits of running multiple types of application on the same platform.
 One is just plain economics.


Microphone

 The higher resource utilization.
 You've seen the hardware prices have increased significantly last two years.
 There is a memory shortage, but the utilization of resources is still remain pretty low for that.
 So when you run multiple applications on the same platform, there is source civilization goes up significantly. Along with that, you also get a benefit of consistent operations policy, security, compliance, list goes on to invest.
 There also will be instances where the customers, or IT organization, will spin up a dedicated platform just for the agentic workload. So, yeah, that's absolutely fine.


Microphone

 But the goal here is a single platform for all the applications.
 If you want to learn more about what we mean by AI native platform, suddenly there is a white paper in the end. We are going to give the link.
 You can find more details for that.
 Second is the most favorite slide or most favorite pillar for that, because it binds the whole play from India to part two.
 It is the expansion of the platform injuring to multiple sonite speeds.


Microphone

 Original platform, injuring 1.0, had a single persona in the forecast.
 Give them the efficiency, reduce the cognitive load for that.
 And the second persona will benefit from the platform injuring was the platform engineering itself, because they build the platform.
 They maintain the platform, major the ROI for, build the KPI for that, too, for measuring the productivity.


Microphone

 Which play from engineering?
 Multiple new personas will use and benefit from this platform.
 Each persona will have a unique requirement for that.
 They will also require their unique abstraction, right tools, right dashboards for that.
 Let's look at their unique requirements.
 Let's just start with the first one, which is the most pressing one right now, is the data scientist and the engineers who will need the self beauty of the reasoning, modern registry, experiment, striking for them.


Microphone

 All to further address the need of AI applications and their security. Security in the compliance team will require a stronger security.
 They will require implementation of security in a much more efficient way with the policy as a court for that.
 Compliance will evolve from a static, time bound compliance check with continuous supply for that.
 AI will also help for auto remediation to the security and compliance teams for that.


Microphone

 And engineering, business leaders, are going to look at for more pot pinox transparency, more pinox predictability, more Dora matches is to measure the performance of it.
 We're going to talk more about, you know, as an independent killer in the next world.
 So you see three new personas have a unique requirement for that unique experience player.
 What it means for play from engineers, they have to build a roadmap, to address the unique needs of free, new human persona.


Microphone

 Along with that, just the human persona, there is a new non human persona when, of course, it's not an alien, but it's an AI agent.
 AI agents will require API.
 They will require a full permission.
 They will require new building blocks, like MPP server and the gateway. They will require a lot of governance and audit logs for that.
 But more importantly, they will also require very strong guard rail product. You'll see that how the platform engine is exponding from just 2 personas to 6 additional persons.


Microphone

 This is the first time where the non human persona will also be benefit.
 And these agents, this persona, is going to outnumber of rest of the personas which you see in this life.
 for that.
 And if you look at the five pillars of the platform engineering 2.0, this binds because each of these pillars addresses the unique needs of each persona over here.
 So that's the reason this is my most favorite life, but it's also the most simplest life.


Microphone

 We reviewed with multiple analyst forms, and consistently, which we heard, that just is the crux of the plates are injuring, serving multiple personas, human and non human personas.
 Move to the third pin, embedded pin. As you have been a practitioner, I played from injuring forces, almost decades. Developer productivity has been the first class signal.


Microphone

 In platform injury, developer product is still remains the first class signal, but the cost also becomes the first class signal.
 And there is a very, very strong reason for that. If you look at the today's finale, it's a bolt. It's react. It's very silent. And that is translating into a very significant cloud wave program. Whether you look at the broad cons of our own private cloud is steady, or whether you look at the finops, harness, finops, report in focus from 2025.


Microphone

 All I'm suggesting are telling that there is a significant cloud waste in the infrastructure is happening.
 And infrastructure is becoming more and more expensive for that.
 My favorite one is the cast AI's report from 2026 state of Cubernet's optimization report.
 That suggests every utilization in public cloud today is 8% CPU, 20% memory, 5% cheaper, your most expensive resources.


Microphone

 Even if these numbers are double and triple, there is a lot of room to reduce the spending, the waste.
 And if you speak to any cloud architect, they will say that I can't predict my cloud bills at this moment.
 Are there reasons for? The reason is that developers led that cost context, at least 50% of them.
 But the good news is that more than 60% wants to take a control on managing the cloud course.


Microphone

 But the reality is that cost management is very hard to life.
 It takes weeks, even months, to identify simple things, like the ideal or for unused cloud resources, whether it's containers, or whether it's a VM, and it takes much longer to even fix it for that.
 And there is a very... lake of focus on smart repetreation of the world.


Microphone

 So that's the reason that today's spin offs has very significant challenges for being a voton and very reactive.
 And platform, injuring 2.0, addresses that by embedding the spin ups deeply into the platform, and infrastructure is the right place where you embed the phenops into it.
 Things like self service, we know, embedded into the platform by deform.
 Real time cost attribution, predeployment cost gates for that.


Microphone

 Let me give you a few examples.
 When you spend up in a new environment, it should be able to tell you that if you run in a public club, this is the cost is going to be.
 If you want to run into a private club, the fox is going to be 30% less for that.
 Or, when you spin up an environment, you should be able to tell you that the current guideline is that much cost for that.
 But your projected cost is more than what the companies spend their policy is that, just like when I want to book a travel from San Francisco to Boston, companies suggest the cheapest price, let's say, $500, but they want to give me a flexibility to choose the right flight, so I reach a reasonable time.


Microphone

 So they give me $200 more to pick up, select the right flight.
 But if I go about 700, quote 500 +200, it says you need an exception from your management.
 Why not these similar things are available in the platform?
 That's what we mean by the embedded thing.
 Toponomics is the whole new district.
 I'm sure you must have heard the bragging rights about the Copenmax thing that you spend all the tokens.
 We have seen that companies that are spending a year one of tokens within the few months there.


Microphone

 It feels like it hit again that you went to a video arcade, and you had a $10 to play for a whole day, and you spend all your tokens to play the games within two hours, you need more money.
 That's the reality of that today for toponomics for that.
 And, of course, a very stronger need for it, autonomous janitors and resizing agents for that.
 So when you embed the finops into the platform itself or the infrastructure, The platform moves from visibility to influencing the decisions that the provision.


Microphone

 And the nirvana is achieved when every developer, every operator, becomes a fin offs practitioner for that.
 And that is the need of the time now for embedding a finoffs for that.
 Moving to the third pillar, security shifts down for them.
 This section is a little bit longer because we covered two very important topics.
 One is the how shift labs is complemented by shifting down the security into the platform itself.


Microphone

 And the second one is how AI is widening the security gap and how it has to be mitigated for that.
 Let's just start a quick recap what shift left was.
 The whole promise of ship left was that developer was the security.
 You automate SASD, DSG, SCA, Tools, into the five lines, and you guess the issues before they reach the production.
 The reality is that it increase the cognitive load on the towel.


Microphone

 That's not it.
 But bigger deal over here is that most of the vulnerability is that is to found in production or post production.
 Because pipeline scans miss the right time. The production environment constantly evolves with the configuration changes, the environment changes, but... It's not just the world. Wonder if you found both production.
 It takes much longer, it still, to re mediate those wonders into the applications. And the... involvement, they might.


Microphone

 That's the reason why you need both of them. Shift lab, catches the security issues.
 And shift down, catches everything else which shift lap would catch sharply.
 By doing two very simple but more immediate needs for that.
 One is embedding security deep into the platform.
 And the second one is policy enforcement at one time.


Microphone

 What do we mean by security embedded deep into the platform?
 By making the infrastructure, making the platform secure by design, enforcing these privileges, enabling mutual TLS like the closing, doing a stronger segmentation between workloads and agents and infrastructure for that.
 Simple things like the secrets management, achieving the efficiency of security deployment through policy as a quote for that.


Microphone

 And also, compliance, become a continuous compliance instead of a snapshot in a time frame.
 Equally important is that security has to become invisible.
 And also immutables, which you should not be able to bypass for them.
 Invisible and immutable is a huge task and need with urgency today.
 Let's move to the next part of the, this pillar.


Microphone

 Our AI date, AI is widening the security gap.
 Everything which you see on this slide is a new attack surface, new vulnerability surface.
 Which current platforms are really not really built to address that.
 Shadow AI is prompt injection, modern poisoning, inference data leaks. And each of these components of security gap brought by AI is very, very vast for that.


Microphone

 So split from injuring has to address that.
 And many of you already, seeing in your organization, shadow AI as well.
 I'm sure you're saying not govern models being used inside the organization. Your setups, team or security teams are very much concerned on the inference data leaks for that.
 We are also worried about the data injection because new no SAST and DST tools can detect that injection in the live inferences stream for that.


Microphone

 So platform has to address that and sometimes these security vulnerabilities are moving faster than we can fix it in the platform itself.
 The good news is that 1st 2 things, you can do it pretty immediately.
 When is the very quick and strong modern registry governance?
 And enforcing the data isolation, which platforms have technology, and that can be implemented quickly.


Microphone

 And near future, you will see more prompt security, more audit, inference, and as more and more AI gateways, more MCP gateways are implemented, the AI will become more and more secure for that.
 So if you implement these things in the platform engine into dot zero, platform will become that dress boundary.
 You're not just securing the applications.
 Now you are securing the data.


Microphone

 You are securing models.
 You are securing inference for that.
 And especially in the case of agent AI, which is the topic, a huge topic by itself, it has to be audited ready by default for that.
 I think security session is one of the most urgent sections which has to be implemented in the platform as soon as you start doing the AI applications or agent to AI inside your organization.


Microphone

 The fifth pillar is the simplest pillar, which has been discussed for a very long time in the industry and very established practice.
 composable by design.
 But what is different this time is the faster repavability, which will be talked about.
 So, So, quick recap, what is the composable architecture?
 It's very simple.
 Mix and match, best of the breed Lego rocks of the infrastructure.


Microphone

 These playform captivities are delivered as a very modular, independently deployable, and interchangeable building blocks.
 That's the very key word you will see in the next line for that.
 And all these building blocks are connected through a very well defined contract, through policies and SLAs.
 And one of the critical component of composable architecture is a lot of CNCF confirmant and certified options for that.


Microphone

 For which, actually, the VMware is one of the top 2 contributors for CNCF for last decade.
 That's what that little bit more detail into what we mean by composer, per flight formula.
 Five layers, infrastructure layer, integration layer, the capivities layer, orchestration layer, the experience layer.
 What complexibility means is that you should be able to evolve each layer independently without cascading those changes.


Microphone

 The last 12 months, you have seen an integration layer.
 There is a new building block, MCP service.
 There is a new building block, MCP Gateway.
 There is new building block, which is the AI gateway for that.
 And what? We pay property and composibility means that you should be able to swap one component with another.
 Like, one of the CICD tools, like Jenkins with harness.


Microphone

 One CNI, another CI, if you are more on the infrastructure layer for the networking, replacing one GPU with another GPU series over here or maybe using both of them simultaneously.
 But platform should be able to repay pretty quickly for that.
 It builds on the same foundation of the composable architecture you have learned over years.
 Modeler by design, API, first contracts, plug and play.


Microphone

 But some of the concepts which we have in CICT before that progressive rollout, we have to bring into the play from engineering with progressive migration.
 Moving from one component to another component in the various both way, and also measuring the performance of it.
 That's a progressive migration from one building block to another building.
 We believe that future of the platform is not going to build and buy.
 It's going to become composed.


Microphone

 However, there will be IT organization, who will is professional built, there will be still, who will just buy off the shelf for buy.
 But majority of customers will start building evolving their platform to compose so they can pick and choose.
 I remember one of the very famous sports, Google CTO said a few weeks before that.
 The developers has the least loyalty to their tools for that, because they are continuously looking to evolve their tool chain to achieve better efficiency.


Microphone

 And that's where this composibility becomes more important for any involved.
 So when you look at these 5 pillars today, they are not independent.
 They are together, and that's what makes the plate from engineering to God Sheila.
 And the binding force between these five pillars is the infrastructure, which is the substrate beneath all the pillars for that.
 Sam, pros is used for next.


Microphone

 And I can forward the slides for you.
 Thank you very much.
 So let's talk about what is next after that.
 Marvelous, Marvelous, Marvelous, breakdown.
 And if you want to go into some more detail in what we talked about there, Pankaj is actually putting together a blog that I think will be published pretty soon, either early next week or maybe even tomorrow.
 Which goes into some of the stuff that we talked about at, and also, of course, the report, associated the end.
 So, jumping over into strategic recognition, things you can really take off with on Monday. Well, for any of the executives here, the more senior folks, or people who have a line of comms onto senior folks, you need to think about how you mandate this evolution as a business case.


Microphone

 You know, you can't be thinking about, oh, you know, we need to improve our platform, so let me just tell this to people.
 No.
 This needs to be something that really, really drive.
 You need to start tying your platform investment to these exact points.
 You need to be thinking about the velocity changes here, how you reduce power costs, and you need to be thinking about AI readiness metrics.
 If you're not, you're gonna have a big problem, and you can't just be using it kind of lukewarm.
 I think you need to go all toes down and think about how you mandate that.
 You also need to be thinking about PNL.


Microphone

 So actually think about establishing your platform PNL.
 So if you're thinking about your internal developer platform of the product, well, what do products have? I always have, you know.
 So you need to be really committing to it.
 And then, of course, you have to set a 12 month AI native platformizer.
 Like 12 months, feels like a long time.
 It is incredibly short in this, and if you aren't really thinking about where you're going to be 12 months from now, in terms of AI natives, you're in, I'm just gonna come right and say it, you're in trouble.


Microphone

 Really?
 You need to be thinking about this.
 That doesn't mean full agentic development platform completely done, the entire organization fully adopted onto it, you know, 1000000s of A averages.
 But we need to be making full progressions, you know, and those stuff.
 Now, for you, is the button out here?
 What? Well, you should already have the fining, if you don't have them.
 The distinct experience layer for each persona.
 You know, what does the experience of the app to have to perform engineer, the security team, the being assignedest or the AI agent?


Microphone

 What does that look like in relation to your platform?
 You need to be thinking about some of this API person compatible architecture.
 So, start adulting.
 If you're not yet, if you haven't yet, you need to start doing that.
 And then, of course, where can you be abetting security themselves directly into the platform there?
 So go take a look at your all the security processes, all the fit offs processes that are connected to people, and then think about, okay, what can we embed in the platform immediately?
 Is it container scanning? Because it's at these things that you can build into the platform immediately on a fin-off side.


Microphone

 Can you do automatic recording?
 Can you build automatic dashboard that are populated automatically by action via the platform?
 You know, if you can start to think about where you can get these things directly, it will make a big distance.
 We also need to immediately, from Monday, you know, maybe if you're a fast ruler, you can go tomorrow, but take Friday and the weekend to think about it. On Monday, start thinking,
 Are you prepared for agentic instruction?
 You probably aren't.
 So you start thinking about, what are the things that you need to do to get yourself ready for?


Microphone

 I'm telling you, this is going to come faster than you expect.
 Obviously, there's many different types of organizations.
 We have many different stages, we have different levels of maturity.
 Many of us have more mature platforms, less mature platforms.
 But a fundamental true for all of us.
 You know, your, your executives, your business people, your salespeople, your marketing people, you know, your developers are going to be spinning out their own agents and they're going to be doing things with those Asians.
 And whether you like it or not, whether you control it or not, whether you keep them safe and secure or not, that is going to happen.


Microphone

 So, really something you need to be thinking about immediately from a guardrail perspective.
 How do you do it safely securely? But also, how do you enable it? So you can get the value from it.
 So if we move over to the next slide, Pankaj? Before we do that, Sam, we have a few questions on the audience.
 Sure, but I'm wondering, maybe we can show you the QR code while we do the questions, if people can scan.
 Um, so this is a report that Punk Hajj and I put together that goes into much more detail.


Microphone

 I tried to pull up super fast and get many words out as possible, and Pankaj is probably the most methodical person.
 Really, we cover as much as we can, but there's, like, a 45 page report.
 There's way more in there, so scan the QR code and download that and get reading.
 And while you have this on your screen, we'll start taking some of the questions.
 So, I see a nice little back and forth here between Satish and Shapur.
 So, from Satish.
 Let me tell you the truth.
 There are many traditional orbs struggling to build a possum engineer at one point 0, and ending up resetting the platform every time when technology changes or business priorities change.


Microphone

 And from Shapur, I agree with Satish.
 Many traditional organizations are still struggling to establish platform engineering 1.0.
 What will be the role of Tebop's engineers in platform engineering 2.0?
 How will their skills and responsibilities evolve as AI and autonomous agents take over more operational work?
 And is there a genuine risk that some traditional dev ops rolls will be replaced?
 I will speak very directly and friendly.
 I think if your role is primarily devops and doesn't incorporate platform engineering, think about things for platforming head blends, you are at risk.


Microphone

 There is a very genuine risk that you will be replaced.
 That does not mean that the work of DevOps, you know, the philosophy of DevOps goes away.
 Of course not.
 You know, platform engineers use the devil's philosophy all the time.
 Absolutely we do.
 But when you are thinking about the things that devops lacks and that is this concept of shipping down, that is treating things like a product, if you are not doing those things, then, you know, I think there is a genuine risk there that you need to be thinking about.
 And it is a valid point that many, many, many platforms, Satish like you raised, they end up kind of resetting their prioritization.


Microphone

 Oh, we should focus on this, we should focus on this, focus on this.
 That's why what we talk about is the foundations are super important.
 What is the fundamental element of the platform?
 You need to be treating it like a poet.
 You need to be thinking, okay, this is a product, and the users are customers.
 Keep that secure. As long as that is never changing, then it's okay, the types of road mapping points you're adding, as long as you're thinking foundationally, and you're thinking about how do these, all of these things get supported together.


Microphone

 And obviously, there's way more detail than we could go into that.
 I think the report does a good job covering some of that stuff.
 And then I think a question for you, Prakash, from Stephen, how much agentic AI is in use at the Mware today?
 We have a very dedicated project for agentic AI or the AI use across all the divisions for that, and we are using and engineering, we are using in marketing, we are using in sales.
 So we are embracing AI tools very heavily.


Microphone

 So I have a question in the Q and A from Wolfgang.
 Why do you name agents as an additional persona?
 The agents will act as different persons, for example, developer, platform engineer, test engineer, and so on.
 Others will act as persons in the business apps.
 They will not be there without having a dedicated role.
 I think that is a fantastic, a fantastic and a really interesting point around how we think about agentic identities.
 And it's also when you think about what type of commissions, what type of controls.
 I guess the question mark to you, Wolfgang, is, would you give the exact same type of controls, freedom, and resources who develop her agent versus a developer themselves?


Microphone

 And I think there's a, as soon as you start to think about that layer of things, you know, a developer, a human being, maybe they, you know, they're not the super superstar developer in the same way an agent might be, but they often have the wherewithal to know, ah, I probably shouldn't delete this.
 So, you often need to think about the agent, not the exact same way as a human.
 So there are these lines where an agent identity, maybe it should have 95%, the control as a human identity.
 But there's that 5% that you need to be thinking about.


Microphone

 And if you're not thinking about it, those are the question marks.
 So, your platform team does need to have those questions, and maybe it will be different organization, organization, but it's not so easy as just to say, oh, well, this is a developer agent, and this is a test agent, and sologist, give it all the same controls and permissions as my test engineer does.
 I'm curious, Pankaj, you're...
 I think that's a great, great idea, and thank you for asking that maybe salmon, myself, or will write an article that how the, uh, are different from the ages.


Microphone

 But there are few perspectives I bring into that.
 One is the how the identity is managed versus human versus agents.
 It a little bit different.
 That's one.
 Second one is that naturally humans have the guardrails around it, agents don't.
 So that's the 2nd big one.
 The third one is the scale of humans versus ages.
 It's pretty likely that any organization may have hundreds of agents pretty quickly built.


Microphone

 If I remember, something Nadella said a few weeks before that Microsoft itself will have 20 million agents inside their organization for that.
 So that's a scale which we're talking.
 So if you have to build the governance, identity, research allocation, the observability.
 We are talking about the scale which we have never even thought about.
 And once the agents become autonomous, that's a very, very different approach, which we have to look.


Microphone

 So, it is a very evolving field.
 We are still lot has to be done, and that's the reason for flight from engineering for 2.0, what Sam and myself agreed that we will evolve this white paper every six months or so when we see the things evolving.
 So this is the very fascinating, fast evolving field, and that's the reason when we talked about the AI native to the platform, we said, agility of the platform is going to be most critical, because my finest example, I will repeat, look at the MCP servers, and if I talked to you last year, it was experimental.


Microphone

 Now every organization is looking, how do I deploy MCP for agent AI workload? MCP is a fundamental building block, whether you're looking server or whether you are looking... gateways.
 Yeah, absolutely.
 And I think I will also supplement the previous question there.
 Some of the organizations are even struggling for platform engineering one, you know.
 Absolutely, absolutely right.
 The maturity varies significantly across multiple organizations, for current application, engineering.


Microphone

 And if you don't achieve the maturity, or you don't focus and put the right ROI and write the strategy behind AI and these new drivers for platform engineering to walls, put organizations far behind and create much more chaos for that.
 It's kind of a week of call for platform, injuring.
 You may be surprised today that today Cubernetis have no awareness of GPUs at all.


Microphone

 They give you blood.
 Back to you, sir.
 Yeah, thank you very much.
 I think we have a time for just a couple more questions.
 We got a great one from Yusuf on FinOps.
 How are you thinking about implementing pin offs in the 2.0?
 Would it be applied across the test, non production and production environments, but primarily focused on production?
 I ask, because in my experience, some lower environments can consume significantly more resources than production, due to the volume of testing.
 At the same time, implementing enforcing phenops across every environment could require considerable effort, which might make a production first approach, more practical and practical.


Microphone

 I'm curious how you're thinking about the trade off.
 Great question.
 I think the most important part of this, as well.
 is the fact that most platform teams have not been thinking this way or thinking about this.
 I mean, most of the people I talk to have, like, a, was a biweekly finops meeting, basically.
 You know, they've got a few finop dashboards related to cloud spend, but there's kind of, you know, exhaustive way of thinking about films.
 And the reality is, it's gonna depend organization to organization.
 I think the very 1st steps is most would kind of agree.


Microphone

 You need to go and do a bit of an assess and understand where the son of cost is, where some of the areas you need to focus on.
 It's probably not realistic from day one to think about embedding kind of automated phenoms across every single environment that you've got.
 But in your organization, if you are seeing, ah, okay, look at our biweekly, this is where we're thinking about cost.
 then identify those paces, identify those elements, and then build that into the sense of it.
 Now, the ambition over time is automated reporting of all of it.


Microphone

 You know, we don't really live in an environment, especially as we go forward, where we should have, there's any reason why we need to have no visibility on all of this stuff, particularly in areas around, like, AI cost, related points, because those can absolutely spike.
 You know, the kind of clear, regular universe that we're aware of.
 But we're already getting kicked in the buff by that event.
 So a bit of a wider answer for you there.
 I'm curious, Pankaj, your view of this.


Microphone

 I think it's going to vary from organization to organization. And with your question, you've already answered your question because you said in your pre-production environment, in your organization looks like finops is a very critical need for that.
 So, if you see that a stronger finance requirement for that, that's very, very, very important.
 And I also believe that if you look at any organization, the pre production environment, they are the most often who remain orphan inside any organizers, you build it, you develop something, and then you do a trial environment, and you completely forget over the weekend to spin it off, and then end of the month, you see a big bill, which has been instanced, is running from that.


Microphone

 This is a very, very common practice for that, and that's the reason that finops is not the area which covers the just the post production or preproduction or the development or test environment into that.
 It covers everything from that.
 Some organizations do a very little development, but more deployment for that, each organization is different.
 Or if you are doing a model training, pinoffs plays a very significant role over there, because the costs are so high.


Microphone

 So... I think it covers every part of the development cycle, but where is the bigger challenge for you?
 These will depend organization too.
 And with that, I want to say a huge thank you, everybody, for joining.
 Thank you for your wonderful questions and your attention.
 Go download that report.
 I think you'll have a wonderful time reading it



```
