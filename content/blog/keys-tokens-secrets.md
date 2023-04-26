---
title: "Keys, Secrets, and Tokens"
date: 2023-04-26T18:10:32+00:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

I have spent some of my time over the last 12 months working out how to improve our response to, first the Heroku leaks, followed later by the LastPass leaks, followed shortly by the CircleCI leaks. Each of which took a significant amount of time to resolve, time that could have been spent improving the features and capability of our main product.

One of the things that was identified as part of this response was that as engineers, we have several names for things that are very closely grouped, namely, Keys, Secrets and Tokens, there might even be others. I think any seasoned engineer will recognise that they do refer to different things, after all, we have AWS KMS and AWS Secrets Manager. But an IAM User Secret is functionally the same thing as what GitHub would refer to as a Personal Access _Token_.

It is helpful when looking to solve a problem to have a common language. We needed a way of describing, without significant friction, a way to refer to values that are used by systems to interoperate (i.e.: not a password), are sensitive, and need careful management.

I decided that the best word to encompass this was _Secret_. I felt this encompassed the meaning of the values more succinctly than any of the others.

I proposed this to our business via our usual engineering approvals board and it got accepted.

It's not to say that the usage of the word Key, or Token was banned, but that Secret emcompassed them all. The word _Secret_ could also mean a key or a token. Something sensitive that needs protecting.

It means that now when talking about secrets, teams know what it means for them.

There are likely differences in each business that may mean that secret isn't the right option for you, but having at least an awareness how these words mean similar, or different things can be helpful.
