<!--
  아래 코드블록 안에 밋업 녹취 스크립트(STT 결과물) 전체를 붙여넣으세요.
  - GitHub 웹에서 바로 수정하면 됩니다 (저장소 → 이 파일 → 연필 ✏️ 아이콘 → 편집 → Commit changes).
    로컬 git 작업이 필요 없습니다. 블로그 상단 "Add Transcript ✏️" 버튼이 이 파일로 연결됩니다.
  - 코드블록 전체가 스크립트 1개 = 포스트 1개로 처리됩니다
    (밋업 요약, 핵심 요점, 기술 해설, 추구 방향, Q&A, 실천 항목, 참고 링크).
  - 여러 밋업을 한꺼번에 처리하려면 `---` 만 있는 줄로 구분하세요 — 블록마다 포스트가 하나씩 생성됩니다.
  - 이 파일을 저장(커밋)하는 순간 파이프라인이 즉시 실행되고(push 후킹),
    매일 07:00 KST에도 한 번 돌아갑니다. 이미 게시된 스크립트는 자동으로 건너뛰므로
    (텍스트 해시 dedup) 지난 내용을 지우지 않고 두어도 됩니다.
  - 코드블록이 완전히 비어 있으면 그날은 기술 토픽 풀에서 하나를 골라
    미니 기술 브리프를 게시합니다. 블로그가 조용해지는 날이 없습니다.
