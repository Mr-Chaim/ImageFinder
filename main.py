# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 20:47:25 2017

@author: samir
"""


import os
import Tkinter
import tkFileDialog


def __init__(self, root):
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'This is a title'
def askdirectory(self):
    return tkFileDialog.askdirectory(**self.dir_opt)

if__name__=='__main__':
    
for i in os.listdir(fileSourcePath):
        if (i.find(keyword2) != -1):
            secondLevel = (fileSourcePath + '\\' + i)
            fileSource.append(secondLevel)
            print secondLevel