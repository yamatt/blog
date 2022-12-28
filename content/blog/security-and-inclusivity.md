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

One of the Cyber Security decisions that really bugs me is the way we typically expire accounts after a period of inactivity. It comes about because the joiners, movers, leavers (JML) process in businesses tends to be hard. Particularly with leavers when line managers get busy and don't fill in or submit the right forms to report leavers. Even when they do this goes to your HR department and may not trigger anything in the IT department. Therefore the thinking goes that accounts may exist long after someone has left. The risk to the business therefore that either someone may have flounced out of the business because they're unhappy for some reason and either let, or sell their account details to a nefarious person. Or it means there are many unused accounts, potentially with weak passwords, that anyone could gain access to, depend upon, you know, you always log in to the database with Barry's account even though he left more than 10 years ago.

And it's a hard problem to solve if you don't have SSO or people are working around SSO.

But the best solution is to fix the underlying problems. Make sure IT is included in the hand-off process. Have reliable and robust processes for when people leave. 

However IT Ops people often take it upon themselves to fix these problems themselves. They'll implement password expiry, they'll disable accounts that haven't been used for a while.

But these have inclusivity effects. For example, someone may take time off work, for any reason, but common examples are maternity, or stress. Once they're back working, they're excited but nurvous about their first day. They'll try to login to find that their account is locked out.

Imagine how this may feel for that person. Having to go through a support number, prove their identity, and get their account unlocked. Does that represent your business? *Should* that represent your business?

This example is not the only one. Historically, before we called it Cyber Security, we would block quotes from form fields, or dashes. This was because of poorly coded database queries that could be used for SQL Injection. Ignoring the fact that many people have those characters in their names.

Or more recently, geo blocking. Assuming that an IP equates to a location and saying we ban people from those countries. But does, or could your business operate in those countries? Are you going to end up blocking legitimate employees?