-->
```
내용을 스토리텔링

YouTube

So to break this out even further, we start with identifying the source.
 And this is really about workload classification.
 So which workloads do I have that are on legacy families?
 In Google, this could be, you know, N1, N2, N2D machine types.
 Um, which of these workloads are stable enough to evaluate, which are causing performance or efficiency pain in my environment today or in my architecture?
 Those pains that you have, those are going to be the best candidates because those are going to provide you an engineering wind and a cost win.


YouTube

 And then we also, you know, we get the performance evaluation or performance data.
 We need to understand how we're getting that utilization, I ops, memory pressure data, right?
 Are we going to be using, you know, installed ops agents on these VMs?
 Are we going to be using native solutions?
 Or are we going to have to take a step back and use generalized benchmarks, like Core Mark, Spec 2017, et cetera?
 And just to be very clear on this, right, you all live in this benchmarking world probably more than I do.
 I'm not here to teach you guys about P99 latency or network throughput, right?


YouTube

 My job is to help us start connecting this story of performance data to cost outcomes.
 And so, What I want to do next, right, is talk about these targets.
 What we do when we identify targets is the 2 things I commonly see is that most people check for 2 things, right?
 They look for, um, does the new vam?


YouTube

This is that new VM family instance type support the workloads that I have today?
 And is what is its list price?
 But there are a few things that almost nobody checks for.
 The 1st is, what is the actual price, right?
 What is the committed run rate of the VMs that I'm moving to?
 What is the discount rates, including their customer negotiated pricing?
 Does that apply to my new machines?
 The problem I see here, right, is that list price comparisons are almost always wrong, as they do not actually match the invoiced reality that you're going to see, reflective of PPAs, enterprise agreements, and enterprise discount programs.


YouTube

 So, That's the pricing conversation.
 The next piece of this is around availability, which is, do I actually have the capacity and availability on the target families?
 So is that available in the regions and zones that I'm looking to move to?
 Um, I've seen far too often, uh, that strong engineering cases die for the modernization, simply because the capacity to do them wasn't actually there.
 And again, AI demand for newer hardware is only making this worse.


YouTube

 So you need to work with your account teams across the respective hyper scalers at AWS, Google, or Azure to get clarity on capacity and availability to know what is available and where that's available.
 And so the takeaway for all this, right, is that it's not just enough to say we want to move on to newer hardware.
 We need to know what you have, what you can move to, whether it performs better and whether it costs less using your rates.
 And finally, right, we need to know whether the capacity actually exists to move.


YouTube

 And so the transition, I want to mention here, right, is that this is really a price question.
 Um, you know, what does it cost on the source and the target and what does that actually cost across the regions and instance families that I'm using?
 And this is kind of a surprisingly hard question to answer with some of the hyper scalars native toy.
 Um, so we actually helped build a tool to help with this problem.
 That's what I'm going to demo quickly.
 If you guys are interested, we can share a link in the chat here so you guys can open this up yourself.
 This is just a quick pricing comparison tool to help us look at some of the data that we're discussing.


YouTube

 So, if you guys go into this link, it's VMPricify.netfloy.app.
 It will take you to this page.
 This is a free tool.
 There's no login, no email gates.
 All this tool does is it compares Google Cloud VM list prices across different regions, machine types, CPU vendors, and then finally, it normalizes for performance.
 So I just want to use this as a quick example, if anyone is interested.
 But this is really just to help us, again, identify that source target conversation I was talking about.


YouTube

 So when I mentioned the term source, I'm looking at source machine types.
 So for Google Cloud, my source might look like I have the abs deployed in U.S. Central, and they're using machine types that are N2 standard aids.
 So they have 8 CPUs, 32 gigabytes of memory by default.
 And I can display this usage that I have today is either a price or a percentage of my percentage of cost.
 If I go to price right, I can view this as monthly costs or potentially daily or hourly cost.
 For the sake of this example, right, I'm going to use monthly costs.


YouTube

 So now that I've identified my source, this is a very common instance type I see in Google.
 I now need to then start identifying my targets, right?
 And we can narrow these targets down.
 Not every single machine type is going to be a good fit for my workload.
 So we can narrow this down by CPU vendor, or we could potentially narrow it down by machine type family.
 You know, Google offers many different types depending on the purpose of your workload.
 Um, if CPU vendors are available, um, this is a very interesting topic, right?
 Because some of the most priced performant machines out there today are on AMD or arm processors, especially for arm right, the new axion processors that Google has are incredibly priced performant, but they do potentially require some architecture redos to actually move your workloads onto them.


YouTube

 And so, once I just give you guys a quick example, let's select a target machine type.
 For the sake of this example, I'm going to be brief and only select one.
 But let's say I want to consider moving from N2s to modernize my workloads onto an N4.
 One of the 1st things that I think is interesting is looking at this purely from a price perspective.
 If I look at N2 to N4 and I run the exact same amount of VCPU in memory, what is my cost going to be?
 Is the N2 going to be more expensive or cheaper than the N4 Atlas rates?


YouTube

 Um, and this is just useful again to really help us with that pricing exercise.
 But then we also need to look at um, normalized performance, right?
 And this is kind of the whole point.
 On raw price, newer machines can look more expensive per hour.
 But if we normalize for benchmark performance, we can actually see that rankings typically flip.
 And so now we're actually comparing against cost per unit of work, not cost per hour.
 And this is important because, you know, we'll kind of go through this exercise a little bit later on in the talk as well.


YouTube

 But if we normalize for performance, we can normalize performance based on relative benchmarks that are available.
 So, um, I can use spec 2017 benchmarks, or I could also use Core Mark, which is a fairly popular one.
 And all of this does is it says, because N4 is a newer machine type, I can actually use less N4s for equivalent performance of N2s.
 And so if I do that, and I'll just go back to this benchmark, right?
 If I can use less that's actually going to result in even greater cost savings.


YouTube

 So if we just look at the percentage difference rate, there, it can be substantial cost savings.
 Not just from the price side, but also if I'm able to use less and reduce my usage as a result of this VM modernization.
 And so this is the tool.
 This is, again, really just designed to help start this conversation.
 It looks at list prices, which I did just say, right?
 This cannot always, this is not always going to be accurate.
 So if you guys are looking at a similar report where you want to understand your pricing, with custom pricing, we can't actually generate an analysis using your pricing data.


YouTube

 There's a little toggle in the top, right, to get started on that process if you're interested.
 Cool.
 So that is really just to, um, help us answer the what question of what do I have today and what do I want to move to?
 Now the question that breaks most plans is the sort of when question, right?
 When is the right time to modernize?
 When is the right window?
 Um, and this is interesting to me because I think this one question about timing is both an engineering and a financial decision.


YouTube

 On the engineering side, right, you guys know this side.
 Maintenance, maintenance and release windows, a safe window where you have to test and roll back, where you have dependencies, risk tolerance, SLO sensitive periods.
 And again, bandwidth, right?
 You might have 10 things on your list, but only capacity to do 3 of them.
 So that's kind of the engineering timing considerations.
 There's also this financial timing, right?
 This is the piece that's usually harder to see on the engineering side, which is when do my existing commitments expire?


YouTube

 What is the burn down of those commitments across my RIs, reservations, CUDs, savings plans?
 Um, right?
 If I'm if I just committed to using N2 resources 18 months ago, and I bought a three-year commitment, if I moved today, that means that I'm paying for capacity.
 I'm no longer using, which is stranded commitment.
 And so it might not make sense or might not make financial sense, right?
 To actually modernize modernize my hardware that I just committed to for 3 years.
 So even if I save money on the workload side by optimizing, that commitment waste I'm going to generate is just going to offset all those potential savings immediately.


YouTube

 So, At the end of the day, this is a coordination problem, right?
 If I modernize blindly, I risk wasting committed spend.
 If I commit blind light, I might block engineering from doing necessary modernizations.
 And so engineering knows when it is safe to move, Venops knows when the commitments expire.
 In my experience, these planning cycles you know, can be commonly disconnected.
 So, the takeaway here, right, is there's kind of this conflict of priorities.


YouTube

 And so you need to plan deliberately.
 And so to do this, I actually want to use 2 kind of concrete examples describing an N 2 to N 4 upgrade on Google Cloud.
 So I'm going to go through 2 options, and I'm going to show you 2 quick examples of beyond modernization.
 Option A relies on using spend-based commitments.
 Think savings plans or spend-based cuts on Google.
 And then I'm also going to show you an option B, which relies on using resource-based commitments.


YouTube

 So you can think reservations, standard reserved instances, resource-based cuts.
 And so across all hyper scalars, the premise of these examples is pretty much the same.
 All hyperscalars offer spend-based commitments, which are usually more technically flexible in the sense that they're not locked into specific machine types or regions, but they receive worse discounts as a trade-off.
 They also offer resource-based commitments, which are more technically restrictive in the sense that they require you to commit to specific instances, families, regions, but in exchange for those restrictions, they receive better discounting.


YouTube

 And so to level set on this example rate, the X axis at the bottom here, this is going to be months from 0 to 36.
 The line in black here is representative of usage.
 And so in option A, um, this is kind of the most common strategy that we see.
 Not because it's necessarily better, but because it's simpler.
 And because it's easier to go execute on.
 And so in option A, just to kind of address why it's easy.
 It's easy because you do not need to know your modernization window.
 So if I have existing and 2 commitments, right, as these begin to expire, what option A does is it allows us to immediately buy new compute flexible cuts or spend-based commitments to replace that.


YouTube

 And it doesn't necessarily, I don't necessarily care whether my usage is on N2 or N4 because these spend-based cuds will naturally float across that usage, even if I do decide to modernize later on.
 And so now a lot of people really like this option where maybe you have existing commitments for N2s, and then you immediately recommit using spend-based commitments.
 Um, because again, it's easy to understand and it's easy to execute on.
 It doesn't require knowing exactly how long your modernization is going to take, or how much of an impact that modernization effort will have in terms of a reduction to your usage, or otherwise known as, you know, price efficiency.


YouTube

 So, In practice, though, when I see customers execute on option A like this, we typically see 2 common issues.
 The 1st is that these compute flexible cuts, or these spend-based commitments that are made, are almost always made too conservatively.
 This is because we see customers, um, that if you don't fully understand what the impact of your modernization is going to be to usage, you may see a drop in usage after modernization, right?
 And so customers don't want to overcommit, so they redo the spend-based CUD purchase and they commit conservatively, which ultimately leaves savings on the table.


YouTube

 The 2nd problem we see is that customers almost always cap their long-term savings outcomes by committing or recommitting with spend-based commitments.
 And this is really just because, again, doing this type of strategy, you're giving up the deeper long-term savings that could be associated with resource-based commitments.
 So this all takes us to an alternative approach that I'm going to describe as option B.
 Um, in option B right, this skips using flex cuts or flexible spend-based commitments, and it rolls straight onto using resource-based cuts.


YouTube

 And this is the option rate that we generally push customers towards, as it can be a better long-term strategy for savings.
 And here's why, right?
 As I as my workloads are my commitments for N2 begin to expire.
 Um, we are going to immediately and temporarily allow this usage to go on demand, right?
 So we're still on N2s, but now that you say just transition to on-demand usage.
 And, um, right, we're going to set what we call a modernization window.
 Realistically, this modernization window from enterprise workloads can be anywhere right from 3 to 6 months, depending on the number of workloads that need to be moved, the capacity and the maintenance windows available to do that migration, right?


YouTube

 And you're going to incur and carry some on-demand costs during this transition.
 And it's really the on-demand cost that scares most people.
 But at the end of the day, this strategy is a math problem.
 It's not a leap of faith.
 And so based on the discount rates associated with your environment, with your private pricing, we can actually calculate the break even point between option A and option B.
 Which is basically just stating, how long can these workloads run on demand before the added cost savings of using resource-based commitments begin to outweigh the long-term savings created by using spend-based cuts?


YouTube

 And so, in most cases, right, the savings that we generate over the lifetime of a commitment.
 Uh, can actually pay for and outweigh the odd demand cost that we would have of doing this modernization period.
 And so, in most cases, right, long term, option B is going to win.
 And so, I know this is an example, specifically for Google Cloud, and it's a very simplified example, but we see the same principle and concept applied for Azure and EWS as well.


YouTube

 Especially in Azure, right, as Azure is retiring, RI reservations for legacy hardware.
 We see lots of customers, potentially panic buying savings plans, which is locking them into significantly worse discounts than reservations.
 And the reason we see this kind of behavior is simply because customers are not able to create a clear plan for modernizing their hardware, which prevents them from using reservations in the future.
 And so, on paper, right? Um, option B, this this kind of plan I'm showing you here, this seems great, but there are some trade-offs.


YouTube

 The 1st is that you need tighter coordination, right?
 You need to know what capacity and what capacity is there and what's the availability to move, right?
 If I don't understand my maintenance windows and how long it's going to take me to modernize, this plan kind of falls apart.
 And so that just means tighter coordination between engineering and fin-ops than option A might demand.
 Trade-off 2 is, you know, future lock in risk.
 Um, you must thoroughly test the machine types that I'm committing to in the future because they are using resource-based commitments.


YouTube

 And so that might lock me into using those over the next one to 3 years.
 And so all of that said, right?
 This is kind of a deliberately simple example, but, you know, it only shows one machine type, one family.
 In real enterprise environments that we work with, there's commonly, right, dozens of machine types and regions that are going to need to be modernized simultaneously.
 And so that's when, you know, figuring out this answer of when, when should I modernize?
 It gets really complicated really quickly.
 And so it kind of raises the obvious question of, if I'm going to do all this work to create this plan, I need to know, is the juice worth the squeeze?


YouTube

 And that's really what takes me to part 3 of the framework.
 which is about worth.
 Um, you know, the kind of a core question here is when we focus on performance improvements, or companies often focus on performance improvements, we can also focus on the financial impact that you can expect.
 And also, right, how does that financial impact?
 How do I translate that and communicate it to leadership?
 And I don't want to spend too much time kind of deep diving, you know, these KPIs.
 Um, this is not designed to be a fin-ups lecture, but at the end of the day, if you're interested in kind of tracking some of the financial KPIs to communicate the worth, um, these are some of the KPIs that we've created at pros props that we really like.


YouTube

 These are objective metrics for tracking the performance of, uh, or savings performance across a portfolio.
 So the 1st one is ESR or effective savings rate.
 This is for tracking the overall ROI from commitments and discounts.
 So am I paying more or less against the list costs than I previously was?
 EAR is actually a different metric, right?
 We call this effective avoidance rate.
 This is about measuring cost avoided by using less infrastructure in the 1st place, right?
 It's a cost avoidance metric.


YouTube

 It not a savings metric.
 And so this is how you can uh, measure and calculate the impact of neon-modernization by using less in the 1st place.
 Then finally, uh, e-core or effective cost optimization rate, this is a combined metric, where I am both paying less and using less.
 And so it aggregates the kind of savings impact across both of those dimensions.
 And so if you're interested in learning more about this, um, we do add blogs uh, linked in the deck as well that kind of show how we calculate all of these rates and how you can go implement them and test them against your real data in, in, in, in practice.


YouTube

 To get back to kind of the story here, um, and sort of talk about why this matters.
 Um, modernization, when we talk about what its impact is, it's going to show up in EAR or the effective avoidance rate.
 And this is the value that vanishes, right?
 If we only report against the list price.
 And so we need to, you know, use kind of some or all of these metrics, if we want to effectively communicate this story to leadership.


YouTube

 Now, to give you guys another example, um, this is talking about price performance without commitments.
 So just to give you guys a quick demo of some of this math by hand here, um, this is talking about an N2 to an N4 upgrade.
 The exact one I was showing in the previous example.
 Um, the point I want to drive home here is that a lot of times, so many people get caught up on the hourly cost of the workloads, and they forget to actually normalize this against cost per unit of work.


YouTube

 When I was showing that pricing tool, right, I was showing normalized cost performance data, which is just the idea that, right, if I have a more efficient VM or VM processor, I can use lots of them.
 And so in this example, if I normalize against, you know, cost per request, I can see that upgrade from an N2 to an N4, even if it's more expensive per hour, it may be cheaper in terms of, you know, cost per unit of work.
 And so we actually have a, again, just plugging a lot of blogs here.


YouTube

 If you're interested in kind of learning how to do this exercise for your own sorts of, you know, cost performance benchmarks that you may have internally in your business.
 We did co-publish a blog with Google, uh, and with a person named Frederico that kind of describes how you can do this again, using your data, using your benchmarks, et cetera.
 So that's linked in the deck as well.
 So that's just, you know, normalizing for cost per per unit of work.
 The next step to this to kind of unlock the kind of true story here is looking at worth with commitments or after my private pricing is taken effect.


YouTube

 And so this is really after we layer this commitment strategy on.
 And this is exactly that kind of option A versus option B comparison that I want to focus on.
 Um, so, right, in option A, we were talking about recommitting using spend-based commitments, an option, an option A, we were talking about recommitting using resource-based commitments.
 And the kind of key effect here is that when we look at committed costs per unit of work, once we layer in these commitment strategies, the added cost benefits, right, that we get by using those resource based commitments.


YouTube

 Uh, can be quite substantial, right?
 In this case, it's up to 26% greater improvement over strategy A versus strategy B.
 Sorry, strategy B outperfor, sorry, strategy, B outperformed strategy A by 26%.
 And this 26% improvement, right?
 That's really the delta that allows us to incur those on-demand costs for a sizable portion of time.
 And so this is kind of that like full worth story that I'm trying to say, is there's obviously performance benefits from modernizing.


YouTube

 And those performance benefits are going to result in an overall usage footprint reduction.
 And that usage footprint production is also what enables us to unlock a better commitment strategy moving forwards.
 And so, this full story is important to kind of understand and it's important to be able to articulate clearly.
 All right, and that's the framework I wanted to talk about, right?
 It's, uh, what, when in worth?
 Um, the last piece I want to sort of touch on, and I'll be very brief about this, is just the use of automation.


YouTube

 Um, everything I just described, read, about mapping your fleets, benchmarking, normalizing, uh, checking against negotiated rates, modeling out different coverage options and modernization windows.
 All of that is very real and hard work to do.
 Um, and I love that quote that we saw in the 1st slide, right?
 Which is I have 10 things to do, but I only have capacity for three.
 I don't want all of this effort to be, you know, number 11.
 And so my point here is simply that modernization can help alleviate some of this.


YouTube

 In our case, right, we can use automations, you analyze cost and usage data, right?
 It can help map your fleet and map your commitments.
 It can help identify modernization recommend, recommendation candidates for specific BM families that should be moved, and it can estimate cost performance using your negotiated rates.
 It can then model out and project cost savings and cost avoidance.
 And then finally, write automation can execute on this on parts or all of this strategy on your behalf.
 So that you're continually covered with commitments throughout this throughout these changes.


YouTube

 And so, you know, there's many routes to automation, automation.
 You can potentially build some automation yourself.
 There's lots of great, you know, AI coding solutions out there that can help with this.
 But if you are looking again for a product solution that is ready to go out of the box, this is exactly the domain and type of problem that prosperops, automates, and solves for.
 Again, if you're interested in this, we're happy to talk specifics after the call today.
 And so the real goal here around VM modernization is just so it should not just improve your infrastructure, right?


YouTube

 If we use automation effectively, we ideally, right, don't create another spreadsheet that someone has to babysit and monitor.
 That is effectively all I had for today's talk, just to kind of close out my final thoughts on this.
 Um, 1st off, right, there's never a perfect time.
 Modernization, or specifically VM modernization rate, it's an ongoing problem, not a one and done type of issue.
 Seconds, modernize for cost performance.


YouTube

 Modernized for cost and performance at once.
 Um, when we look at the best outcomes that get created, we have to be looking at both the fin-ops and the engineering scorecard.
 Three, um, use the framework.
 What, when, and worth?
 I love this framework.
 It just is a very simple way to communicate this sort of modernization effort to multiple different stakeholders.
 Number four, um, real savings, right?
 They go beyond list price.
 If you want to do this work accurately, you have to use negotiated rates.


YouTube

 Number five, measure with ROI-based metrics.
 Today, in our call, right, we discussed effective savings rate, effective avoidance rate, and e-core.
 Um, but there are plenty of other industry standards that you can include and use as well.
 The number six, right?
 Automated.
 This is just, so if you write, if you could automate a problem, you should.
 And so this is going to ultimately be the lever that's going to free up your capacity to go focus on higher priority work.


YouTube

 And so all in all, uh, just to round out my talk here, there's never a perfect time to modernize.
 Right?
 But there is a smart time to modernize.
 Know what you're moving, time it against your commitments, and do the math on whether the juice is worth the squeeze.
 And so, in the example we talked through today, it was worth about 26%.
 And really, you know, that's the talk here.
 So, um, that's all I have for today.
 Let's please, uh, get the questions, open this up for Q and A.


YouTube

 Nice.
 Thanks so much, Andrew.
 Fort and sweet and to the point.
 I loved the framework, especially very interesting.
 Um, well, before you guys are warming up with the questions, uh, something I was interested in.
 So I guess you work with customers a lot.
 So what you see is the biggest obstacle between, you know, we should actually modernize and people doing it.
 Yeah, what is the biggest obstacle between wanting to modernize and getting it accomplished?


YouTube

 Yeah, I mean, most recently, I have to say it's the capacity.
 Like, everything I was talking about around timing, I could have this awesome multi-layered plan around, uh, you know, moving my workloads from N2s to N4s.
 And then I have this thoroughly laid out.
 I have, you know, 7 different approvals from every one of my company.
 The problem we see is that when customers get that plan approved finally, they go click the button, they get an air message from Google or from Azure saying, we actually don't have capacity on the new hardware.


YouTube

 Um, and that's really, again, I mentioned this because that data is so hard to get.
 Hyper scalers keep that capacity and availability information incredibly close to their chests.
 And so as you're creating this plan for modernization, um, it's really important that you loop in your technical account managers or you're, uh, you know, uh, architects at these hyper scalars so that you can get information from them on where the availability is and what zones and regions that availability is in.


YouTube

 Hmm.
 No, makes sense.
 Uh, then there is a question from Dirk. Uh, what is the obsession to migrate from VM very on premise to, um, to Azure?
 Yeah, that's a very interesting question, right?
 Um, the example I was talking about around, um, modernization, the examples I was focusing on are primarily within a hyper scalar.
 So that was assuming, right, that I already was using Azure, and I was running legacy hardware, so like VM instance types or families that Azure introduced seven, 8 years ago.


YouTube

 And I want to upgrade those onto newer hardware within Azure.
 That being said, though, there's plenty of modernization, uh, with the most common form of modernization out there across the customers we see is modernization from on-premise hardware to cloud hardware.
 Um, that's in a completely different set of financial analysis.
 Um, you know, it's kind of that classic, uh, you know, cost of ownership analysis that needs to be done about, uh, kind of renting the services versus outright ownership, outright owning them, which you traditionally have in an on-prem environment.


YouTube

 Um, so yeah, that's a totally different set of problems.
 Um, I think, you know, generally speaking, kind of kind of the sentiment I hear amongst the customers we talk to is a little bit of like, maybe we move too much too quickly to the cloud, uh, in just the respect that, um, you know, cloud can be prohibitively very expensive, right?
 And if you're not careful about how you're managing your costs, a lot of customers have had sticker shock in terms of we've moved from VMware to Azure with the expectation that we would save us, lots of money.


YouTube

 And then those savings haven't come to fruition.
 So, um, yeah, I don't know.
 that's a perfect answer to your question, Dirk, but it is a good one to ask.
 Yep.
 Um, are there any other questions?
 Can you guys?
 And uh, do you do you see this like fin-ups like frameworks evolving now with uh, obviously whole, uh, you know, uh, Companies tracking like more and more this like wordlog spots driven by agents instead of human headcounts.


YouTube

 Yeah, I think, um, you know, in terms of how this applies to the FinOps framework, I think the FinOps framework for one is expanding.
 So it is including things like on premises, costs, and AI costs as well.
 Um, The reason I'm so fascinated by VM modernization to begin with, is it's one of the most clear cut ways to save money nowadays.
 Um, It's also very tangentially related, you know, just to be transparent, right?
 It's very tangentally related to what we already do.
 As I mentioned, right, pros props, those commitment management via modernization is largely impacted by commitments themselves.


YouTube

 Um, but to answer your question, Maria, I think what I find fascinating about modernization is, especially when we look at, just take a step back.
 Cloud Span is going up, AI costs are going up into the right.
 Um, and across all of the organizations that we work with and analyze their data for, um, we see VMO modernization as one of the low effort.
 I savings outcome sort of opportunities that still remains.
 It's not that hard to move my instances from N2 to N4 or from a legacy as your instance to a new one.


YouTube

 And if we quantify the potential savings, uh, it can it can be quite substantial when we look at total cost avoidance.
 Like, again, 20 to 50% of the total compute spent in the cloud environment.
 And so, um, to tie my answer back to your question.
 I get excited about it because it's the low hanging fruit.
 If we can do this modernization strategy quickly and effectively, we are, we can combat a lot of the rising costs that we see elsewhere within the cloud environment.


YouTube

 Yep.
 Oh, totally.
 Uh, there is, uh, I'm not sure, uh, sure, Rama, if you have a question, but uh, I guess it's more of the statement, right?
 In GP, we can use computer class to define backups in case the machine family we picked is out of stock.
 Yeah, that is actually really good information.
 I was not, I was not aware of that.
 I might be following up with you after a day's call to ask you the movie more about that.
 Sounds cool.
 Nice.
 So I guess if there are no other questions, you guys can always contact Andrew either in the platform engineering slack or over the email.


YouTube

 Um, and uh, the Prosper Ops team is going to follow up with the slides and the recording from from the session, so you can always have it uh, handy and review with your team.
 Thank you so much for today, Andrew, and everyone for joining.
 I'll have burgers for dinner.
 So, I'll tell you how it goes.
 Do you have a special recipe?
 Oh, no, I'm mostly, I'm bad cooked, so I usually go out in Chicago and try to try to find all the good restaurants.


YouTube

 So if anyone's ever in town, let me know.
 But yeah, thank you guys so much for having me.
 It's been a pleasure getting to do this session with you all.
 Um, yeah, pleasure.
 Nice.
 Thank you so much.
 See you.


마이크

It can help identify modernization, recommend, recommendation candidates for specific VN families that should be moved, and it can estimate cost performance using your negotiated rates.
 And then model out and project cost savings and cost avoidance. And then finally, right, automation can execute parts of all of this strategy on your behalf, so you're continually covered with commitments throughout this throughout these changes.
 And so, you know, there's many routes to automation, automation.
 You can potentially build some automation yourself.


마이크

 There's lots of great, you know, AI coding solutions out there that can help with this.
 But if you are looking again for a product solution that is ready to go out of the box, this is exactly the domain and type of problem that pros drops, automates, and solves work.
 Again, if you're interested in this, we're happy to talk specifics after the call today.


마이크

here around modernization is just so it should not just improve your infrastructure, right?
 If we use automation effectively, we ideally, right, don't create another spreadsheet that someone has to babysit and monitor.
 That is effectively all I had for today's talk, just to kind of close out my final thoughts on this.
 First off, right, there's never a perfect time.
 Modernization is specifically neon modernization, right?
 It's an ongoing problem, not a one and done type of issue.


마이크

 Seconds, modernized for cost performance.
 Modern asper cost and performance at once.
 When we look at the best outcomes that we've created, we have to be looking at both withinops and the engineers scorecard.
 Three, um, use the framework, what, when, work?
 I love this framer.
 It just is a very simple way to communicate this sort of modernization effort to multiple different stakeholders.
 Number four, real savings, right?
 They go beyond list price. If you want to do this work, accurately, you have to use negotiated writs.


마이크

 Number five, measure with RLI-based metrics.
 Today, in our all right, we discussed effective savings rate that can avoid this rate, and e-corp.
 But there are plenty of other industry standards that you can include and use as well.
 The number six, right?
 automated.
 This is just, so if you read, if you can automate a problem, you should.
 And so this is going to ultimately be the letter that's going to free up your capacity to go focus on higher priority work.


마이크

 So all in all, just around at my talk here, there's never a perfect time to modernize, right?
 There is a smart time to modernize.
 Know what you're doing, time it against your commitments, and do the math on whether the juice is worth the squeeze.
 And so, in the example we talked through today, it was worth about 26%.
 Really, you know, that's the talk here.
 So, um, that's all I have for today.
 Let's please, uh, open something Q&A.
 Nice.

```
