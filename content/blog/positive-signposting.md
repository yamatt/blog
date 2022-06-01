---
title: "Positive Signposting"
date: 2022-05-27T18:10:32+01:00
slug: ""
description: "Avoiding negative messaging"
keywords: []
draft: true
tags: []
math: false
toc: false
---

Whenever possible, one of the rules I follow when writing IT Security guidance is to create positive messaging. As a society we have a tendency to tell people to stop doing something, rather than telling them how to do the right thing. It's more instinctive to say "Stop doing that!" rather than "Could you do this instead?", possibly because it's easier to know what not to do, than to be creative about what could be done.

The issue though is that when we are presented with multiple options, negative signposting removes one option, rather than providing guidance on finding the right solution. This creates poor customer experience as it makes it painful for those that are genuinely looking for the right solution.

I encountered a real-world example of this in the office recently. There are paper-towels in the office kitchen for drying cutlery, crockery and our hands. We are also provided with a choice of bins to discard our waste items. There is a recycling bin, a food waste bin, and a general bin. Being environmentally conscious, I, and clearly out others, were discarding our paper-towels in the recycling bin. This is apparently incorrect.

The solution the people who manage the office came up with was to affix a note to each kitchen in the building.

![A kitchen counter with 3 bins labelled 'General waste', 'Food only', and 'Recycling' with an additional label beside recycling that says 'No paper-towels'](/img/blog-post/positive-signposting/negative-signposting.png)

Do you see the problem?

Where _should_ the paper-towels go? Food waste? Could be. General waste? I'd like to avoid it if at all possible. It isn't clear.

## How do we improve this?

The quickest answer is a near identical sticker next to whichever is to the correct opening saying "Paper-towels", or perhaps "Paper-towels here please", or even better "Paper towels yum-yum". But that's not the end of the story.

The other issue is that the messaging doesn't scale. Today it's paper-towels, next week people are incorrectly disposing their used pizza boxes in the wrong bin. Where should those go?

Most boroughs in London, where my office is, often send leaflets to the people living in their area and [put guidance on their websites about what you can recycle](https://www.westminster.gov.uk/check-before-you-chuck#paragraph-id-3463). Learning from their approach perhaps more information could be provided either directly to staff, either on internal services, or in the kitchens themselves. A nice infographic that can be absorbed at a glance.

But let us not stop there. What if a new technology comes along, such as a new kind of eco-packaging, that messes with people's expectations and disrupts the information provided? Perhaps that can go in to food waste? But it could also mean people could be wasting materials that should be recycled.

Now we're getting to the bottom of the underlying issues.

One option I can see is to educate people in the kitchens not about what can or cannot go in to the bins, but in to the disposal processes. Enabling them to make informed decisions about where items should be disposed. After all maybe the General Waste bin is a very sensible place to put things. I don't know what happens to it.

There will also likely be edge-cases and for those situations perhaps we can provide a service that helps people identify where those items should go, like a phone line or an app. Although that is likely context dependent, and potentially expensive.

Another option is that there could be a single bin and the sorting takes place in a different place where the proper assessment of the materials can take place, with trained individuals. I'm sure there are issues with the mixing of materials and again, no doubt expensive.

Another option is to use [affordance](https://en.wikipedia.org/wiki/Affordance) that encourages the separation of different kinds of items, such as [Amberol bins that have shaped openings that encourage in particular bottle and paper recycling](https://amberol.co.uk/bins/outdoor-recycling-bins/olympic-dual-bin). This allows people to make minimal effort decisions about where their product should go because they will identify the lowest effort bin to use.

## The security angle

You now might be saying "You've lost me. You've written a lot about bins. What on earth does this have to do with security?"

Well, a lot.

What I'm trying to illustrate here is that using ["common sense" is not the answer]({{< ref "./common-sense-as-bad-practice.md" >}}) and neither is blaming your customers. If you want to create a difference to a problem you are experiencing you need to analyse the problem and come up with solutions that work in most if not all cases, because our first instincts are often bad.

Worried about weak passwords? Let's enforce more complex ones. Worried about phishing? Lets phish our users and blame them for clicking on the links.

Or we could think about the problem and provide tools our customers want, beyond guidance and in to services that allows them to make good, informed, decisions.

If something has gone wrong, don't mark the action as wrong and control for it, identify what needs to be done to make it go right.
