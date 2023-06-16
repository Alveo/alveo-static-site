---
title: 'Training a Speech Recogniser with HCS vLab'
date: '2014-02-03T15:16:47+11:00'
author: 'Steve Cassidy'
layout: post
permalink: /2014/02/03/training-a-speech-recogniser-with-hcs-vlab/
categories:
    - News
---

I just received a report from Matt Atcheson, one of our HDR testers at UWA, with the results of some work he’s done on evaluating the HTK integration with the HCS vLab. Matt used [my template Python interface](https://bitbucket.org/stevecassidy/hcsvlab_api_testing) to download audio files from the vLab and feed them to the HTK training algorithms to train a digit string recogniser. He was then able to test the recogniser on unknown data also downloaded from the vLab.

The results were interesting:

> Using the full set of digit recordings that I could find (about 940 of them), setting aside 10% for testing, and with a grammar that constrains transcripts to exactly four digits, I get about 99% word accuracy, and about 95% sentence accuracy.

> ====================== HTK Results Analysis =======================

 Date: Tue Jan 28 21:08:50 2014

 Ref : &gt;ntu/hcsvlab_api_testing_matt/digitrec/data/testing_files/testref1.mlf

 Rec : &gt;buntu/hcsvlab_api_testing_matt/digitrec/data/testing_files/recout.mlf

———————— Overall Results ————————–

SENT: %Correct=94.74 [H=90, S=5, N=95]

WORD: %Corr=98.95, Acc=98.42 [H=564, D=3, S=3, I=3, N=570]





Matt also gave us some good feedback based on his experiments. If there are other testers interested in trying to repeat this experiment or explore a bit on their own, Matt’s code is [available on BitBucket](https://bitbucket.org/mhongkong/hcsvlab_api_testing_matt/overview).



To run his experiments, Matt made use of a virtual machine on the [Nectar Research Cloud](http://nectar.org.au/research-cloud). Any Australian researcher can login to the cloud and get a free allocation of virtual machines. We’ve made a VM image (called ‘HCSvLab Tools’, listed in the Public list of snapshots on your dashboard) that has HTK, DeMoLib and INDRI pre-installed; as a user, you can create your own instance of this image and start working with these tools.







