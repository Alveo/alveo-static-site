---
title: 'Report from SocioPhonAus 2016 Brisbane'
date: '2016-07-13T00:35:30+10:00'
author: 'Steve Cassidy'
layout: post
permalink: /2016/07/13/report-from-sociophonaus-2016-brisbane/
categories:
    - News
tags:
    - austalk
    - speech
---

I was invited to give a presentation on Alveo and Austalk at [First workshop on Sociophonetic Variability in the English Varieties of Australia](https://www.griffith.edu.au/conference/sociophonaus2016) held at Griffith University in Brisbane in June. The workshop, organised by Gerry Docherty and Janet Fletcher, was supported by the [Centre of Excellence for the Dynamics of Language](http://www.dynamicsoflanguage.edu.au) was attended by phoneticians from around the country with a keynote given by Prof. Jonathan Harrington who flew in from Munich.

The program included a number of interesting talks about the minutiae of Australian English with a few excursions into other varieties. Many of the talks included mention of the use of the Austalk corpus, a collection of 900 speakers of Australian English that is available through Alveo. Researchers used data from Austalk to look at changes in vowel production in different populations around the country; Austalk is ideal for this kind of study as it contains large samples from most major cities and significant data in other areas too. It’s great to see that researchers are starting to get real results from the data we collected.

In my presentation on Austalk and Alveo I was able to provide an update on the status of the collection and publication of the Austalk data which I’ll summarise here.

Austalk was funded in 2011 and data collection was a major logistical undertaking involving 13 Black Box recording studios shipped around the country. While most of the data collection was done in 2011-12 we were still finalising some recordings in 2015 and have only recently got all of the data safely stored on our central server. For this reason, the version of Austalk that is available in Alveo is a snapshot from 2014 of the data that was finalised at that time. We are now in a position to process the whole of the data and do a new upload to Alveo to make it all available to researchers. We now have around 35T of data including 4T of audio from around 900 speakers. We are waiting on a couple of external factors relating to storage of data but we hope to be able to update the Austalk collection in Alveo before the end of August this year.

I tried to clarify the different ways that researchers can access Austalk:

- [The Austalk Website](https://austalk.edu.au) (austalk.edu.au) was built to support data collection and recruitment of speakers, for project members there are some reports there on the status of data collection but no easy way to access the data. This site will be retired soon and be superseded by:
- The [new Austalk Website](http://bigasc.edu.au) (bigasc.edu.au) which was designed to hold information about the collection in the longer term and provide some access to data. Registered users of this site can browse the data by recording site, speaker and components and preview recordings in the browser.
- [Alveo](https://app.alveo.edu.au/) is the long term platform to get access to data from Austalk, the resources of Alveo allow searching the metadata and downloading subsets of the data via the API. We are working to build better tools to make the data more easily available, for example the[ Austalk Query](http://austalk-query.apps.alveo.edu.au/) web tool.

We also discussed making the [ANDSOL](/andosl) collection available through Alveo. ANDOSL is an earlier collection of Australian English collected in the 1990s and currently managed by the [Australasian Speech Science and Technology Association](http://assta.org) (ASSTA). We hope to be able to find the resources to ingest this collection in the near future. This would be a great resource for research on the changes of Australian English since along with the Mitchell and Delbridge collections this gives three snapshots taken over a fifty year period.

There was also a lot of discussion about the kinds of tools that would be useful for Alveo to support relating to speech data. I described our work on the Galaxy workflow engine and we discussed the kinds of tools that might be useful made available in this way. Examples were:

- Forced alignment, eg. using [MAUS](https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html)
- Feature extraction – MFCC, formants, pitch tracking, harmonics
- Acoustic segmentation – eg. speaker segmentation, speech/non-speech/music detection

We will be working on some of these in the near future and encourage anyone with an interest in being able to work with speech data from Alveo to get in touch and help define what these tools should do. One of my own goals is to be able to easily generate a vowel formant plot for any speaker from Austalk by finding the hVd words, running forced alignment, then the formant tracker and finally plotting the vowel formants at the midpoint.