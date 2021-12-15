---
title: "The Maintenance Cost of Security Controls"
date: 2021-12-15T13:35:32+01:00
slug: ""
description: "The impact of controls"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I used to work with a security architect who thought that every risk should be mitigated by use of "IP [white-lists](https://www.ncsc.gov.uk/blog-post/terminology-its-not-black-and-white)" for limiting user authentication.

There are some immediate concerns with that approach. The poor user experience, and the speed in which it can be over-come the, but one of the other concerns, that I often don't see discussed, is the support impact of such a control.

Firstly let's assume that the user realises the reason that a service has been unavailable for hours, or days, is because their IP has changed. They will then have to find a way to request help outside those to get their new IP added to the allow list.

Even with a single user this could be a big over-head. If they were using something like a 4G dongle for their internet connection, which changes IP addresses regularly, they could be making several changes a week. That is an extreme example, but multiply that by even a modest number of users and your support teams quickly become overwhelmed. You could create some sort of self-service, but then why have the control at all? All it does is create bureaucracy.

This post isn't entirely about bashing IP allow-lists, although it demonstrates the issues effectively.

Another example is using [AWS's Customer Managed Keys for KMS](https://docs.aws.amazon.com/whitepapers/latest/kms-best-practices/aws-managed-and-customer-managed-cmks.html). By using CMK you now have to manage your own encryption keys. You have to create an entire ecosystem for managing those keys, ensure they're protected, rotated, and safely removed. That has the additional effort that you are not putting in to delivery, as well as the additional security risk associated with getting every step right.

Any control proposed to mitigate a risk needs to be adequately weighed up and the impact and implications of that control, because each control has it's own risks, the secondary effects on how to effectively manage that control, and everything that comes with it.

<!--alex ignore knife fight -->
With IP allow-listing there is an interesting asymmetry between the risk and the control. The control is vastly more impactful than the thing you're trying to protect against. To mix metaphors it's like bringing a barn-door to a knife fight. You have to be careful that each control chosen is measured against the risk, rather than taken at face value.
