
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:48:19 2017
@author: root
"""

import time
import thread
import Tkinter as Tk
import writecsv2
import datalogger
import gyro
#import UDP_Simulator
from multiprocessing import Process

def update(text=str()):
   """---textfeld aktualisieren"""
   print(text)
   textbox.insert(Tk.END,text)
   root.update()  

    


def _start():
    
    active_stat.set(False)
    start_button.destroy()#hide Startbutton
    probantenname=name_box.get()
    data=dict()
    
    process_gyr=Process(target=gyro.gyro_sensor, args=(name,queue))
    
    gt=datalogger.inithializegt()
    start=time.time()
    name=probantenname+" " + time.ctime(start)
    process_gyr.start
    update(name)
    data["action"]=[]
    data["start"]=[]
    data["start"].append(start)
    
    
    writecsv2.writedatacsv(name,data,1)
    
    datalogger.readdata(1,gt,data)
    writecsv2.writedatacsv(name,data,0)
    output=str(data)+" \n"
    update(output)
        
    update(name)
    while True:
        datalogger.readdata(1,gt,data)
        writecsv2.writedatacsv(name,data,1)
        output=str(data)+" \n"
        update(output)
        if active_stat.get():
            data.clear()
            
            
            break
        
        if  active_action.get():
            active_action.set(False)
            data.clear()
            
            data["action"]=[]
            data["action"].append(timestamp.get())
            print data["action"]
            timestamp.set(0)
            writecsv2.writedatacsv(name,data,1)
            
    update("Fahrversuch Beendet")
    data["end"]=[]
    data["end"].append(timestamp.get())
    writecsv2.writedatacsv(name,data,0)
    process_gyr.terminate()    
       
    
def _action():
    active_action.set(True)
    timestamp.set(time.time())
    print("action")
    

def _stop():
    active_stat.set(True)
    update("Abbruchwunsch \n")
    timestamp.set(time.time())


root = Tk.Tk()

active_stat = Tk.BooleanVar(root)
active_action = Tk.BooleanVar(root)
timestamp=Tk.DoubleVar(root)



'''=========Code line for syn. with simulator 
queue = multiprocessing.Queue() 
dir_path = os.path.dirname(os.path.realpath(__file__))
proc1=Process(target=UDP_Simulator.udp_simulator, args=(queue,)) # Process for udp
================='''

textbox=Tk.Text(root) 
textbox.pack(side=Tk.TOP)
name_box=Tk.Entry(root)
name_box.pack(side=Tk.BOTTOM)
 
start_button=Tk.Button(root, text='Start', command=_start)
start_button.pack(side=Tk.LEFT)
Tk.Button(root, text='Action', command=_action).pack(side=Tk.LEFT)
Tk.Button(root, text='Stop', command=_stop).pack(side=Tk.LEFT)
Tk.Button(root, text='Quit', command=root.quit).pack(side=Tk.LEFT)
root.mainloop()

 


