---
title: "The Maintenance Cost of Security Controls"
date: 2021-11-22T13:35:32+01:00
slug: ""
description: "The impact of controls"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I used to work with a security architect who thought that every risk could be solved by IP white-lists.

Along with the poor user experience, the speed in which you can over-come the control, especially a properly motivated actor, one of my other concerns that I often don't see discussed is the maintenance impact of such a control.

Firstly lets assume that the user realises the reason that a service has been unavailable for hours, or days, is because their IP has changed, you then have to find a second path outside those controls to request that your IP is added to the allow list.

Even with a single user this could be massive over-head if they were using something like a 4G dongle for their internet connection. Multiply that by even a modest number of users and it has a huge maintenance impact. If you created some sort of self service, then why have the request at all?

This post isn't exclusively about bashing IP white-lists, although they are certainly they demonstrate the issues most clearly.

Another example is using [AWS's Customer Managed Keys for KMS](https://docs.aws.amazon.com/whitepapers/latest/kms-best-practices/aws-managed-and-customer-managed-cmks.html). By using CMK you now have to manage your own encryption keys. You have to create an entire ecosystem for managing those keys, ensure they're protected, rotated, safely removed. That has a personnel cost, as well as the additional security risk associated with it.

Any control proposed to mitigate a risk needs to be adequately weighed up and the impact and implications of that control need to be measured against user experience. However, there is also the secondary effects on how to effectively manage that control, and everything that comes with it.

With IP white-listing there is an interesting asymmetry between the risk and the control. The control is vastly more impactful than the thing you're trying to protect against. To mix metaphors it's like bringing a barn-door to a knife fight.
