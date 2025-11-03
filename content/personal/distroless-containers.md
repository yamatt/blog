---
title: "Distroless Containers"
date: 2025-01-03T19:47:28+00:00
slug: "distroless-containers"
description: "Understanding what Distroless Containers actually are"
keywords: ["docker", "bsides", "containers", "security"]
draft: false
tags: ["docker", "containers", "security"]
math: false
toc: false
---

I was at BSides London the other week, and there was a talk I wanted to go to on Distroless Containers. I wasn't able to make it though as there were so many good talks I had to make a call and went to a different talk.

I have however done a bit of research on the subject of Distroless Containers over the last few days after [writing my first tool in Go](https://github.com/yamatt/dwnldr), and I recalled there is a way for a Docker image to load a Go binary directly and I was trying to work out if Distroless Containers were the path to that.

<!--more-->

Turns out, no, it isn't. [What I wanted were scratch containers](https://james-farrell.com/posts/scratch-docker-golang-images/).

But to get to the point of this post, I learnt about Distroless Containers, and I wanted to share my understanding because there's a lot of words written about it, and I wasn't impressed with much of it. So I wanted to make it easier for others to understand.

The first thing is that they're not Distroless at all. It's Google's whacky naming making things confusing.

Really Distroless Containers are the name for a way of building Docker images that keeps the file size small, and therefore have a reduced footprint and therefore a smaller attack surface, i.e.: more secure.

The second thing to understand is that it uses a pre-existing feature of Docker, in that a Dockerfile can contain multiple image definitions, or stages, that do different things.

In practice it means that in one stage of your definition, your image first builds the binaries it needs, then you use the second stage to run the binary. The second step throws away everything in the build step, and starts with a new clean environment, which you copy your binaries from the build step in to.

You are really just using the FROM parameter in your Dockerfile a second time. And Docker knows to discard the build step but still allows you to COPY your binary from it.

Turns out this was something I was doing unintentionally already. But I do love it when you discover a name for something that you happenee to be doing.
