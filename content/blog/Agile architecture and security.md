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

However, these changes are usually the 'v2' solution and are too expensive to implement now, they are therefore always over the next horizon. The engineering team are then left performing fixes, or adding new features that are more expensive than they should be. That is until someone decides that the 'v2' is less expensive than the next feature they are trying to build.

What I find interesting though is that the stopage looks like the original gate-keeping policies of any legacy IT security delivery, the security architects lament "you should have come to us sooner". This forgets that security is an on-going and continuous process and should be able to take over at any stage of the process.

Because of this I have been exploring the same challenges in architecture, and putting myself in the position that architecture can delivered at any point in a delivery, not just in [green-field environments](https://matt.copperwaite.net/blog/green-brown-teams/). What I found was that while building green-field gives you more flexibility, and feels faster, it can also work well while the project is running too, and in fact can be faster.

The benefits that have already been discussed is not having to stop and work on just on the architecture. This can often turn your project in to something that cannot be run in parallel because any new features might be replaced later. This means leaving one of your team doing the architecture work, while the others work on something else.

If however you make incremental steps, such as building a JSON Schema, OpenAPI or gRPC spec in one sprint and adding that to your code in another sprint, you're able to start on your journey. Other ways you can treat this is by starting to make your code idempotent, or your images mutable. This starts you on your journey to making your system repeatable and in-fact easier to switch to other technologies.

In fact generally moving towards standards is a great way of improving your architecture and your collaboration.

Other ways can be to do small bits of refactoring, or breaking out your code in to modules as part of other peices of work. I recently worked on a piece of code where logging was non-existent. So as part of that change I also spent a bit of additional effort getting the code closer to something that was more pythonic. It was necessary for the logging to be effective. I didn't refactor the entire codebase, which would take time and either involve a lot of rebasing or stopping other people on the team working on the code entirely, I did just enough that necessary to improve the logging. At a later stage I or someone else would revisit the code and do the same.
