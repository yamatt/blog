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

I have spent some of my time over the last 12 months working out how to improve our response to, first the [Heroku leaks](https://www.theregister.com/2022/04/21/github-stolen-oauth-tokens-used-in-breaches/), followed later by the [LastPass leaks](https://www.wired.com/story/lastpass-engineer-breach-security-roundup/), closely followed by the [CircleCI leaks](https://circleci.com/blog/january-4-2023-security-alert/). Each of which took a significant amount of time to resolve, time that could have spent improving the features and capability of our main product.

I identified as part of this response was that as engineers, have many names for things that are very closely related, namely, Keys, Secrets and Tokens, there might even be others. I think any seasoned engineer will recognise that they do refer to different things, after all, we have [AWS KMS](https://aws.amazon.com/kms/) and [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). But an IAM Users has [both keys and secrets in the same sentence](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and that keys is a differnt key to the KMS key.

It is helpful when looking to solve a problem to have a common language, a way of describing a problem when talking to teams that they know what it means for them.

I needed a way of describing, without significant friction, a way to refer to values that are used by systems to interoperate (i.e.: not a password), are sensitive, and need careful management.

I decided that the best word to encompass this was _Secret_. It seemed like it had more meaning, in a more succinct way than any of the other terms available.

I proposed this to our business via our usual engineering approvals board and it got accepted.

It's not to say that the usage of the word Key, or Token was banned, but that Secret emcompassed them all. The word _Secret_ could also mean a key or a token. Something sensitive that needs protecting.


There are likely differences in each business that may mean that secret isn't the right option for you, but having at least an awareness how these words mean similar, or different things can be helpful.
