# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 00:42:01 2017

@author: samir
"""
import os
files = []
keyword = 'null'
resolution = 10
#from SorterMain import keyword, resolution
def fileLookupFunc():
    firstLevel = 'C:\\CSVFiles\\Sources'
    
    for i in os.listdir(firstLevel):
        if (i.find(keyword) != -1) or keyword == 'null':
            secondLevel = (firstLevel + '\\' + i)
            
            for j in os.listdir(secondLevel):
                if j.find(('RES_'+ str(resolution))) != -1:
                    thirdLevel = (secondLevel + '\\' + j)
                    
                    for k in os.listdir(thirdLevel):
                        if k.find(('outline_' + str(resolution) + 'pixels')) != -1:
                           # print (thirdLevel + '\\' + k)
                            newPath = (thirdLevel + '\\' + k)
                            files.append(newPath)
fileLookupFunc()