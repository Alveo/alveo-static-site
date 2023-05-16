---
title: 'Using Alveo Data with EMU/R'
date: '2014-08-01T18:09:32+10:00'
author: peterr
layout: help
---

EMU is a speech processing package which runs in the free R statistical computing and graphics environment. (See the [Alveo HELP](/alveo-help "Alveo Help") page for more background on EMU/R and and the R environment.)

## **Installation of EMU/R**

Before you can use EMU/R you need to install R, EMU, the EMU prerequisite packages and the Alveo R library. These are all available for free download from the internet.

### Installing R

You will need to download and install R from the local mirror . Version 3.0.2 or later is required.

Installation of the R Base package is sufficient. Downloads for Mac, Windows and Linux are available.

### Installing EMU and its prerequisite packages

After successfully installing R, you must download and install EMU and its prerequisite packages. These must be installed into your R environment. Again, downloads for Mac, Windows and Linux are available.

Instructions for installation can be found at  on the GitHub open source repository. These instructions direct you to download and install the following components.

| **alveo** | The Alveo R Library, which accesses the Alveo web service and downloads your Alveo the Documents from your Item List into the R environment. |
|---|---|
| **emuSX** | The core of the EMU/R speech analysis package |
| **wrassp** | This library is required by emuSX and the Alveo R Library |
| **websockets** | This library is required by emuSX and the Alveo R Library |

## **Using Your Data in EMU/R**

Alveo does not launch EMU (unlike the way Alveo launches Galaxy / Alveo). Instead, Alveo provides the details which you need in your EMU/R environment to access the data in your Alveo Item List.

To Access Alveo Data in EMU/R…

- **Click** on **Item Lists** in the Alveo Navigation Bar. The names of your available Item Lists will be displayed.
- **Click** on the name of the Item List you want to access in EMU/R. The Items in this Item List will be shown.
- **Click** Item List Actions and select **Use in EMU/R** from the dropdown menu which is displayed. The **Use *&lt;Item List&gt;* in EMU/R** dialog (shown below) will be displayed.
- **Click** Download API key config file. A file save dialog will appear. Save the alveo.config file into the directory recommended in the dialog for your operating system. (**&lt;user&gt;** means your computer login User Name. The directory should already exist.)
- **Drag** the cursor over the R code in the lower part of the dialog to highlight it.
- **Press** Ctrl+C to copy the R code to the clipboard.
- **Click** Close to close this dialog.
- **Launch** the R environment on your computer (independently from Alveo).
- **Paste** the clipboard text into the R console window. You may need to press Enter to get the last command to execute.

![EMUDialog](/assets/files/2014/08/EMUDialog.png)

- Your Item List Documents will appear in your R environment as a data structure under the item\_list variable.
- The API Key only needs to be exported once, unless you have subsequently regenerated your API Key.

Further operation of R is beyond the scope of this Help. You can refer to the pages linked on the main [Alveo HELP](/alveo-help "Alveo Help") page.
