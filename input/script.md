<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

 But that's, once again, is another tool, right?
 So you can always control what goes in, what goes out, right?
 The filters in, filters out.
 You know, before and after the large language models, but the large language models themselves are generative in nature.
 That's why, you know, same input can produce different outputs.
 Okay?
 Next one is collaborative.
 This is a power, right?
 It's not just one tool, one thing doing one task.


Microphone

 It's multiagent.
 And the coordination piece is important.
 The planning piece is important.
 Plan for doing stuff into several steps, and then those several steps equates to multiple tools, multiple agents, right?
 And distributed failure model, so that when you ask a tool to do something, and if it doesn't come back with, you know, what the output that you're looking for, you can always try another tool.
 And then, last but now, they staple.


Microphone

 Remembers, right?
 Some of the conversation that you have, the answers that you cut back, is persistent.
 It doesn't go away, right?
 So for sensive memory, as power.
 Okay?
 And also, though, you have to kind of be careful. Once you have data that is persistent, there's always a possibility that privacy, you know, is gonna be kind of sticky, right?
 So you have to make sure that the data that you are storing, you are protecting the privacy of that information.


Microphone

 Right?
 And also, you know, hackers are not going in there and modifying this information.
 So the integrity is going to be an issue as well, right?
 So the people cannot hack into it.
 So those risks comes with once you start to save data, to persist data.
 All right, so here's the last slide on this.
 These are some of these tools, uh, to, that the aid is provide you with, to do all the pieces that I've just been talking about, right?
 So let's quickly go over these.


Microphone

 The reasoning part of it, okay, is the major part is the Amazon bedrock.
 So Amazon bedrock has collection of foundation models, right?
 So these are called FMs, foundation models.
 So the foundation models are, you know, in simple, these are different types of large language models that you could pick and choose from.
 You can choose from the AWS, creative ones, you could choose from third party ones.


Microphone

 You could even create your own and put it in bedrock will, you know, make that available to you.
 So why have it in one place, where you could actually go and pick and choose the existing large language models?
 Well, because Benrock, that is the power, that is, everything is in one place.
 So at some level, bedrock will treat these individual large language models in a generic fashion so that you can apply, let's say, security in a generic fashion, regardless of what individual large language models you're choosing, right?


Microphone

 So, it's great to have that in one place.
 And that security, that specifically that security, that you can apply to all the models that's in the foundation model, is the bedrock guardrails, right?
 So it's a safety and policy filters, and these policy filters, remember the one that I told you, the one that goes before the last language model, the one that comes after the larger language models.
 so that you can be, you know, stay within your governor's rules, those governors' guard whales, uh, to protect your customers and your corporate data, uh, and make sure that, you know, the systems are used in a safe manner.


Microphone

 as far as the security is concerned.
 Taking action, right?
 This is the part that you do things.
 Well, Adam's lamb that, as I mentioned, is a perfect foundation, uh, infrastructure, for writing these tools, right?
 So, it's a surplus tool, right?
 You don't have to worry about the infrastructure.
 AIDS provides you with the enterprise grade infrastructure to run your code, and the code are these ejected codes, these tools that you write.


Microphone

 Now, API gateway is normally the doorway, the window, from the outside world, that is, i.e., from the internet, into, let's say, reaching land the function, and other things internal.
 So, APA gateway does give you a standard way to provide your application programming interfaces to the outside world, right?
 So the entry point, the tools, or even give you interface into authentication systems as well.
 So it's very, very useful.


Microphone

 Orchestration, orchestration, okay, so coordination, right, of all these tools.
 So, I have here about three that are common ones, there are others as well.
 You can even use lime to function to orchestrate, but, you know, why do that?
 Why write your own when they're already very, very capable systems?
 So, step function is, it looks like a workflow, right?
 So, you know, dragon drop these workflows and start creating, you know, start from the top and go at the end. In between, you have these decision points, you know, is X one or two.


Microphone

 And then if it's one, called this lamb, the function, if it's two, called the other lamb, the function, right?
 So step function is that way.
 It's a long running workload, and it does have a rudimentary logic, so it will catch errors, and it'll have loops, okay?
 And it's a plug and play.
 So that is, you know, once you make a decision to go to a program, you can always plug in tool A, tool B, tool C, right?
 So think of that as a workflop.
 Event bridge is a, when something happens, right? So let's say somebody drops in a file into the S3 bucket, for example, right?


Microphone

 S3 is one of these services that's called the source of events, right?
 So, the fact that somebody did something to S3, S3 can actually generate an event.
 Event.
 And so that's the event source.
 And that event could trigger other things.
 And one way to trigger things is for that event to be registered into the service called the event bridge.


Microphone

 And event bridge is like a, um, it will take a particular event that you're looking for.
 Let's say, you know, oh, somebody just put in the file into this bucket, it goes into the event bridge, and then it can actually trigger another action.
 So maybe you have a tool that is looking for that event.
 And then that tool will do its action, because somebody just dropped a file into an S3 bucket, and it was connected to the event bridge.


Microphone

 Okay. And in a similar fashion, Amazon SQS, simple Q service is that way.
 So, it's a cue.
 so that an event can place a message into the cube, and we have, let's say, tools that are waiting for something to come into the cube.
 And as soon as something comes into the queue, it picks it up and takes action.
 Okay?
 And even before the agenda framework, SQS is a used to be, and it still is, a very, very popular tool to do what's called decoupling.


Microphone

 So decoupling is separating out, right?
 The thing that is creating the events and the things that are handling the events, right?
 So if you have, let's say, a program that accepts an input, and then directly tries to call another program that will handle that.
 Well, what if the thing that's handling is busy?
 Right?
 It says, Oh, wait, you know, can you wait for a moment?
 I'm still working on something, right?


