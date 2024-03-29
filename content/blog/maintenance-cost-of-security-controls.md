---
title: "The Maintenance Cost of Security Controls"
date: 2021-12-16T13:00:32+01:00
slug: ""
description: "The impact of controls"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I used to work with a security architect who thought that every risk can be mitigated by use of "IP [white-lists](https://www.ncsc.gov.uk/blog-post/terminology-its-not-black-and-white)".

There are some immediate concerns with that approach in many scenarios. In most cases the poor user experience, and the ease in which it can be over-come. But one of the other concerns, that I often don't see discussed, is the support impact of such a control.

Firstly let's assume that this is to limit user authentication. The user has to realise the reason that a service has been unavailable for hours, or days, is because their IP has changed. They will then have to find a way to request help through a different path.

Even with a single user this could be a big over-head, requesting help several times a year. If they were using something like a 4G dongle for their internet connection, which changes IP addresses frequently, they could be requesting help several times a week. That is an extreme example, but multiply that by even a modest number of users and your support teams become overwhelmed. You could create some sort of self-service, but then why have the control at all? All it does is create bureaucracy.

This post isn't entirely about bashing IP allow-lists, although it demonstrates the issues effectively.

Another example is using [AWS's Customer Managed Keys for KMS](https://docs.aws.amazon.com/whitepapers/latest/kms-best-practices/aws-managed-and-customer-managed-cmks.html). By using CMK you may have mitigated whatever concern you thought you had, but you now have to manage your own encryption keys. You have to create an entire ecosystem for managing those keys, ensure they're protected, rotated, and retired securely. That has the additional effort that you are now not putting in to delivering value to your users, as well as the additional security risk associated with getting every step right.

Any control proposed to mitigate a risk needs to be adequately weighed up and the impact and implications of that control has its own risks. You have to consider the secondary effects on how to effectively manage that control, and everything that comes with it.

<!--alex ignore knife fight -->
With IP allow-listing there is an interesting asymmetry between the risk and the control. The control is vastly more impactful than the thing you're trying to protect against. To mix metaphors it's like bringing a barn-door to a knife fight. You have to be careful that each control chosen is measured against the risk, rather than taken at face value.
