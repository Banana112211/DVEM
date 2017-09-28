# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:10:05 2017

@author: ubuntu
"""
#HRM datalogger


import pexpect
import writecsv

    
    
def inithializegt():        
        gt = pexpect.spawn("sudo gatttool -i hci0 -b 00:22:D0:2C:C5:A5  -I")
               
        gt.expect(r"\[LE\]>")
       
        gt.sendline("connect")
        gt.expect(["Connection successful.", r"\[CON\]"], timeout=30)
        gt.sendline("char-write-req 0x0012 0100")
        return gt
        
def readhrdata(t,gt,hr,rr):
         hr_expect = "Notification handle = 0x0011" + " value: ([0-9a-f ]+)"
         count=0
         
         while count<t:
             try:
                 gt.expect(hr_expect)
                 datahex = gt.match.group(1).strip()
                 print(datahex,count)
                 data = map(lambda x: int(x, 16), datahex.split(' '))
                 res = interpret(data)
                 #print res
                 if res.has_key("rr"):
                     for i_rr in res["rr"]:
                                #print i
                         
                         rr.append(i_rr*1000/1024)
                 #print res["hr"]
                 hr.append(res["hr"])
                 count+=1
             except KeyboardInterrupt:
                print("Received keyboard interrupt. Quitting cleanly.")
                break        
         return hr,rr               
        
        
def hrm(t,name):

    max=3600*8 #8h-> ~50 kb pro list
    hr=[]
    rr=[]
    data={}
    #name="test" #time.ctime()
    #writedata(hr,rr,name)
    try:
        gt=inithializegt()
        #--------festlegen wie lange augezeichnet wird: alle 90s abspeichern in csv
        if t<max:
            readhrdata(t,gt,hr,rr)
            data["hr"]=hr
            data["rr"]=rr
            writecsv.writedatacsv(data,name)
            
#        elif t=0:
#            while 1:
#                try:
#                   readhrdata(max,gt,hr,rr)
#                   writedata(hr,rr,name) 
#               
#                except KeyboardInterrupt:
#                    print("Received keyboard interrupt. Quitting cleanly.")
#                    break  
            
        else:
            runs=t/max
            leftover=t%max
            run=0
            while(run<runs):
                try:
                    readhrdata(max,gt,hr,rr)
                    writedata(hr,rr,name)
                
                except KeyboardInterrupt:
                    print("Received keyboard interrupt. Quitting cleanly.")
                    break 
            
            readhrdata(leftover,gt,hr,rr)
            writedata(hr,rr,name)
        

    
            

    finally:gt.sendline("quit")

def interpret(data):
    """
    data is a list of integers corresponding to readings from the BLE HR monitor
    """

    byte0 = data[0]
    res = {}
    res["hrv_uint8"] = (byte0 & 1) == 0
    sensor_contact = (byte0 >> 1) & 3
    if sensor_contact == 2:
        res["sensor_contact"] = "No contact detected"
    elif sensor_contact == 3:
        res["sensor_contact"] = "Contact detected"
    else:
        res["sensor_contact"] = "Sensor contact not supported"
    res["ee_status"] = ((byte0 >> 3) & 1) == 1
    res["rr_interval"] = ((byte0 >> 4) & 1) == 1

    if res["hrv_uint8"]:
        res["hr"] = data[1]
        i = 2
    else:
        res["hr"] = (data[2] << 8) | data[1]
        i = 3

    if res["ee_status"]:
        res["ee"] = (data[i + 1] << 8) | data[i]
        i += 2

    if res["rr_interval"]:
        res["rr"] = []
        while i < len(data):
            # Note: Need to divide the value by 1024 to get in seconds
            res["rr"].append((data[i + 1] << 8) | data[i])
            i += 2

    return res

def main():
    name="test2" #time.ctime()
    t=5
    hrm(t,name)
    
if __name__ == '__main__':
    main()                