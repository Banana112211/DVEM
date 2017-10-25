import numpy as np
import cv2
import time
#todo: Anpassung der Faktoren für die Erkennung von Pupillen? Warum werden Pupillen nicht
 # erkannt wird
#todo: While-Loop: Erfassung im Protokoll wann Augen erkannt wurden
 #todo: Per Tnesorflow die Anpassung derAugen erkennung verbessern? Eventuell Pytorch? 

#todo: Kann dadruch die Fahreblickwinkel  bestmmt werden=
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

##cap = cv2.VideoCapture(0)
##now= time.asctime()
##while 1:
##    ret, img = cap.read()
##    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
##
##    for (x,y,w,h) in faces:
##        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
##        roi_gray = gray[y:y+h, x:x+w]
##        roi_color = img[y:y+h, x:x+w]
##        
##        eyes = eye_cascade.detectMultiScale(roi_gray)
##        for (ex,ey,ew,eh) in eyes:
##            print ex,ey,ew,eh,now
##            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
##    print "Fahrer schaut nicht auf die Strasse!",now
##    cv2.imshow('img',img)
##    k = cv2.waitKey(30) & 0xff
##    if k == 27:
##        break
##
##cap.release()
##cv2.destroyAllWindows()
##
##
###1.Step: read picture
#2.Step: identify feature of pitcure
import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('WIN_20171012_17_51_00_Pro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#3.Step: Save the processed pitcure
#4.Step: Write the identify feature into a .txt
