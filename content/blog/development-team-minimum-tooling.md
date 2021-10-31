---
title: "Development Team Minimum Tooling"
date: 2020-11-21T18:10:32+01:00
slug: ""
description: "A list of tooling any development team needs"
keywords: []
draft: true
tags: []
math: false
toc: false
---

Since I've been working with a new development team lately on a green field project, I've been thinking about the tooling developers need as a minimum to get working effectively.

I'm sure there is a lot debate on this, and may depend on your experiences, but I think it's worth starting to build a common compendium, because first it saves discussion, and two gets your teams working faster.

The reason I think these tools need to be in place is because sooner or later your development teams will need them, and if they don't have them, or can't find them, they will end up building and maintaining them themselves, which is additional effort that is put in to that rather than providing a better service to their users. This means these tools should be provided by a centralised team that is providing these services to one or more development teams.

## Centralised Version Control
As a utter lowest common tooling you need, you need a place for your development teams to collaborate on code. I've known teams who (not even that long ago) worked on code in a shared directory, which seems very scary to me. Not to be biased towards any particular tools (although do start with GitLab or GitHub if you're not doing this already), but you need a way for code to be version controlled, for code to not be over-written or lost accidentally.

## Deployment Platform

Be it a cloud provider, a bunch of servers in a data centre, or a Raspberry Pi under a desk,

## CI/CD

## Knowledge Base

Usually a Wiki

## Development Devices

A computer that has considerable administrative controls for developers. This is because first, we know developers are expensive resources, if you impede their development that is a lot of money being washed down the drain. Second, a locked down environment for a developer is different to a locked down environment for a standard user. Mainly because a developer will see it as a challenge to over-come. Third, your security controls will likely make your developer have to do things that actually lower security, such as automating password entry.

The easiest thing to do is to give developers full access to their devices. There is often concern that developers have significant control over an environment and full access to your data. However there is a big difference between a developer and a systems administrator, and that should be clear from the outset. In a well architected environment developers should not have access to production, and any administrative level access is strongly monitored with automated alerting.
