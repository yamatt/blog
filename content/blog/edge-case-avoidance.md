---
title: "Edge Case Avoidance"
date: 2020-11-21T18:10:32+01:00
slug: ""
description: "The opposite to the Dead Cat analogy"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I was talking recently about a phenomenon in the IT security world, and that is shutting down an idea because someone thought of a reason the idea won't work. I don't think it's something that is specific to security circles, but anecdotally it seems more common place.

It's an immensely frustrating scenario to be involved in. You are looking for solutions to complex problems, and someone comes up with a way of solving it. Lets say during an incident post-mortem an admin logged in to a system and messed something up. Your control is to remove all direct admin logins that aren't via Single-Sign On. Then someone points out, if the Single-Sign On fails admins can't log in to fix it.

Not an insurmountable problem to some I'm sure, but because one solution has been countered with another problem and the meeting is just about to finish, you don't have time to work on the additional solution. You come away dejected because someone identified a weakness in what was just an idea.

These solution bombing edge cases are things you are going to have to consider, but they are also damaging to the purpose of the meeting. It may discourage people from contributing because others believe their idea will get shut-down.

In an iterative Agile world the solution is to try the idea out, _find_ the issues while you are developing them, not try to predict them.

However myself and my colleagues who have several years of experience in the industry have also been on the side of providing those Edge Cases, and it's important to share that knowledge, but it's important to recognise at this stage to let go of one's own ego and to caveat that knowledge that the past doesn't predict the future. They are things to consider while working on the solution.

The right answer should be to chose a solution, and for further discussions about potential weaknesses happen as part of the building process. The edge cases need to be the ones to be shut down, not for them to shut down the conversation.