Microphone

 The front end has to wait normally.
 Well, instead of doing that, the front says, No, I can't wait.
 I have other people that I have to serve.
 So if that's the case, it's better to decouple those two functions.
 So the front end and the back end, so that the front end says, okay, I got the request, I'm gonna put it into the cube, and, you know, I'm just gonna go back and service whoever's coming with a new request.
 And as soon as you give me the new request, I'm gonna put it in the queue.
 put it in the queue.
 put it into the queue.
 And the thing that's handling the back end says, Okay, I'm working at the paste that I'm capable of.


Microphone

 So I'm just gonna work at my own pace, you know, going back to the cube, you know, handling the work.
 So the analogy here is, like, you know, going to the coffee shop, right?
 So, in a crowded coffee shop, you give your order to, you know, the cashier, the cashier places the order, maybe she takes, or he takes the posted notes and post and say, okay, we have, you know, one espresso, and the other one is, you know, latte, whatever.
 And then we have the baristas working feverishly, and going back to the queue and say, okay, what's next?


Microphone

 Oh, okay, we'll have to do the espresso.
 In the next one.
 Oh, yeah, we have to do the latte, right?
 So that's separated, right?
 It's not the cashier that takes the order and actually makes the coffee at the same time.
 No, right?
 So that is basically what SQS does in a digital world.
 All right, another one is remembering.
 Remember we talked about how remembering is very, very important, the memory, okay?
 We've already talked about Dynamo DB.
 It is a no SQL database.
 It is a enterprise class database. It is super, super fast.
 Super efficient.


Microphone

 The knowledge basis, so knowledge bases are historical data, corporate data.
 It's probably what you would imagine as a database, as I mentioned, but we call them more generically as a data sources.
 Now, it doesn't have to be a database per se.
 As long as there is a historical data, that one can go ahead and pull like a database.
 Then, remember the monitoring part, the operational part, right?
 It's not enough, just to make this thing and make it work.
 It has to keep on working.


Microphone

 And understand when something goes wrong.
 then to perhaps notify people when there are some abnormal behavior, right?
 So that all requires monitoring.
 And Cloud Watch is the hub for monitoring activities.
 Uh, the metrics, right, performances, uh, in AWS infrastructure. So, Cloud Watch.
 IAM stands for Ididity Access Management.
 That is where we can assign what a, let's say, an entity.


Microphone

 We call them principal, principal identity can do.
 So programs are considered to be identity slash principal.
 So this is where we can give it permission to access certain things and do certain things.
 So, I am is the hub for identity based management of users, and the permissions.
 All right, so we talked a lot, but this is the foundations, okay?
 And we are almost ready to move into the next tour, which is the architecture pillar, which is a pillar number one.


Microphone

 All right, so let's talk about the first major pillar of this webinar is the architecture, right?
 So the architecture, what are we talking about?
 How do you design this?
 How do you design this?
 And it has to be the enterprise create, right?
 Not just a proof of concept, not just demos, okay?
 So, I will show you a slide that kind of tries to put everything in one slide, so it may look a little bit busy, sorry.


Microphone

 But let's go ahead and take a look at it.
 First thing that I would like for you to look at is that they are layered, right, and I have them as experience layer, so experience layer would be the user experience.
 You know, what does the user see?
 And how are they interacting with the system?
 Then we have the orchestration layer, that makes decisions as to, okay, who do I need to corral to, you know, do this thing that the user is asking for?


Microphone

 Then we have the agent runtime layer.
 This is where the heart of the AWS's agentic framework comes in.
 And so this is where we will incorporate all the, and I'll explain what the supervisor is, but the aged Amazon deadrock in its systems.
 Then, we have the tools and memory and data layer at the bottom.
 So the fourth layer.
 And so we've already, you know, discussed what memories are.


Microphone

 And then, at the bottom, we have the crosscutting, horizontally crosscutting features of existing AWS services that is going to add to this whole thing, okay?
 All right, so let's go back.
 up into the user experience layer.
 I'm not sure if my cursor is going to show up here, but I'll give a shot here.
 right?
 So right now, I'm pointing to the users and application, right?
 So that's usually how users will, you know, get into the system, is that there's some type of a user interface.


Microphone

 Now, that's not a large language model.
 is usually a, you know, a user interface program than somebody wrote.
 Okay.
 And normally, unless it's open to everyone, and, you know, you don't have to prove who you, you know, who you say you are.
 And normally, it's where you have to provide who you are, and then it's determined, okay, so please do the authentication, provide proof that you are who you say you are, okay?


Microphone

 And also, based on that, the system will know what you are allowed to ask, what kind of systems you are allowed to touch, right?
 So that authorization pieces of it.
 And also, everything that the user does is record it, you know, for later use, and also for observing if there are any type of behavior that is, like, you know, anomalous behavior.
 And that part comes in at the authorization, Cognito, right?
 So, Cognito is a AWS service that helps with what's called the Federated User Management, Identity Management, and also, it can help you with the authorization with incorporating the identity access management for that user or for that role, right?


Microphone

 So, this class isn't really about the security class, so I'm not going to go into those individual pieces, but, you know, if you're interested, a intercom has classes based around AWS and security.
 So please, you know, think about taking a look at those classes.
 The Amazon APA gateway, I've already mentioned, is the doorway or the gateway, into the ADS world where all the tools, the programs, reside, right?
 So, items has a very strong security model where people, not anybody who just wants to come in can come into AWS.


