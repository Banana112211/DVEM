#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:19:49 2017

@author: root
"""

import socket

server_addr = ("time.fu-berlin.de", 13)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("", server_addr)
daten, addr = client_socket.recvfrom(1024)
datenstring = daten
client_socket.close()
del client_socket
print(datenstring)