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
newdestPath=[]
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
                directory = ((firstLevel + '\\' + 'sourceFolders' + '\\' + 'unknownItem_' + str(z) + '_'))
                while os.path.exists(directory) == True:
                    z+=1
                    directory = ((firstLevel + '\\' + 'sourceFolders' + '\\' + 'unknownItem_' + str(z) + '_'))
                newdestPath = (directory + '\\' + 'unknownItem_' + str(z) + '_.jpg' )
                os.makedirs(directory)
                shutil.move(thirdLevel, newdestPath)            
                #newfiles.append(newdestPath)
fileOrganizerFunc(keyword)
def jpgFinder():
    firstLevel = 'C:\\CSVFiles\\SourcePics'
    secondLevel ='null'
    thirdLevel ='null'
    Newdirectory = (firstLevel + '\\' + 'sourceFolders')
    for i in os.listdir(Newdirectory):
        secondLevel = (Newdirectory + '\\' + i)
        for j in os.listdir(secondLevel):
            thirdLevel = (secondLevel + '\\' + j)
            #print thirdLevel
            newdestPath.append(thirdLevel)
jpgFinder()           