Microphone

 So, especially for accessing the programs which are represented by APIs, application program interfaces, and the Amazon API gateway is a very common tool that we use to regulate that part.
 So, normally, users will reach out for the application, it hits the API gateway, and then the APA gateway may reroute them to authorization piece, which is managed by Cognito, right?
 in some fashion.
 I'm not saying that that's 100% that's always the case, no, but that's a very common case.


Microphone

 So then once we have the user who is authenticated and authorized to use the system, now it will invoke, that is, to make a request, to ask something to do something.
 Right?
 So we're coming into the zergetic system.
 And the first layer, after the experience layer, is the orchestration layer.
 So here, we have the Amazon event bridge, step function, and SQS, right?
 So these tools is what the size, okay, who do I call?


Microphone

 Okay.
 And do I put this request in a queue in a asynchronous decoupled manner, right?
 So that's usually the SQS, right?
 So it buffers, and it decouples the front end, from the rest of the process.
 And you can use that if a immediate answer is not necessary.
 So if you are used to going to an application with a web browser, and then ask a question, and you wait until the answer comes back.


Microphone

 Yeah, that's not usually what the SQS does, right?
 So SQS is, you ask a question and then the answer comes back in a separate channel.
 in a separate way.
 So it's asynchronous, right?
 Not as synchronous.
 So that's for being coupling.
 So SQS may not always be the good choice, depending upon what you're trying to do.
 But the event bridge is where you ask a question, and then that message that's in the event bridge would trigger action downstream.
 Okay, so it routes these events, and then it will trigger other actions.


Microphone

 And step function is a very similar way.
 You can trigger the sub function to run, and it's going to run your request in a, like, a flow chart manner, right?
 So all these things will decide as to what to run net in what way?
 Synchronous, asynchronous, buffer, non-buffer, right?
 So that's the choice that we have.
 Then the exciting part here is, okay, now, these orchestration layer, the size, all right, we're going to, you know, help this user, 1st by hitting the supervisor, right?


Microphone

 So you see the agent runtime layer, and see the request going to the supervisor.
 But what in the world is a supervisor?
 We know the word.
 We know in the human system what a supervisor is, right?
 You could probably imagine what it does.
 Okay.
 So, you know, let me take some time to kind of talk about this supervisor.
 So in Amazon bedrocks, uh, you know, now, now multi-agent, uh, framework, a supervisor is a, a top level agent, right?


Microphone

 that actually coordinates a team of specialized collaborators or subagents, right?
 Uh, for, um, solving a complex, multi step tasks.
 Okay? So notice how, in this picture, the supervisor is going to the research agent, the action agent, okay?
 So these are for breaking down complex problems into its individual, you know, specialties.
 Okay?


Microphone

 Then, so rather than, you know, the supervisor, oh, you know, I think, I think I know that answer.
 Okay?
 And I'm going to solve that problem myself.
 No, it doesn't do that, right?
 It breaks down the request, and delegates pieces to the right specialist agent, right?
 And then, it's going to, I guess, in a way, stitches their output back into the final response.
 Okay? And then, you know, feed it back right into the user.
 Okay?
 So some of the key points here of what the supervisor does, because they're so, so important.


Microphone

 is that, uh, there are, you know, what you can do is there are collaborat, what's called collaboration modes.
 So in a plain supervisor mode, the supervisor is going to analyze the input, and then he decomposes complex problems into simpler components.
 Then it will call or invoke the sub agents, perhaps in a serial manner, or in a parallel manner.
 It just depends.
 And they will iterate through until this task is solved.
 That's what we've been talking about, right?


Microphone

 So that's the normal flow of things, okay?
 Now, however, there is a second mode, uh, called the supervisor with routing mode.
 with a routing boat.
?
 So what that is, is that you'll first try to route, simple request, directly to one subagent.
 Yeah? Because it's faster, right?
 Low latency.
 And only falls back to full orchestration for more complex or, you know, something that is ambiguous.


Microphone

 Some, you know, answer that it's kind of, like, not too clear on, okay?
 So it has these capabilities, right?
 So that's the supervisor mode.
 Okay.
 The 2nd major thing it does is it delegates.
 But it then okay, but it doesn't say, okay, I'm done. No, pelicans, but it stays accountable.
 So the supervisor will hand off the subtask to specialists, or specialist agents, but it's gonna say, Well, I'm gonna wait.
 I'm gonna be waiting for the answer.


Microphone

 So it would be, you know, it will retain responsibilities, so to speak, right, it's kind of nice, right, for the overall outcome?
 Because remember, I told you that supervisor will stitch back the answers coming back from all these sub agents, and then, you know, responding back to the user as a one, you know, cohesive answer.
 So it doesn't fully transfer the ownership.
 of the problem.
 It just delegates, right?
 But the responsibility stays.
 Now, supervisor, as I mentioned, is an agent.


Microphone

 Remember, I told you it's an Asian.
 So it's as an Asian itself, the supervisor has access to tools.
 Right?
 And we'll talk about this thing called the action group, when we talk more about the Lambda function.
 So, it has the set of actions and the set of tools that it has a convention to.
 It has access to knowledge bases, and it has access to guardmills, right?
 Just like any other bedrock agent.
 Okay?
 But, you know, it's called a supervisor.
 Now, when you're setting up the supervisor, you designate an existing or new agent as a supervisor.


Microphone

 I say, Yeah, you're it, right?
 Then, you can actually map to or associate up to 10 collaborative agents to it.
 Right? And each agent has a very clear role in the instructions to avoid overlooking responsibilities, because remember, our supervisor is responsible for the entire thing.
 So, sub agents, where these agents that support the supervisor agent, can themselves have collaboration in Abel, right?
 Up to a very soft limit of, like, 3 hierarchical layers.


