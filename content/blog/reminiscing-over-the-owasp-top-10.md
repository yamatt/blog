---
title: "Reminiscing over the OWASP Top 10"
date: 2022-10-13T18:10:32+00:00
slug: ""
description: "Things were better in my day"
keywords: []
draft: true
tags: []
math: false
toc: false
---

<!--alex disable failure-->

I was having a discussion last night some friends who were mostly in agreement about how [much less useful the OWASP Top 10 list is now](https://web.archive.org/web/20221008005542/https://owasp.org/Top10/), and we realised I couldn't find anything anyone had written who was critical of them.

I should point out that I do understand where the changes have come from, I don't think they have been well explained on the Top 10 page itself as to why the changes were made. To me, the list is dynamic, that's why it's a Top 10, and it has to change over time. However I think they missed out one consideration, the audience. The changes themselves make sense in that it is covering what is the most common from a security perspective, but I used to use the Top 10 as a reference when having a discussion with engineers about what things they should be considering when looking at improving the security of their services. Now, when I look at the list with my engineering hat on, some of the language is difficult, and the areas they cover wouldn't be my responsibility.

Lets enumerate the noteworthy changes:

* A02:2021-Cryptographic Failures: This one mostly covers data leaks. Cryptographic failure, crypto, sounds like, if not about Bitcoin, then about encryption. Would gaining access to a public file in S3 that contains sensitive data count as a cryptographic failure?
* A04:2021-Insecure Design: This one talks about "move left" with [scare quotes](https://en.wikipedia.org/wiki/Scare_quotes) like it's a fad. Insecure Design sounds to me like an upfront task, before any engineer has a look-in, right leaning.
* A05:2021-Security Misconfiguration: Security Misconfiguration is pretty much the entire list isn't it?
* A09:2021-Security Logging and Monitoring Failures: Is it a failure? Or does it not exist?
* Also have a read of _A06:2021-Vulnerable and Outdated Components_ and _A08:2021-Software and Data Integrity Failures_ work out how they differ.

I think my expectations were wrong. What I'm looking for is guidance for engineers on how to secure their web apps in 2022 that are the minimum things that we should look for. Taking that as the case, let's fix that.

First off I'm going to be [referencing the least old version of the Top 10](https://web.archive.org/web/20210820092716/https://owasp.org/www-project-top-ten/) that I agree with the naming, and using that as a basis of things to check for when building a web app. I'm also going to be taking some from the new list because it's not all bad.

## The List
This list is a list of things that an engineer should check is handled. Most of these won't be a problem if you have a good PaaS architecture, and are using modern web framework, but it's always useful to have a checklist as reference.

These are presented in no order as I do not have the clout of OWASP to identify how common these are, but I know these are still common based on my experience of managing a HackerOne programme.

* [A1:2017-Injection](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection)
* [A2:2017-Broken Authentication](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
* [A3:2017-Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure)
* [A7:2017-Cross-Site Scripting XSS](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS))
* [A8:2017-Insecure Deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)
* [A10:2017-Insufficient Logging & Monitoring](https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring)
* [A06:2021-Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

