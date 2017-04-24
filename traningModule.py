# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:11:53 2017

@author: samir
"""

import os
import shutil
import cv2
import csv
from variables import fileSource, BLACK, typeOsource, firstLevelIMG, firstLevel, newdestPath, count


def csvWriter():
    img3 = cv2.imread(dst2)
    imgPathCSV = open((previousFilePath),"w+")
    writeToCsv = csv.writer(imgPathCSV, lineterminator = '\n')
    firstItemFound = 0
    for r in xrange (0,a):
        for c in xrange (1,a):
            if int(img3[r][a-c][1]) >= 1:
                if firstItemFound == 0:
                    firstItemFound = 1
                    row = r
                    column = c
                writeToCsv.writerow([(a-c)-column,(a-r)-row])
                break         
    for r2 in xrange (1,(a)):
        for c2 in xrange (0,(a)):
            if (img3[a-r2][c2][1]) >= 1:
                writeToCsv.writerow([((c2)-column),((r2)-row)])
                break    
    imgPathCSV.close


# creates an array with the jpegs paths.

testDirectory = (firstLevel + '\\' + typeOsource)
#print testDirectory
for i in os.listdir(testDirectory):
    secondLevel = (testDirectory + '\\' + i)
   # print secondLevel
    try:
        for j in os.listdir(secondLevel):
            thirdLevel = (secondLevel + '\\' + j)
    except WindowsError:
        thirdLevel = secondLevel
    #print thirdLevel
    newdestPath.append(thirdLevel)

for n in newdestPath:
    imgPath = n  # path to the JPEG
    #os.rename(imgPath,imgPath[:-4])
    a = 10  # initial pixel count
    imgEdgesMap = ((imgPath[:-4]) + 'edges.png')   # jpeg with the edges 
    img = cv2.imread(imgPath) # module to read image from the JPEG
    gray1 = cv2.Canny(img, 200, 200) # module to turn image to gray scale
    dst2 = ((imgPath[:-4]) + '_' + str(a) + 'pixels' + '.png') 
    cv2.imwrite(imgEdgesMap, gray1)
    img2 = cv2.imread(imgEdgesMap)    
    img3 = cv2.imread(dst2)
    numRows = len(img)
    numCols = len(img[0])


    if numRows > numCols:
        squareSize = numRows
        topBottom = (squareSize - numCols)/2
        squareEdgesFull = cv2.copyMakeBorder(img2,0,0,topBottom,topBottom, cv2.BORDER_CONSTANT, value=BLACK)
        cv2.imwrite(imgEdgesMap, squareEdgesFull)
    else:
        squareSize = numCols
        topBottom = (squareSize - numRows)/2
        squareEdgesFull = cv2.copyMakeBorder(img2,topBottom,topBottom,0,0, cv2.BORDER_CONSTANT, value=BLACK)
        cv2.imwrite(imgEdgesMap, squareEdgesFull)



    while a<=50:
        dst2 = ((imgPath[:-4]) + '_' + str(a) + 'pixels' + '.png')
        dsize = (a,a)
        small = cv2.resize(img2,dsize, interpolation= cv2.INTER_AREA)
        cv2.imwrite (dst2, small)
        img3 = cv2.imread(dst2)


        testDir = (firstLevelIMG + "\\" + typeOsource + "\\" + str(a) + "_pixels")
        newfile = (testDir + '\\' + 'unknownItem_' + str(count) + '_' + str(a) +'pixels' + '.csv')
        previousFilePath = ((imgPath[:-4]) + '_' + str(a) +'pixels' + '.csv')
        print previousFilePath
        if os.path.isdir(testDir) != True:
            os.makedirs(testDir)
        
        fileSource.append(previousFilePath)
        csvWriter()
        
        if os.path.isfile(newfile) != True:
            shutil.move(previousFilePath,newfile)
            shutil.move(dst2,(newfile[:-4] + '.png'))
        else:
            while os.path.isfile(newfile) == True:
                count+=1
                newfile = (testDir + '\\' + 'unknownItem_' + str(count) + '_' + str(a) +'pixels' + '.csv')
                shutil.move(previousFilePath,newfile)
                shutil.move(dst2,(newfile[:-4] + '.png'))

       
        a+=10
    os.remove((imgPath[:-4]) + 'edges.png')
    count+=1