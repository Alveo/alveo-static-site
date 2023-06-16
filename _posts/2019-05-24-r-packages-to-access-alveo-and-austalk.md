---
title: 'R Packages to Access Alveo and Austalk'
date: '2019-05-24T21:01:20+10:00'
author: 'Steve Cassidy'
layout: post
permalink: /2019/05/24/r-packages-to-access-alveo-and-austalk/
categories:
    - News
---

While we’ve had a Python package to access the Alveo API for some time (pyalveo) there has not been a properly tested solution for R users until now. We’re happy to announce the release of the alveo library for R which allows R users to write code to access metadata and data from the Alveo Virtual Laboratory. The package can be found on [Github](https://github.com/Alveo/alveo-r) and can be installed directly from there with the help of the devtools package:

```R
> library(devtools)
> install_github("Alveo/alveo-r")
```

The library provides a range of methods to access all parts of the Alveo API from your R script. The first step is to create a client object, this will read your Alveo API Key from the file alveo.config in your home directory (see [here for help with downloading this file](/documentation/getting-access-to-alveo-and-galaxy/whats-an-api-key)). This ensures that all access from your script is authorised by your own key – if you share the script, the other person will need their own API key. We can then use the client object to access the API, for example to get a list of item lists:

```R
> library(alveo)
#Loading required package: rjson
#Loading required package: httr
> client 
> mylists <- client$get_item_lists()
```

You can then use the library to get details of an item list, get the metadata for items in the list and then even download documents associated with each item.

## Access to Austalk

Austalk is an important collection on Alveo and since it is big and complex it can be hard to navigate to find the data you want. We’ve built some web based tools (the [Austalk website](https://austalk.edu.au/) and [Austalk Query](https://austalk-query.apps.alveo.edu.au/)) to make this easier but sometimes it is better to be able to interrogate the data from scripts more directly. If you are an R user, there is now another new library to make accessing Austalk data much easier. We’ve also been able to build in access to some parts of the Austalk metadata that were quite hard to get at any other way.

The [alveo library](https://github.com/Alveo/austalk-r) can again be found on Github and can be installed in the same way:

```R
> library(devtools) 
> install_github("Alveo/austalk-r"
```

Once loaded there are functions to access speakers, fetch items for a list of speakers and download documents. You can also retrieve lists of prompts for each of the components in Austalk – eg. the word or sentence lists. Here are a few examples.

Here we get a data frame containing metadata for all speakers, then filter out female speakers over the age of 75.

```R
females <- merge(females, spk.items, by='speaker')
females[,c('speaker', 'age', 'digits', 'sentences')]
#>   speaker age digits sentences
#> 1   1_697  77     24        59
#> 2   3_243  79     24        59
#> 3   3_417  79     24        59
#> 4   3_995  80     24        59
#> 5  4_1339  79     24        59
#> 6   4_341  77     24        59
```

The components() function returns a data frame describing the different components (tasks) in the Austalk protocol. We can find the prompts for a given component. Here are the digits.

```R
prompts('digits') 
#>    componentname itemid               prompt 
#> 1         Digits     12     oh four two nine 
#> 2         Digits      4   one two three zero 
#> 3         Digits      1   zero one two three 
#> 4         Digits     10   three zero one two 
#> 5         Digits     11 five six seven eight 
#> 6         Digits      9 eight five six seven 
#> 7         Digits      3 six seven eight five 
#> 8         Digits      6     two oh nine four 
#> 9         Digits      2     nine four two oh 
#> 10        Digits      8     four nine oh two 
#> 11        Digits      5 seven eight five six 
#> 12        Digits      7   two three zero one
```

Then we can use the list of female speakers to locate a group of target items. Here we find the digits for these speakers and download the speaker16 WAV files associated with each of these into the local directory ‘data’.

```R
file_list <- downloadItems(items, 'data', 'speaker16')
```

The returned value is a list of the local files that were downloaded.

There is a more detailed vignette with the library that walks through all of these and more examples.

This is the first released version of these packages and we welcome feedback on how useful they are and any improvements we could make. Even better, we’d welcome pull requests that add new features!
