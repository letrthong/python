# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def fun1(str):
    str = "Pass by reference in Python"
    
def fun2(array):
    array.append(4)
    array.append(6)
    array.append(7)

#https://realpython.com/python-pass-by-reference/
str= "Pass by value in Python"
print(str)

fun1(str) 
print(str)


device_list  = []
fun2(device_list)
print(len(device_list))

item = device_list.pop(0)    
print(item)

print(len(device_list))
# https://www.geeksforgeeks.org/shallow-copy-and-deep-copy-in-c/
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
