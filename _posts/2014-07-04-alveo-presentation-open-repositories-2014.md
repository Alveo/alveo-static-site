---
title: 'Alveo presentation, Open Repositories 2014'
date: '2014-07-04T14:01:02+10:00'
author: ptsefton
layout: post
permalink: /2014/07/04/alveo-presentation-open-repositories-2014/
categories:
    - News
---

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](/licenses/by/4.0)  
`Alveo presentation, Open Repositories 2014` by Steve Cassidy,Dominique Estival, Peter Sefton, Jared Berghold &amp; Denis Burnham is licensed under a [Creative Commons Attribution 4.0 International License](/licenses/by/4.0).

Presentation delivered by Peter Sefton at [Open Repositories 2014](http://or2014.helsinki.fi/) in Helsinki

#   **ALVEO The Human Communication Science Virtual Laboratorybuilding on HCSNet (an ARC research network)Presented by: Peter Sefton** 

\[NOTE: This talk uses some slides, mostly screenshots which have been used in other presentations, but the narrative is different for this conference\] The Human Communication Science Virtual Lab (Alveo) represents a new kind of data driven research collaboration environment which has at its heart a repository of human communication data, drawn from research collections in a broad range of fields including speech science, speech technology, computer science, language technology, behavioural science, linguistics, music science, phonetics, phonology, and sonics and acoustics. The repository contains text, audio and video data as well as annotations which describe the data, with a discovery search/browse interface. But this is not a just a repository project – the main function of the lab is to provide a platform for doing things with data in ways that were previously difficult, via a rich programming interface (API), and via a workflow engine which allows a large cross-disciplinary research community to run combinations of tools on the data held in the repository in a reproducible way. The presentation will cover vLab’s genesis as an Australian Government funded project consisting of a dozen universities and institutions led by the University of Western Sydney, with development provided by Intersect NSW. We will provide a walk-through of the functionality of the lab including showing how familiar repository functionality such as search-and-browse is linked to the creation of stable, citable collections known as “item lists”, and how item lists can be processed and analysed in various ways using linguistic parsers, acoustic and phonetic analysis, and visual processing and how this fits in to the research lifecycle including how data and publications will be linked and cited, and explore the relationship between the lab and other scholarly infrastructure such as institutional repositories.

See http://alveo.edu.au

#   **Funding** 


##  Alveo acknowledges funding from the NeCTAR project [   **http://www.nectar.org.au**   ](http://www.nectar.org.au/) NeCTAR is an Australian Government project conducted as part of the Super Science initiative and financed by the Education Investment Fund.

 *Avleo*   
is funded by NeCTAR, a body set up by the Australian Government as part of the Super Science initiative and financed by the Education Investment Fund. 
 **Background &amp; Goals** The vLab1,2 project was funded by NeCTAR, which is one of a number Australian Government investments in eResearch infrastructure over the last decade, following on from a number of repository programs3,4, familiar to the Open Repositories audience, and the Australian National Data Service (ANDS)5, which is well on the way to establishing research data management infrastructure including research data catalogues (AKA metadata stores) and/or research data repositories as business-as-usual systems for all universities and many other research institutions in the country. On the content side, Alveo follows on from Australian National Corpus Project6, funded by ANDS which established the core repository framework and collected the first tranche of language data to be included in the vLab. AusNC itself is one of many projects that emerged from the ARC-funded Human Communication Science Network7 involving over 1000 Australian researchers across the disciplines mentioned above. Alveo will both continue that work and take it to a new virtual accessible level that will further engender research collaboration.

The aim of the lab is to make data-driven research using a wide variety of tools more accessible to a broader range of researchers, both with and without technical skills, to facilitate new kinds of research, involving novel tool-data combinations to take place. Walters8 surveys similar work, in “Assimilating Digital Repositories Into the Active Research Process” which is an apt title, the vLab did not grow out of a library-based publications repository and attempt to add services to it; rather, the vLab was built around a framework for connecting data to code part of a research workflow and brought in a repository to effect this.

#   **Contributing Partners** 

University of Western Sydney, Macquarie University, the Australian National University, University of Canberra, Flinders University, University of Melbourne, University of Sydney, University of Tasmania, University of New South Wales, University of Western Australia, RMIT, University of New England, LaTrobe University, NICTA (National ICT Australia, ASSTA (Australasian Speech Science and Technology Association), #   **Development partner: Intersect** 

##   **Intersect Development Team:** 

##  Ilya Anisimoff Jared Berghold David Clarke Georgina Edwards Karen El-Azzi Gabriel Gasser Matthew Hillman Chris Kenward Nasreen Sharique Kali Waterford Elyse Wise Marc Ziani de Ferranti Shuqian Hon Sean Lin Theeban Soundararajan Vincent Tran Stanley Hon Pierre Estephan Simon Yin

#   **Watch the video!** 

A good way to get a an understanding of what the virtual lab can do is to have a look at this video by Steve Cassidy from Macquarie University made for the launch of Alveo v3 (after the conference) http://youtu.be/pgSeyMEdCsc 
During this presentation we will build a view of the Architecture of the lab by looking at its various functions. The lab has a data repository at its heart but the primary aim of the lab is not to archive data, or even to make it discoverable, it is to make data usable and re-usable for research, which requires that there be discovery and archiving services. This is accomplished via two main avenues, firstly via the web based API which allows services to be built on top of the core repository, and secondly via a web-based drag and drop workflow engine. The chosen workflow engine is the Galaxy system9–11, which originated as a bio-informatics analysis platform but is now being used in a variety of other contexts, including as an image analysis tool in other NeCTAR projects12.

(This is a picture of the band “Architecture in Helsinki”, playing in Helsinki. Group Architecture in Helsinki  
[  
CC BY-SA 3.0  ](http://creativecommons.org/licenses/by-sa/3.0)

[  
Leena Hernesniemi  ](http://commons.wikimedia.org/wiki/User:Elena_xxx)  
– Own work)

#   **Data Discovery** 

The laboratory has a data-discovery portal which houses a growing number of data sets. We originally called these ‘corpora’ but this turned out to a problem, as (a) many people don’t know what a corpus is or how to tell their corpus from their corpora and (b) it is specific to some disciplines, so these are now know as Collections. All the current collections in the lab require researchers to agree to a license, usually via web-click, some require an offline contract. This is not Open Data in the normal sense but given the terms under which most of the collections were collected this is the best we can do to make data available as broadly as possible.

#   **Discover data via metadata facets** 

The discovery interface is very similar to that found on many repository services, it has faceted browsing and full-text search for resources. But the repository function is not the main or sole purpose of the lab, it is designed to allow people to DO things with data and to report on and save the results. 
This diagram is not anatomically correct but it does show the major components of the repository part of the lab.  *Collections (corpora) of items*   
, where an item is defined as a communicative event, e.g., a single text, conversation, utterance or musical performance. As with the kinds of repositories familiar to an Open Repositories audience, items can have multiple data streams representing different versions or aspects of the event, including text versions. Unlike typical institutional publications repositories the primary kind of  
 *text*   
object is a plain-text stream with all formatting and analytical annotation stored as stand-off annotations.

 *Per-collection access control.*   
Many of the data sets have been collected from human participants under a variety of consent agreements requiring researchers to agree to a click-through license, or go through an offline process to have access approved.

 *Multiple indexes,*   
An  
[  
Apache Solr  ](https://lucene.apache.org/solr/)  
text index and an RDF triple store are supplied as core functionality, but the intention is that other indexing services will be able to be added. The first of these is being built using the INDRI14 information retrieval engine; INDRI is in fact one of the research tools that has been integrated into the platform, it is used by researchers in information retrieval to experiment with new search engine architectures and features. It is now being used to build an advanced search tool for the data stored on the vLab. We expect that other search services will be implemented in future.

#  Q. What do you call something that automatically prepares data for ingest?

##  Q. What do you call something that automatically prepares data for ingest?

This repository does not have a ‘front door’. There is no end-user accessible way to add materials to the data-store. There are two reasons for this. The first is that the lab is built on existing stable data collections or ‘corpora’.

#  A: Robochef

- ##  A: Robochef

Each corpus (data collection) is ingested by preparing metadata and then running a script the ‘robochef’ named for it’s ability to ‘automatically prepare things for ingest’ #   **Sivusto Rakenteilla** 

The second reason that there is no front door is essentially that we have not built one yet. During the second phase of the project we will be focusing on sustainability and driving adoption of the lab, making it easier to add content. Image source: http://commons.wikimedia.org/wiki/File:Under_construction_graphic.gif

#   **Architecture: Discovery leads to data** 

The lab has a data-storage component which can look after large amounts of heterogeneous data, with any kind of digital resource stored against an item. #   **Including various media** 

This is an example of speech data from the Mitchell and Delbridge corpus (data set) collected in the 1960s. #   **Post discovery: compile your own stable “Item Lists”** 

Researchers can create their own sets of working-data from items in the repository, the discovery interface can be used to define and save an item list. Item lists are stable, reusable and in future will be citable, they are NOT like saved searches. This contrasts with a saved-search in something like the National Library’s Trove service where the same search or API call might yield a different set of items on different days.

These are know as item lists and these are the key to re-doable research workflows as they allow the same stable data set to be run through multiple processes. Item lists are available via the web interface and via the API.

#   **Concordance: a tool run on an Item List** 

Steve’s demo shows some examples of simple, broadly useful text analysis tools that are built into the Alveo data site. #   **API Access: Get a key** 

All the data and discovery services available in Alveo are available via the API, the Application Programming Interface. This is one of the key features of the lab, coupled with the stable, reusable Item Lists we looked at above, this is the key to opening up data in new ways. #   **Copy-paste access to data** 

Programmers are able to use Item Lists in custom code. The discovery interface makes this as easy as copy and paste (assuming that you’ve installed the software libraries you need in your programming interface). The API respects the access control of data collections in the lab, via a per-user private API key.

The ultimate aim of the lab is to make sure that you can do everything via the API.

#   **Workflow: Galaxy** 

Like other NeCTAR virtual labs, Alveo uses the Galaxy workflow engine to allow researchers to construct research workflows that can be run over different data sets, and share them with others. In phase two of the project we will work on reusability and reproducibility with research teams. #   **Chain processes on Item Lists – eg \[Tokenizer\] -&gt; \[Frequency List\]** 

This simple demo shows how an Item List is used in Galaxy, where multiple operations can be performed on data with each step feeding its result into the next one. This allows for more flexibility than the simple ‘canned’ tools built into the Alveo data web site. A similar approach will be used for audio and video data allowing researchers to create item lists, set some parameters and run analytical processes, resulting in new data sets or graphical plots.


This particular workflow processes audio data using the PsySound3 software toolkit (which was developed by Densil Cabrera, Emery Schubert and others to analyse sound recordings using physical and psychoacoustical algorithms). Given any audio recording as input, this workflow will perform an FFT (Fast Fourier Transform), Hilbert transform and Sound Level Meter analysis on the audio file and plot a graph for each one. 
The second screenshot shows the plot resulting from one of the analyses performed – the FFT. The input audio file used in this example came from the Mitchell-Delbridge corpus (a database containing the recordings of Australian English as spoken by 7736 students at 330 schools across Australia, mostly collected in 1960). 
The lab also allows annotation of all kinds of materials including text and time-based media. At the moment this is accessible via the API.  *Annotations stored with items,*   
a core facility is the storage and management of  
 *standoff annotations*   
on the data stored in the vLab. Annotations are attached to points or regions in the text, audio or video data (represented as start/end points) and may contain a simple label or a complex feature structure. Example annotations might mark a speaker turn in a dialogue, a headline in a text file or a individual phoneme in a speech recording. Researchers generate annotations manually and automatically and there are many diverse file formats and tools that work with them. The vLab implements the DADA Annotation Store15 which represents annotations in RDF and provides a general model that unifies many styles of annotation. The API currently exposes a basic feed of annotations for each item. In the future, we expect to build comprehensive annotation query services on top of this annotation store.


This diagram shows the overall architecture of the lab – with the repository in the center, feeding data to the Galaxy workflow engine at the top, but also accessible from computing platforms directly. Everything hinges on the API. #   **Reuse** 

This project uses a number of open source components to scaffold the lab including Hydra which is Ruby on Rails framework wrapping:

Apache Solr and blacklight

The Duraspace Fedora Commons repository

Apache Solr, via the blacklight project

Workflow courtesy of Galaxy “Data intensive biology  
 *for everyone.” 🙂*

#   **Reproducible Research** 

 **What will vLab-enabled research look like?** Phase one of the HCS vLlab project is running between early 2013 and mid 2014, and by June 2014 version 3 will have been completed and launched. The second two-year phase will involve further development but also a much greater emphasis on promoting the use of the service, with a view to having research articles that use the lab, its data and tools, and successful grant applications that incorporate use of the vLab. The Alveo community will be exploring ways to:

Cite item lists as reusable data.

Cite the products of particular processes (code, Galaxy workflows) which have been run on item lists.

One of the key goals of the vLab is to allow reproducible research and re-runnable research processes and workflows. To enable this, it is important that there are stable, referenceable entities that can be re-processed and re-used. We have yet to solve all the challenges involved in preserving item-lists exactly, and maintaining access-control.


  
 **Architectural issues**

Using the Fedora repository and Hydra toolkit has one major advantage; the project team were able to establish very quickly a discovery interface with rich faceted search; however there have been some problems; the major one being the Fedora stack is designed around an environment where users access one repository item at a time, usually via a web interface. Hydra had poor performance on batch-access to item-lists as there is a significant overhead in the software stack for accessing an individual item. This has meant that we have had to build special purpose SOLR indices to improve access times for the core data, extending the common technique of supplementing Fedora’s built in services with external index-based services.

Our wish list for a platform (some of which we believe are proposed for Fedora 4) would include:

Tight integration with access-control and the back-end repository service

Efficient access-controlled batch-access without resorting to hacks such as hand-tuned indexes.

The ability to mount a repository as a file system for efficient direct access to data.

#   **User feedback** 

##  “I really liked using the system and the instructions were very easy to use and the system easy to navigate. \[…\] This platform would be very useful for my research.”

##  –Tester

“It seemed pretty easy to use after I got used to the two platforms. I would certainly like to use it in my future research!” “It is looking very good. Lots of possible uses and a nice interface.”

“The platform is easy to use and has the great potential to help with Linguistic research and wide applications in other areas…”

“The system seemed to be quite user-friendly. As first I was relying on the manual, however when the manual became more streamlined with less details, the system was still easy to follow.”

“This is a powerful tool and I think it is pretty good.”

“I really liked using the system and the instructions were very easy to use and the system easy to navigate. \[…\] This platform would be very useful for my research.”

“I think it’s quite easy to use. \[…\] Generally the platform is very clearly organised, and user-friendly.”

“The platform overall is very good.”

“Very nice platform with great user interface!”

“A very promising and impressive setup so far!”

“I’m impressed with the platform – it’s smooth and the interface is very intuitive.”

“I think it’s quite easy to use. \[…\] Generally the platform is very clearly organised, and user-friendly.”

“The platform overall is very good.”

“Very nice platform with great user interface!”


 **References** 1\. Goecks, J., Nekrutenko, A., Taylor, J. &amp; Team, T. G. Galaxy: a comprehensive approach for supporting accessible, reproducible, and transparent computational research in the life sciences.  
 *Genome Biol*   
 **11,**   
R86 (2010).

2\. Giardine, B.  
 *et al.*   
Galaxy: a platform for interactive large-scale genome analysis.  
 *Genome Res.*   
 **15,**   
1451–1455 (2005).

3\. Blankenberg, D.  
 *et al.*   
Galaxy: A Web-Based Genome Analysis Tool for Experimentalists.  
 *Curr. Protoc. Mol. Biol.*   
19–10 (2010).

4\. Awre, C.  
 *et al.*   
Project Hydra: Designing &amp; Building a Reusable Framework for Multipurpose, Multifunction, Multi-institutional Repository-Powered Solutions. (2009). at &lt;http://smartech.gatech.edu/handle/1853/28496&gt;

5\. Strohman, T., Metzler, D., Turtle, H. &amp; Croft, W. B. Indri: A language model-based search engine for complex queries. in  
 *Proc. Int. Conf. Intell. Anal.*   
 **2,**   
2–6 (Citeseer, 2005).

6\. Cassidy, S. An RDF Realisation of LAF in the DADA Annotation. in  
 *Serv. Proc. ISA-5 Hong Kong*   
(2010).

