import time
import Tkinter as Tk
import writecsv2
import datalogger
import subprocess

def update(text=str()):
   """---textfeld aktualisieren"""
   print(text)
   textbox.insert(Tk.END,text)
   root.update()    

def GSR(data=dict()):
    """--- GSR mitteln und zurück geben-----"""
    gsr_cur=0
    for gsr in data["gsr"]:
        gsr_cur+=gsr
        
    gsr_cur=gsr_cur/len(data["gsr"])
    
    return gsr

def _start():
    
    active_stat.set(False)
    start_button.destroy()#hide Startbutton
    probantenname=name_box.get()
    data=dict()
    gsr_relax=int()
    gsr_current=int()
    start=time.ctime()
    t_eis=int(180)
    gt=datalogger.inithializegt()
    name=probantenname+" " + start+" \n"
    timer=int()
    

      
    update(name)
    
    datalogger.readdata(15,gt,data)
    writecsv2.writedatacsv(name,data,0)
    
    #--------Step 1------------ Grundlevel GSR HR...----------------
    
    update("------------------------------------------- \n Der Eiswassertest beginnt in gleich")
    
    
    update("noch 15 s \n")
    datalogger.readdata(10,gt,data)
    writecsv2.writedatacsv(name,data,1)
    #Grundlevel Hautleitfähigkeit festlegen
    
    gsr_relax=GSR(data)
    update(str(gsr_relax))
    update("noch 5 s \n")
    
    
    datalogger.readdata(5,gt,data)
    writecsv2.writedatacsv(name,data,1)
    
    data.clear()
    
    data["t_start_eis"]=[]
    data["t_start_eis"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
    data.clear()
    
    update("jetzt bitte Hand bis zum Handgelenk in den Eimer \n")
#--------Step 2------------Eisawassertest----------------
    
    while t_eis>0:
       datalogger.readdata(10,gt,data)
       writecsv2.writedatacsv(name,data,1)
       t_eis=t_eis-10
       update("noch "+ str(t_eis) +" Sekunden \n")
            
       if active_stat.get():
          data.clear()
          data["t_end_eis"]=[]
          data["t_end_eis"].append(time.time())
          writecsv2.writedatacsv(name,data,0)
          break
                
                    
    
    update("Bitte die Hand nun heraus nehmen und ein wenig entspannen \n")
 #--------Step 3------------ Entspannen ----------------
    while ( gsr_current< (gsr_relax-5)) or (timer< 70):
        
        datalogger.readdata(10,gt,data)
        writecsv2.writedatacsv(name,data,1)
        
        timer+=10
        update("Gleich geht's weiter\n")
        gsr_current=GSR(data)
            
        if timer>150:
            break
            
    update("nun folgt noch eine kurze Video Sequenz \n")
#--------Step 3------------ Video ----------------    
    data.clear()
    data["t_start_video"]=[]
    data["t_start_video"].append(time.time())
    writecsv2.writedatacsv(name,data,0)
   
    subprocess.call("xdg-open 'Stressor.mp4'" , shell=True)
    
    datalogger.readdata(120,gt,data)
    writecsv2.writedatacsv(name,data,0)
    
    update("Vielen Dank!")
    
    

def _stop():
    active_stat.set(True)
    update("Abbruchwunsch") 

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
