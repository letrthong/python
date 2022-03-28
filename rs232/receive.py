import serial
import pty
import os
import time

# ser = serial.Serial('/dev/ttyUSB0')
port = serial.Serial('/dev/pts/3', baudrate=115200, timeout=3.0,  rtscts=True,dsrdtr=True)
if port.is_open == True:
    while True:
        print("readline")
        ser_bytes  =  port.readline()
        if len(ser_bytes) > 0:
            print( ser_bytes )
        else:
            print( "ser_bytes is empty" )

    port.close()

