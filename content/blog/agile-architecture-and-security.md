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

I should point out that while my background is in Cyber security, I have a passion for systems architecture. I also believe that they compliment each other. That good, well reasoned and mature architecture creates an environment where IT security becomes the default, rather than an afterthought. Unfortunately in environments running Agile practices, architecture is often only considered once the current way the system evolves becomes part of the problem, rather than up-front where it can be the help most.

That's why I was excited to see the [Agile meets Architecture](https://www.agile-meets-architecture.com/) conference happening in Berlin at the beginning of next month.

If it wasn't for having a young family, making spending several days in another country unrealistic for me, I would absolutely be throwing everything at getting myself there. It looks like a really exciting conference to happen and I hope everyone who attends gets a lot out of it.

Despite me not being able to attend, it has made me think about the problem of architecture and security in agile contexts.

There are some separation of concerns at a business level that I've seen a few times now, usually as a DevX team that usually provides things like SEIM integration and ingress detection in addition to the cloud [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). But beyond that, systems architecture is left to the individual engineering teams to decide, until they eventually discover how important good up-front architecture could have helped them.

My team are going through this realisation now, where several systems which were built by the previous incarnation of the team have bits that have not stood even the short amount of time they were in use.

The response to that, including my own, has been that we needed to step away from the every day bug fixing and feature implementation and dedicate some time to better understanding the problem we are trying to solve. A focus on technical debt specific to architecture. However this take the development teams away from their day jobs, and make them work on activity that is difficult to run in parallel. Instead leaving engineering team performing fixes, or adding new features that are more difficult, and time consuming than they should be.

That is until someone decides that the architectural changes are less expensive than building the next feature

What I find interesting though is that taking time away to focus on architectural technical debt looks like the legacy gate-keeping policies of last generation IT security delivery, reminding me of the security architects lament "you should have come to us sooner". This overlooks that architecture, much like security, is an on-going and continuous process and should be treated as something that can take over at any stage of the delivery.

This doesn't mean you don't have to do architecture up-front, but instead building with tooling that makes architectural changes easier.

What this means for you depends on your circumstances. Perhaps you have built and are having to maintain a common pattern, such as authentication, or Kubernetes that could be handed off to a specialist team. Or perhaps it means that you should create some OpenAPI and JSON Schema standards for your interactions.

But whatever it means for you, it means moving away from thinking of architecture as unchanging, and try thinking about how you might take steps to get to your better state.
