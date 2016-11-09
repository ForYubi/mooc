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
    urlInput = input("Enter - ")
    if len(urlInput) < 1 :
        url = urllib.request.urlopen(sampleData)
    else:
        url = urllib.request.urlopen(urlInput)
    data = url.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find_all('span')
    print('Count', len(tags))
    print('Sum', sum(int(tag.contents[0]) for tag in tags))
except urllib.request.HTTPError as error:
    print(error)