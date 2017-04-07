# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 06:32:10 2017

@author: samir
"""

import os
import shutil
newfiles = []
keyword = 'jpegs'
resolution = 10
#from SorterMain import keyword, resolution
def fileOrganizerFunc(keyword):
    firstLevel = 'C:\\CSVFiles\\SourcePics'
    secondLevel ='null'
    thirdLevel ='null'
    newdestPath='null'
    z = 1
    for i in os.listdir(firstLevel):
        if (i.find(keyword) != -1) or keyword == 'null':
            secondLevel = (firstLevel + '\\' + i)
            for j in os.listdir(secondLevel):
                thirdLevel = (secondLevel + '\\' + j)
                print thirdLevel
                newdestPath = (firstLevel + '\\' + 'sourceFolders' + '\\' + 'unknownItem_' + str(z) + '_\\' + 'unknownItem_' + str(z) + '_.jpg' )
                os.makedirs((firstLevel + '\\' + 'sourceFolders' + '\\' + 'unknownItem_' + str(z) + '_'))
                shutil.move(thirdLevel, newdestPath)            
                newfiles.append(newdestPath)
                z+=1
fileOrganizerFunc(keyword)