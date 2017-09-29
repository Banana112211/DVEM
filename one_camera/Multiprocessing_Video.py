#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:12:55 2017

multiprocessing

prozesse werden nacheinander gestartet und abgearbeitet. am ende wartet
mit join das programm auf den jeweiligen prozess und führt das programm dann weiter

@author: odroid
"""
#Frage: Welche Processoren werden durch multiprocessing angesteuert?
#Könnte man Ihm anweisen, dass er die starken ansteuert?

import os
#Import Funktion zum Videospeichern (Abkürzung zu "video")
import Video_Frame_recored as video
#Import Multiprocessing
from multiprocessing import Process
 

def multithreating_2cams():   #Funktionsdef.
    #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start Process1
    proc1 = Process(target=video.videoaufzeichnung, args=(960, 720,0,dir_path,1000))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    
    #start Process2
    proc2 = Process(target=video.videoaufzeichnung, args=(960, 720,1,dir_path,1000))    #(bridth,width,cam_port2,path,frames)
    proc2.start()
    
    #wait for Process1
    proc1.join()
    #wait for Process2
    proc2.join()
    
#==================== Delete after test!!
    
multithreating_2cams()    #Funktionsaufruf
