#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2014, Baidu Inc.
# Author: Zhong Yi <zhongyi01@baidu.com>

import sys
from HTMLParser import HTMLParser

filtered_tags = ['meta', 'div']

class EvernoteHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self) 
    self.list_prefix_ = []

  def handle_starttag(self, tag, attrs):
    if tag in filtered_tags:
      return

    if tag == 'ul':
      self.list_prefix_.append('- ')
    elif tag == 'ol':
      self.list_prefix_.append('1. ')
      print ''
    elif tag == 'li':
      print ''.join(self.list_prefix_),

      
    # print '<' + tag,
    # if tag == 'a':
      # print attrs[0][1],

  def handle_endtag(self, tag):
    if tag in filtered_tags:
      return

    if tag == 'ul' or tag == 'ol':
      self.list_prefix_.pop()
    elif tag == 'b':
      print '\n===================================================================================='
    elif tag == 'font' or tag == 'br':
      print '',
    elif len(self.list_prefix_) > 1:
      print '',
    else:
      print ''


    # print tag +  '>'

  def handle_data(self, data):
    if data == "\n":
      return 

    print data,

html = open(sys.argv[1], 'rb').read()
parser = EvernoteHTMLParser()
# parser.feed("<html><head><title>Test</title></head>"
    # "<body><h1>Parse me!</h1></body></html>")
parser.feed(html)
