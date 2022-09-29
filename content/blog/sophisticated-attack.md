---
title: "Sophisticated Attack"
date: 2022-09-29T18:35:32+01:00
slug: ""
description: "Not really"
keywords: []
draft: false
tags: []
math: false
toc: false
---

<!--alex disable attack-->
<!--alex disable attacks-->

A trend I and some friends in the industry noticed over the last few years is that whenever a company gets hacked they almost always [call it a "sophisticated attack"](https://www.google.com/search?q=site%3Abbc.co.uk%2Fnews%20%22sophisticated%20attack%22). It kind of became a running joke, no-matter whether the attack was a Denial of Service, or data left in a public S3 bucket, that term was always used.

The latest one to use that term is the [Chief Executive of Optus](https://www.bbc.co.uk/news/world-australia-63056838), a mobile service provider in Australia, when they had their data stolen, seemingly by having their data available publicly on the web. This time [the government of Australia called them out on this](https://twitter.com/ClareONeilMP/status/1574361824102711296). Serious questions should be asked whether a government should call out a private business in that way, and the impact on their working relationship in the future, but it is refreshing for that term being picked up as being false by the media.

What's strange is that whenever these hacks occur they always use the same term 'sophisticated attack'. Almost as if there is a single comms playbook being used across all these organisations and countries.

The reason the term is used is because companies want the public to think that it wasn't a trivial amount of effort and deflecting criticism that the company were negligent in their responsibilities to finding and patching vulnerabilities. Whereas the reality is that these events are inevitable, and we need to plan for and minimise them. Does a mobile service provider need to store people's driving license details?

I wanted to explore the term 'sophisticated attack' some more. Where did it originate? How old is it? Is there a playbook? And lastly, can we improve how it is used?

The first step is to check Google Trends:

  <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3045_RC01/embed_loader.js"></script>
  <script type="text/javascript">
    trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"\"sophisticated attack\"","geo":"","time":"2004-01-01 2022-09-29"}],"category":0,"property":""}, {"exploreQuery":"date=all&q=%22sophisticated%20attack%22","guestPath":"https://trends.google.co.uk:443/trends/embed/"});
  </script>

Well that was disappointing. I was expecting a linear or exponential increase. If anything that is a decrease. The related queries seem to involve military usage, so perhaps the term originates in the military and that has been transferred to cyber security. It wouldn't be the first time.

During this research I discovered that [I'm not alone](https://www.engadget.com/2016-06-06-dnp-sophisticated-hack-attack-dont-believe-the-hype.html) in trying to look in to the origins. I don't agree with some of the language used, but if a paid journalist can't find the origins I don't think I can either.

Ok, so let's finish off by looking at how we can use the term 'sophisticated attack' better.

The types of attack most people on social media seem to exclude are open services leaking data and DDoS. I don't want to base the definition off a list of types of attack because having an exhaustive list will be difficult to maintain. The other commonality is that these exploits can be performed by anyone pressing a button, such as on a DDoS service or an online scanning tool like Nessus. It seems to me then that the definition can exclude running a single script or action to perform the exploit.

That means that chaining exploits is probably a better way to define the level of sophistication. If the attack involved 2 or more steps to get access to the data that seems like it took effort and skill. If an attacker found a [SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery) to exfiltrate cookies and used that to gain access to a poorly protected admin interface, that is 2 or 3 steps. That is sophisticated.

It also means as security improves 2 steps can become norm and 3 steps will be the new 'sophisticated'.

By communicating about these attacks better we can start to have real conversations about how to protect data better. 
