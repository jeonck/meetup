<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

one, what we would have once thought would have taken us in a green field manner, 12 weeks.
 Once the platform for agentic engineering has been running, we can do it in one week.
 And if it's non greenfield, that is... The pace and delivery of software is becoming exponentially faster.
 And the interesting thing is that we find that writing code is way under the bottleneck of engineering.


Microphone

 If you think about historically how we've done software development over time, you know, two week sprints, you go to your business, you pull a lot of information from them, and you come back, and you react to it, build software, you update your platform, you spend time enabling your developers through your IDP, for them to be self serviced, and then they have to go do the work, and that is taking now.
 would take two and a half weeks, three weeks to do, you're running it significantly faster.


Microphone

 And those agents are just gonna get a bit more, uh, better at what they do all the time.
 And you're moving away, too, from a copilot style of AI level of engineering.
 So, you know, within my IDE, you're moving away from, I'm just chatting with Claude, for example, or with Codex.
 I'm just chatting with it, and it's giving me what the coach should be or giving me suggestions.


Microphone

 Now I'm telling it to go run, and I'm running multiple agents at once, and they're pulling in stories and writing code and making it work.
 And so, the multi step work is gonna become the norm.
 And we see that moving further and further within the Enterprise Organization across the world.
 You know, you start off with large, gigantic, multibillion dollar organizations that have built this, and now smaller companies that would have never thought they had the opportunity to build software, and they primarily focused on buying.


Microphone

 Now they're thinking, How can I build exactly what I need and have it continue to be serviced and managed over time?
 So the platform becomes even more important in terms of agenic engineering, an organization that wouldn't have normally thought about it.
 So, um, you know, what we have historically built our platforms for people, and now we need to think about moving and adding scope of what our platforms can do with Asians, agents that are gonna act on our behalf, that we delegate work to, or agents that are gonna run on their own.


Microphone

 And so, uh, just some some thoughts around this here.
 You know, we have to, we, as the platform engineers, need to be thinking about things that are going to enable the agents to be more successful.
 One of the conversations that we were just having yesterday, Dan brought up a really good point, is our AI, ultimately, we are gonna be the engineering team members, were responsible for what it's going to do.
 No one else is gonna be viable, so if an AI agent goes and brings down a whole production environment, you know, we're not gonna go, uh, go yell at the agent, right?


Microphone

 We're gonna go do investigation, and we're gonna understand what happened, and ultimately, it's gonna bear some responsibility on us.
 Whether we're the ones managing the agent specifically, or we built a platform available for what the agents can do.
 So, as we are starting to think through where agents can work in the context of the platform, we think in terms of the three most important ways.
 Context, execution, and governance, right?
 Your agents need to know the context of what your platform is and what your platform enables.


Microphone

 What are the APIs available for them?
 What are the APIs that have been built?
 What is the overall architecture?
 What is service discovery capabilities, those types of things?
 How can we execute?
 How can we execute standardized paths that are automated, that are gonna be predictable?
 And while we know that AI itself is not necessarily deterministic, we want to drive it to a point of consistency.
 And finally, what can it do?
 Do we have governance and visibility and observability in what it's doing and moving forward?


Microphone

 So, let's dive a little bit deeper into these.
 We're gonna talk about these under the guise of building a task.
 So we ask an agent to create, test, and employ a new API.
 And so as we have asked this agent, it's gonna go out and build it, how are we gonna follow along with context, with execution, and with a governance?
 So, context, how does the agent know what exists and how does it know how it fits together with a new organization?


Microphone

 Historically, those things have just sort of happened in the head of all of your developers.
 I have been a team member at this organization forever, and I just kind of know, and I know where all the skeletons are, and I know, you know, hey, don't mess with that API.
 It's really brittle.
 It's really fragile, and, you know, maybe I have to sort of hit the machine every Friday, and remind it that it's supposed to be up and running.
 But those things can no longer be hidden.
 They need to be aware and discoverable.


Microphone

 They need to have interfaces, and the knowledge of what they do within your organization is gonna become even more important.
 So, good context looks like these four things, service discovery.
 You need to be able to, your agents need to be able to know what's out there, how can they access it?
 What are the dependencies? Who owns it?
 What environments it's gonna work under, and what's the infrastructure that it can run under?
 Those organizational, that organizational knowledge, becomes even more important, and it's sort of a blessing and a curse.


