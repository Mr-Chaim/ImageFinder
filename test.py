# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 01:04:50 2017

@author: samir
"""

import Tkinter, Tkconstants, tkFileDialog

class TkFileDialogExample(Tkinter.Frame):

  def __init__(self, root):

    Tkinter.Frame.__init__(self, root)
    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
    Tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'This is a title'

  def askdirectory(self):
    return tkFileDialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()