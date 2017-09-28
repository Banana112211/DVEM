# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:08:21 2017

@author: home
"""

#csv ausgabe


import csv
import os.path
import os

def main():

    name="test"
    datain={} 
#    gsr=[7,8,9]
#    datain["gsr"]=gsr
    
    hr=[4,5,6]
    rr=[8,9]
    datain["hr"]=hr
    datain["rr"]=rr
#    duration=len(data["hr"])
#    c_rr=len(data["rr"])
#    if c_rr<duration:
#        while c_rr<duration:
#            data["rr"].append(0)
#            c_rr+=1
                    
    writedatacsv(datain,name)
    
def writedatacsv(data,name):
    exist=os.path.isfile(name+'.csv')
    
    
    if exist == 0:
        writer = csv.writer(open(name+'.csv', 'w'))
        writer.writerow(["hr","rr","GSR"])
    
    if "hr" in data:
        reader=csv.DictReader(open(name+'.csv', 'r'))
        for row in reader:
            print(row)
        writer = csv.writer(open(name+'.csv', 'w'))
        hr=[]
        rr=[]
        for i in data["hr"]:
            hr.append(i)
        for i_rr in data["rr"]:
            rr.append(i_rr)
        duration=len(hr)
        c_rr=len(rr)
        if c_rr<duration:
            while c_rr<duration:
                rr.append(0)
                c_rr+=1
        if duration<c_rr:
            while duration<c_rr:
                hr.append(0)
                duration+=1
        for i in range(duration):        
            writer.writerow([hr[i],rr[i]])
            
    if "gsr" in data:
        
        reader = csv.reader(open(name+'.csv'))
        
        cache=[]
        gsr=[]
        #values in lokale Variable speichern
        for i in data["gsr"]:
            gsr.append(i)
        #Header ueberspringen    
        reader.next()
        
        #vorhandene Werte aus csv einlesen und "spalte" anfuegen
        n=0
        for row in reader:
            try:
                row.append(gsr[n])
            except:
                    pass  
            n+=1    
            cache.append(row)
        #csv schreiben
        writer = csv.writer(open(name+'.csv', 'w'))
        writer.writerow(["hr","rr","GSR"])
        for c in cache:
            writer.writerow(c)


if __name__ == '__main__':
    main() 
    
            