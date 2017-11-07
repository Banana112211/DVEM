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
dir_path = os.path.dirname(os.path.realpath(__file__))

import Video_Frame_recored as video
#Import Multiprocessing
from multiprocessing import Process
import multiprocessing
import gps_sensor
os.chdir(dir_path)
import server



def One_Kamera():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #video.videoaufzeichnung(352,288,0,dir_path,"key",1000,"nein",20)
    proc1=Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,"key",1000,"nein",20,))
    proc1.start()
    proc1.join()

 
def multiprocessing_3cam_1gps():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        proc1 = Process(target=video.videoaufzeichnung, args=(320,240,2,dir_path,"objekt",40000,"nein",20))#Fahrer
        proc1.start()
        proc2 = Process(target=video.videoaufzeichnung, args=(1280, 960,1,dir_path,"objekt",40000,"nein",80)) #Front
        proc2.start()
        proc3 = Process(target=video.videoaufzeichnung, args=(432,240,0,dir_path,"objekt",40000,"nein",20)) #hinten
        proc3.start()
        proc4=Process(target=gps_sensor.gps_signal, args=())
        proc4.start()
        print "Please enter"
        userinput=input()
        while True:
            if userinput=="kill":
                proc1.terminate()
                proc2.terminate()
                proc3.terminate()
                proc4.terminate()
                return
            print "Please enter"
            userinput=input()
    except:
            proc1.terminate()
            proc2.terminate()
            proc3.terminate()
            proc4.terminate()
            print "everything is dead"
            return
def multiprocessing_2cams():   #Funktionsdef.
    #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start Process1

    proc1 = Process(target=video.videoaufzeichnung, args=(960,720,0,dir_path,"key",1000))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    
    #start Process2
    proc2 = Process(target=video.videoaufzeichnung, args=(960,720,1,dir_path,"key",1000))    #(bridth,width,cam_port2,path,frames)
    proc2.start()
    
    #wait for Process1
    proc1.join()
    #wait for Process2
    proc2.join()
    
def multiprocessing_3cams_server_gps():   #Funktionsdef.
    #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start proc_server
    proc_server = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,"key",1000,"nein",20))    #(bridth,width,cam_port1,path,frames)
    proc_server.start()
    
    #start proc_gps
    proc_gps=Process(target=gps_sensor.gps_signal, args=())
    proc_gps.start()
    
    #start proc_driver_camera
    proc_driver_camera = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,"key",1000,"nein",20))    #(bridth,width,cam_port1,path,frames)
    proc_driver_camera.start()
    
    #start proc_front_camera
    proc_front_camera = Process(target=video.videoaufzeichnung, args=(352,288,1,dir_path,"key",1000,"nein",20))    #(bridth,width,cam_port2,path,frames)
    proc_front_camera.start()
    
    #start proc_back_camera
    proc_back_camera = Process(target=video.videoaufzeichnung, args=(352,288,2,dir_path,"key",1000,"nein",20))
    proc_back_camera.start()
    
    #wait for proc_driver_camera,proc_front_camera,proc_back_camera
    proc_driver_camera.join()
    proc_front_camera.join()
    proc_back_camera.join()
    proc_server.join()
    proc_gps.join()
    
#==================== MAIN =================================
def multiprocessing_1cam_server():
        #1.Step:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #start Process1
    proc1 = Process(target=video.videoaufzeichnung, args=(352,288,0,dir_path,"key",1000,"nein",20))    #(bridth,width,cam_port1,path,frames)
    proc1.start()
    
    #start Process2
    proc2=Process(target=server.server,args=('192.168.0.1',55605))
    proc2.start()
    
    #wait for Proc1, Proc2
    proc1.join()
    proc2.join()
if __name__=="__main__":
    multiprocessing_3cams_server_gps()
    #multiprocessing_3cam_1gps()

