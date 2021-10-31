---
title: "Questioning Defence in Depth"
date: 2020-11-20T18:10:32+01:00
slug: ""
description: "Security Grenades"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I'm starting to consider the value of defence in depth. This, on the face of it, is a really good principle and term that I use quite often.

However, my concern is that by itself doesn't account for the user context. For example, if a user needs to access Dropbox it might be blocked by an administrator. Breaking down the reason it is blocked you discover that it's a common way of attackers sharing binaries that could aid in them affecting your system.

However you have several other layers of protections such as virus scanning, and network isolation. However defence in depth ignores the user need and says block it anyway, and therefore also has an impact on improving security.
