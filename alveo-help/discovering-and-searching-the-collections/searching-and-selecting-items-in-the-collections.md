---
title: 'Searching and Selecting Items in the Collections'
date: '2014-07-29T15:17:33+10:00'
author: peterr
layout: help
---

The **Discover** operation screen provides a method of finding Items in the Collections which suit your research purposes. It follows a “Facet search” model which is widely used across the Internet.

You can add or remove search conditions on any of the Facets shown in the **Limit your search** control. Displayed Items will be from any of your licensed Collections, and will only be those that satisfy ***all*** of the search conditions you enter.

## **Text Searching**

[![TextSearching](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/TextSearching.png)](/assets/files/2014/07/TextSearching.png)

Clicking Advanced search in this search control opens a screen where you can enter an [Apache Lucene/Solr syntax search string](http://lucene.apache.org/core/2_9_4/queryparsersyntax.html). There are comprehensive instructions linked from that Advanced Search page.

You can enter complex search conditions in the **Search Text Containing…** box, including combining word searches with **AND** or **OR**, using brackets **()** to group terms, and using **NOT**. For example, **(cat OR dog) AND NOT mouse** will find Items with text documents which contain either of the words “cat” or “dog”, and which do not contain the word “mouse”. (The logical operators do not need to be upper case. This is just for clarity in this description.)

You can put double quotes around strings to search for that exact string. For example, **“don’t give up”** will search for exactly that phrase. If you want to search for the words “and”, “or” or “not”, you will also need to put double quotes around them.

You can also use wildcards, such as **c?t**, which finds “cat”, “cut”, “cot” etc, or **c\*t** which in addition finds words like “cart”, “coat”, “chat”, “cheat”, “chalet”, “castanet” etc. More complex strings with multiple **?** or **\*** markers, or specifying more characters are also possible. For example, **gre\*** means all words staring with the letters “gre”, such as “great”. **g?e?t** or **g??at** will also match “great”. These tests are not case sensitive.

## **Searching by Facet**

![SearchSelection](/assets/files/2014/07/SearchSelection.png)

The search results are updated each time you click a Facet value.

## **Search Results and Refining the Search**

You can remove search conditions and add new search conditions based on other Facets until you have the Item List you require.

[![Searches](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/Searches.png)](/assets/files/2014/07/Searches.png)

Each time you refine your search list, the displayed list of matching Items will be updated.

When you are happy with the list of Items that your search has found, you should proceed to [Saving Your Search Results to an Item List](/help/discovering-and-searching-the-collections/saving-your-search-results-to-an-item-list "Saving Your Search Results to an Item List").