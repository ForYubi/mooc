# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding:utf-8
"""
Created on Tue Nov  8 19:34:55 2016

@author: yubi
"""
import re
import urllib.request
#from urllib.request import urlretrieve

sampleData = 'http://python-data.dr-chuck.net/regex_sum_42.txt'
actualData = 'http://python-data.dr-chuck.net/regex_sum_303857.txt'

sampleData = 'http://python-data.dr-chuck.net/regex_sum_42.txt'
actualData = 'http://python-data.dr-chuck.net/regex_sum_303857.txt'

urllib.request.urlretrieve(sampleData, 'test1.txt')
with open('test1.txt', 'r') as newFile:
    print(newFile.read())

#url = 'http://example.com/'
response = urllib.request.urlopen(sampleData)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
for items in text:
    print(type(items))
'''
g = urllib.request.urlopen('http://media-mcw.cursecdn.com/3/3f/Beta.png')
with open('test.png', 'b+w') as f:
    f.write(g.read())

file = open('myfile.dat', 'w+')
with urllib.request.urlopen(sampleData) as urlFile:
    file.write(urlFile.read())

response = urllib.request.urlopen(sampleData)
html = response.read().decode('utf-8')
print('Retrieved', len(html), 'characters')
'''
'''
#print(html)
for line in html:
    numberList = re.findall('[0-9]+?', line)
    print(numberList)

'''