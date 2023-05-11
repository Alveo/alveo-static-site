---
id: 1597
title: 'Accessing Austalk in Alveo'
date: '2015-11-18T16:57:03+11:00'
author: aidan
layout: page
guid: 'http://alveo.edu.au/?page_id=1597'
---

[Austalk](http://bigasc.edu.au/) is a large collection of spoken Australian English collected in the last few years at sites around Australia. When the collection is complete it will have close to 1000 speakers each with a range of recordings from isolated words to interview and map task recordings. Alveo contains most of the data and will have the complete corpus when collection and data processing is complete.

You can browse the data via the default discovery interface (eg. [here](https://app.alveo.edu.au/?f%5Bcollection_name_facet%5D%5B%5D=austalk)) but since there is a lot of data (622520 items) and since the facets in the discovery interface don’t match up very well with the Austalk metadata, it is hard to find your way through the collection like this. We are working on better ways to present the data, this blog post is intended to give some ideas about how to make use of Austalk data right now.

## Finding Annotated Data

A subset of the speakers have had some data annotated by hand. Annotations are contributed back by researchers as [Annotation Contributions](https://app.alveo.edu.au/contrib/) and you can find a list of the contributions relating to the Austalk collection on that page. Each contribution page links to the individual files that have been uploaded and also contains a button that will allow you to download both the annotations and the original audio files.

## Using Metadata

If you look at that example of ‘tangerine’ you’ll see on the item page that you can play the audio but also that there is a list of metadata for that item. This gives us a way of further narrowing down the search: each of these metadata terms can be used in a query. So if I want to find all examples of this word I look down the metadata list and see that the field ‘prompt’ has the value ‘tangerine’ . I can go back to my search results and click on “Search Metadata” in the left hand menu, then enter the search “prompt: tangerine” and click the magnifying glass button to run the search. You should now see 8 instances of this word by three different speakers.

Similarly, I could find all recordings for one speaker with “speaker: 1\_1308” or all digit recordings with “componentName: digits”. Any of the metadata fields can be used in a search like this. We even provide a separate page for [Advanced Search](https://app.alveo.edu.au/catalog/advanced_search) which has some links to help you formulate queries – they can actually be quite complex if you’re up to it. Here’s one that finds all of the sentences by this speaker:

```
collection_name:austalk AND componentName:sentences AND speaker: 1_1308
```

## Make an Item List

Once you have found an interesting set of data you probably want to do something with it. The next step is to save your search as an [Item List](http://alveo.edu.au/alveo-help/discovering-and-searching-the-collections/saving-your-search-results-to-an-item-list/), which is the starting point for further analysis. Click on “Add all to List” and give your new list a name that will help you remember what it contains. Item lists will be saved with your account so you can reference them later and you can share them with others if they contain interesting collections of items.

Once you have an item list you can download all of the data for each item as a zip file. Note that if your item list is large, this may take a while. For Austalk this means you will get all of the audio channels for each item – we’re working on an interface to allow you to select just one channel (you probably want channel 6 which is the headset microphone). This will also download the TextGrid files which you can then use locally in Praat or Emu to begin your analysis.

We’re working on an interface to Emu that will make it easy to download an item list and begin working with the annotated data – watch this space for news (or contact Steve Cassidy if you can’t wait).

## A Better Search Interface

We’re aware that this is not the easiest way to find data so we’re working on a better search interface for Austalk data in Alveo. You can see a prototype of this interface here: [austalk-query.](http://austalk-query.apps.alveo.edu.au/) To use this you need to get your [Alveo API key](http://alveo.edu.au/alveo-help/getting-access-to-alveo-and-galaxy/whats-an-api-key/) and enter it in the first page.

This interface first lets you find speakers that you are interested in using speaker metadata, so you can look for males over 50 from Melbourne if you wish. From this list of speakers you have the option of getting all of their items or narrowing down the items you’re interested in. Click on “Search Items” and you’ll see a form that allows you to search by prompt (the text read by the speaker) or component name (words, digits etc) or select from a few pre-defined lists like hVd words. Click on search and you should see (after a short delay) a list of items that match your search – these are only those from your selected speakers. Once you have this list you have the option of saving it as an Alveo item list; do this and you can download it as described above.

## The Future

I hope this has been a useful introduction to getting your hands on Austalk data through Alveo. If you’re a speech person, the same techniques (apart from the last one) will work for Mitchel &amp; Delbridge collection which has forced-aligned annotations for all of the read speech.

We’re aware that this is not the optimum way to access this data and welcome suggestions on how to improve it. We’re working on implementing a better query system and integrating tools like Emu/R directly with Alveo to facilitate research using Austalk. We hope to add new annotations generated by forced alignment for a wider range of data – things can only get better.