Microphone

 And in the AWS, when we say, soft, you know, softness, it can be changed, but you need to talk to AWS about it, okay?
 Now, there is something called the inline agents, inline agents, okay?
 And supervisor can also be created dynamically at runtime.
 Yeah, it's like it didn't exist now, but it exists now, you know, 5 minutes later, right?
 Rather than from a predefined structure.
 And I'm not sure if you know what a CDK is, a cloud developer kit.


Microphone

 It's a developer interface into cloud formation, kind of sort of, right?
 And it supports that you let you template reusable agent on the fly.
 Right?
 So if you have a background in CDK, you can actually create these, a supervisor, what's called inline agents, on a fly, based on the conformation template that you can go ahead and, you know, take advantage of through your program using a CDK.


Microphone

 Those are a lot of acronyms, sorry.
 But that's basically how that works.
 Anyway, so this is the supervisor capability.
 And, as you can see, by the subagents, and then at the heart of it, you have Amazon bedrock.
 So Amazon Bedrock is the AWS's hub for everything foundation model.
 And tools, okay?
 And also, I've already mentioned about the bedrock Godrail, so I won't repeat that process, okay?


Microphone

 And the one thing I do want to bring out, and I'm sorry, the slide is a little bit, the words a little bit overlapping, but specialist agents, right?
 So each with one job, okay?
 And these privileged access.
 What does that mean?
 Okay?
 So, this job, so that the agent is not a, you know, something that can do everything.
 A little bit of everything.
 No.
 We're talking about, it can do one thing, but it does that one thing very, very well.


Microphone

 Okay?
 It does one thing, it does it very, very well.
 So that's usually a specialist agent, okay?
 And this privilege is a security rule, rule form, that we and security use, and it says, Okay, when you have a program, like an agent, okay?
 Give it enough permission, but just enough to do its work.
 Nothing more.
 Don't over permission anything.
 And obviously, you can't underprodition it, or I say, won't be able to do its work.


Microphone

 So that's basically what these privileged access is.
 And that's usually done, uh, through, uh, what's called rules, in AWS.
 Okay, I think I mentioned that already.
 And the next one is the tools memory.
 So here, I actually have a separate side that goes a little bit more into memory, so I'll go ahead and, you know, talk about that.
 A little bit later on.
 But notice the supervisor at that layer interfaces into the tools and memory data layer, okay?


Microphone

 And let's take a look at the first one, the lambda tools.
 Okay, lamb tools.
 Okay, so we'll talk about landa, right?
 And landa is a generic platform that's available on AWS that is cerbalus, okay?
 So, let's talk a little bit more about that, because Lanta has huge role to play inside this framework, right?
 So, Landa is an execution layer, right?
 That allows for bedrock agents, like supervisor, or the collaborator, right, those sub agents, actually do stuff.


Microphone

 in the real world, right?
 Rather than just be a big brain, right?
 That's kind of floating in some kind of, you know, liquid, right?
 So it's just a reasoning in text, no, right?
 It sits behind an ages action group.
 So the actual group is a way for which agent call tools.
 So how does lambda fit in into this whole scheme of things?
 Okay. So, remember I told you about, I kind of sort of mentioned the action group, right?


Microphone

 So what does an action mean?
 An action group is a definition or set of capabilities that the agent can evoke, that is, to call.
 So if it's a, oh, no, like a hotel, uh, reservation system, uh, maybe an action group could be,
 Hey, book a hotel.
 Or, hey, check for my reservation status.
 That kind of stuff, right?
 Um, and then, the... So, that's how, what can I do stuff?


Microphone

 It's not just an API schema, right?
 Or anything like that, right?
 But it is, maybe it will map to an API, and it will map to a simple function.
 You know, with parameters, right?
 So action group are those things, right?
 If I accept the capabilities that the agents can evoke via the API, normally.
 And each action group is connected or wired to exactly one land of function.


Microphone

 Okay?
 And then, when the function decides, it needs to call a specific API, bedrock sends an input, right?
 The event, and, you know, with the operation name, plus the parameters, and maybe a session data to that lab.
 So the lab that has all the information, it needs to do that one thing.
 Now, the Landa function actually contains your business logic.
 So, that's the program, right?


Microphone

 Whether to call a database, you know, call another API, query a data store, running calculation, right?
 So those are land functions.
 And then return a structured response.
 Remember, Landa is not AI, right?
 Landa is the way for you to run regular programs.
 So it will respond back to the agent.
 Then the agent will take that answer, and they incorporate it into its next reasoning step.
 Maybe it's a final answer.


Microphone

 Maybe it's a step to calling another agent.
 Okay?
 So that's where London happens.
 Then, remember, going back to the action group, one action group can define up to 11 API operations.
 Okay? But all these API actions only maps back to one land of function.
 Okay, so if you work with London, I think you understand that.
 So, one length of function can have multiple functions within it.
 Okay.
 So internal functions.
 So that function typically branches internally, you know, on the function name it receives.


Microphone

 Okay. And then, permissions, right?
 Because limeda's pretty powerful, right?
 It's a program, okay?
 So land actually has a two different types of permission systems.
 One is actually called a resource based policy, and the other one is a identity based policy.
 So yeah, land actually has both.
 Because land can be a resource that something could call, right?
 So Lambda can say, okay, this program can call me.


