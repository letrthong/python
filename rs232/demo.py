import serial
import pty
import os
import time

# ser = serial.Serial('/dev/ttyUSB0')
#ser = serial.Serial('/dev/tty16')
#if ser is not None:
    # ser.baudrate = 19200
    #print(ser.name)
    # ser.write(b'hello')
    #ser.close()

# open new pseudo-terminal pair
# using os.openpty() method
#
# A tty is a physical terminal-teletype port on a computer (usually a serial port).
#  (master, slave) for the pty and the tty
master, slave = pty.openpty()


 # Get the terminal device
# name associated with
# file descriptor master 
m_name = os.ttyname(master)
print(m_name)



# Get the terminal device
# name associated with
# file descriptor slave
s_name = os.ttyname(slave)
print(s_name)


ser = serial.Serial(s_name)

# To Write to the device
current_time = time.time()
print("start at= [" + str(current_time)  + "]")
ser.baudrate = 115200
for i in range(200):
    print("i= " + str(i))
    ser.write('Your text')
    time.sleep(1) 

 
print("end at = [" + str(current_time)  + "]")
# To read from the device
data = os.read(master,1000)
print(data)