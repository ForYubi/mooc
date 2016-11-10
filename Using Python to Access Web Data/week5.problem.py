# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:05:59 2016

@author: yubi
"""
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib.request

sampleData = 'http://python-data.dr-chuck.net/comments_42.xml'
actualData = 'http://python-data.dr-chuck.net/comments_303859.xml'

try:
    url = urllib.request.urlopen(sampleData)
    #soup = BeautifulSoup(url.read().decode('utf-8'), 'html.parser')
    #tags = soup.find_all('count')
    #print(tags)
    #print(sum(int(tag.string) for tag in tags))
    tree = ET.fromstring(url.read().decode('utf-8'))
    '''
    results = tree.findall('.//count')
    for item in results:
        print(type(item.text))
    '''
    results = tree.findall('.//count')
    for items in results:
        print(int(items.text))

except urllib.request.HTTPError as error:
    print(error)