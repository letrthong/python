import serial

s1 = serial.Serial('/dev/pts/0')
s2 = serial.Serial('/dev/pts/1')

s1.write('hello\r\n')

data = s2.readline()
print(data)

s1.close()
s2.close()