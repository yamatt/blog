---
title: "Notes on Cyber Advisories"
date: 2023-03-24T18:10:32+00:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

The weekend of March 18th was an interesting one for security communication.

Towards the end of the working week [Google announced several bugs affecting Android baseband modems](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html), and it was a serious bug. Any Android device with a particular set of hardware could be forced to run remote code simply by knowing someone's phone number. This could lead to the another [Pegasus](https://en.wikipedia.org/wiki/Pegasus_(spyware)).

Project Zeros audience is for technical readers looking to understand a problem and are interested the detail. I have no issue with that.

But many businesses, including my own, took this threat and thought it important enough to provide some additional awareness to their staff, based off of the Project Zero blog post, or similar articles from technical news outlets. Your internal staff is an entirely different audience and the original wording was not helpful for the wide range of technical knowledge that will exist among your staff. People working in Cyber tend to be technical and will likely understand the problem and will likely not understand the needs of their staff in a situation like this.

An extract of the article leads on to knock on problems. If you're not communicating effectively then your audience will either ignore your advice or look to you to help them. Communications need to minimise both those outcomes to be effective. There is a secondary effect that if both of those outcomes are also not handled well it will train your audience to ignore that advice in future.

## Indentifying your Audience

The first step is to minimise who you are communicating to. If your business runs entirely iPhones, then there is no need to alert everyone. This would create alert fatigue. So we need to work out who to communicate to. The Project Zero article listed some of the hardware that was affected. This meant that if you had detailed data on what your staff were using you could be really targetted. There were two problems with this however. One was that the list was a guess, secondly most people didn't have this level of data. I know that I didn't. This was combined with the article being published at the same time as the patch, at least for Google devices, so that meant any adivories would be sent out to people who didn't need to do anything. So we decided to warn any Android user. Not ideal, but it was the best we had.

## What to Communicate

There were two things to avoid here.

One was the list of devices, that as discussed above, is inaccurate. The true answer to this turned out to be really simple. Your device needed a patch, if you were going to get a patch you will receive a notification. There was no need for your staff to know what device they had -- and most don't. It became self selecting. There is a selection of users whose devices are old and therefore won't receive the patch, but that is an entirely different problem.

The second was the note in the blog post about turning off VoLTE and Wi-Fi calling. This was originally pretty high and highlighted in the article. I'm relieved to see it has been demoted. While this advice could be useful for a technical audience, and we're likely to be someone targetted by this attack, to the general user this is of no use at all. I outlined why in our original communication which I'm going to reproduce here:

* Android fragmentation means that there is no way to provide one set of instructions that works for everyone - this will lead to queries which someone needs to be equipped to solve, and to re-iterate it's a fragmentation problem so it's not an easy thing to solve
* It's a very technical and specific thing to ask someone to do without supervision - It seems likely a user would choose the wrong option and cause further problems that we have a responsibility to solve
* It would impact the users ability to make phone calls which in low signal environments could be extremely important either personally or professionally
* Not knowing if they have to do it or not because we can't be certain which devices are affected, or have been patched
* Having to remember to reverse the change when the update has been applied and doing that correctly
* Now knowing if the update that has been applied is the one that affects them
* The liklihood of it affecting the majority of your staff is really small

## Our Actions

In the end we went with some advice to Android users telling them that there was a new threat and reminding them to be on the look out for and apply the patches that their phone asks them to apply. We also spoke directly to our people on the list of 'important' people who may genuinely be targets for the attack and with their permission turn of WiFi calling.

This may sound unsatisfactory. It feels like a cop-out. We're not giving very useful advice that could have been given out at any time. That is true, but you will be surprised how many people don't update their devices, OS or browser, because it's inconvenient, and events like this can be a useful talking point to get involved with.


