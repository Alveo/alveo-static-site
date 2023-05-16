---
title: 'Alveo Data Structures'
date: '2014-07-18T12:29:44+10:00'
author: peterr
layout: help
---

## **Three-level hierarchy**

Alveo allows access to a large body of data. In order to facilitate access to this data it is organised in a three-level hierarchy of [Collections](http://alveo.edu.au/alveo-help/alveo-data-structures#collections), [Items](http://alveo.edu.au/alveo-help/alveo-data-structures#items-in-a-collection) and [Documents](http://alveo.edu.au/alveo-help/alveo-data-structures#documents-in-an-item).

| **Collections**

A Collection has a single owner.  The information in a Collection is for a related purpose or reason.  A Collection may be large or small.  Each Collection has Metadata associated with it.  

 | **…each Collection contains many…** | **Items**

Items within a Collection relate to the same communication event.  Each Item has Metadata associated with it.  

 | **…each   Item contains many…** | **Documents**

Documents are like files of data.  Documents within an Item are related closely.  Documents can be of various forms, such as video, audio, text etc.  

 |
|---|:-:|---|:-:|---|

## **Collections**

Collections group data with a similar purpose or origin. For example:

- The AustLit Collection of Australian Literature (short name “austlit”), which dates from 1795 to 1930.
- The Audio-Video Australian English Speech Data Corpus (short name “avozes”), which includes audio-visual material.
- Australia’s contribution to the International Corpus of English, which is ICE-AUS (short name “ice”), dated 1992 to 1995.

…and many more.

#### Collection Metadata

There are Metadata associated with Collections. Although they are not directly searchable in the Alveo web interface (unlike Item Metadata), they can be viewed as the Collection Details. (See [Browsing the Collections](/alveo-help/discovering-and-searching-the-collections/browsing-the-collections)).

#### Collections are Licensed

Collections are licensed for use, with licence conditions that may be of critical importance in some cases. They often restrict the ways you can use the data. For example, in many cases you are only permitted to use the data for research purposes. **It’s important that you are aware of the licence conditions of the collections that you use.**

To review and accept licences for a Collection you wish to use, see [Accepting Licences to Access Collections](/alveo-help/getting-access-to-alveo-and-galaxy/accepting-licences-to-access-collections). You will not be able to access the Collection until you have done this.

When you first get access to Alveo, you will have no Collection licences and so will not be able to do any useful operations until you access the [licensing screen](/alveo-help/getting-access-to-alveo-and-galaxy/accepting-licences-to-access-collections "Accepting Licences to Access Collections").

#### Viewing Collections

To view a summary of the Collections that are available in Alveo, select the **Collections** tab. See [Browsing the Collections](/alveo-help/discovering-and-searching-the-collections/browsing-the-collections "Browsing the Collections") for more information.

## **Items in a Collection**

An Item is a group of documents that all relate to the same communication event – for example a speaker saying a particular word or sentence, a chapter in a book, a transcript of a speech.

Each Collection contains one or more Items.

#### Item Metadata or Facets

Associated with each Item is a list of Metadata. Metadata elements are also referred to as “Facets”. Alveo supports searching for Items by their Item Metadata.

Alveo uses the Metadata elements which are described by the Australian National Corpus.

The values of some Metadata Facets will be shared across all Items in a Collection. Others are specific to an Item.

Examples of Metadata elements or Facets are…

- The date on which the item was created or recorded
- The type of recording it is
- The type of speech style it records

…and many more.

To see a complete list of Metadata fields…

- **Select** the **Discover** tab from the navigation bar at the top of the screen. The **Item search** screen is displayed.
- **Click** on the blue **Advanced Search** link in the left hand panel. The **Advanced Search** screen is displayed.
- **Click** on the blue **Searchable Fields** link from within the explanatory text paragraphs. The list of Searchable Metadata Fields is displayed.



- You must be logged in to Alveo in order to see this list.

## **Documents in an Item**

Each Item will contain one or more Documents which are related on some way. Typically they all relate to the same communication event, and are often the same information recorded in different ways, such as a recording of the spoken word and a transcipt file.

These Documents can be of various forms, such as video, audio, text etc.

Alveo search operations operate on Items, not individual Documents. However when exported, such as to the Galaxy or Emu/R tools, documents can be processed individually.

#### Document Metadata

Document Metadata are limited to the Document’s file type, name and size. They are displayed when the Item Metadata are displayed (see [Searching and Selecting Items in the Collections](/alveo-help/discovering-and-searching-the-collections/searching-and-selecting-items-in-the-collections)).