---
title: 'Getting Started with Galaxy'
date: '2014-08-01T12:00:05+10:00'
author: peterr
layout: page
---

## **The Galaxy Screen**

The Galaxy operation screen generally has this configuration.

![GalaxyScreen](/assets/files/2014/08/GalaxyScreen.png)

You can return to this screen by clicking **Analyze Data** in the Galaxy Navigation Bar.

## **Running Tools**

When you run a tool, it generally uses one of your loaded datasets (which are listed in the History Panel) as **input**.

Tools run as **background processes**. That is, after you click on Execute, the operation screen clears and shows a Galaxy logo while the tool runs. You can do other Galaxy operations while you wait for this Tool to complete its processing. The Tool’s execution is indicated in the History Panel by the output file name and a rotating processing icon of dots.

When Tool processing completes, the **output** file’s name is displayed at the top of the file list in the History Panel. You can click on it to see its details or use it as input for running another tool.

You can run multiple tools simultaneously, provided that one does not rely on the output of another.

To Run a Tool…

- **Click** on the Group Name of the Tool Group which contains this Tool to open that group and display the names of the Tools it contains.
- **Click** on the name of the Tool you want to run. Its parameter will be displayed in the Operation Panel.
- **Select** the input file/s you require by clicking in the input file name parameter control and selecting the correct file from the drop down list. Some Tools are restricted in the type of file they can operate on. For example, they may only be able to operate on text input.
- **Enter** the other parameters you require, by clicking in each of their controls or using Tab to skip between them.
- **Click** Execute to start the tool processing. The Tool’s parameters will clear from the Operation Panel.
- **Wait** for the Tool to complete processing before using its output file. You can run another Tool, or examine output files while you wait.



## **Managing Your Datasets**

Datasets stored in Galaxy have **metadata** stored for them, including optional tags and annotation, which you can use to help you remember what the file is for. Information about the date and time the dataset was created, how it was created and what it contains are also stored.

There are a number of icons shown against each file in the History Panel. Some are not shown until you click on the file name to view its details. If you move your mouse over them, you will see tool-tips which explain their use. Here are few commonly used ones.

![GalaxyFileIcons](/assets/files/2014/08/GalaxyFileIcons.png)