---
title: "TV Show Chart"
imageurl: /static/img/tv-show-chart.png
date: 2020-11-28T17:14:32+01:00
slug: ""
description: "Visualise the popularity ratings of TV shows from IMDb data"
link: https://yamatt.github.io/tv-show-chart/
license: AGPLv3
keywords: []
draft: false
tags: []
math: false
toc: false
---

There used to be a website that did this for you. It seemed to go away. So I decided to write some quick hacks to make my own. It is really bare minimum to get it working.

It started off being nothing good or professional about the code behind the repo. I am not a front-end person at all, other than I like doing a bit of JavaScript from time to time.

I personally prefer the IMDb popularity scores, but their API is functionally non-existent. So I wrote some Python to pull all the code together.

Originally my plan was to store the episode data objects in maybe S3 or B2 and process the data in AWS Lambdas.

However I could never get the Lambdas to complete in time and I was worried if the site became popular I would be paying for bandwidth.

I then realised I might be able to store the data in GitHub, but the data as JSON was far too big. I seem to remember reading that there is a 2Gb limit on GitHub repo sizes. So I created my own proprietary format to store the data in a more succinct way.

Recently I've been playing with static sites in GitHub and these work really well with GitHub Actions, commiting the code back to the repo.

Plus I read an article about grabbing [Covid data using GitHub Actions on a schedule](https://coviddata.github.io/coviddata/). It really made me want to revisit this work since the data hadn't been updated in months.

I also found that GitHub Actions are way more powerful that Lambdas so I could run the scripts in a matter of minutes, which was nice.

There are definitely some UX improvements I would like to make so it's possible to search for TV shows, but I need to do a bit of professionalisation first.
