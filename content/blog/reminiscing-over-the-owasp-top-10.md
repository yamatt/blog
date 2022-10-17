---
title: "Reminiscing over the OWASP Top 10"
date: 2022-10-17T18:10:32+00:00
slug: ""
description: "Things were better in my day"
keywords: []
draft: true
tags: []
math: false
toc: false
---

<!--alex disable failure-->
<!--alex disable failures-->

I was having a discussion with some freinds recently and we realised we were in agreement about how [much less useful the OWASP Top 10 list is now](https://web.archive.org/web/20221008005542/https://owasp.org/Top10/), and I discovered there was nothing anyone had written that was critical of the 2021 changes.

Before the 2021 change the OWASP Top 10 used to be the reference point when engineers were considering how to protect their web services. Now when I direct an engineer to it they're provided confusing wording and subjects that are out of their expected scope.

The issue is that the building of web services has changed since the last Top 10 in 2017, it's understandable to encompas more of the build environment. It means that engineers looking to cover the basics of how to secure web services do have to consider more, and it's admirable that OWASP want to encourage securing of pipelines and better archiecture. The trouble is that this list has a vast audience, and some of the list might not be the engineers responsibility, which causes friction and makes consuming the list more difficult.

Here are the changes I find interesting:

* A02:2021-Cryptographic Failures: This one used to be about data leaks. This is now somehow, about cryptographic failure, crypto, sounds like, if not about Bitcoin, then about encryption. Would gaining access to a public file in S3 that contains sensitive data count as a cryptographic failure?
* A04:2021-Insecure Design: This one talks about "move left" with [scare quotes](https://en.wikipedia.org/wiki/Scare_quotes) like it's a fad. Insecure Design sounds to me like an upfront task, before any engineer has a look-in.
* A05:2021-Security Misconfiguration: Security Misconfiguration is pretty much the entire list isn't it?
* A09:2021-Security Logging and Monitoring Failures: Is it a failure? Or does it not exist?
* Also _A06:2021-Vulnerable and Outdated Components_ and _A08:2021-Software and Data Integrity Failures_ are too closely related.

The changes and the reasoning for them is not well explained on the Top 10 page itself. If I was looking for advice on how to to secure pipeline I would not refer to OWASP. I think I will still use the [2017 reference for most conversations](https://web.archive.org/web/20210820092716/https://owasp.org/www-project-top-ten/).
