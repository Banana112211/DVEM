# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:08:16 2017

@author: root
"""
import os

def logfile_schreiben():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+"/"+"Log.txt", "a") as myfile:
        myfile.write("Hallo\n")
logfile_schreiben()