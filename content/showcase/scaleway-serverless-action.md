---
title: "Scaleway Serverless Container Deploy GitHub Action"
imageurl: /img/scaleway-serverless-action.png
date: 2021-03-10T18:50:32+01:00
slug: ""
description: "A GitHub Action to deploy images in Scaleways Container Registry to Scaleways Serverless Container"
link: https://github.com/marketplace/actions/scaleway-serverless-container-deploy
license: CC BY-SA 4.0
keywords: []
draft: false
tags: []
math: false
toc: false
---

[This project](https://github.com/yamatt/scaleway-serverless-container-deploy-action) was, after a long play with both GitHub Actions and Scaleways Serverless beta, my first foray in to improving my deployment workflow.

Scaleways Serverless public beta is a new service that that lets you run both AWS Lambda like FaaS and Docker images in a ephemeral way. It is also free while in public beta, but of course there are issues because it is in beta, which I will not go in to in detail here.

The documentation hasn't been brilliant, neither is GitHub Actions, but I did get to a point where I had a really good self deployment workflow when pushing changes to GitHub. However, despite successfully using GitHub Actions since their public beta, I had never created a GitHub Action before. So I decided to combine that, and this is what I ended up with.

It doesn't work on it's own or isolation. You need to import your images in to Scaleway Container Registry to do that, and there are plenty of good and existing GitHub Actions that can already do that.

I simply wrapped the API using cURL (and jq for testing) that makes deployment a one step process, and published it to the marketplace for others to use, then promoting it in the Scaleway Slack to get feedback. I also used it in my original test project and it works beautifully.
