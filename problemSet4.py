# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:11:24 2016

@author: Administrator
"""
import string
import random

def getRandomList(n = 7):
    return [random.choice(string.ascii_lowercase) 
            for times in range(n)]
    
def getWordsDict(filename):
    try:
        fopen = open(filename, 'r')
    except IOError:
        print('Failed to open the file %s.'%filename)
    else:
        return fopen.read().split()
    finally:
        fopen.close()

def isWordInList(word, nList):
    '''
    #copyList = nList
    copyStr = ''.join(nList)
    try:
        for letters in word:
            if letters in nList:
                nList.remove(letters)
            else:
                nList = [items for items in copyStr]
                print('else, ', copyStr)
                return False
    except:
        nList = [items for items in copyStr]
        print('except, ', copyStr)
        return False
    else:
    ---------------------------------
    for letters in word:
        if not letters in nList:
            return False
    lastList = [items for items in nList]
    for letters in word:
        try:
            nList.remove(letters)
        except:
            nList = lastList
            return False
    return True
    '''
    copyList = nList[:]
    for letters in word:
        if letters in copyList:
            copyList.remove(letters)
        else:
            return False
    return True
        
def scoresValue(word):
    valueDict = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    #for letters in string.ascii_lowercase:
    #    valueDict[letters] = 1
    
    value = 0
    if len(word) == 7:
        value += 50
    for letters in word:
        value += valueDict[letters]
    return value
    
def getScores(wordsDict, nList, word):
    '''
    isWordInList:remove adjust, and failed
    '''
    #copyList = nList[:]
    if word in wordsDict:
        if isWordInList(word, nList):
            #wordDelete(nList, word)
            score = scoresValue(word)
            print('"%s" earned %d points.'%(word, score), end = '')
            for letters in word:
                nList.remove(letters)
            return score
        else:
            print('Invalid word, please try again.')
    return 0
    
def game(wordsDict, nList):
    #lastList = [items for items in nList]
    lastList = nList[:]
    scores = 0
    print('Current Hand:', ''.join(letter+' ' for letter in nList ))
    
    messageInfo = 'Enter word, or a "." to indicate that you are finished: '
    word = input(messageInfo)
    while word != '.':
        scoreOnce = getScores(wordsDict, nList, word)
        if scoreOnce:
            print('Total: %d points'%scores)
            if not len(nList):
                print('Run out of letters.', end=' ')
                break
        print('Current Hand:', ''.join(letter+' ' for letter in nList ))
        word = input(messageInfo)
    print('Total score: %d points.'%scores)
    nList = lastList
        
filename = 'words.txt'
wordsDict = getWordsDict(filename)
'''
for index, item in enumerate(wordsDict):
    if index < 10:
        print('{} {}'.format(index, item))
'''
#nList = getRandomList()
choiceItem = None
messageStr = ('Enter n to deal a new hand, '
             'r to replay the last hand, '
             'or e to end game: ')

while choiceItem != 'e':
    if choiceItem == 'n':
        #game(wordsDict, nList = getRandomList())
        nList = getRandomList()
        lastList = [items for items in nList]
        game(wordsDict, nList)
    if choiceItem == 'r':
        game(wordsDict, lastList)
    choiceItem = input(messageStr).lower()
             