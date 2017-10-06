# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:01:13 2017

@author: Gustav Willig
"""
import socket
#todo: the received data need to be written to a log.txts
UDP_IP = "192.168.0.104"
UDP_PORT = 3333

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