Microphone

 AI is really good at creating documented organizational knowledge for us, but they need a baseline to start with.
 So where, where, where do we, as an organization, want to, um, how do we want to build something?
 What are the patterns we want to be using?
 What do we think is good documentation?
 And how can we build run books so that when the next team member comes in, and maybe they don't have as much context, and they're building and deploying agents, that those things can pull in the right documentation, and build the right solutions.


Microphone

 For us, MCPs are a constant conversation.
 We're having across the board.
 Every SAS company is deploying an MCP, every tool within your organization is now starting to build one.
 And organizations themselves are deploying MCPs, uh, that agents, whether they're primarily copilot style agents, or automated agents, are gonna be able to start accessing.
 And so we, as the platform team, we need to be thinking about what is the MCP capabilities that we need to be deploying so that there is an interface available for those agents to query, to understand, to interrogate, and to be able to work where.


Microphone

 And finally, we need to have the same guardrails, same level of permission, aware context, uh, that you would have, um, in any normal organization, at least permission, possible, even thinking about delegated permissions, those types of conversations.
 So context becomes the ability for your agents to want, run and execute, and deploy their solution.
 Context comes before we write code, right?


Microphone

 So we deploy a story, we deploy a unit of work, and our agents go out and start picking it up.
 Context is going to allow those agents to build a good engineered solution.
 They will build something, whether it meets your requirements is one thing.
 The next thing is execution, the standard way of how to act.
 Once an agent knows what to do, how is it going to do it safely and consistently and securely?


Microphone

 Um, paths an agent can actually follow.
 This is where we, as the platform team, we can take our built in expertise and build it beyond where humans normally sat, right?
 So a lot of these things become, we already do this as an organization,
 How do we make it agentically aware, right?
 The golden past, the repeatable ways of doing things, self service workflows.
 Agents need to be able to deploy solutions in a way that are managed by the platform team, so that they aren't going and building it out themselves.


Microphone

 We want to have tooling that is available for our agents that can be executed automatically.
 You know, just like we don't want a click op solution from a human perspective, we wouldn't want agents to be deploying tickets for us to work in as well.
 And so, we can spend the time building execution paths that are right for your organization, right, for your security posture, right for your governance posture, that can be invoked and not just clicked.


Microphone

 So that's where the context becomes important, MCP's being available that can have the automate automation capabilities ready for your agents.
 And finally, isolated and ephemeral environments where agents can validate changes.
 The interesting thing about agentic engineering, this idea that code becomes a commodity.
 How often can I make changes?
 I can be deploying changes as many times as I want.
 Is code now the thing that we need to protect as we once did, or does context, and specifications, and business requirements, and engineering requirements?


Microphone

 Those things now become the most valuable thing within your organization because code can be written in minutes, in seconds, with agents.
 We can rewrite whole platforms and whole solutions in a fraction of a time that we once would have thought about doing.
 Execution often comes through an approved execution path.
 How do you want your agents to be acting?


Microphone

 They want to start from an approved spec, an approved templates.
 So not only do you need to have those specs defined from a business perspective, but we want them defined from a platform perspective.
 So we can meet business requirements, but we need to make sure that the agents are meeting all of the technical requirements, as well.
 We need to have testing environments, just like we would for human beings.
 And those things can be spun up and automated and spun down, just like we would, we would expect for a human being.


Microphone

 Every engineering task, if they have a manual process, agentic delivery isn't going to scale.
 Because they can build things at a faster rate than we can.
 And so, if you think about the nightmare scenarios of developers deploying out, um, random test projects across your cloud organization, and they're not tagged correctly, and you don't have them in your governance, uh, governance processes, and they sort of go out there, and they live sort of as a ghost project forever.


Microphone

 Think about the, think about what agents can do, and AI can do, and the number of projects that they can deploy, that would eventually hit your bill, and it's always gonna be that retroactive conversation.
 Someone from your finance department coming down and saying, Why is our cloud go so high this month?
 Why is our environment built hitting so high?
 If we, as we, as the platform team, we have that repeatable execution process, we know that we have things tagged correctly.
 We know we have things deployed correctly.
 We know we're minimizing security vulnerabilities.


Microphone

 And we also can have our own agents that are interrogating environments and making sure that things haven't run amok.
 Finally, just like normal goods, software development practices, push out poll requests, have agents that are evaluating them, not only from a code completeness, completeness perspective, but we as the platform team, we can put in our thoughts on, let's make sure that these follow all the good, best practices from a platform perspective.


