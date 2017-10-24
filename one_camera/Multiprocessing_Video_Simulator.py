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
import multiprocessing
import UDP_Simulator

dir_path = os.path.dirname(os.path.realpath(__file__))
#video.videoaufzeichnung(432,240,0,dir_path,"key")
def multiprocessing_1cam_udp():
    queue = multiprocessing.Queue() 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    proc1=Process(target=UDP_Simulator.udp_simulator, args=(queue,)) # Process for udp
    proc1.start()
    proc2 = Process(target=video.videoaufzeichnung, args=(432,240,0,dir_path,queue)) 
    proc2.start()
    #Step: exti all exisiting processes
    proc1.join()
    proc2.join()

def multiprocessing_2cam():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    proc1 = Process(target=video.videoaufzeichnung, args=(640,480,1,dir_path,"objekt",100,"nein",20))#Fahrer
    proc1.start()
    proc2 = Process(target=video.videoaufzeichnung, args=(640,480,2,dir_path,"objekt",100,"nein",85)) #Front
    proc2.start()

    proc1.join()
    proc2.join()


def multiprocessing_3cam():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    proc1 = Process(target=video.videoaufzeichnung, args=(320,240,0,dir_path,"objekt",100,"nein",20))#Fahrer
    proc1.start()
    proc2 = Process(target=video.videoaufzeichnung, args=(1280, 960,1,dir_path,"objekt",100,"nein",20)) #Front
    proc2.start()
    proc3 = Process(target=video.videoaufzeichnung, args=(432,240,2,dir_path,"objekt",100,"nein",20)) #Front
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()
    
    
def multiprocessing_3cam_udp_all():
    queue = multiprocessing.Queue() 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    proc1=Process(target=UDP_Simulator.udp_simulator, args=(queue,)) # Process for udp
    proc1.start()
    Einstellungn=[(176, 144),(320,240),(352,288),(432,240),(544,288),(640,480),(800,448),(864,480) ,(960, 544),(960, 720),(1184, 656), (1280, 960)]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for element in Einstellungn:
        proc2 = Process(target=video.videoaufzeichnung, args=(element[0],element[1],0,dir_path,queue)) # Hinterkamera
        proc2.start()
        proc3 = Process(target=video.videoaufzeichnung, args=(element[0],element[1],1,dir_path,queue)) #Front
        proc3.start()
        proc4 = Process(target=video.videoaufzeichnung, args=(element[0],element[1],2,dir_path,queue)) #Fahrer
        proc4.start()

        proc2.join()
        proc3.join()
        proc4.join()
        
    proc1.join()



if __name__ == '__main__':   
    multiprocessing_3cam()
