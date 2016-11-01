# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:49:39 2016

@author: yubi
"""

import string

class Message(object):
    
    def __init__(self, text = None):
        self.message = text
        self.cipherText = None
        
    def __str__(self):
        return self.message
        
    def isWord(self, char):
        return char in string.ascii_letters
        
    def cipher(self, cipherNum):
        alphabet = string.ascii_lowercase * 2 + string.ascii_uppercase * 2
        for letter in self.message:
            if self.isWord(letter):
                self.cipherText += alphabet[alphabet.index(letter) + cipherNum]
            else:
                self.cipherText += letter
                
    def getCipherText(self):
        return self.cipherText
            
        
        
class PlaintextMessage(Message):
    
    def encrypt(self, encryptNum):
        self.cipher(encryptNum)
        
    
class CiphertextMessage(Message):
    
    def decrypt(self, decryptNum):
        self.cipher(decryptNum)
 