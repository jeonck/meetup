<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
Microphone

Then about 925 events like these and 30 Google conferences all across the world, including different cities where they're North America.
 We have 45 of my chapters, more result towards the end of the session, and we've had 90,000 plus cumulative intentions so far.
 So in case you're wondering, like, what's the test stripe or actually offers to its members, you can have a quick look here.
 We have different options for people across across their pedal.
 So we have a membership, we have on demand courses, live trainings for both consumers as well as businesses.


Microphone

 We have conferences, city meetups, free weaponers, and special mentorship sessions.
 For mentors who selected from across the group, to match your interest.
 Now, just before we begin the session, there's enough promotion from us, right?
 We would like to just give you a quick shout out to our sponsors for the session and our partner's browser start.
 Browser stat has recently undergone local change in case you are already aware of that.
 They have a very short note where even though their grinding is changing, they still remain one of the top solutions within Q.


Microphone

 thank you so much once again.
 And now, folks, as I said, we'll dive right into the session.
 Oh, I'd like to welcome on stage or the speaker for the D Srikan.
 Srikanth is more than 20 years leading technology initiatives for fortune 500 companies across gigging, automotive healthcare and industry platforms.
 Yeah, it's modernized entry systems into Lexi processes into secure AI needed build platforms.
 He's currently pursuing a PhD in here, which you might find interesting, with a focus on Jenny, I, uh, and uh, agentic a lot, normal spices.


Microphone

 He's also an international speaker, researcher, reviewer, netter, and we can all collectively learn from him.
 We have a very warm test drive, welcome from SHIEL. And Shita, thank you so much for doing this.
 Thank you so much, Sandra.
 Yeah.
 Hello, everyone.
 Um, should I get started?
 Do you want me to share? Yes, cut.
 But, folks, can I see a little more activity in the chat?
 Can you welcome Shikha?


Microphone

 off my camera after the same guy every month.
 Yeah, we have the welcomes coming in.
 fantastic.
 Over DC man.
 Sure. Yeah, like me, go and share my screen.
 Oh.
 Is it anyone to say?
 The pain is visible.
 We can see the window right now.
 Yes.
 Cool.
 Yeah.


Microphone

 Okay, um, good morning, good afternoon, good evening.
 Wherever you are.
 Thanks so much for joining today.
 Um, I'm very happy to represent a test tribe and, you know, just go through, um, what is, um, AI tribon automation we have for the mobile testing and today I'm focusing only on the Android part of it.
 As I said, you know, I'm an automation architect working for Caesars.
 Um, I also have um, a couple of chrome extensions, which I'll be being used by, uh, a couple of a few uh, members in the community, which is a playwright student, and also the uh, framework generator.


Microphone

 I'm also part of a browser stack being a chapter lead for them in the Dallas area.
 Um, so let's uh, let's go ahead and uh, tie in.
 Okay, so the agenda is 1st let's try to understand how the mobile technology landscape would be, what kind of technology is used to build a mobile apps, and from the testing standpoint, we can use AI within our command line.


Microphone

 Or we can set up our framework with the AA context, and we'll try to create a small disk case with a plain English prompt, and a demo.
 I have a small app which is built.
 For demo purpose.
 So we'll review that. And then any questions and answers not later.
 Okay.
 Okay, so let's now, let's start with the question, right?


Microphone

 You know, we know that, um, the mobile apps from the front end, it looks same, right?
 Now, how it has been built, we really don't know, right?
 So are they using the same kind of locators?
 Are they using the same kind of technology?
 What exactly it is?
 is what we're going to 1st look into that.
 For that, I have 3 sections here, right?
 There are 3 ways to be is what I know.
 There might be multiple ways, so there might be, yeah, I played way of building as well.


Microphone

 But most of the apps are built by these 3 major technology, I would say.
 The 1st one is the react native, which is based on the JavaScript, um, JavaScript, and it's it's bridged to a real native components.
 Um, and uh, in the middle you see, it's a flatter.
 It does not have any native components at all.
 It draws every pixel with its own engine.
 So it is quite different from, you know, whatever the way the other apps are be to know who the locators are there.


Microphone

 It's totally different.
 Um, and on the right side, you see there's um, uh, native Android, uh, which is uh, based on Jetpack, uh, cocaine and, you know, some of the XML views, you know.
 This other way of building like an hybrid way where you have the web view and also the native view, right?
 That is one more way of building an app, right?
 If you have any questions, now, just start collecting them and we can go through the end of the session again.


