---
title: 'Part 2: Galaxy'
date: '2015-11-18T16:54:04+11:00'
author: aidan
layout: page
---

This is Part 2 of a four-part tutorial in using Alveo. You can find the outline of the tutorial, and links to the other three parts on the [Tutorials](/tutorials "Tutorials") page. This Part will cover the basics of Galaxy, including importing Alveo lists into Galaxy, and using histories.

## Introduction to Galaxy

Galaxy is an online workbench originally designed for bioinformatics, that allows you to run data through tools stored on the cloud. Galaxy is used by a number of other disciplines such as astronomy and economics, as it is a very powerful workflow engine that allows researchers to define their own data manipulation and analytical tools. The version of Galaxy that we use in Alveo contains tools that have been specifically designed for language, speech, video or text analysis.

You can think of Alveo as a scientific laboratory, with data sitting in filing cabinets and drawers. Galaxy is another part of the laboratory that contains the equipment and machinery that you use to experiment on your data. In order to experiment, you need to find the right data first, and then carry it over to the workbench where all the equipment is located.

This part of the tutorial involves using your Alveo data lists in Galaxy, and using the Galaxy tools to concatenate and rename files, as well as using histories to track your steps.

## Getting Access to Galaxy

You can access Galaxy via the link at the top of the page in Alveo or via the URL .

The first time you attempt to use Galaxy, you should create an account. This account is different from your account on Alveo. After you have given Galaxy an email address, a password and an account name, you will be logged in. You can do some things without an account, but if you want to keep track of your data and saved workflows, you will need to login.

## Getting Alveo Data in to Galaxy

Galaxy is a workbench for running tools over data; to do some work we need to have some data on the Galaxy server. You can upload data from your own computer directly to Galaxy or you can get data from Alveo using the tools provided.

The main way to get data from Alveo is to create an **Item List** on Alveo with the data you want to work with, then use the Alveo tools in Galaxy to get the data. The following video illustrates how to do this to get some audio files into Galaxy.



There is also a special purpose tool that will query the Austalk collection to find the hVd words for a given speaker. This has been designed for a particular workflow (generating vowel plots) and is an example of the kind of special purpose tool that is relatively easy to make for Galaxy. The following video illustrates the use of this tool.



When Galaxy performs a task, it runs in the background, allowing you to do other things. It lets you know the progress with an entry in the history viewer, located in the right-hand sidebar.

![](/wp-content/uploads/2015/10/image07.png)

When a job has completed, it will turn green in the history. It will also produce more than just the single output file. You can click on the file names to see the details and, in the case of text documents, a preview of the text. In order to see the full text, click the eye icon. Next to the eye icon is a pencil icon, which is for editing the attributes of the dataset, including its name.

You can also download files from the Galaxy workbench. This may be helpful later in the process after you have used Alveo and Galaxy to analyse and compute your data, if you want to download your results. To download, select a file in the history by clicking it, and notice that a few more options become available. One of these, represented by an icon of a floppy disk, is for downloading the file to your computer.

![](/wp-content/uploads/2015/11/2016-02-29_13-42-23.png)

## Histories

The history pane, on the right of the screen, lists all your previous steps and contains all output files from any jobs you run. You can also create more histories and rename them, and when you run workflows (which you will learn in Part 4) you can tell Galaxy to output the data to a new history. Different histories are a good way to manage different projects and data sources within Galaxy.

It is also possible to move or copy datasets from one history to another, or move them into a new history, by selecting **Copy datasets** from the gear icon in the history sidebar.

| **Tutorial Task 5:** Copy the three concatenated lists that you imported from Alveo into a new history, and call it *Text analysis*. ![](/wp-content/uploads/2015/10/image34.png) |
|---|

Proceed to [Part 3: Tools](http://alveo.edu.au/tutorials/part-3-tools).