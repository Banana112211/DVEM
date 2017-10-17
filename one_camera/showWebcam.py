# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 08:26:10 2017

@author: odroid
"""
import numpy as np
import cv2
import datetime


cap = cv2.VideoCapture(2)
video_wdth=800
video_hight=600
cap.set(3,video_wdth) # wdth
cap.set(4,video_hight) #high


while(True):
    now=datetime.datetime.now()
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLORMAP_HOT) #rum stillen!
     # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        message= str(fps)+" Frames"+"\t"+str(now)+"\n"
        with open("Log.txt", "a") as myfile:
            myfile.write(message)
    else :
        fps = cap.get(cv2.CAP_PROP_FPS)
        message= str(fps)+" Frames"+"\t"+str(now)+"\n"
        #"Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)+now
        with open("Log.txt", "a") as myfile:
            myfile.write(message)
        
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       with open("Log.txt", "a") as myfile:
            myfile.write("\n"+"="*40)
       break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
