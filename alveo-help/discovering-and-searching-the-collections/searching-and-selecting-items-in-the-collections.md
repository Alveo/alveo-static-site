---
id: 928
title: 'Searching and Selecting Items in the Collections'
date: '2014-07-29T15:17:33+10:00'
author: peterr
layout: page
guid: 'http://alveo.edu.au/?page_id=928'
---

The **Discover** operation screen provides a method of finding Items in the Collections which suit your research purposes. It follows a “Facet search” model which is widely used across the Internet.

You can add or remove search conditions on any of the Facets shown in the **Limit your search** control. Displayed Items will be from any of your licensed Collections, and will only be those that satisfy ***all*** of the search conditions you enter.

## **Text Searching**

[![TextSearching](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/TextSearching.png)](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/TextSearching.png)

<aside class="panel panel-default aside"><div class="panel-body">Clicking <span style="color: #3366ff;">Advanced search</span> in this search control opens a screen where you can enter an [Apache Lucene/Solr syntax search string](http://lucene.apache.org/core/2_9_4/queryparsersyntax.html). There are comprehensive instructions linked from that Advanced Search page.</div></aside>You can enter complex search conditions in the <span style="color: #999999;">**Search Text Containing…**</span> box, including combining word searches with **<span style="color: #993300;">AND</span>** or **<span style="color: #993300;">OR</span>**, using brackets **<span style="color: #993300;">()</span>** to group terms, and using **<span style="color: #993300;">NOT</span>**. For example, **<span style="color: #993300;">(cat OR dog) AND NOT mouse</span>** will find Items with text documents which contain either of the words “cat” or “dog”, and which do not contain the word “mouse”. (The logical operators do not need to be upper case. This is just for clarity in this description.)

You can put double quotes around strings to search for that exact string. For example, <span style="color: #993300;">**“don’t give up”**</span> will search for exactly that phrase. If you want to search for the words “and”, “or” or “not”, you will also need to put double quotes around them.

You can also use wildcards, such as **<span style="color: #993300;">c?t</span>**, which finds “cat”, “cut”, “cot” etc, or **<span style="color: #993300;">c\*t</span>** which in addition finds words like “cart”, “coat”, “chat”, “cheat”, “chalet”, “castanet” etc. More complex strings with multiple **<span style="color: #993300;">?</span>** or <span style="color: #993300;">**\***</span> markers, or specifying more characters are also possible. For example, **<span style="color: #993300;">gre\*</span>** means all words staring with the letters “gre”, such as “great”. **<span style="color: #993300;">g?e?t</span>** or **<span style="color: #993300;">g??at</span>** will also match “great”. These tests are not case sensitive.

## **Searching by Facet**

![SearchSelection](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/SearchSelection.png)

The search results are updated each time you click a Facet value.

## **Search Results and Refining the Search**

You can remove search conditions and add new search conditions based on other Facets until you have the Item List you require.

[![Searches](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/Searches.png)](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/Searches.png)

Each time you refine your search list, the displayed list of matching Items will be updated.

When you are happy with the list of Items that your search has found, you should proceed to [Saving Your Search Results to an Item List](http://alveo.edu.au/help/discovering-and-searching-the-collections/saving-your-search-results-to-an-item-list/ "Saving Your Search Results to an Item List").