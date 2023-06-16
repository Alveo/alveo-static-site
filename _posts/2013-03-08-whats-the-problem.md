---
title: 'What&#8217;s the Problem?'
date: '2013-03-08T01:03:09+11:00'
author: 'Steve Cassidy'
layout: post
categories:
    - 'User Requirements'
---

One of the first things we developed on the project is a *problem statement*. This is intended as a high level summary of the problem we’re trying to solve in building the HCS Virtual Laboratory. I thought I’d present our current problem statement here and provide a bit of a commentary.  
  
 Here’s the problem statement in the semi-formal language of the Agile software development methodology:

| The problem of |
|---|
| a lack of awareness, access and proficiency in the use of the full range of corpora, tools and techniques available to researchers of the diverse disciplines that constitute the human communication science research field |
| affects |
| researchers whose research is based on quantitative and qualitative studies using samples of human communication data; |
| the impact of which is |
| - research studies are limited to a subset of the range of corpora and tools available, and interdisciplinary research studies are not occurring as much as possible - sharing of datasets not occurring as much as possible and researchers are collecting new data when existing datasets could potentially be used |
| A successful solution would |
| - support the discovery of new research opportunities, in particular by broadening access to tools and corpora and enabling interdisciplinary approaches - help make HCS research more efficient, more collaborative and more easily reproducible |

Taking the second part first, we try to describe the audience for the Virtual Laboratory. This is quite broad since we span disciplines from Computer Science, Psycholinguistics and Phonetics to Music and Sociolinguistics. The common thread is that our users work with samples of human communication data – primarily samples of language use but since we have music researchers involved, we also have users interested in samples of musical performance. The range of research carried out on this data also varies from heavy statistical analysis of very large quantities of data to small scale qualitative studies of the use of a particular word or grammatical construct.

The problem we’ve identified is also a side effect of the breadth of disciplines that make use of this kind of data. While the kinds of data are similar in many cases (text, audio, video), the tools that are used with this data have evolved within each discipline and are not well known outside of the disciplines themselves. So for example, a researcher in Acoustic Phonetics might use [Emu](/) to perform acoustic analysis on speech data unaware of the package [PsySound](http://psysound.wikidot.com) developed for Psycho-acoustics research which can process the same kinds of data and possibly provide a useful transformation that hadn’t been tried before in this domain. These tools use different platforms and make different assumptions which creates a barrier to their integration. One of our goals is to reduce these barriers where possible to enable researchers to explore beyond their traditional discipline boundaries.

A similar situation exists with the source data that we use in Human Communication Sciences. There are many corpora that have been collected to support research in one discipline that might provide a useful resource in a different area. Our goal is to provide a uniform platform for storing and searching these collections so that any researcher can discover interesting data and apply whichever tools are relevant to the analysis of that data. This might make some of the large text collections used in search engine research available to the Linguist searching for examples of a particular grammatical construct or a corpus of video interviews collected for socio-linguistic research available to researchers evaluating audio-visual speech recognition algorithms.

We hope that a successful solution to this problem will provide a useful resource to further the research goals of the broad range of disciplines that make up the Human Communication Sciences.