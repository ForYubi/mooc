# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 00:36:36 2016

@author: yubi
"""

from bs4 import BeautifulSoup
import urllib.request
'''
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
try:
    link = urllib.request.urlopen(url)
    soup = BeautifulSoup(link.read().decode('utf-8'), 'html.parser')
    #print(soup)
    tags = soup.find_all('a')
    for tag in tags:
        print(tag.get('href', None))
except urllib.request.HTTPError as error:
    print(error)
'''   
def hrefSwith(url, position):
    try:
        link = urllib.request.urlopen(url)
        soup = BeautifulSoup(link.read().decode('utf-8'), 'html.parser')
        return soup.find_all('a')[position - 1].get('href', None)
    except urllib.request.HTTPError as error:
        print(error)

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/known_by_Anish.html'
for times in range(int(count) + 1):
    print('Retrieving:', url)
    url = hrefSwith(url, int(position))
    