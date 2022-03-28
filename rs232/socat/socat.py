#socat.py

import serial

s1 = serial.Serial('/dev/pts/0')
s2 = serial.Serial('/dev/pts/1')

print("s1 sent")
s1.write('hello socat\r\n')

print("s2 recieve")
data = s2.readline()
print(data)

s1.close()
s2.close()