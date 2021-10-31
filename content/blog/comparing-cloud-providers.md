---
title: "Comparing Cloud Providers"
date: 2020-11-21T18:10:32+01:00
slug: ""
description: "Comparing Tangerines and Clementines"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I've been involved in some discussions recently about comparing cloud providers. I'm all for evaluation and assessment of the correct tool for the job, but I think cloud platforms are a bit of an exception.

Yes, Azure has Databricks natively, AWS has SageMaker and Jupyter Labs natively.

Yes, AWS has some nice machine learning based fraud and anomaly detection tools, and Azure doesn't so much.

Yes, Azure is somewhat more "and the kitchen sink" than AWS when it comes to pricing.

But I don't think features is really the point. They are all innovating so fast that they are close to parity so that today your evaluation gives Azure the edge, and in 12 months time it will be AWS. And no one in their right mind is going to spend the effort flip-flopping between providers every 12 months. It's hugely time inefficient, costly and wasteful.

For me, if you're going to evaluate cloud providers, you have a few factors you can assess. Most of them only once you've bit the bullet. There are actually only 2 factors you can assess up front. Both of which are summed up nicely in the [Last Week in AWS blog](https://www.lastweekinaws.com/blog/the-lock-in-you-dont-see/).

## Data Gravity

This is explained very well elsewhere, but in short, getting data in to cloud is cheap. Getting it out is expensive. What you need to consider is where does your data currently live, and how much would it cost to move it out of there. Out-bound fees for data are *massive*. If you were to take a storage optimal approach and have some kind of hybrid environment where for example all your data lives in AWS S3 and all your processing lives in Azure you're going run up some enormous bills just on data transfer. Choose one provider and stick with it.

## Delivery Team Experience

As is also mentioned in the _Last Week in AWS_ post, but for me is the most important point, you have to consider the experience in your delivery teams. If your team has a majority of experience in AWS and you choose Azure based on technical grounds, you now have to spin a lot of cycles on re-education to get your delivery teams spending a lot of time getting used to the new way of working. You also open yourself to more risks because for example, practices for a secure environment that make sense for AWS, will likely need different arrangements in Azure, resulting in a greater chance of causing a security weaknesses by not playing to your teams strengths.

## What you can't predict

Cloud platforms are a complex beast. There will be so many assumptions you haven't identified until you start using it. Maybe you pinned all your hopes on Amazon Workspaces, only to find it doesn't do as much of the job as you had hoped, and now your decision calculus changes and your assessment based on that single factor makes AWS no-longer the better option, however you're already 6 months in to your development and changing your mind now is will entail significant rework.

Other things that might not have seemed import to you at the start of the project become important as you build out. Such as maybe it  takes 30 minutes to build an Elasticsearch as a Service on Azure, and 20 minutes to build an Amazon Elasticsearch Service and maybe that doesn't meet your SLAs. Now you have to re-evaluate if changing everything and starting again is worth it.

## Conclusion

What this boils down to is a form of analysis paralysis. Doing too much design up front without recognising your assumptions.

So save your time and effort deciding on what platform to use. Quick finger in the air. Where does most of your data live, and what experience does your team have? If they're different you have an actual business decision to make. If not, you will have saved yourself a whole load of time and effort. Time that could be spent delivering value to your users.

And don't regret your decision. Technology is always solvable. It might not be optimal, but there is always an answer.
