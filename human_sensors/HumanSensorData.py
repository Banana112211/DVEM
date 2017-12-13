# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:22:26 2017

@author: home
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:48:19 2017
@author: root
"""

import time


import writecsv2
#import datalogger
#import gyro
#import UDP_Simulator
from multiprocessing import Process
import postprocessing





    


def log(name):
    
    
    
    probantenname=name
    data=dict()
    start=time.time()
    name=probantenname+" " + time.ctime(start)
    
    process_gyr=Process(target=gyro.gyro_sensor, args=(name,))
    
    gt=datalogger.inithializegt()  
    process_gyr.start
    
    print(name)
    data["action"]=[]
    data["start"]=[]
    data["start"].append(start)
    
    
    writecsv2.writedatacsv(name,data,1)
    
    datalogger.readdata(1,gt,data)
    writecsv2.writedatacsv(name,data,0)
    output=str(data)+" \n"
    print(output)   
    
    while True:
        try:
            datalogger.readdata(1,gt,data)
            writecsv2.writedatacsv(name,data,1)
            output=str(data)+" \n"
            print(output)
        
    except KeyboardInterrupt:
        print("Fahrversuch Beendet")
        data["end"]=[]
        data["end"].append(timestamp.get())
        writecsv2.writedatacsv(name,data,0)
        process_gyr.terminate()
        postprocessing((name+'.csv')
        break
       
    

    
if __name__ == "__main__":
    log() 

 

