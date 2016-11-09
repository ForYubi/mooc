# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:33:23 2016

@author: yubi
"""
import socket
import urllib.request

url = 'http://data.pr4e.org/intro-short.txt'

'''
try:
    response = urllib.request.urlopen(url)
    print(response.getcode())
    print(response.geturl())
    print(response.info())
except urllib.request.HTTPError as error:
    print(error)
#html = response.read()
'''
domain = 'data.pr4e.org'
mysock = socket.socket()
mysock.connect((domain, 80))
mysock.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512).decode('utf-8')
    if len(data) < 1:
        break
    print(data)
mysock.close()

