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

It instantly puts you on the defensive, and in my experience, it's also not true.

On top of that the phrasing creates an information asymmetry and puts you in a position you have to defend. You may in reality be in a strong position, but by starting off with a non-collaborative discussion it can be difficult to identify the true problem.

[As I mentioned twice in my previous post](./armchair-security-experts) security is all about context, and I wanted to expand on that point. You may, in isolation, have something in your environment that isn't ideal. We all do. The alternative is to have no service at all. But IT security is entirely about risks and trade-offs.

It may well be that you do have an issue here, and it may also be that you have managed it already through another control such as alerts that warn when that scenario happens, but to an outsider it is often difficult to draw the relationship between a risk and a control.

Let's turn it around. Say you discover an issue in someone else's service and you want to draw their attention to it. What would be the best way to broach that subject? It needs to be collaborative and resolves the issue. This question appears a lot in interviews in this industry, in one form or another, but I've yet to see a response I'm entirely happy with. Let's expand on it then.

First off, setting the scenario. I'm excluding where you are an outsider as bug bounty programmes are [well established and documented](https://en.wikipedia.org/wiki/Bug_bounty_program).

In this scenario you are a Security Architect, Engineer or similar in a business. You have access to the source code. You also have access to the person who is responsible for the code, and that you're using modern delivery methodologies.

As mentioned, the first issue you have is that perhaps the issue you've found has already been risk managed. To account for this the first step is to check the documentation. There is a chance that the issue you are seeing has been documented but difficult to find. Unless you're somewhere that employs enough people and pays well enough to attract good people it's unlikely this is documented at all, but let's try to minimise wasting someone else's time first. Time they could spend resolving other issues.

In general terms you're trying to identify if the issue you are seeing is actually an issue and test your assumptions.

In the more likely scenario that the documentation doesn't exist, hard to find, or have the information you need. Next is to approach the person responsible. I think it's important to coach your wording appropriately. Never make assumptions about the issue you have found. You want to look like you are coming from the position of being wrong or were not able to find the right information. You are now attempting to find the right information. Phrase it something like:

> I was looking at your code and I'm trying to identify if something I'm seeing is actually an issue.

Followed by explaining the issue.

There's no point saying there is a massive security issues because, as mentioned, you put the other person on the defensive, and it may well be that you are wrong. You are reducing your chances that they will pay attention to you in the future, when perhaps there is a genuine issue.

You may discover at this point that they have identified the issue, mitigated it, and the documentation is good, but not something that can be found quickly. At this point you may want to suggest making it easier to find the documentation and your job is done.

However, if they have mitigated the issue but they haven't documented well, or they haven't mitigated it at all then you have some work to do.

This is your opportunity to create some security credit and I recommend you take it. This will make working on issues in future much easier.

The first step is to offer to raise a ticket for the work. This means that it has a greater chance of the issue being worked on. If you're unfamiliar with the project this is also the point to clarify where they record their issues so you know it's somewhere they will see it.

Ideally the next step is to be proactive, although it's not always practical.

If it's a documentation issue then offer to update their documents.

It also may well be a genuine unmitigated issue, and much the same way with the documentation, if you're comfortable you should then be proactive in fixing the problem. Raising a Pull Request for the change and adding or updating tests.

That way the team with the issue are more likely to listen to you and fix the problem next time, which is the ultimate goal: reducing the risk of disruption to your system.
