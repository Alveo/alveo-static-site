---
title: 'Using Voyant Tools'
date: '2018-11-16T13:58:19+11:00'
author: 'Steve Cassidy'
layout: help
order: 5.5
---

[Voyant](http://docs.voyant-tools.org/) is a web based text analysis platform. Data uploaded to a Voyant Tools server can be analysed and visualised in a number of different ways to provide insight into the texts. While it is possible to upload data to a public Voyant Tools instance for analysis, the data then becomes public by default (although there are ways to protect it) and you are creating yet another copy of your dataset that needs to be managed.

To facilitate the analysis of text data stored on Alveo, an instance of Voyant Tools is available as part of the Alveo platform and any text collection stored in Alveo can be made available for analysis on Voyant. The advantage of this approach is that users don’t need to create new copies of data to upload to Voyant and, importantly, collections are protected by the same user permissions as the rest of the Alveo platform. Users who have not agreed to the licence terms for a collection or been granted access to it cannot access the collection via Voyant Tools.

The data owner of a collection must configure Voyant integration for their collection. Once that is done, any user with access to the collection can get easy access to the collection in Voyant.

## Configure Voyant for a Collection

As the data owner, visit the collection page for your collection (Click on your collection from [the main collections page](https://app.alveo.edu.au/catalog/)). There you will see a button at the right of the page to configure Voyant.

![](/assets/files/2018/11/Screenshot_2018-11-16-Alveo-1-1024x225.png)

Click on this button and you will be see the following form:

![](/assets/files/2018/11/Screenshot_2018-11-16-Alveo1-1024x683.png)

![](/assets/files/2018/11/Screenshot_2018-11-16-Alveo2-1024x979.png)

This form asks you to select which files form your collection will be sent to Voyant. Here you need to select the files from each item that contain data that can be analysed by Voyant Tools. This will typically be a plain text version of the item but Voyant is also able to understand other file formats such as HTML, PDF and Word. If you want to select the text files, enter a pattern to match them such as \*.txt and click \[Preview\] to see the list of files selected.

In some cases you might want to select only some of the text files in the collection, for example if each item has both a plain text and a marked up text version. Then you could use a pattern such as \*-plain.txt to match only those files.

Once you are happy with the collection of files selected, click on \[Confirm\] and these files will be packaged and sent to Voyant Tools and the appropriate controls put in place to make this data available to collection users. When you re-visit your collection page after the configuration is complete, you will see the following text:

![](/assets/files/2018/11/Screenshot_2018-11-16-Alveo3-1024x88.png)

Users can now click on the “Go to Voyant Tools” link and be taken directly to the Voyant Tools server with this collection loaded.

![](/assets/files/2018/11/Screenshot_2018-11-16-Voyant-Tools-1024x571.png)

Refer to the [Voyant Tools documentation](http://docs.voyant-tools.org/) for information about how to use Voyant to analyse your text.