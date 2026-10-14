<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

We have one AWS account today.
 So when do we start with multi-account?
 Because notice that in my, um, webinar, uh, I concentrated a lot on the organization, okay?
 Uh, so that's a multi-account, right?
 So, do you need to do this?
 How do you need to create an organization?
 Well, Yeah, I mean, there are a lot of things, especially in security, that you can centralize using organization, okay?
 Um, so, but don't migrate everything all at once.


Microphone

 No, right?
 Set up the, if it's an organization, and perhaps if you're going to do this seriously, set up a control power landing zone 1st and then slowly, but surely, uh, you know, move new workloads, uh, go into new accounts, right?
 Maybe that's what you can do.
 And the original counts become one workload account over time.
 So you can move that eventually.
 Um, and, uh, but for security, you probably do want to have maybe 3 accounts beyond management account that is log archiving account.


Microphone

 So, you know, archive all your accounts, law, you know, law is centrally managed, all your logs in one account.
 Uh, security tools, but all these tools, they enable them, uh, in one account and maybe a sandbox where you can test these things out.
 Okay?
 Thank you for that question.
 Uh, the 2nd question is, um, uh, it's around automation.
 Yeah, so let me see, it says, isn't automated containment risky in production?
 Yes.
 Yes, right?
 So, if you orbeate everything, yeah, of course.


Microphone

 So, remember, use the maturity model that I gave you that you took a snapshot.
 Automate only high confident findings where the action is reversible.
 Okay?
 All right, reversible.
 Right?
 Don't start to go terminate stuff because that's not reversible.
 So, start with notification, and move to maybe a, uh, one click human approved, uh, run books or automations.
 Then full automation for specific types of findings, right?


Microphone

 So, do small, in small steps, and learn by making mistakes, and, you know, move forward from there.
 So in small steps, right?
 So, and then always, always preserve evidence first.
 Notice that I did the snapshot first before I started the containment, in that lamb process.
 That's an example of that, right?
 So, always preserve evidence first, and scope by tags, and exactly as you saw them in the demo.


Microphone

 Yeah, good point.
 Let's see the third one is...
 How do we justify the cost of guard duty and the security hub?
 Well, you know, security costs money, right?
 So, but they both have free trials.
 So, for example, I mean, the guard duty, 30 day free trial.
 So, and also the guard duty console estimates your monthly costs from real usage during the trial, too.
 So that may be a nice way to look at it.


Microphone

 And then, but most of all, compare against cost of building something similar from the log pipelines, through the intel, you may have to pay for correlating yourself, and then staff to run them.
 Okay,
 So if you're going to do something like this, yeah, compare the alternative and see how much that's gonna cost, right?
 So the demo showed, you know, it showed seconds, right, to contain.
 So, you have to kind of look at the business case around the, uh, the reduced dwell time that is, you know, the the thing being bad longer.


Microphone

 Okay?
 Uh, and containment happens slowly.
 Yeah, compare the cost to that.
 Okay?
 Uh, so yeah, uh, security does cost money.
 And, you know, I'm so glad you brought up because, you know, people kind of say, ah, you know, why do we have to use those services?
 Okay?
 Uh, let's see, the next question is,
 Do we still need a VPM if we adopt 0 trust on AWS?
 Ah, good question.
 Good question, right?
 So for many internal web applications, no, right?
 So ADS verified access gives per request, identity, and device aware access.


Microphone

 Mhm, right?
 So it's not a place, because if you use VPN, it lands you in a place, like a subnet, a segment.
 So that is a legacy way of looking at it, right?
 But some legacy protocols and admin uses may still need a VPN or session manager for now, okay?
 So, 0 trust isn't a, like, a big bank thing that you implement now and done?
 No, right?
 It's a journey, okay?
 So reduce the number of things that depend on, you know, being on the network, and then slowly but surely move to 0 trust as new things come along.


Microphone

 All right, that is actually one of my interest areas, 0 trust.
 All right, so last question.
 So, how should we secure generative AI and agents on AWS right now?
 Okay, so, um, give each agent its own least privileged role.
 Okay?
 So never reuse a human or admin's permission, you know, separate rules.
 Use bedrock guardwils, right?
 So check out Bedrock.


Microphone

 There's this thing called guardrails, for content and sensitive data filtering.
 Um, and log, log every model invocation.
 So if somebody, you know, invokes a model, make sure you love that, okay?
 And for high impact tool action, require human approval.
 Yeah, you can do that right now, right?
 Include AI apps and threat modeling, prompt injection, you know, excessive agency, and things like that.
 All right, wow, those are a great question.


Microphone

 Thank you so much.
 Uh, and I hope you enjoyed the uh, the lecture and I hope you got something new out of this.
 And thank you so much for your attention, right?
 And please come on back for another webinar.
 I look forward to seeing you in the webinar again.
 Thank you so much.
 And see you later.
 Once again, I want to remind you that as you leave this session today, you...



```
