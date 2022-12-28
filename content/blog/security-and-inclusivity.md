---
title: "Safety and Inclusivity"
date: 2022-12-28T18:10:32+00:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

I was recently putting together a talk about myths that existing within and from outside of Cyber Securtiy for an internal work conference. A trend popped out at me while writing it, that showed how poor security recommendations can often impact the culture of your business and in particular impacts inclusivity.

There were a few examples that I put in to the presentation, but I'm going to focus on one here to demonstrate it in more detail.

One of the common Cyber Security decisions that really bugs me is the way accounts expire after not being used for some time. It comes about because getting the leavers process in businesses tends to be difficult. Line managers will get busy when someone leaves and don't fill in or submit the right forms to report a leaver. Even when they do this goes to your HR department and may not trigger anything in the IT, or perhaps it's manual and gets overlooked. This leads to the account existing long after that person has left.

This has several risks to the business. The most likely one is that there ends up being many unused accounts, that anyone could gain access to or even depend upon. It could also mean that someone may have flounced out of the business because they're unhappy for some reason and either let, or sell their account details to a nefarious person.

The best solution is to fix the underlying problems, but in my experience IT often take matters in to their own hands and tweak the things they have buttons to control, such as implementing password expiry, and disabling accounts that haven't been used for a while. But these buttons have inclusivity impacts.

<!--alex ignore maternity-paternity-->
For example, someone may take time off work, such as maternity, or stress. Once they're back working, they're excited but nervous about their first day. They'll try to login to find that their account is locked out.

Imagine how this may feel for that person. Having to go through a support number, prove their identity, and get their account unlocked. Does that represent your business? *Should* that represent your business?

This example is not the only one.

Historically, before such things we even called it Cyber Security, we would prevent quotes or dashes from being used in form fields. This was usually because of poorly coded database queries that could be used for SQL Injection. Ignoring the fact that many people have those characters in their names.

Or in more recent controls, geo blocking. Assuming that an IP equates to a location and saying we ban people from those countries. But does, or could your business operate in those countries? Those databases are not entirely accurate. Especially if they're not updated often. Are you going to end up blocking legitimate employees? Are those who are going to use your service going to use a VPN anyway? What happens if that block also prevents them from being unblocked?

<!--alex ignore obvious-->
When presented with a risk, the mitigation often seems obvious. But it takes time and research to identify the impact of it. Without that work you can lead to unintended concequences.

The true responsibility of Cyber Security is to ensure that security controls are reasonable, equitable, and justified.
