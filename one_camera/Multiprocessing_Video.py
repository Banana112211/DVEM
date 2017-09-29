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
import Video_Frame_recored as video
 
from multiprocessing import Process
 
#def doubler(number):
#    """
#    A doubling function that can be used by a process
#    """
#    
#    result = number * 2
#    proc = os.getpid()
#    print('{0} doubled to {1} by process id: {2}'.format(
#        number, result, proc))
 
    
#def double(var1):
#    
#    result = var1 * 2
#    proc = os.getpid()
#    print('{0} doubled to {1} by process id: {2}'.format(
#        number, result, proc))
if __name__ == '__main__':    =100 #Anzahl der Frames: 15 Frames= 2 sec=> 4500 Frames=5 Minuten
    #numbers = [5, 10, 15, 20, 25]
    #procs = []
#    x=2
#    y=4
#    obj = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    
    proc1 = Process(target=video.videoaufzeichnung, args=(960, 544,0,dir_path))
    proc1.start()
    
    proc2 = Process(target=video.videoaufzeichnung, args=(960, 544,1,dir_path))
    proc2.start()
    
    proc1.join()
    proc2.join()
    
#    for index, number in enumerate(numbers):
#        proc = Process(target=doubler, args=(number,))
#        procs.append(proc)
#        proc.start()
        
        #In multiprocessing, processes are spawned by creating a 
        #Process object and then calling its start() method.
        #print"message______________________1337"

#    for proc in procs:
#        proc.join()
        
        #If the optional argument timeout is None (the default), 
        #the method blocks until the process whose join() method is 
        #called terminates.
        
        #print"message______________________1234"
        