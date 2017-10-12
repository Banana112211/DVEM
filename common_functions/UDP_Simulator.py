# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:01:13 2017

@author: Gustav Willig
"""
import socket
import Write_Logfile
#=======#Change the working direction to "common_functions" and back
dir_path = os.path.dirname(os.path.realpath(__file__)) #real current working direction
dir_path_seperated=str(dir_path).split("/")# divide the current working direction
common_functions=str(dir_path_seperated[0])+"/"+str(dir_path_seperated[1])+"/"+str(dir_path_seperated[2])+"/"+str(dir_path_seperated[3])+"/"+"common_functions"
os.chdir(common_functions)
#common load modul
import Write_Logfile
import UDP_Simulator.py
#==============
#todo: the received data need to be written to a log.txts
#todo: received time stampe give to Video_Frame_recored

def udp_simulator():
    UDP_IP = "192.168.0.104"
    UDP_PORT = 3333       
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    Write_Logfile.logfile_schreiben("Current_time,WheelAngle,Accelrator,Brakepetal,SpeedInKilometers,PositionX,PositionY","Simulator")
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #print ("received message:", data)
        Write_Logfile.logfile_schreiben(str(data),"Simulator")
        value=str(data).split(";")
        print value[0]
        return value[0]
    

