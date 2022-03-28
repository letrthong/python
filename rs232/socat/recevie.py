import serial
import pty
import os
import time

 
port = serial.Serial('/dev/pts/2' )
if port.is_open == True:
    while True:
        #print("readline")
        ser_bytes  =  port.readline()
        if len(ser_bytes) > 0:
            print( ser_bytes )
        else:
            print( "ser_bytes is empty" )

    port.close()

