#socat.py

import serial
import time

s1 = serial.Serial('/dev/pts/1')
 
start_time = time.time()
print("start at= [" + str(start_time)  + "]")
for i in range(2000):
    str_val = str(i)
    # converting string to bytes
    byte_val = str_val.encode()
    s1.write(' hello socat\r\n')
    s1.write(byte_val)

end_time = time.time() 
print("end at  = [" + str(end_time)  + "]")



print("s2 recieve")
 

s1.close()
 