Microphone

 So, let me take a simple example here.
 We have a login, login button, which is on the screen.
 Um, from the friend, from the uh, the way we see, it looks like it's a normal, right?
 But for the automation, when we are trying to automate, how the automation script should look at, right?
 So if it's an Android native app, the button is found by the resource ID and context description, right?


Microphone

 And by the text, right?
 You can identify the object with multiple ways.
 You can, of course, use expat, but that is not recommended, right?
 If it's a react native, it's by the test ID or by the accessibility ID, which is a common way of identifying the allocators or the objects on the, on the screen, and with the flatter, with his, you know, it's a semantic labeling or, you know, it's a, you know, key in the widget tree kind of stuff.


Microphone

 I don't have much experience on the flutter automation, but yeah, if anybody is in the group who have more knowledge on flutter, I would like to hear from them as well.
 You know, if they are trying to do any automation on the flutter apps.
 But, you know, for as a human, right, as we see, it's only one button, but for a lot of mission framework, it's a presentation of that button with a different way, right?
 It changes based on that technology, correct?


Microphone

 Um, so one gap, uh, what we need to fill in, right?
 for the same login scenario, which I see, we need to set up context.
 From the unit, it's a simple one sentence.
 No, we don't have to do anything like, you know, we just a view at the screen.
 But for the automation framework, what we need to do is set up the context.
 We need to sell with the locator, which attributes, it needs to be, you know, what is stable, uh, can I pick export?
 Can I pick accessibility AD if I don't have accessibility AD?


Microphone

 What is the other way? Do I need to use a predicate or all those kind of things?
 right?
 Um, and then what kind of weight we need for uh, element to be visible? And um, the actions, what we have to perform, or whether it needs to be an uh, tap on the screen, it needs to be a swipe, or it needs to be on the, uh, on the screen with um, with the coordinates, and then validating, you know, making sure the assertion is uh, also done, right?


Microphone

 So these are the 5 different steps, which we need to provide to the automation framework. That way the framework is much more stable and, you know, the disk is created or valuable.
 Okay, so let me go further. So I said, the framework, what I'm going to show, which is, again, you know, which is there on the guitar, you know, if you want to download and you can go through that.


Microphone

 What we have, it's a 4 components, what I was split into.
 Um, 1st is, um, we have the A, which is an A, I, CLI, which, which will help us to, um, it's like according tool that runs in the terminal and it, it, it's a files, it runs a check after every edit we do and also it can commit every changes to the gate.
 No, that's a small tool, which is, which I'm using gear.
 Um, There is one more, um, the 2nd tool, which uh, which I've made for myself, uh, to save some, uh, tokens uh, what the AI uses.


Microphone

 So basically it removes the repeated context before it goes to the model so that, you know, we have, there isn't the fever tokens.
 This is, again, it's an MPM package, which is uploaded there.
 And the 3rd one is, um, the repo by itself, or Kit Labrapo, where we have our, um, the web driver.
 I'm using the web driver, I go.
 Within the web driver I go, the framework is having the conventions dot MG5.
 It has the spec files.


Microphone

 It has the app map. MD5 where we have the actual app related locators and the text and those kind of things.
 And there are certain standard prompts which you can use.
 And what are the validations you need to do whenever you create a new test case, you can always run the validate a script where you go, review all the unit test cases, which is built within the framework.


Microphone

 And, um, literally, we will provide you the feedback now if you have, if there is any fixes you need to do.
 And the 4th part is the browser stack, you know, the browser stack, uh, as you know, like, you know, they have the real, uh, phone, which is, which we can connect. And we run our test cases against the process stack, uh, devices, right?
 So whenever we try to create a test case, usually it will not touch the phone until unless we are executing them using the browser stack.


Microphone

 You can always set up your local Android emulator, you know, for you to run.
 But no process tag is having all the setup, you can always use that.
 But either way, it's your choice.
 Right.
 So within the framework, what I, as I said, within the frame of what we have is, uh, the either.config. ML file.
 Um, this is just a small config file.


