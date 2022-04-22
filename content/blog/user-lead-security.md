---
title: "User Lead Security"
date: 2022-04-22T18:10:32+01:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

I was speaking to a friend recently who works for a company that supplies a widely used piece of software. They also provide, for a fee, a product, on top of their main product, that increased security by encrypting data. The data is in AWS and is encrypted anyway, this additional tool worked at the read-write layer to add extra assurance.

The who was buying this software was one I was familiar with, and both he and I knew that they didn't need this software. We had both separately consulted with (different) experts in the field who also agreed that they would not need this kind of software.

The trouble was the company wanted it anyway.

The problem is, how do you know if a piece of additional security is worth it or not. You can do your risk analysis which says, yes, this will reduce your likelyhood and impact. But let's be frank here, the risk matrix is based on numbers that are picked out of the air. They're individual to each company, their threats and their risk appetite, as well as how big of a problem they think they have.

If you have a company that didn't realise it was a threat to a nation state attack, they might consider a XSS vulnerability a big issue, and not monitor their real problem areas.

The other issues with risk matrix is that it contains a unit of probability, this means it gives you no information about the cost impact of a singular risk because something that is unlikely can still happen, and something that is very likely may never happen. Especially if you're in the context of a defence in depth system.

The concept I have been evolving over the years is User Lead Security. This is about understanding their users and their needs, and this actually fixes a lot of the problems outlined above.

First off, what is User Lead Security. It borrows a lot of concepts such as User Lead Design and User Experience. It is about putting users first. Properly capturing their needs and desires and having that determine your security controls.

From this perspective it seems completely insane how security is placed above users needs. Security is supposed to be about enabling users, as anyone working in security for 30 years without having once spoken to a user, will tell you.

For me any control must be backed up by an evidenced conversation with a user as to why they need it.
