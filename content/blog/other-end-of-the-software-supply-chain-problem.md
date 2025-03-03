---
title: "The Other End of the Software Supply Chain Problem"
date: 2022-10-07T13:35:32+01:00
slug: ""
description: "What is the other way of managing it"
keywords: []
draft: true
tags: []
math: false
toc: false
---

You can't read a blog post or watch a talk on security in IT at the moment without [this XKCD](https://xkcd.com/2347/) being positioned prominently within it. Software supply chain security has been rattling a few people's cages this year after many in the industry had their Christmas holidays ruined by [Log4J](https://www.ncsc.gov.uk/information/log4j-vulnerability-what-everyone-needs-to-know) and [SolarWinds the year before](https://en.wikipedia.org/wiki/SolarWinds#2019%E2%80%932020_supply_chain_attacks) that. Leading some of us to wonder what _present_ we'll be receiving this year.

You know the software supply chain problem has gotten bad, because some are now questioning if it's even the right term.

There are of course now many companies telling you how their products can help. They tend to do this is scanning your repos, covering as many package managers as possible and alerting when it hits a list of un-trusted dependencies. I'm not saying to stop using these tools, it is additional defence in depth. But these methods are often reactive. If you have a continuous delivery pipeline it's likely you will push something in to production, then discover later that there was an issue with the release, and perhaps it's too late by that point.

For this reason some places I have worked don't want you to run the latest release but only one behind. This in-turn makes you more vulnerable to zero-days.

I like to look at the other end of the problem hole and ask, how can we be proactive about protecting our systems from it's own supply chain.

The first thing is to have a [mature delivery pipeline](https://www.scaledagileframework.com/continuous-delivery-pipeline/). It feels weird to be saying that in the year 2022 but it honestly wasn't that long ago for me that I discovered a team storing their code in a file share.

The next step is to use that pipeline to deploy idempontent code. Idempotent is a fancy word, that I'm not even sure how to say out loud, but means that the code is reliable and repeatable. Or, in practical terms, have tests and pin the version of your dependencies including a hash for that version.

The final step is likely controversial, but it will be a life-saver, your deployment pipeline has to package up your dependencies. Not once the code is deployed, but within the pipeline itself. With a Lambda or similar you have to try very hard to do anything else, but Docker images don't have to follow this rule. In fact often within Dockerfiles there is in-effect a second hidden package manager that downloads it's own packages independently. And certainly with EC2s and VMs this is really common. The recommendation here is to build secured gold images with the lowest attack surface possible by default.

Other things you can do are to ensure your deployed packages cannot call out to the internet by themselves. Taking it a step further it would be ideal to only allow your deployed package to contact the specific parts of the internet it needs, and that's what all the previous steps of the pipeline is for, to automate the environment your tooling runs in so that you know exactly what it can call out to.

You will also need infrastructure to support this. No-longer one big AWS Account but discrete accounts for each service you build (be reasonable here). Then you can set up your VPCs, Subnets, DNS and TLS certs along with the tools you have built to restrict network access to what your tool needs and what your tool needs only.
