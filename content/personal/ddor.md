---
title: Daily Dose of Reddit
draft: false
date: 2026-01-16T19:00:47+00:00
---

There's always a lot of down time around Christmas, and I always end up getting stuck back in to Reddit. Almost like an addiction or something.

I always regret it.

The enshittification, the infinite scroll, and the sore neck I get for killing hours on there.

I also really like the format of [Daily Dose of Internet on YouTube](https://www.youtube.com/@DailyDoseOfInternet), where  every few days they publish a sub 10 minute video of the best social media videos. No "reactions", no filler.

I was thinking, well maybe I could do that for Reddit. Scrape the best 20 or so posts every day, and put it in an RSS feed.

So I built [DDOR](https://github.com/yamatt/ddor/).

One limitation, the enshittification of Reddit means there is no longer an open API.

So I switched to Lemmy, and its working pretty well.

What I came to realise though, is that my 'Top posts' algorithm is flawed.

Because there are so many communities (subreddits), you have to take the top of each one, and combine them.

I'm taking the last 24 hours of posts, which means that posts closer the time I take my snapshot of those communities, will have a lower score, and therefore won't be as high up.

This leads to me potentially missing high quality posts that haven't reached their pinacle yet.

I could take quite a few approaches. I thought about looking at yesterdays posts, but then the oldest post might be 48 hours old. I could look at the trajectory of a post, how many votes it got since it's been published, but that is potentially noisy. I could put the posts in 'top' and 'hot' buckets. [Y Combinators Hacker News has it's own ranking algorithm](https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d) published, [so does Twitter/X](https://github.com/twitter/the-algorithm).

But then I realised the rabbit hole I'm going down is the exact same thing all these social media companies are trying to do to keep you on the site for longer, and they have got in trouble for.

Not that I expect to get in to trouble, and I'm not trying to keep myself on my feed reader for longer. I just want to kill 10 minutes when I have the time to.

I'm ok with missing a few posts, and I believe that's a healthier place to be.

I'm recording some data about the posts I am putting in my RSS feed, so I could use that later if I want. I know that there are about 140 new posts per day on the Lemmy communities I'm following, and I re-publish about 15% of the daily posts.

Butwhat I found really interesting was that my silly little side project has lead me to have more of an understanding of what social media companies are doing, why they are doing it.

We tend to think these algoithms are mystical black boxes designed to enslave us. But really they're hard problems with multiple solutions, and none of them right.

Hopefully when you next think of these alogithems you, like I, will have more insights in to what that means.
