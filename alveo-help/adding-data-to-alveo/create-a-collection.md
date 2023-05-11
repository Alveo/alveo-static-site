---
title: 'Create a Collection'
date: '2017-11-23T00:50:06+11:00'
author: 'Steve Cassidy'
layout: page
---

In addition to providing you with access to public, open access corpora and datasets, and conditional access corpora for you to search and analyse, Alveo also allows you to upload your own datasets and optionally make them available for other researchers to access.

## Obtaining access

In order to be able to create collections, you must be a *Data Owner* rather than an ordinary user. If you want to request data owner status, look at the bottom of the [main collections page](https://app.alveo.edu.au/) once you are logged in, you should see the following button:![screen shot of button to request data owner status](assets/files/2017/12/Screen-Shot-2017-12-05-at-8.43.45-am-1024x164.png)

Clicking on this button will take you to a form where you can request this change in status. You should include a little information about your collection: when and how you collected it, what sort of data it contains, what sort of data structure it has, and how large it is. The administration team may then have further questions for you, or may simply grant your request.

Once you have Data Owner status, the button will change to say “Create a Collection”, you can then click on this to start the creation process.

## Uploading methods

There are two ways to upload your own collections to Alveo: the first is by using the web interface to upload your files as a zip file, and the second is by using the Application Programmatic Interface (API).

The API is more fully featured and powerful than the web interface, but it is for advanced users who have some background in using a command-line interface and scripting methods. It would be more suitable for uploading larger collections with rich metadata. For details, see the [API documentation](http://alveo.edu.au/help/http-api-reference/) and [this blog post](/2016/08/19/uploading-data-to-alveo) that describes a sample upload script.

The Alveo website allows data owners to upload new items to a collection either individually or in bulk as a zip file. This method is suitable for small to medium sized collections.

## Collections, Items and Documents

In Alveo, data is organised into **Collections** as the highest level or the structure, with **Items** as a lower level. An item is a single communication event. Items contain files, which can be text, audio, video, etc, which are referred to as **Documents**, whatever their type. There may be several Documents for a single Item; for example, an audio recording and the text file of its transcription relate to the same communication event, and are both Documents within one Item.

To upload your own data, you’ll first need to create the Collection, then create the Items within that collection, and finally upload the Documents from your computer into the Items.

## Metadata

Alveo can support metadata in a number of standardised schemas, as well as any custom metadata fields. When you browse, filter and search Alveo data, you are using the metadata fields specified for the Alveo collections to see only those items that match your search. When creating collections and uploading data into Alveo, you can also specify metadata fields to be used to search, browse and filter your data. As with uploading data, metadata can be added through either the web interface or the API. This tutorial only covers the web interface uploading facility.

Adding metadata is a little more complicated than uploading data, and is described at the end of the tutorial. However, please note that, once uploaded, collections and items cannot be edited using the web interface. This means that, if you are using the web interface, metadata must be added at the same time as the collections or items are created. Metadata can be added later through the API, but this is a more advanced process. For this reason, we suggest reading the entire tutorial first before uploading any data.

## Creating Collections

Once you have obtained Data Owner access from the Alveo administrators, you will see different options on some of the Alveo pages. Go to the **Collections** page, and notice that there is now a button to **Create New Collection**. Click this.

When creating a collection, you need to provide a few details: the **Collection Name**, the **Collection Title** and the **Collection Owner**. In addition, you can provide a **Collection Abstract** which is essentially a description of the collection. You also need to decide whether other people will have to ask for your approval to access your data (**Private**), and which **Licence** to publish your collection under.

The **Collection Name** is a short, unique identifier that differentiates your collection from other collections in Alveo. In the example above, the name *egcoll* will sit alongside *cooee*, *austalk* or *ace*. This name will also be used in URLs for your collection and items, so make sure to pick a name that is very short and descriptive.

The **Collection Title** is a brief, free-text field to explain what the collection is. The Title can be an explanation of the Name. For example, the Title of the *cooee* collection is *Corpus of Oz Early English*. Choose a collection title that is descriptive and fits into just a few words.

The **Collection Owner** field should contain the name of the person or organisation that owns the materials that you are uploading. If this is you, simply put your own name into this field.

The **Collection Abstract** is a short (255 character) description of the collection that will appear on the main collections page. Use this to highlight the main contents of your collection to potential users.

The **Collection Description** is a longer, richer description of the collection which will make up the body of the main page for your collection. It should contain a full description of the collection, for instance who collected it, with what sort of equipment, or using what sort of methods, and when. You can format this page as you wish and even insert images and links to PDF or other attachments in the page. You may also want to include details of how to cite your collection should other researchers use it in their own studies.

If you want to restrict access to your collection so that other users need to ask for your approval, check the **Private** box. Lastly, the **Licence** drop-down menu allows you to select a licence – from a number of Creative Commons licences among others – under which your collection will be published. When accessing your collection, other users will need to acknowledge and agree to the conditions of access as set out by the licence, irrespective of whether the collection is private or not.

Once you have filled in these fields, click **Create**. You will be taken to the *Collection Details* page for your collection, and at the top of the page will be a notification telling you that your collection was successfully created. It is now visible to all other users of Alveo from the **Collections** tab, however they may or may not be able to access it without asking permission from you first, depending on whether you specified **Privacy**.

Note that the name chosen in the **Name** field appears as: 1) an identifier in the collection list on the left, 2) as the title of the page describing the collection, and 3) part of the URL. This is why the Name must be unique, otherwise a user (or the system itself) would not be able to differentiate between collections.