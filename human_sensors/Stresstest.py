#-*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:55:06 2017

@author: home
"""
import time

import writecsv2

import datalogger

import subprocess

def main():
    #1.Step: Ini. der benötigten Variabellen
    data={} 
    gsr_relax=int()
    gsr_current=int()
    abbruch=bool()
    #2.Step: Start des Blue-Tooth Dongle
    
    probantenname=raw_input('Probantenname:')
    gt=datalogger.inithializegt()
    print(probantenname)
    start=time.ctime()
    t_eis=180
    name=probantenname+" " + start
    print(name)
    datalogger.readdata(15,gt,data)
    writecsv2.writedatacsv(name,data,1)
    for gsr in data["gsr"]:
        gsr_relax+=gsr    
    gsr_relax=gsr_relax/len(data["gsr"])
    print("-------------------------------------------")
    print("Der Eiswassertest beginnt in kürze")
    
    
    
    
    raw_input("bereit?")
    print("noch 15 s")
    datalogger.readdata(10,gt,data)
    writecsv2.writedatacsv(name,data,1)
    print("noch 5 s")
    datalogger.readdata(5,gt,data)
    data.clear()
    data["t_start_eis"]=[]
    data["t_start_eis"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
    print("jetzt bitte Hand bis zum Handgelenk in den Eimer")
    
    
    while t_eis>0:
        datalogger.readdata(10,gt,data)
        writecsv2.writedatacsv(name,data,1)
        t_eis=t_eis-10
        print("noch "+ str(t_eis)+" Sekunden")
        if abbruch==1:
            data.clear()
            data["t_end_eis"]=[]
            data["t_end_eis"].append(time.time())
            writecsv2.writedatacsv(name,data,0)
            break
     
        
    print("Bitte die Hand nun heraus nehmen und ein wenig entspannen")
    timer=0
    while gsr_current> gsr_relax-5:
        datalogger.readdata(10,gt,data)
        writecsv2.writedatacsv(name,data,1)
        for gsr in data["gsr"]:
            gsr_current+=gsr    
        gsr_relax=gsr_relax/len(data["gsr"])
        timer+=10
        print("Gleich geht's weiter")
        if timer>150:
            break
    print("nun folgt noch eine kurze Video Sequenz")
    data.clear()
    data["t_start_video"]=[]
    data["t_start_video"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
    # Oeffnete die .mp4 in Webbrowser
    subprocess.call("xdg-open 'Stressor.mp4'" , shell=True)
    datalogger.readdata(150,gt,data)
    writecsv2.writedatacsv(name,data,1)
    print("Vielen Dank!")


if __name__ == '__main__':
    main()        
                 
