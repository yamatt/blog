---
title: "Is Public Wi-Fi More Secure Than Personal VPN Services?"
date: 2021-08-13T18:10:32+01:00
slug: ""
description: "Challenging commonly held wisdom"
keywords: []
draft: true
tags: []
math: false
toc: false
---

An IT security group I associate with recently wrote a blog post on [threats and scenarios for securing mobile phones](https://joelgsamuel.medium.com/how-to-keep-your-smartphone-safe-from-spying-d7d50fbed817). It's well worth a read.

One line stood out to me as interesting because I wanted to understand the evidence for that. It _feels_ true, but that's not the same as _being_ true.

That Greg is...
<!--alex ignore he-she-->
> more likely to select a malicious VPN provider than he is to run into malicious Wi-Fi

Speaking to the authors the answer was more anecdotal than quantifiable based upon the lack of reports on malicious public Wi-Fi in recent years and the number of reports of malicious personal VPN providers, although the stated example was a Tor exit relay re-writing bitcoin addresses on the fly.

Tor being different in both ways of working and economic incentives so I'm going to exclude it from exploring further.

Even so there are [plenty of examples](https://www.theregister.com/2020/07/17/ufo_vpn_database/) of personal VPN services leaking logs, however [that doesn't make those services more, or indeed less, secure than they are now](https://matt.copperwaite.net/blog/assessing-security-practices-of-3rd-party-projects/).

While public VPN services are not a new concept, they have [become more prominent in the last 5-6 years](https://trends.google.co.uk/trends/explore?date=all&geo=GB&q=%2Fg%2F11gfj_yxtn,%2Fg%2F11hbgq8gct,%2Fg%2F11b7y71slf). Conversely using public Wi-Fi has been [a concern for many people for far longer](https://www.theregister.com/2007/08/02/public_wifi_hack/) but with phone 3G and up being more common place this would mean its usage is  likely lower. However, evidence for this and 'hacks' on public WiFi service having significant effects in the real world are hard to track down. The reasons for this are either because it rarely happens, or rarely gets identified.

## Comparisons

The core of the question here is, are you more likely to use a public WiFi that has a vulnerability that could do you harm, or a personal VPN service that has a vulnerability that could do you harm.

Part of the complexity in answering this is that we're comparing apples and oranges. You can tell through a logic test, that you can run a VPN over public Wi-Fi but not the other way around. This dissimilarity makes comparing risks difficult and the only reasonable way to measure it is through qualitative thought experiments.

For clarity a _public [WiFi](https://en.wikipedia.org/wiki/Wi-Fi) service_ is any wireless network with an internet connection provided by a company in a public space. This means coffee shops such as [Starbucks](https://wifi.starbucks.com/) but does not include corporate Guest WiFi that you might find in a workplace. A _public WiFi provider_ is the company that provides that WiFi service.

Whereas personal VPN services are a kind of internet service provider that supplies internet access via a [Virtual Private Network](https://en.wikipedia.org/wiki/Virtual_private_network) and is aimed [directly at consumers rather than businesses](https://en.wikipedia.org/wiki/Direct-to-consumer). A personal VPN provider is a company such as NordVPN or ExpressVPN that run these services.

### Economic Incentives for Security

To start with lets look at the reasons a company might run one of these services as the economic models for public WiFi services and personal VPN services are quite different. Using Behavioural Economics we can identify constraints and motivations for running it.

Personal VPN services have a very traditional "quid pro quo" subscription model, this means that those who tout their services as improving security have a specific interest in you having secure system, or they would be out of business. It doesn't mean it won't happen, but they are incentivised to make it secure, in the same way cloud providers are.

The payment model for public WiFi services is more complex. Coffee shops and libraries are widely regarded as a place to get free WiFi. The payment model is indirect. In coffee shops you are paying for your WiFi as a portion of the food and drink you purchase. The WiFi encourages you to choose that venue over other similar venues, and the act of you staying there means you spend more on food and drink. You can infer therefore, that a coffee shop or library is more interested in providing it as a lowest cost service. It's not going to harm their business as much if there's malware flying around the network.

Sometimes public WiFi providers up-sell you to improve your service such as speed, or amount of data, or amount of time for a fee, but this I would be very surprised if this is taken up.

### Security Considerations

I wanted to address some of the good, although patchy and inconsistent work that personal VPN providers do on security of their services. WiFi providers, as mentioned, don't have the same incentives to provide this information.

[Some personal VPN services do bring in auditors for their code](https://www.pcmag.com/news/what-does-a-vpn-security-audit-really-prove), which is good as long as you trust the audit, but also comes with the caveat that the audit covers the code for a particular point in time. [Some also have vulnerability reporting incentives](https://hackerone.com/nordsecurity?type=team).

A thing to consider is that personal VPN service typically requires you to download and install potentially untrustworthy applications on to your machine to gain access to their services.

### Discoverability

The final part really is discoverability. This is your likelihood of accessing a personal VPN service vs a public WiFi service.

<!--alex ignore virgin-->
A personal VPN service would typically be a one-to-one relationship between consumer and business. Where as there are a lot of public WiFi providers. In the United Kingdom public WiFi services are usually from big telecoms providers such as [Virgin Media](https://tfl.gov.uk/campaign/station-wifi), [BT](https://www.btwifi.co.uk/) and [Sky](https://www.sky.com/wifi), but they could also in a smaller shops be an ad-hoc PSK posted on a wall, or printed on a menu. You may use several in a year (or used to). However a personal VPN service can be accessed from anywhere at any time.

I think it's also a likely scenario that if you were new to personal VPN services you would probably [perform a search for the best providers](https://www.techradar.com/uk/vpn/best-vpn) which is really a list of affiliate links and the one at the top probably gives the author the largest share of the referral fee, but you might not choose the top one because they're the most expensive, so maybe the 5th one? Then at some point down the road that company isn't doing so well and gets bought out by someone not so reputable, and [sunk cost fallacy](https://en.wikipedia.org/wiki/Escalation_of_commitment) says you're going to stick with it anyway.

## Moot Points

There are some security considerations that both public WiFi services and personal VPN services share. It's worth drawing those out here as some may see them as one providing an advantage of one over another.

### HTTPS

The [vast majority of web traffic is now HTTPS](https://blogs.vmware.com/networkvirtualization/2020/09/network-security-encrypted.html/) which means you are less likely to have your traffic changed in some way, but it is still likely that the providers can see meta data about your traffic. Typically you provide a public WiFi provider some information about you on sign-up, although I rarely see that being verified. A personal VPN provider can probably tell who was accessing what because you've presumably provided them some payment details, although I'm sure some more privacy minded folks might pay via a crypto currency.

### Further Monetisation

I have no doubt that large public WiFi providers monetise your traffic by taking meta data and selling that on. While some VPN providers claim they don't, if you're looking to make cost savings and choosing a cheaper provider I would count on them doing that.

### Data Leaks

Both [public WiFi services](https://www.bbc.co.uk/news/technology-51682280) and [personal VPN services](https://www.teiss.co.uk/free-vpn-apps-leaked-personal-data/) have leaked personal data in the past. I expect it will happen again. It's the nature of IT, as mentioned though I don't think it's necessarily a reflection of the current IT practices of those services.

## Conclusion

Like most answers in IT security, it really depends on your circumstances. [Tom Scott does (like always) provide a fantastic summary of why you might want to use a VPN](https://youtu.be/WVDQEoe6ZWY) and I completely agree, while [Troy Hunt has a less than unbiased view on why you should use NordVPN](https://www.troyhunt.com/im-partnering-with-nord-as-a-strategic-adviser/).

What this demonstrates is it is not a straight-forward answer, even for technically minded people. There are a lot of ways to get it wrong. Then there is your standard IT security line that the more you pay the more secure something is -- to a point.

That means if you're in a position to use a personal VPN services, given the amount of choices you may choose one that doesn't meet all your security needs. Whereas public WiFi services are less frequently used and have a larger surface area, and where they are most used they are run by large reputable companies.

So it seems like public WiFi services are probably less malicious than some or all of the personal VPN services, but a huge aspect of that is exposure.
