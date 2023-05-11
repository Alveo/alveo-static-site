---
id: 1809
title: 'Uploading Data to Alveo'
date: '2016-08-19T01:59:19+10:00'
author: 'Steve Cassidy'
layout: post
guid: 'http://alveo.edu.au/?p=1809'
permalink: /2016/08/19/uploading-data-to-alveo/
categories:
    - News
    - Tutorials
---

When we set out to build Alveo the aim was always that it should be a repository for new collections contributed by researchers; however, the initial impetus was to get a number of older collections ingested and build the platform capabilities. New collections were added to Alveo via a back-end process that only the developers could run.

We have since worked on adding the hooks into the API to allow new collections, items and documents to be added to the Alveo repository. This extended API has now been deployed on the main system and we have extended the [pyalveo library](https://pypi.python.org/pypi/pyalveo) to allow scripts to be written that add new data. I recently used this facility to add the first contributed collection to Alveo: a collection of children’s speech data. This blog post describes the script that I wrote to do this by way of a bit of a tutorial on the process.

The whole script is saved as a gist ([upload\_children.py](https://gist.github.com/stevecassidy/087f08c1844efd5ba2d20d60d5eb5894)) but I will include code snippets below as I describe the process.

## The Data

The data that I’m working with is a corpus of recordings of children’s speech collected by Catherine Watson and myself in 1998 and used in a number of publications looking at the properties of children’s speech. One of my motivations is that I’m working on reproducing the results in one paper as an exercise in developing workflows for the Alveo system:

S. Cassidy and C. Watson (1998) Dynamic Features in Children’s Vowels. Paper presented at the *International Conference on Speech and Language Processing*, Sydney, Australia, November 1998. ([pdf](http://web.science.mq.edu.au/~cassidy/papers/children.pdf))

We collected recordings of eight children reading words and digit strings. Recordings were separated into individual files and we manually annotated phonetic segments for all recordings. We also generated formant tracks (using the now defunct ESPS formant tracker) and hand-corrected the tracks where mis-tracking had occurred. As is common with this kind of data, some metadata was encoded in the filenames, in this case the speaker identifier (sp1 to sp8) and the prompt made up the file basename with different file extensions for different types of data. So for one prompt (card) we have:

```
sp1/data/sp1.card.sf0 
sp1/data/sp1.card.sfb  
sp1/data/sp1.card.wav  
sp1/labels/sp1.card.hlb  
sp1/labels/sp1.card.lab  
sp1/labels/sp1.card.trg
```

Each speaker is in a separate directory and the data is split between data and labels directories. The data contains the original audio recording (.wav) along with pitch (.sf0) and formant (.sfb) data in the SSFF format supported by the[ Emu system](http://ips-lmu.github.io/EMU.html). The labels are stored in the old Emu format (.hlb) as well as the simpler ESPS format for phonetic (.lab) and vowel target (.trg) labels.

## Writing an Upload Script

Uploading the data to Alveo is relatively simple, the API provides endpoints for creating new collections and items and adding documents to items (see the [API documentation](http://alveo.github.io/apidocs/#/)). The easiest way to use this API is via the pyalveo library and the recently released version (0.6) supports these new operations. The simple form of the code to create an item is:

\[python\]  
client = pyalveo.Client(configfile=config)  
collection\_uri = client.create\_collection(name, collection\_meta)  
item\_uri = client.add\_item(collection\_uri, itemid, meta)  
client.add\_document(item\_uri, docname, docmeta, file=file)  
\[/python\]

The first line creates a client connection to the Alveo API, we then create a collection, add an item to it and attach a document to the item. In all cases we add some metadata to the created entities, a big chunk of the script is about how to generate this metadata.

For each speaker in our collection we have some demographic data. I have this stored in a spreadsheet which I’ve saved as a CSV file so that it can be easily processed by my script. The spreadsheet contains columns for Speaker ID, Gender, Age, Place of Birth, State, Country, Parents first language, Other languages spoken at home and Sibling (two of the subjects were siblings, this column just names the other sibling). My script will add all of these properties to every item as it is uploaded so my first job is to read the spreadsheet. I do this with a procedure read\_demographic which reads the CSV data and returns a dictionary with one key per speaker, each key contains a dictionary corresponding to a row in the spreadsheet.

\[python\]  
def read\_demographic(basedir):  
 """Read the demographic spreadsheet  
 return a dictionary with speaker ids as keys  
 containing one dictionary per speaker"""

 if demographics == None:  
 demographics = dict()  
 with open(os.path.join(basedir, "sp1-sp8-demographic.csv")) as fd:  
 reader = csv.DictReader(fd)  
 for row in reader:  
 demographics\[row\[‘Speakerid’\]\] = row  
 return demographics  
\[/python\]

## Converting Metadata

The next task is to turn this metadata into a form suitable for Alveo. The main job is to translate the property names into suitable names for Alveo – if possible, matching property names already in use. For example, the gender column should map to the property name `foaf:gender` since that is used for all existing collections in Alveo. The list of [currently used property names](https://app.alveo.edu.au/catalog/searchable_fields) is available on the Alveo site (the first column). In some cases these are well-known names (like the dc properties from Dublin Core), in other cases they are specific to a collection. If nothing fits, then you can just use a plain name for the property.

I define a python dictionary that I will use to map between the headings in my spreadsheet and the property names:

\[python\]  
DEMOGRAPHIC\_MAP = {  
 ‘Speakerid’: ‘olac:speaker’,  
 ‘Gender’: ‘foaf:gender’,  
 ‘ParentsLanguage’: ‘austalk:parents\_first\_langage’,  
 ‘OtherLanguage’: ‘austalk:other\_languages’,  
 ‘Age’: ‘foaf:age’,  
 ‘POB’: ‘austalk:pob\_town’,  
 ‘State’: ‘austalk:pob\_state’,  
 ‘Country’: ‘austalk:pob\_country’,  
 ‘Sibling’: ‘sibling’  
 }  
\[/python\]

I then write a procedure to return the translated metadata for a given speaker:

\[python\]  
def speaker\_meta(speaker, demographics):  
 """Return a dictionary of metadata for this speaker"""

 if speaker in demographics:  
 result = dict()  
 for key in demographics\[speaker\].keys():  
 metakey = DEMOGRAPHIC\_MAP\[key\]  
 if demographics\[speaker\]\[key\] != ”:  
 result\[metakey\] = demographics\[speaker\]\[key\]  
 return result  
 else:  
 return dict()  
\[/python\]

## Data Handling

I now come to the task of creating the items with their associated documents. I’ve split this up into two parts in the script: the first is a generator of items and documents, the second uploads these to Alveo.

The [generator](http://pymbook.readthedocs.io/en/latest/igd.html#generators) is a procedure that returns the items in the collection one at a time. It does this by traversing the main collection directory then the speaker directories etc. This is the part of the script that knows about how the collection is laid out on disk. My motivation here was that I could perhaps rewrite this part for another collection while leaving the rest of the script untouched – I’m sure that’s not quite true of the current implementation but that’s the direction I was going in.

This procedure also returns the metadata for each item as a python dictionary. This is generated from a fixed metadata dictionary which is the same for every item, the speaker metadata and a couple of fields derived from the item filename (title and prompt). Each return value is a tuple containing the item id, the metadata dictionary and the list of documents for that item.

\[python\]  
def corpus\_items(basedir):  
 """Return an iterator over items in the corpus,  
 each item is returned as a tuple: (itemid, metadata, \[file1, file2, file3\])  
 where itemid is the identifier  
 metadata is a dictionary of metadata  
 fileN are the files to attach to the item  
 """  
 base\_meta = {  
 ‘dcterms:creator’: ‘C. Watson and S. Cassidy’,  
 "ausnc:mode": "spoken",  
 "ausnc:communication\_context": "face-to-face",  
 "olac:language": "eng",  
 "ausnc:interactivity": "read",  
 "ausnc:audience": "individual",  
 }

 read\_demographic(basedir)

 for spkr in os.listdir(basedir):  
 meta = base\_meta.copy()  
 meta\[‘olac:speaker’\] = spkr  
 meta.update(speaker\_meta(spkr))

 # iterate over wav files  
 for wav in os.listdir(os.path.join(basedir, spkr, ‘data’)):  
 files = \[\]  
 (sp, prompt, ext) = wav.split(‘.’)

 if ext == ‘wav’:  
 meta\[‘dcterms:title’\] = prompt  
 meta\[‘austalk:prompt’\] = prompt

 # gather the files  
 files.extend(glob(os.path.join(basedir, spkr, ‘data’, sp+’.’+prompt+’.\*’)))  
 files.extend(glob(os.path.join(basedir, spkr, ‘labels’, sp+’.’+prompt+’.\*’)))

 yield (spkr + "." + prompt, meta, files)  
\[/python\]

The final part of the puzzle is the procedure to do the upload via the Alveo API. This procedure iterates over the items generated by `corpus_items` and calls the API to add items and documents. As a first step I’ve made it delete any existing items from the collection – partly this is for debugging purposes as I tested the script so this could be removed in future. The only other comment to make here is on the construction of metadata for each document. I’ve used another dictionary (`EXT_MAP`) to convert file extensions into a document type name for Alveo. Alveo currently uses names like Audio, Text etc for document types (there’s a case for using a more standard nomenclature like mime types – perhaps in future we should consider this). This dictionary assigns a name for the file types I know I have in the dictionary based on their extension.

\[python\]

def process(basedir):  
 """Process the files in this corpus"""

 client = pyalveo.Client(configfile=CONFIG, verifySSL=False)

 collection\_uri = client.api\_url + "catalog/" + COLLECTION\_NAME

 # delete any existing items  
 print "Deleting items: ", list(client.get\_items(collection\_uri))  
 for itemuri in client.get\_items(collection\_uri):  
 client.delete\_item(itemuri)

 for itemid, meta, files in corpus\_items(basedir):  
 start = time.time()  
 item = client.add\_item(collection\_uri, itemid, meta)  
 print "Item: ", itemid, time.time()-start

 for file in files:  
 docname = os.path.basename(file)  
 root, ext = os.path.splitext(docname)  
 if ext in EXT\_MAP:  
 doctype = EXT\_MAP\[ext\]  
 else:  
 doctype = "Other"

 docmeta = {  
 "dcterms:title": docname,  
 "dcterms:type": doctype  
 }  
 try:  
 client.add\_document(item, docname, docmeta, file=file)  
 print "\\tDocument: ", docname, time.time()-start  
 except pyalveo.pyalveo.APIError as e:  
 print "Error: ", e

\[/python\]

That completes this example implementation for uploading the children’s data. Hopefully it is useful for others who are working on upload utilities for Alveo. If you are writing scripts like this and want to test them without messing up the main Alveo repository, please get in touch with me (Steve.Cassidy@mq.edu.au), I can give you access to a staging server that can be used for development.

One comment to make is about the speed of upload. In the current implementation it takes around 30s to upload one item with a few documents from the children’s data. This means that uploading the whole dataset took over a day to complete. We are aware of the bottleneck in the system that is causing this slowdown and have implemented a new faster ingest method. We have a little more work to do connecting it up to the API but once we do it should show a marked improvement in performance. There may be some small changes to the API in the process but if you use the pyalveo interface, we will try to ensure that the code changes required are minimal.