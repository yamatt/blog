---
title: "Standard Pipeline Steps"
date: 2020-12-15T18:10:32+01:00
slug: ""
description: "What steps to run as part of your pipeline"
keywords: []
draft: true
tags: []
math: false
toc: false
---

I wanted to list out the steps of a CI/CD pipeline that I find are useful no-matter the project (almost). I'm so prone to forgetting one, and yet getting it right can be the difference between a successful project and one with a bunch of weaknesses in it.

So I'm going to list the steps that I think are important and why they're important.


## Linting
Ensure it meets coding standards

## Static Tests
Run static tests against the code

## Build
Compile the program

## Unit Tests
Run code tests

## Vulnerability Scanning
Run a vulnerability and dependency scanner like Snyk, or requires.io

## Package
Make it deployable

## Deploy
Publish the package to common locations

## Documentation Generator
Generate documentation. You might also want to publish it.
