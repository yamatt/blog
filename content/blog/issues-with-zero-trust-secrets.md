---
title: "The Issues with Zero Trust: Secrets"
date: 2023-03-17T18:10:32+00:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

I wanted to start a series on the issues with Zero Trust. I am a big fan of it and it can be enormously powerful and effective for security. I have built cloud environments before the name came in to being and moving away from that draw-bridge model makes a lot of sense.

But that's not to say that it doesn't have it's issues.

One of those is secrets management.

For a bit of background, secrets are a kind of password that programs use to talk to each other over a network. Their widely used and effective. They work well in zero trust environments where you need a way to enforce authorisation between programs on the internet.

They do however have quite a lot of problems. The main one is that anyone that can get their hands on their secret they can access whatever it has access to, usually too much, and it can be very difficult to know that is happening.

The solution to that is to change secrets regularly, but this is non-trivial and usually involves another secret to do it automatically. There are tools out there that can help such as Akeyless and Doppler, but Ithis is papering over a mâché of problems.

One of which is the superior solution of OIDC. This allows a managed negotiation between the source and destination that reverses the usual flow and allows the destination to select who is able to access it. It means no more secrets, well there are, but not from the standard engineers perspective.

This also does away with the other issue of what happens when a secret gets leaked. As with all step ones in cyber security the first is to panic, but after that changing secrets can be an enormous task. Especially in large or complex environments, which are likely your most vulnerable.

The secondary issue to that is that secrets don't hold much data about themselves, usually. There are efforts to create standards for the format of secrets to try to identify where they come from, which is welcome, until they conflict. We have taken the approach that secrets need meta data that describe the source of a secret as well as the destination. That way you should have some indication when you're in the white heat of a leak incident, where you can claim a new secret.

Secrets are often stored in things like a `.env` files or in environment variables. These are things that are trivial to get at by any malware. Your AWS creds file? It's one miss-click from walking out of your network. Doppler and some tooling for Vault does attempt to solve this by only loading them in when you need them, but this is not a widely used feature.

My final point is a mention on versioning. Secrets are often stored in places that aren't versioned. You update the wrong field and your old secret is gone. Taking production with it. Now you need to go find a copy or request a new one.

Another issue with secrets is that on the server side, they're hard to protect. You could hash them, in the same way we do with passwords, but to hash the secret for every request, potentially 1000s per second is going to be very process intensive, even before any action has taken place.