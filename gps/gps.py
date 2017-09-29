#General informationen:
#If you enter the following  code line in the cmd, you will get the port information of the gps-device "python -m serial.tools.list_ports"

import serial

#1.Step:Ensure that the gps-device is succesfull conected to the odroid
gps=serial.Serial("/dev/ttyACM0",baudrate=9600)
#print(gps) if you print the gps signal and not an error message occur 
while True:
    line=gps.readline()
    data=line.split(",")
    if data[0]=="$GPRMC":
        if data[2]=="A":
           print "Latitude: %{}".format(data[3])
           print "Longitude: %{}".format(data[4])
           