Microphone

 So we can take advantage of the fact now that the code review process can be expanded on, and we can do security and pen testing.
 We can do governance checks during our pool requests.
 We can, and our code reviews, we can do platform checks and tests during our code reviews.
 Once that may have seen onerous and laborious, we can now take advantage of the fact that agents can do these and bubble up issues for us.


Microphone

 Last of our three is governance.
 So, agents, they, AI does, uh, I always share to my children, AI is going to tell you what you think it wants you, what they think you want to hear, right?
 How do you give agents useful autonomy without losing control?
 We as the platform team, we are the guardrails of our platform, of our organization, of our cloud, of our internal, um, internal infrastructure environments.


Microphone

 We become the gargoyles for it, and so for us, having a well defined governance structure allows us to enable our engineering teams so they can move at light speed.
 Right?
 Identity, all of the things that you would normally expect from a well built governance perspective, become even more important in the world of agentic engineering.
 And it goes beyond that, right?
 So agentic identities, uh, maybe now are not specifically tied to human beings.


Microphone

 And so now, you know, what we would once have service accounts that things may run under, um, we would provision identity access.
 We now need to be thinking about how to know your agent, how to know what agent is working against it, how to make sure that, um, they haven't, they don't have, um, escalated permission sets, how their credentials and secret managements are scoped correctly.
 We need to have policy as code.
 Those agents are gonna pull those in, and they're gonna enforce it for us, and bubble up when they can't.


Microphone

 So enforced enforced automatic standards become really important, compliance rules, that human beings would normally just take the time to build in, because we know them, and we live them.
 Now we need to build them in as code.
 Where can we bubble up, audit, and observability?
 What things have changed?
 What agents are acting?
 Why are they acting the way they're acting?
 And are they trying to act in a way that's elevated beyond what you would expect them to be asking?
 And finally, where do you have human in the loop?


Microphone

 Checkpoints and controls.
 When are you letting agents deploy and modify code on your own versus when do you bubble it up so that a person is there?
 How do you have independent agents that are reviewing and testing? How do you ensure that the governance that you've put in is actually being followed?
 These guardrails, these things that we put in, allow us to move very, very quickly. And one of the things Dan and I talk about all the time is that the speed of software is moving at a pace that none of us, I don't think, could ever possibly have imagined.


Microphone

 For almost my whole career, I've always said organizations should legitimately consider buying overbuilding.
 Because building software is difficult, building a platform is hard.
 Now what happens when the cost of building those things starts to drop to a point to maybe even near, as close to zero as possible, what does the world look like?
 And so, the platform teams, there's this onerous, uh, uh, sort of, you know, shadow in the room coming, because I believe, and I think tensure, we believe, that the amount of engineering and the amount of software that's getting ready to be deployed out in the world is gonna be significant, and how we interact with it is gonna be wildly different.


Microphone

 So the guardrails that you have are gonna speed up that delivery, but also make that delivery safer.
 The better your guardrails, the more autonomy you can grant your agents.
 That's the bottom line, the bottom rule.
 So, for our API that we want to build, and we want to deploy it out, where Asians can work, and what are the requirements.
 How can we ensure that the agent has the right context?
 The platform provides service catalogs, accessible knowledge, dependency standards, and the agents can build it using a proven approved approach.


Microphone

 The platform provides golden paths, CICD, test environments, ephemeral environments, API availability, IAC, and the agents can execute it, implement it, implement it, test it, and do delivery through repeatable workflows.
 The platform provides identity, logging, observability, visibility, reporting, approval checks, quality checks, the governance of your platform.
 The agents can operate within that well defined permission set that you know what they're doing, and you're not guessing after the fact.


Microphone

 They all three are important, and the maturity of your platform is going to define the maturity of your agentic engineering experience.
 If you miss one, the other two aren't going to be able to make up for the lack of maturity in that area.
 Whereas before, we just relied on humans.
 We relied on them to follow, you know, the governance that wasn't policy enforced, through code.
 We just relied on our coworkers to do the right thing and to know what they were expected to do.


Microphone

 For the context, we just assumed that our team members, if they didn't know the information, they knew where to go find it.
 And those things may not be true in the future of an agent led engineering world.
 And so, it's incumbent upon us to invest in all three areas of the platform, plus all the other ones, but these three specifically, for your agentic engineering experience.
 So, um, you know, the questions that you should be asking with in your organizations align on context, execution, and governments.


