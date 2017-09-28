# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:14:48 2017

@author: ubuntu
"""

#!/usr/bin/python

import thread
import time
import hrm
import oszi

    
t=90
name="test"
# Create two threads as follows
try:
   t1=thread
   t2=thread
   t2.start_new_thread( hrm.hrm,(t,name) )
   t1.start_new_thread( oszi.gsr,(t,name) )
except KeyboardInterrupt:
    t1.interrupt_main()
    t2.interrupt_main()       
    
except:
   print( "Error: unable to start thread")

while 1:
    time.sleep(0.01)
    pass