# -*- coding: utf-8 -*-
"""Handles packaging, distribution, and testing."""


#import ez_setup
#ez_setup.use_setuptools()

from setuptools import setup


setup(

# Basic package information.
name = 'reddit-top',
version = '1.0',
scripts = ['reddit_top'],
py_modules = ['pyredditstories', 'BeautifulSoup'],

# Packaging options.
zip_safe = False,
include_package_data = True,

# Metadata for PyPI.
author = 'Peteris Krumins',
author_email = 'peter@catonmat.net',
license = 'GPL',
url = 'http://www.catonmat.net/blog/follow-hacker-news-from-the-console/',
keywords = 'hacker news cli',
description = 'A top-like program for monitoring stories on hacker news.',
long_description = open('readme.txt').read()

)

