---
title: "Using Scaleway's Serverless Service For Containers"
date: 2021-01-04T18:10:32+01:00
slug: ""
description: "Trialling a public beta"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I have been fortunate enough to have conversations with many cloud and traditional infrastructure providers over the years. I still would argue that AWS is the best in the business, but as always it depends on your needs.

Scaleway recently launched their public beta of their Serverless service, and I decided to take a break from spending my spare time playing with their instance offering to see what their new service was like. I find what Scaleway are doing at the moment to be particularly exciting. Their blog is always full of interesting posts about what they're up to, and in these IaaS wars that seem to be going on between the main providers are the ones that for me provide the technology I am most interested in.

First it should be made doubly clear that Scaleway's Serverless is a public beta and things are likely to change. However it is based upon their existing technology, and I'm sure despite their best efforts, from having only a spare few hours there is definitely some "Getting Started" documentation that is missing, particularly on the Container aspects of the service.

Going slightly off topic from the main purpose of this post, as I was having some difficulty using their service I'm looking to document the process of getting containers working in Scaleway's Serverless and and hopefully it will be something others will find useful.

## Create an Image Repository

I'm going to assume you have a fully configured Scaleway account. If not, do create one.

The first step is actually to log in to Scaleway and [create a Namespace in the Container Registry](https://console.scaleway.com/registry/namespaces). This is effectively running your own Docker Hub. Serverless cannot use any registry other than it's own to source containers from. The name can be almost anything, it doesn't have to be globally unique, you get a random ID assigned to the namespace anyway. It's just a way for you to more easily identify it.

It's worth noting the price disparity at this point. "Private" is the default option, but also has costs associated with it. If you select [Public then you won't be charged for storing your Docker images](https://www.scaleway.com/en/pricing/#container-registry) up to 75Gb, which is a lot of Docker images. They will be accessible by anyone from what is essentially a random URL, so it's public, but not exactly easy to find.

## Upload a Docker Image

You're going to need a Docker image that runs a HTTP server on port 8080. There are some ones that (Scaleway provide themselves in Python, running Flask)[https://github.com/scaleway/serverless-scaleway-functions/tree/master/examples/container]. This isn't ideal as Flask isn't meant to be run this way, but it's a starting point.



## Limitations

Here is a short list of limitations which I'm sure will be over-come when Serverless leaves Beta.

* You cannot run Serverless outside your default Project (which is functionally equivalent to AWS Accounts, or more accurately Resource Groups in Azure).
* You can only run Serverless in one Region
* You can only run containers from your own registry. This might be a pain if you want to use images from the public Docker registry.
