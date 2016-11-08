# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:34:55 2016

@author: yubi
"""
import re
import urllib.request


sampleData = 'http://python-data.dr-chuck.net/regex_sum_42.txt'
actualData = 'http://python-data.dr-chuck.net/regex_sum_303857.txt'

response = urllib.request.urlopen(sampleData)
html = response.read()

line = '3036 many reasons, ranging from making your living to solving 7209'
numberList = re.findall('[0-9]+', line)
print(numberList)

'''
#print(html)
for line in html:
    numberList = re.findall('[0-9]+?', line)
    print(numberList)

'''