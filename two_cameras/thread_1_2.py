import thread
import time
import Video_Frame_recored
import os
# Create two threads as follows
#try:
dir_path = os.path.dirname(os.path.realpath(__file__))
print "message1"
thread.start_new_thread( Video_Frame_recored.videoaufzeichnung, (432, 240,6,dir_path) )
time.sleep(2)
print "message2"
thread.start_new_thread( Video_Frame_recored.videoaufzeichnung, (176, 144,7,dir_path) )

#Video_Frame_recored.videoaufzeichnung(320, 240,0,dir_path)
   
###Testdaten===============
#Einstellungn=[(176, 144), (320, 240), (352, 288), (432, 240), (544, 288), (640, 480), (800, 448), (864, 480), (960, 544),(960, 720),(1184, 656), (1280, 960)]
#
#for element in Einstellungn:
#    thread.start_new_thread( Video_Frame_recored.videoaufzeichnung, (element[0],element[1],0,dir_path) )
#    time.sleep(2)
#    thread.start_new_thread( Video_Frame_recored.videoaufzeichnung, (element[0],element[1],1,dir_path) )
