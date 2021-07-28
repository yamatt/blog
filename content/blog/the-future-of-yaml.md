---
title: "YAML: Out of Order"
date: 2021-07-28T18:10:32+01:00
slug: ""
description: "The Future of YAML"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I did enjoy [Drew DeVault's wish-list for the future of YAML today](https://drewdevault.com/2021/07/28/The-next-YAML.html). I have to agree with all of it. YAML is terrigood.

I recall reading an article years ago (that of course I can't find now) comparing the  YAML spec to other similar languages such as XML, JSON, etc, and whatever you pick YAML's spec blows them out of the water in terms of length. The implication being that YAML is very difficult to implement correctly.

But YAML is also great, and I think that is down to the syntax being very intuitive. It's familiar to a lot of people, especially those familiar with a bit of Python.

One thing I think Drew over-looked though, and I'm sure many, like Drew, would not automatically recognise this, is that one really important aspect of YAML, and why languages like TOML won't replace every case of YAML, is the inference of sequencing in a YAML file.

This becomes particularly apparent with Ansible. You cannot have an Ansible script without a sequence. There is a top down order to the structure of an Ansible playbook. You will also find this in most CI languages such as GitLab CI and GitHub Actions, although they are less apparent because you can also break the sequence by referring to other steps.

This inferred sequencing is not something you can do in TOML. Much like in CI pipelines you could reference other steps, but it starts to feel very much like `GOTO 10` as well as using greater cognitive load to find all the steps across a file, by not enforcing an order to the way steps are read.

Terraform is another good comparison, HCL doesn't enforce a sequence, however each block usually references another. You then end up creating complex graphs in your parser to identify what needs to be run first, and what needs to be run after that.

Again, I do not disagree with Draw's assessment, but I do think we also have to recognise that the sequencing is an important part of what makes YAML so accessible, and why other similar tools struggle to be an immediate replacement for YAML.
