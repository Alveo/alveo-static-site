---
title: 'Annotation Contributions'
date: '2017-11-23T00:57:54+11:00'
author: 'Steve Cassidy'
layout: help
order: 6.3
---

An **Annotation Contribution** is an uploaded set of annotations or other value added files that will be associated with an existing collection. Any user is able to upload a contribution that will be made available to all users who have access to the original collection.



For example, I might download some audio files from the Austalk collection and create a phonetic segmentation of them using Praat. This results in a set of TextGrid files corresponding to the original WAV files. I create a zip file with these new TextGrid files and I can then upload these as an Annotation Contribution. The individual files will be associated with the original items in Alveo based on matching the filenames with the original documents.



## Create an Annotation Contribution



To create a contribution, click on the [Contribution](https://app.alveo.edu.au/contrib) link in the navigation bar to go to the Annotation Contributions page. Click on the “Create New Contribution” button at the bottom of the list of contributions. This will take you to the form to fill in the details of your annotations.

![Annotation Creation Form Screenshot](/assets/files/2017/12/Screen-Shot-2017-12-01-at-4.40.33-pm-1024x761.png)

First give your contribution a title and choose which collection your contribution will be associated with. Each contribution is linked to only one collection because the system needs to look within that collection to associate your files with existing items.

Enter an abstract for your contribution. This should be a short description that will appear on the page listing contributions. Provide enough detail to allow people who might be interested to recognise what is included.

More detail can be provided in the Description. This can be a rich text entry with formatting that can be used to describe your annotations in full. This will appear on the page corresponding to your contribution. The URL of this page is something that you could share with others who might re-use what you’ve done. It could, for example, be included in a publication that made use of these annotations.

## Uploading your Files



Once the contribution has been saved, you will see a button “Import Zip” on the contributions page. Click on this to be able to upload your zip file.

Your zip file should contain files with the **same base name** as an existing item in the target collection. So, if the collection contains an item with a document **foo.wav**, you could have **foo.txt** in your zip file. You can even upload a file that has the same name as an existing file attached to an item; in that case, your file will be renamed to something like **foo-c93.wav** (where 93 is the id number of your contribution).

Select the zip file you want to upload and click on **Upload and Preview**. This will upload your zip file to the server, unpack it and look for matches with existing files in the collection. The page will be updated to display the items and the files that have been found for you to review.

![screen shot of contribution upload preview page](/assets/files/2017/12/Screen-Shot-2017-12-01-at-5.18.03-pm-1024x498.png)

This preview page will show a error message if some of the files in your zip file did not match existing files in the collection. This could be because you have changed the file name in some way (eg. by adding a suffix). You can fix this by renaming your files and re-creating the zip file and then trying the upload again.

For files that were matched to existing items you will see details of the file and the other files already associated with the item.

If there are no errors and you are happy with the preview, click **Proceed Import** to finalise the import of your data (this button is not enabled if there were errors in matching your files). You will then be shown the page for your contribution that will list the items and files that you have uploaded.

![screen shot showing a contribution page](/assets/files/2017/12/Screen-Shot-2017-12-01-at-5.30.07-pm-1024x483.png)



The links on this page allow you to go to the page for each item that you’ve linked an annotation file with. If you follow that link to view the item, you will see your file along with a link back to your contribution page. This enables people to see where this file came from and find the other files that you’ve uploaded.

![screen shot of a file from a contribution](/assets/files/2017/12/Screen-Shot-2017-12-01-at-6.13.02-pm.png)

From the contribution page, you can also download all of your contributed files via the **Export Zip** button.

If you **Delete** your contribution, all of the files that you have uploaded will be removed from the system and your contribution will be removed.

Note that you can upload files in more than one zip file if you want to add further files to your contribution incrementally.



