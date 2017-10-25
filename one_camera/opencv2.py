import numpy as np
import cv2
from matplotlib import pyplot as plt

###1.Step: read picture and load classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('WIN_20171012_17_51_00_Pro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#2.Step: identify feature of pitcure
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
cv2.imshow('img',img)
cv2.imwrite('processed.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#3.Step: Save the processed pitcure
#4.Step: Write the identify feature into a .txt
