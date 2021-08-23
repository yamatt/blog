---
title: "ZeroTrust: Web by Default"
date: 2021-08-23T18:10:32+01:00
slug: ""
description: "Web All The Things - Like Spiderman"
keywords: []
draft: true
tags: []
math: false
toc: false
---

While people still try to work out what ZeroTrust means for them, one of the guiding principles that I created and found useful when working on building ZeroTrust systems previously is _Web by Default_.

When moving to ZeroTrust from large enterprise IT with a bunch of legacy systems you often have that one weird, bespoke tool, that hasn't yet reached the modern era and exists only as thick-client install. Then it communicates to a back-end server via a weird unsecured protocol.

Some people call this system electronic mail.

I jest. E-mail is actually not too difficult and there are a lot of web-mail alternatives such as M365 and GMail to name the big players. It should be the first thing you solve.

But I'm sure there are weird, often CRM, systems, that your initial reaction is to backhaul the data over a VPN. But the Web by Default principle meant that VPN is never the answer.

The real solution to that problem is services like Amazon Workspaces, Azure Virtual Desktop, Amazon AppStream 2.0.

When done right these tools have huge security gains. You can _Desktop as Code_ the infrastructure so that they always patched. They take installing random software away from the EUDs, and you can put the back-end server in a secure network that can only be reached by the front-end tool.

Often there exists concern that these systems are slow, but in our experimentation we actually found these tools to be faster than running it locally because you can bump up the RAM and CPU more than you can on a laptop, and you are only run it when the users are using it, which saves money.
