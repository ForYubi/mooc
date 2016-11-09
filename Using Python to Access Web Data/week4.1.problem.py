# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:24:09 2016

@author: yubi
"""

import urllib.request
from bs4 import BeautifulSoup

sampleData = 'http://python-data.dr-chuck.net/comments_42.html'
actualData = 'http://python-data.dr-chuck.net/comments_303862.html'

try:
    url = urllib.request.urlopen(sampleData)
    data = url.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find_all('span')
    #print(tags)
    #for tag in tags:
        #print(tag.contents[0])
    print(sum(int(tag.contents[0]) for tag in tags))
except urllib.request.HTTPError as error:
    print(error)
