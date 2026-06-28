---
title: "Checklists"
date: 2022-04-14T18:10:32+01:00
slug: ""
description: "Who watches the watchers"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I had originally starting writing an article titled "Embrace the chaos". In it I was bemoaning strong controls that enforce a way of working that is inherently going to break once something changes, and encouraging people to develop more dynamic approaches. However in researching the subject my view softened a little on it and I no-longer am certain about it's premise.

Those changes in my view stem from a couple of areas:

* [On The Metal podcast featuring Star Simpson](https://oxide.computer/podcasts/star-simpson) in this episode who talked about the virtues of checklists in autonomous flight
* Similarly [preflight checklists](https://en.wikipedia.org/wiki/Preflight_checklist).
* A recent [Cautionary Tales podcast episode](https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vY2F1dGlvbmFyeXRhbGVz/episode/ZmIzNzIyYjYtYTE0Ni0xMWVjLTgyMTUtYzc1MGU2NjVjOGM4?sa=X&ved=0CAUQkfYCahcKEwiIy8LUyZP3AhUAAAAAHQAAAAAQAQ) about architects using checklists.
<!--alex ignore dive-->
* A conversation with a colleague about Scuba Diving and [Dive Planning](https://en.wikipedia.org/wiki/Dive_planning) and the checks that they do.

I also realised that we use checklists in DevOps, or as most people practising DevOps would call them, a test suite. I have checklists in the deployment pipeline for this blog in the form of a several tests that look for [insensitive words](https://alexjs.com/), [ensuring sentences make sense](https://github.com/yamatt/python3-hemoglobin), that [the language I use isn't too complex](https://github.com/yamatt/python3-textstat-cli), and a small set of bash scripts that check that when I hit the merge button there is a chance it will actually be published.

A CI pipeline and the examples above differ in one significant way however, and that is that they have differing levels of risk. Flying vehicles, constructing a building, and scuba diving have a higher likelihood of loss of life than software engineering, in general. And I hope in the situations where it doesn't you are using a technique that is less about embracing failure.

There are definitely things to take-away from both sides though. Those checklists for flight vehicles aren't designed one day by thinking about the problem hard. They are built from the study of cases of where things have gone wrong. Either directly specifically for that plane, or for planes in general. One site I enjoy perusing when I'm _really_ bored is [The Aviation Herald](https://avherald.com/h?list=&opt=3840) and in that you can filter for reports, which is the post-mortem of incidents in flights.

<!--alex ignore attacks-->
In DevOps and especially in SRE we have to [study the instances of downtime](https://www.atlassian.com/incident-management/postmortem) to see what we can learn from it. If you're building something new, groups like OWASP give you [indicators of common ways things can go wrong](https://owasp.org/Top10/). [Snyk, Dependabot and similar](https://alternativeto.net/software/snyk/) provide information about another common risk, supply chain attacks.

Unfortunately there is no one checklist suite that can work for all software. In the same way a checklist for one type of plane won't work for another. A checklist for a Jumbo Jet will look very different from a Concorde. But they may well share some similarities.

To be better we need to find our opportunities to improve.
