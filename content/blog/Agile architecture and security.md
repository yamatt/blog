---
title: "Agile Architecture And What It Means For Security"
date: 2022-08-15T18:10:32+00:00
slug: ""
description: "Adaptive architecture for better security"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I should point out that while my background is in Cyber security, I have a passion for systems architecture. I also believe they compliment each other. I believe that good, well reasoned and mature architecture creates an environment where IT security becomes the default, rather than an afterthought. Unfortunately architecture seems to often be considered part way in to a project, rather than up-front where it can be the most help.

That's why I was exciuted to see the [Agile meets Architecture](https://www.agile-meets-architecture.com/) conference happening in Berlin at the beginning of next month.

If it wasn't for having a young family making spending several days in another country unrealistic for me, I would absolutely be throwing everything at getting myself there. It looks like a really exciting conference to happen and I hope everyone who attends gets a lot out of it.

Despite me not being able to attend, it has made me think about the problem of architecture and security in agile projects.

There are some neat separation of concerns at a business level that I've seen a few times now. Usually there is a DevX, Cloud Enablement team that provide some additional support to engineers, over and above the usual [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), such as providing guardrails and local business best practices. This usually looks like automatically turning on monitoring in to the SEIM and detecting suspicious open ports within the engineering team's boundary.

But systems architecture is left to the engineering teams to decide, and everyone, eventually, discovers how important architecture is.

My team are going through this realisation now, where several systems which were built by the previous incumbents, have some well architected bits and some bits that have not stood even the short amount of time they were in use.

The response to that, including my own, has been that we needed to step away from the every day bug fixing and feature implementation and dedicate some time to better understanding the problem we are trying to solve.

These changes are considered the 'v2' solution and are always over the next horizon. The engineering team are then left performing fixes, or adding new features that are more expensive than they should be. That is until someone decides that the 'v2' is less expensive than the next feature they are trying to build.

What I find interesting though is that the stopage looks like the original gate-keeping policies of any legacy IT security delivery, the security architects lament "you should have come to us sooner". This forgets that security is an on-going and continuous process and should be able to take over at any stage of the process.

Because of this I have been exploring the same challenges in architecture, and putting myself in the position that architecture can delivered at any point in a delivery, not just in [green-field environments](https://matt.copperwaite.net/blog/green-brown-teams/). What I found was that while building green-field gives you more flexibility, and feels faster, it can also work well while the project is running too, and in fact has several benefits.
