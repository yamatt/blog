---
title: "Experiments in Stateless Terraform"
date: 2022-05-28T18:10:32+01:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

This article about the history of statefulness in Terraform really resonated with me. I have been toying with a concept recently of a configuration of Terraform that no-longer required the storage of the Terraform state file.

The origins for me were based on the observation that early DevOps tooling, and in particular Configuration Management tools, started off their history as stateful (Puppet, Chef) and evolved into statelessness (Ansible) as being the dominant model for managing servers.

I wanted to share my observations from my experiments and the linked article because I have found that under the current way AWS works, it is not possible to use Terraform without state, but further than that it is a problem I don't think AWS can fix, but others have.

The key issue here is the deletion or removal of resources that are no-longer used. You need some way to discard them without knowing that they exist. I was working on the assumption that it would be possible to use an AWS Account as an ephemeral container for everything that needed to be built and destroyed.   

## Becoming stateless

I already have a zero-cost [AWS Landing Zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/) platform in Terraform where new AWS Accounts are configured in YAML files per project. The Terraform in my pipelines uses a root account to create further sub-accounts.

To maintain availability and to treat AWS Accounts as disposable I was intending to use a [Green/Blue Deployment](https://www.redhat.com/en/topics/devops/what-is-blue-green-deployment) where we can build the new deployment in one account, then remove the old account when the new one has been switched over to. A separate load balancer account would switch between the two when the new one is up and running.

## MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED

There are a few problems with this, and this where I ran out of options.

The primary one is that automating the deletion of AWS Accounts is really difficult. The sub-account requires credit card details for an account to be removed, even as part of an AWS Organization, and that to me, makes it a manual step.

<!--alex ignore black hole-->
There is an alternative however, which is what I called the account "black hole". Which is an OU in your AWS Organization that has a policy on it that prevents all roles from being assumed. That way your resources cannot run and your cost will eventually reach zero.

You then run in to another issue, that is that there are soft limits on the number of sub-Accounts that an AWS Organization can have. This can be adjusted if you ask Amazon nicely, but if you are deploying several times a day (and hopefully you are) then you will be rinsing your limits.

It _is_ a soft limit, so you can ask Amazon for that limit to be raised, but you do the math, and you can see you'll likely have an unhappy Amazon asking you why you are doing that.
