---
title: "Lets End Design Authority"
date: 2020-11-21T18:10:32+01:00
slug: ""
description: "Design Authorities are ineffective and damaging to IT security. Lets end the cycle."
keywords: []
draft: true
tags: []
math: false
toc: false
---

In every large, i.e.: "Enterprise" organisation I have worked in has some kind of "Design Authority" team. This is sometimes known as "Digital Design Authority" or "Enterprise Design Authority", but I think the idea extends from [Architecture Governance](https://pubs.opengroup.org/architecture/togaf8-doc/arch/chap26.html) in [TOGAF](https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework) where there is a kind of quality standards body responsible for authorising all technology solutions within a business.

In my experience they tend to be concerned with a considerable range of objectives, with varying degrees of priority. I think there are some nice ideas about detecting doomed projects early, identifying any over-lap in a large business, and security considerations, all with the intention of minimising future costs. The idea is that projects cannot complete without Design Authorities blessing.

However in my experience they are another gate-keeper with substantial bureaucracy that ultimately increases costs because even projects that could have been small, nimble, and ephemeral, falls within their gravity, and provides little efficiency savings because their understanding of a project skirts the edges without viewing the whole.

## The Elephant in the Room

As I say to my team regularly these days, you if you're going to eat an elephant, you don't want to try to swallow it whole. You need to break it in to small chunks.

The issue that should immediately stick out with Design Authority processes is that it tends to assume a big-bang delivery, whereas Agile methodologies tend to work on problems gradually over time. If you have a good Design Authority team they will often accept that you will have done significant work up-front before presenting to the Design Authority team. Acknowledging briefly the risk delivery teams take on if they fail to engage early, the first thing that stands out is cultural. Projects rooted in Waterfall methodologies, or a risk adverse delivery team, may seek to request Design Authority approval before any engineer commits any code. This can cause significant delays, and incur waste.

The next apparent thing about seeking permission first when using Agile methodologies is your delivery team will struggle to adequately meet a lot of Design Authority requirements because you are not at the stage of being able to consider them. You have to answer them as if you have met the requirement, at which point, what does Design Authority bring if they're approving something that may or may not exist.

## The Big Bang

My personal biggest bugbear with Design Authorities is that naturally, as a project develops, it evolves. In theory, each change, no-matter how minor, should go back to Design Authority for approval. Your delivery team downs tools, the documentation is re-issued, and all the same discussions are had again. No one would consider that pragmatic.

In reality delivery teams tend to negotiate a middle ground, an amorphous verbal agreement that small changes don't need to go back for Design Authority approval, but big architectural changes. Seems reasonable. But after 6 months of development you then may have made 10 small architectural changes and now those constitute in a big one, so you go back to Design Authority who chastise you for not coming to them sooner.

In my experience where this has worked well before is that Design Authority team has an open invitation to Sprint Reviews so that they can be taken on the journey with your delivery team, see progress and get an understanding of the delivered service and how it evolves, rather than comparing point A to point B over a significant period of time, which looks like a massive change.

## Broad but Shallow Knowledge

Another aspect is that the majority of those on Design Authority teams do not have the deep technical knowledge to know how to best engage the delivery team, to make sensible security recommendations and when to identify over-lap between projects. AWS ECS and Azure ACI are similar products at a high level, but for the purposes of cost saving offer limited value through knowledge sharing between two teams who use each product. However building common Docker images likely does. This nuance can be difficult for a non-domain expert to grasp. If you have 10 teams who use Docker and half of them use Azure and the other half use AWS, there is limited value in putting them all in touch with each other, unless they all need to run a Nginx Docker image.

Getting teams who have shared interests to find each other is a nuanced problem, however chat collaboration tools like Slack can successfully fill this gap. Creating channels for Azure ACI and AWS ECS as well as ones for Docker becomes an opportunity for self-selecting knowledge exchange.

The other thing that I find helps is Town Halls. Get your teams using Azure ACI presenting it to your teams using AWS ECS every month or so and they will find their own networks of knowledge.

## Enable, not gate-keep

I have presented a few alternative solutions to Design Authorities already. I am a massive proponent of asynchronous working, and minimising large meetings. There are things that Design Authorities could do that would help improve the quality of delivery teams. One of them is to take the current gate-keeping a level higher. For me, they should assure the delivery teams are using best practice. For example, does the delivery team have regular retrospectives? Is the delivery team actually following user lead design? Does the delivery team have good architectural principles around Infrastructure as Code, and CI/CD?

The other thing as well is, if the delivery teams are not meeting those best practices, get involved. Help them out. It's about success of the delivery team, rather than forcing them to fail. Be proactive and work with the teams to create good practice and a healthy and collaborative working environment.