Microphone

 Right?
 But no other programs could, you know, use my function.
 So that would be the resource based policy.
 But then the lab that can turn around and call other functions.
 So when it does that, it's acting as an identity, and then it could be limited or given power to call those other services and functions.
 Okay.
 So there you go.
 So lambda, that's how the permission flows.
 Now, alternative dilemma, there's something called return control.


Microphone

 So instead of them invoking Lambda directly, an agent can handle the predicted action and parameter back to your own application code to execute.
 So, it's useful when you want execution outside of AWS or need extra control.
 Okay?
 So that's basically how lambda kind of fits into the school thing.
 Then you have other systems, right? The Enterprise systems, then the VDV for memory, knowledge based, or...
 I have vectors in there, but, you know, red doesn't have to be a vector.


Microphone

 So vector is a way for you to access and query a database.
 It could be any type of data source.
 Then you have Amazon has three, humongous, you know, storage capability as far as the object storage is concerned.
 So that is, once again, one of the main players in massive amounts of storage, and S3 is very, very common platform for that.
 Then, cutting across all these is, we've already talked about the monitoring layer, which is Amazon Cloud Watch, right?


Microphone

 Cardwatch is actually, it used to have three functions, so Cloudwatch could read in logs from other applications.
 So, there's something called cloud trail.
 Uh, and, uh, PBC 4 logs, right? So there are other logs that Cloud Watch can be, uh, told to read in that data, okay?
 So that is, that's still where it's called was lost.
 And Cloud was because it receives all this information can actually create metrics.
 So, for example, if you have a virtual machine, a Cloud Watch can tell you what is the average CPU utilization and such, right?


Microphone

 So it has plugs into these metrics.
 And metrics can be can have assignment and say, okay, so if the CPU utilization goes above, let's say, you know, 60%, do something else.
 So, you can tie that to an action.
 And it used to have something called Cloudwatch events, called watch events, is now, it's a separate, much bigger, much more functions, called the event bridge.


Microphone

 that we actually discussed, right?
 Event bridge, okay?
 So that's at the orchestration there.
 But that's separate now.
 It's no longer as a part of a cloud watch.
 Amazon, or AWS X-rays, right?
 It is pretty pretty good.
 So, you know, when we talk about tools, and we say, these tools are very focused.
 You know, do one thing and do that one thing well.
 That means if you want to do a lot of things, you have to have a lot of applications, a lot of lava functions, okay?


Microphone

 And a lot of these Lambda function, we'll talk to each other, so let the function A, talks a lot, the function B, which talks a lot of the function C, which talk to database, right, A, B.
 It's a network of small applications.
 Normally, we call it microservices.
 But when something goes wrong, how do you troubleshoot these things?
 When you have these little pieces, kind of spread out all over the place across your network.
 Okay?
 This is where it is X ray comes into play because it traces, it traces your request across multiple lambdas, for example, right?


Microphone

 So, or, you know, data sources.
 So once, you know, when something was working right yesterday, but it's not working right today, you could look at x ray and see,
 Well, what happened?
 What's the difference?
 What's the bottleneck?
 So it's an excellent, excellent way to, you know, look at your performance and also as a troubleshooting tool.
 I am always, right, close security person.
 Okay?
 So, at least privilege, remember, we talked about least privilege, and how these programs have to be, you know, guardrailed and, uh, limited in, uh, its powers.


Microphone

 That's exactly what an IA will do.
 And of course, all these things comes with cost, right?
 So we have the cost, and tagging is how you group things together, so we can group things together based on cost, so that it will show up in your billing.
 Or we can group things together for operations, say, Okay, I want, you know, grouping of these tools, group A, to be, you know, troubleshoot or updated, whatever, but not group B, okay?


Microphone

 So, yeah, tagging is very, very helpful.
 ADS is best practice is if you are kind of thinking about, should I tag this thing or not tag this thing?
 The prospectus is tag it.
 Always.
 Okay, you can always take out, pick off the tag.
 But it's hard to put in the tag later on and hope to get information that the tag wouldn't provided you earlier.
 So there you go.
 Look at the, the, the, you know, the, the ecosystem, right?
 The ecosystem, where the agentic framework works.


Microphone

 All right, so, remember, we talked about the, here, the land of function, right?
 So I just want to kind of just very quickly go over some of these features.
 I'm not gonna go into detail here, because we were even talking about most of these things.
 Stateless compute, okay?
 So the state list compute is actually one of the, um, the design principles for something called the cloud leader applications, right?
 Causative applications, more generic way that these applications are written in the cloud, something like Lambda function, okay?


Microphone

 And the best practice is, for that application, to not to hold or persist state.
.
 So that's basically what a stateless compute is.
 Land the function is that.
 And if you think something like lamborf function, land that only exists for maximum of 15 minutes, right?
 So you cannot run a lander, the tool, in this case, an agent, right?
 agentic tool for longer than 15 minutes.
 And then what happens?
 It goes away.
 Right?
 So, if you store data in that lab of function, it goes away.


Microphone

 So might as well not store anything, right?
 But what if you need to store something?
 It says, But I need to know the result of A by this Lambda function, so that it survives the Lambda function itself.
 Okay, then, then put that data in something that is more persistent.
 Like Dynamo DB, okay?
 Don't save it inside the process.
 So that is one of the, you know, the architectural principles.
 Lambda for tools and logic.
 Yes.


Microphone

 Um, it fits the surface model. And you know, you don't have to worry about the infrastructure, it will be created when you need it.
 You're not charged.
 For land of function, that doesn't exist.
 Now the function will come into existence when you call it.
 Yeah.
 So you only pay when you use it.
 You know, compared to that, if you have something running on a server, um, it doesn't matter if anybody comes to the server.
 The server is still running.
 You're paying for the server.


