---
title: "Experiments in Stateless Terraform"
date: 2022-05-31T18:10:32+01:00
slug: ""
description: ""
keywords: []
draft: false
tags: []
math: false
toc: false
---

[This article about the history of statefulness in Terraform](https://www.bejarano.io/terraform-stateless/) really resonated with me. Over the last few months I have been playing with setting up Terraform in such a way that the state file was no-longer required.

This post is about sharing my observations from those experiments because what I found instead was that with the current way AWS works, while it is possible to use Terraform without state, there are some limitations with AWS that made this more difficult than I expected.

The key limitation you encounter when you no-longer know the state of your infrastructure is identifying which resources are no-longer needed. You either need to enumerate them, or to discard them without being aware that they exist. The first solution I tried was to use the AWS Account as an ephemeral container for everything that is built and destroyed.

## Becoming stateless

The concept is that everything you need is first built in to one AWS Account, then when you want to release a new instance, re-create everything in a second AWS Account and switch over to it. The first AWS Account can then be removed without needing to consider what is in it. A separate AWS Account with a load balancer can then perform the switching when the new infrastructure is up and running. This is a form of [Green/Blue Deployment](https://www.redhat.com/en/topics/devops/what-is-blue-green-deployment).

## MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED

There are a some limitations with this, and this is where I think it gets interesting.

I do recognise that what I'm attempting to do is a hack, Terraform and AWS are not designed to be used this way. Terraform will not have made their decision to use state in isolation, they will have also encountered the problems I am have stated and the solution they went for was adding complexity through state files. I don't see that as unreasonable, they made those decisions based upon the limitations of AWS, and AWS made assumptions they made about how their was intended to be used, and that is pretty unusual.

My first thought to clearing out the old resources is to delete the AWS Account. However, the deletion of AWS Accounts from an AWS Organization requires the sub-account to have credit card details associated to the Account. That makes it a manual step. A manual step means no automated Green/Blue deployment.

<!--alex ignore black hole-->
There is an alternative, I call it the "black hole". This is an OU in your AWS Organization that has a policy on it that prevents all roles from being assumed in that Account. That way your resources cannot run and your cost will reach zero.

This then runs in to another issue, that there are soft limits on the number of sub-Accounts that an AWS Organization can have. It _is_ a _soft_ limit, so you can ask Amazon nicely for an increase of that limit, but you do the math on the number of deployments you do a day, and I bet in a short amount of time you will have an unhappy Amazon asking you what you are up to and can you please stop.

## Better Solutions

I think the only other way of doing this is to follow the enumeration path. Fortunately tooling such as [cloud-nuke](https://github.com/gruntwork-io/cloud-nuke) exist to empty an AWS Account of resources. You can even be selective about allow-listing certain resources, but it is a very slow process and it [may not cover everything](https://github.com/gruntwork-io/cloud-nuke/issues/281).

However, the interesting part here was finding the limits of what was possible in AWS. Not something I encounter often. I don't have a lot of experience in other PaaS services so I would love to hear if doing this is possible in Azure or GCP.

I do wonder if its something Amazon will fix, but I also think it will be a fundamental limitation in how AWS built Accounts and assumptions that were made at that time. Otherwise they would no doubt have made it easier.

A different solution I've started to see with services like [Fastly](https://docs.fastly.com/en/guides/working-with-services#editing-and-activating-versions-of-services) and [Doppler](https://docs.doppler.com/docs/versioning) is that they have configuration versioning built right in to their web UI.

I am hopeful that this is a tend towards a [ClickOps model](https://www.lastweekinaws.com/blog/clickops/) which has the ability to make Infrastructure as Code, and therefore managing state, redundant. The first PaaS services to do infrastructure versioning this way is going to get a lot of attention to me. However, I don't see this happening in AWS for a long time.
