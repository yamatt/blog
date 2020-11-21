---
title: "Assessing Security Practices of 3rd Party products"
date: 2020-11-20T18:10:32+01:00
slug: ""
description: ""
keywords: []
draft: false
tags: []
math: false
toc: false
---

In recent months I've been involved in discussions about whether remote working tools are "secure" or not. The answer to any blunt question like that is, as always, "it depends", but this is as helpful as getting financial advice from YouTube adverts.

It struck me that a lot of people interested in IT security often judge tools based upon how many vulnerabilities there are in a product. But lets be accurate here, they are judging it on how many security vulnerabilities are reported, or visible.

<!--alex ignore white-->
Once the pandemic forced us all to work from home, [Zoom seemed to be the target for every "white hat" hacker consultancy](https://www.bbc.co.uk/news/business-52115434) _generously_ giving their time to declare the 0 days they found to news websites, with nothing more in return than their company name to be placed along side the ~~advert~~ article.

These articles seemingly leading to several instances of "Enterprise" security teams declaring Zoom as insecure and made attempts to block its usage in their environments.

But is Zoom unsecure? And does blocking it improve things?

If you block Zoom, what will people use instead? Google Hangout? Skype? Chime? WebEx? Some random tool they found on the internet? Is blocking Zoom making things more or less secure?

Zoom got the attention because its user base and visibility increased massively during the pandemic. Admittedly it did have some low hanging fruit, but was it more or less of a threat to a business than your employees using something like [Omegle](https://en.wikipedia.org/wiki/Omegle) for work?

If we used the same metrics in which we judge Zoom and apply it to Windows or Linux those security teams would block almost all operating systems out there except maybe OpenBSD and BeOS.

##  IT security shouldn't be reactionary

IT security needs to be evidence lead. Would you say now that Zoom, after 6 months of global usage it is not secure? Other than the occasional [person posting their Zoom codes](https://twitter.com/mvanhulten/status/1329885925862760450), which is the Video Conferencing equivalent of calling your S3 bucket `big-bank-data`.

So can how can we be less reactionary in future?

One thing is to [recognise that Zoom fixed a lot](https://www.theregister.com/2020/04/03/zoom_security_improvements/), if not all, the issues that the security researchers were making a fuss over. Usually within days or weeks.

Where-as shouldn't we [trust GitHub less](https://www.zdnet.com/article/google-to-github-times-up-this-unfixed-high-severity-security-bug-affects-developers/) for having a long standing issue it's been unable or unwilling to fix?

What I'm proposing is instead of making decisions based upon what we read in the tech news this week, we measure good security practice from 3rd parties on how quickly and responsibly vulnerabilities in their products are announced and fixed, and be pragmatic about what your users need and expect from their IT.
