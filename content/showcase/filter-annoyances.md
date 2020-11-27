---
title: "Filter Annoyances"
image_url: /static/img/filter-annoyances.png
date: 2020-11-27T17:14:32+01:00
slug: ""
description: "uBlock Origin filters to remove annoying things about the web."
link: https://yamatt.github.io/filter-annoyances/
license: CC0
keywords: []
draft: false
tags: []
math: false
toc: false
---

This is my first foray in to making uBlock origin. I was at the time, and still do, wanted to remove the cookie and GDPR pop-ups but still use the site. These filters help facilitate that.

There are a couple of built-in ones to uBlock such as [easylist cookie](https://github.com/easylist/easylist) and uBlock Annoyances, but these looked difficult to contribute to.

I did use [_I don't care about cookies_](https://addons.mozilla.org/en-GB/firefox/addon/i-dont-care-about-cookies/) for a little while, which worked fine, but I couldn't find it's source code anywhere, despite it saying it's open source. So I thought to be safe I would stop using it.

I'm kind of curious about ways you can test and validate uBlock Origin filters. It seems kind of difficult.

I also found that the [filter syntax used in uBlock Origin comes from Adblock Plus](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax), and they can be very imprecise. But the uBlock Origin element picker tool is amazing. Some of the time I use it then copy the generated rule in to this repo.

I chose (rather unusually for me) the CC0 license for these filters because I wanted to put them as much in to the public domain as possible, and because they are not really programmatic scripts.

The distractions list is purely for things that take me away being productive on sites I use day-to-day. Kind of dark patterns really that keep you on their site.

The aggressive filter I've moved away from because it was too difficult to maintain and I kept having to switch off uBlock to see if the page worked, which then meant I saw adds.
