---
title: "SaaS Permissions Models"
date: 2022-04-22T18:10:32+01:00
slug: ""
description: "'No-body' is a bold statement"
keywords: []
draft: true
tags: []
math: false
toc: false
---

One thing that the issues that Heroku are dealing with has made me think about is how the permission models in SaaS products are usually pretty terrible.

In fairness I think we're spoilt by policy documents schemas, and the granularity in PaaS services. We expect to be able to define a re-usable JSON document that describes in which read or write permissions for a particular feature is needed for any particular service. It's a really great model.

But compare this to [creating a Personal Access Token (PAT) in GitHub](https://github.com/settings/tokens/new) where you are given a huge large number of tick boxes that could mean anything. AWS isn't really any better, in fact it's worse, but that's also it's strength. You want to disable just read access on DynamoDB, you can do that. GitHub on the other hand, if you wanted to give a PAT token just permissions on a single repo to create Pull Requests, I wouldn't even know what is the correct option to choose.

GitHub isn't alone. I think anyone to has much experience with GitLab will know the pains of using it's very opinionated permission model. One pickle I ended up in was when using the Managed Terraform State feature in GitLab. I didn't want to give the apprentices I was looking after merge rights because I felt it was a valuable learning experience to check code before they merged it. However that same permission level also meant that they didn't have rights to access the Managed Terraform State so they were also unable to test their code unless someone senior re-ran the pipeline for them. That clearly doesn't scale. But there was no option to make the change to the permissions in GitLab. They have a fixed set of permissions and levels.

I have never built a permission model, of note anyway. No doubt building them is hard. Looking at AWS IAM policies the logic is hard to understand for someone writing them. Any Deny over-writes the Allow. It makes sense, but this is big-brain thinking stuff.

Implementing a permission model retrospectively must be an excruciating exercise. Never knowing when the thing you've just locked out is going to break someone's assumptions about how their thing works. You can see this is the S3 permission model. S3, being one of AWS's first services, has had a difficult relationship with security controls.

I expect the true answer lies in having well defined controls from inception. But unless you are building global scale tooling, and a lot of companies have ambition but don't get there, that is an over-head that just won't happen.

SaaS tooling is best placed to solve this problem, but they don't seem able to.
