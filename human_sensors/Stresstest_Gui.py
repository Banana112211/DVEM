import time
import Tkinter as Tk
import writecsv2
import datalogger
import os
import subprocess

def _start():
    active_stat.set(False)
    start_button.destroy()
    probantenname=name_box.get()
    data={}
    gsr_relax=int()
    gsr_current=int()
    gt=datalogger.inithializegt()
    
    print(probantenname)
    textbox.insert(Tk.END,probantenname)
    root.update()
    
    start=time.ctime()
    t_eis=180
    name=probantenname+" " + start
    print(name)
    textbox.insert(Tk.END,name)
    root.update()
    datalogger.readdata(15,gt,data)
    writecsv2.writedatacsv(name,data,1)
    for gsr in data["gsr"]:
        gsr_relax+=gsr
        
    gsr_relax=gsr_relax/len(data["gsr"])
    textbox.insert(Tk.END,str(gsr_relax))
    root.update()
    print("-------------------------------------------")
    print("Der Eiswassertest beginnt in gleich")
    
    textbox.insert(Tk.END," Der Eiswassertest beginnt in gleich \n")
    textbox.insert(Tk.END," noch 15 s \n")
    root.update()
    
    print("noch 15 s \n")
    datalogger.readdata(10,gt,data)
    writecsv2.writedatacsv(name,data,1)
    print("noch 5 s")
    textbox.insert(Tk.END,"noch 5 s \n")
    root.update()
    
    datalogger.readdata(5,gt,data)
    data.clear()
    data["t_start_eis"]=[]
    data["t_start_eis"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
    print("jetzt bitte Hand bis zum Handgelenk in den Eimer")
    textbox.insert(Tk.END,"jetzt bitte Hand bis zum Handgelenk in den Eimer \n")
    root.update()
    
    while t_eis>0:
        datalogger.readdata(10,gt,data)
        writecsv2.writedatacsv(name,data,1)
        t_eis-=10
        print("noch "+ str(t_eis)+" Sekunden")
        textbox.insert(Tk.END,"noch "+ str( t_eis) +" Sekunden \n")
        root.update()
        if active_stat.get():
            data.clear()
            data["t_end_eis"]=[]
            data["t_end_eis"].append(time.time())
            writecsv2.writedatacsv(name,data,0)
            break
                
                    
     
    print("Bitte die Hand nun heraus nehmen und ein wenig entspannen")
    textbox.insert(Tk.END,"Bitte die Hand nun heraus nehmen und ein wenig entspannen \n")
    timer=0
    while gsr_current< (gsr_relax-5):
        datalogger.readdata(10,gt,data)
        writecsv2.writedatacsv(name,data,1)
        timer+=10
        print("Gleich geht's weiter")
        textbox.insert(Tk.END,"Gleich geht's weiter \n")
        root.update()    
        if timer>150:
            break
            
    print("nun folgt noch eine kurze Video Sequenz")
    textbox.insert(Tk.END,"nun folgt noch eine kurze Video Sequenz \n")
    data.clear()
    data["t_start_video"]=[]
    data["t_start_video"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
    subprocess.call("xdg-open 'Stressor.mp4'" , shell=True)
    datalogger.readdata(150,gt,data)
    writecsv2.writedatacsv(name,data,1)
    print("Vielen Dank!")
    textbox.insert(Tk.END,"Vielen Dank! ")
    root.update()
    

def _stop():
    active_stat.set(True)


root = Tk.Tk()

active_stat = Tk.BooleanVar(root)
active_stat.set(True)

#counterstr=Tk.StringVar() 
#Tk.Label(root, textvariable=counterstr).pack(side=Tk.TOP)
textbox=Tk.Text(root) 
textbox.pack(side=Tk.TOP)
name_box=Tk.Entry(root)
name_box.pack(side=Tk.BOTTOM)
 
start_button=Tk.Button(root, text='Start', command=_start)
start_button.pack(side=Tk.LEFT)
Tk.Button(root, text='Stop', command=_stop).pack(side=Tk.LEFT)
Tk.Button(root, text='Quit', command=root.quit).pack(side=Tk.LEFT)
root.mainloop()
