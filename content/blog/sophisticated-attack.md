---
title: "Sophisticated Attack"
date: 2022-09-29T18:35:32+01:00
slug: ""
description: "Not really"
keywords: []
draft: true
tags: []
math: false
toc: false
---

A trend I and some friends in the industry noticed over the last few years is that whenever a company gets hacked they almost always [call it a "sophisticated attack"](https://www.google.com/search?q=site%3Abbc.co.uk%2Fnews%20%22sophisticated%20attack%22). It kind of became a running joke, no-matter whether the attack was a Denial of Service, or data left in a public S3 bucket they always used that term.

The latest one to use that term is the [Cheif Executive of Optus](https://www.bbc.co.uk/news/world-australia-63056838), an Australia based mobile service provideder, when they had their data stolen, seemingly by having their data available publicly on the web. This time however [the Australian government called them out on this](https://twitter.com/ClareONeilMP/status/1574361824102711296). There are serious questions there as to whether a government should call out a private business in that way, and the impact on their working relationship in future. However it was refreshing for that term being picked up as being false by the media.

What's really strange is that whenver these hacks occur they always use the same term 'sophisticated attack'. Almost as if there is a single comms playbook being used across all these organisations and countries.

The reason the term is used is because companies want you to think that it wasn't easy and they were negligent in their responsibilities in finding and patching 

I wanted to explore this term some more. Where did it originate? How old is it? Is there a playbook? And lastly, can we improve how it is used?

The first step is to check Google Trends:

  <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3045_RC01/embed_loader.js"></script>
  <script type="text/javascript">
    trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"\"sophisticated attack\"","geo":"","time":"2004-01-01 2022-09-29"}],"category":0,"property":""}, {"exploreQuery":"date=all&q=%22sophisticated%20attack%22","guestPath":"https://trends.google.co.uk:443/trends/embed/"});
  </script>

Well that was disapointing. I was expecting a roughly linear or exponential increase. If anything that is a decrease. The related queries seem to involve military usage, so perhaps the term is originates in the military and that has being transferred to cyber security. It wouldn't be the first time.

During this search it turns out [I'm not alone](https://www.engadget.com/2016-06-06-dnp-sophisticated-hack-attack-dont-believe-the-hype.html) in trying to look for the origins of this. I don't agree with some of the agressive terminology, but if a paid journalist can't find the origins I don't think I can either.

Ok, so let's move on to how we can use the term 'sophisticated attack' better. The obvious thing is that open services leaking data and DDoS are out. These are things anyone can do with a bit of scripting knowledge. What it immediately makes me think is that chaining exploits is probably a better way to define it. If it involved 2 or more steps to get access to the data that seems like it took effort and skill, therefore sophisticated. It also means as security improves we can say that actually 2 steps is the new norm and 3 steps will be the new 'sophisticated'.
