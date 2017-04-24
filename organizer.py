# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 06:32:10 2017

@author: samir
"""
'''

 serves as the start of the training module, 
 after you select the origin, 
 the script will move all of the images from originDir[variables] to a new folder with an Unknown name for transparency purposes.


'''
import os
import shutil
from variables import originDir, firstLevel, jpegArray, typeOsource

#changes the name of the files to Unknown_N and moves them to the folder firstLevel \\ typeSource
z = 1
for i in os.listdir(originDir):
    if (i.find('.jpg') != -1):
        jpegArray.append(originDir + '\\' + i)
if os.path.isdir(firstLevel+'\\'+typeOsource) != True:
    os.makedirs(firstLevel+'\\'+typeOsource)

for s in jpegArray:
    directory = ((firstLevel + '\\' + typeOsource + '\\' + 'unknownItem_' + str(z) + '_.jpg'))
    if os.path.isfile(directory) != True:
        shutil.move(s, directory)
    else:
        while os.path.isfile(directory) == True:
            z+=1
            directory = ((firstLevel + '\\' + typeOsource + '\\' + 'unknownItem_' + str(z) + '_.jpg'))
        shutil.move(s, directory)          
    print directory