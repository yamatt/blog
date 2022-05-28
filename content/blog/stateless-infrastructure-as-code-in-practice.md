---
title: "Stateless Infrastructure as Code in Practice"
date: 2022-05-28T18:10:32+01:00
slug: ""
description: ""
keywords: []
draft: true
tags: []
math: false
toc: false
---

This article about the history of statefulness in Terraform really resonated with me. I had been toying with a concept recently, based on the observation that early DevOps tooling, and in particular Configuration Management tools, started off their history as stateful (Puppet, Chef) and evolved into statelessness (Ansible) as being the dominant model for managing servers.

I wanted to share my observations from my experiments based on the and the linked article, as I believe I found ways to over-come them.

My research initially focused on what stateless options exist for Infrastructure as Code (IaC) tools, playing unsuccessfully with CDK and Pulumi. These experiments lead me to believe that statelessness in IaC doesn't exist, yet, and I was disinclined to build my own given the plethora of cloud services that would have to be supported. So I started to develop a concept that would make it possible to use Terraform in a way that meant that I could discard the state file.

Some of the things that came up in the article are also things that frustrated me about stateful.

One being that state file initialisation was a catch-22, that you need somewhere to put your state file before building your infrastructure. Services like GitLab's Managed Terraform State do take the pain out of it, but it's far from a universal service.

The other issue is the deletion of resources that are no-longer used. You need some way to discard them without being specific about where they are and what they're called.  

## Becoming stateless

The chicken and egg problem with Terraform state files is actually the easiest to fix. I had already built a zero-cost [AWS Landing Zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/) platform in Terraform a few months back where new AWS Accounts are configured in YAML files per project. The Terraform in my pipelines then uses a root account to create further AWS Accounts and as a part of that pipeline they also provide an S3 bucket and DynamoDB where state files can be securely stored and locked. Then I needed to find some way telling your new service where to find these resources. So I went a step further and the pipeline also created a GitHub repo with the Action Secrets configured with the details that Terraform and other IaC tools need to store state.

The other thing to do now is to solve the problem of deleting resources you know nothing about.
