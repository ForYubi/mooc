# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:05:59 2016

@author: yubi
"""
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib.request
import re

sampleData = 'http://python-data.dr-chuck.net/comments_42.xml'
actualData = 'http://python-data.dr-chuck.net/comments_303859.xml'

try:
    url = urllib.request.urlopen(actualData)
    #soup = BeautifulSoup(url.read().decode('utf-8'), 'html.parser')
    #tags = soup.find_all('count')
    #print(tags)
    #print(sum(int(tag.string) for tag in tags))
    results = re.findall('<count>([0-9]+)</count>', url.read().decode('utf-8'))
    print(sum(map(int, results)))
    '''
    tree = ET.fromstring(url.read().decode('utf-8'))
    results = tree.findall('.//count')
    print(sum(int(item.text) for item in results))
    '''
    '''
    results = tree.findall('.//count')
    for item in results:
        print(type(item.text))
    '''

except urllib.request.HTTPError as error:
    print(error)