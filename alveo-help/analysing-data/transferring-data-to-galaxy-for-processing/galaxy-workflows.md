---
title: 'Galaxy Workflows'
date: '2014-08-12T13:44:48+10:00'
author: peterr
layout: help
---

Galaxy offers this very powerful tool for chaining together the processing of multiple tools to run in a single background operation. Workflows are very powerful, so creating and configuring them is necessarily not trivial.

Here is a quick set of steps to create a basic workflow, but you will definitely also need to see the [Galaxy Project Workflow Help](https://wiki.galaxyproject.org/Learn/#Shared_Pages.2C_Histories_.26_Workflows) for more information.

To Create a Workflow…

- **Click** on **Workflow** in the Galaxy Navigation Bar.
- **Click** Create New Workflow to show the parameters for creating a new workflow.
- **Enter** a name for your new Workflow.
- **Click** Create to add it as an empty workflow to your list of workflows. The list will be displayed.
- **Click** on your new workflow’s name to see a dropdown list of actions, and select **Edit** from the dropdown menu. The workflow edit screen is displayed, showing the Galaxy Tools on the left, the gridded Workflow Canvas in the centre and the workflow component parameter panel on the right. See the example below.
- **Click** in the left panel on the names of the Tools you want to add to your workflow. They will appear as boxes on the Workflow Canvas.
- **Drag** the small outward pointing arrow of a Tool in the Workflow Canvas to the inward pointing arrow of another Tool to create a data pipe (a “noodle” in Galaxy jargon) between the two.
- **Click** on a Tool in Workflow Canvas to see and edit its run-time parameters in the right hand panel.
- **Click** on the one of the **Workflow Control** options at the bottom of the left hand panel to add it to your workflow.
- **Click** on the small black cog icon at the top right of the gridded Workflow Canvas to see a dropdown menu which allows you to **Save**, **Close** or **Run** your workflow.



![GalaxyWorkflowEdit](/assets/files/2014/08/GalaxyWorkflowEdit.png)