Microphone

 Why do that?
 Only pay for something when you're using it, and land the function will actually do that for you.
 And so it scales from zero to end.
 And, of course, you could put limits on, you know, how many length of function you wanted to run, and you only pay for its use.
 The unimportancy in keys, it's safe to run twice.
 So, let's say, a tool is called three times, okay?
 Right after another.
 So you call, you know, Asian A, three times.


Microphone

 So it's called the first time.
 It's still running, and then somebody calls it the second time run.
 The second instance of that Landa function comes into B.
 And then while the 1st one and the 2nd one is running, the 3rd one is called, and the 3rd one comes into being, right?
 They all work okay.
 You know, they're all separate, and they don't get in the way of each other.
 Sometimes, when you write this kind of application, it's so easy to forget that, right?
 It says, Oh, okay, the second one overwrote my memory that the first one was working on, right?


Microphone

 So that doesn't happen.
 with lamb defunction.
 Horizontal scale and recovery?
 Any worker bees, like lander function, should be able to handle any requests, and if you need more, you should be able to produce more.
 If you need to learn the function, just have two.
 If you need 20, have 20, right?
 So that's usually called horizontal scaling.
 And also, if a lander function dies for some reason, right?
 Maybe it just took in the data that it couldn't handle for whatever reason, you should have a, you know, the dying warper loses nothing because it doesn't store data, right?


Microphone

 Remember, it's not persistent.
 It says, oh, whatever the data.
 Oh, man, that thing that was running, it crashed for some reason and we've all saw the data.
 No, it doesn't happen, right?
 Because we don't store data.
 Okay?
 In the Lambda function.
 So yeah, it recovers, you know, very nicely.
 There you go.
 So this is a surplus first.
 But serverless first does not mean serverless only, okay?
 You have the freedom to create agents in one of the platforms that suits you.


Microphone

 And, you know, best, of course, to have an API interface.
 Yeah.
 So it doesn't have to be loud, though.
 But lamb is just the right fit for this role.
 All right, let's talk about memory, shall we?
 Okay?
 Because memory is pretty important, okay?
 And so here, I have on the side, once again, this is kind of, you know, busy slide, and I do apologize.
 But after the webinar, you should have, you know, access to these information.


Microphone

 So, you know, come back to it and, you know, take a look at it and, you know, research more for anything that I'm not able to cover in this workshop, okay?
 But let's break this down into two major categories, short term memory and long term memory.
 Okay?
 So, uh, what's called the, uh, the A Divus's Asian core memory, okay?
 These are the two categories.
 The short term memory is, it's like a session, right?
 It's like the conversation that you're currently having with the system.


Microphone

 So, it captures it as entropinary, captures the raw, turn by turn, conversation, right?
 Every user message, every agent response, and every tool calls, right?
 We'll create an event.
 It will have a session ID attached to it.
 Okay?
 And if we have a multiuser, we have what's called actor ID, but, you know, a similar sense, right?
 So this is what lets the agent understand a follow up.


Microphone

 Like, okay, so that's what we've been talking about now, but how about tomorrow?
 Okay.
 If he has, how about tomorrow, Asian has to understand, well, okay, so what are we doing today?
 Okay, so that's accessing the memory within the conversation that we're having right now.
 Okay?
 So if we say what about tomorrow, it references what was just discussed, right?
 It's stored and reloaded automatically each turn.
 So the agent doesn't need, but you to resend that history.


Microphone

 We used to, right?
 Several years ago, that was a common thing.
 It says, you know, once you start to catch that, the agent is, like, losing memory.
 Okay, it's like, you know, information just flowing outside of its ears, okay?
 I had to go back to our earlier conversation and then just, you know, copy the whole thing, and then paste it back.
 Okay?
 And then the, uh, it used to be that he'll tell you, I'm sorry, I'm running out of memory of, uh, who we started a new session.
 Okay?
 Then I said, What about all the stuff that we've been talking about?


Microphone

 Uh, you could cut and paste certain pieces, okay?
 But see, you see, that's how a short term memory helps you.
 Okay?
 load up automatically.
 No, compared to that, long term memory.
 So the long term memory works across sessions.
 It runs as a background process that extracts, what's called durable knowledge, right?
 So something that it wants to keep long term, from the raw, short term conversation that we're having.
 And, you know, it stores it for retrieval later, using something called a semantic search.


Microphone

 Okay
 So the semantic search is facts, knowledge, mentioned in the conversation.
 Okay?
 Now, there's also language models are very good at another thing called summarization.
 So it runs summary of a session's key points and decisions.
 But remember, what it summarizes, it could drop some information that you think is important, but the large language model doesn't, okay?
 So, yeah, be careful with that.
 And also use the preferences.
 So, remember, I told you that when I was having a conversation, it says, Oh, I know that you are an aidivist instructor, and you know such and such.


Microphone

 Okay.
 I told you, you know me, okay?
 So, user preferences, like likes, choices, style, preferences.
 Um, I actually have a certain preferences for conversation style.
 Um, I don't usually speak, um, you know, uh, in a language that is disrespectful to the agents, okay?
 I tried to be nice.
 And I expect large language models to come back to me in a nice way, too.


Microphone

 So, if it comes back to me, like, you know, like, we're peers, or, you know, like a rough speak, I'll tell it.
 I say, no, I don't like that language.
 So he remembers the preference anyway, just my thing.
 Um, episodic, custom.
 So other structured extraction patterns that you tell it, okay?
 So, uh, what happens is the, um, you know, how it's used in, you know, when you're using the system, is on new, you know, on each new invocation of the agent, the agent lose the recent, most recent short-term events for immediate contacts.


