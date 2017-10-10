#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:12:55 2017

multiprocessing

prozesse werden nacheinander gestartet und abgearbeitet. am ende wartet
mit join das programm auf den jeweiligen prozess und führt das programm dann weiter

Verschiedene machbare Auflösungen der Cams:
(176, 144),(320,240),(352,288),(432,240),(544,288),(640,480),(800,448),(864,480) ,(960, 544),(960, 720),(1184, 656), (1280, 960)

=============================================
TODO!:
    Prozessorkern finden und anzeigen lassen
    --> Auslastung anzeigen lassen
=============================================    

@author: odroid
"""
#Frage: Welche Processoren werden durch multiprocessing angesteuert?
#Könnte man Ihm anweisen, dass er die starken ansteuert?

import os
#Import Funktion zum Videospeichern (Abkürzung zu "video")
import Video_Frame_recored as video
#Import Multiprocessing
from multiprocessing import Process
#=======#Change the working direction to "common_functions" and back
dir_path = os.path.dirname(os.path.realpath(__file__)) #real current working direction
dir_path_seperated=str(dir_path).split("/")# divide the current working direction
common_functions=str(dir_path_seperated[0])+"/"+str(dir_path_seperated[1])+"/"+str(dir_path_seperated[2])+"/"+str(dir_path_seperated[3])+"/"+"gps"
os.chdir(common_functions)
#common load modul
import gps_sensor
 
 
def multiprocessing_1cam_1gps():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    proc1 = Process(target=video.videoaufzeichnung, args=(432,240,6,dir_path,1000))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    proc2 = Process(target=video.videoaufzeichnung, args=(432,240,7,dir_path,1000))    #(bridth,width,cam_port2,path,frames)
    proc2.start()    
    proc3=Process(target=gps_sensor.gps_signal, args=())
    proc3.start()
def multiprocessing_2cams():   #Funktionsdef.
    #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start Process1
    proc1 = Process(target=video.videoaufzeichnung, args=(432,240,6,dir_path,1000))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    
    #start Process2
    proc2 = Process(target=video.videoaufzeichnung, args=(432,240,7,dir_path,1000))    #(bridth,width,cam_port2,path,frames)
    proc2.start()
    
    #wait for Process1
    proc1.join()
    #wait for Process2
    proc2.join()
    
def multiprocessing_3cams():   #Funktionsdef.
    #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start Process1
    proc1 = Process(target=video.videoaufzeichnung, args=(544,288,0,dir_path,500))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    
    #start Process2
    proc2 = Process(target=video.videoaufzeichnung, args=(544,288,1,dir_path,500))    #(bridth,width,cam_port2,path,frames)
    proc2.start()
    
    #start Process3
    proc3 = Process(target=video.videoaufzeichnung, args=(544,288,2,dir_path,500))    #(bridth,width,cam_port2,path,frames)
    proc3.start()
    
    #wait for Process1
    proc1.join()
    #wait for Process2
    proc2.join()
    #wait for Process3
    proc3.join()
    
#==================== MAIN =================================
    
#multiprocessing_2cams() 
    
multiprocessing_1cam_1gps()   #Funktionsaufruf


