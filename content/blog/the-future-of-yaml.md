---
title: "YAML: Out of Order"
date: 2021-07-28T18:10:32+01:00
slug: ""
description: "The Future of YAML"
keywords: []
draft: false
tags: []
math: false
toc: false
---

I did enjoy [Drew DeVault's wish-list for the future of YAML today](https://drewdevault.com/2021/07/28/The-next-YAML.html). I have to agree with all of it. YAML is terrigood.

I recall reading an article years ago (that I can't find now) comparing the YAML spec to other similar languages such as XML, JSON, etc, and whatever you pick YAML's spec surpasses any of them in terms of length. The implication being that YAML is particularly difficult to implement correctly.

But YAML is also great, and I think that is down to the syntax being highly intuitive. It's familiar to a lot of people, and in particular those familiar with Python.

One thing I think Drew over-looked though, and I'm sure there are others like Drew who would not automatically recognise this, is one really important aspect of YAML, and is why languages like TOML won't replace every case of YAML, is the inference of sequencing in a YAML file.

This becomes particularly apparent with Ansible. You cannot have an Ansible playbook without sequencing, they have a top down order to the structure. You will also find this in most CI languages such as GitLab CI and GitHub Actions -- although they are less apparent because you can also break the sequence by referring to other steps.

This inferred sequencing is not something you can do in TOML. Much like in CI pipelines you could reference other steps, but it starts to act much like `GOTO 10` as well as increasing the cognitive load on the reader to find all the steps across a file or set of files.

Terraform is another good comparison, HCL doesn't enforce a sequence, each block in most cases references another. You then end up creating potentially complex graphs in your parser to identify what needs to be the first to run, and what needs to be run after that.

Again, I do not disagree with Draw's assessment, but I do think we also have to recognise that the sequencing is an important part of what makes YAML so accessible, and if we're looking to the future of YAML this is a feature that needs to be retained.
