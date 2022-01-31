---
title: "Analysing the Value of Web Certificates"
date: 2022-01-31T18:10:32+01:00
slug: ""
description: "Something Something Let's Encrypt"
keywords: []
draft: true
tags: []
math: false
toc: false
---

Stargrave provides a blog that I often read. I did enjoy my recent read of "[Why I won't use Let's Encrypt](http://stargrave.org/WhyNotLE.html)". I think it's a really interesting and powerful analysis of when encryption doesn't work in your favour. I think the conclusions are wrong, and that's ok. We all have different experiences and context that will lead us to different conclusions. Working in isolation also leads us to biases and blind-spots which are really hard to identify.

Which is why it's so interesting to delve in to this article in particular to see if they hold up to scrutiny.

I will say I'm having to make a lot of assumptions about the environment that Stargrave has to work in. One of them is his location and I think this is a big contributing factor to his decision making. However at a cursory glance I cannot see any specific reference to a country and can only derive that information based upon the language used, which when thrown in to Google Translate says is Russian. Stargrave could well be a Russian speaker anywhere in the world so it's not a certainty that he is based in Russia, but it's likely enough for an assumption.

This will have an understandable colouring on his up-bringing the material he is exposed to and therefore outlook, and this is important. A lot of encryption technology has come out of the US, a long-standing adversary of Russia, and historically encryption has been linked back to intelligence services who are somewhat motivated to break encryption. Some examples of this include the [PGP export law](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States#PC_era) and [A5 encryption used in GSM mobile devices](https://en.wikipedia.org/wiki/A5/1#History_and_usage). Lets not forget the actions of intelligence services does not engender trust in their actions. Something I think does need to be recognised as [being improved upon](https://www.troyhunt.com/open-source-pwned-passwords-with-fbi-feed-and-225m-new-nca-passwords-is-now-live/).

I'm not blowing anyone's minds here, but this backstory I think is important when challenging both Stargrave and my own assumptions about the adoption of certificates on the web.

Stargrave helpfully summarised his article at the end. This is where I want to start breaking down, although to save on verbiage I'm going to do them out of order.

I also want it clear that this is about having a dialogue. I'm not saying Stargrave or myself are right. It's the exercise that is interesting.

## "tarballs and Git tags are validated anyway by OpenPGP signatures"

The point behind this was that Stargrave's VPS provider, where the blog is run from, has access to the disk, making the public and private keys are stored in plain text on the disk. Meaning anyone could grab them and decrypt the traffic. Whereas his code is signed using PGP which has the certificates stored on his machine.

There's a lot to go in to here. Unless someone proves me wrong I don't know of any VPS providers who encrypt the disk. Cloud providers do, as much as you can also trust them, but you are talking, in the main, about 3 large US providers. There is of course other problems there that we'll touch in the next section.

One thing to note is that Stargrave's blog is not signed using OpenPGP. The same motivated attacker who could take your certificate private keys could right now post a new blog post through the same route saying your PGP keys have changed and that the codebase has moved - possibly due to a now very real, malicious attack.

There has to be an aspect of pragmatism if you're not hosting your own services, and even if you are you are likely beholden to an ISP who have ultimate say over your traffic. You have to trust someone somewhere, and if you don't trust your VPS provider with your private keys you need to find another provider, because if you believe they are capable of breaking your encryption they are capable of a lot more.

## "LE is definitely a NOBUS"

It's worth a brief introduction to the term NOBUS as it was a new one to me:

>  term used by the United States National Security Agency (NSA) to describe a known security vulnerability that it believes the United States (US) alone can exploit.

The implication being that Lets Encrypt is in some way able to be exploited by the US government. It's impossible to prove or disprove.

There's no doubt that laws like the [PATRIOT Act](https://en.wikipedia.org/wiki/Patriot_Act) do make this kind of thing more scary. With at least theoretical access to your data.

However looking at the history of Lets Encrypt - which is started by both Mozilla and in particular the Electronic Frontier Foundation, both of which hold data privacy in high regard and are regularly critical of government over-reach it seems unlikely that there is much validity to the NOBUS claim.

But then what is the data your protecting? A blog - which is public. Open Source Code - which is public.

Not using Lets Encrypt on these grounds seems like a biting conclusion - but the foundation of it is weak at best.

## "do not be conducted with security theatres and deceitful assumptions." [sic]

I think this is a great point. Stargrave's post could just as easily be a conspiracy to discourage people to use encryption as much as Lets Encrypt is a conspiracy to control people's access to content.

You need weighed, balanced, and transparent decision making to create a healthy security environment. Many governments across the world do not encourage this discourse.

## My Thoughts

I do think there is an argument to say. Why bother? Most of my online activity is public and where I don't want it to be, such as buying stuff online or banking it is protected.

However that doesn't mean that there isn't someone out there who wants to view what I put out securely, because their government disagrees with my message. Or it can be used as a fishing exercise to identify those who are innocent.
