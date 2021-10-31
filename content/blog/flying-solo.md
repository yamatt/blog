---
title: "Flying Solo"
date: 2020-11-21T18:10:32+01:00
slug: ""
description: "Working securely when working in isolation"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I'm currently working on a project where I am the lead and only engineer doing full time delivery. I find this a really weird state to be in, to me if something is worth doing it's worth putting the necessary support framework in.

You often hear of [BOFH](https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell) trope where an engineer, typically in a Sys Admin like role is the that is the master of all they survey, calling people idiots for forgetting their passwords, creating brittle systems that mean they can't even go on holiday without something breaking, and ensuring their job security for life by retaining all knowledge about the environment in their head.

I don't consider myself a BOFH, and my intention is to ensure that when others do make it on to their project that they have as smooth of a transition as I can reasonably make it. My approach to this isn't the focus of this post, the short of it is about prioritising code quality, automation, and documentation as much as delivery.

However when working in isolation there are so many assumptions you make, as well as rubber-ducking activity that you only really notice when you voice them with others.

https://twitter.com/SwiftOnSecurity/status/1385022532655280129

Attempting to be a good corporate citizen I wanted to raise the risk of working in isolation on such systems, but found it difficult to articulate the impact of not being able to identify assumptions. However, despite the BOFH trope there doesn't seem to be much written up, at least that I could find, on ways of identifying your assumptions for documentation, and basically, how to remain sane. And by remain sane I mean not get frustrated by your users constantly locking themselves out, or e-mailing all your financial details to a phisher.

Perhaps part of the answer is automation. Perhaps if you build tools that allow users to help themselves such as a self-service password reset tool, and providing MFA options they start to ask more interesting questions that represent their real needs.

Of course this requires you to have the space to provide self service tools. Sadly automation is more time intensive than doing something once (obviously). Or having the fortiude to ask to dedicate more time to automation.