Microphone

 What were we talking like 5 minutes ago, right?
 Then runs a semantic search.
 Remember facts and knowledge, right?
 Over the long term memory, okay?
 Record relevant information to the current query, and injecting both into the context window.
 So context window is what I can handle right now, right?
 Before it tries to reason, what answer I'm supposed, you know, what is supposed to give back, by default.
 Okay?
 Um, so, um, so anyway, so that's basically how it works.


Microphone

 Now, there is a more simpler path.
 The older path that a classic bedrock agent used.
 Okay?
 So if you're not using this new, new world feature in A-Divis, something called Asian core, if you're just using a plain bedrock agent, support at a lighter memory feature, it applies it and specify a memory ID per user as sessions in.
 So the foundation model generates a session summary.
 We taste it for, like, one to a year, 365 days.


Microphone

 It falls the 30 days, and pulls it into future sessions, sharing the, you know, the same memory ID.
 So that's the older way of doing it, but, you know, it's a simpler way of doing it, okay?
 So, the practical guidance from AWS is that, you know, get the session, short term memory, solid, first, right?
 Typically, backed by Daniel DB, or Inase Cash, which is another type of storage, but more, it's faster, it's memory resident based, by elastic cash.
 Then later on, the long term, semantic memory, only once your knowledge needs, you know, needs our rule that fits into the context window.


Microphone

 So if it starts, if the short term memory starts to overflow, right, then yeah, use the, you know, back it up by downloading the DB in elastic cash.
 Okay, so that's usually how they're used.
 So there you go.
 Okay.
 So I have a bounded, you know, separated, scope it, expire it, right?
 Because, you know, certain memory becomes obsolete after a certain period of time, and you can make that decision yourself.
 Alrighty.
 Let's go here.


Microphone

 Tools, and secure Enterprise Theater access.
 Let's take a look.
 So, this is pretty much, like, a summary of what we've been discussing.
 Okay?
 Um, so, agent, uh, says, I need to do X, right?
 So we've seen that.
 Previously, in the site, it was a user who was saying, I need to do X, but, you know, that gets passed to the agent, okay?
 So in this case, let's say each tool is a, like, a toolbox.
 It's like a locked, you know, toolbox.
 So each tool is a drawer with its own key, right?


Microphone

 Because remember, right, it does one thing, it does one thing well.
 right?
 The Asian can, the Oakland, the, let's say, the refund drawer, but only up to $50.
 Remember, those are guardwales, and never the customer drawer at all, because that agent, in this example, is prohibited from doing that.
 So that would be another, let's say, a drawer, okay?
 So then, the tools interface, these are the functions that the agents will use to do that.
 That is, to refund the customer, let's say, up to $50, right, et cetera.


Microphone

 Okay.
 So here, function calling MCP, MCP, I haven't mentioned it yet, so this is the 1st time that this comes into the site, is a model context protocol.
 So MCP is a protocol, so it's a standard for communicating from one to another, right?
 So agents calling these tools, and I believe Anthropic created the initial version of NCP.
 So that, you know, whoever's creating this agentic system doesn't have to come up with their own protocol every single time, right?


Microphone

 So that if you have a standard way to speak to tools and agents and such, then other people can start creating tools, and you can plug and play these tools, because they all communicate using one language, which is the MCP.
 Then in this case, the least privileged boundaries using the IAM.
 So this is a security, right, boundaries. And here, we have maybe a look up order function, Lambda function, issue refund function, okay?


Microphone

 that's the one that we're talking about right now.
 And search document function.
 Let's say.
 And let's say this agent, the tools interface says, okay, I need to actually, I need to do these things.
 So, you know, if a customer comes in, and if they're requesting a refund, I need to look up that order, then issue a refund, okay?
 And perhaps, you know, put that into the database, okay?
 So, or put it into the data source, in that, you know, in that organization.
 So maybe the look of order function, which is the land of function, will call some enterprise system that maintains the orders, and the order's database, and call that using the, you know, the APIs, order API.


Microphone

 And then issuing refund is the payments enterprise system, with certain limits like $50 in this case, and then call that, once again, using the API.
 Then, search documents, using the knowledge base, here, perhaps the data is stored in S3, in this example.
 So the knowledge base, or the knowledge source, is stored, okay?
 So, there is, and let me just, you know, kind of reiterate the secure enterprise data access, because that's a security piece, that keeps everything private and secure, is, number one, one scope, I enroll per tool.


Microphone

 Roll is a temporary way to assign permissions to an application, like Landa.
 So, give a role to the lemon function, to a tool, right?
 So the agent can only touch what its task requires.
 So that's the least privilege, right?
 Remember?
 Least privilege.
 The second one is data stays in your account, retrieval red, returns the snippets, not the blanket access.
 So, you know, in a traditional system, that was one of the major vulnerabilities.


Microphone

 I'm not sure if you've heard about, um, these types of attacks, or the vulnerability is called esQL injection.
 Very, very scary type of vulnerability, uh, where you meant to use a database in a certain way, but the hacker comes in and just get, like, you know, pretty much free access to everything that's in that database, right?
 Unlimited.
 It's a flaw in the application, but it's a type of attack that the hackers love to do, because a lot of our, you know, modern systems has, you know, data behind it.


Microphone

 And if the hackers can get to the data, in any way that they want, you know, they win.
 So we need to limit that.
 So here, data stays in your house.
 Retriever, we turn snippets, not the whole thing, and, you know, not a blanket access to it, right?
 Limit access to data, right?
 And then last one, at least, every tool call is log, and attributable to the specific actions, specific agent.
 So here, it's about knowing who did, what went, and, you know, if you did it in behalf of someone who did, who did you do in behalf of someone?


