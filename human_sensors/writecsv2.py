 #-*- coding: utf-8 -*-
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

    writedatacsv(name,datain,0)

def csvreader(name,append):
    reader=csv.DictReader(open(name+'.csv', 'r'))
    dread=dict()

    #get vorhandene Spalten(not empty)
    try:
        for key in reader.fieldnames:
            dread[key]=[]

    except:next
    #vorhandene Spalten mit Daten befüllen
    if append==0:
        for row in reader:
            for key in row:
                try:
                 dread[key].append(row[key])
                except:next
        
    return dread
    
    

def csvwriter(dread,f,append):

#            print(for key in dread: dread[key][0])
    line=1
    count=0
    if append==0:
        w = csv.writer(open(f+'.csv', 'w')) 
        w.writerow(dread.keys()) 
    else:
        w = csv.writer(open(f+'.csv', 'a'))

    #über datenlänge iterieren ´= Zeilenanzahl
    while count<line:
        c=[]
        #über Spalten Zeilen schreiben
        for item in dread:

            if len(dread[item])>line:
                line =len(dread[item])
            try:
                c.append(dread[item][count])                   
            except:
                c.append("")
        count+=1
        w.writerow(c)

def writedatacsv(name=str(),data=dict(),append=bool()):
    """CSV daten schreiben,bestehen csvwriter() csvreader()"""
    exist=os.path.isfile(name +'.csv') 

    if exist == 0:

        writer = csv.writer(open(name+'.csv', 'w'))
        writer.writerow(data.keys())
        
    dread=dict()
   #---------------------------------------------------------------------------------------     
    dread=csvreader(name,append) 
   #überprüfen ob input Dict(data) schon in csv vorhanden falls nicht erstellen, falls ja Daten anhängen
    for key in data:
        if key in dread:
            for d in range(len(data[key])):
                dread[key].append(data[key][d])

        else:
            dread[key]=data[key]

    #daten schreiben        
    csvwriter(dread,name,append)

if __name__ == '__main__':
    main() 
