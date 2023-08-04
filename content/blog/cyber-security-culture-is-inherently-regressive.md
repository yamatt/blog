---
title: "Cyber Security Culture Is Inherently Regressive"
date: 2023-03-17T18:10:32+00:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---


Cyber Security culture is inherently regressive. What do I mean by that? What do I mean by regressive?

[Regressive policies are in the news in the UK at the moment](https://www.bbc.co.uk/news/business-66268073). If you [look up a definition of regressive](https://dictionary.cambridge.org/dictionary/english/regressive) it tends to be defined by way of example and referring to tax. But for me it's a form of control, that is designed to make changes in a group through negative effects, rather than positive effects.

In tax terms regressive policy is used discourage a particular activity, such as discouraging eating foods with high fat or sugar content by making those foods more expensive.

I see this technique used in Cyber Security a lot. Don't want your users visiting websites with suspicious content? Put in a firewall that blocks those sites. A widely used example of this is not being able to block pirate websites, or sites that are new. Or perhaps put in an _allow-list_ of approved sites that users can have access to.

But this will have a [maintainance cost](./maintenance-cost-of-security-controls.md) to the business. Not just in terms of keeping that list up to date, but those lists inexactly repesenting each user and the opportunity cost to the business when users are inadvertently caught in the list and are blocked from doing their work.

I believe this true for all regressive Cyber Security policies. Where users are prevented from doing bad things and costing the business to have to work around them.

The opposite to a regressive approach is a _progressive_ approach. In tax terms this means making fruit and vegtables cheaper, so people are encouraged to buy them.

In Cyber Security terms this doesn't exactly mean make Google better, rather I believe it means alerting over blocking, and not assuming a user is trying to do a bad thing.

Lets go back to the example where you have an alert for a user visiting a website used for pirated material. Let us first check that the user is expecting that activity to have happened on their machine. Maybe they did it by accident. Maybe they let their laptop to their child. Maybe it's some malware. There are so many other reasons it could be something other than what it looks like on the surface.

A place to look to fix these things is the Acceptable Use Policy. I've seen many that say to the effect "Don't do bad things on this computer". But let's think about it. Would a user necesserily know they've done a bad thing? Surely that's our job to detect that activity. My Acceptable Use Policy would say "If you see something happen that shouldn't, you have to tell us". There is no pressure on a typical user to report something if they don't see it as strange, but a more experienced user is informed of their duty to report anything suspicious.