Microphone

 Can the agents find what they need to find about your systems and dependencies and engineering rules?
 Because if they not, if they can't find it, they might make it up on their own.
 Can they run the common engineering workflows through standardized processes?
 And do the standardized processes that we already have built today, do we need to think about changing them for the world of agentic engineering?
 And finally, when something has changed, when we deploy, can we prove what it accessed, what was changed, and what controls were applied?


Microphone

 All of those all of those things are all really important.
 And so what is a great way for you to start?
 Pick one area of your organization, right?
 Test it, execute against it, make sure that you can, make sure you can deploy software agentically, all throughout the process.
 And if you can't, close the gap in, where are you missing context?
 How have you hindered execution?
 Where's governance, not there?
 And then expand autonomy for your agents.


Microphone

 They're gonna be here, they're not going away, even if it's just a single developer, using them within their IDE, they're going to be here.
 Attention, we have an agentic maturity assessment.
 You find it on our website, and it walks through all of the different agentic engineering maturity levels that we see organizations going through.
 Sam?


Microphone

 Moment of silence to appreciate.
 what I just got to listen to.
 So, we've got a few minutes now for Q and A, with how active everybody was with sharing where they're calling from, which I love to see.
 Very international.
 We've got a few times for questions.
 Um, I had a question message to me, which you kind of touched on, the build versus buy point.
 Um, but maybe while we warn people up a little bit, we can zoom in on, on build versus buy, a little bit more there.


Microphone

 Uh, so the question was basically, where does build versus buy sit in all of this?
 And I know you touched it on that.
 But maybe we can zoom in a little bit on most of the big providers that we're seeing at the moment are rapidly increasing the amount of tools that they have, the scope at which they touch on to different things. For example, we have our famous reference architecture.
 The average amount of spots in that reference architecture that one of our partners touched was four last year.


Microphone

 Now it's 18.
 So, this is a, literally, almost a 5x in terms of how many places things are touched.
 So I think it makes it harder and harder for people to maybe make that judgment call.
 So what would be some of your advice for making the judgment call between Bill versus Spy here?
 Yeah.
 Dan, I don't know if you have any thoughts?
 Yeah, one of the things I would say is, um, usually those buy versus build conversations, um, you're, you're making a sacrifice, right?


Microphone

 So you're accepting, because of the cost, you'll take 80% of what you want, um, and just buy off the shelf and deal with a 20% gap, some other way.
 Well, we're finding is customers now are really challenging that and they're actually feeling like, you know, it is, it might still cost us more than the licensing fees, but not that much more.
 And we can get 100% on what we want instead of 80%.
 Like, we're willing to make that investment.


Microphone

 Um, and so, it has changed that equation. Uh, it's still worth asking the question, and wrestling with it, and understanding, you know, the trade-offs, but it is, uh, it is becoming far more achievable to lean towards build or buy, uh, than it has been in the past, you know, years.
 I'll cheekily ask my own person on that, 'cause I'm curious, you guys would expect it.
 Are there different domains where the arithmetics are filled with by changes?


Microphone

 So, for example, like, a developer productivity tool versus a security tool or something really strong and secure.
 Yeah, a lot of that often goes, just in the business world, it's a transfer viability, right?
 Like, a security tool, you know, there's, even if it's not becoming actually taking on your status provider, your security tool provider, taking on the liability, right? There's sort of a mind share of, okay, well, we have this tool.


Microphone

 They're the expert on security.
 We, even though we could build something, we just know that they're going to build it better than us.
 And so, it becomes, that usually becomes the tipping point on, you know, where is the business risk?
 And productivity tools become one that often are get moved in internally.
 I've been around long enough.
 I actually built a CICD process before Jenkins existed.
 And so when Jenkins came around, I said, Well, why would anyone do it?


Microphone

 Why would anyone build their own CICD process?
 And now I'm not saying you should go out and do one.
 by any stretch of imagination.
 But now the question becomes, why can't we go out and do something we need?
 And, you know, it also to your organizational size and your maturity.
 Can you actively maintain and build something?
 I think we're gonna see an explosion of open source software over the next couple years, and that just is blows away anything we've ever seen.


Microphone

 Yeah, I think it also, the complexity of the software, and that cuts both ways.
 So, uh, it could be that the software is complex, but the actual this particular client and their use case, they only want to use a small subset of what that functionality is.
 And so they kind of feel like they're overpaying for this more complex solution, and they want to just build their own simplified version of it. Or the software's so complex that it doesn't make sense to try and reinvent the wheel here, and we should go with it.


