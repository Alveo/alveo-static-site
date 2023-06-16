---
title: 'New Version of Pyalveo Module Released'
date: '2016-07-24T23:11:08+10:00'
author: 'Steve Cassidy'
layout: post
permalink: /2016/07/24/new-version-of-pyalveo-module-released/
categories:
    - News
---

Pyalveo is the Python module that interfaces to the Alveo web API to allow automation of any task relating to Alveo. I have just made a [new version (0.5) available on PyPI](https://pypi.python.org/pypi/pyalveo/0.5), the Python package repository (you can also find it [on Github](https://github.com/Alveo/pyalveo)). The main changes in this release are:

- Supports both Python 2.7 and 3.4
- Adds support for creating new collections (for data owners)
- Adds support for adding new items and documents
- Behind the scenes changes to make the module more robust
- Tests now use mock requests so can be run without an API key

The package now includes a few example scripts that use the upload API to create new collections. While these are intended for developers to make use of, we’re working on some user-level tools to help you contribute your data to Alveo in the near future.