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
###=======#Change the working direction to "common_functions" and back
##dir_path = os.path.dirname(os.path.realpath(__file__)) #real current working direction
##dir_path_seperated=str(dir_path).split("/")# divide the current working direction
##common_functions=str(dir_path_seperated[0])+"/"+str(dir_path_seperated[1])+"/"+str(dir_path_seperated[2])+"/"+str(dir_path_seperated[3])+"/"+"common_functions"
##os.chdir(common_functions)
###common load modul
import Write_Logfile
import UDP_Simulator

dir_path = os.path.dirname(os.path.realpath(__file__))
#video.videoaufzeichnung(432,240,0,dir_path,"key")
def multiprocessing_1cam_1gps():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    proc1 = Process(target=video.videoaufzeichnung, args=(432,240,0,dir_path,"key")) 
    proc1.start()
##    while True:
##        key=UDP_Simulator.udp_simulator()
##        proc1 = Process(target=video.videoaufzeichnung, args=(432,240,0,dir_path,key,1000))    #(bridth,width,cam_port1,path,frames)

multiprocessing_1cam_1gps()   #Funktionsaufruf