Microphone

 Every time when the when the tester is trying to send the prompt, um, it's going to go through this, um,
 Sorry about that.
 Like, it's going to go through the, um, conventions MD.
 It will go through the app map.md.
 It'll review the screen dot GS5.
 And also we can go through the data dot JS file.
 So what do we have within the convention?


Microphone

 You know, we have certain rules set up for the framework to do, 8 rules, basically, but we go through one by one and when I open the framework and we can look into that.
 Um, app map, it'll have the, the screen, their IDs.
 There is a message or the text which we need to assert.
 Everything is set up as part of the app map.
 It like a locator file.
 You can see, you know, if it's, if it's a deer or automation frame, which are built.


Microphone

 What screen and data is having?
 They are having like a shared weights, how the key keyboard should be angry, whether it needs to be a swipe or tap or those kind of things.
 And also other test data within that, right?
 And, um, we have the same file, um, very, as I said, you know, it will run the validate script.
 And it can validate, like, you know, if there is any failures, you know, immediate failures, you can see if there is any syntax, or, you know, the formatting, it's going to show up for you.


Microphone

 Okay.
 Leaving more context on app MD file, um, as I said, we will have something like this where we have a sign in screen.
 Um, we have an locator, um, like email is a field, and uh, uh, this is accessibility, uh, accessibility KID.
 So we have input type on email is what the object locator is similar to that password or any other objects or locators we have got on the screen.


Microphone

 really be identified by this manner, you know, right now I'm using all the accessibility IDs here.
 You can always use predicate as well.
 That's a more way to identify the screen.
 So. Just good things.
 Hopefully everyone, at least most of them, are working with mobile test automation, or you are going to work on the mobile test automation, is what I assume, or you, whatever the interest is, you are having on the mobile automation.


Microphone

 Yeah, please list on your questions so now we can go through that.
 Right?
 So, the context part is very important, you know, for AI driven test automation free work.
 Without the context, provided, you know, we cannot create any test cases by just by the regular prompt, you know, we'll have to provide the context of your application.
 We'll have to tell, we'll have to set up in a way that now we know what kind of screens we have got.


Microphone

 If there is a new screen, we have to go back and update our identity files, you know, those kind of things we need to do.
 Uh, and again, we can use AI for that as well, you know, after your app is built, and we can tell, yeah, to go back and update your app and defile and also the locators for your application. Um, but we need to set the context to our framework, you know, that way we'll be able to create a good test cases.
 Right?


Microphone

 Um, So this is the kind of 8 or 7 steps, which we need to do.
 One is the intent.
 Say, for example, I'm going to write sign into, sign in with our demo data.
 Uh, log, um, your gym.
 This is a gym map, you know, you log in your workout.
 Uh, with whatever the, uh, reps you're going to do, and then, you know, enter the count and log out of the screen, you know, those kind of, uh, uh, prompt you need to provide.


Microphone

 You'll ask the framework to create a test case for your app, or it can be any app, you know, in this matter, it is the gym app.
 So, the 2nd step, it'll understand the project, if you find the screen on the object, if it is not able to find the locator or not, it'll go or take the app to file, and it'll resolve the locators based on the context it is going to get, and if you generate the web driver, I go, um, I went play when I would test script, you know, the spec files and everything, it'll run the validate, uh, script,


Microphone

 And then it'll run on the actual Android device.
 Now if you have set it up on the cloud.
 Okay, so before I go to the live, I'm also, this is just a, a small app, as I said, I don't know, which is based on Expo, and, um, it's a very simple app, and you log in, you see a small screen where you learn to all your gym workout data, and then, you know, move further.
 Um, and then log out, right?
 So, Let me skip out of this and then go to the actual framework.


Microphone

 Okay.
 So, this is a framework what we've got, as I said, we have multiple folders here.
 The interest of what we need to see is the apps, you know, this is the APK file, which I have uploaded for for us to run the test case. And this is again uploaded to the closest tank, you know, that way we can run the test cases on the process tack.


Microphone

 Uh, if you're using your local emulator, you can always um, point it, point your, um, test, test cases to this particular app, so that, uh, so that it can open in the emulator.
 Um, The main thing is our, uh, test, we have a spec files here.
 So all these pick files are created by the AI, script with the prompts.
 There are multiple scripts here.
 We try to create one more.


