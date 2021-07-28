---
title: "Backblaze B2 Upload File GitHub Action"
imageurl: /img/b2-upload-action.png
date: 2021-07-28T18:50:32+01:00
slug: ""
description: "A GitHub Action to upload files to a Backblaze B2 bucket"
link: https://github.com/marketplace/actions/backblaze-b2-upload
license: AGPLv3
keywords: []
draft: true
tags: []
math: false
toc: false
---

[This started this project](https://github.com/yamatt/backblaze-b2-upload-action) because I had another project that needed to upload files straight to Backblaze B2. I guess you could use the S3 GitHub Action and point it at your Backblaze bucket, but I forgot and figured I could solve it this way.

I forked [Wilson's B2-setup Action](https://github.com/wilsonzlin/setup-b2), figuring I could apply another layer to then just upload the file based on arguments, and save me a bunch of effort because Wilson had already figured out how to get the B2 CLI working on all OS available in GitHub Actions. Although I ran in to a few problems.

One was that the B2-setup action does not have a license. Meaning it was copyrighted and I had concerned about extending the code base. I still worked in the fork, which looks weird, but if you look at the commit history I actually almost started again and built my action using Docker.

The other issue was I had difficulties getting the input arguments to work and the project needed the dependencies built in to the package and it was all starting to get complicated. I then used the [cURL Action](https://github.com/enflo/curl-action) as inspiration to use Docker.

I suspect Docker runs are slower as it looks like it builds the docker image before running, it also only runs on the Linux images. It does work though so that's what I've got for now.

I released a V4 based upon the release cycle from Wilson's code, but then when adding the action to the marketplace I had to create a new release as I couldn't work out how to delete the v4 tag in the GitHub interface. So for no reason v4 isn't used and v5, which is identical is the published version.

I am very pleased with the icon.

I licenced this one under AGPLv3, unlike my [other GitHub action](https://matt.copperwaite.net/showcase/scaleway-serverless-action/). I was reminded of the purpose of AGPLv3 and in the case of an Action I would expect it only mattered if someone changed this action for some reason.
