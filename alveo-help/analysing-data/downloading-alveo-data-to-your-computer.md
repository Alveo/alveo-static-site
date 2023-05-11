---
id: 1106
title: 'Downloading Alveo Data to Your Computer'
date: '2014-08-05T12:30:08+10:00'
author: peterr
layout: page
guid: 'http://alveo.edu.au/?page_id=1106'
---

You can download all of the data in an Item List to your computer as a Bagit ZIP file.

Bagit is a simple ZIP file format, which contains a directory structure based on the Items in your Items List and the Documents in each Item. You can find information about the Bagit format and further links on the Wikipedia [Bagit](http://en.wikipedia.org/wiki/BagIt) page.

<section class="panel panel-default instructions"><div class="panel-title">To Download an Item List as a ZIP File…</div><div class="panel-body">- **Click** on **Item Lists** in the Alveo Navigation Bar. The names of your available Item Lists will be displayed.
- **Click** on the name of the Item List you want to download. The Items in the Item List will be displayed.
- **Click** <button class="btn btn-default" type="button">Item List Actions</button> and select **Download as ZIP** from the dropdown menu that is displayed. A File Save dialog will be displayed.
- **Select** the directory into which you wish to save the ZIP file and click <button class="btn btn-default" type="button">Save</button>.

</div></section>The format of the downloaded Bagit ZIP file will match this example.

![DownloadedZIP](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/08/DownloadedZIP.png)

- The top level of the ZIP file has some .TXT files containing information files about the BAGIT format and this ZIP file in particular.
- The JSON format stores key/value pairs. It is (somewhat) human readable, but the most convenient way to directly view it is to use a JSON plug-in for your browser. There are many available. There are also many JSON readers available for a wide variety of programming languages, which permit automatic processing of these files. The instructions for installing the R environment for EMU/R include an instruction to install a JSON reading package. Information about JSON can be found at <http://json.org>.