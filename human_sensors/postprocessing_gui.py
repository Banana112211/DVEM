# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:39:42 2017

@author: home
"""


#==============================================================================
import tkinter as tk#Tkinter in 2.7
from tkinter import filedialog #tkFileDialog
import postprocessing

def main(filename,test=1):#
    postprocessing.main(filename)    
    root.destroy()

    


root = tk.Tk()

#root.withdraw()
    
# 
#
filepath=str() 
file_path = filedialog.askopenfilename()
print(file_path)
#==============================================================================

    
if __name__ == "__main__":
    main(file_path) #
    

    
    
        