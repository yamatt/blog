---
title: "Cooldown Vs Zero Days"
date: 2025-11-22T10:30:32+01:00
slug: ""
description: ""
keywords: []
draft: false
tags: []
math: false
toc: false
---

<!--alex disable attacks-->

I love a blog post where I learn something new about a product I thought I was familiar with.

I use Dependabot every day. I've even got GitHub Workflows setup to automatically merge changes raised by Dependabot.

So I enjoyed the [post about Dependabot's cooldown feature](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns) that [I hadn't even heard of](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference).

But it reminded me of a discussion when I started in Cyber Security Engineering as to how to handle dependency updates.

The prevailing thinking at the time was that we should follow _release-1_, that is one version behind the latest release. Now there are complexities with that when using [semver](https://semver.org/), like what does one version behind mean when a minor version is patched.

The reasoning is sound, [after SolarWinds](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach) there were concerns about supply chain attacks, but my argument was that the vulnerability was in SolarWinds for a long time, and being on version behind would keep us on a vulnerable version longer.

On top of that _release-1_ is arbitrary. Why not _-2_ or _-3_ it's an arbitrary unit. What is the reasoning for chosing one or another?

And at the time zero-days were starting to become more common, so I pushed for day zero releases, which is _realease-0_ or update as soon as a version is released.

Now it seems we're back round where [supply chain attacks are in the news](https://blogs.jsmon.sh/shai-halud-worm-new-npm-supply-chain-attack-strikes-crowdstrike-many-others/), and everyone has forgotten about zero days, and people want solutions to supply chain attacks.

This seems likely to be a cycle.

They also seem like they're incompatible solutions.

Zero days mean go for day zero release. Supply chain attacks mean delay your releases.

But what this says to me is, that there might be other ways of thinking about this, and the way I'm thinking about this is to break it down further. Supply chain attacks is a broad term that could mean many things.

### Breaking it down

Supply chain attacks make good headlines, but belies several different classes of issues.

### Dependency take-over

Where a dependency is updated, intentionally by the author or not, to include malicious code.

Examples of this would be the Shai Hadid worm, linked above.

This usually affects older releases to.

But these changes seem to be detected pretty quickly because usually someone gets suspicious if a hash changes.

Your only option here is version hash pinning. Fortunately most dependency managers automatically support that with lock files these days.

### Latent Vulnerability

This is an unknown vulnerability that has been in the codebase for a long time, but only recently identified and shared.

Good examples of this would be [Log4shell](https://en.wikipedia.org/wiki/Log4Shell).

This was in Log4J forever before someone noticed, similar with Heartbleed and SolarWids.

That is why these are so painful to fix. A lot of systems that had been hanging around for years had this vulnerability and because they had been hanging aroud for years they were really difficult to update.