Microphone

 And so, those questions cut both ways.
 I'd say another question that comes up quite a bit is, like, if there are a smaller organization, um, and they don't have a platform team, what does that look like?
 Now they're a software vendor?
 Like, do they want that?
 You know, do they want to engage with managed services, contract, to, like, sort of manage the fact that now they own software, and they've got to maintain the software.
 Those are all questions worth wrestling with as well.
 But more and more, there is interest to go down that path, and we see the value of that.


Microphone

 Super interesting.
 So we have a question here from Mayank.
 So, how are you tackling the architecture for context?
 Context lies across the org, knowledge, data, process, business.
 How do you bring that together?
 Is there a reference architecture already out there?
 Yeah, great question.
 One of the things that exists within most organizations is there is context that exists, right?
 So you have design diagrams, data, database diagrams, you have architecture diagrams, you have business context, business rules that have been documented.


Microphone

 And, you know, we're all professionals.
 We understand that that stuff often isn't the most up to date.
 Um, uh, it's only as up to date as the last person who was, who sort of went on a documentation tayer with an air organization.
 And one of the ways that I find is one of the most effective at capturing all of that.
 It's actually just having a call and recording it.
 Instead of sitting there and thinking about what needs to be done, one of the things I've done recently is I pulled up some architecture documentation, and I sat with a person who built it and said, Tell me about this, tell me about why it was built away it was, and then tell me about what's wrong with this documentation currently.


Microphone

 And then I use my AI tooling to create and update new documentation.
 And then from there, as things get built and added on, our engineering processes include steps of updating that documentation.
 And so, it now becomes a living, breathing part of your overall ecosystem that is constantly being maintained and updated.
 Yeah, in that same vein, uh, we hear a lot about, uh, engineering leaders talking about the knowledge that's stuck inside of people's heads, and, like, they just don't know how to deal with that.


Microphone

 And so, just reminding them that that, yes, there is a lot of knowledge and individuals, uh, brains, but we also have, uh, a lot of recorded meetings where people have asked these questions. Like, the questions that are being asked aren't new questions.
 They been asked before.
 Likely they've been asked in each slack or teams or in meetings that have been transcribed and recorded.
 And so taking advantage of all that data that you do have, and sort of building a knowledge base out of it, um, is worthwhile.


Microphone

 And so taking and harvesting the information that you do have, and not just relying on the current documentation and the current people.
 But, uh, mind the data that's available to you in your organization.
 Very nice, and we've got a question from YouTube.
 So, how do you assess prioritization for the three platform requirements, and how much does that change for highly regulated businesses?


Microphone

 I would start with the area that's the weakest of the three, personally.
 Um, you know, wherever you're the weakest.
 Usually, execution is usually the strongest point in an organization, because we haven't, I would say, for lack of a better term, we've sort of solved the process of deploying software, and not everything is automated, but, you know, the execution is usually the most mature, because it has affected us the most.
 And so, engineering team members are often the best at making their lives easier.


Microphone

 And I would say start where you're weakest.
 The, from a highly regulated, um, industry perspective, um, one of the, one of the struggles that they come up with is, um, the, the process and the slowness, that is important in those organ, in those industries, in those organizations, from a risk management standpoint, um, might impede you, and so, you know, a governance, document, a governance, um, policy, a governance, markdown file, that's gonna drive.


Microphone

 drive your agents.
 You know, a lot of I's are gonna are gonna have on that.
 And I would say, take, um, run it through, make sure everyone is on board with it, but understand there is a level of urgency and importance, because regardless of what's actually said in your organization, your engineering teams are using these tools, uh, they're using them, you know, even if they're sort of doing it on their own.
 And they're only gonna become more prevalent.


Microphone

 I'll ask another cheeky question of my own.
 Um, one of the things that we're seeing a lot is that platform teams are starting to have to serve far more than just the engineering department.
 They're having to serve. Business teams, I think almost 40% of thought from teams who were surveyed, and that recent report we did, said that business users, general business users, marketing, sales, legal, finance, are becoming customers of their platform.
 Do these three requirements still are still the core focus when talking to those business uners? And how might that change the way you think about, which one you prioritize?


Microphone

 It sounds like, maybe, in those cases, I'm curious, is it because those business units are using these tools, and 'cause we're seeing a lot of that, you know?
 customers coming to us, and, you know, they may have an engineering department and a platform team already, but, you know, someone in finance has, you know, built their own finance tool of some sort, and now they're like, well, what do we do with this?
 And so, yeah, this workflow can apply there, but it's in those cases, it's often starts with more of like an audit and risk assessment, sort of, of like what's already been done.


