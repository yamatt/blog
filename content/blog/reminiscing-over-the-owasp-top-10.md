---
title: "Reminiscing over the OWASP Top 10"
date: 2022-10-17T18:10:32+00:00
slug: ""
description: "Things were better in my day"
keywords: []
draft: false
tags: []
math: false
toc: false
---

<!--alex disable failure-->
<!--alex disable failures-->

I was having a discussion with some freinds recently where we found that we were in agreement about how [much less useful the OWASP Top 10 list is since the updates](https://web.archive.org/web/20221008005542/https://owasp.org/Top10/). I found that no one had written anything that was critical of the 2021 changes.

Before the 2021 change I would use the OWASP Top 10 as a checklist for when engineers wanted to know how to improve the security of their web services.

Understandably the delivery of web services has changed significantly since the last time the Top 10 was run in 2017. But those changes don't apply to everyone.

It's good that OWASP are looking to include more of the delivery pipeline. But this means when I direct an engineer to it they're provided confusing wording and subjects that could be outside of their responsibility, making engineers looking to cover the basics no-longer able to find the information they need.

Here are the changes I find interesting:

* A02:2021-Cryptographic Failures: This one used to be about data leaks. This is now somehow, about cryptographic failure, crypto, sounds like, if not about Bitcoin, then about encryption. Would gaining access to a public file in S3 that contains sensitive data count as a cryptographic failure?
* A04:2021-Insecure Design: This one talks about "move left" with [scare quotes](https://en.wikipedia.org/wiki/Scare_quotes) like it's a fad. Insecure Design sounds to me like an upfront task, before any engineer has a look-in.
* A05:2021-Security Misconfiguration: Security Misconfiguration is pretty much the entire list isn't it?
* A09:2021-Security Logging and Monitoring Failures: Is it a failure? Or does it not exist?
* Also _A06:2021-Vulnerable and Outdated Components_ and _A08:2021-Software and Data Integrity Failures_ are too closely related.

The changes and the reasoning for them is not well explained on the Top 10 page itself. If I was looking for advice on how to to secure pipeline I would not automatically think of OWASP. Instead I think I will still use the [2017 reference for in most situations](https://web.archive.org/web/20210820092716/https://owasp.org/www-project-top-ten/).
