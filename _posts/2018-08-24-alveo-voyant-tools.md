---
title: 'Alveo and Voyant Tools'
date: '2018-08-24T20:23:57+10:00'
author: 'Steve Cassidy'
layout: post
permalink: /2018/08/24/alveo-voyant-tools/
categories:
    - News
    - Screencast
---

I’d like to preview a new feature under development in Alveo which is an integration with the excellent [Voyant Tools](https://voyant-tools.org/) for text analysis. Voyant includes a wide range of tools to explore text collections from word-clouds to concordances and network graphs. This extension to Alveo allows the owner of a collection to enable Voyant analysis. This is a simple process for the collection owner and once completed, means that any Alveo user who has permission to access the collection will be able to get access to it in Voyant.

The video below demonstrates the current implementation of this facility. It starts by creating a new collection and adding a number of texts uploaded as a zip file. We then enable the collection in Voyant. The effect of this is to send all of the texts to our Voyant server as a custom collection. When this is complete, users can access the collection in Voyant via a button on the Alveo collection page.



We still have some work to do on this, in particular we need to implement the appropriate password protection so that collections that are available through Voyant have the same level of protection as collections on the main Alveo system. We plan to have that completed soon and following further testing will make this option available for all Alveo collections.