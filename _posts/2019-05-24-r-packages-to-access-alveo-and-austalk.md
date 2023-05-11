---
id: 2088
title: 'R Packages to Access Alveo and Austalk'
date: '2019-05-24T21:01:20+10:00'
author: 'Steve Cassidy'
layout: post
guid: 'http://alveo.edu.au/?p=2088'
permalink: /2019/05/24/r-packages-to-access-alveo-and-austalk/
categories:
    - News
---

While we’ve had a Python package to access the Alveo API for some time (pyalveo) there has not been a properly tested solution for R users until now. We’re happy to announce the release of the alveo library for R which allows R users to write code to access metadata and data from the Alveo Virtual Laboratory. The package can be found on [Github](https://github.com/Alveo/alveo-r) and can be installed directly from there with the help of the devtools package:

```
<pre class="wp-block-preformatted">> library(devtools)<br></br>> install_github("Alveo/alveo-r")
```

The library provides a range of methods to access all parts of the Alveo API from your R script. The first step is to create a client object, this will read your Alveo API Key from the file alveo.config in your home directory (see [here for help with downloading this file](http://alveo.edu.au/documentation/getting-access-to-alveo-and-galaxy/whats-an-api-key/)). This ensures that all access from your script is authorised by your own key – if you share the script, the other person will need their own API key. We can then use the client object to access the API, for example to get a list of item lists:

```
<pre class="wp-block-preformatted">> library(alveo)<br></br>Loading required package: rjson<br></br>Loading required package: httr<br></br>> client <- RestClient()<br></br>> mylists <- client$get_item_lists()
```

You can then use the library to get details of an item list, get the metadata for items in the list and then even download documents associated with each item.

## Access to Austalk

Austalk is an important collection on Alveo and since it is big and complex it can be hard to navigate to find the data you want. We’ve built some web based tools (the [Austalk website](https://austalk.edu.au/) and [Austalk Query](https://austalk-query.apps.alveo.edu.au/)) to make this easier but sometimes it is better to be able to interrogate the data from scripts more directly. If you are an R user, there is now another new library to make accessing Austalk data much easier. We’ve also been able to build in access to some parts of the Austalk metadata that were quite hard to get at any other way.

The [alveo library](https://github.com/Alveo/austalk-r) can again be found on Github and can be installed in the same way:

```
<pre class="wp-block-preformatted">> library(devtools) <br></br>> install_github("Alveo/austalk-r"
```

Once loaded there are functions to access speakers, fetch items for a list of speakers and download documents. You can also retrieve lists of prompts for each of the components in Austalk – eg. the word or sentence lists. Here are a few examples.

Here we get a data frame containing metadata for all speakers, then filter out female speakers over the age of 75.

```
<pre class="wp-block-preformatted">```
females <- merge(females, spk.items, by='speaker')
```<br></br>```
females[,c('speaker', 'age', 'digits', 'sentences')]
```<br></br>```
<em>#>   speaker age digits sentences</em> 
```<br></br>```
<em>#> 1   1_697  77     24        59</em> 
```<br></br>```
<em>#> 2   3_243  79     24        59</em> 
```<br></br>```
<em>#> 3   3_417  79     24        59</em> 
```<br></br>```
<em>#> 4   3_995  80     24        59</em> 
```<br></br>```
<em>#> 5  4_1339  79     24        59</em> 
```<br></br>```
<em>#> 6   4_341  77     24        59</em>
```
```

The components() function returns a data frame describing the different components (tasks) in the Austalk protocol. We can find the prompts for a given component. Here are the digits.

```
<pre class="wp-block-preformatted">```
prompts('digits') 
```<br></br>```
<em>#>    componentname itemid               prompt</em> 
```<br></br>```
<em>#> 1         Digits     12     oh four two nine</em> 
```<br></br>```
<em>#> 2         Digits      4   one two three zero</em> 
```<br></br>```
<em>#> 3         Digits      1   zero one two three</em> 
```<br></br>```
<em>#> 4         Digits     10   three zero one two</em> 
```<br></br>```
<em>#> 5         Digits     11 five six seven eight</em> 
```<br></br>```
<em>#> 6         Digits      9 eight five six seven</em> 
```<br></br>```
<em>#> 7         Digits      3 six seven eight five</em> 
```<br></br>```
<em>#> 8         Digits      6     two oh nine four</em> 
```<br></br>```
<em>#> 9         Digits      2     nine four two oh</em> 
```<br></br>```
<em>#> 10        Digits      8     four nine oh two</em> 
```<br></br>```
<em>#> 11        Digits      5 seven eight five six</em> 
```<br></br>```
#> 12        Digits      7   two three zero one
```
```

Then we can use the list of female speakers to locate a group of target items. Here we find the digits for these speakers and download the speaker16 WAV files associated with each of these into the local directory ‘data’.

```
<pre class="wp-block-preformatted">items <- componentItems(females, 'digits')<br></br>```
filelist <- downloadItems(items, 'data', 'speaker16'
```
```

The returned value is a list of the local files that were downloaded.

There is a more detailed vignette with the library that walks through all of these and more examples.

This is the first released version of these packages and we welcome feedback on how useful they are and any improvements we could make. Even better, we’d welcome pull requests that add new features!