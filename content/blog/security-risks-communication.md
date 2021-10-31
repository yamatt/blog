---
title: "Communicating Security Risks as part of the Sprint"
date: 2021-07-15T18:10:32+01:00
slug: ""
description: "You need to identify your highest priority risks"
keywords: []
draft: true
tags: []
math: false
toc: false
---

One of the things that has to be kept in mind when delivering a service is communicating risks. As engineers we should be doing this anyway, from telling your team when you're going to a dentist appointment and you won't be available for the morning, to making huge architectural decisions about two or more potential solutions that both have risk.

If it's a big risk stemming from an architectural decision this is the perfect place for an [Architecture Decision Record](https://adr.github.io/). Anyway, this makes an official note of the architectural change, but it doesn't work the same for security considerations.

The scenario I've come across is that to deliver value quickly my team deliberately delivered a less secure version of the service. There were other things we could do to improve the security posture, however we were attempting to solve the stories for the sprint. Therefore we have some technical debt and potential security weaknesses that hadn't been addressed.

We did what we normally do in this situation and recorded them as tickets. This records the risk in the form of a clean-up activity, but doesn't communicate the risk.
