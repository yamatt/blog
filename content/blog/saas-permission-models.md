---
title: "Convenience is Antithetical to IT Security"
date: 2022-04-22T18:10:32+00:00
slug: ""
description: "A mixed bag"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I've been keeping my eye on the recent Heroku issues -- and sure the Travis CI ones too, but less so.

The thing I find that has been most interesting about it is that it's taken Heroku a long time to come up with a fix.

For context Heroku provide apps in to GitHub via OAuth. The access that Heroku has to your GitHub repo via OAuth is huge. Edit, delete, CI pipelines, secrets, team management. But these apps provide a really useful facility in Heroku that means that you don't need to configure your CI pipeline to deploy to Heroku. Heroku is configured to pick a branch on your repo and when it sees the code is updated in that it will build and deploy it for you. This isn't the only mechanism to deploy your code, but it is the most convenient.

It looks like GitHub identified that some got hold of the OAuth app secrets that Heroku uses for authenticating, and GitHub notified Heroku and the app was disabled. At the time of writing that was a week ago, and yet Heroku are still to provide any indication when they are going to turn that feature back on beyond confirming that they plan to.

The impact of this that a lot of people who use Heroku cannot deploy their changes, and by now are no doubt re-writing their CI pipelines to re-implement said feature, but this should be a more secure mechanism.

A conversation I had with a colleague this week reminded me of a saying I use about 'convenience being the opposite to IT security'. It takes me back to the closest thing to a security breach I've been involved in, when MongoDB defaulted to bind to `0.0.0.0` rather than localhost. [Subsequently there were something like 10,000 MongoDB servers servers on the internet with default passwords](https://en.wikipedia.org/wiki/MongoDB#Security).

So I'm expecting that the delays, are not technical in nature, but are due to a discussion between Heroku and GitHub on how to get the most granular permissions possible, while maintaining a very convenient feature. 