Microphone

 Because if you don't keep track of that, if you only keep track of the very last part of something asking for data, you have to ask the questions, say, well, why did you ask that data?
 Right?
 And if that turns out to be some kind of a hacker reaction, you want to know, was that a hacker? Was there something else?
 Like, who asked for you to ask for that data?
 So that's why we're looking for the, you know, who did you do this in behalf of, right?
 So, this is just in case something happens.
 Right?
 Just in case something happens, you can learn and track and do analysis, we usually call it forensics, into the access, perhaps a unauthorized access, so that you can learn that this doesn't happen again.


Microphone

 Right?
 So there it is, right?
 So that's the monitoring, logging, observability layer.
 There you go.
 Oh, we got about a couple more here.
 So choosing the foundation model.
 So, now we're gonna go into the, um, to Dead Rock, right?
 So, model choice.
 In bedrock, you have so many model choices.
 I don't have it, uh, the exact number, but, uh, go go to bedba, you see list of foundation models that you can choose from.
 And, so, some are AWS, natives, AWS created foundation models, some are third party models, and some are UO models.


Microphone

 Okay?
 But the model choice is an architecture decision, right?
 And it has impact, direct relationship to cost, okay?
 Latency as well, right?
 Some are fans, some are so and capabilities.
 Some are specialized, some are good with certain things, some are, you know, some models are trained with some data that you need some or not, okay?
 So, there are compatibility to your application as to your choices on which foundation model you're going to choose.


Microphone

 Okay.
 So, you know, maybe you're looking for some cheap, um, you know, high value type of stuff, and you may want to, you know, use multiple foundation models, maybe for classification type of stuff.
 extracting information or formatting, maybe you want to use a cheap, high volume type of model.
 To a smaller one, maybe you don't need as powerful.
 Maybe, you know, you don't have a tight latency requirement.
 You know, you can save costs that way, right?


Microphone

 And you can separate these things out into multiple models, oftentime in a separate, I'm sorry, in the same workflow. So, yeah, you can use multiple if you want.
 But think about what is it?
 What are you looking for and what is the best cost effective way to do that?
 So, because bedrock is one API, that is, it's all centralized, you know, keep a model, reference, configurable.
 That means you can plug and play these things.
 You could change them later, right?
 That's the nice thing about having it centralized.


Microphone

 So, you know, it's almost like, you know, and I'm not sure you may do this, but analogy here is, you know, you don't send a senior partner in the company to photocopy something.
 I said, hey, can you, uh, can you, can you go to the fax machine if, if you still have fax machines?
 to do that.
 Okay.
 Um, yeah.
 I'm not even I don't even know who you would call that, but maybe you do it yourself, okay?
 Anyway, so let's, let's but they lease the architecture recap for this, um, this here is, let's take a look at it.


Microphone

 Okay?
 A layer with clean boundaries.
 Okay, so we have four layers in the cross cutting functions.
 Use agents that are stateless.
 Yeah, because, you know, because you are writing agents, I guess you could write them a staple, but that's not the current trend in the software design.
 Okay?
 And then, if you must keep space, and yeah, it makes sense that you keep states, the data, right?
 from that conversation, put it somewhere external, where it belongs, like in Dalamudibi, or elastic cash, or into some, you know, relational database.


Microphone

 You know, whatever fits, okay?
 Memory, make sure they're bounded, so you don't keep everything.
 I mean, you know, make sure that, you know, the, um, the separated and scope protein, because of security, who has access to it, right?
 And by bounding it, that is, you're limiting to certain types of memory in certain conversations, that also helps you when there is some kind of a data breach.
 And we call this the blast radius.
 So the blast radius, when someone reaches your data source, how bad can it get?


Microphone

 Right?
 Okay?
 If it's unbounded, yeah, the tax will be unbounded too.
 And make sure you expire the memory, some memory just becomes irrelevant after a while.
 Okay?
 Time to live is a term that's used TTL, set the TTL on these data.
 The tools you use, make sure to assign least privilege, least privilege, okay?
 Because, you know, security's not 100%, it's possible that these agents can be compromised.
 When it is compromised, make sure that it can only do little things, right?


Microphone

 Limited things.
 Okay?
 There is a type of attack called the escalation privilege attack, where a attacker comes into the application, and it will change the application so that it can do anything, right?
 So make sure that make sure that they won't be able to do that by limiting, strictly limiting, privileges, to that agent, to what it needs to do and know.
 Use I am, right?


Microphone

 I didn't dance as management.
 Right size models?
 Choosing the foundation model, that is not too big, not too small, just right?
 for the purpose.
 And every added service equals more to secure, monitor, and pay for, right?
 And because there are a bunch of little programs running around, they're highly distributed.
 And when you have distribution, distributed application, you know, there's gonna be certain things that will cause failures, like network outages and such.
 So, when you have these models, right, that is, what's called Microservices model, that's distributed, that's stateless, you are introducing the nature of distributed application, which has its own set of failures that you need to monitor for and to be prepared for.


Microphone

 Okay.
 That's it for that architecture pillar?
 And I think this probably is a good place to take a break.
 So let's go and take a break.
 Come on back in five minutes and we'll go into the next pillar, which is the orchestration pillar.
 Thank you, and I'll see you back in 5 minutes.
 Sure, we are now going to take a 5 minute break, but before we do that,
 We are going to launch a quick poll that we want to invite you to participate in.
 Doing so helps us know how we can better serve you by telling us



```
