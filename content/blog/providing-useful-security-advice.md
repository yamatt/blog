---
title: "Providing Useful Security Advice"
date: 2021-10-29T18:10:32+01:00
slug: ""
description: "And Armchair Security Experts"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I know I certainly dread that message:

> You have a massive security issues by the way

And the interesting thing is, it's often not true.

The trouble is it instantly puts you on the defensive. The phrasing "a major issue" creates an information balance and puts you in a position you have to defend, and you may be in a strong position, but it's stressful and not collaborative.

[As I mentioned twice in my previous post](./armchair-security-experts) security is all about context, and I wanted to expand on that point. You may, in isolation, have something in your environment that isn't ideal. But IT security is entirely about risks and trade-offs. It may well be that you do have an issue, and it may also be that you have managed that already through another control such as alerts for that scenario to happen. Finding that information can sometimes be difficult.

Therefore, the person raising the issue creates an information asymmetry that is hard to develop upon.

Let's turn it around. Say you discover an issue in someone else's service and you want to draw their attention to it. How would you do it in a way that is collaborative and resolves the issue? This question appears a lot in interviews in this industry, but I've not seen a response I'm entirely happy with. Let's expand on it then.

First off, setting the scenario. I'm excluding where you are an outsider as bug bounty programmes are [well established and documented](https://en.wikipedia.org/wiki/Bug_bounty_program).

In this scenario you are a Security Architect, Engineer or similar in a business. You have access to the source code. You also have access to the person who is responsible for the code, and that you're using modern delivery methodologies.

As mentioned, the first issue you have is that perhaps the issue you've found has been risk managed. To account for this, the first step is to check the documentation. I would bet that the issue you are seeing has been documented and difficult to find. Unless you're somewhere that employs enough people and pays well enough to attract good people it's unlikely this is well documented, but let's try to minimise wasting someone else's time first.

In general terms you're trying to identify if your issue is actually an issue and test your assumptions.

Let's say the documentation doesn't have the information you need. Next is to approach the person responsible. I think it's important to coach your wording appropriately. Never make assumptions about the issue you have found. You want to look like you are coming from the position of being wrong, but were not able to find the right information. You are now attempting to find the right information. Phrase it as such. Something like:

> I was looking at your code and I'm trying to identify if something I'm seeing is actually an issue.

Followed by explaining the issue.

There's no point saying there is a massive security issues because, as mentioned, you put the other person on the defensive, and it may well be that you are wrong. You are reducing your chances that you will be listened to in the future, when perhaps there is a genuine issue.

You may discover at this point that they have identified the issue, mitigated it, and the documentation is not something that can be found quickly. At this point you may want to suggest making it easier to find the documentation, but your job is done.

Therefore, if they have mitigated the issue, but they haven't documented it at all or well enough, or they haven't mitigated it at all then you have some work to do.

This is where you should at the very least offer to raise a ticket for the work. This means that it has a greater chance of it being worked on. If you're unfamiliar with the project, this is the point to clarify where they record their issues so you know it's somewhere they will see it.

Ideally the next step is to be proactive. If it's a documentation issue then offer to update their documents.

It also may well be a genuine unmitigated issue, and much the same way with the documentation. If you're comfortable you should then be proactive in fixing the problem. Raising a Pull Request for the change and adding or updating tests.

That way the team with the issue are more likely to listen to you and fix the problem next time, which is the ultimate goal: reducing the number of vulnerabilities.