Microphone

 Is it usable? Or is this just a prototype that we use to feed into the engine and start over with what they've done?
 Um, and so it's that assessment is a really important part upfront when you've got those kind of situations.
 Yeah, and I think too, it's, um, it's going to become consistently more prevalent.
 For some of our audience who've been around for a long time, you know, the old term was Shadow IT, right?


Microphone

 You'd have the, you'd have the marketing department with the server that was under their desk.
 You know, it was running the thing they wanted to run.
 But, um, you know, the prevalence of these AI tools and the capabilities with them, not even just to build an application or to build a solution, but just to run in sort of their own context, run in their own tooling.
 Uh, it's just gonna become, uh, more stronger, a more, you know, forward thinking solution.


Microphone

 And I don't think platform teams should be afraid of that.
 I think we should be excited for that, because that's the whole purpose of the platform.
 is to enable the organization to take advantage of the platform and to accomplish what it needs to be accomplished.
 And so, I think we should be jumping for joy at this, because it raises the level of importance of the platform within an organization.
 And if you can get ahead of that shadow AI work that's happening and instead let the team, let the whole organization know, hey, this platform exists.


Microphone

 Um, use it, and then, so maybe, you know, someone who is going off and building some of this stuff if they're, if they're following the guidelines and the governance that you now have in place through the platform, then you can skip that audit that I mentioned, right?
 And you can say, like, okay, good.
 Now, we just need to, you know, it's got to go through the productionization process, whatever, however that's defined within the organization, and we can roll it out.
 Yeah, I'll really emphasize, like, this is a golden opportunity for, basically, all of you as a platform engineer listening to this, either live with us or in the future.


Microphone

 I know you're there, high from future, but it's nice.
 Platform teams have just an amazing opportunity in front of them to be the enablers of AI across the entire organization, like everything that we're talking about here.
 Um, it's nice to see, really does.
 These are things you can apply to thinking about these other customers.
 And to tell you a kind of a cheeky anecdote, I just heard I was in the Bay Area last week, a company that almost all of you have heard of, so their company had no kind of coding, like, clawed limits for non business users.


Microphone

 They did for engineers, engineers had sets, limits, no token max saying, set limits.
 Business users, zero limit.
 As you can imagine, that was a total disaster.
 They had to deactivate cord usage for everyone, basically, except for engineers.
 The platform team had been saying, Guys, we can see, because we're pulling all of this spin ups through the butt form, we can see this is gonna be a disaster, and it was a disaster like that that was able to get the platform team, the mandate, finally, to say, Look, the parts that we're running through the platform, we had total control of the cost.


Microphone

 We're doing more at, like, for cheaper.
 And that was the mandate.
 Now, you listening to this, don't wait for there to be a disaster.
 You know, come with some of the positive stuff here and say,
 Hey, look at the opportunity we can take on.
 And we've just got a question come in from Rohit.
 I'm curious to learn from your experience on AI's impact on delivery outcome.
 The metrics that they impact, is it limited to no dementrix moved? If there is more, what is that?
 Have you come across also the link to spend, token spend, to impact analysis, and make that kind of aware and to optimize the AI token usage?


Microphone

 Yeah, um, I can go at it from a business perspective, Dan, if you want to take it from, like, a technology perspective.
 From a business perspective, right now, the the, the metrics that have moved is, um, features going out faster, right?
 Teams, teams are, uh, businesses are expecting more because they've just been sold on the promise that AI engineering is, you know, it's so much faster.
 And it is, but what we have found is that the bottleneck has moved from engineering to the business.


Microphone

 The business isn't ready for what AI engineering has to offer.
 They're just, they're not.
 We can move at a speed now that the process of building a technology solution has just been put on its head.
 And so businesses have to re learn.
 Um, as far as, like, token spend, I, what I've seen is, is there is a just, just sort of like what you were just saying.
 Open the floodgates, everyone can do what they want, because we want to sort of change our organization.


Microphone

 We wanna become AI first, and then you get two or three months of just high quad bills, and then there's a reaction.
 Right?
 And so we, as the platform team, we can put in reporting visibility, observability, and those types of things on spend.
 Because there will come a point, just like, in the cloud, that there will come a point in which you start, um, we start having, uh, allocation to revenue.
 Right? Get our cocaine spin dry, right?


Microphone

 Yeah.
 I can say, you know, with our more conservative enterprise customers, you know, they're seeing like a 3X in feature flow development workflow, pipeline,



```
