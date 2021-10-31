---
title: "Software Development has Matured"
date: 2021-07-26T18:10:32+01:00
slug: ""
description: "Delivering services to software engineers securely"
keywords: []
draft: true
tags: []
math: false
toc: false
---

A conversation that I have regularly is how to secure developers. Your version control is your crown jewels, and yet development teams  often believe they have specific requirements that mean that admin access to their devices is the only reasonable option.

As someone who is primarily a developer myself, I still do recommend giving developers admin access as a solution, in a COPE and ZeroTrust environment I believe this works well as long as your version control system has sensible controls, such as approvers on merge requests.

Although considering a world where locked-down devices are the norm, there is a perception from developers that this is unacceptable. Think of all the random libraries on the internet you wouldn't be able to download and access. However I think we are at a tipping point now where as long as developers have access to an IDE and a browser there shouldn't be a need for any special software and permissions on the devices.

I certainly recall working in those locked-down environments and the amount of time it took to get new libraries in took days. This has serious security implications because you would not be able to use the most recently patched version of your tooling. But modern development has matured and everything is, or should be, run in your CI/CD pipelines.

This means there no-longer is a need to install spurious SDKs or libraries being installed on your devices. Everything is handled in a secure instance far away from your devices and write access to the code.

## Helpful Tooling

One of the caveats to this is that a lot of modern development tooling depends upon you downloading and installing a library (usually by piping curl to sudo) that goes about setting up some directories and files for you. I'm looking at you, Hugo, Kitchen CI, Molecule. Their documentation tends to assume you work this way and it can be very difficult to set it up without this helper tool, which makes things difficult when you don't have local install access and everything is run in a pipeline.

## Keeping up to date

One thing to consider however is that developers love to play and try new things. A good example of this is the recent release of [Copilot from GitHub](https://copilot.github.com/). Or lets not forget the sudden excitement for IDEs of a few years ago, starting with Sublime Text, and culminating in the release of VSCode and Atom within about 6 months of each other. Lets add more complications and say that Google release an IDE in the next few months.

If you have a reasonably sized delivery team it is likely that at least one person will want to experiment with it. It may even provide code quality improvement of upwards of 10%. This is something your developers will start to resent and look for alternatives if you aren't able to adapt.

You may think that giving back developers admin access is the only answer. However it's nieve to think that the fast turn around of new tooling is a requirement unique to engineers. What I propose is that your software packaging and deployment mechanisms should be really quick. Like 24 hours quick. Automate as much of it as you can, you'll likely need some human interaction, but if you're keeping your software up-to-date and patched on a regular basis, packaging a new one should not be much different in a majority of cases.
