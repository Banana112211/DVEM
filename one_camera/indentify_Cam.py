


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:34:56 2017

@author: odroid
"""

import cv2
import time
import os 


for j in range(0,10):
  innenkamera = cv2.VideoCapture(j)
  print (j)
  success,image = innenkamera.read()
  count = 1
  time.sleep(1 )
  success = True
  for i in range(0,1):
    success,image = innenkamera.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("frame%d.jpg" % i, image)    
    i += 1