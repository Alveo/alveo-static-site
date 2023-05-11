---
id: 1940
title: 'Alveo Transcription Tool'
date: '2018-04-11T00:22:44+10:00'
author: 'Steve Cassidy'
layout: post
guid: 'http://alveo.edu.au/?p=1940'
permalink: /2018/04/11/alveo-transcription-tool/
categories:
    - News
    - Screencast
---

<iframe allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/ixQR-c4R0Ss?rel=0" width="560"></iframe>

We’re pleased to announce the latest tool in the Alveo stable for transcription of audio recordings. The [Alveo Transcription Tool](https://alveo.github.io/alveo-transcriber/) is a browser based system that works with audio stored on the Alveo platform to facilitate time-aligned transcription. The eventual goal is to support the entire workflow from uploading of recordings to transcription and then analysis of transcripts. In this first release of the tool though we are looking for feedback on the user interface and automated segmentation.

As shown in the video, when you connect to the tool you will be asked to login with Alveo. This works best if you’re already logged in to the [Alveo application](https://app.alveo.edu.au/) in your browser – if you are then you’ll just see a few screen refreshes and you’ll be logged in. You can then download data from Alveo – this is just to get the list of item lists you have access to. The idea is that you would create an item list of the items you want to transcribe and use that to drive your workflow in this tool.

Once you select an item list you can choose the item to transcribe and then the audio file you want to look at. You are then shown the transcription interface with a display of the audio waveform and a few controls.

A key feature of the tool is that it will automatically segment the audio for you to facilitate transcription. Click the Autosegment button and the audio will be sent to the backend server for segmentation. In this first version segmentation is by speech activity detection only but future versions will include a smarter speaker diarization system.

Segmentation will give you a set of speaker turns to transcribe. You can then click on one and if Autoplay is selected, you’ll hear it play. Transcribe what you hear, hit tab and keep going.

The transcription you create is saved in your browser’s local storage. This means that if you login again later, it will still be there for you to continue with, even if you shut down your browser and re-start it.

The current version of the tool allows you to download the transcript as a CSV file or as a JSON structure. The next stage of development will be to add a backup server that will store your transcriptions in the cloud. Beyond that we will develop a workflow to push transcriptions back to Alveo as an [Annotation Contribution](http://alveo.edu.au/help/adding-data-to-alveo/contributions/) so that they are associated with the original recordings and available to other Alveo users.

If you want to test the transcription tool you’ll need an Alveo account. I’ve prepared a shared item list with some sample recordings that we’ve tested called **transcription-sample**. If you select this you can try transcribing these recordings to get a feel for the user interface. Note that this item list contains data from the Austalk, Mitchell &amp; Delbridge and AVCOM collections – you’ll need to agree to the licence terms for each of these to be able to use the data.

Your feedback on any aspect of this is most welcome – please email me at Steve.Cassidy@mq.edu.au.