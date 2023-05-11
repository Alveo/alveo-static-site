---
id: 823
title: 'What’s an API Key?'
date: '2014-07-18T12:07:20+10:00'
author: peterr
layout: page
guid: 'http://alveo.edu.au/?page_id=823'
---

<aside class="panel panel-default aside"><div class="panel-body">Because the API Key acts like a password, you are advised against allowing others to use your API Key.</div></aside>Alveo permits access to its Collections directly by programs which use Alveo’s HTTP web <abbr title="Application Programming Interface">API</abbr>. (See [HTTP API Reference](http://alveo.edu.au/alveo-help/http-api-reference/) for details of the operation of this API.)

However, programs must also have authority to use an Alveo account in order to access Alveo data. They must present an API Key to Alveo to demonstrate this authority. This key is a sequence of apparently meaningless characters which acts like a combined User Name and Password for an Alveo account.

On creation your Alveo account does not have an API Key, but every account can generate and view their API Key.

<section class="panel panel-default instructions"><div class="panel-title">To generate an API key for your account…</div><div class="panel-body">- **Click** on your email address at the top right of the main screen to show the Administration options menu.
- **Move** the mouse over **API Key** in the menu which is displayed. The API Key sub-menu is displayed.
- **Click** on **Regenerate API Key** in this sub-menu. A unique API Key will be stored for your account.

</div></section><section class="panel panel-default instructions"><div class="panel-title">To view your account’s API key…</div><div class="panel-body">- **Click** on your email address at the top right of the main screen to show the Administration options menu.
- **Move** the mouse over **API Key** in the menu. Your account’s API Key is displayed at the top of the sub-menu in grey, as shown below.

</div></section>![APIKey](http://bigasc.science.mq.edu.au/wp-content/uploads/2014/07/APIKey.png)

When you access Galaxy from the Alveo menus, this string of characters is automatically passed to Galaxy so that it can use it to access Alveo for your data requests. To use EMU/R you need to load this API Key into the R environment. See [Using Alveo Data with EMU/R](http://alveo.edu.au/alveo-help/analysing-data/using-alveo-data-with-emur/) for more information. This API Key can also be used by other programs which require Alveo access. Use the **Copy to Clipboard** sub-menu item to allow pasting into other applications, or the **Download API Key** sub-menu item to download a small file (named `alveo.config`) which can be used by other tools (for example, Java, R or Python tools) to access your Alveo data.

If you believe your API Key has been compromised, generate a new one using the **Regenerate API Key** sub-menu item. The old API Key will be disabled and the new one will now be used for Galaxy access. You will also need to update the API Key value in any programs or scripts which use your old one.

If you do not want to have an API Key, select **Delete API** Key from the sub-menu. Your API Key will be deleted and not re-generated, so no API Key will be available for your Alveo account. You will not be able to use Galaxy / Alveo nor import data to EMU/R until you generate a new API Key.