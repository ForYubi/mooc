# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding:utf-8
"""
Created on Tue Nov  8 19:34:55 2016

@author: yubi
"""
import re
import urllib.request

sampleUrl = 'http://python-data.dr-chuck.net/regex_sum_42.txt'
actualUrl = 'http://python-data.dr-chuck.net/regex_sum_303857.txt'

response = urllib.request.urlopen(actualUrl)

text = response.read().decode('utf-8')

numList = re.findall('[0-9]+', text)

print(numSum = sum(map(int, numList)))
#554392
'''
#from urllib.request import urlretrieve

urllib.request.urlretrieve(sampleUrl, 'sampleData.txt')
with open('sampleData.txt', 'r') as dataFile:
    print(dataFile.read())
'''
