#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stephen McCullough'
SITENAME = 'pyBelfast'
SITEURL = ''

PATH = 'content'

ARTICLE_URL = 'meetup/{slug}'
ARTICLE_SAVE_AS = 'meetup/{slug}/index.html'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = (
  ('Home','/index.html'),
  ('About','/pages/about.html'),
  ('Meetup','/category/meetup.html')
)
