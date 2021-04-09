---
title: "Engineers Care Less About The OS"
date: 2021-04-08T18:10:32+01:00
slug: ""
description: "'No-body' is a bold statement"
keywords: []
draft: false
tags: []
math: false
toc: false
---

[Last Week in AWS](https://www.lastweekinaws.com/blog/) is another one of my favourite blogs, but [this weeks one titled 'Nobody Cares About the Operating System Anymore'](https://www.lastweekinaws.com/blog/nobody-cares-about-the-operating-system-anymore/) definitely got me thinking.

If you've never read Last Week in AWS the thing to note is that scores really high on the snark factor, and like most blogs it tends towards the hyperbolic titles to attract readers and discussion, after all, it's not as pithy, and not going to attract as much attention if the title is 'In the cloud, Engineers don't really care about the Operating System anymore'. Which is probably why my blog is much less snarky, and much more boring.

However, in this case I think the premise is wrong. It's not that even engineers no-longer really care about what Operating System you choose but that Cloud based Virtual Machines (as a catch all for EC2s, Azure VMs and whatever GCP calls compute) is no-longer used and for me is actually an indicator of 'infrastructure smell'. I.e.: that something is old, or unpatched, or not cloud native. For me, if I have to use a VM in [hyperscale cloud](https://en.wikipedia.org/wiki/Hyperscale_computing), something has gone wrong somewhere.

There are instances where you might use VMs, or more commonly called VPS, and dedicated boxes, which you find on more commodity providers such as DigitalOcean, Scaleway, or RedStation (to broach the tip of the iceberg), but when you have SaaS, FaaS, and Serverless Docker environments such as Fargate and Kubernetes, I really struggle to see the value in using dedicated, always on, compute. If anything its technical debt that you need to monitor, maintain, patch and scale.

As a side note, yes you [sometimes](https://chemidy.medium.com/create-the-smallest-and-secured-golang-docker-image-based-on-scratch-4752223b7324) have to choose a base Linux distribution for Docker images, but this is essentially a game of pick your preferred package manager, and then it's done and you never ever change that `FROM` value except to update the version number.

I can see why Corey would interpret that as nobody cares about the Operating System, but the broader picture to me is not that the Operating System doesn't matter, it's that we're at a point in technology in hyperscale cloud that the technologies allow us to abstract away VMs, making the variety of choice of Operating System is less relevant, but it's the cloud providers abstraction layers that enable that, rather than engineers not caring.
