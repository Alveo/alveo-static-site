---
id: 160
title: 'AeRO UX Review: HCS vLab'
date: '2013-10-30T17:19:57+11:00'
author: 'Steve Cassidy'
layout: post
guid: 'http://ic2-hcsvlab-galaxy-qa-vm.intersect.org.au/?p=160'
permalink: /2013/10/30/aero-ux-review-hcs-vlab/
categories:
    - News
---

\[This User Experience review of the HCS VLab code is posted with the permission of the Author and [AeRO](http://www.aero.edu.au/ "Australian eResearch Organisations."), the group who commissioned the review\]

```
Reviewer:     Sam Wolski,
              eResearch Services, Griffith University
              s.wolski@griffith.edu.au

OS:           OSX 10.8.2

Browser:      Chrome 29.0.1547.65
 
Test Case(s): Supplied ‘HCS vLab Testing August’ document.
```

### Preliminary Comments:

The HCS vLab is easily one of the best interfaces I’ve come across in Australian research projects and eResearch applications. The Bootstrap framework is a great development platform and the workflows and interfaces of the HCS vLab have been integrated well to form a beautifully clean and usable application. The following feedback is intended to provide a list of small improvements to the application.

### Review Feedback:

1. Home page – large unused area adjacent to the facet column. Area contains a very brief title and slogan, but could be better used for some short tutorial content or even call-to-actions for your most sought-after collections. Definitions of each facet may also be useful.
2. No hover state on header logo. Suggest adding something subtle. E.g. A transparent white background color (5-10%) or slight opacity change on the logo itself.
3. After selecting a facet item during a search, in some circumstances I’m able to select another item from that facet to return a greater number of results. However, in other circumstances selecting a facet hides the remaining items from that facet. *E.g. Select ‘spoken’ under the ‘Mode’ facet. Modes ‘D’ and ‘TV’ remain as possible filters. By contrast, select ‘dialogue’ under the ‘Interactivity’ facet. All other ‘interactivity’ filters are removed.* *The app CSS effectively demonstrates active selections and possible new selections, but that functionality is inconsistent. If possible, multiple items should always be selectable to add to the returned results.*
4. Item view template – large empty space in right. Content area is ‘span9’ class, recommend either extending to ‘span12’ or preferably split the content into two columns to reduce page height (E.g. item details in ‘span8’ and file table in ‘span4’).
5. Item view template – lack of footer is slightly conflicting and can make the bottommost content easy to miss. Suggest using a simple footer (such as the search interface footer) and keeping it consistent throughout the application templates.
6. Suggest adding some horizontal padding between fields in ‘Item lists’ template search form.
7. ‘Item lists’ template search form would benefit from some validation for blank submissions and from some contextual placeholders on the search input. (E.g. When a user selects the *‘Created’ facet the input’s placeholder could be changed to display ‘YYYY – YYYY’ to suggest the correct input format to users).*
8. Sentence Segmenter tool in Galaxy incorrectly recognizes periods within quotation marks to be the end of the parent sentence. This could be useful if it also recognized the beginning of the quoted sentence otherwise it causes inconsistent results.
9. Test 10.8 failed for me. No errors or output in the browser console. According to the tests, the partial play buttons should play only the selected segment of video. For me it would only resume playing, as if I had simply clicked the play button after pausing. Selecting a segment during play had no effect at all.
10. Test 10.10 &amp; 10.11 failed for me. No sections were highlighted at all during play and segmented play had the same problem as 10.8.
11. The Galaxy tool would benefit greatly from the HCS vLab’s Bootstrap-based styles and interface framework. If it is within the project’s scope, it will be a welcome addition. A consistent colour scheme between the two would also be useful.

### Conclusion:

It was quite difficult to find implementable suggestions during this review because the application has such a well-developed and well-designed interface. Application tools appear contextually in locations users will be expecting them and the faceted search interface has almost no learning curve. Item lists and searches are clean and simple, with wonderful typographic hierarchy. For the most part, the feedback outlined above is for minor changes that can hopefully be applied easily to this already outstanding UI.