Microphone

 And as I said, you know, this is the app, map.indefile, um, where we have the landing screen, signing screen, and those locators are objects.
 Um, similar to that, uh, some of the test accounts, sign up screen, you know, all the, all the screens what we have got on the app, you know, that has been captured here.


Microphone

 Um, And I wanted to go to the conventions, um, So this is a convention dot MD5, which I was talking about.
 Um, so this is what I'm telling you, right?
 Every test starts on the landing screen and it has to have a behavior with it.
 And a spec calls intent level screen methods needs to be created. And you can change this, you know, you can use a demo or whatever those, what are the test accounts you want to use, right?


Microphone

 And we say, what are the screen methods we have got here?
 Um, and we provide a golden example of exactly it needs to create a discuse.
 This should be on this kind of, right?
 And we also say never weaken the, or date an assertion, to make the test passion, to make sure that it's always doing the right thing, right?
 And also don't change the configs.
 Uh, don't edit the files, um, which you're not asking you to do, you know, those kinds of things, right?


Microphone

 So, this, this conventions, you can always go back and update, right?
 You, you, uh, based on how the framework is generating your test cases, you know, uh, you can always go back and uh, do that.
 So, How do we bring up our AI tool is, um,


Microphone

 Yeah, so.
 Sorry, I just, um, I did a NPM install already here on once you download the framework, all you need to do is uh, 10 PM alarm setup.


Microphone

 It will run the full setup for you.
 Right now, it's already installed.
 Oh, it's failing.
 Yeah.
 Okay.
 So it's all past now.
 So you can do a NPM, Iran.
 AI.
 You can, I'm going to use golf, but you can use Gym Rai or if you want to use anthropic.
 Or if you want to use a new open EI or anything, right, you can of this, uh, use them.


Microphone

 I'm not sure. It is too many.
 Okay.
 So, yeah, I'm gonna see a simple diskies, create a new test case, or login, and name it as... login, test, thoughts, like, okay?


Microphone

 Log in.
 This isn't me just, let's see if it's going to be great.
 Uncle, come here.


Microphone

 Okay, um, seems like it's not getting connected, but Let me go back to my deck.
 I think I've captured uh, Those here.
 So say, for example, if I'm going to create a provide a prompt here, this is a prompt which I'm going to enter.
 Um, as I said, and I was trying to run the AI tonight and um, write the test, right?
 What it does is, you know, it's going to create a test case for us and then it can validate, as I said, you know, you learn the MPM validate, and he'll have like, um, 25 plus unit test cases, it's going to run that.


Microphone

 Uh, and then, uh, we run it on the process tack.
 Okay.
 So, let me see if I can at least run that disk case on the process.
 It's always happens whenever I'm doing demo.
 So, I'm going to run uh, logins spec, uh, test case on the process tack.


Microphone

 Again, and all, I've set up my closest credentials over here, um, with our, uh, invite file and it's going to run this particular, this case.
 Let me bring up the closer stack.
 Yeah, it started a new disk case here.
 Yeah, I'll go back and verify on the framework.


Microphone

 Um, one is that the gym name was not able to get connected, but, uh, the Gork was supposed to work.
 I didn't know why I did not.
 Let me try... Lord.
 It's not set.
 Okay, so, that this case is running, yeah, so let me go back to the one which was already executed.


Microphone

 Um, so it'll have a session created for us.
 In that.
 And this is our test steps, which has happened.
 So, basically, There's an app I'm going to run from here.
 It's going to bring up the app and provide the credentials.


Microphone

 And then log out, very simply just kiss.
 Yeah, I think even this is done.
 Let's see.
 Cool, yeah, so.
 I think that's all I got, um, Let me try one more time if I'm able to.


Microphone

 Oh.


Microphone

 Okay.
 Okay, seems like to be working, so I just provided the prompt and It is asking me to, whether or not it needs to create a new fight.
 I'm going to say yes.
 And the Spect 5 will be I'd work out, login and logouts back.
 Hopefully, it should come down Korea, let's see.


Microphone

 Okay.


Microphone

 Yeah, so basically, that's all I had to present, but I'm trying to see if I can able to find the test file.
 I did not provide the location if I provide the location, it should have created the right place I play.
 Sure, fair enough, fair enough.
 You can take a couple of questions till that's legal.
 Sure. Like, what are you waiting for it?
 So, a couple of questions around the app. MAP5.
 Uh, right? Yeah, put my file.
 So, like, how do you exactly go ahead and build that?


