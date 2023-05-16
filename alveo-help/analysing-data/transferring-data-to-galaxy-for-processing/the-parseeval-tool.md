---
title: 'The ParseEval Tool'
date: '2014-08-01T17:37:18+10:00'
author: peterr
layout: help
---

ParseEvaL is a tool developed by Dr. Jason A. Shaw of the University of Western Sydney and Prof. Adamantios I. Gafos of the University of Potsdam.

ParseEval has been integrated into Galaxy / Alveo as a Galaxy Tool. You can run it in the same manner as other Galaxy Tools.

## **Running ParseEval**

You must be running Galaxy to use this tool.

To Run ParseEval…

- **Click** on **Analyze Data** to show the Analyze Data screen, unless it is already showing.
- **Click** on **ParseEval** in the Tools panel on the left hand side of the screen. The Tools Group will open, although it contains only the ParseEval Tool.
- **Click** on the ParseEval Tool name. The ParseEval parameters will be shown in the Operation Panel. There are about 15 numeric parameters and an output file name.
- **Enter** the parameter values you require.
- **Enter** the name of the output file your require.
- **Click** on Execute to start the processing.



- The numeric ParseEval are parameters are defaulted to zero. These are not reasonable values, so users must set meaningful values into these parameters.
- The meaning of the ParseEval parameters is beyond the scope of this Help. If you require further information on these parameters, please see the references at the end of the Help page.

## **ParseEval Background**

Languages that differ in syllable structure have been shown to differ as well in patterns of articulatory coordination, e.g., Georgian vs. Berber (Goldstein et al., 2007), English vs. Arabic (Shaw and Gafos, 2010). Relevant articulatory data has recently been collected on a range of languages including Slovak, Romanian, English, German, Arabic, Italian, Maltese, Serbian and Berber; however, the measurements used to diagnose articulatory coordination can vary from study to study (Tilsen et al., 2013) and sometimes give conflicting results (Shaw et al., 2009).

ParseEval is a tool for diagnosing patterns of articulatory coordination related to syllable structure from speech movement data. Given a set of parameters estimated from the data it simulates the range of stability patterns arising from two different coordination patterns, the pattern characteristic of syllables with complex syllable onsets and the pattern characteristic of languages that prohibit complex syllable onsets, i.e., simplex onsets (Shaw et al., 2011). The simulated stability patterns are then evaluated for goodness of fit against the stability pattern input to ParseEval. A description of the evaluation procedure is provided in Shaw and Gafos (2010). Analytical expressions are reported in Gafos et al., (2014).

ParseEval assumes the temporal alignment patterns schematized in Figure 1 correspond to simplex (a) and complex (b) syllables. The key difference between the simplex and complex temporal alignment schemas is in the relative timing of the vowel to the pre-vocalic consonants. To use ParseEval you must input the stability of the three intervals, right edge to anchor, centre to anchor, and left edge to anchor intervals (see Shaw et al., 2009 for definitions and measurement procedure) expressed as relative standard deviation (RSD) as well as a set of lower level phonetic parameters, specified as constants, kp , kipi, kvowel, and associated error terms ,ɛp , ɛipi. The constants can be set to mean measurements of the data and the error terms can be set to the standard deviation of those measurements. These values are requested as inputs from the ParseEval menu in Galaxy/Alveo (Figure 1, Right). Inquiries about using ParseEval can be directed to Jason Shaw at J.Shaw@uws.edu.au.

## **Acknowledgements** 

ParseEval was developed by Dr. Jason A. Shaw of the University of Western Sydney and Prof. Adamantios I. Gafos of the University of Potsdam. Work on ParseEval has been support in part by the European Research Council (E Advanced Grant STIMOS 249440), Australian Research Council (DECRA, DE120101289) and the National Science Foundation (Grant No. 0922437). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## **References**

Gafos, A. I., Charlow, S., Shaw, J. A., &amp; Hoole, P. (2014). Stochastic time analysis of syllable-referential intervals and simplex onsets. Journal of Phonetics, 44, 152-166.

Goldstein, L., Chitoran, I., &amp; Selkirk, E. (2007, August). Syllable structure as coupled oscillator modes: evidence from Georgian vs. Tashlhiyt Berber. In Proceedings of the XVIth international congress of phonetic sciences (pp. 241-244).

Shaw, J. A., &amp; Gafos, A. I. (2010). Quantitative evaluation of competing syllable parses. In Proceedings of the 11th Meeting of the ACL Special Interest Group on Computational Morphology and Phonology (pp. 54-62). Association for Computational Linguistics.

Shaw, J., Gafos, A. I., Hoole, P., &amp; Zeroual, C. (2009). Syllabification in Moroccan Arabic: evidence from patterns of temporal stability in articulation. Phonology, 26(01), 187-215.

Shaw, J. A., Gafos, A. I., Hoole, P., &amp; Zeroual, C. (2011). Dynamic invariance in the phonetic expression of syllable structure: a case study of Moroccan Arabic consonant clusters. Phonology, 28(03), 455-490.

Tilsen, S., Zec, D., Bjorndahl, C., Butler, B., L’Esperance, M. J., Fisher, A., … &amp; Sanker, C. (2012). A cross-linguistic investigation of articulatory coordination in word-initial consonant clusters (pp. 51-81). Cornell Working Papers in Phonetics and Phonology.