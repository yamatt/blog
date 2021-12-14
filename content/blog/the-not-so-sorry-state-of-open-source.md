---
title: "The Not So Sorry State Of Open Source"
date: 2021-12-14T10:30:32+01:00
slug: ""
description: ""
keywords: []
draft: false
tags: []
math: false
toc: false
---

I've seen recent discussions bemoaning the state of Open Source software. This seems likely to me to have been brought on by questions about their security and integrity in light of recent concerns about supply chain exploits.

I will declare myself now, I am not a fan of Java. In my personal ranking of programming languages I hate, Java is there right below PHP. I will admit with the log4j issues over the weekend I have been quietly smirking to myself a bit. Although it goes without saying, #hugops to those who have had their weekends ruined.

However, I do recognise that ranking them comes from my personal biases and is not backed up by any data. It does not [make the Java (or PHP) ecosystem insecure](./assessing-security-practices-of-3rd-party-projects).

I'm sure this also applies to those with concerns about the security of Open Source software. Lashing out with whatever their personal biases tell them without any considered reasoning. It makes me think of the SystemD arguments that are still around today.

Given the broad use and severity of the log4j issues, what does actually concern me is environments that are difficult to update. I do recognise that we are in a time of transition right now. A lot of software is still manually deployed, if the engineers who built it are still working for the company. And even the ones that are automatically deployed may not fully understand the tooling within them. I'm sure much like Heartbleed the fixes will be gradual rather than big bang.

Open Source software, Java, PHP, whatever needs tooling that allows it to be patched quickly, reliably and effectively. I would hypothesise that those who are letting their personal biases lead them to conclusions about whatever technology they hate are actually victims of ineffective tooling.

Hopefully this will be another opportunity for businesses to have the discussion "what can we do to prevent this from happening again?" and do some fish-bone analysis rather than listening to the loudest person in the room then being surprised when we run in to the same issues again.
