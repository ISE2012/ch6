# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:50:47 2020

@author: ucobiz
"""

inputObj = open("newfile.txt") 
outputObj = open("output-newfile.txt", "w")

# convert the sentence into UPPERCASE
for sentence in inputObj:
    newSentenceUpper = sentence.upper()
    outputObj.writelines(newSentenceUpper)

inputObj.close()
outputObj.close()
