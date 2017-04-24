# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 00:42:01 2017

@author: samir
"""
import os
from variables import files, keyword, resolution

def fileLookupFunc():
    firstLevelLookup = 'C:\\CSVFiles\\Sources'
    
    for i in os.listdir(firstLevelLookup):
        if (i.find(keyword) != -1) or keyword == 'null':
            secondLevel = (firstLevelLookup + '\\' + i)
            
            for j in os.listdir(secondLevel):
                if j.find(('RES_'+ str(resolution))) != -1:
                    thirdLevel = (secondLevel + '\\' + j)
                    
                    for k in os.listdir(thirdLevel):
                        if k.find(('outline_' + str(resolution) + 'pixels')) != -1:
                           # print (thirdLevel + '\\' + k)
                            newPath = (thirdLevel + '\\' + k)
                            files.append(newPath)
fileLookupFunc()