# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 02:27:47 2017

@author: samir
"""
pathResize = 'C:\\Users\\samir\\Documents\GitHub\\Image_Resize_Outline_Exporter\\imageResize_and_Export_outline.py'
pathlookout = 'C:\\Users\\samir\\Documents\\GitHub\\FileLookout\\fileLookout.py'

#import os
import csv
import math
import fileLookout as flt
#from fileLookout import files
from imageResize_and_Export_outline import fileSource
#files=[]

keyword = 'porche911'
resolution = 50
exactRes = (resolution/10)-1
sourceArray = []
flt.fileLookupFunc(keyword)
def saveSource():
    with open(fileSource[exactRes]) as sourceCSV:
        sourceCSVreader = csv.reader(sourceCSV)
        for row in sourceCSVreader:
            sourceArray.append(row[0])
saveSource()
def probFinder():
    currentProbability = 0
    finalPotential = 0
    fFinal = 'null'
    for f in files:
        with open(f) as potentialCSV:
            potentialCSVreader = csv.reader(potentialCSV)
            if finalPotential<=currentProbability:
                finalPotential = currentProbability
                fFinal = f
            #print (f + " " + str(currentProbability))
            instantProbability = 0
            currentProbability = 0
            g = 0
            for row in potentialCSVreader:
                try:
                    if (int(row[0]) != 0) and (int(sourceArray[g]) != 0):
                        absVal = math.fabs(int(row[0]) - int(sourceArray[g]))
                        if absVal >= int(row[0]):
                            instantProbability = 0.001
                        else:
                            instantProbability = absVal / int(row[0])
                    else:
                        instantProbability = 1
                    currentProbability = ((currentProbability*(g+1)+instantProbability)/(g+2))
                    
                    g=+1
                except IndexError:
                    if finalPotential<=currentProbability:
                        finalPotential = currentProbability
                        fFinal = f
                    break
    print (fFinal + " " + str(finalPotential))
probFinder()
