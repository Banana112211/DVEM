import cv2
import time
import os 



print(cv2.__version__)
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