Microphone

 Yeah, so the app. MD file, you can always ask your AI to build.
 Um, based on the app, you would have uh, so you can provide your app uh, details to the uh, to your uh, AICLI and ask it to create uh, uh, the locators, you know, because it is integrated with APM.
 Uh, it can go back and review your app and, you know, get all the locators for you and create a laptop and file for you.
 Yeah, cool.


Microphone

 And then follow-up question to that.
 Why do we need it?
 Why do we need that app to identify?
 Why can't you just use conventional TH object?
 So you can, but I'm trying to split between uh, uh, the files to care, look, because uh, what happens is, um, when your app gets more complex, you'll be having multiple screens and, um, ideally, uh, earlier I was thinking, you know, it has to be based on each screen, you know.


Microphone

 Again, it is based on the complexity of the hat, right?
 So it is always to better to split and keep it a little small.
 I would say.
 I mean, that's how I'll do it.
 But you can always work, you know, as per you are, um, you are need and, you know, how the app is behaving.
 If it's a very small app, you can put everything inside into one line, you can always do it.
 So, uh, the next question comes from Manisha, big, uh, he asks, uh, big, they, you have guard, or guardians and peace, which is good.


Microphone

 How do you ensure that they're maintained like a value like this?
 Yeah, that's a very good question.
 So maintenance is always a challenge.
 Um, So, there is a, there is a way you can do a self-feeling part of it along with the, uh, with your, um, in the conventions while you can always go back and add a certain unit test.
 Telling that, you know, before you run out, before you create a new test, you can always go back and valocate the existing one.


Microphone

 And within your conventions while you can define that part of it, um, and also you can have a separate script created for the self-feeling part of it, you know, whenever you run your 90s, say, for example, you're doing a nightly execution and you see like, um, there is a bunch of tests which is failing.
 You can have an self-feeling script created and where it will go and verify if the locator is a change or if the screen is changing, you can generate a report, claim that what exactly causing the issue, right?


Microphone

 If it's a one issue, which is failing, all of the test cases are, it's a different issue, right?
 So you can set up your framework in such a way, where you can self-feel and maintain by itself.
 Um, but it has to be like um, every time, like every night or weeky or whatever.
 Again, it is based on the complexity of your application.
 Go.
 Go, go.
 Yeah.
 Do you want to proceed right now or like with no questions or do you just want to?


Microphone

 Yeah, I mean, I mean, I'm done with my demo, basically.
 Okay.
 I'm just trying to see whether it's going to create a file, but mostly I'm done.
 Got it. No problem.
 Yeah.
 Agreed, so just a couple of things here.
 Shika, like this one suggestion, I think you might have shown your keys, like your intake is at some point.
 might as well change that up to the session.
 Right? And again, once you are able to change your keys, the people that are asking for their repo, again, folks, like you can have a look, but at least do change the keys.


Microphone

 Okay, she can't try and do that hopefully before that.
 You can scan an equal on your screen right now.
 You'll be seeing you'll be getting access to the guitar, like the record.
 Sure, yeah.
 I'm going to change that.
 I did not realize that you are recording.
 I like it.
 But before we share the recording, please, we just should, uh, if we'll give you more than in the pin.
 And all those who are asking in the audience, like whether we be sharing the recording, yes, we will.
 So, uh, with that, uh, again, uh, like I'd like to give a huge thank you uh, to Srikanth for doing this.


Microphone

 It's lovely to, it's lovely to hear from you, not this limited amount of information that's coming in with respect to AI and mobile automation particularly.
 This gives us a really good view into it. And take a wheat, encourage you to speak more on this topic, like teach as many people as you can on this topic, because it is an important one, for sure.
 And with them at home, I'd like give a youth statue, which you can't like that. Can you just get a couple of packages in the chat for Sri, during this session? Because again, he's the people in our community do this of their own, like on their own free time.


Microphone

 They all have regular jobs, right?
 They take it out to educate the community and get better at it.
 So a huge thank you, THC, but for the session.
 Sure, thank you, thank you so much.
 Thanks for the opportunity, and of course, when you go to the repository, please download and see what we can do and it's still baiting, right?
 So there might be a lot of feedback.
 I am sure I'm waiting for that, you know, I want, we want to make sure that it's really working.



```
