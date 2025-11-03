---
title: "Storing Terraform state in your repo"
date: 2025-03-07T20:56:46+00:00
slug: "storing-terraform-state-in-your-repo"
description: "An alternative approach to managing Terraform state files"
keywords: ["github", "terraform", "infrastructure", "devops"]
draft: false
tags: ["terraform", "devops"]
math: false
toc: false
---

If you've known me for 5 minutes, I'll probably have told you how much I dislike all existing Infrastructure as Code tooling.

Of all of them I hate Terraform the least. HCL is _another_ DSL to get your head around in this cloudy world of DSLs. And given its similarities, but not, to JSON the learning curve is sharper than it should really be. But once you're comfortable with it, it's very quick to work with.

<!--more-->

But the thing I really hate is having to manage the state file.

The recommended route is to put it in S3 and then to have a state lock in DynamoDB, which is additional complexity and security you have to manage, and it still finds ways to mess up.

I don't want to manage state myself, I want something that manages state for me.

GitLab has a really nice service that automatically manages Terraform state for you. But I use GitHub and not much is going to change that.

Which got me thinking. GitLab has had this feature forever, maybe I missed something in GitHub that replicates it.

Possibly not something native, a quick Google confirms that. But maybe there's a GitHub action that does _something_?

Searching the GitHub Actions marketplace did identify a couple of candidates that store and retrieve state from artifacts, which is a nice idea.

Some of them even encrypt the artifacts, I guess in case someone downloads them.

But encryption adds extra complexity when you could:

- Not put secrets in your state file
- Use a private repo

But it got me thinking, if you're storing the state in artifacts, why not just store it in the repo. After all, it's just a JSON file.

So that's what I did. I created a blank branch called and stored and retrieved the state file from there.

There are some advantages over artifacts, such as being able to protect the branch and only allowing the workflow to manage that branch.

By itself it's difficult to scale because there's no state lock, two workflows could overwrite each other.

This isn't something I've tried, but merge queues should allow you to prevent two workflows running at the same time.

So I think this is something worth exploring and trying for a bit.

If it works out I might write an action for it.

I think if it was an action it would be more elegant with a standing up and tearing down process, but it works well enough and was pretty quick to get going.
