#def viedocamera(eingang):
import numpy as np
import cv2
import time


def videoaufzeichnung(video_wdth,video_hight,video_fps,seconds):
	"Speichert frames fuer gebene Aufloesung
    cap = cv2.VideoCapture(7)
    cap.set(3,video_wdth) # wdth
    cap.set(4,video_hight) #hight 
    cap.set(5,video_fps) #hight 
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    name_Video=str(video_wdth)+"x"+str(video_hight)+"_fps "+str(video_fps)+".avi"
    out = cv2.VideoWriter(name_Video,fourcc,video_fps, (video_wdth,video_hight))

    #out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    
    start=time.time()
    zeitdauer=0
    while(zeitdauer<seconds):
        end=time.time()
        zeitdauer=end-start
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,180)
            # write the flipped frame
            out.write(frame)
    
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
