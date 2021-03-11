---
title: "This Blog"
imageurl: /img/this-blog-showcase.png
date: 2021-03-10T18:50:32+01:00
slug: ""
description: "Static blog using Hugo that is built using GitHub Actions."
link: https://matt.copperwaite.net
license: CC BY-SA 4.0
keywords: []
draft: false
tags: []
math: false
toc: false
---

[This blog](https://matt.copperwaite.net) is my attempt at consolidating my IT security knowledge using Agile methodology.

I had a couple of requirements:

* Cost sensitive - When it comes to personal projects I try to keep costs as low as possible
* No Analytics - I appreciate it if people read my blog, but I'm mainly writing for myself. I don't care in detail who reads it or how they interact with it.
* Minimal bandwidth costs - I don't want this blog to go down if I have the fortunate problem of becoming popular
* Static site - I knew I wanted to play with a static site generator
* Use of Content linting tools - I wanted to ensure the quality of the content of my blog by using a pipeline that measured content quality.
* Create content from mobile - So if I have a few spare minutes I can throw something together

I really enjoy this sort of thinking. It initially left me one option a public S3 bucket, however because the S3 costs are not zero I spent time thinking about it more and realised the tool that filled most of these options was GitHub Pages.

Now GitHub Pages does have its own static page generator, but after a bit of research I settled on Hugo as being the most widely used as well as being the best documented.

One thing that didn't work out was being able to edit content from a phone. It turns out all the GitHub Android apps are pretty terrible and out-dated and editing files from them isn't really possible. Ah well. Can't win them all.

That is not to say my journey in to Hugo was fun, things like using submodules in git makes me squirm, but I'm super happy with the results. I've also set it up in a way which means if I wanted to set up other blogs it would be very little effort to get it going.

## Content Quality

I used to have (or more accurately abandoned) a Twitter account after seeing the Twitter backlash and decided I didn't feel comfortable with my own writing. One of the things that concerned me is my ability to explain complex problems in a concise way. I saw a lot of people revert to blogs when Twitter didn't fill the gap, so I figured a blog was the best answer. I also wanted to minimize my own biases in my writing and wanted to be as inclusive as possible with the aim to minimise backlash. To me the only way of doing that was to bring in content quality tooling in much the same way you would bring in linters and tests to bring in code quality, seemed the best way of doing that.

After some discussions with colleagues I gathered some tooling that I wanted to incline in a CI/CD pipeline. I don't think this is the extent of tools that could be included but enough tooling to make me comfortable with writing a blog.

### AlexJS

Using GitHub Actions allowed me to inline the assessment of the quality of my content. One of the tools I chose was [AlexJS](https://alexjs.com/). I was already a little familiar with it anyway, having been referred it by a friend. AlexJS looks to improve the equality in your use of language and is super cool and it's been fascinating how it's been teaching me to adapt my language. I looked for similar products that I could also include, but I wasn't very successful.

### Make words better

Another things I did want to include was something like Grammarly to improve the understanding of the content, however as it was not open source and the API didn't seem to meet what I wanted to do I discovered GrammarBot. It still didn't integrate nicely with CI/CD pipelines, so [I wrote a wrapper](https://github.com/yamatt/python3-hemoglobin) to print human readable results.

### Reading complexity and length

The other thing I wanted to do to improve content quality was to ensure that when writing about complex topics I was not alienating anyone  and that the reading length is not too long. I really struggled to find many tools here. The one I found is a Python library called textstat, which reads plain text files and derives lots of stats about complexity. I haven't taken the time to study in detail what the numbers mean, but I figured if the numbers were at least reasonably consistent I'm probably doing OK.

However, since textstat is a library I needed to [write a wrapper](https://github.com/yamatt/python3-textstat-cli) that allowed it to be included in a CI/CD pipeline and be human readable.

The other thing I wanted to do was to ensure the reading length of the text was no more than 10 minutes. I use Firefox's Reader view quite a lot and at the top it gives you an approximate reading time. My upper bound on that is 10 minutes. It's partly a free time thing, but also I feel like if I can't explain a problem within a reasonable time-frame I need to break it out in to separate posts that explain a specific problem in more detail.

This reading length requirement is actually a really quick bit of maths to detect the number of words and then divide that by a variety of people's reading speeds. It was so quick to do I actually bundled it in to [textstat-cli](https://github.com/yamatt/python3-textstat-cli).

## Future

### Stats

One day, once I get enough posts together I will try to see what interesting stats I can find. Since I'm not using analytics I'll never be able to do that end of year blog post that my favourite blog posts do that usually discuss their most popular blog posts. But perhaps for me that will be the time I do my stats reviews.

### Comments on Posts

I did want to include comments on blog posts as a proxy for page impressions and to improve engagement. I played with using GitHub Issues as comments and as you might expect I'm [far from alone](https://github.com/krasimir/octomments) in that. However I am yet to have the time to include it.

### Link Validation

Another thing I'm thinking of doing is to also validate any links I use in my posts. If I link to something that page needs to exist, and be stored in the Way Back Machine. This is kind of harder to achieve than I was expecting, so something for another time.
